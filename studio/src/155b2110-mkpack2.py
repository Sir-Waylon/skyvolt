import json,difflib,re,importlib
import bank4
P=json.load(open('circuit-lab-b.pack.json'))
if P.get('_v')==2: raise SystemExit('already merged')
new=bank4.N
# topics
for t in P['topics']: t['tier']='core'
P['topics']+= [{'id':'mag','name':'Magnetism & induction','area':'adj','note':'n12','tier':'adjacent'},{'id':'cap','name':'Capacitance','area':'adj','note':'n13','tier':'adjacent'}]
# notes
N={n['id']:n for n in P['notes']}
N['n2']['html']=N['n2']['html'].replace('</table></div>','<tr><td>Ørsted</td><td>1820</td><td>Current deflects a compass: first link of electricity and magnetism</td></tr><tr><td>Faraday</td><td>1831</td><td>Electromagnetic induction; the farad</td></tr><tr><td>Tesla</td><td>1880s</td><td>AC induction motor, polyphase AC; the tesla (flux density)</td></tr></table></div>',1)
N['n4']['html']+='<h3>Household AC (2026 list)</h3><ul><li>US outlet: <b>hot</b> (black, ≈120 V RMS to ground), <b>neutral</b> (white, return path, ≈0 V), <b>ground</b> (green or bare, fault path only).</li><li><b>RMS</b> is the DC-equivalent heating value: V<sub>rms</sub> = V<sub>peak</sub>/√2, so 120 V RMS ≈ 170 V peak.</li><li>Breaker panel: 15 A and 20 A branch circuits; GFCI at wet locations. Power in a line is P = VI, so I = P/V.</li></ul>'
P['notes']+=[
{'id':'n12','title':'Magnetism and induction (adjacent)','html':'<p><b>Listed on the 2026 Division B page; absent from the 2027 text you were given. Learn the basics in case they return.</b></p><ul><li><b>Poles:</b> like repel, unlike attract. Field lines leave N, enter S, never cross; closer lines = stronger field. Earth’s geographic north is a magnetic <i>south</i> pole. Iron, nickel and cobalt are attracted; copper, aluminum and gold are not.</li><li><b>Ørsted:</b> current makes a magnetic field. <b>Straight wire (right-hand rule):</b> thumb along conventional current, fingers curl the way the field circles. <b>Coil:</b> fingers curl with the current, thumb points to the N pole.</li><li><b>Electromagnet strength:</b> more turns, more current, soft iron core. It switches off with the current.</li><li><b>Motor:</b> electrical → mechanical (force on a current in a field, F = BIL; the commutator reverses current each half turn). <b>Generator:</b> mechanical → electrical.</li><li><b>Induction (Faraday):</b> a changing flux through a coil induces a voltage. Faster motion, stronger magnet and more turns give more voltage. Lenz: the induced current opposes the change.</li><li><b>Transformer (AC only):</b> V<sub>s</sub>/V<sub>p</sub> = N<sub>s</sub>/N<sub>p</sub>. Ideal: P<sub>in</sub> = P<sub>out</sub>, so stepping voltage down steps current up by the same ratio.</li><li><b>Units:</b> tesla (T) for flux density, N/(A·m).</li></ul><div class="card"><b>Electromagnet station.</b> Wrap many turns of insulated wire around an iron bolt, connect a battery, test with paper clips. More turns or a second cell picks up more. Keep it brief: the wire and battery heat up.</div>'},
{'id':'n13','title':'Capacitance (adjacent)','html':'<ul><li>Two conductors separated by an insulator. <span class="f">C = Q/V</span> (farad; usually µF). Energy <span class="f">E = ½CV²</span> (doubling V gives 4× the energy).</li><li>Parallel plates: C grows with plate area and with a dielectric, shrinks as the gap grows.</li><li><b>Parallel:</b> C adds. <b>Series:</b> 1/C = 1/C₁ + 1/C₂ (opposite of resistors).</li><li>Once charged in DC, it acts like an open circuit. Electrolytic capacitors are polarized: wrong polarity can fail.</li></ul><div class="card"><b>Example.</b> 100 µF at 12 V: Q = 1.2 mC; E = 7.2 mJ.</div>'}]
# bench
P['bench'].append(['Electromagnet (2026 list)','Wind insulated wire around an iron bolt (20+ turns), connect one battery, count paper clips lifted. Double the turns, compare. Disconnect between trials.'])
# merge questions
cnt={}
for q in P['questions']:
    k=q['t'];cnt[k]=max(cnt.get(k,0),int(q['id'].split('-')[1]))
for q in new:
    cnt[q['t']]=cnt.get(q['t'],0)+1
    d={'id':'%s-%03d'%(q['t'],cnt[q['t']])};d.update(q);P['questions'].append(d)
P['meta']['intro']='Core = 2027 text. Adjacent = listed in other years or by other states; learn after core.'
P['_v']=2
# checks
Q=P['questions'];stems=[q['q'] for q in Q]
assert len(set(stems))==len(stems),'dup stem'
for i,a in enumerate(stems):
    for b in stems[i+1:]:
        if difflib.SequenceMatcher(None,a,b).ratio()>0.9: print('SIMILAR',a,'|',b)
for q in Q:
    if q['type'] in('mcq','multi'):
        assert len(set(q['o']))==4,q['q']
        a=q['o'][0]
        if re.search(r'\b(always|never|only|cannot|all)\b',' '.join(q['o'][1:]),re.I): print('ABS',q['id'],q['o'])
    if q['type']=='short' and 'text' in q:
        for acc in q['text']:
            pass
from collections import Counter
print(len(Q),Counter(q['type'] for q in Q))
mc=[q for q in Q if q['type']=='mcq' and q['id'] in {x['id'] for x in Q[212:]}]
print('new mcq correct strictly longest:',sum(1 for q in mc if len(q['o'][0])>max(len(o) for o in q['o'][1:])),'of',len(mc))
json.dump(P,open('circuit-lab-b.pack.json','w'),ensure_ascii=False,indent=0)
