# -*- coding: utf-8 -*-
from wid_h import *
W={}
W['static']={
"Coulomb's Law":calc('Move the charges. How does the force change?',[P('q1','Charge 1',1,10,1,3,' µC'),P('q2','Charge 2',1,10,1,3,' µC'),P('d','Distance',1,10,1,3,' m')],[O('Force','9000*q1*q2/d^2',900,' mN',1)],eq='F = k q₁ q₂ ÷ d²',note='F = 9×10⁹ × {q1}µC × {q2}µC ÷ {d}² = <b>{=9000*q1*q2/d^2|1}</b> mN.',pre=('Double the distance between two charges. The force becomes…',['1/2','1/4','2×'],1,'Force depends on 1/d². Twice as far = 1/4 the force.')),
'Distance is squared':calc('Watch the force fall off.',[P('d','Distance',1,10,1,1,' m')],[O('Relative force','1/d^2',1,'',3)],note='<b>{=1/d^2|3}</b> of the force at 1 m.'),
}
W['virpe']={
"Ohm's Law":calc('Change V and R. Watch I change.',[P('v','Voltage V',1,24,1,12,' V'),P('r','Resistance R',1,24,1,6,' Ω')],[O('Current I','v/r',24,' A',2)],eq='I = V ÷ R',note='{v} ÷ {r} = <b>{=v/r|2}</b> A.',take='I = V ÷ R.'),
'Power formulas':calc('Three ways to find power.',[P('v','V',1,24,1,12,' V'),P('i','I',.5,5,.5,2,' A')],[O('P = V·I','v*i',120,' W',1),O('P = I²·R','i^2*(v/i)',120,' W',1)],note='Both give <b>{=v*i|1}</b> W. R = V/I = {=v/i|1} Ω.'),
}
W['circ']={
'Series':calc('In series, resistors add and the same current goes through all.',[P('r1','R1',1,20,1,10,' Ω'),P('r2','R2',1,20,1,10,' Ω')],[O('Total R','r1+r2',40,' Ω',1),O('Current from 12 V','12/(r1+r2)',12,' A',2)],note='R = {r1} + {r2} = <b>{=r1+r2|1}</b> Ω. I = 12 ÷ {=r1+r2|1} = <b>{=12/(r1+r2)|2}</b> A.'),
'Parallel':calc('In parallel, current has more paths, so total resistance drops.',[P('r1','R1',1,20,1,10,' Ω'),P('r2','R2',1,20,1,10,' Ω')],[O('Total R','1/(1/r1+1/r2)',20,' Ω',2)],eq='1/R = 1/R₁ + 1/R₂',note='Total = <b>{=1/(1/r1+1/r2)|2}</b> Ω, smaller than either branch.',pre=('Two 10 Ω resistors in parallel make a total of…',['20 Ω','10 Ω','5 Ω'],2,'Two equal paths halve the resistance: 5 Ω.')),
'Voltage divider':calc('Two resistors share the battery.',[P('r1','R1',1,20,1,10,' kΩ'),P('r2','R2',1,20,1,10,' kΩ')],[O('V across R2 (9 V in)','9*r2/(r1+r2)',9,' V',2)],note='<b>{=9*r2/(r1+r2)|2}</b> V.'),
}
W['kirch']={'KVL: loop rule':calc('Voltage rises equal voltage drops around a loop.',[P('v','Battery',3,24,1,12,' V'),P('v1','Drop across R1',0,12,1,5,' V')],[O('Left for R2','v-v1',24,' V',1)],note='{v} − {v1} = <b>{=v-v1|1}</b> V across R2.')}
W['logic']={'AND, OR, NOT':simple('gate','Flip A and B. Learn when the lamp lights.',g='AND'),'NAND, NOR':simple('gate','NAND is AND turned upside down.',g='NAND'),'XOR, XNOR':simple('gate','XOR is on when the inputs differ.',g='XOR'),'Binary counting':simple('bits','Flip switches to count.',n=5)}
W['diode']={'LED resistor':calc('An LED needs a resistor so it does not burn out.',[P('v','Supply',3,12,1,9,' V'),P('i','LED current',5,30,5,20,' mA')],[O('Resistor','(v-2)/(i/1000)',1000,' Ω',0)],eq='R = (supply − 2 V) ÷ current',note='<b>{=(v-2)/(i/1000)|0}</b> Ω.')}
W['cap']={'Energy':calc('A capacitor stores energy in an electric field.',[P('c','Capacitance',1,100,1,10,' µF'),P('v','Voltage',1,20,1,9,' V')],[O('Energy','0.5*c*v^2',20000,' µJ',0)],eq='E = ½ C V²',note='<b>{=0.5*c*v^2|0}</b> µJ.')}
W['dcac']={'Frequency and period':wave('AC swings; frequency counts swings per second.',[P('A','Amplitude',1,10,1,5),P('f','Cycles shown',1,6,1,3)],'{f} cycles shown.'),'RMS voltage':calc('Wall power is 120 V rms.',[P('v','Peak',1,170,1,170,' V')],[O('RMS','v/1.414',130,' V',1)],note='<b>{=v/1.414|1}</b> V')}
WID=W
