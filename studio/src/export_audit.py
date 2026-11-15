import json,re,sys,collections,os
def strip(h):return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)).strip()
def ans(q):
    if q['type']=='mcq':return q['o'][0]
    if q['type']=='multi':return '; '.join(q['o'][i] for i in q['a'])
    if q['type']=='short':
        if q.get('num'):n=q['num'];return '%s (tol %s%s)'%(n.get('v'),n.get('tol'),(' '+n['u']) if n.get('u') else '')
        return ' | '.join(q.get('text',[]))
    if q['type']=='order':return ' > '.join(q['items'])
    if q['type']=='match':return '; '.join('%s=%s'%tuple(p) for p in q['pairs'])
    return str(q.get('a') or q.get('text') or '')
def export(ev,short,outdir):
    p=json.load(open(f'events/{ev}/pack.json'));Q=p['questions'];notes={n['id']:n for n in p['notes']}
    by=collections.defaultdict(list)
    for q in Q:by[q['t']].append(q)
    for t in p['topics']:
        tid=t['id'];qs=by.get(tid,[]);fam=collections.defaultdict(list)
        for q in qs:fam[q.get('fp') or q['id']].append(q)
        L=['# %s / %s: %s  (%d questions, %d families)'%(ev,tid,t['name'],len(qs),len(fam))]
        n=notes.get(t.get('note'))
        if n:L.append('## STUDY NOTE (what students are taught)\n'+strip(n['html'])[:3500])
        L.append('## QUESTIONS  format: id | level(1 easy,2 core,3 hard) | type | question || correct answer || wrong options || why')
        for fp,g in fam.items():
            ex=g if len(g)<=3 else g[:3]
            if len(g)>3:L.append('### FAMILY %s: %d generated variants of one template (3 shown; numbers vary)'%(fp[:60],len(g)))
            for q in ex:
                wr=[x for i,x in enumerate(q.get('o',[])) if not (q['type']=='mcq' and i==0) and not (q['type']=='multi' and i in q.get('a',[]))] if q['type'] in('mcq','multi') else (q.get('o',[])[1:] if q.get('o') else [])
                L.append('%s | %s | %s | %s || %s || %s || %s'%(q['id'],q['l'],q['type'],q['q'],ans(q),' ; '.join(map(str,wr)),(q.get('w') or '')[:200]))
        open(f'{outdir}/{short}_{tid}.txt','w',encoding='utf8').write('\n'.join(L))
        print(short,tid,len(qs),len(fam),sum(len(x) for x in L))
if __name__=='__main__':
    export('circuit-lab-b','circuit','../audit/in');export('meteorology-b','met','../audit/in')
