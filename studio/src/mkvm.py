# -*- coding: utf-8 -*-
# 31.0: Voltaic (Circuit Lab B) and Stratus (Meteorology B) expansion, written to src/docs/QUESTION_RULES.md.
# Every item: [Subject | Subtopic | Tier n] tag, clean numbers, 2 hints + diagnostic solution with the common trap.
# Numeric answers are computed here (never typed by hand). v is in base SI units unless the unit is free text (km, kt, mph...).
import json,math,sys
def fmt(x):
    s='%.3g'%x
    return s
def tag(subj,sub,tier):return f"[{subj} | {sub} | Tier {tier}]"
def b(tier):return round(max(-1,min(1,-1+tier*0.1)),1)
def NUM(subj,t,sub,tier,q,v,u,h1,h2,sol,trap,fp,tol=0.015):
    num={'v':v,'tol':tol}
    if u:num['u']=u
    return dict(t=t,l=1 if tier<=5 else 2 if tier<=12 else 3,b=b(tier),type='short',q=tag(subj,sub,tier)+' '+q,num=num,w=trap,sol=[h1,h2,sol+' Trap: '+trap],fp=fp)
def MCQ(subj,t,sub,tier,q,o,h1,h2,sol,trap,fp):
    return dict(t=t,l=1 if tier<=5 else 2 if tier<=12 else 3,b=b(tier),type='mcq',q=tag(subj,sub,tier)+' '+q,o=o,w=trap,sol=[h1,h2,sol+' Trap: '+trap],fp=fp)
V=[];M=[]
C='Circuits'
# ---------- VOLTAIC: capacitors and RC timing ----------
for i,(R,Cc) in enumerate([(20e3,50e-6),(47e3,100e-6),(10e3,470e-6),(5e3,200e-6)]):
    tau=R*Cc
    V.append(NUM(C,'cap','Capacitance',3,f"A {R/1e3:g} kΩ resistor charges a {Cc*1e6:g} µF capacitor from a battery. What is the time constant τ = RC? (seconds)",tau,'s',
     'Time constant is a product, not a sum.','Convert kΩ to Ω and µF to F before multiplying.',f"τ = RC = {R:g} Ω × {Cc:g} F = {fmt(tau)} s.",'Forgetting the µ (10⁻⁶) makes the answer a million times too large.',f'v31_cap_tau{i}'))
for i,(Vs,n) in enumerate([(12,2),(10,3),(9,1),(6,5)]):
    v=Vs*(1-math.exp(-n))
    V.append(NUM(C,'cap','Capacitance',7,f"A capacitor charges through a resistor from a {Vs} V supply. How many volts is it at after {n} time constant{'s' if n>1 else ''}?",v,'V',
     'The curve rises fast at first then flattens.','Use v = Vs(1 − e^(−t/τ)) with t/τ = '+str(n)+'.',f"v = {Vs}(1 − e^−{n}) = {fmt(v)} V.",'After one τ the capacitor is at 63%, not 100%, and never exactly reaches the supply.',f'v31_cap_n{i}',tol=0.01))
for i,(tau,Vs,Vt) in enumerate([(1,10,8),(1,10,5),(0.5,12,9),(2,6,4)]):
    t=-tau*math.log(1-Vt/Vs)
    V.append(NUM(C,'cap','Capacitance',9,f"With τ = {tau} s, a capacitor charges from 0 V toward a {Vs} V supply. How many seconds until it reaches {Vt} V?",t,'s',
     'Rearrange the charging equation to solve for time (a logarithm).','t = −τ ln(1 − V/Vs).',f"t = −{tau} ln(1 − {Vt}/{Vs}) = {fmt(t)} s.",'Using ln(V/Vs) instead of ln(1 − V/Vs) gives a negative time: the curve tracks the REMAINING gap.',f'v31_cap_t{i}'))
for i,(R,Cc,V0,V1,lab) in enumerate([(400,250e-6,8,2,'a relay coil'),(385,187e-6,7.67,2.451,'a hovercraft relay coil (385 Ω, pull-in 7.67 V, drop-out 2.451 V)'),(500,200e-6,6,3,'a relay coil'),(200,500e-6,9,3,'a relay coil')]):
    t=R*Cc*math.log(V0/V1)
    nm=f"A {Cc*1e6:g} µF capacitor discharges through {lab}" if i!=1 else f"A {Cc*1e6:g} µF capacitor discharges through {lab}"
    extra='' if i==1 else f" of {R} Ω"
    V.append(NUM(C,'cap','Capacitance',11,f"{nm}{extra}. The relay stays closed while the capacitor is above {V1} V; it starts at {V0} V. How long (in ms) does the relay hold?",t,'ms',
     'Discharge is exponential decay through the coil resistance.','t = RC ln(V₀/V₁). Check that your answer is a few τ at most.',f"t = {R}×{Cc:g}×ln({V0}/{V1}) = {fmt(t*1000)} ms.",'Using ln(V₁/V₀) gives a negative time; and the ratio, not the difference, goes inside the log.',f'v31_cap_dis{i}',tol=0.02))
for i,(Cc,Vv) in enumerate([(100e-6,12),(470e-6,9),(1000e-6,5),(220e-6,6)]):
    E=0.5*Cc*Vv*Vv
    V.append(NUM(C,'cap','Capacitance',4,f"How much energy (mJ) is stored in a {Cc*1e6:g} µF capacitor charged to {Vv} V?",E,'mJ',
     'Energy depends on the square of the voltage.','E = ½CV².',f"E = ½ × {Cc:g} × {Vv}² = {fmt(E*1000)} mJ.",'Dropping the ½, or forgetting to square V, are the two usual slips.',f'v31_cap_E{i}'))
for i,(C1,C2,mode) in enumerate([(100,300,'s'),(6,3,'s'),(47,100,'p'),(22,33,'p')]):
    ce=(C1*C2/(C1+C2)) if mode=='s' else C1+C2
    nm='in series' if mode=='s' else 'in parallel'
    V.append(NUM(C,'cap','Capacitance',5,f"A {C1} µF and a {C2} µF capacitor are connected {nm}. What is the equivalent capacitance (µF)?",ce*1e-6,'µF',
     'Capacitors are the opposite of resistors for series and parallel.','Parallel adds. Series: 1/C = 1/C₁ + 1/C₂.',f"{'C = C₁C₂/(C₁+C₂)' if mode=='s' else 'C = C₁ + C₂'} = {fmt(ce)} µF.",'Using the resistor rules for capacitors swaps the two answers.',f'v31_cap_eq{i}',tol=0.01))
for i,(Vs,R,t,tau) in enumerate([(10,10e3,2,1)]):
    I=Vs/R*math.exp(-t/tau)
    V.append(NUM(C,'cap','Capacitance',9,f"A 10 V supply charges a capacitor through 10 kΩ with τ = 1 s. What is the charging current (in mA) at t = 2 s?",I,'mA',
     'Current is biggest at the start and decays.','I = (Vs/R)e^(−t/τ).',f"I = (10/10 000)e^−2 = {fmt(I*1000)} mA.",'The starting current Vs/R = 1 mA is NOT the answer at 2 s; it has already fallen.',f'v31_cap_I{i}'))
# ---------- DC circuits ----------
for i,(Vs,R1,R2,RL) in enumerate([(12,1e3,1e3,1e3),(12,2e3,2e3,2e3),(10,1e3,1e3,1e3),(9,3e3,6e3,6e3)]):
    Rb=R2*RL/(R2+RL);Vo=Vs*Rb/(R1+Rb)
    V.append(NUM(C,'circ','DC circuits',9,f"A divider has R₁ = {R1/1e3:g} kΩ on top and R₂ = {R2/1e3:g} kΩ on the bottom across {Vs} V. A {RL/1e3:g} kΩ load is connected across R₂. What is the load voltage?",Vo,'V',
     'The load changes the bottom resistance.','Replace R₂ and the load by their parallel equivalent, then divide.',f"R₂‖R_L = {fmt(Rb/1e3)} kΩ, so V = {Vs}×{fmt(Rb/1e3)}/({R1/1e3:g}+{fmt(Rb/1e3)}) = {fmt(Vo)} V.",'The unloaded divider answer ignores that the load drags the voltage down.',f'v31_div{i}'))
for i,(Vs,Rs) in enumerate([(12,4),(24,6),(10,5),(18,9)]):
    P=Vs**2/(4*Rs)
    V.append(NUM(C,'circ','DC circuits',12,f"A {Vs} V source has {Rs} Ω of internal resistance. What is the largest power (in watts) it can deliver to a load resistor?",P,'W',
     'Delivered power rises, peaks, then falls as the load changes.','The peak is when the load equals the internal resistance.',f"R_L = {Rs} Ω, current = {Vs}/{2*Rs} A, P = I²R = {fmt(P)} W.",'Using the whole V²/R_s (4× too high) forgets that half the voltage is lost inside the source.',f'v31_mpt{i}'))
for i,(E,r,I) in enumerate([(12,0.5,4),(9,0.2,5),(6,0.4,2.5)]):
    Vt=E-I*r
    V.append(NUM(C,'virpe','V, I, R, P, E',7,f"A battery has EMF {E} V and internal resistance {r} Ω. What is its terminal voltage while supplying {I} A?",Vt,'V',
     'Some voltage is lost inside the battery itself.','Terminal voltage = EMF − I·r.',f"V = {E} − {I}×{r} = {fmt(Vt)} V.",'Adding I·r instead of subtracting it gives a terminal voltage above the EMF, which is impossible while discharging.',f'v31_term{i}'))
for i,(I,t) in enumerate([(5,12),(4,18),(3,15)]):
    mAh=I*t/3.6
    V.append(NUM(C,'virpe','V, I, R, P, E',7,f"A hovercraft fan draws {I} A for a {t} s run. How many mAh of battery charge does it use? (number only)",mAh,'',
     'Charge is current × time.','1 mAh = 3.6 coulombs.',f"Q = {I}×{t} = {I*t} C = {fmt(mAh)} mAh.",'Treating seconds as hours is a factor of 3600 error.',f'v31_mAh{i}',tol=0.02))
for i,(Vb,I,t) in enumerate([(12,4,18),(9.6,2.5,15),(7.2,5,12),(12,3,10)]):
    E=Vb*I*t
    V.append(NUM(C,'virpe','V, I, R, P, E',7,f"A {Vb} V pack supplies {I} A for {t} s. How many joules of energy does the load use?",E,'J',
     'Energy is power × time.','P = VI first, then multiply by the time.',f"E = {Vb}×{I}×{t} = {fmt(E)} J.",'Stopping at power (W) is the partial-step trap: the question asks for energy.',f'v31_En{i}'))
for i,(a,bb,c) in enumerate([(100,200,150),(300,100,450),(120,240,90)]):
    d=bb*c/a
    V.append(NUM(C,'kirch','Kirchhoff',8,f"A Wheatstone bridge is balanced with R₁ = {a} Ω and R₂ = {bb} Ω in one arm pair and R₃ = {c} Ω with R₄ unknown (R₁/R₂ = R₃/R₄). Find R₄ in ohms.",d,'Ω',
     'At balance no current flows through the meter.','Set the two ratios equal and solve for R₄.',f"R₄ = R₂R₃/R₁ = {bb}×{c}/{a} = {fmt(d)} Ω.",'Inverting one ratio gives R₄ = R₁R₃/R₂, which is wrong.',f'v31_wb{i}'))
for i,(I,Ra,Rb2) in enumerate([(3,6,3),(6,4,12),(9,6,3)]):
    Ia=I*Rb2/(Ra+Rb2)
    V.append(NUM(C,'circ','DC circuits',7,f"{I} A enters a parallel pair of {Ra} Ω and {Rb2} Ω resistors. How many amps flow through the {Ra} Ω resistor?",Ia,'A',
     'Current prefers the easier path.','Current in one branch = total × (the OTHER resistance) / (sum).',f"I = {I}×{Rb2}/({Ra}+{Rb2}) = {fmt(Ia)} A.",'Using its own resistance in the numerator gives the other branch’s current.',f'v31_cdiv{i}'))
for i,(Vs,R1,R2) in enumerate([(12,3e3,6e3),(10,1e3,4e3),(15,2e3,3e3)]):
    Rth=R1*R2/(R1+R2)
    V.append(NUM(C,'circ','DC circuits',12,f"A {Vs} V source feeds a divider R₁ = {R1/1e3:g} kΩ, R₂ = {R2/1e3:g} kΩ. What is the Thevenin resistance (Ω) seen by a load across R₂?",Rth,'Ω',
     'Short the source and look back into the output terminals.','With the source shorted, R₁ and R₂ are in parallel.',f"R_th = R₁‖R₂ = {fmt(Rth)} Ω.",'Adding R₁ + R₂ is the series mistake; the shorted source ties R₁ to the other rail.',f'v31_th{i}'))
for i,(Vs,Vf,I) in enumerate([(9,2,20e-3),(5,2,10e-3),(12,3,20e-3),(6,2,16e-3)]):
    R=(Vs-Vf)/I
    V.append(NUM(C,'diode','Diodes & LEDs',7,f"An LED with a {Vf} V forward drop must carry {I*1000:g} mA from a {Vs} V supply. What series resistor (Ω) is needed?",R,'Ω',
     'The resistor only sees the voltage the LED does not use.','R = (Vs − Vf)/I.',f"R = ({Vs} − {Vf})/{I:g} = {fmt(R)} Ω.",'Using the full supply voltage gives a resistor that is too big and a dim LED.',f'v31_led{i}'))
for i,(Rc,Vp) in enumerate([(400,8),(385,7.67)]):
    I=Vp/Rc
    V.append(NUM(C,'mag','Magnetism & induction',3,f"A relay coil has {Rc} Ω resistance and pulls in at {Vp} V. What coil current (mA) flows at pull-in?",I,'mA',
     'The coil is just a resistor for steady DC.','I = V/R.',f"I = {Vp}/{Rc} = {fmt(I*1000)} mA.",'Mixing up volts and amps leads to answers near 50 instead of 20.',f'v31_pull{i}'))
for i,(L,R) in enumerate([(0.5,100),(2,400)]):
    tau=L/R
    V.append(NUM(C,'mag','Magnetism & induction',5,f"What is the time constant (ms) of a {L} H inductor in series with {R} Ω?",tau,'ms',
     'Inductive time constants divide, capacitive ones multiply.','τ = L/R.',f"τ = {L}/{R} = {fmt(tau*1000)} ms.",'Using R·L (the RC form) is the rule-confusion trap.',f'v31_LR{i}'))
for i,(Vp,) in enumerate([(170,),(10,),(325,)]):
    Vr=Vp/math.sqrt(2)
    V.append(NUM(C,'dcac','DC & AC',4,f"A sine wave peaks at {Vp} V. What is its RMS voltage?",Vr,'V',
     'RMS is the DC value that gives the same heating.','Vrms = Vpeak/√2.',f"{Vp}/1.414 = {fmt(Vr)} V.",'Multiplying by √2 (instead of dividing) goes the wrong way.',f'v31_rms{i}'))

# ---------- VOLTAIC conceptual (every wrong option is one named misconception) ----------
def m(t,sub,tier,q,c,w1,w2,w3,h1,h2,sol,trap,fp):V.append(MCQ(C,t,sub,tier,q,[c,w1,w2,w3],h1,h2,sol,trap,fp))
m('cap','Capacitance',7,"A hovercraft timer charges a capacitor through a resistor. You double the resistor, keeping the supply and capacitor. What changes?",
 "It takes twice as long to reach any given voltage","It reaches twice the final voltage","It stores twice the energy at full charge","It charges to the same voltage in half the time",
 'Think about what limits the current.','τ = RC, so doubling R doubles τ.','A bigger R only slows the charging; the final voltage is still the supply.','Mixing speed with final value: R sets how fast, not how much.','v31_m_rc1')
m('cap','Capacitance',9,"On a relay-hold timer the capacitor discharges through the coil. Which change makes the relay stay closed LONGER?",
 "A larger capacitor","A coil with lower resistance","A lower starting voltage","A higher drop-out voltage",
 'Longer hold means more time before the voltage falls to the drop-out level.','t = RC ln(V₀/V₁).','Larger C increases RC. Lower R, lower V₀ or higher V₁ all shorten the hold.','Lower coil resistance feels like “easier flow” but it empties the capacitor faster.','v31_m_rc2')
m('cap','Capacitance',5,"After about how many time constants is a charging capacitor within 1% of its final voltage?",
 "5","1","2","10",
 'Each τ closes about 63% of the remaining gap.','e^(−5) ≈ 0.0067.','After 5τ the remaining gap is 0.7%.','After 1τ the capacitor is at 63%, which many students remember as “charged”.','v31_m_5tau')
m('cap','Capacitance',9,"Two capacitors of different sizes are connected in series to a battery. Which statement is true?",
 "They carry the same charge, and the smaller capacitor has the larger voltage","They have the same voltage","The larger capacitor has the larger voltage","They carry different charges",
 'What is the same for every component in a series chain?','Q = CV and Q is the same, so V is bigger where C is smaller.','The series chain passes equal charge; the voltage splits inversely to capacitance.','Copying the resistor rule “bigger gets more voltage” reverses the result.','v31_m_sercap')
m('circ','DC circuits',5,"A third resistor is added in PARALLEL with two resistors already connected to a battery. What happens to the total resistance and the battery current?",
 "Resistance falls and battery current rises","Resistance rises and current falls","Resistance and current both stay the same","Resistance falls and current falls",
 'Every extra parallel path is another route for current.','Total conductance adds, so total R decreases.','Smaller R with the same voltage means bigger current.','Adding a component does not automatically add resistance; that is only for series.','v31_m_par')
m('circ','DC circuits',9,"Two identical bulbs are in series with a battery. One bulb is shorted with a wire. What happens to the other bulb?",
 "It gets brighter","It goes out","It stays the same","It gets dimmer",
 'Draw the circuit. What does the shorted bulb carry now?','The remaining bulb now sees the full battery voltage and a smaller total resistance.','Total resistance halves, current doubles, power in the working bulb is four times larger.','Assuming a short “kills” the circuit confuses a short across a part with a short across the source.','v31_m_short')
m('virpe','V, I, R, P, E',6,"The voltage across a fixed resistor is doubled. By what factor does its power change?",
 "×4","×2","×1/2","×8",
 'Power can be written with V and R only.','P = V²/R.','Doubling V squares to 4.','Treating power as proportional to voltage (V alone) misses the square.','v31_m_pv')
m('virpe','V, I, R, P, E',12,"A source feeds a load. At the load value that gives MAXIMUM power, what is the efficiency?",
 "50%","100%","25%","75%",
 'Compare the power in the load with the power in the internal resistance.','At the match R_L = R_s, they share the voltage equally and carry the same current.','Half the power is wasted inside the source.','“Maximum power” does not mean “maximum efficiency”; efficiency keeps rising with R_L.','v31_m_eff')
m('virpe','V, I, R, P, E',9,"A battery’s terminal voltage drops when you draw more current. Why?",
 "More voltage is lost across its internal resistance","The EMF decreases instantly","The wires become superconducting","Electrons run out of energy",
 'The battery is not a perfect source.','Model it as an ideal EMF with a small resistor in series.','V_terminal = EMF − I·r.','Thinking the EMF itself changes confuses the ideal source with its real model.','v31_m_int')
m('kirch','Kirchhoff',8,"A Wheatstone bridge is balanced. What is the reading of the meter across its middle?",
 "Zero, because the two midpoints are at the same voltage","The supply voltage","Half of the supply voltage always","The average of the four resistances",
 'A balanced bridge is a statement about two voltage dividers.','Both dividers produce the same midpoint voltage.','Equal midpoint voltages mean no current in the meter.','Confusing “balanced” with “all four resistors equal” – only the ratios must match.','v31_m_bridge')
m('circ','DC circuits',10,"A 10 MΩ voltmeter is placed across a 100 kΩ resistor in a divider. Another 10 MΩ meter is placed across a 10 MΩ resistor. Which reading is MORE distorted?",
 "The one across the 10 MΩ resistor","The one across the 100 kΩ resistor","Both are the same","Neither; meters never change the circuit",
 'Compare the meter’s resistance with the part it measures.','Parallel combination changes the part a lot only when the two are similar.','10 MΩ ‖ 10 MΩ = 5 MΩ halves the resistance.','Believing a voltmeter is perfect ignores loading.','v31_m_meter')
m('diode','Diodes & LEDs',9,"A relay coil is driven by a transistor. Where does the flyback diode go and why?",
 "Across the coil, reverse-biased in normal operation, to give the collapsing current a path","In series with the coil, forward-biased, to protect it from reverse current","Across the battery, to stop it discharging","Across the transistor base, to speed up switching",
 'What does an inductor do when the current is suddenly cut?','It tries to keep the current flowing, creating a large voltage spike.','The diode conducts only at turn-off and clamps the spike.','Putting the diode forward-biased in normal operation short-circuits the coil.','v31_m_fly')
m('mag','Magnetism & induction',9,"The relay current is switched off in 1 ms. Why does the transistor see a much larger voltage than the supply?",
 "The coil’s collapsing magnetic field induces a voltage L·dI/dt","The battery voltage doubles","The capacitor releases extra charge","The resistor heats up",
 'A rapid change in current matters.','Faraday: induced voltage grows with how quickly the current falls.','A fast turn-off makes dI/dt large.','Blaming the battery overlooks the inductor’s stored energy.','v31_m_spike')
m('virpe','V, I, R, P, E',10,"A hovercraft fan runs through long, thin wires and draws a large current. What happens to the voltage at the fan compared with the battery?",
 "It is lower, by I × R of the wires","It is higher, because wires add voltage","It is identical, since wires have zero resistance","It oscillates",
 'Real wires have resistance.','Series wires drop I × R_wire.','A few ohms of wire at several amps cost volts and power.','Treating wires as ideal ignores a voltage drop that matters at high current.','v31_m_wire')
m('virpe','V, I, R, P, E',10,"A fresh pack is labelled 12.0 V nominal but reads 12.6 V with no load, then 11.6 V when the fan runs. Which statement explains this?",
 "Nominal is an average; the voltage depends on charge state and load current","The meter is broken","Batteries have exactly the labelled voltage","The fan adds voltage when it spins",
 'Compare no-load with loaded readings.','Open-circuit voltage is higher than the loaded voltage because of internal resistance.','Always measure under the condition the rules or your design care about.','“The label is the truth” is the nominal-versus-measured trap.','v31_m_nom')
m('circ','DC circuits',12,"A motor spins up slowly. At the instant of switch-on, is the current larger or smaller than at full speed, and why?",
 "Larger, because the spinning motor has not yet produced a back-EMF","Smaller, because the coil is cold","The same, because the battery is constant","Smaller, because friction is large",
 'A spinning motor also acts like a generator.','Back-EMF opposes the supply and rises with speed.','At start, I = V/R_winding is large; at speed, I = (V − EMF)/R.','Assuming current must be steady forgets back-EMF.','v31_m_motor')
m('logic','Digital logic',6,"A 2-input NAND gate has inputs A = 1 and B = 1. What is the output, and what does the gate do to an input of 1 on both pins?",
 "0, because NAND is AND followed by NOT","1, because NAND is OR","1, because both inputs are high","0, because NAND is always off",
 'Do AND first.','AND(1,1) = 1, then invert.','The output is 0, the only input pair that gives 0.','Reading NAND as “not AND” means the opposite of AND’s truth table.','v31_m_nand')

# ---------- STRATUS: Meteorology B ----------
Me='Meteorology'
def N2(t,sub,tier,q,v,u,h1,h2,sol,trap,fp,tol=0.015):M.append(NUM(Me,t,sub,tier,q,v,u,h1,h2,sol,trap,fp,tol))
def M2(t,sub,tier,q,c,w1,w2,w3,h1,h2,sol,trap,fp):M.append(MCQ(Me,t,sub,tier,q,[c,w1,w2,w3],h1,h2,sol,trap,fp))
for i,(dz,T0) in enumerate([(3,35),(2,30),(1.5,25),(0.5,20)]):
    T=T0-9.8*dz
    N2('upper','Upper air, soundings, CAPE',7,f"A dry parcel at {T0} °C rises {dz} km without condensation. What is its temperature (°C)?",T,'°C',
     'Rising air expands and cools.','Dry adiabatic lapse rate is 9.8 °C per km.',f"T = {T0} − 9.8×{dz} = {fmt(T)} °C.",'Using the environmental lapse rate (about 6.5 °C/km) instead of the parcel’s own rate.',f'v31_dalr{i}')
for i,(T,Td) in enumerate([(30,18),(28,16),(32,22),(30,22)]):
    h=125*(T-Td)
    N2('clouds','Severe-weather clouds',7,f"The surface temperature is {T} °C and the dew point is {Td} °C. About how high (m) is the lifting condensation level (cloud base)?",h,'m',
     'Cloud base sits where the temperature falls to the dew point.','Rule of thumb: about 125 m per °C of the temperature–dew-point spread.',f"LCL ≈ 125×({T}−{Td}) = {fmt(h)} m.",'Using the lapse rate (9.8 °C/km) without noting that the dew point also falls slightly.',f'v31_lcl{i}',tol=0.02)
for i,s in enumerate([15,12,18,30]):
    d=s/3
    N2('light','Lightning',4,f"You count {s} seconds between a lightning flash and its thunder. About how far away (km) was the strike?",d,'km',
     'Light arrives almost instantly; sound does not.','Sound covers roughly 1 km in 3 seconds.',f"{s}/3 = {fmt(d)} km.",'Dividing by 5 is the “miles” rule; mixing the units makes the answer off by 1.6.',f'v31_fb{i}',tol=0.02)
for i,t_ms in enumerate([2,1,0.5,1.2]):
    R=3e8*t_ms*1e-3/2/1000
    N2('torn','Tornadoes and radar',9,f"A radar pulse returns {t_ms} ms after it was sent. How far away (km) is the echo?",R,'km',
     'The pulse goes out and back.','Range = c·t/2, with c = 3×10⁸ m/s.',f"R = (3×10⁸ × {t_ms}×10⁻³)/2 = {fmt(R*1000)} m = {fmt(R)} km.",'Forgetting the factor of 2 doubles the range (partial-step trap).',f'v31_rng{i}')
for i,(d,sp) in enumerate([(60,30),(45,30),(90,45),(120,20)]):
    t=d/sp
    N2('tstorm','Severe thunderstorms',6,f"A storm is {d} km away moving straight toward you at {sp} km/h. How many hours until it arrives?",t,'h',
     'Distance divided by speed.','Check the units agree (km and km/h).',f"t = {d}/{sp} = {fmt(t)} h.",'Dividing speed by distance gives hours per km, not hours.',f'v31_arr{i}')
for i,(T,Td) in enumerate([(25,20),(30,20),(22,18),(28,13)]):
    rh=100-5*(T-Td)
    N2('maps','Maps, station models, METAR',7,f"Temperature is {T} °C and dew point {Td} °C. Use RH ≈ 100 − 5(T − Td). What is the relative humidity (%)? (number only)",rh,'',
     'The smaller the spread, the closer to saturation.','Plug into the given rule of thumb.',f"RH ≈ 100 − 5×{T-Td} = {rh}%.",'The rule fails for large spreads; use it only when T − Td is under about 15 °C.',f'v31_rh{i}',tol=0.02)
for i,(vin,vout) in enumerate([(-20,40),(-25,35),(-18,30)]):
    vr=(vout-vin)/2
    N2('torn','Tornadoes and radar',11,f"A velocity couplet shows {abs(vin)} kt inbound next to {vout} kt outbound. What is the rotational velocity (kt)?",vr,'kt',
     'Rotation has equal and opposite parts.','Vrot = (V_out − V_in)/2, with inbound written as negative.',f"Vrot = ({vout} − ({vin}))/2 = {fmt(vr)} kt.",'Dividing the SUM by two gives the mean motion of the storm, not its rotation.',f'v31_vrot{i}')
for i,cape in enumerate([2000,1250,3200,5000]):
    w=math.sqrt(2*cape)
    N2('upper','Upper air, soundings, CAPE',12,f"A sounding shows CAPE = {cape} J/kg. What is the theoretical maximum updraft speed (m/s) from w = √(2·CAPE)?",w,'m/s',
     'Convert buoyancy energy to speed.','Kinetic energy per kg = ½w², set equal to CAPE.',f"w = √(2×{cape}) = {fmt(w)} m/s.",'Real updrafts are well below this because of entrainment and drag.',f'v31_cape{i}',tol=0.02)
for i,(T0,T2,z) in enumerate([(25,5,2),(30,12,3),(28,18,1)]):
    g=(T0-T2)/z
    N2('upper','Upper air, soundings, CAPE',7,f"A sounding reads {T0} °C at the surface and {T2} °C at {z} km. What is the environmental lapse rate (°C/km)?",g,'°C/km',
     'Temperature change per height.','Divide the drop by the height difference.',f"({T0} − {T2})/{z} = {fmt(g)} °C/km.",'Comparing with 9.8 °C/km: bigger means absolutely unstable.',f'v31_elr{i}')
for i,(T0,lr) in enumerate([(15,5),(9,6),(18,6),(10,5)]):
    z=T0/lr
    N2('winter','Winter storms',7,f"The surface temperature is {T0} °C and falls {lr} °C per km. At what height (km) is the freezing level?",z,'km',
     'Where does the temperature reach 0 °C?','Height = temperature / lapse rate.',f"{T0}/{lr} = {fmt(z)} km.",'Subtracting instead of dividing gives a temperature, not a height.',f'v31_frz{i}')
for i,(ratio,liq) in enumerate([(10,1.5),(15,0.8),(20,0.5),(8,2.5)]):
    s=ratio*liq
    N2('winter','Winter storms',5,f"A snow-to-liquid ratio of {ratio}:1 and {liq} inch of liquid water means about how many inches of snow? ",s,'in',
     'Ratio times liquid.','Multiply the liquid equivalent by the ratio.',f"{ratio}×{liq} = {fmt(s)} in.",'Wet heavy snow has a LOW ratio (8:1); cold powder is high (20:1).',f'v31_snow{i}')
for i,(vals) in enumerate([(15,20),(30,40),(9,12)]):
    sv,wv=vals;sh=math.hypot(sv,wv)
    N2('setup','Setup: jets, fronts, shear',11,f"Surface wind is a {sv} kt southerly (blowing northward) and the wind at 6 km is a {wv} kt westerly (blowing eastward). What is the magnitude of the 0–6 km bulk shear (kt)?",sh,'kt',
     'Shear is the VECTOR difference.','South wind and west wind are at right angles: use Pythagoras.',f"√({sv}² + {wv}²) = {fmt(sh)} kt.",'Adding the speeds (35) forgets they are perpendicular.',f'v31_shr{i}')
for i,(G,w) in enumerate([(2,50),(1,50),(3,20)]):
    r=G*w/100
    N2('setup','Setup: jets, fronts, shear',11,f"The temperature drops {G} °C for every 100 km to your west, and the wind from the west is {w} km/h. How many °C per hour does cold advection cool a fixed point? (number only)",r,'',
     'Moving air carries its temperature along.','Rate = wind speed × temperature gradient.',f"{w}×{G}/100 = {fmt(r)} °C/h.",'Without the 100 km conversion the answer is 100× too big.',f'v31_adv{i}')
for i,(norm,act) in enumerate([(20,14),(30,21),(10,6)]):
    p=100*act/norm
    N2('dh','Drought and heat waves',3,f"A town normally receives {norm} inches of rain and received {act} inches. What percent of normal is that? (number only)",p,'',
     'Part over whole.','Divide actual by normal, times 100.',f"{act}/{norm}×100 = {fmt(p)}%.",'Reporting the deficit (30%) instead of the percent of normal (70%).',f'v31_pctn{i}',tol=0.01)
for i,(q,uu) in enumerate([(0,0)]):pass
# conceptual MCQs
Mq=[
('upper','Upper air, soundings, CAPE',12,"A sounding has CAPE of 3500 J/kg but also a strong cap (large CIN). Why might no storms form by afternoon?",
 "Parcels cannot rise through the warm layer aloft until something forces them to break through","Large CAPE always means storms","CIN is just another name for CAPE","A cap raises the temperature so parcels have no energy left",
 'Look for the stable layer.','CIN is the energy a parcel needs to overcome.','Storms need lifting (fronts, dryline, outflow) to get past the cap.','Equating high CAPE with guaranteed storms.','v31_m_cin'),
('setup','Setup: jets, fronts, shear',14,"Winds turn clockwise with increasing height in the lowest 3 km. What is this called and why does it matter for supercells?",
 "Veering, because it favours a rotating updraft","Backing, because it favours a rotating updraft","Veering, because it makes the updraft weaker","Backing, because it removes shear",
 'Clockwise turning has a name.','Veering = clockwise; backing = counter-clockwise (in the Northern Hemisphere).','Veering with height supports a storm-relative inflow and rotation.','Swapping veering and backing is the most common vocabulary slip.','v31_m_veer'),
('torn','Tornadoes and radar',12,"A radar scan shows strong inbound velocity directly beside strong outbound velocity. What does this couplet indicate?",
 "Rotation (a mesocyclone or tornado vortex)","A line of straight-line winds","Hail growing aloft","A stationary front",
 'Opposite directions side by side.','Doppler radar sees motion toward or away from the beam.','Adjacent opposite velocities mark rotation.','Reading it as a uniform wind misses the opposite sign.','v31_m_couplet'),
('winds','Damaging winds',10,"After a damaging wind event, trees are all laid in the same direction in a straight swath. Which was most likely?",
 "A downburst or derecho (straight-line winds)","A tornado","An earthquake","A dust devil",
 'Look at the pattern of damage.','Tornado damage converges or swirls; straight-line wind damage diverges outward in one direction.','Same-direction debris means divergent outflow.','Assuming any severe wind damage is a tornado.','v31_m_down'),
('hurr','Hurricanes',11,"A hurricane moves north at 15 mph with maximum winds of 100 mph. Which quadrant usually has the strongest winds?",
 "The right-front quadrant, because storm motion adds to the rotation","The left-rear quadrant","The center of the eye","The left-front quadrant",
 'Add vectors in the Northern Hemisphere, where the circulation is counter-clockwise.','On the right side, rotation and motion point the same way.','Right side: 100 + 15 = 115 mph; left: 100 − 15 = 85 mph.','Thinking the eye has the strongest wind – it is the calm center.','v31_m_rfq'),
('hurr','Hurricanes',8,"Which condition most strongly weakens a hurricane?",
 "Strong vertical wind shear","Very warm water","Low pressure at the surface","High humidity",
 'Shear tears the vertical structure.','A hurricane needs a tall, stacked circulation.','Shear tilts the storm and blows the heat release away from the center.','Warm water and low pressure are growth factors, not weakeners.','v31_m_shear'),
('precip','Precipitation and floods',6,"How deep can moving water be before it can float most cars?",
 "About 1 foot (12 inches)","About 6 inches","About 4 feet","More than 10 feet",
 'It is far less than people think.','Moving water as shallow as 6 inches can knock a person down; 12 inches floats many vehicles.','Remember: “Turn around, don’t drown.”','Thinking a car is heavy enough to hold the ground.','v31_m_ftw'),
('winter','Winter storms',10,"Rain falls through a deep warm layer and then a shallow layer below 0 °C at the surface. What reaches the ground?",
 "Freezing rain","Sleet","Snow","Hail",
 'Check which layer is warm and which is cold.','Sleet needs a deep cold layer near the ground to refreeze drops first.','A shallow cold layer lets drops stay liquid until they hit a freezing surface.','Calling any ice sleet confuses which layer is sub-freezing.','v31_m_zr'),
('winter','Winter storms',10,"For lake-effect snow, cold air flows across a warmer lake. About what temperature difference between the lake surface and 850 mb air is usually needed?",
 "About 13 °C or more","About 2 °C","About 5 °C","Zero – any difference works",
 'It must be large enough for strong instability.','Rule of thumb for the Great Lakes.','A difference near 13 °C makes the low layer unstable enough for bands.','Using a tiny difference gives clouds but not heavy bands.','v31_m_lake'),
('dh','Drought and heat waves',9,"A strong upper-level ridge sits over a region for days. Why do temperatures soar?",
 "Sinking air warms by compression and skies stay clear","Rising air cools and leaves heat behind","Cold air masses are pushed in","The sun is closer",
 'Which way does air move in a ridge?','Sinking air is compressed and warmed adiabatically.','Subsidence also suppresses clouds and rain.','Rising air cools, so it cannot explain a heat wave.','v31_m_ridge'),
('light','Lightning',8,"About how many strokes of lightning give the visible “flash”?",
 "Several return strokes within a fraction of a second","Only one stroke ever","Dozens of separate flashes per minute from one channel","None – it is all one continuous arc",
 'Flicker is real.','The first leader opens the channel; return strokes follow.','Multiple return strokes explain the flicker you see.','Assuming one flash is one stroke.','v31_m_strokes'),
('obs','Observation tools',5,"Each 10 dBZ increase in radar reflectivity means about how much more returned power?",
 "10 times","2 times","10 dBZ is the same power","100 times",
 'dB scales are logarithmic.','10 dB is a factor of 10 in power.','So 50 dBZ returns 10× the power of 40 dBZ.','Treating dB as a linear scale.','v31_m_dbz'),
('maps','Maps, station models, METAR',7,"A METAR reads 27015G25KT. What does it say about the wind?",
 "From 270° at 15 kt with gusts to 25 kt","Toward 270° at 15 kt","From 270° at 25 kt with gusts to 15 kt","From 150° at 27 kt",
 'Wind direction is where the wind comes FROM.','Direction (3 digits), speed (2), G for gust.','270° is westerly: from the west.','Reading direction as where the wind is going.','v31_m_metar'),
('maps','Maps, station models, METAR',6,"On a station model, a wind barb has two full barbs and one half barb. What is the speed?",
 "25 kt","20 kt","15 kt","35 kt",
 'Full barb 10 kt, half barb 5 kt.','Add them.','10 + 10 + 5 = 25 kt.','Counting a half barb as a full barb.','v31_m_barb'),
('safety','Hazards and safety',5,"A tornado WARNING is issued for your town. What does it mean?",
 "A tornado is occurring or imminent; take shelter now","Conditions are favourable; be ready","A tornado was seen last week","Winds will be strong but there is no tornado",
 'Watch vs warning.','A watch means favourable conditions; a warning means it is happening.','Warning = act now.','Mixing up watch and warning delays shelter.','v31_m_warn'),
('upper','Upper air, soundings, CAPE',10,"A lifted index of −6 means what?",
 "Unstable air that can support strong storms","Very stable air","No moisture","A strong cold front passed",
 'LI = environment temperature − lifted-parcel temperature at 500 mb.','Negative LI means the parcel is warmer than the environment.','The more negative, the more unstable.','Reading the negative sign as “weak” instead of “unstable”.','v31_m_li'),
('tstorm','Severe thunderstorms',6,"By NWS criteria, a thunderstorm is severe if it produces hail of at least what size?",
 "1 inch (quarter size)","Pea size (¼ inch)","Golf ball only (1.75 inch)","Baseball only (2.75 inch)",
 'It was raised from ¾ inch in 2010.','Quarter-sized hail.','Severe also means winds of 58 mph or higher or a tornado.','Remembering the old ¾ inch criterion.','v31_m_hail'),
('torn','Tornadoes and radar',8,"A 140 mph tornado is rated what on the Enhanced Fujita scale?",
 "EF3","EF2","EF4","EF1",
 'EF3 is 136–165 mph.','Memorise the three-second-gust ranges.','EF0 65–85, EF1 86–110, EF2 111–135, EF3 136–165.','Rating by damage vs wind speed ranges.','v31_m_ef'),
('hurr','Hurricanes',6,"A hurricane has sustained winds of 120 mph. Which Saffir-Simpson category is it?",
 "Category 3","Category 2","Category 4","Category 5",
 'Cat 3 is 111–129 mph.','Learn the thresholds: 74, 96, 111, 130, 157.','120 falls between 111 and 129.','Assuming 120 is Category 4 because it is “big”.','v31_m_cat'),
('clouds','Severe-weather clouds',9,"A storm’s updraft is strong enough to push a flat anvil-like top above the tropopause. What is this called?",
 "An overshooting top","A wall cloud","A shelf cloud","A mammatus cloud",
 'The top is above the anvil.','It signals a very strong updraft.','Persistent overshooting tops mean an intense storm.','Confusing it with a wall cloud, which is on the base.','v31_m_ot'),
('clouds','Severe-weather clouds',9,"Which cloud lowering is usually found under the rain-free base of a supercell and may rotate?",
 "Wall cloud","Shelf cloud","Roll cloud","Mammatus",
 'It sits beneath the updraft.','Wall clouds form from rain-cooled air near the updraft.','A rotating wall cloud often precedes a tornado.','A shelf cloud is on the leading edge of outflow and does not rotate.','v31_m_wall'),
('setup','Setup: jets, fronts, shear',10,"Where does a dryline form in the Great Plains and why does it matter?",
 "Between moist Gulf air and dry desert air; storms often fire along it","Between two cold air masses","On the east coast","Where sea breezes meet; no storms ever",
 'Look at the moisture contrast.','Dry air is denser than moist air at the same temperature.','Moist air is lifted over the dry air.','Treating the dryline as a temperature front.','v31_m_dry'),
('setup','Setup: jets, fronts, shear',11,"Why are severe weather outbreaks often tied to a jet stream streak overhead?",
 "It provides divergence aloft and strong shear","It heats the surface","It adds moisture","It removes all clouds",
 'Think upper-level support.','Jet streaks create divergence and shear.','Divergence aloft promotes rising air; shear organises storms.','Thinking the jet directly heats the ground.','v31_m_jet'),
('cases','Historic cases and data',10,"A past outbreak lists large CAPE, strong shear, a cold front and a dryline. Which ingredient list is most complete for supercells?",
 "Moisture, instability, lift and wind shear","Heat only","Cold air only","Lightning only",
 'There are four classic ingredients.','Moisture, instability, lift and shear.','Without any one of them, storms are weaker or do not form.','Memorising only instability.','v31_m_ingr'),
]
for a in Mq:M2(*a)

# options re-balanced so the right answer is not the longest (no length cue)
OVR={
'v31_m_sercap':["Same charge on each; the smaller capacitor has the larger voltage","Same voltage on each; the smaller capacitor holds less charge","Same charge on each; the larger capacitor has the larger voltage","Different charges on each; the voltages are equal"],
'v31_m_int':["Voltage is lost across its internal resistance","The EMF itself falls as the current rises","The chemicals suddenly lose their stored energy","The connecting wires get longer at high current"],
'v31_m_bridge':["Zero: the two midpoints sit at equal voltage","The full supply voltage appears across the meter","Half the supply voltage, whatever the resistors are","The average of the four resistor values, in volts"],
'v31_m_fly':["Across the coil, reverse-biased, to carry the collapsing current","In series with the coil, forward-biased, to block reverse current","Across the battery, so that it cannot discharge by itself","From the transistor base to ground, to speed up switching"],
'v31_m_spike':["The coil’s collapsing field induces a voltage L·dI/dt","The battery voltage doubles when the switch opens","The capacitor dumps extra charge into the transistor","The resistor heats up and pushes charge back"],
'v31_m_nom':["Nominal is an average; real voltage depends on charge and load","The meter must be broken, since the label never changes","A battery always outputs exactly its labelled voltage","The fan adds voltage to the pack when it spins"],
'v31_m_motor':["Larger: the motor has no back-EMF until it speeds up","Smaller: the windings are still cold when it starts","The same: a battery always supplies constant current","Smaller: friction holds the motor back at the start"],
'v31_m_nand':["0, because NAND is AND followed by NOT","1, because NAND is a version of the OR gate","1, because both of the inputs are high","0, because NAND is always switched off"],
'v31_m_cin':["Parcels cannot get through the warm layer without lifting","High CAPE always guarantees that storms will form","CIN is simply another name for the CAPE value","The cap heats parcels until no energy is left"],
'v31_m_couplet':["Rotation (mesocyclone or tornado vortex)","A line of straight-line winds across the area","Large hail growing in the cloud aloft","A stationary front passing over the radar"],
'v31_m_down':["A downburst or derecho (straight-line wind)","A tornado with a narrow converging path","An earthquake shaking the trees down","A dust devil lifting debris upward"],
'v31_m_rfq':["The right-front quadrant: motion adds to rotation","The left-rear quadrant, behind the storm","The middle of the eye at the centre","The left-front quadrant, ahead of the storm"],
'v31_m_ftw':["About 1 foot (12 inches)","About 6 inches (half a foot)","About 4 feet (48 inches)","Over 10 feet of fast water"],
'v31_m_zr':["Freezing rain","Sleet (ice pellets)","Snow flakes","Hail stones"],
'v31_m_ridge':["Sinking air warms by compression, skies clear","Rising air cools and leaves its heat behind","Cold air masses are pushed in from the north","The sun is closer to the ground at that time"],
'v31_m_warn':["A tornado is happening or imminent: shelter now","Conditions are favourable: stay alert and be ready","A tornado was reported in the area last week","Winds will be strong but no tornado is expected"],
'v31_m_li':["Unstable air that can support strong storms","Very stable air with no chance of storms","Air with no moisture in the whole column","A strong cold front passed through earlier"],
'v31_m_dry':["Between moist Gulf air and dry desert air","Between two cold air masses of equal moisture","Along the east coast where sea breezes meet","Between two jet streaks in the stratosphere"],
'v31_m_jet':["Divergence aloft and strong wind shear","Direct heating of the surface air below","A fresh supply of moisture from the stratosphere","Removal of all cloud so the sun can heat"],
'v31_m_ingr':["Moisture, instability, lift and wind shear","Warm temperatures and clear blue skies","Cold air and a strong high pressure","Lightning and thunder showing on radar"],
}
import random as _r
_R=_r.Random(7)
for q in V+M:
    if q['fp'] in OVR:q['o']=OVR[q['fp']]
if __name__=='__main__':
    json.dump({'new':V},open(sys.argv[1],'w',encoding='utf8'),ensure_ascii=False)
    json.dump({'new':M},open(sys.argv[2],'w',encoding='utf8'),ensure_ascii=False)
    print(len(V),len(M))
