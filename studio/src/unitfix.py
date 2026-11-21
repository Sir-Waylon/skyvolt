# unitfix.py pack.json : grader expects num.v in BASE units when num.u has an SI prefix (mA, kΩ, ms, µF).
# Some questions stored v in the displayed unit. Decide from the solution's own numbers and convert.
import json,sys,re
F={'m':1e-3,'µ':1e-6,'μ':1e-6,'n':1e-9,'k':1e3,'K':1e3,'M':1e6}
U=re.compile(r'^([mµμnkKM]?)(V|A|Ω|W|J|C|F|H|Hz|s|Wh)$')
NUM=re.compile(r'-?\d[\d,]*\.?\d*(?:\s*[×x]\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹-]+)?')
SUP=str.maketrans('⁻⁰¹²³⁴⁵⁶⁷⁸⁹','-0123456789')
def nums(s):
    o=[]
    for m in NUM.finditer(str(s).replace('−','-')):
        t=m.group(0).replace(',','');e=re.search(r'10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹-]+)',t)
        try:
            b=float(re.split(r'\s*[×x]',t)[0])
            if e:b*=10**int(e.group(1).translate(SUP))
            o.append(b)
        except:pass
    return o
p=json.load(open(sys.argv[1],encoding='utf8'));n=0
for q in p['questions']:
    nm=q.get('num')
    if not nm or not nm.get('u') or not nm.get('v'):continue
    m=U.match(str(nm['u']).strip())
    if not m:continue
    f=F.get(m.group(1),1)*(3600 if m.group(2)=='Wh' else 1);v=nm['v']
    sn=nums(' '.join(map(str,q.get('sol',[])))+' '+str(q.get('w','')))
    near=lambda x:any(abs(s-x)<=abs(x)*0.03+1e-12 for s in sn)
    if near(v/f):continue                      # already base units: display value appears in the solution
    if near(v) or near(v*f):nm['v']=float('%.12g'%(v*f));n+=1
    elif v!=float('%.12g'%v):nm['v']=float('%.12g'%v)   # stored in displayed unit: convert to base
json.dump(p,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'));print('unitfix',sys.argv[1],n)
