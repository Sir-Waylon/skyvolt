# -*- coding: utf-8 -*-
# 31.1: give EVERY question a hidden numeric `tier` (1-20, QUESTION_RULES.md taxonomy). Never shown to students.
# Questions written with a visible "[Subject | Subtopic | Tier n]" prefix have it moved into q['tier'] (prefix stripped).
# Older questions are tiered from level (l), difficulty (b), type, answer-step count and wording cues. Idempotent.
import json,re,sys
TAG=re.compile(r'^\[[^\]|]+\|[^\]|]+\|\s*Tier\s*(\d+)\]\s*')
BAND={1:(1,6),2:(5,13),3:(11,19)}
CUE=[ # (regex on question text, tier) - first match wins; these map the wording to a named tier of the taxonomy
 (r'^(what|which) (is|are) (the )?(term|name|symbol|unit)\b|\bstands? for\b|\bis called\b|\bdefinition of\b',2),
 (r'\bwhich (unit|units)\b|\bdimension|order of magnitude|\bin what unit\b',5),
 (r'\bcritical (angle|point|value)|\bthreshold\b|\bat the (limit|edge)\b|\bjust (barely|enough)\b',9),
 (r'\berror\b|\bmistake\b|\bwhat went wrong\b|\bwhy (does|do) the (data|measurement|result)\b',13),
 (r'\bapproaches? (zero|infinity)|\bvery (large|small)\b.*\bwhat happens\b|\bas .* (grows|increases) without',16),
 (r'\bwhich (diagram|graph|figure|picture)\b|\bmatches? (the )?(diagram|graph|figure)\b',3),
]
def tier(q):
    m=TAG.match(q.get('q',''))
    if m:return int(m.group(1)),True
    l=q.get('l',2);lo,hi=BAND.get(l,(5,13));t=q.get('type')
    s=q.get('b',0)
    sol=q.get('sol') or []
    steps=len([x for x in sol if isinstance(x,str) and not x.startswith('Notes|') and not x.startswith('From your notes')])
    n=len(q.get('q',''))
    if t=='short' and q.get('num') and steps>=3:s+=0.12
    if t in('match',):s-=0.12
    if t=='order':s+=0.05
    if t=='proof':lo,hi=13,19
    if n>200:s+=0.1
    elif n<70:s-=0.1
    s+=min(n,400)/2000.0+min(sum(len(x) for x in sol if isinstance(x,str)),900)/6000.0+0.02*len(re.findall(r'\d+(?:\.\d+)?',q.get('q','')))   # longer, number-heavy items rank harder within their level
    return ('raw',s,lo,hi),False
def finish(q,raw,pct):
    _,s,lo,hi=raw
    base=round(lo+pct*(hi-lo));low=q.get('q','').lower()
    for rx,tr in CUE:
        if re.search(rx,low):
            base=max(lo-2,min(hi+2,tr));break   # a cue pulls toward its named tier, at most 2 outside the level band
    return max(1,min(20,base))
if __name__=='__main__':
    pf=sys.argv[1];p=json.load(open(pf,encoding='utf8'));dist={};qs=p['questions'];raws={}
    for i,q in enumerate(qs):
        t,tagged=tier(q)
        if tagged:q['q']=TAG.sub('',q['q']);q['tier']=t;dist[t]=dist.get(t,0)+1
        else:raws[i]=t
    byl={}
    for i,r in raws.items():byl.setdefault((qs[i].get('l',2),qs[i].get('type')=='proof'),[]).append((r[1],i))
    for k,lst in byl.items():
        lst.sort();n=len(lst);j=0
        while j<n:
            e=j
            while e<n and lst[e][0]==lst[j][0]:e+=1
            pct=((j+e-1)/2)/max(1,n-1)     # average-rank percentile so ties share one value
            for x in range(j,e):
                i=lst[x][1];qs[i]['tier']=finish(qs[i],raws[i],pct);dist[qs[i]['tier']]=dist.get(qs[i]['tier'],0)+1
            j=e
    json.dump(p,open(pf,'w'),ensure_ascii=False,separators=(',',':'))
    print('addtier',len(qs),' '.join('%d:%d'%(k,dist[k]) for k in sorted(dist)))
