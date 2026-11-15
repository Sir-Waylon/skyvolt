import json,re
x=json.load(open('ck/extracted.json'));bank=json.load(open('bank.json'));t=open('template2.html',encoding='utf8').read()
notes=[]
for m in re.finditer(r'<details id="(n\d+)"[^>]*><summary>(.*?)</summary><div class="in">(.*?)</div></details>',t,re.S):
    notes.append({'id':m.group(1),'title':re.sub(r'^\d+\.\s*','',m.group(2)),'html':m.group(3).strip()})
topics=[['hist','History','i','n2'],['static','Charge & Coulomb','ii','n3'],['dcac','DC & AC','iii','n4'],['virpe','V, I, R, P, E','iv','n5'],['circ','DC circuits','v','n6'],['ctrl','Control devices','vi','n8'],['diode','Diodes & LEDs','vii','n9'],['logic','Digital logic','viii','n10'],['kirch','Kirchhoff','ix','n7'],['hands','Hands-on & safety','','bench'],['sym','Symbolic logic','','n11']]
cnt={}
qs=[]
for q in bank:
    c=cnt.get(q['t'],0)+1;cnt[q['t']]=c
    d={'id':'%s-%03d'%(q['t'],c),'t':q['t'],'l':q['l'],'type':'multi' if q.get('m') else 'mcq','q':q['q'],'o':q['o'],'w':q['w']}
    if q.get('m'): d['a']=q['a']
    if q.get('fig'): d['fig']=q['fig']
    qs.append(d)
pack={'schema':'scioly-pack/1','meta':{'id':'circuit-lab-b-2027','title':'Circuit Lab','division':'B','year':2027,'org':'Science Olympiad',
 'facts':[['50 min','Team of 2'],['2 × Class III','Calculators'],['Any notes','Binder'],['50–75%','Written'],['25–50%','Hands-on']],
 'intro':'Rules: soinc.org. Not an official Science Olympiad document.'},
 'topics':[{'id':a,'name':b,'area':c,'note':d} for a,b,c,d in topics],
 'notes':notes,'plan':x['DAYS'],'cards':x['C'],'written':x['WD'],'bench':x['BN'],'questions':qs}
json.dump(pack,open('circuit-lab-b.pack.json','w'),ensure_ascii=False,indent=0)
print(len(notes),len(qs),cnt)
