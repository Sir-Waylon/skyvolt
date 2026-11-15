#!/usr/bin/env python3
"""shortify.py pack.json : turn multiple-choice questions whose answer is a number or a short term into typed
short-answer questions. The original choices stay on the item (q.o) as an optional, XP-halving hint. Idempotent."""
import json,re,sys
p=sys.argv[1];pack=json.load(open(p,encoding='utf8'))
PRE={'n':1e-9,'u':1e-6,'µ':1e-6,'μ':1e-6,'m':1e-3,'k':1e3,'K':1e3,'M':1e6}
SI=set('ΩVAWJCNFTs')|{'Hz'}
NUM=re.compile(r'^([−-]?\d+(?:\.\d+)?)(?:\s*/\s*(\d+))?\s*(.*)$')
BAD_STEM=re.compile(r'which of the following|which (statement|option|choice|pair|one|sentence)|all of the following|\bexcept\b|best (describes|explains|summar)|most likely|true or false|\(a\)|incorrect|not true|which is (true|false)|what is true|which.*\bbelow\b|statements?\b.*\?$',re.I)
def unit(u):
    u=u.strip().replace('ohms','Ω').replace('ohm','Ω')
    if not u:return None,1.0,''
    m=re.match(r'^([nuµμmkKM]?)(Hz|[ΩVAWJCNFTs])$',u)
    if m and (m.group(2) in SI):return u,PRE.get(m.group(1),1.0),'u'
    return u,1.0,'free'
def conv(q):
    if q.get('type')!='mcq' or 'o' not in q or len(q['o'])<2:return False
    a=q['o'][0].strip();stem=q['q']
    if BAD_STEM.search(stem):return False
    m=NUM.match(a.replace('−','-'))
    if m and not re.search(r'[a-zA-Z]{4,}',m.group(3) or '') and m.group(3) not in ('%',':1') and ':' not in a and '=' not in a and 'x' not in a.lower().replace('x10','') :
        v=float(m.group(1))
        if m.group(2):
            d=float(m.group(2))
            if d==0:return False
            v=v/d
        u,f,kind=unit(m.group(3) or '')
        if kind=='u':num=dict(v=v*f,u=u,tol=0.02)
        else:num=dict(v=v,free=True,tol=0.005 if abs(v)<1e4 else 0.01)
        if kind=='free' and u and u not in ('°','°C','°F','K','m','cm','mm','km','kg','g','mph','kt','kts','m/s','hPa','mb','ft','mi','rad','s','min','h','days','°N','°S','knots','ft/s','km/h','mm/h','in','inches','miles','m/s²','V/m','kHz','MHz','%','mm','dBZ','J/kg','kJ','Pa','kPa','mbar','m²','cm²','m³','cm³','units','square units','sq units','cm/s'):
            return False
        if '%' in a:return False
        num['show']=a
        q['num']=num;q['type']='short';return True
    if re.search(r'[=×÷→↔^]|\d{3,}',a) or len(a.split())>3 or len(a)>28 or a.lower() in ('yes','no','true','false') or re.match(r'^\d',a):return False
    if len(a.split())==3 and not a.replace(' ','').replace('-','').isalpha():return False
    rel=re.match(r'^[a-z]\s?[<>≤≥]\s?[−-]?\d+(?:/\d+)?$',a)
    if re.search(r'[<>≤≥]',a) and not rel:return False
    if not rel and not all(ch.isalnum() or ch in " .-'’/()" for ch in a):return False
    if re.search(r'counterexample',stem,re.I):return False
    alts=[a]
    base=re.sub(r'\s*\([^)]*\)','',a).strip()
    if base and base!=a:alts.append(base)
    if not rel and not re.search(r'\d',a):
        for part in re.split(r'\s+or\s+|\s*/\s*',a):
            if part.strip() and part.strip() not in alts and len(part.split())<=3:alts.append(part.strip())
    for x in list(alts):
        if not rel and not x.isupper() and len(x)>=6 and x.replace(' ','').replace('-','').isalpha():
            if x.endswith('s'):alts.append(x[:-1])
            else:alts.append(x+'s')
    seen=[];[seen.append(x) for x in alts if x not in seen]
    q['text']=seen;q['type']='short';return True
n=0
for q in pack['questions']:
    if conv(q):n+=1
json.dump(pack,open(p,'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
import collections
print('shortify',p,n,dict(collections.Counter(q['type'] for q in pack['questions'])))
