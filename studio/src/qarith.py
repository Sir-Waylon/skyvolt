import json,re,sys,math,collections
EQ=re.compile(r'(?<![\w)\].×÷·*/+\-−^=≈(]\s)(?<![\w)\].×÷·*/+\-−^=≈(])((?:[\d.,]+|[()π√]|\s|[×÷·*/+\-−^]|sin|cos|tan|ln|log)+?)\s*[=≈]\s*(-?−?[\d.,]+(?:\s*[×x]\s*10\^?[−-]?\d+)?)(?!\s*[×÷/·*+\-−^(\w.]|\d)')
def ev(e):
    e=e.replace('−','-').replace('×','*').replace('·','*').replace('÷','/').replace('^','**').replace('π','math.pi').replace(',','')
    e=re.sub(r'√\s*\(','math.sqrt(',e);e=re.sub(r'√\s*([\d.]+)',r'math.sqrt(\1)',e)
    e=re.sub(r'(\d)\s*\(',r'\1*(',e);e=re.sub(r'\)\s*(\d|\()',r')*\1',e)
    if not re.fullmatch(r'[\d\s.+\-*/()a-z_]*',e):return None
    if not re.search(r'[+\-*/]',e) and 'sqrt' not in e:return None
    try:return eval(e,{'math':math,'__builtins__':{}})
    except Exception:return None
def val(s):
    s=s.replace('−','-').replace(',','').replace(' ','')
    m=re.fullmatch(r'(-?[\d.]+)[×x]10\^?(-?\d+)',s)
    try:return float(m.group(1))*10**int(m.group(2)) if m else float(s)
    except:return None
bad=collections.defaultdict(list);n=0;chk=0
for slug in sys.argv[1:]:
    P=json.load(open(f'events/{slug}/pack.json'))
    for q in P['questions']:
        n+=1
        for line in list(q.get('sol',[]))+([q['w']] if isinstance(q.get('w'),str) else []):
            line=str(line)
            for m in EQ.finditer(line):
                a=ev(m.group(1).strip());b=val(m.group(2))
                if a is None or b is None:continue
                chk+=1
                tol=0.02*max(abs(b),abs(a))+0.006
                # allow rounding to sig figs of stated value
                if abs(a-b)>tol and abs(a-b)>0.06*max(abs(b),1e-9):bad[slug].append((q['id'],m.group(0).strip()[:70],round(a,4)))
print('questions',n,'equations checked',chk)
for s,v in bad.items():
    print(s,len(v))
    for x in v[:25]:print('  ',x)
