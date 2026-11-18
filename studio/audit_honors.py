import json,collections,re,sys
p=json.load(open('events/apex-merged/pack.json'))
H=['fn','qd2','pl','ra','ex','lg','sq','tc','tg','ti','iv','id','tl','cn','pp']
Q=[q for q in p['questions'] if q['t'] in H]
print(len(Q),'honors-range questions')
for t in H:
    c=collections.Counter(q['l'] for q in Q if q['t']==t);ty=collections.Counter(q['type'] for q in Q if q['t']==t)
    print(t.ljust(3),'L',dict(sorted(c.items())),dict(ty))
iss=collections.defaultdict(list);seen={}
for q in Q:
    s=q.get('sol') or []
    if not s:iss['nosol'].append(q['id'])
    elif sum(len(x) for x in s)<50:iss['thinsol'].append(q['id'])
    o=q.get('o')
    if o and len(set(map(str,o)))<len(o):iss['dupopt'].append(q['id'])
    k=q['q'].strip().lower()
    if k in seen:iss['dupstem'].append((q['id'],seen[k]))
    seen[k]=q['id']
    if q['type']=='short' and 'num' not in q and 'pt' not in q:iss['noanswerkey'].append(q['id'])
    if 'num' in q and q['num'].get('free') and not q['num'].get('show'):iss['freenoshow'].append(q['id'])
    if q['type']=='mcq' and o and len(o)<3:iss['fewopts'].append(q['id'])
    if q['t'] in('tc','tg','ti','iv','id','tl') and q['l']==3 and q['type']=='mcq' and o and max(len(str(x)) for x in o)<4:iss['trivial3'].append(q['id'])
for k,v in iss.items():print(k,len(v),v[:6])
