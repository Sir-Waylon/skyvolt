import json,collections,sys
LB={1:-1,2:0,3:1.1}
def tier(q):
    b=q.get('b',LB[q['l']])
    return 0 if b<-0.75 else 1 if b<-0.1 else 2 if b<0.8 else 3
def table(f):
    p=json.load(open(f'events/{f}/pack.json'));T=collections.defaultdict(lambda:[0,0,0,0]);nb=0
    for q in p['questions']:
        T[q['t']][tier(q)]+=1;nb+= 'b' in q
    return p,T,nb
if __name__=='__main__':
    for f in ['circuit-lab-b','meteorology-b','geometry-readiness']:
        p,T,nb=table(f);print(f,len(p['questions']),'with b:',nb)
        for t,v in T.items():print('  %-8s F%-4d B%-4d C%-4d M%-4d'%(t,*v),'  need',[max(0,n-x) for n,x in zip((12,12,20,12),v)])
