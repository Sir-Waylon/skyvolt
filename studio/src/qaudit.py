import json,re,sys,collections
def norm(s):return re.sub(r'\s+',' ',str(s).strip().lower())
BAD=re.compile(r'TODO|undefined|NaN|\bnull\b|\?\?|\{\{|\}\}|\[object|lorem|FIXME|xxx',re.I)
def audit(slug):
    P=json.load(open(f'events/{slug}/pack.json'));Q=P['questions'];out=collections.defaultdict(list)
    seen=collections.defaultdict(list)
    for q in Q:
        i=q.get('id');t=q.get('type','mcq');txt=q.get('q','')
        def F(k,m):out[k].append((i,m))
        if not txt or len(txt)<8:F('short-q',txt)
        if BAD.search(txt):F('bad-token-q',BAD.search(txt).group())
        seen[norm(txt)+'|'+norm(q.get('o',[''])[0] if q.get('o') else q.get('num',{}).get('v',''))].append(i)
        if not q.get('sol') and not q.get('w'):F('no-solution','')
        for s in q.get('sol',[]) or []:
            if BAD.search(str(s)):F('bad-token-sol',BAD.search(str(s)).group())
        if q.get('l') not in (1,2,3):F('level','%s'%q.get('l'))
        if not q.get('t'):F('no-topic','')
        if t=='mcq' or t=='multi':
            o=q.get('o',[])
            if len(o)<3:F('few-options',len(o))
            n=[norm(x) for x in o]
            if len(set(n))<len(n):F('dup-options',o)
            if any(re.search(r'all of the above|none of the above|both a and b',x) for x in n[:]):F('aota',o)
            if t=='mcq' and len(o)>=3 and all(len(str(o[0]))>1.6*len(str(x)) for x in o[1:]):F('correct-longest',str(o[0])[:40])
            if t=='multi':
                a=q.get('a',[])
                if not a or any((not isinstance(k,int)) or k<0 or k>=len(o) for k in a):F('multi-index',a)
                if len(a)==len(o):F('multi-all',a)
        if t=='order':
            it=q.get('items',[])
            if len(it)<3 or len(set(map(norm,it)))<len(it):F('order-items',it)
        if t=='match':
            pr=q.get('pairs',[])
            if len(pr)<3 or len(set(norm(p[0]) for p in pr))<len(pr) or len(set(norm(p[1]) for p in pr))<len(pr):F('match-pairs',pr)
        n=q.get('num')
        if n:
            tol=n.get('tol')
            if tol is not None and not(0<=tol<=0.05):F('tol',tol)
            if not isinstance(n.get('v'),(int,float)):F('num-v',n.get('v'))
        if t=='short' and not n and not q.get('o'):F('short-noanswer','')
    for k,v in seen.items():
        if len(v)>1:out['duplicate'].append((v[0],v[1:]))
    return Q,out
if __name__=='__main__':
    for s in sys.argv[1:]:
        Q,o=audit(s);print('==',s,len(Q))
        for k,v in sorted(o.items()):print(' ',k,len(v),v[:3])
