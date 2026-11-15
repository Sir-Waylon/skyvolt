import json, math
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/c3.json"
T="virpe"; new=[]; n=[0]
def fp():
    n[0]+=1; return f"c3_{n[0]:02d}"
def mcq(l,b,q,o,w,sol): new.append(dict(t=T,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(l,b,q,o,a,w,sol): new.append(dict(t=T,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=T,l=l,b=b,type="short",q=q,num=dict(v=round(v,6) if abs(v)<1e15 else v,tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(l,b,q,text,w,sol): new.append(dict(t=T,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(l,b,q,items,w,sol): new.append(dict(t=T,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(l,b,q,pairs,w,sol): new.append(dict(t=T,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))
# lock-it-in
txt(1,-0.8,"What unit is mAh a measure of?",["charge","electric charge","amount of charge"],"mAh = current × time, which is charge, not energy.",["1 mAh = 0.001 A × 3600 s = 3.6 C.","Energy needs voltage too (Wh).","Trap: mAh is NOT energy."])
txt(1,-0.7,"One joule per coulomb is the definition of which unit?",["volt","volts","V"],"Voltage is energy per charge: 1 V = 1 J/C.",["Voltage = energy ÷ charge.","1 A = 1 C/s and 1 W = 1 J/s are the other two."])
num(1,-0.6,"Convert 250 mA to amperes.",0.25,"A","Milli means ÷1000.",["250 ÷ 1000 = 0.25 A.","Trap: moving the decimal the wrong way."])
num(1,-0.5,"A 12 V battery moves 5.0 C of charge through a circuit. How much energy does it deliver, in joules?",60,"J","E = Q·V.",["Volt = joule per coulomb.","E = 5.0 × 12 = 60 J."])
mcq(1,-0.5,"To measure the current through a bulb, an ammeter must be placed:",["in series with the bulb","in parallel with the bulb","across the battery only","next to the bulb, not in the circuit"],"Current must flow through the meter, so it goes in the path.",["Ammeter: in series (low resistance).","Voltmeter: in parallel.","Trap: parallel ammeter shorts the part."])
mcq(1,-0.4,"A voltmeter measures the voltage across a resistor. It is connected:",["in parallel with the resistor","in series with the resistor","only at the battery","with the circuit broken first"],"Voltage is a difference between two points, so the meter bridges them.",["Voltage is measured across a part.","Series is for current."])
txt(1,-0.4,"Write the resistor color bands (first three colors) for 10 Ω: digit 1, digit 0, multiplier ×1.",["brown black black","brown, black, black"],"Brown = 1, black = 0 and black multiplier = ×1 → 10 Ω.",["Digits: brown 1, black 0.","Black as multiplier means ×1 (no zeros)."])
txt(2,0,"Three bands red, red, red (then gold). Give the value in kΩ as a number.",["2.2","2.2k","2.2 kΩ","2200"],"Red red red = 22 × 100 = 2200 Ω = 2.2 kΩ.",["2 and 2, then red multiplier is ×100.","2200 Ω = 2.2 kΩ."])
mcq(2,0,"A 220 Ω resistor has ±10% tolerance. Which value could it measure?",["238 Ω","190 Ω","250 Ω","200 Ω"],"10% of 220 is 22, so range is 198 to 242 Ω.",["220 × 0.10 = 22.","Range 198–242 Ω.","Only 238 fits."])
mcq(2,0,"A 100 Ω resistor is tested on a meter and reads 108 Ω. Its tolerance band must be at least:",["10% (silver)","5% (gold)","1% (brown)","2% (red)"],"108 is 8% above 100, so 5% fails and 10% passes.",["Error = 8 ÷ 100 = 8%.","Gold 5% is too tight, silver 10% works."])
multi(2,0.2,"Select ALL that equal one joule.",["1 W·s","1 V·C","1 A·V·s","1 W/s"],[0,1,2],"J = W·s = V·C, and A·V·s is the same as W·s. W/s is not energy.",["Power × time = energy.","Voltage × charge = energy.","A·V = W, so A·V·s = W·s.","W/s has the wrong units."])
match(2,0,"Match each quantity to its formula.",[["Power from V and R","V²/R"],["Charge from I and t","I·t"],["Energy from P and t","P·t"],["Resistance of a wire","ρL/A"]],"Each formula has one job.",["P = V²/R.","Q = It.","E = Pt.","R = ρL/A."])
# multi-step basics
num(2,0.2,"A 1500 W kettle is used for 90 minutes in total over a day. Energy used in kWh?",2.25,"kWh","E = P·t with kW and hours.",["1500 W = 1.5 kW; 90 min = 1.5 h.","1.5 × 1.5 = 2.25 kWh.","Trap: minutes not converted."])
num(2,0.3,"A 100 W computer runs nonstop for 30 days. Electricity is $0.25 per kWh. Total cost in dollars?",18,"$","Energy first, then cost.",["30 d × 24 h = 720 h.","0.1 kW × 720 h = 72 kWh.","72 × 0.25 = $18."])
num(2,0.3,"A 2000 mAh battery is rated 3.7 V. How much charge is that in coulombs?",7200,"C","2000 mAh = 2 Ah, and 1 Ah = 3600 C.",["2 A·h × 3600 s/h = 7200 C.","Voltage is not needed for charge."])
num(2,0.4,"A 3.7 V, 2000 mAh battery powers a motor that draws a steady 0.50 A. How long does it last, in hours (ideal case)?",4,"h","t = capacity ÷ current.",["2.0 Ah ÷ 0.50 A = 4.0 h.","Voltage is not needed here."],0.01)
num(2,0.4,"A 12 V car battery stores 50 Ah. How much energy is that, in Wh?",600,"Wh","Wh = V × Ah.",["12 × 50 = 600 Wh.","Trap: reporting Ah as energy."])
num(2,0.4,"The 600 Wh car battery powers a 60 W lamp. How many hours (ideal case)?",10,"h","t = E ÷ P.",["600 Wh ÷ 60 W = 10 h."])
num(2,0.5,"An EV needs 40 kWh. The charger delivers 7.0 kW. How many hours to charge (ideal)? Give one decimal.",5.7,"h","t = E/P.",["40 ÷ 7.0 = 5.71 h.","Cost would be kWh × rate."],0.02)
num(2,0.5,"A wire carries 20 A and has resistance 0.050 Ω. How many watts are wasted as heat in the wire?",20,"W","P = I²R.",["20² × 0.050 = 400 × 0.05 = 20 W.","Trap: P = V·I with the full supply voltage."])
num(2,0.5,"A 9.0 V supply lights an LED that needs 2.0 V and 20 mA. Resistor needed to limit current, in ohms?",350,"Ω","The resistor takes the leftover voltage.",["Leftover V = 9.0 − 2.0 = 7.0 V.","R = 7.0 ÷ 0.020 = 350 Ω."])
# hard
mcq(3,0.9,"A 100 W and a 60 W bulb (both 120 V) are wired in series across 120 V. Which glows brighter?",["The 60 W bulb","The 100 W bulb","Both equal","Neither lights"],"Series current is equal; the 60 W bulb has more resistance so P = I²R is larger.",["R = V²/P: 60 W → 240 Ω, 100 W → 144 Ω.","Same current in series.","P = I²R is bigger for 240 Ω.","Trap: brighter = bigger rating."])
num(3,1.0,"A 120 V, 60 W bulb is run on 60 V. Treating its resistance as constant, what power does it use?",15,"W","P goes as V².",["R = 120²/60 = 240 Ω.","P = 60²/240 = 15 W.","Half voltage → ¼ power."])
mcq(3,1.0,"The voltage across a fixed resistor is halved. The power becomes:",["¼ as large","½ as large","twice as large","unchanged"],"P = V²/R.",["Half V → (½)² = ¼.","Trap: P is not proportional to V."])
mcq(3,1.2,"A heater's supply voltage stays fixed. Its resistance is cut to half. The heat produced per second:",["doubles","halves","quadruples","stays the same"],"P = V²/R, so lower R means more power.",["V fixed, R ÷2 → P ×2.","Trap: thinking more resistance means more heat at fixed voltage."])
mcq(3,1.5,"Both the voltage across a resistor and the resistance are halved. The power becomes:",["½ as large","¼ as large","unchanged","twice as large"],"P = V²/R: (½)² ÷ ½ = ½.",["V² factor ¼.","Dividing by half R doubles it: ¼ × 2 = ½."])
mcq(3,1.1,"A wire is stretched uniformly to twice its length (same total volume of metal). Its resistance becomes:",["4 times as large","2 times as large","½ as large","unchanged"],"Longer AND thinner both raise R.",["L ×2 → R ×2.","Same volume → area ÷2 → R ×2 more.","Total ×4."])
num(3,1.5,"A 2.0 Ω wire is stretched uniformly to three times its length (volume unchanged). New resistance in ohms?",18,"Ω","R ∝ L² when volume is fixed.",["L ×3 → R ×3.","Area ÷3 → R ×3 more.","2.0 × 9 = 18 Ω."])
mcq(3,1.4,"A wire has twice the diameter and twice the length of another wire of the same metal. Its resistance compared with the other is:",["½ as large","twice as large","4 times as large","unchanged"],"Length ×2 → R ×2. Diameter ×2 → R ÷4. Net ½.",["2 ÷ 4 = ½.","Trap: forgetting area depends on diameter²."])
num(3,1.9,"A 12 Ω wire is cut into four equal pieces. The pieces are twisted together side by side to make one thick wire. What is its resistance in ohms?",0.75,"Ω","Length ÷4 and area ×4 gives ÷16.",["Each piece is 3 Ω.","Four 3 Ω paths side by side: 3 ÷ 4 = 0.75 Ω.","Or R ×(¼)(¼) = 12/16."],0.02)
num(3,1.3,"A wire has resistance 8.0 Ω. Another wire of the same metal has half the length and half the diameter. Its resistance in ohms?",16,"Ω","Half length gives ½; half diameter gives ×4.",["R ∝ L/d².","(½) ÷ (¼) = 2.","8.0 × 2 = 16 Ω."])
num(3,1.0,"How many times larger is the resistance of an aluminum wire than a copper wire of the same length and area? (ρ Al 2.65, Cu 1.68, ×10⁻⁸ Ω·m) One decimal place.",1.6,"×","Ratio of resistivities.",["2.65 ÷ 1.68 = 1.58.","About 1.6."],0.02)
num(3,0.9,"A copper wire (ρ = 1.68×10⁻⁸ Ω·m) is 2.0 m long with area 0.50 mm². Its resistance in ohms?",0.0672,"Ω","R = ρL/A with area in m².",["0.50 mm² = 0.50×10⁻⁶ m².","R = 1.68×10⁻⁸ × 2.0 ÷ 0.5×10⁻⁶ = 0.067 Ω.","Trap: mm² → m² is ×10⁻⁶."])
num(3,1.4,"A copper wire has resistance 10.0 Ω at 20 °C. Resistance rises 0.39% per °C (R = R₀(1 + 0.0039·ΔT)). Resistance at 70 °C, in ohms?",11.95,"Ω","Add the rise from ΔT = 50 °C.",["0.0039 × 50 = 0.195.","10.0 × 1.195 = 11.95 Ω."])
mcq(3,1.2,"A tungsten bulb filament is cold. At the instant it is switched on, compared with normal glow, the current is:",["much larger","much smaller","the same","zero"],"Hot metal has more resistance, so cold filament resistance is low.",["Cold filament: low R.","I = V/R is large at first.","Current then falls as it warms."])
num(3,1.3,"A bulb draws 0.50 A at 120 V when glowing. Its cold resistance is 20 Ω. What is the switch-on current in amperes?",6,"A","Use the cold R.",["I = 120 ÷ 20 = 6.0 A.","Glowing: 240 Ω; cold much less."])
mcq(3,1.0,"Current enters a bulb at 2.0 A. The current leaving the bulb is:",["2.0 A","less than 2.0 A, since the bulb uses it","0 A","more than 2.0 A"],"Charge is not used up; energy is.",["Charge conservation.","The bulb converts energy, not current.","Same current out."])
num(3,1.3,"A power line carries 1.0 MW at 10 kV through wires of total resistance 2.0 Ω. Power lost in the wires, in kW? (I = P/V)",20,"kW","Find I first, then I²R.",["I = 1.0×10⁶ ÷ 10⁴ = 100 A.","Loss = 100² × 2.0 = 20 000 W = 20 kW."])
num(3,1.8,"The same line now sends 1.0 MW at 100 kV (10 times higher voltage), same 2.0 Ω wires. Power lost, in kW?",0.2,"kW","Current falls 10×, loss falls 100×.",["I = 10 A.","Loss = 10² × 2.0 = 200 W = 0.2 kW."])
num(3,1.6,"Two 100 Ω, ¼ W resistors are in series. What is the largest supply voltage that keeps both within their rating, in volts?",10,"V","Same current; each limited to 50 mA.",["Imax = √(0.25/100) = 0.050 A.","Total R = 200 Ω.","V = 0.050 × 200 = 10 V."])
num(3,1.7,"Two 100 Ω, ¼ W resistors are in parallel. Largest supply voltage within ratings, in volts?",5,"V","Same voltage; each limited by V = √(PR).",["V = √(0.25 × 100) = 5 V.","Each resistor carries 50 mA at that point."])
num(2,0.6,"A 1.0 kΩ, ¼ W resistor. What is the largest voltage across it, in volts? One decimal.",15.8,"V","V = √(PR).",["√(0.25 × 1000) = √250 = 15.8 V."])
num(3,1.0,"A 15 A breaker protects a 120 V circuit. What is the largest total power it allows, in watts?",1800,"W","P = V·I.",["120 × 15 = 1800 W.","A 1500 W heater plus 800 W toaster draws 19 A and trips it."])
mcq(3,1.0,"A 120 V, 15 A circuit runs a 1500 W heater and an 800 W toaster. What happens?",["The breaker trips; the total is 19 A","It runs; each appliance has its own 15 A","It runs; current adds only in series","The heater slows down"],"Appliances share the circuit, so their currents add.",["2300 W ÷ 120 V = 19.2 A.","19.2 A > 15 A.","Trap: thinking each device has a separate limit."])
num(3,1.2,"A kettle heats 1.0 kg of water from 20 °C to 100 °C. Water: 4186 J/(kg·°C). How many joules?",334880,"J","Q = mcΔT.",["ΔT = 80 °C.","1.0 × 4186 × 80 = 334 880 J."],0.02)
num(3,1.6,"A 1500 W kettle is 80% efficient and heats 1.0 kg of water by 80 °C (4186 J/(kg·°C)). Time needed in seconds?",279,"s","Useful power is 80% of input.",["Heat needed 334 880 J.","Useful power = 1200 W.","t = 334 880 ÷ 1200 = 279 s."],0.02)
num(3,1.3,"A motor is 80% efficient and drives a gearbox that is 90% efficient. Overall efficiency, as a percent?",72,"%","Multiply the efficiencies.",["0.80 × 0.90 = 0.72.","Not an average."],0.01)
num(2,0.5,"An LED driver takes in 5.0 W and gives out 3.5 W of light, wasting 1.5 W as heat. Efficiency in percent?",70,"%","Efficiency = useful ÷ input.",["3.5 ÷ 5.0 = 0.70.","Heat is the waste."],0.01)
num(3,1.2,"A 1.5 A current flows for 2.0 minutes. About how many electrons pass a point? (e = 1.60×10⁻¹⁹ C) Answer in scientific notation, e.g. 1.1e21.",1.125e21,"electrons","Q = It, then Q ÷ e.",["Q = 1.5 × 120 = 180 C.","180 ÷ 1.60×10⁻¹⁹ = 1.1×10²¹."],0.03)
num(2,0.3,"A 1.0 A current is how many electrons per second? (e = 1.60×10⁻¹⁹ C), e.g. 6.2e18.",6.25e18,"electrons/s","1 A = 1 C/s.",["1 ÷ 1.60×10⁻¹⁹ = 6.25×10¹⁸."],0.03)
mcq(3,1.1,"Table: V = 2, 4, 6 V gives I = 0.10, 0.18, 0.24 A. What does it show?",["Resistance rises with voltage, so not ohmic","An ohmic 20 Ω resistor","Resistance falls with voltage, so not ohmic","An ohmic 25 Ω resistor"],"V ÷ I = 20, 22, 25 Ω. An ohmic part has constant R.",["Compute V/I for each row.","20, 22.2, 25 Ω: it changes.","Trap: using only the first row."])
order(3,1.0,"Order these same-length wires by resistance, lowest first.",["silver, 2.0 mm²","copper, 1.0 mm²","aluminum, 1.0 mm²","copper, 0.50 mm²"],"R ∝ ρ/A. Compare ρ ÷ area.",["Silver: 1.59/2 = 0.80.","Copper 1.0: 1.68.","Aluminum 1.0: 2.65.","Copper 0.5: 3.36."])
order(3,1.2,"Order by energy, smallest first.",["1.0 kW for 5 min","100 W for 1 h","3600 kJ","60 W for 24 h"],"Convert all to kWh.",["1 kW × 1/12 h = 0.083 kWh.","0.1 kWh.","3600 kJ = 1.0 kWh.","0.06 × 24 = 1.44 kWh."])
multi(2,0.4,"Select ALL changes that raise a wire's resistance.",["Make it longer","Make it thinner","Heat it up (metal)","Swap copper for gold","Make it thicker"],[0,1,2,3],"R = ρL/A, and hotter metal has more R. Gold ρ (2.44) is above copper (1.68).",["Longer: more R.","Thinner: more R.","Hotter metal: more R.","Gold ρ > copper ρ.","Thicker lowers R."])
num(3,1.1,"A 30 m copper cable (1.5 mm²) feeds a load, so current travels 60 m in total out and back. It carries 10 A. Voltage lost in the cable, in volts? (ρ = 1.68×10⁻⁸ Ω·m)",6.72,"V","Find R of the full loop, then V = IR.",["R = 1.68×10⁻⁸ × 60 ÷ 1.5×10⁻⁶ = 0.672 Ω.","V = 10 × 0.672 = 6.72 V.","Trap: using only 30 m."])
num(3,1.3,"A 10 Ω and a 40 Ω resistor are in series across 20 V. Power in the 40 Ω resistor, in watts?",6.4,"W","Series current first.",["I = 20 ÷ 50 = 0.40 A.","P = 0.40² × 40 = 6.4 W.","Trap: using the full 20 V across it."])
mcq(3,1.2,"A 10 Ω and a 40 Ω resistor are each connected alone across the same 20 V. Which dissipates more power?",["10 Ω: 40 W against 10 W","40 Ω: higher R means more heat","Both equal","Neither: voltage is the same"],"With fixed voltage, P = V²/R, so smaller R gives more power.",["10 Ω: 400/10 = 40 W.","40 Ω: 400/40 = 10 W.","Opposite rule holds with fixed current."])
num(3,1.0,"A converter that is 85% efficient runs a 2.5 W device from a 9.25 Wh battery. Battery input power is 2.5 ÷ 0.85. Run time in hours?",3.145,"h","Battery supplies more than the device uses.",["Input power = 2.94 W.","t = 9.25 ÷ 2.94 = 3.15 h."],0.02)
num(2,0.5,"A 5.0 V charger outputs 2.0 A and is 85% efficient. Input power from the wall, in watts? One decimal.",11.8,"W","Input = output ÷ efficiency.",["Output = 10 W.","10 ÷ 0.85 = 11.8 W."])
num(2,0.5,"A 24 Ω heater carries 0.50 A for 10 minutes. Energy in joules?",3600,"J","P = I²R, then E = Pt with t in seconds.",["P = 0.25 × 24 = 6.0 W.","t = 600 s.","E = 3600 J."])
mcq(2,0.3,"The kilowatt-hour on your electric bill is a unit of:",["energy","power","charge","current"],"kW × h = power × time = energy.",["Power × time is energy.","Trap: kilowatt alone is power."])
mcq(3,1.0,"Current through a fixed resistor doubles. Compared with before, the heat per second is:",["4 times","2 times","½","unchanged"],"P = I²R.",["I × 2 → I² × 4.","Trap: thinking P doubles with I."])

def N(v,u,tol=0.02): return {"v":v,"tol":tol,"u":u}
fix={
"virpe-007":{"num":N(50,"mA"),"l":2,"b":0.4},
"virpe-008":{"l":2,"b":0.4},
"virpe-015":{"l":2,"b":0.3},
"virpe-016":{"l":2,"b":0.6},
"virpe-023":{"num":N(5.556,"h",0.01)},
"virpe-028":{"num":N(20,"mA")},
"virpe-031":{"num":N(0.30,"kWh")},
"virpe-033":{"num":N(84,"Wh")},
"virpe-034":{"num":N(1.54,"h")},
"virpe-128":{"num":N(2.4,"mA")},"virpe-129":{"num":N(4,"mA")},"virpe-130":{"num":N(3,"mA")},
}
keep={151,159,166,172,186,234}
dele=[f"virpe-{i:03d}" for i in list(range(43,46))+list(range(263,266))+list(range(342,345))+[i for i in range(148,258) if i not in keep]]
fam=["X resistor of # Ω has # X across it. What current flows?","# X is across a # kΩ resistor. Current?","X resistor has # X across it with # X flowing through it. It","X # Ω resistor carries # X. The power dissipated is:"]
rep=("Found numeric-key errors (wrong units/scale): 007 (0.05 mA should be 50 mA), 028 (0.02 mA -> 20 mA), 031 (1080000 kWh -> 0.30), 033 (302400 Wh -> 84), 034 (5544 h -> 1.54), 128-130 (family of kΩ current: key in A but unit mA; family likely wrong, deleted via del_family header text, ids 128-130 fixed anyway), 023 (tol 0.5 pct too tight for 5.556). Re-leveled 007,008,015,016 from 3 to 2. Deleted ~100 near-identical resistor color-code items (kept 6 plus 017/018) and 3 duplicate trivial families (043 I=V/R, 263 R=V/I, 342 P=I2R; del ids + del_family by header text since fp keys not visible). Added %d questions, about half level 3: wire stretching/folding, series/parallel power ratings, transmission loss, cold filament, breaker, efficiency chains, resistivity, temperature coefficient. Doubts: del_family keys are header strings, caller should resolve to fp; cold-resistance q assumes metal filament; study note says '1/4 W 100 ohm' which is fine.")
rep=rep.replace("%d",str(len(new)))
json.dump({"fix":fix,"del":dele,"del_family":fam,"new":new,"report":rep},open(OUT,"w"),ensure_ascii=False,indent=0)
print(len(new),sum(q["l"]==3 for q in new),len(dele))
