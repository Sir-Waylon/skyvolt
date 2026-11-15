# (stem prefix, patch)  — applied after merge; keeps options as [correct, wrong...]
FIX=[
('The voltaic pile was a stack of',{'o':['Zinc and copper discs separated by wet cloth','Iron and carbon rods separated by oiled paper','Glass plates rubbed with silk cloth','Two magnets wrapped around a copper coil']}),
('Which statement about electric shock',{'o':['Current through the body does the harm','Voltage alone does the harm','Alternating current is the only danger','Anything under 100 V is harmless']}),
('Three identical bulbs are connected in parallel',{'o':['keep the same brightness','go completely dark','become noticeably dimmer','become noticeably brighter']}),
('Two identical LEDs share a single resistor',{'o':['Small differences in forward voltage make one LED hog current','The two LEDs see different supply voltages','One resistor would overheat from both currents','The LEDs would flash on and off together']}),
('A transformer needs AC',{'o':['it needs a changing field to induce voltage','DC cannot flow through wire coils','its iron core blocks any DC','AC has a higher voltage than DC']}),
('The tesla is the SI unit of',{'o':['magnetic flux density','magnetic flux','magnetic permeability','magnetic field energy']}),
('The voltage across a capacitor is doubled',{'o':['four times as large','twice as large','half as large','the same as before']}),
('A charged capacitor stores energy in',{'o':['the electric field between the plates','the chemical makeup of the plates','the magnetic field around the leads','the heat inside the dielectric']}),
('Ampere is best known for having',{'o':['studied the relationship between electricity and magnetism','formulated the junction (current) and loop (voltage) laws','experimentally demonstrated electromagnetic waves','invented the first chemical battery, the voltaic pile']}),
('The Earth’s "magnetic north"',{'o':['South pole of Earth’s field','North pole of Earth’s field','Point of zero field','Neutral point']}),
('A slow-blow fuse is used',{'o':['tolerates a short startup surge','opens at once on any surge','resets itself after an overload','trips when current leaks to ground']}),
('Outside a bar magnet, magnetic field lines run',{'o':['from the north pole to the south pole','from the south pole to the north pole','from the center outward in all directions','from north pole to north pole']}),
('An ammeter must be connected',{'o':['in series with the load','in parallel with the load','to the ground','across the battery terminals']}),
('Conventional current flows from the',{'o':['Positive terminal toward the negative terminal','Ground toward the battery','Negative terminal toward the positive','Either way, depending on the load']}),
('If you break a bar magnet in half',{'o':['Two magnets, each with a north and a south pole','One north-pole piece and one south-pole piece','Two non-magnetic pieces','One magnet and one iron bar']}),
('Outside a magnet, field lines are drawn from',{'o':['North pole to south pole','Toward the nearest iron','Center to ends','South pole to north pole']}),
('The unit of electrical potential is named',{'q':'What is the SI unit of electric potential difference (voltage)?'}),
]
def apply(P):
    n=0
    for q in P['questions']:
        for pre,patch in FIX:
            if q['q'].startswith(pre):q.update(patch);n+=1
    return n
