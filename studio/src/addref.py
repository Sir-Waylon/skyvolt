"""Adds a final explanation step quoting the best-matching sentence from the pack's own notes ('From your notes · Title: ...')."""
import json,re,sys,math,html
STOP=set('the a an of to in on is are and or for with by at as it its that this be from into than then when which what how not no yes can has have will more most also each any all one two per use used using your you they them their there these those such only over under between about out up down if so do does'.split())
def toks(s):return [w for w in re.findall(r"[a-z0-9]+(?:\.[0-9]+)?",s.lower()) if w not in STOP and len(w)>2]
def sents(h):
    t=re.sub(r'</(li|p|tr|h\d|div)>|<br\s*/?>',' \n ',h);t=html.unescape(re.sub(r'<[^>]+>','',t));out=[]
    for line in t.split('\n'):
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])',line.strip()):
            s=re.sub(r'\s+',' ',s).strip()
            if 25<=len(s)<=320:out.append(s)
    return out
CM={'hist':'n2','static':'n3','dcac':'n4','virpe':'n5','circ':'n6','kirch':'n7','ctrl':'n8','diode':'n9','logic':'n10','sym':'n11','mag':'n12','cap':'n13','hands':'n6'}
def run(path):
    p=json.load(open(path,encoding='utf8'));S=[]
    for n in p['notes']:
        for s in sents(n['html']):S.append((n['title'],s,set(toks(s))))
    df={}
    for _,_,t in S:
        for w in t:df[w]=df.get(w,0)+1
    idf=lambda w:math.log(1+len(S)/(1+df.get(w,0)))
    c=0
    for q in p['questions']:
        sol=q.get('sol')
        if sol:
            while sol and (sol[-1].startswith('From your notes') or sol[-1].startswith('Notes|')):sol.pop()
        a=q['o'][0] if q['type']=='mcq' else str(q.get('a',q.get('ans','')))
        if isinstance(q.get('num'),dict):a+=' '+str(q['num'].get('v',''))
        qa=set(toks(a));qq=set(toks(q['q']+' '+q.get('w','')))
        best=None;bs=0
        for ti,s,t in S:
            ov=(qa&t);ov2=(qq&t)
            if not ov and not (len(qa)==0 and len(ov2)>=3):continue
            sc=sum(idf(w) for w in ov)*2+sum(idf(w) for w in ov2)
            if len(ov|ov2)<4 or len(ov2)<2:continue
            if sc>bs:bs=sc;best=(ti,s)
        if best and bs>=15:
            sol=q.setdefault('sol',[q['w']] if q.get('w') else [])
            sol.append('From your notes · '+best[0]+': '+best[1]);c+=1
        ids={n['id']:n['title'] for n in p['notes']};nid=CM.get(q['t']) if CM.get(q['t']) in ids else ('n-'+q['t'] if 'n-'+q['t'] in ids else None)
        if nid and len(p['notes'])>2:q.setdefault('sol',[q['w']] if q.get('w') else []).append('Notes|'+nid+'|'+ids[nid])
    json.dump(p,open(path,'w'),ensure_ascii=False,separators=(',',':'));return c,len(p['questions'])
for f in sys.argv[1:]:print(f,run(f))
