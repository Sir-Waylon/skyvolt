import json,re,collections,difflib,sys
BASE='events/circuit-lab-b/pack_v2_base.json';OUT='events/circuit-lab-b/pack.json'
P=json.load(open(BASE,encoding='utf8'));H=json.load(open('src/harvest.json',encoding='utf8'))
PRE={'n':1e-9,'µ':1e-6,'m':1e-3,'k':1e3,'M':1e6}
UNIT=re.compile(r'^(-?\d[\d,]*\.?\d*(?:e-?\d+)?|-?\.\d+)\s*(kΩ|MΩ|Ω|ohms?|mA|µA|A|mV|kV|V|mW|kW|W|kWh|Wh|mJ|kJ|J|mC|µC|nC|C|N/C|N|kHz|Hz|ms|µs|s|h|min|%|µF|mF|F|T)?$')
def fac(u):
    if not u:return 1
    if u in('%','N/C'):return 1
    if u=='Wh':return 3600
    if u=='kWh':return 3.6e6
    if u=='h':return 3600
    if u=='min':return 60
    if u in('Hz','N','T','F','J','C','A','V','W','s','Ω'):return 1
    if u.startswith('ohm'):return 1
    return PRE[u[0]]
SUP=str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻','0123456789-')
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
def topic(f,r):
    c=r['cat'];q=r['q'].lower()
    if f.startswith('a60274'):
        if c=='chg':return 'dcac' if re.search(r'\b(ac|dc|mains|outlet|transformer)\b',q) else 'static'
        if c=='dev':return 'ctrl' if re.search(r'fuse|relay|gfci|breaker|switch|ground fault',q) else 'diode'
        return {'hist':'hist','ohm':'virpe','ckt':'circ','log':'logic','sym':'sym'}[c]
    if f.startswith('975f'):
        if c=='s0':return 'static' if re.search(r'charge|coulomb|force|static|field',q) else 'hist'
        return {'s1':'virpe','s2':'circ','s3':'circ','s4':'ctrl','s5':'diode','s6':'logic'}[c]
    return {'s0':'hist','s1':'static','s2':'virpe','s3':'circ','s4':'circ','s5':'circ','s6':'virpe','s7':'mag','s8':'sym'}[c]
def fp(q):return re.sub(r'\b[A-Z]\b','X',re.sub(r'\d+(\.\d+)?','#',q))[:80]
stats=collections.Counter()
exist=[q['q'] for q in P['questions']];exn={norm(s) for s in exist}
cnt=collections.Counter();[cnt.update({q['t']:1}) for q in P['questions']]
byfp=collections.Counter();fam_c=collections.Counter();new=[];seenstem=set()
for f,rows in H.items():
    for r in rows:
        o=[str(x) for x in r['o']];a=r['a']
        if not(0<=a<len(o)):stats['badidx']+=1;continue
        cor=o[a];wr=[x for i,x in enumerate(o) if i!=a]
        if any(x!=x.strip() or not x.strip() for x in o):stats['pad']+=1;continue
        if len({x.lower().replace(' ','') for x in o})<len(o):stats['dupopt']+=1;continue
        if any(re.search(r'all of the above|none of the above|both',x,re.I) for x in o):stats['allabove']+=1;continue
        nq=norm(r['q'])
        if nq in exn or nq in seenstem:stats['dupstem']+=1;continue
        t=topic(f,r)
        if len(norm(cor))>=3 and norm(cor) in nq:stats['ansinstem']+=1;continue
        L=sorted(len(x) for x in o)
        if len(cor)>=len(max(wr,key=len))*1.4 and len(cor)>22:stats['longcue']+=1;continue
        k=fp(r['q'])
        capn=8 if t=='sym' else int(sys.argv[1])
        fam=' '.join(re.sub(r'[\d.]+','#',r['q']).split()[:4])
        if byfp[k]>=capn or fam_c[fam]>=30:stats['cap']+=1;continue
        c2=cor.replace('−','-').replace('$','')
        c2=re.sub(r'^(-?\d+\.?\d*)\s*×\s*10([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)',lambda mm:'%se%s'%(mm.group(1),mm.group(2).translate(SUP)),c2)
        m=UNIT.match(c2)
        d={'t':t,'q':r['q'],'w':(r['t'] or r['h'] or '').strip()}
        if m and len(wr)>=2:
            try:v=float(m.group(1).replace(',',''))*fac(m.group(2))
            except Exception:stats['badnum']+=1;continue
            d['type']='short';d['num']={'v':v,'tol':0.02}
            if m.group(2):d['num']['u']='Ω' if m.group(2).startswith('ohm') else m.group(2)
            d['l']=2;stats['num->short']+=1
        else:
            d['type']='mcq';d['o']=[cor]+wr;
            nd=len(re.findall(r'\d+',r['q']));d['l']=1 if (len(r['q'])<95 and nd==0) else (3 if (nd>=4 or len(r['q'])>170) else 2)
            stats['mcq']+=1
        d['fp']=k;byfp[k]+=1;fam_c[fam]+=1;seenstem.add(nq);new.append(d)
for d in new:
    cnt[d['t']]+=1;d['id']='%s-%03d'%(d['t'],cnt[d['t']]);P['questions'].append(d)
for q in P['questions']:
    q.setdefault('fp',fp(q['q']))
import gen_extra
for d in gen_extra.OUT:
    cnt[d['t']]+=1;d['id']='%s-%03d'%(d['t'],cnt[d['t']]);P['questions'].append(d)
import fixes;print('fixes',fixes.apply(P))
P['_v']=3
json.dump(P,open(OUT,'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
print(dict(stats));print('total',len(P['questions']),collections.Counter(q['type'] for q in P['questions']));print(collections.Counter(q['t'] for q in P['questions']))
