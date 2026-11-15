import json,sys,glob,re
# usage: applyextra.py pack.json audit_dir_glob  -> merges fix/del/del_family/new from each audit json (idempotent)
pf=sys.argv[1];p=json.load(open(pf,encoding='utf8'));qs=p['questions'];ids={q['id'] for q in qs}
bad=[];nf=nd=nn=0
OKU=re.compile(r'^[nuµμmkKM]?(V|A|Ω|ohms?|W|J|C|F|H|Hz|s|Wh|N/C|V/m|%)$')
def norm(nm):
    if not nm or not nm.get('u') or nm.get('norm'):return
    u=str(nm['u']).strip()
    if u in('h','hr','hours'):nm['v']=nm['v']*3600;nm['norm']=1
    elif u in('min','minutes'):nm['v']=nm['v']*60;nm['norm']=1
    elif not OKU.match(u):
        nm['free']=True;nm['show']=('%.6g'%nm['v'])+' '+u
def ok(q):
    t=q.get('type')
    if not q.get('q') or not q.get('w'):return 'missing q/w'
    if t=='mcq':
        o=q.get('o')
        if not o or len(o)<3 or len(set(map(str,o)))!=len(o):return 'bad options'
    elif t=='multi':
        if not q.get('o') or not q.get('a'):return 'bad multi'
    elif t=='short':
        if not(q.get('num') and 'v' in q['num']) and not q.get('text'):return 'short without answer'
    elif t=='order':
        if not q.get('items') or len(q['items'])<3:return 'bad order'
    elif t=='match':
        if not q.get('pairs'):return 'bad match'
    else:return 'type'
    if not 1<=q.get('l',0)<=3:return 'level'
    return ''
for f in sorted(glob.glob(sys.argv[2])):
    d=json.load(open(f,encoding='utf8'));tag=re.sub(r'\.json$','',f.split('/')[-1])
    fam=set(d.get('del_family',[]));dl=set(d.get('del',[]))
    if fam or dl:
        before=len(qs);qs[:]=[q for q in qs if q['id'] not in dl and q.get('fp') not in fam and not q['id'].startswith(('x-',))];nd+=before-len(qs)
    for i,v in d.get('fix',{}).items():
        norm(v.get('num'))
        for q in qs:
            if q['id']==i:q.update(v);nf+=1;break
    have={q['id'] for q in qs}
    for k,n in enumerate(d.get('new',[])):
        n=dict(n);r=ok(n)
        if r:bad.append((tag,k,r));continue
        norm(n.get('num'))
        n['id']='%s-x%s%03d'%(n['t'],tag,k+1)
        if n['id'] in have:continue
        n.setdefault('fp',n['id']);qs.append(n);have.add(n['id']);nn+=1
p['questions']=qs
json.dump(p,open(pf,'w'),ensure_ascii=False,separators=(',',':'))
print('applyextra fixes',nf,'deleted',nd,'new',nn,'rejected',len(bad),bad[:5])
