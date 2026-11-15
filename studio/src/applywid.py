# -*- coding: utf-8 -*-
"""applywid.py pack.json wid_module : attach interactive widget specs to lesson cards by (topic, card title)"""
import json,sys,importlib,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
p=json.load(open(sys.argv[1],encoding='utf8'));W=importlib.import_module(sys.argv[2]).WID
n=0;miss=[]
for u in p['units']:
    m=W.get(u['id'],{})
    for L in u['lessons']:
        for c in L['cards']:
            if c['h'] in m:c['lab']=m[c['h']];n+=1
have={c['h'] for u in p['units'] for L in u['lessons'] for c in L['cards'] if True}
for t,d in W.items():
    for h in d:
        if not any(c['h']==h for u in p['units'] if u['id']==t for L in u['lessons'] for c in L['cards']):miss.append((t,h))
json.dump(p,open(sys.argv[1],'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
tot=sum(len(L['cards']) for u in p['units'] for L in u['lessons'])
print('widgets',n,'of',tot,'cards','MISSING' if miss else '',miss)
