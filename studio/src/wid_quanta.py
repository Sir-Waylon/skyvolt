# -*- coding: utf-8 -*-
from wid_h import *
W={}
W['kin']={
'Speed':calc('Speed is how far you go each second.',[P('d','Distance',0,100,5,40,' m'),P('t','Time',1,20,1,8,' s')],[O('Speed','d/t',20,' m/s',2)],eq='speed = distance ÷ time',note='{d} m in {t} s is <b>{=d/t|2}</b> m/s.',pre=('You run 100 m in 10 s. How fast is that?',['5 m/s','10 m/s','100 m/s'],1,'100 ÷ 10 = 10 m/s.'),take='speed = distance ÷ time'),
'Acceleration':plot('Acceleration is how fast the speed changes. Steeper line = bigger acceleration.',['v0+a*x'],[P('v0','Start speed',0,10,1,0,' m/s'),P('a','Acceleration',-2,4,.5,2,' m/s²')],x=(0,10),y=(-10,50),out='Speed after t seconds = {v0} + {a}·t. After 10 s: <b>{=v0+a*10|1}</b> m/s.',xl='time (s)',yl='speed'),
'Falling objects':plot('Without air, everything falls with the same acceleration (10 m/s²).',['5*x^2'],[],x=(0,4),y=(0,80),out='Distance fallen = ½·g·t² = 5t². After 3 s: <b>45 m</b>.',xl='time (s)',yl='distance (m)',pre=('Without air, which hits the ground first: a heavy ball or a light ball?',['Heavy','Light','Same time'],2,'Gravity pulls harder on the heavy one, but it is also harder to speed up. The two effects cancel.')),
'Reading motion graphs':plot('On a position-time graph, the slope is the speed.',['v*x'],[P('v','Speed',-3,5,1,2,' m/s')],x=(0,10),y=(-30,50),out='Slope = <b>{v}</b> m/s. A steeper line is faster. A flat line is standing still.',xl='time (s)',yl='position (m)'),
}
W['ohm']={
'Charge, current and voltage':calc('Voltage pushes. Current flows.',[P('v','Voltage',1,12,1,6,' V'),P('r','Resistance',1,12,1,6,' Ω')],[O('Current','v/r',3,' A',2)],note='A {v} V battery pushes <b>{=v/r|2}</b> A through {r} Ω.'),
"Ohm's law":simple('formula','',),
'Resistance':calc('Resistance is how hard the path is for current.',[P('r','Resistance',1,20,1,5,' Ω')],[O('Current from 10 V','10/r',10,' A',2)],note='Bigger resistance, less current: 10 V ÷ {r} Ω = <b>{=10/r|2}</b> A.',pre=('If you double the resistance and keep the same battery, the current…',['doubles','halves','stays'],1,'I = V ÷ R. A bigger R makes a smaller I.')),
'Electric power':calc('Power is energy per second: P = V × I.',[P('v','Voltage',1,24,1,12,' V'),P('i','Current',0,5,.5,2,' A')],[O('Power','v*i',120,' W',1)],eq='P = V × I',note='{v} V × {i} A = <b>{=v*i|1}</b> W.'),
}
W['ohm']["Ohm's law"]=calc('Change V and R. Watch I change.',[P('v','Voltage V',1,24,1,12,' V'),P('r','Resistance R',1,24,1,6,' Ω')],[O('Current I','v/r',24,' A',2)],eq='I = V ÷ R',note='{v} ÷ {r} = <b>{=v/r|2}</b> A.',take='I = V ÷ R. More voltage means more current; more resistance means less.')
W['frc']={
"Newton's second law":calc('Same push, different masses. Who speeds up more?',[P('f','Force',1,50,1,20,' N'),P('m','Mass',1,20,1,5,' kg')],[O('Acceleration','f/m',30,' m/s²',2)],eq='a = F ÷ m',note='{f} N on {m} kg gives <b>{=f/m|2}</b> m/s².',pre=('Push twice as hard on the same cart. The acceleration…',['doubles','halves','stays'],0,'a = F ÷ m. Doubling F doubles a.'),take='F = m × a.'),
'Weight and mass':calc('Mass stays the same everywhere. Weight depends on gravity.',[P('m','Mass',1,100,1,50,' kg'),P('g','Gravity',1,25,1,10,' N/kg')],[O('Weight','m*g',2500,' N',0)],eq='W = m × g',note='{m} kg with g = {g} weighs <b>{=m*g|0}</b> N. (Earth about 10, Moon about 1.6.)'),
'Inclined planes':calc('On a slope, only part of gravity pulls you along it.',[P('a','Slope angle',0,80,5,30,'°')],[O('a along slope','10*sind(a)',10,' m/s²',2)],eq='a = g sin θ',note='At {a}°, a sliding box speeds up at <b>{=10*sind(a)|2}</b> m/s². Flat (0°): no sliding. Vertical (90°): free fall.'),
'Friction':calc('Friction fights sliding: f = μN.',[P('mu','Roughness μ',0,1,.1,.4,''),P('n','Push into surface N',10,200,10,100,' N')],[O('Friction','mu*n',200,' N',0)],note='Max friction = {mu} × {n} = <b>{=mu*n|0}</b> N.'),
}
W['nrg']={
'Kinetic energy':calc('Kinetic energy grows with the square of speed.',[P('m','Mass',1,10,1,2,' kg'),P('v','Speed',0,20,1,5,' m/s')],[O('Kinetic energy','0.5*m*v^2',1000,' J',0)],eq='KE = ½ m v²',note='<b>{=0.5*m*v^2|0}</b> J. Double the speed and the energy is 4 times bigger.',pre=('If you double your speed, kinetic energy becomes…',['2×','4×','8×'],1,'v is squared: 2² = 4.')),
'Potential energy':calc('Lift something higher and it stores more energy.',[P('m','Mass',1,20,1,5,' kg'),P('h','Height',0,20,1,10,' m')],[O('Potential energy','m*10*h',4000,' J',0)],eq='PE = m g h (g = 10)',note='{m} kg at {h} m stores <b>{=m*10*h|0}</b> J.'),
'Conservation of energy':calc('Drop a ball: potential energy turns into kinetic. The total stays the same.',[P('h','Height fallen',0,10,1,5,' m')],[O('Potential left','10*(10-h)',100,' J',0,'var(--gold)'),O('Kinetic gained','10*h',100,' J',0)],note='A 1 kg ball starts 10 m up. After falling {h} m: PE = <b>{=10*(10-h)|0}</b> J, KE = <b>{=10*h|0}</b> J. Total always 100 J.'),
'Power':calc('Same work, less time = more power.',[P('w','Work done',100,1000,100,500,' J'),P('t','Time',1,20,1,5,' s')],[O('Power','w/t',500,' W',0)],eq='P = W ÷ t',note='<b>{=w/t|0}</b> W.'),
}
W['mom']={
'Momentum':calc('Momentum is mass × velocity: how hard something is to stop.',[P('m','Mass',1,20,1,5,' kg'),P('v','Velocity',0,20,1,4,' m/s')],[O('Momentum','m*v',400,' kg·m/s',0)],eq='p = m v',note='<b>{=m*v|0}</b> kg·m/s.'),
'Conservation of momentum':calc('Two carts crash and stick. Total momentum before = after.',[P('m1','Cart 1 mass',1,10,1,2,' kg'),P('v1','Cart 1 speed',0,10,1,6,' m/s'),P('m2','Cart 2 mass (at rest)',1,10,1,4,' kg')],[O('Speed after','m1*v1/(m1+m2)',10,' m/s',2)],eq='m₁v₁ = (m₁ + m₂)v',note='v = {m1}×{v1} ÷ ({m1}+{m2}) = <b>{=m1*v1/(m1+m2)|2}</b> m/s.'),
'Impulse':calc('Impulse = force × time = change in momentum.',[P('f','Force',1,100,1,50,' N'),P('t','Time',.1,2,.1,.5,' s')],[O('Impulse','f*t',200,' N·s',1)],note='<b>{=f*t|1}</b> N·s. A longer stopping time needs less force for the same impulse (airbags!).'),
}
W['cir']={
'Centripetal acceleration':calc('Going around a circle needs an inward pull.',[P('v','Speed',1,20,1,10,' m/s'),P('r','Radius',1,20,1,5,' m')],[O('Inward acceleration','v^2/r',100,' m/s²',1)],eq='a = v² ÷ r',note='<b>{=v^2/r|1}</b> m/s². A tighter turn (small r) or a faster speed needs more.'),
'Gravity between masses':calc('Gravity gets weaker with distance squared.',[P('d','Distance (Earth radii)',1,10,1,1,'')],[O('Relative pull','1/d^2',1,'',3)],note='At <b>{d}</b> Earth radii from the center, gravity is <b>{=1/d^2|3}</b> times its surface value.'),
}
W['wav']={
'Frequency and period':wave('A wave: how many peaks pass each second?',[P('A','Amplitude',1,10,1,5),P('f','Frequency',1,6,1,3,' Hz')],'<b>{f}</b> waves per second. Period = 1/{f} = <b>{=1/f|2}</b> s.'),
'Wavelength and speed':calc('Wave speed = frequency × wavelength.',[P('f','Frequency',1,20,1,5,' Hz'),P('l','Wavelength',1,20,1,3,' m')],[O('Speed','f*l',400,' m/s',0)],eq='v = f λ',note='<b>{=f*l|0}</b> m/s.',take='v = f × λ'),
'Sound':calc('Sound travels about 343 m/s in air. How far is the lightning?',[P('t','Seconds between flash and thunder',1,20,1,5)],[O('Distance','343*t',7000,' m',0)],note='{t} s × 343 m/s = <b>{=343*t|0}</b> m.'),
}
W['opt']={
'Reflection':plot('Angle in = angle out.',['x*tand(a)','-x*tand(a)'],[P('a','Angle from the normal',10,80,5,40,'°')],x=(-5,5),y=(0,5),out='The ray hits at <b>{a}°</b> and leaves at <b>{a}°</b>.'),
'Refraction':calc('Light bends going into glass. Snell: sin θ₁ = n sin θ₂.',[P('a','Incoming angle',0,80,5,40,'°'),P('n','Material n',1,2.4,.1,1.5)],[O('Bent angle','asind(sind(a)/n)',90,'°',1)],note='Air → n = {n}: {a}° bends to <b>{=asind(sind(a)/n)|1}°</b>, toward the normal.'),
'Lenses and mirrors':calc('Move the object. Where does the image form?',[P('f','Focal length',5,20,1,10,' cm'),P('d','Object distance',11,60,1,25,' cm')],[O('Image distance','1/(1/f-1/d)',60,' cm',1)],eq='1/f = 1/d₀ + 1/dᵢ',note='Image at <b>{=1/(1/f-1/d)|1}</b> cm. Magnification {=1/(1/f-1/d)/d|2}×.'),
}
W['thm']={
'Specific heat':calc('Heat needed to warm water.',[P('m','Mass',1,10,1,2,' kg'),P('t','Temperature rise',1,80,1,20,' °C')],[O('Heat','m*4186*t/1000',3000,' kJ',0)],eq='Q = m c ΔT',note='<b>{=m*4186*t/1000|0}</b> kJ.'),
'Gas laws':calc('Squeeze a gas and its pressure rises.',[P('v','Volume',1,10,1,5,' L')],[O('Pressure','10/v',10,' atm',2)],eq='P × V = constant',note='P = 10 ÷ {v} = <b>{=10/v|2}</b> atm.'),
}
W['est']={
"Coulomb's law":calc('Charges push or pull; double the distance makes the force 4 times weaker.',[P('d','Distance',1,10,1,2,' m')],[O('Relative force','1/d^2',1,'',3)],note='<b>{=1/d^2|3}</b> times the force at 1 m.',pre=('Triple the distance between two charges. The force becomes…',['1/3','1/6','1/9'],2,'Force falls as 1/d²: 3² = 9.')),
}
W['kvl']={
'Voltage and current dividers':calc('A voltage divider shares a battery between two resistors.',[P('r1','R1',1,20,1,10,' kΩ'),P('r2','R2',1,20,1,10,' kΩ')],[O('Output across R2 (12 V in)','12*r2/(r1+r2)',12,' V',2)],note='<b>{=12*r2/(r1+r2)|2}</b> V.'),
}
W['rc']={
'RC charging':plot('A capacitor charges quickly at first, then slows.',['5*(1-exp(-x/t))'],[P('t','Time constant τ',.5,5,.5,2,' s')],x=(0,15),y=(0,6),out='After one τ ({t} s) it reaches 63% of 5 V = <b>3.16</b> V.',xl='time (s)',yl='volts',pts=[dict(x='t',y='5*(1-exp(-1))',l='63%')]),
}
W['ac']={
'What AC means':wave('AC voltage swings back and forth.',[P('A','Peak voltage',1,10,1,5,' V'),P('f','Cycles shown',1,6,1,2)],'Peak <b>{A}</b> V.'),
'RMS values':calc('RMS is the steady voltage that heats like the AC.',[P('v','Peak voltage',1,170,1,170,' V')],[O('RMS','v/1.414',130,' V',1)],note='<b>{=v/1.414|1}</b> V rms. The wall outlet: 170 V peak ≈ 120 V rms.'),
}
W['flt']={
'RC cutoff':plot('A low-pass filter lets low frequencies through.',['1/sqrt(1+(x/f)^2)'],[P('f','Cutoff frequency',1,10,1,4,' Hz')],x=(0,20),y=(0,1.2),out='Half power (0.707) at <b>{f}</b> Hz.',xl='frequency',yl='gain',pts=[dict(x='f',y='0.707',l='−3 dB')]),
}
W['dev']={'Diodes':simple('gate','A diode is like a one-way door. (Toggle: voltage on or off)',g='AND'),}
del W['dev']
W['dig']={
'Binary':simple('bits','Flip the switches to count in binary.',n=6,say='Each switch is worth double the one on its right.',take='Binary uses only 0 and 1. Each place is a power of 2.'),
'Logic gates':simple('gate','Flip A and B. When is the lamp on?',g='AND',take='AND: both must be 1. OR: either one.'),
'Truth tables':simple('gate','Try OR. Then compare with AND.',g='OR'),
}
W['mag']={
'Force on a wire':calc('A wire with current in a magnetic field feels a push.',[P('b','Field B',.1,2,.1,.5,' T'),P('i','Current',1,10,1,4,' A'),P('l','Length',.1,1,.1,.5,' m')],[O('Force','b*i*l',10,' N',2)],eq='F = B I L',note='<b>{=b*i*l|2}</b> N.'),
'Transformers':calc('A transformer changes voltage by the turns ratio.',[P('n1','Primary turns',50,500,50,100),P('n2','Secondary turns',50,1000,50,200)],[O('Output (from 120 V)','120*n2/n1',480,' V',0)],eq='V₂/V₁ = N₂/N₁',note='<b>{=120*n2/n1|0}</b> V out.'),
}
W['pwr']={
'Why power lines use high voltage':calc('Same power at higher voltage means less current and far less loss.',[P('v','Line voltage',1,100,1,10,' kV')],[O('Loss (relative)','1/v^2',1,'',4)],note='Loss falls as 1/V². At {v} kV the loss is <b>{=1/v^2|4}</b> of the loss at 1 kV.'),
}
WID=W
