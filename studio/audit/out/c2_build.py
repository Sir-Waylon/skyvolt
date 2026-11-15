import json, math
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/c2.json"
new=[]; n=[0]
def fp():
    n[0]+=1; return f"c2_{n[0]:03d}"
def mcq(t,l,b,q,o,w,sol): new.append(dict(t=t,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(t,l,b,q,o,a,w,sol): new.append(dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(t,l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=round(v,4),tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(t,l,b,q,text,w,sol): new.append(dict(t=t,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(t,l,b,q,items,w,sol): new.append(dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(t,l,b,q,pairs,w,sol): new.append(dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))
D="dcac"; C="ctrl"; H="hands"
s2=math.sqrt(2)
# ================= DCAC =================
num(D,1,-1,"A signal repeats 10 times every second (10 Hz). How long does one cycle take, in milliseconds?",100,"ms",
 "Period is the time for one cycle, the flip side of frequency.",["Period T = 1 ÷ f.","T = 1 ÷ 10 = 0.1 s.","0.1 s = 100 ms (multiply seconds by 1000)."])
num(D,1,-0.8,"A signal has a frequency of 25 Hz. Find its period in milliseconds.",40,"ms",
 "T = 1/f, then convert seconds to ms.",["T = 1 ÷ 25 = 0.04 s.","Multiply by 1000 to change seconds to milliseconds: 40 ms.","Common slip: leaving the answer in seconds."])
num(D,1,-0.8,"A signal has a frequency of 60 Hz. Find its period in milliseconds.",1000/60,"ms",
 "T = 1/f; US mains cycle takes about 16.7 ms.",["T = 1 ÷ 60 s = 0.01667 s.","In ms: 16.7 ms.","Memory hook: 60 Hz is about 16.7 ms, 50 Hz is exactly 20 ms."])
num(D,2,0,"An oscilloscope shows one full cycle lasting 8 ms. What is the frequency in hertz?",125,"Hz",
 "Frequency is 1 divided by period, so a short period means a high frequency.",["f = 1 ÷ T.","Change 8 ms to 0.008 s.","f = 1 ÷ 0.008 = 125 Hz."])
txt(D,1,-0.8,"What is the unit of frequency? (one word)",["hertz","hz","Hz"],
 "Hertz means cycles per second.",["Frequency counts cycles each second.","One cycle per second is 1 hertz (Hz)."])
num(D,2,0,"A sine wave has a peak voltage of 170 V. What is its peak-to-peak voltage?",340,"V",
 "Peak-to-peak spans from the top peak to the bottom peak, so it is twice the peak.",["Peak is measured from zero to the top.","Peak-to-peak goes from −170 V to +170 V.","170 + 170 = 340 V."])
num(D,2,0,"Wall power is 120 V RMS. What is its peak voltage? Give your answer to the nearest volt.",120*s2,"V",
 "Peak is about 1.414 times the RMS value.",["RMS is the DC-equivalent heating value, always smaller than the peak.","V_peak = V_rms × √2.","120 × 1.414 ≈ 170 V."])
num(D,3,1.0,"A 12 Ω heating element runs on 120 V RMS. How much power does it use?",120**2/12,"W",
 "RMS voltage works in P = V²/R just like DC voltage.",["RMS was defined to give the same heating as DC.","So use P = V²/R with V = 120 V.","P = 14400 ÷ 12 = 1200 W. Do not use 170 V peak here."])
num(D,3,1.0,"On an oscilloscope a sine wave goes from +8 V to −8 V (16 V peak-to-peak). Find its RMS voltage.",8/s2,"V",
 "Convert peak-to-peak to peak first, then divide by √2.",["Peak-to-peak 16 V means peak = 16 ÷ 2 = 8 V.","V_rms = V_peak ÷ √2.","8 ÷ 1.414 = 5.66 V. Common error: dividing 16 by √2."])
num(D,3,1.3,"An oscilloscope is set to 2 ms per division. One full cycle spans 5 divisions. Find the frequency in hertz.",100,"Hz",
 "Time per cycle = divisions × time per division; frequency is its inverse.",["Period = 5 × 2 ms = 10 ms = 0.010 s.","f = 1 ÷ T.","1 ÷ 0.010 = 100 Hz."])
num(D,3,1.5,"A sine voltage with a 12 V peak is applied to a 6 Ω resistor. What is the average power? (Use RMS.)",(12/s2)**2/6,"W",
 "Average power uses RMS, not peak, because the voltage spends time near zero.",["V_rms = 12 ÷ √2 = 8.49 V.","P = V_rms² ÷ R = 72 ÷ 6 = 12 W.","Using the peak gives 24 W, twice too big, because the peak only lasts an instant."])
num(D,3,1.8,"An ideal transformer steps 120 V down to 12 V. The 12 V side supplies a 5 A load. What current flows in the 120 V side?",0.5,"A",
 "An ideal transformer passes power through unchanged: lower voltage means higher current on that side.",["Secondary power = 12 V × 5 A = 60 W.","Ideal means input power = output power = 60 W.","I = P ÷ V = 60 ÷ 120 = 0.5 A."])
num(D,2,0,"A transformer has 100 turns on its primary and 500 turns on its secondary. The primary gets 120 V AC. What is the secondary voltage?",600,"V",
 "Voltage is proportional to turns, so more secondary turns steps voltage up.",["Voltage ratio = turns ratio = 500 ÷ 100 = 5.","120 V × 5 = 600 V.","Transformers only work on AC, because a changing field is needed."])
mcq(D,3,1.4,"Which quantity does an ideal transformer NOT change between its input and output?",
 ["The frequency of the AC","The voltage","The current","The number of turns"],
 "The magnetic field alternates at the supply frequency, so the output cycles at the same rate.",["A transformer changes voltage and current in opposite directions.","The magnetic field in the core is driven by the input AC, so output repeats at the same rate.","60 Hz in means 60 Hz out."])
num(D,3,1.0,"A power line must deliver 10 kW. The line wires total 2 Ω. If it is sent at 2000 V, how many watts are lost heating the wires?",50,"W",
 "Find the line current first, then use I²R.",["I = P ÷ V = 10000 ÷ 2000 = 5 A.","Loss = I²R = 25 × 2 = 50 W.","At 200 V the current would be 50 A and loss would be 5000 W, half the power."])
mcq(D,3,1.0,"A 12 V DC source and an AC source with 12 V RMS are each connected to identical resistors. Compared with the DC resistor, the AC resistor gets:",
 ["The same average heating","About 1.4 times more heating","About half the heating","No heating, because AC reverses"],
 "RMS is defined so that it gives the same average heating as DC of that voltage.",["RMS = the DC value that heats equally.","Current direction does not matter for heating, since I²R is always positive.","So 12 V RMS AC heats like 12 V DC."])
mcq(D,2,0,"A meter set to AC volts is placed between the hot slot and the neutral slot of a working US outlet. It reads about:",
 ["120 V","0 V","60 V","170 V"],
 "Hot-to-neutral is the full supply, shown as the RMS value.",["The hot wire swings about the neutral voltage.","A meter reads RMS by default: about 120 V.","170 V is the peak, which a normal meter does not display."])
mcq(D,3,0.9,"A lamp switch is wired into the hot wire rather than the neutral wire. Why is this safer?",
 ["With the switch off, the lamp socket is not at 120 V","Hot wires carry no current","It makes the lamp brighter","It turns the AC into DC"],
 "A switch in the hot leg removes the 120 V from everything after it.",["Neutral is near 0 V; hot is the live one.","If the switch opened the neutral, the lamp would still be connected to hot.","Someone touching the socket could then be shocked."])
mcq(D,3,1.0,"A frayed hot wire touches the metal case of a toaster, which has a ground wire. What does the ground wire do?",
 ["Gives the fault a low-resistance path so the breaker trips","Lowers the case voltage by raising resistance","Converts the AC to DC","Carries the toaster's normal current back"],
 "Ground is only a safety path. It makes a big fault current so the breaker opens fast.",["The hot wire shorts to the case.","Case is bonded to ground, so a large current flows and the breaker trips.","Normal return current goes in the neutral wire, not ground."])
txt(D,2,0,"How many diodes does a full-wave bridge rectifier use? (number)",["4","four"],
 "A bridge uses four diodes so both halves of the AC cycle give current in one direction.",["Two diodes conduct on each half cycle.","Four are arranged in a diamond (bridge)."])
num(D,3,1.0,"A US full-wave rectifier works on 60 Hz mains. How many output pulses are produced each second?",120,"pulses/s",
 "A full-wave rectifier flips the negative half cycles, so it gives two pulses per cycle.",["Each AC cycle has one positive and one negative half.","Full-wave uses both halves.","2 × 60 = 120 pulses per second (a half-wave gives 60)."])
num(D,2,0.3,"Dry skin may have a resistance near 100 kΩ. How much current flows if 120 V is placed across it?",1.2,"mA",
 "Use Ohm's law. Notice how small the current is when resistance is high.",["I = V ÷ R = 120 ÷ 100000.","I = 0.0012 A = 1.2 mA.","That is only just felt. Wet skin has far lower resistance, so the current is much greater."])
num(D,3,1.2,"Assume wet hands give a body resistance of 1500 Ω. How much current flows from 120 V through the body? Answer in mA.",80,"mA",
 "Wet skin means low resistance, so the same voltage pushes a dangerous current.",["I = V ÷ R = 120 ÷ 1500 = 0.08 A.","That is 80 mA.","Over 100 mA across the chest can cause fibrillation, so 80 mA is in the danger zone. Voltage is the push; current does the harm."])
num(D,2,0,"Four lemon cells (copper and steel) are connected in series. Each gives about 0.7 V. What is the total voltage?",2.8,"V",
 "Series cells add their voltages.",["Each cell is a copper plate, a steel plate and acid juice.","Series: add the voltages.","4 × 0.7 = 2.8 V."])
mcq(D,2,0,"Why does a lemon with a copper strip and a steel strip make a voltage?",
 ["Two different metals in an electrolyte react differently","The lemon is a tiny AC generator","The lemon stores charge like a capacitor","Copper and steel are both magnets"],
 "A battery needs two unlike metals and a conducting liquid.",["The acid juice is the electrolyte.","The two metals react differently with it, so one gains electrons and one loses them.","Two strips of the same metal would give about 0 V."])
num(D,2,0.2,"Two 1.5 V AA cells, each rated 2000 mAh, are connected in parallel. What is the total capacity in mAh?",4000,"mAh",
 "Parallel cells share the load, so capacity adds but voltage stays the same.",["Parallel: voltage stays 1.5 V.","Each cell supplies half the current, so the pack lasts twice as long.","2000 + 2000 = 4000 mAh."])
mcq(D,3,1.0,"Two parallel strings each have three 1.5 V, 2000 mAh cells in series. The strings are joined in parallel. The pack is:",
 ["4.5 V and 4000 mAh","9 V and 4000 mAh","4.5 V and 2000 mAh","3 V and 6000 mAh"],
 "Series adds voltage. Parallel adds capacity.",["One string: 3 × 1.5 = 4.5 V, 2000 mAh.","Two identical strings in parallel: voltage stays 4.5 V, capacity doubles to 4000 mAh.","Do the series step and the parallel step separately."])
num(D,2,0,"A 9 V battery holds 500 mAh. A circuit draws a steady 25 mA. About how many hours will the battery last?",20,"h",
 "Capacity in mAh divided by current in mA gives hours.",["mAh is current × time.","Time = 500 mAh ÷ 25 mA.","= 20 h."])
num(D,2,0.3,"A 3.0 V battery holds 2000 mAh. How much energy is stored? Answer in watt-hours.",6,"Wh",
 "Energy in Wh = volts × amp-hours.",["Change 2000 mAh to 2.0 Ah.","E = V × Ah = 3.0 × 2.0.","= 6 Wh."])
num(D,3,1.3,"A 1000 W heater made for 230 V is plugged into 120 V instead. Assuming its resistance stays the same, about how much power does it use?",1000*(120/230)**2,"W",
 "For a fixed resistance, power goes with voltage squared.",["Find R: R = V²÷P = 230² ÷ 1000 = 52.9 Ω.","New P = 120² ÷ 52.9.","P ≈ 272 W. Halving voltage cuts power to one quarter."])
num(D,3,1.8,"A 120 V RMS, 60 Hz outlet has v = 170 sin(2π·60·t). What is the instantaneous voltage at t = 2.0 ms? Give your answer in volts.",170*math.sin(2*math.pi*60*0.002),"V",
 "Put the time into the sine formula, with the angle in radians.",["Angle = 2π × 60 × 0.002 = 0.754 rad (43°).","sin(0.754) = 0.685.","v = 170 × 0.685 ≈ 116 V. The wave is not at its peak yet."],tol=0.03)
num(D,3,1.3,"A 50 Hz sine wave crosses zero going up at t = 0. When does it first reach its peak? Answer in ms.",5,"ms",
 "The peak comes a quarter of a period after the zero crossing.",["Period = 1 ÷ 50 = 20 ms.","Zero to peak is one quarter of the cycle.","20 ÷ 4 = 5 ms."])
mcq(D,3,1.7,"A 10 V peak sine wave and a 10 V DC source are connected to identical resistors. The AC resistor's average power compared with the DC one is:",
 ["One half","The same","Twice as much","About 0.7 times as much"],
 "RMS of the AC is 10 ÷ √2 ≈ 7.07 V, and power goes with V².",["V_rms = 7.07 V.","Power ∝ V², so (7.07 ÷ 10)² = 0.5.","The 0.7 option is the voltage ratio, not the power ratio."])
multi(D,2,0.2,"Select ALL statements that are true about AC power in a US home.",
 ["The voltage reverses direction 120 times each second","Transformers can step the voltage up or down","The 120 V rating is an RMS value","The current always flows one way","The neutral wire is the dangerous live wire"],[0,1,2],
 "60 Hz means 60 full cycles a second, and each cycle reverses twice.",["Each cycle has two reversals: 60 × 2 = 120 per second.","Transformers need changing current, so they work on AC.","Neutral is near 0 V; hot is the live wire."])
order(D,2,0,"Put these in order for electric power going from a power plant to a wall outlet.",
 ["Generator","Step-up transformer","High-voltage transmission lines","Step-down transformer","Wall outlet"],
 "Power is stepped up for the long trip and stepped down for safe use.",["The generator makes the AC.","Step up the voltage so current and I²R loss are small.","Step down near the home to 120 V."])
match(D,1,-0.5,"Match each wire in a US outlet to its job.",
 [["Hot","carries about 120 V RMS"],["Neutral","normal return path, about 0 V"],["Ground","fault safety path only"]],
 "Each wire has a different role.",["Hot is the live one.","Neutral completes the circuit.","Ground gives faults a path and does nothing in normal use."])
mcq(D,1,-0.5,"A car battery with liquid acid inside is called a:",
 ["Wet cell","Dry cell","Solar cell","Rectifier"],
 "A wet cell uses a liquid electrolyte.",["Lead-acid car batteries contain liquid.","Dry cells use paste, such as alkaline AA cells."])
num(D,1,-0.5,"A 60 W bulb runs on 120 V. How much current does it draw?",0.5,"A",
 "Use I = P ÷ V.",["Power = voltage × current.","I = 60 ÷ 120 = 0.5 A."])
mcq(D,2,0.4,"Which is a typical reason AC is used for the power grid instead of DC?",
 ["Transformers can easily change AC voltage","AC needs no wires","AC does not heat the wires","AC has no frequency"],
 "Transformers only work with changing current, and they let us pick the best voltage for each job.",["High voltage cuts line current and loss.","Low voltage is safer in the home.","Transformers do both easily with AC."])

# ================= CTRL =================
mcq(C,1,-1,"Which switch simply makes or breaks one path, with one pole and one throw?",
 ["SPST","SPDT","DPDT","Relay"],
 "SPST is the plain on/off switch.",["S = single pole, T = throw.","One moving contact and one path: SPST."])
num(C,1,-0.5,"How many terminals does a standard SPDT switch have?",3,"terminals",
 "One common terminal plus two outputs.",["Single pole: one common.","Double throw: two positions, each with an output terminal.","1 + 2 = 3."])
num(C,2,0,"How many terminals does a standard DPDT switch have?",6,"terminals",
 "A DPDT is two SPDT switches moved by one handle.",["Each pole has one common and two outputs (3 terminals).","Two poles give 2 × 3 = 6."])
mcq(C,2,0,"A small 5 V signal needs to turn on a 120 V lamp. Which device lets the small signal control the lamp while keeping the circuits separate?",
 ["Relay","Fuse","GFCI","SPST switch only"],
 "A relay uses a coil to move contacts, so the control side and load side are not connected.",["The coil is the small control circuit.","The magnetic field closes contacts in the separate lamp circuit.","A fuse only protects and a GFCI only detects leaks."])
mcq(C,3,1.5,"A diode is put across a relay coil to stop a voltage spike when the coil is switched off. How should it be connected?",
 ["Cathode (stripe) to the positive side of the coil","Anode (plain end) to the positive side of the coil","In series with the coil, forward biased","Across the contacts instead of the coil"],
 "The diode must be reverse-biased during normal operation so it only conducts during the spike.",["During normal use the supply pushes current through the coil, so the diode should block.","When the switch opens the collapsing field reverses the coil voltage.","Then the diode conducts and absorbs the energy. The stripe (cathode) goes to the + side."])
mcq(C,3,1.2,"Why does a relay coil make a high-voltage spike when its current is switched off?",
 ["The collapsing magnetic field forces the current to keep flowing","The contacts store electric charge","The supply voltage doubles","The diode adds voltage"],
 "A coil resists a change in current. Cutting power makes its field collapse and induces a voltage.",["A coil stores energy in its magnetic field.","Cutting the current quickly makes the field collapse quickly.","The fast collapse induces a large voltage that can damage a transistor or switch."])
mcq(C,2,0.2,"A lamp is wired through the normally closed (NC) contact of a relay. What happens when the coil is energized?",
 ["The lamp turns off","The lamp turns on","The lamp stays on","The coil melts"],
 "Energizing the coil moves the common contact from NC to NO.",["At rest, NC touches the common, so the lamp is on.","Coil power pulls the armature away from NC.","The circuit through NC opens and the lamp goes off."])
num(C,2,0,"A relay coil has a resistance of 300 Ω and is powered by 12 V. How much coil current flows, in mA?",40,"mA",
 "The coil is just a resistor as far as DC current goes.",["I = V ÷ R = 12 ÷ 300 = 0.04 A.","= 40 mA."])
mcq(C,3,1.0,"A relay has contacts rated 10 A at 120 V. Which load can it safely switch?",
 ["A 1000 W heater","A 1500 W heater","A 1800 W heater","A 2400 W heater"],
 "Compare each load's current (P ÷ V) with the 10 A contact rating.",["1000 W ÷ 120 V = 8.3 A, which is under 10 A.","1500 W gives 12.5 A, 1800 W gives 15 A and 2400 W gives 20 A.","Those would overheat or weld the contacts."])
mcq(C,3,1.4,"A microcontroller pin can supply only about 20 mA, but a relay coil needs 70 mA. What is the usual fix?",
 ["Use a transistor to drive the coil","Connect the coil directly to the pin","Put a fuse in series with the pin","Use a bigger diode across the pin"],
 "The pin controls a transistor, and the transistor carries the larger coil current.",["70 mA is more than the pin can give.","A small current into the transistor's base lets it switch the larger coil current.","The flyback diode still goes across the coil."])
num(C,2,0.2,"A 1200 W hair dryer runs on 120 V. Which is the smallest standard fuse (5, 10, 15, 20 A) that will not blow? Answer in amps.",10,"A",
 "Find the current, then pick a rating at or above it.",["I = 1200 ÷ 120 = 10 A.","A fuse rated exactly 10 A is enough in this question's rule: at or above.","(Real installs often leave extra margin, but use the rule given.)"],tol=0)
num(C,2,0.4,"A 300 W load runs on 12 V. Which is the smallest standard fuse (10, 20, 25, 30, 40 A) that will not blow? Answer in amps.",25,"A",
 "The current is much bigger at low voltage.",["I = 300 ÷ 12 = 25 A.","25 A is available, so choose 25 A (at or above 25).","Low-voltage circuits need high current for the same power."],tol=0)
mcq(C,3,1.0,"A circuit uses 14 AWG wire, which is rated for 15 A. A person swaps the 15 A fuse for a 30 A fuse. What is the danger?",
 ["The wire can overheat without the fuse blowing","The fuse will blow more often","The voltage will double","The load will get less current"],
 "A fuse protects the wire. A fuse that is too big lets too much current flow.",["The wire gets hot when current is above its rating.","A 30 A fuse still carries 20 A without blowing.","The wire insulation could melt and cause a fire."])
num(C,2,0.4,"A 1000 W heater, an 800 W toaster and 400 W of lamps all run on one 120 V circuit. What is the total current in amps?",2200/120,"A",
 "Loads in parallel add their currents, which is the same as adding their power.",["Total power = 1000 + 800 + 400 = 2200 W.","I = P ÷ V = 2200 ÷ 120.","≈ 18.3 A. That trips a 15 A breaker."])
mcq(C,2,0.3,"Why does plugging more appliances into one outlet circuit make the breaker more likely to trip?",
 ["Appliances are in parallel, so their currents add","Appliances are in series, so their voltages add","More appliances lower the voltage","The breaker rating drops"],
 "Home loads are connected in parallel across 120 V, so each draws its own current.",["Each appliance adds its own current.","The total current in the wire is the sum.","When the sum goes above the breaker rating, it trips."])
mcq(C,3,1.2,"A GFCI sees 8.020 A leaving on the hot wire and 8.000 A returning on the neutral. What happens?",
 ["The GFCI trips","Nothing, because the current is under 15 A","The breaker trips first","The GFCI trips only if the difference is over 1 A"],
 "A GFCI compares outgoing and returning current. A 20 mA gap means current is leaking somewhere else.",["Difference = 8.020 − 8.000 = 0.020 A = 20 mA.","A GFCI trips at about 5 mA of difference.","The missing current may be going through a person."])
mcq(C,1,-0.5,"Where do building codes require GFCI protection?",
 ["Near water, such as bathrooms and outdoors","Only in bedrooms","Only on lamps","Only on 240 V circuits"],
 "Wet places raise the chance of current passing through a person to ground.",["Water lowers body resistance.","GFCIs cut the power within milliseconds of a leak.","So they are used by sinks, bathrooms, outdoors."])
num(C,2,0.5,"A person with wet skin (about 2000 Ω) touches a 120 V hot wire and ground. How much current flows, in mA?",60,"mA",
 "Use Ohm's law for the body path.",["I = 120 ÷ 2000 = 0.060 A.","= 60 mA.","A GFCI would trip at 5 mA; a 15 A breaker would not trip at all."])
mcq(C,2,0.5,"A three-way circuit has the lamp ON. You flip switch A, then switch B, then switch A again. The lamp is now:",
 ["Off","On","Dim","Depends on the order"],
 "Every flip of either switch changes the lamp state.",["Start on.","Flip A: off. Flip B: on. Flip A: off.","Three flips (an odd number) leave it changed from the start: off."])
mcq(C,3,1.8,"To control one hallway lamp from THREE places, which switch set is correct?",
 ["Two SPDT switches at the ends and one DPDT wired as a crossover in the middle","Three SPST switches in series","Three SPDT switches in parallel","Two DPDT switches at the ends only"],
 "The middle switch must swap the two traveler wires, which is a DPDT wired crossed.",["End switches are SPDT (3-way).","The middle one swaps which traveler goes where, so it is a DPDT wired crossed.","Each flip then still toggles the lamp."])
mcq(C,2,0.5,"A lamp should light only when a door switch AND a key switch are both closed. How should they be wired?",
 ["In series","In parallel","In a loop around the lamp","One across the battery"],
 "Series switches give AND logic.",["Current must pass through both.","Open either, and the path breaks.","Parallel would give OR."])
mcq(C,3,1.2,"A lamp must light when (A and B) are closed, OR when C is closed. Which wiring does this?",
 ["A in series with B, and that branch in parallel with C","A, B and C all in series","A, B and C all in parallel","A in parallel with B, and that pair in series with C"],
 "Series is AND, parallel is OR.",["A and B need to both be closed: series.","Either that branch or C: parallel.","So (A series B) parallel C."])
num(C,1,-0.3,"How many separate circuits can a DPDT switch control at the same time?",2,"circuits",
 "A DPDT has two poles, which are moved together.",["Each pole is an independent moving contact.","Two poles = two circuits."])
mcq(C,2,0.2,"A circuit breaker's bimetal strip bends and trips the breaker when it is hot. Why does it bend?",
 ["The two metals expand by different amounts","The strip melts at one end","Magnetism pulls it away from the contact","The strip gets shorter"],
 "Two bonded metals expand at different rates, so the strip curves when heated.",["Overcurrent heats the strip.","One metal grows more than the other.","The curve pushes a latch that opens the contacts."])
mcq(C,3,1.2,"A breaker has both a thermal part and a magnetic part. Which statement is right?",
 ["Magnetic reacts fast to very large short-circuit current; thermal reacts slowly to small overloads","Thermal reacts fast to shorts; magnetic reacts to slow overloads","Both react only after one minute","Only the magnetic part can be reset"],
 "Big surges need an instant trip; mild overloads need time to heat the strip.",["A short circuit makes huge current in an instant, and a coil's strong field trips it at once.","A 20% overload heats the strip slowly, so it trips later.","Together they cover both cases."])
mcq(C,3,1.6,"A motor runs at 3 A but draws about 18 A for 0.2 s at startup. Which fuse is the best choice?",
 ["A 5 A slow-blow","A 5 A fast-blow","A 1 A slow-blow","A 20 A fast-blow"],
 "A slow-blow fuse ignores a brief surge but still opens on a lasting overload.",["Running current 3 A means a 5 A rating gives a small margin.","A fast-blow 5 A would open on the 18 A surge.","Slow-blow rides through 0.2 s."])
mcq(C,2,0.3,"A new fuse blows right away after replacing a blown fuse of the same rating. What is the most likely cause?",
 ["A short circuit or overload is still present","The fuse was too small, so use a bigger one","Fuses need a break-in period","The voltage is too low"],
 "A fuse is a sign, not the problem. The fault must be found and fixed.",["Blowing again means the current is still too high.","A bigger fuse would hide the problem and risk a fire.","Unplug loads and look for a short."])
order(C,2,0,"Put the steps of a relay turning on in order.",
 ["Control circuit sends current to the coil","The coil makes a magnetic field","The armature is pulled toward the coil","The contacts close","The load circuit is powered"],
 "Relays turn a small electrical signal into motion and then into a switched circuit.",["Current flows in the coil.","The field attracts the armature.","The contacts touch and the load turns on."])
match(C,2,0,"Match each term to its meaning.",
 [["Pole","a moving contact that is switched"],["Throw","a position or path the contact can reach"],["NO","open when the relay is at rest"],["NC","closed when the relay is at rest"]],
 "Switch names count poles and throws.",["Poles are the switched circuits.","Throws are the choices.","NO and NC describe the rest state."])
multi(C,2,0.2,"Select ALL devices that open a circuit when current goes above a set value.",
 ["Fuse","Circuit breaker","Relay","DPDT switch","GFCI"],[0,1],
 "Fuses and breakers respond to overcurrent.",["A relay switches by a coil signal.","A DPDT switch is moved by hand.","A GFCI responds to imbalance (leakage), not size of current."])
num(C,2,0.2,"A 15 A breaker is on a 240 V circuit. What is the largest power it can carry before it trips, in watts?",3600,"W",
 "Power = voltage × current.",["P = V × I.","240 × 15 = 3600 W."])
mcq(C,2,0.4,"A SPDT switch has its common wired to the supply, and each of the other two terminals to a different lamp. Which result is correct?",
 ["Exactly one lamp is on at a time","Both lamps are on","Both lamps are off in the middle","Both lamps are dimmed"],
 "The common connects to only one output at any time.",["The common touches either terminal 1 or terminal 2.","So current goes to one lamp.","The other lamp is off."])
mcq(C,3,1.6,"A lamp's switch is wired in the neutral wire instead of the hot wire. With the switch OFF, a person touches the metal socket thread. What is the problem?",
 ["The socket is still connected to hot and can shock","Nothing, since the lamp is off","The lamp will glow dimly","The breaker will trip"],
 "The switch must break the hot connection to make the socket safe.",["Neutral switch off leaves hot wire going to the socket.","Hot is at 120 V to ground.","A person touching it and ground gets a shock path, even though the lamp is off."])
txt(C,1,-0.5,"In what unit is a fuse rating given? (one word)",["amperes","amps","ampere","amp","A"],
 "A fuse rating is a current limit.",["Fuses melt when current is too high.","Current is in amperes (amps)."])

# ================= HANDS =================
mcq(H,1,-1,"To measure the current in a circuit, the meter is connected:",
 ["In series, so the current goes through the meter","In parallel across the part","Across the battery with no load","Only to the ground wire"],
 "An ammeter counts the charge that passes through it, so it must be in the path.",["Break the circuit at one point.","Put the meter in the gap.","In parallel, an ammeter acts like a short."])
mcq(H,1,-1,"To measure the voltage across a resistor, the meter is connected:",
 ["In parallel across the resistor","In series with the resistor","After removing the resistor","In series with the battery"],
 "A voltmeter measures the difference between two points, so touch its probes to both ends.",["Voltage is measured across a part.","The meter has very high resistance, so it barely changes the circuit."])
mcq(H,1,-0.8,"On most multimeters, the black probe goes into which jack?",
 ["COM","VΩ","10 A","mA"],
 "COM means common and is the reference for all readings.",["Black always plugs in COM.","The red probe moves between the other jacks depending on what is measured."])
num(H,1,-0.5,"A resistor has color bands brown, black, red, then gold. What is its value in ohms?",1000,"Ω",
 "The first two bands are digits, the third is the multiplier. Gold is a 5% tolerance.",["Brown = 1, black = 0.","Red = ×100.","10 × 100 = 1000 Ω (1 kΩ), ±5%."])
num(H,2,0,"A resistor has color bands yellow, violet, orange, gold. What is its value in kΩ?",47,"kΩ",
 "Digits 4 and 7, then ×1000.",["Yellow = 4, violet = 7.","Orange = ×1000.","47 × 1000 = 47000 Ω = 47 kΩ."])
num(H,2,0,"A resistor has color bands red, red, brown, gold. What is its value in ohms?",220,"Ω",
 "Red is 2 and brown multiplies by 10.",["Red red = 22.","Brown = ×10.","22 × 10 = 220 Ω."])
num(H,3,1.0,"A resistor is orange, orange, yellow, gold (5%). What is the lowest value it could really be, in kΩ?",330*0.95,"kΩ",
 "Read the nominal value, then subtract the tolerance.",["Orange orange = 33, yellow = ×10,000, so 330 kΩ.","Gold means ±5%, so the lowest is 95% of 330.","330 × 0.95 = 313.5 kΩ."])
num(H,3,0.8,"A red LED needs 15 mA and drops 2.0 V. It runs from a 9 V battery with a series resistor. What resistance is needed, in Ω?",7/0.015,"Ω",
 "The resistor must drop whatever voltage the LED does not.",["Resistor voltage = 9 − 2.0 = 7.0 V.","R = V ÷ I = 7.0 ÷ 0.015.","≈ 467 Ω. A standard 470 Ω would be used."])
mcq(H,3,1.2,"A 100 Ω resistor has 12 V across it. Which is the smallest power rating that is safe?",
 ["2 W","1/4 W","1/2 W","1 W"],
 "Heat in the resistor is P = V²/R. The rating must be above that.",["P = 12² ÷ 100 = 1.44 W.","1/4, 1/2 and 1 W resistors would overheat.","The smallest listed rating above 1.44 W is 2 W."])
num(H,2,0.3,"Two resistors, 1 kΩ and 2 kΩ, are in series with a 9 V battery. What is the voltage across the 2 kΩ resistor?",6,"V",
 "In a series circuit the voltage is shared in proportion to resistance.",["Total R = 3 kΩ.","I = 9 ÷ 3000 = 3 mA.","V = 3 mA × 2 kΩ = 6 V."])
mcq(H,2,0.5,"On a breadboard, both legs of a resistor are pushed into the same 5-hole column. What does this do?",
 ["Shorts out the resistor so it does nothing","Doubles its resistance","Makes it a diode","Makes no difference"],
 "Holes in one column are connected, so both ends of the part are the same node.",["Both leads touch the same metal strip.","Current can flow around the resistor through the strip.","A part with both ends on the same node has 0 V across it."])
mcq(H,2,0.5,"Why do ICs go across the center gap of a breadboard?",
 ["So pins on opposite sides are not connected","To make the IC cooler","To connect the sides together","To power the rails"],
 "The center gap splits the two halves, so each pin gets its own column.",["Each pin needs its own connection.","The gap isolates the two rows of pins.","Otherwise left and right pins would short."])
mcq(H,3,1.0,"A series circuit has a 9 V battery, a switch, resistor R1 and resistor R2. The lamp isn't lit. A voltmeter reads 9 V across R2 and 0 V across R1. What is the fault?",
 ["R2 is open (broken)","R1 is open","R2 is shorted","The battery is dead"],
 "In a series loop, an open part takes the whole supply voltage.",["No current flows, so there is no drop across good parts: R1 reads 0 V.","The open part has all 9 V across it.","The battery is fine, since 9 V is available."])
mcq(H,3,1.4,"Three identical bulbs are in series on a battery. A wire is then connected across one bulb (shorting it). What happens to the other two?",
 ["They get brighter","They get dimmer","They stay the same","They go out"],
 "Shorting one bulb lowers the total resistance, so the current goes up.",["Total R drops from 3R to 2R.","I = V ÷ R rises by 1.5×.","More current through the two bulbs means more brightness."])
mcq(H,3,1.7,"A voltmeter is wrongly connected in series with a lamp and a 9 V battery. What do you see?",
 ["The meter reads nearly 9 V and the lamp stays dark","The lamp is extra bright","The meter reads 0 V","The lamp glows normally"],
 "A voltmeter has a huge resistance, so it takes almost all the voltage and lets almost no current pass.",["Meter resistance is millions of ohms.","The tiny current cannot light the lamp.","Almost all of 9 V drops across the meter, so it reads almost 9 V."])
mcq(H,1,-0.5,"What is a continuity test used to check?",
 ["Whether there is a low-resistance path between two points","The voltage of a battery","The brightness of a lamp","The speed of electrons"],
 "Continuity mode beeps if the path has very low resistance.",["Turn power off first.","Touch the probes to both ends of the wire or fuse.","A beep means a good, unbroken path."])
mcq(H,2,0.2,"A meter on a resistance range shows \"OL\" (or \"1\") while measuring a resistor. This usually means:",
 ["The resistance is above the range or the path is open","The resistance is exactly zero","The battery is exactly 9 V","The meter is measuring current"],
 "OL means overload: the value is too large for that range.",["Try a higher range.","If it still shows OL, the part or wire may be open (broken)."])
num(H,1,-0.5,"A meter shows 2.2 kΩ. What is this in ohms?",2200,"Ω",
 "k (kilo) means a thousand.",["1 kΩ = 1000 Ω.","2.2 × 1000 = 2200 Ω."])
num(H,1,-0.5,"Resistors of 220 Ω, 330 Ω and 470 Ω are connected in series. What is the total resistance?",1020,"Ω",
 "Series resistances add.",["Add the three values.","220 + 330 + 470 = 1020 Ω."])
num(H,2,0.3,"Resistors of 100 Ω, 100 Ω and 50 Ω are connected in parallel. What is the total resistance?",25,"Ω",
 "Parallel adds conductances (1/R).",["1/R = 1/100 + 1/100 + 1/50 = 0.01 + 0.01 + 0.02 = 0.04.","R = 1 ÷ 0.04 = 25 Ω."])
num(H,3,0.9,"A 100 Ω resistor is in series with two 200 Ω resistors in parallel, and then a 50 Ω resistor in series. What is the total resistance?",250,"Ω",
 "Reduce the parallel part first, then add the series parts.",["200 ∥ 200 = 100 Ω.","Series: 100 + 100 + 50.","= 250 Ω."])
order(H,2,0,"Put these steps in order for measuring current safely in a powered circuit.",
 ["Turn the power off","Break the circuit at one point","Set the meter to amps and move the red lead to the current jack","Connect the meter into the gap","Turn the power on and read"],
 "A current meter must be placed in the path, so the circuit has to be opened first.",["Never open a live circuit.","Set the meter on the right range and jack before connecting.","Then power up and read."])
num(H,3,1.3,"A 9 V battery powers an unknown resistor Rx in series with a 1 kΩ resistor. The voltage across the 1 kΩ is 3 V. What is Rx, in kΩ?",2,"kΩ",
 "Find the series current, then find Rx from its share of the voltage.",["I = 3 V ÷ 1 kΩ = 3 mA.","Voltage across Rx = 9 − 3 = 6 V.","Rx = 6 ÷ 3 mA = 2 kΩ."])
num(H,3,1.5,"Two LEDs in series each drop 2.0 V. They run at 10 mA from a 9 V battery. What series resistor is needed, in Ω?",500,"Ω",
 "Subtract all the LED drops from the supply before using Ohm's law.",["LED drops: 2 × 2.0 = 4.0 V.","Resistor drop: 9 − 4 = 5 V.","R = 5 ÷ 0.010 = 500 Ω."])
mcq(H,3,1.4,"Three red LEDs (about 2.0 V each) are in series with a resistor on a 5 V supply. What happens?",
 ["They do not light, since 6 V is needed","They light brightly","One LED lights","The resistor burns"],
 "The supply must exceed the sum of the LED drops.",["3 × 2.0 V = 6.0 V.","5 V is less than 6 V.","Too little voltage for them to conduct, so no current flows."])
mcq(H,1,-0.8,"The longer leg of an LED is the:",
 ["Anode (positive side)","Cathode (negative side)","Resistor side","Ground side"],
 "LEDs only work one way: current enters the anode.",["Long leg = +.","The flat spot on the case marks the cathode."])
mcq(H,1,-0.5,"What can happen if an LED is connected straight to a battery with no resistor?",
 ["It draws too much current and burns out","It glows dimly","It becomes an AC source","Nothing; LEDs limit current themselves"],
 "An LED has almost no resistance once it conducts, so the resistor sets the current.",["Without a resistor, the current is limited only by the battery.","Too much current overheats the LED and destroys it."])
mcq(H,1,-0.5,"Before changing wires in a circuit you are building, you should first:",
 ["Disconnect the power","Touch the wires to check","Add a bigger battery","Connect the meter in series"],
 "Do changes with the power off to avoid shorts and shocks.",["Wiring changes with power on can cause shorts.","Disconnect the battery first."])
mcq(H,2,0.3,"A battery you are using becomes hot while you wire a circuit. What is the best action?",
 ["Disconnect it and look for a short","Keep going, it will cool","Add another battery in parallel","Cover it with tape"],
 "Heat means a large current, which could mean a short.",["Heat comes from high current through resistance.","A short can make a battery overheat.","Disconnect it, then fix the wiring."])
num(H,3,1.0,"A 12 V battery drives an 8 Ω resistor in series with a 16 Ω resistor. What power is used in the 8 Ω resistor, in watts?",(12/24)**2*8,"W",
 "Find the current first, then use P = I²R.",["Total R = 24 Ω.","I = 12 ÷ 24 = 0.5 A.","P = I²R = 0.25 × 8 = 2 W."])
match(H,1,-0.5,"Match each meter setting to its use.",
 [["V with a straight line","measures battery voltage (DC)"],["V with a wavy line","measures AC voltage"],["Ω","measures resistance (power off)"],["A","measures current (in series)"]],
 "Choosing the right setting is the first step of every measurement.",["Straight line means DC.","Wavy line means AC.","Ω is for resistance with the power off, A needs the meter in the path."])
multi(H,2,0.3,"Select ALL steps that are correct when measuring a resistor that is in a circuit.",
 ["Turn the power off","Lift one lead of the resistor out of the circuit","Set the meter to Ω","Leave the battery connected","Use the amps range"],[0,1,2],
 "The meter supplies its own test current, so the rest of the circuit must not interfere.",["Power off, so the battery doesn't change the reading.","Lift one leg so other parts in parallel are not measured.","Use the Ω setting."])
num(H,3,2.0,"A battery reads 9.0 V with nothing connected. With a 100 Ω load connected it reads 8.5 V. What is its internal resistance, in Ω?",0.5/0.085,"Ω",
 "The missing voltage dropped across the battery's own resistance.",["Load current = 8.5 ÷ 100 = 0.085 A.","Lost voltage = 9.0 − 8.5 = 0.5 V.","r = 0.5 ÷ 0.085 ≈ 5.9 Ω."])
num(H,1,-0.5,"A lamp has 12 V across it and 0.25 A through it. What is its resistance?",48,"Ω",
 "Use Ohm's law R = V ÷ I.",["R = 12 ÷ 0.25.","= 48 Ω."])
num(H,1,-0.5,"How many ohms are in 1 MΩ?",1000000,"Ω",
 "M (mega) means a million.",["k = 1000.","M = 1,000,000."],tol=0)

fix={
 "hands-001":{"num":{"v":1.25,"tol":0.02,"u":"kΩ"}},
 "dcac-008":{"num":{"v":20,"tol":0.02,"u":"ms"},"w":"T = 1/f; 1/50 s = 20 ms."},
 "dcac-011":{"num":{"v":2.5,"tol":0.02,"u":"ms"}},
 "hands-015":{"l":1,"b":-0.7},
 "hands-018":{"l":2,"b":0.0},
}
dele=["dcac-012","dcac-013","dcac-019","ctrl-014","hands-017","hands-019"]
delf=["per","lineloss","usb","X # X load runs on # X DC. Which fuse is the smallest that w"]
rep="""dcac: found period family (per) and dcac-008/011 had value in seconds but unit ms (wrong; fixed or deleted); lineloss family trivial (deleted); dcac-012/013 dup, dcac-019 ambiguous (deleted). ctrl: fuse family 'X..DC' lacked list so 6.25 A->7.5 A ambiguous (deleted); ctrl-014 dup. hands: hands-001 answer was 1250 with unit kOhm (fixed 1.25); usb family answers in seconds not hours (deleted); hands-017 vague, hands-019 scope claim unverified (deleted); hands-015 re-leveled to 1. Added ~35 new per topic (about half level 3). Fuse 'at or above' rule is textbook-simplified; real practice uses margin. Not web-verified: AWG 14 =15 A (NEC)."""
json.dump({"fix":fix,"del":dele,"del_family":delf,"new":new,"report":rep},open(OUT,"w"),ensure_ascii=False,indent=1)
from collections import Counter
print(len(new),Counter((q['t'],q['l']) for q in new))
for q in new:
    if q['type']=='mcq': assert len(set(q['o']))==4,q['q']
    assert len(q['q'].split())<=55,q['q']
