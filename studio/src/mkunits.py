# -*- coding: utf-8 -*-
"""mkunits.py: attach units/lessons (study cards each followed by a related try-it question) to a pack.
usage: python3 src/mkunits.py pack.json"""
import json,re,sys,collections
STOP=set('the a an of to in is are and or for on with as at by from that this which what when be it its not than into does do you your can will'.split())
def W(s):return {w for w in re.findall(r"[a-z0-9µΩ°]+",s.lower()) if w not in STOP and len(w)>2}
def build(p,per=3):
    Q=p['questions'];st=p['study'];used=set();units=[]
    byt=collections.defaultdict(list)
    for q in Q:byt[q['t']].append(q)
    for t in p['topics']:
        cards=st['cards'].get(t['id'],[])
        if not cards:continue
        cands=[q for q in byt[t['id']] if q['type'] in('mcq','short') and q['l']<=2]
        lessons=[];cur=[]
        for c in cards:
            cw=W(c[0]+' '+c[1]+' '+(c[2] if len(c)>2 else ''));best=None;bs=0
            for q in cands:
                if q['id'] in used:continue
                qw=W(q['q']+' '+q.get('w',''));s=len(cw&qw)*2+(1 if q['l']==1 else 0)
                if q['type']=='short' and len(c)>2:s+=1
                if s>bs:bs=s;best=q
            card={'h':c[0],'t':c[1]}
            if len(c)>2:card['f']=c[2]
            if best and bs>=5:card['q']=best['id'];used.add(best['id'])
            cur.append(card)
            if len(cur)==per:lessons.append(cur);cur=[]
        if cur:
            if lessons and len(cur)==1:lessons[-1]+=cur
            else:lessons.append(cur)
        ls=[{'id':f"{t['id']}-L{i+1}",'title':(' · '.join(c['h'] for c in L[:2])),'cards':L} for i,L in enumerate(lessons)]
        units.append({'id':t['id'],'title':t['name'],'lessons':ls})
    p['units']=units;return p
if __name__=='__main__':
    p=json.load(open(sys.argv[1],encoding='utf8'));build(p)
    json.dump(p,open(sys.argv[1],'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
    n=sum(len(L['cards']) for u in p['units'] for L in u['lessons']);m=sum(1 for u in p['units'] for L in u['lessons'] for c in L['cards'] if 'q' in c)
    print(len(p['units']),'units',sum(len(u['lessons']) for u in p['units']),'lessons',n,'cards',m,'with try-it')
