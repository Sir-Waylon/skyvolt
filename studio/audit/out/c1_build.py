import json, math
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/c1.json"
new=[]; n=[0]
def fp():
    n[0]+=1; return f"c1_{n[0]:03d}"
def mcq(t,l,b,q,o,w,sol): new.append(dict(t=t,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(t,l,b,q,o,a,w,sol): new.append(dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(t,l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=v,tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(t,l,b,q,text,w,sol): new.append(dict(t=t,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(t,l,b,q,items,w,sol): new.append(dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(t,l,b,q,pairs,w,sol): new.append(dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))
k=8.99e9; e=1.602e-19
H="hist"; S="static"
# ---------------- HIST ----------------
mcq(H,1,-1,"In 1820 Ørsted saw a compass needle swing when it was placed near a wire carrying current. What did this show?",
 ["A current produces a magnetic effect","Static charge on the wire pulls on iron","The wire was heating the air around the needle","Gravity from the wire bends the needle"],
 "Ørsted's compass result was the first link between electricity and magnetism.",
 ["A compass needle is a tiny magnet, so it only reacts to magnetic effects.","The needle moved only while current flowed, so the current made the magnetic effect.","Heat and static charge do not turn a compass; this was a new discovery."])
txt(H,1,-1,"Which scientist discovered in 1820 that a current deflects a compass needle? (Spell it any way you like.)",
 ["Ørsted","Oersted","Orsted","Hans Christian Ørsted","Hans Christian Oersted"],
 "Hans Christian Ørsted (also spelled Oersted) found the first electricity and magnetism link.",
 ["Compass needle = tiny magnet.","Only a magnetic effect from the wire can turn it.","Ørsted, 1820. Ampère followed within weeks."])
mcq(H,1,-1,"What could the voltaic pile of 1800 do that rubbing amber or glass could not?",
 ["Give a steady, continuous current","Give a bigger single spark","Make a magnet","Light a room with ease"],
 "Volta's pile was the first source of steady current instead of one-shot static sparks.",
 ["Friction machines gave short sparks.","A pile uses chemical reactions between metals and a wet cloth, which keep going.","A steady current is what circuits need."])
txt(H,1,-1,"Who is credited with naming the two kinds of charge positive and negative?",
 ["Franklin","Benjamin Franklin","Ben Franklin"],
 "Benjamin Franklin introduced + and − and the idea of conventional current.",
 ["Franklin studied charge in the 1700s.","He labeled the charges + and −.","His guess about flow direction is why conventional current runs + to −."])
txt(H,1,-1,"In Boole's algebra, what is 1 AND 0?",["0","zero"],
 "AND gives 1 only when every input is 1.",
 ["AND means both must be true.","Here one input is 0.","So the answer is 0."])
txt(H,1,-0.8,"In Boole's algebra, what is 1 OR 0?",["1","one"],
 "OR gives 1 when at least one input is 1.",
 ["OR means either one is enough.","One input is 1.","So the answer is 1."])
mcq(H,1,-1,"Which unit is named for the Scottish engineer James Watt?",
 ["The watt, a unit of power","The volt, a unit of potential difference","The joule, a unit of charge","The farad, a unit of energy"],
 "The watt measures power: energy per second.",
 ["Watt, volt and farad are all people's names.","The watt is the rate of using energy.","One watt = one joule per second."])
txt(H,1,-0.7,"US wall outlets supply alternating current. How many cycles per second (in Hz) does it go through?",["60","60 Hz","sixty"],
 "In the US, mains AC is 60 Hz (50 Hz in much of the world).",
 ["AC reverses direction again and again.","Hertz means cycles per second.","US power is 60 Hz."])
order(H,1,-0.8,"Put these in order, earliest first.",
 ["Coulomb's force law (1785)","Volta's pile (1800)","Faraday's induction (1831)","Hertz's radio waves (1887)"],
 "Dates: 1785, 1800, 1831, 1887.",["Coulomb is the earliest, from the 1780s.","Volta made the battery in 1800.","Faraday found induction in 1831, and Hertz made radio waves in 1887."])
mcq(H,1,-0.7,"Which pair is matched correctly with the unit named for the scientist?",
 ["Faraday: capacitance","Hertz: resistance","Ohm: frequency","Volta: current"],
 "The farad is the unit of capacitance.",["Faraday = farad = capacitance.","Hertz = frequency, Ohm = resistance, Volta = voltage.","Current is the ampere."])
mcq(H,1,-0.5,"The ancient Greek word for amber, which Thales noticed attracts light objects after rubbing, gave us which modern word?",
 ["Electricity","Magnetism","Battery","Circuit"],
 "Greek elektron means amber; rubbed amber showed static electricity.",
 ["Amber was one of the first known things to show static charge.","The Greek word elektron became 'electric'.","Magnetism comes from lodestones, a different story."])
# L2
match(H,2,0,"Match each unit to what it equals.",
 [["ampere","one coulomb per second"],["volt","one joule per coulomb"],["ohm","one volt per ampere"],["watt","one joule per second"],["farad","one coulomb per volt"]],
 "Each unit is a ratio of other quantities.",["Current is charge per time.","Voltage is energy per charge; resistance is voltage per current.","Power is energy per time; capacitance is charge per volt."])
mcq(H,2,0,"Ørsted showed that a current makes a magnetic effect. Faraday's discovery is the reverse. What is it?",
 ["A changing magnetic field can create a voltage and current","A current cannot flow in a magnet","Magnets store charge","Static charge can make a magnet"],
 "Ørsted: electricity to magnetism. Faraday: magnetism to electricity.",
 ["Faraday moved magnets near coils in 1831.","A changing magnetic field pushes charges, giving a voltage (induction).","This is how generators work."])
mcq(H,2,0,"A power-plant generator turns a magnet inside coils of wire. Whose discovery does it use?",
 ["Faraday's electromagnetic induction","Coulomb's inverse-square law","Volta's pile","Boole's algebra"],
 "Moving magnets near coils induces a voltage: induction.",
 ["Generators need a changing magnetic field through a coil.","That is Faraday's induction.","Volta's pile is a chemical battery and has no motion."])
num(H,2,0,"AC power at 60 Hz goes through how many complete cycles in 3.0 s?",180,"cycles","1 Hz = 1 cycle per second.",
 ["Cycles = frequency × time.","60 × 3.0 = 180.","A common slip is to give 60, one second's worth."])
num(H,2,0.2,"What is the period of 50 Hz AC, in milliseconds?",20,"ms","Period = 1 / frequency.",
 ["Period T = 1/f.","1/50 = 0.020 s.","0.020 s = 20 ms."])
num(H,2,0.2,"What is the period of 60 Hz AC, in milliseconds? Round to 0.1.",16.7,"ms","Period = 1 / frequency.",
 ["T = 1/f = 1/60 s.","That is 0.01667 s.","Convert to ms: 16.7 ms."])
mcq(H,2,0,"In 1937 Claude Shannon showed that Boole's algebra could describe what?",
 ["Networks of relay and switch circuits","Planetary orbits","Batteries and chemical cells","Radio antennas"],
 "Boole's 0 and 1 map onto open and closed switches.",
 ["Switch on or off is two-valued, like Boole's 0 and 1.","Shannon used Boolean algebra to design switching circuits.","This is the basis of digital logic."])
num(H,2,0,"Kirchhoff's current law: 5.0 A flows into a junction. 2.0 A leaves in one wire and 1.5 A in another. What current leaves in the third wire?",1.5,"A","Charge in equals charge out at a node.",
 ["Charge cannot pile up at a node.","Out total must be 5.0 A.","5.0 − 2.0 − 1.5 = 1.5 A."])
mcq(H,2,0,"Why did power companies choose AC for long-distance power lines?",
 ["Transformers can step the voltage up, which lowers the current and the heat loss in the wires","AC wires have no resistance","AC electrons move faster than DC electrons","DC cannot light a bulb"],
 "High voltage means low current, and low current wastes little power as heat.",
 ["Wire loss is I²R, so lower current wastes much less.","Transformers work only with changing (AC) current.","AC wires still have resistance, and DC lights bulbs fine."])
match(H,2,0,"Match each scientist to the unit named for them.",
 [["Volta","volt"],["Hertz","hertz"],["Faraday","farad"],["Coulomb","coulomb"],["Ohm","ohm"]],
 "Many SI electrical units honor these scientists.",["Volt = potential difference.","Hertz = frequency; farad = capacitance.","Coulomb = charge; ohm = resistance."])
txt(H,2,0,"Name the American scientist whose name is on the unit of inductance (the henry).",["Henry","Joseph Henry"],
 "Joseph Henry discovered induction independently of Faraday.",["Inductance is measured in henrys.","The unit honors Joseph Henry.","He found self-induction too."])
mcq(H,2,0,"Galvani saw frog legs twitch near two different metals. Volta argued the electricity came from:",
 ["the contact of the two different metals","special 'animal electricity' inside the frog","the heat of the room","a magnet nearby"],
 "Volta's view led to the pile: two metals plus an electrolyte.",
 ["Galvani thought the frog made the electricity.","Volta tested stacks of metal and found current without any animal.","That led to the first battery."])
mcq(H,2,0,"Franklin guessed that current flows from + to −. We now know that in a metal wire the moving charges are electrons. Why do we still use Franklin's 'conventional current'?",
 ["Circuit rules give the same results either way, and the convention is standard","Electrons really do flow from + to −","Protons carry current in wires","Franklin's rule makes the math work only for batteries"],
 "Conventional current is a bookkeeping choice that still works.",
 ["Electrons move from − toward +.","A positive charge moving one way acts like a negative charge moving the other way.","So the rules for V, I and R stay valid."])
txt(H,2,0,"Who discovered the electron in 1897 while studying cathode rays?",["Thomson","J. J. Thomson","JJ Thomson","Joseph John Thomson"],
 "J. J. Thomson showed cathode rays are tiny negative particles.",["Cathode rays bend in electric fields toward +.","So they carry negative charge.","Thomson named them electrons (corpuscles at first)."])
mcq(H,2,0,"In the 'war of the currents', Edison's early power stations supplied which type of electricity?",
 ["Direct current (DC)","Alternating current (AC)","Radio waves","Static electricity"],
 "Edison used DC; Tesla and Westinghouse promoted AC.",
 ["DC flows one way only.","Edison's 1880s New York system used DC.","AC won for long lines because transformers could raise voltage."])
mcq(H,2,0,"The Leyden jar of the 1740s stored charge. Which modern part does it most resemble?",
 ["A capacitor","A resistor","A diode","An inductor"],
 "Two conductors (foil inside and out) separated by glass hold charge: a capacitor.",
 ["It stored charge between two conducting layers.","That is what a capacitor does.","The farad honors Faraday."])
order(H,2,0.3,"Put these events in order, earliest first.",
 ["Ørsted's compass deflection (1820)","Faraday's induction (1831)","Kirchhoff's circuit laws (1845)","Boole's laws of thought (1854)","Hertz's radio waves (1887)"],
 "Dates: 1820, 1831, 1845, 1854, 1887.",["Ørsted and Faraday are in the first half of the 1800s.","Kirchhoff is 1845 and Boole 1854.","Hertz is last, in 1887."])
txt(H,2,0,"Which unit equals one joule per second?",["watt","watts","W"],"Power is energy per time.",["A joule is energy.","Per second gives a rate.","One joule per second is one watt."])
txt(H,2,0.2,"Which scientist's name is on the unit of magnetic flux density?",["Tesla","Nikola Tesla"],"The tesla (T) measures magnetic flux density.",["Tesla also developed AC systems.","The unit of flux density is the tesla.","It is named for Nikola Tesla."])
multi(H,2,0,"Select ALL that are SI units named for scientists.",["volt","hertz","farad","second"],[0,1,2],
 "Second is a time unit with no person's name.",["Volta, Hertz and Faraday are all honored.","The second is not named after anyone.","So volt, hertz and farad are the correct picks."])
mcq(H,2,0,"Before the voltaic pile (1800), experimenters mostly had which sources of electricity?",
 ["Friction machines and Leyden jars","Batteries and generators","Solar cells","Transformers"],
 "Only static sources existed until Volta.",["They could make sparks by rubbing.","Leyden jars stored that charge briefly.","No steady source existed until the pile."])
mcq(H,2,0,"Coulomb's law of electric force and Newton's law of gravity share which feature?",
 ["Force falls off with the square of the distance","Both forces only attract","Both depend on mass","Both are equally strong"],
 "Both are inverse-square laws, but electric force can repel and is far stronger.",
 ["Both ∝ 1/r².","Electric force depends on charge, not mass, and can push or pull.","Gravity is only attractive."])
mcq(H,2,0,"A wire with current is held over a compass. How does the needle behave?",
 ["It turns away from its north-pointing direction","It stays still because current has no magnetic effect","It spins endlessly","It points straight at the wire"],
 "Current makes a magnetic field that the compass needle follows.",
 ["The needle follows the combined field of Earth and the wire.","That moves it off north.","It does not spin or point at the wire."])
num(H,2,0,"A pile has 30 identical cells in series, each giving 0.90 V. What is the total voltage?",27,"V","Series voltages add.",
 ["Series cells stack their voltages.","30 × 0.90 V.","= 27 V."])
mcq(H,2,0,"One ohm is equal to one:",["volt per ampere","ampere per volt","coulomb per second","joule per coulomb"],
 "Ohm's law R = V/I.",["R = V ÷ I.","So ohm = volt ÷ ampere.","Coulomb per second is the ampere; joule per coulomb is the volt."])
mcq(H,2,0,"One watt is equal to one:",["volt × ampere","volt ÷ ampere","ampere ÷ volt","volt × second"],
 "Power P = V × I.",["Power = voltage × current.","That is volt × ampere.","Volt ÷ ampere is the ohm."])
# L3
num(H,3,1.0,"A 10 kW load is fed through a line with 2.0 Ω resistance at 1000 V. How many watts are lost as heat in the line?",200,"W","Current I = P/V, loss = I²R.",
 ["I = 10 000 W / 1000 V = 10 A.","Loss = I²R = 10² × 2.0.","= 200 W. Using V²/R with 1000 V would be the wrong voltage: that is the drop across the load, not the line."])
num(H,3,1.0,"Sending the same power at 10 times higher voltage cuts the line's heat loss by what factor?",100,"×","Loss = I²R and I = P/V.",
 ["10 times the voltage means 1/10 the current.","Loss ∝ I², so 1/100.","The loss is 100 times smaller."])
num(H,3,1.5,"A plant sends 50 kW through lines with total resistance 0.40 Ω at 500 V. What percent of the power is lost in the lines?",8,"%","I = 100 A, so loss = 4000 W.",
 ["I = P/V = 50 000/500 = 100 A.","Loss = I²R = 100² × 0.40 = 4000 W.","4000/50 000 = 8%."])
num(H,3,1.5,"The same plant (50 kW, 0.40 Ω line) steps up to 5000 V. How many watts are lost in the lines?",40,"W","I falls to 10 A.",
 ["I = 50 000/5000 = 10 A.","Loss = 10² × 0.40.","= 40 W, 100 times less than at 500 V."])
mcq(H,3,0.9,"A transformer is wired to a steady DC battery. After the switch is closed, the output voltage is zero. Why?",
 ["Induction needs a changing magnetic field, and steady DC gives a constant one","DC has too little voltage","Transformers only work with static charge","The primary coil has no resistance"],
 "Faraday's induction needs changing flux.",
 ["A constant current makes a constant magnetic field.","A coil only gets a voltage when the field through it changes.","AC changes all the time, so transformers use AC."])
mcq(H,3,0.8,"Which statement best contrasts Ørsted and Faraday?",
 ["Ørsted: current makes a magnetic effect. Faraday: a changing magnetic field makes a voltage","Ørsted: magnets make current. Faraday: current makes magnets","Both showed that static charge makes magnets","Both discovered the battery"],
 "They are opposite directions of the same link.",
 ["Ørsted (1820) went from electricity to magnetism.","Faraday (1831) went from magnetism to electricity.","Mixing the two is the common error."])
mcq(H,3,1.0,"A magnet is held perfectly still inside a coil connected to a meter. What current does the meter show?",
 ["Zero","A steady current proportional to the magnet's strength","A current that alternates","A current that grows with time"],
 "Induction needs change, not just a magnetic field.",
 ["Faraday found a current only while the field changes.","A still magnet means no change in flux.","So the reading is zero."])
mcq(H,3,0.9,"A magnet is pushed into a coil first slowly, then quickly. Compared with the slow push, the quick push gives:",
 ["a larger induced voltage","a smaller induced voltage","the same voltage","no voltage"],
 "Induced voltage depends on how fast the magnetic flux changes.",
 ["Faster motion = faster change.","Induced voltage grows with the rate of change.","Speed matters, not just the magnet's presence."])
num(H,3,1.4,"A magnet pushed into a coil over 0.50 s induces 0.40 V. If the same push takes 0.10 s, how many volts are induced?",2.0,"V","Induced voltage ∝ rate of change of flux (1/time).",
 ["Same flux change, 5 times faster.","So 5 times the voltage.","0.40 × 5 = 2.0 V."])
num(H,3,1.6,"A coil gives 0.40 V. Now the magnet moves twice as fast through a coil with twice as many turns. How many volts?",1.6,"V","Voltage ∝ turns × speed.",
 ["Twice the speed doubles the voltage.","Twice the turns doubles it again.","0.40 × 2 × 2 = 1.6 V."])
mcq(H,3,1.0,"Hertz's radio-wave experiments of the 1880s confirmed whose prediction?",
 ["Maxwell's electromagnetic theory","Coulomb's inverse-square law","Ohm's law","Boole's algebra"],
 "Maxwell predicted electromagnetic waves; Hertz made and detected them.",
 ["Maxwell's equations predicted waves moving at light speed.","Hertz generated them with sparks and detected them across a room.","He also showed they reflect and refract like light."])
mcq(H,3,1.0,"Hertz showed radio waves reflect, bend and polarize like light. What did this suggest about light?",
 ["Light is also an electromagnetic wave","Light is a flow of electrons in a wire","Light is a sound wave","Light is a magnetic field only"],
 "Same behavior pointed to the same kind of wave.",
 ["Radio waves are electromagnetic.","They act like light in many tests.","So light is an electromagnetic wave of higher frequency."])
num(H,3,1.0,"A radio station transmits at 100 MHz. What is the wavelength in meters? (c = 3.0×10⁸ m/s)",3.0,"m","Wavelength = c / f.",
 ["λ = c/f.","f = 100 MHz = 1.0×10⁸ Hz.","λ = 3.0×10⁸ / 1.0×10⁸ = 3.0 m."])
num(H,3,1.2,"A transmitter makes waves 0.60 m long. What is their frequency in MHz? (c = 3.0×10⁸ m/s)",500,"MHz","f = c / λ.",
 ["f = c/λ.","3.0×10⁸ / 0.60 = 5.0×10⁸ Hz.","That is 500 MHz."])
txt(H,3,0.8,"Evaluate in Boole's algebra: (1 AND 0) OR (NOT 0). Give 0 or 1.",["1","one"],
 "Work the brackets first.",["1 AND 0 = 0.","NOT 0 = 1.","0 OR 1 = 1."])
txt(H,3,1.3,"Evaluate NOT(A AND B) OR C for A = 1, B = 1, C = 0. Give 0 or 1.",["0","zero"],
 "Work inside out.",["A AND B = 1.","NOT 1 = 0.","0 OR 0 = 0."])
mcq(H,3,1.2,"De Morgan (a contemporary of Boole) showed that NOT(A AND B) equals:",
 ["(NOT A) OR (NOT B)","(NOT A) AND (NOT B)","A OR B","NOT A AND B"],
 "Test with A = 1, B = 0: NOT(0) = 1 and (0 OR 1) = 1.",
 ["Try A=1, B=0: A AND B = 0, so NOT gives 1.","(NOT A) OR (NOT B) = 0 OR 1 = 1 (matches).","(NOT A) AND (NOT B) = 0 AND 1 = 0 (does not)."])
num(H,3,1.0,"How many different input combinations does a 4-input Boolean circuit have?",16,"","Each input has 2 values.",
 ["Each input is 0 or 1.","Combinations = 2⁴.","= 16."])
mcq(H,3,1.2,"The I–V graph of a light-bulb filament curves, because its resistance rises as it heats up. What does that say about Ohm's law V = IR?",
 ["R = V/I still defines resistance at each point, but R is not constant","Ohm's law is false for all conductors","The bulb has zero resistance when cold","The current is independent of voltage"],
 "Ohm's 'law' means constant R; V/I is still defined everywhere.",
 ["A straight I–V line means constant R (ohmic).","A curve means R changes with V (temperature).","V = IR still works as a definition at each point."])
mcq(H,3,0.8,"Ohm found that doubling the voltage across a metal wire at steady temperature does what to the current?",
 ["Doubles it","Halves it","Leaves it unchanged","Quadruples it"],
 "I = V/R with R constant.",["Current ∝ voltage for an ohmic wire.","Double V, double I.","Quadrupling would need V²."])
num(H,3,1.5,"Coulomb's torsion balance twists 8.0° when two charged spheres are 0.10 m apart. Twist is proportional to force. How many degrees will it twist at 0.05 m, with the same charges?",32,"°","Halving r multiplies force by 4.",
 ["Force ∝ 1/r².","Half the distance gives 4 times the force.","Twist 8.0° × 4 = 32°."])
mcq(H,3,0.9,"Why was a stack of metal discs separated by wet (brine-soaked) cloth able to make current?",
 ["The brine lets ions move between the two metals so each cell completes its circuit","The cloth is a magnet","The cloth insulates so no charge moves","The brine supplies electrons by itself"],
 "Two metals plus an electrolyte make a chemical cell.",
 ["A cell needs two unlike metals and an electrolyte.","Ions carry charge through the brine.","Stacking cells in series adds voltage."])
mcq(H,3,1.0,"Two parallel wires carry current in the same direction and attract. If the current in one wire is reversed, the force becomes:",
 ["repulsive","attractive and stronger","zero","attractive and weaker"],
 "Ampère: same-direction currents attract, opposite-direction currents repel.",
 ["Same direction attracts (Ampère, 1820s).","Reversing one current flips the force.","So the wires repel."])
num(H,3,1.1,"A 9.0 V cell and a 3.0 V cell are in series but facing each other (opposing) across a 12 Ω resistor. How much current flows, in amperes?",0.50,"A","Net voltage is the difference.",
 ["Opposing sources subtract: 9.0 − 3.0 = 6.0 V.","Kirchhoff's voltage law around the loop.","I = 6.0 V / 12 Ω = 0.50 A."])
num(H,3,0.9,"Kirchhoff's current law: 3.2 A and 1.1 A flow into a junction and 2.0 A flows out one wire. What current flows out of the other wire?",2.3,"A","In = out.",
 ["Total in = 4.3 A.","One wire carries away 2.0 A.","4.3 − 2.0 = 2.3 A."])
mcq(H,3,0.9,"Millikan's oil-drop experiment (1909) found that the charge on each drop was:",
 ["a whole-number multiple of one smallest charge","any value at all","always exactly 1 C","zero"],
 "Charge is quantized in units of e = 1.602×10⁻¹⁹ C.",
 ["Drops had charges like e, 2e, 3e.","No fractions of e were seen.","That showed charge comes in lumps."])
mcq(H,3,1.2,"Which expression equals one watt?",["one ampere² × one ohm","one volt ÷ one ohm","one ampere ÷ one volt","one volt × one second"],
 "P = I²R.",["P = VI and V = IR, so P = I²R.","Volt ÷ ohm is the ampere.","Ampere ÷ volt is the siemens."])
mcq(H,3,1.3,"Which named unit equals one ampere × one ohm?",["volt","watt","coulomb","farad"],
 "V = IR.",["Ohm's law: V = I × R.","So amp × ohm = volt.","Watt would be amp × volt."])
match(H,3,1.3,"Match each discovery to the year (best-known date).",
 [["Voltaic pile","1800"],["Ørsted's compass deflection","1820"],["Faraday's induction","1831"],["Kirchhoff's laws","1845"],["Hertz's radio waves","1887"]],
 "A timeline helps tie names to ideas.",["Volta 1800.","Ørsted 1820, Faraday 1831.","Kirchhoff 1845, Hertz late 1880s."])
mcq(H,3,1.4,"Siemens (S) is the SI unit of conductance, honoring Werner von Siemens. How is it related to the ohm?",
 ["1 S = 1/Ω","1 S = 1 Ω","1 S = 1 V/C","1 S = 1 A·V"],
 "Conductance is the reciprocal of resistance.",["Resistance R = V/I.","Conductance G = I/V = 1/R.","So siemens = ohm⁻¹."])
mcq(H,2,0.2,"Millikan, Thomson and Coulomb all helped explain charge. Which is matched correctly?",
 ["Thomson: the electron","Coulomb: the electron's mass","Millikan: the force law","Thomson: the voltaic pile"],
 "Thomson found the electron (1897); Millikan measured its charge (1909).",["Thomson = electron discovery.","Millikan = size of its charge.","Coulomb = force between charges."])
mcq(H,3,0.8,"Tesla's AC induction motor spins without electrical contact to its rotor. What lets the rotor turn?",
 ["A rotating magnetic field induces current in the rotor","A battery inside the rotor","Static charge on the rotor","Gravity"],
 "Faraday induction plus a rotating field (from polyphase AC).",
 ["Polyphase AC makes a rotating magnetic field.","That field induces currents in the rotor.","The induced currents feel a force, so the rotor turns."])
mcq(H,3,1.5,"A student says: 'Ohm's law shows current is used up as it passes through resistors.' Which Kirchhoff idea corrects this?",
 ["Charge is conserved, so the current is the same coming out of a series resistor as going in","Voltage is used up so current is too","Current doubles after each resistor","Resistors store current"],
 "Current is flow of charge, which cannot vanish.",
 ["KCL: current in = current out.","Energy, not current, is used up (the voltage drops).","This is the voltage-law and current-law contrast."])
mcq(H,3,1.3,"Which pair correctly links the history to the physical law each person found?",
 ["Kirchhoff: charge and energy are conserved in circuits","Ohm: charge is conserved at nodes","Volta: energy is conserved around loops","Hertz: the inverse-square force law"],
 "KCL = charge conservation; KVL = energy conservation.",["Kirchhoff covers both laws.","Ohm relates V, I, R.","Hertz did waves; Coulomb did the force law."])

# ---------------- STATIC ----------------
# L1
mcq(S,1,-1,"A balloon rubbed on hair gains electrons. The balloon is now:",["negatively charged","positively charged","neutral","magnetized"],
 "Gaining electrons makes an object negative.",["Electrons carry negative charge.","More electrons than protons means net negative.","Protons stay put."])
mcq(S,1,-1,"Which particles move when an object is charged by rubbing?",["Electrons","Protons","Neutrons","Atoms of the metal"],
 "Only electrons are free to move between materials.",["Protons are held in nuclei.","Electrons are loosely held at the outside.","Rubbing moves electrons."])
mcq(S,1,-0.8,"Which material holds static charge best?",["Plastic","Copper","Aluminum","Salt water"],
 "Insulators keep charge in place; conductors let it spread and escape.",["Plastic is an insulator.","Metals and salt water conduct.","Charge cannot easily leave an insulator."])
mcq(S,1,-1,"A neutral object contains:",["equal amounts of positive and negative charge","only protons","no charge at all","only electrons"],
 "Neutral means the charges balance, not that they are absent.",["Atoms hold protons and electrons.","Equal numbers means net zero.","Charges can still shift (polarization)."])
mcq(S,1,-1,"Electric field arrows around an isolated positive point charge point:",["away from the charge","toward the charge","in circles","all the same direction"],
 "Field points the way a positive test charge is pushed.",["A positive test charge is repelled by +.","So the arrows point outward.","Toward is for negative sources."])
mcq(S,1,-0.8,"Which of these is a good conductor?",["Copper wire","Rubber glove","Dry wood","Glass rod"],
 "Metals have free electrons.",["Free electrons carry charge.","Copper has many.","Rubber, wood and glass are insulators."])
mcq(S,1,-0.8,"Electric field lines drawn closer together show where the field is:",["stronger","weaker","zero","reversed"],
 "Line density shows field strength.",["More lines per area means stronger field.","Spread lines mean weaker.","Direction is given by arrows."])
mcq(S,1,-0.8,"Silk rubbed on glass gives the glass +2 nC of charge. What happens to the silk?",["It gains −2 nC","It stays neutral","It gains +2 nC","It loses all charge"],
 "Charge is conserved: the total stays zero.",["Electrons moved from glass to silk.","Silk gained what glass lost.","So the silk is −2 nC."])
mcq(S,1,-0.5,"Proton and electron charges compared: they are",["equal in size and opposite in sign","equal in size and the same sign","different in size and opposite","different in size and same"],
 "Both have magnitude 1.602×10⁻¹⁹ C.",["A proton is +e.","An electron is −e.","That is why atoms are neutral."])
# L2
num(S,2,0,"Two charges, +2.0 µC and +3.0 µC, are 0.60 m apart. Find the force between them in newtons. (k = 8.99×10⁹)",round(k*6e-12/0.36,4),"N","F = kq₁q₂/r².",
 ["Convert µC to C.","F = (8.99×10⁹)(2.0×10⁻⁶)(3.0×10⁻⁶)/0.60².","≈ 0.15 N, repulsive."])
num(S,2,0.2,"A rod gains 5.0×10¹² extra electrons. What is its charge in µC? (e = 1.602×10⁻¹⁹ C; give the magnitude)",round(5e12*e*1e6,4),"µC","Q = ne.",
 ["Q = 5.0×10¹² × 1.602×10⁻¹⁹ C.","= 8.0×10⁻⁷ C.","= 0.80 µC (negative)."])
num(S,2,0,"A 5.0 nC test charge feels a force of 2.0×10⁻⁴ N. What is the electric field strength, in N/C?",4e4,"N/C","E = F/q.",
 ["Convert nC to C: 5.0×10⁻⁹ C.","E = 2.0×10⁻⁴ / 5.0×10⁻⁹.","= 4.0×10⁴ N/C."])
num(S,2,0,"A 4.0 µC charge sits in a field of 2500 N/C. What force acts on it, in newtons?",0.010,"N","F = qE.",
 ["Rearrange E = F/q to F = qE.","F = 4.0×10⁻⁶ × 2500.","= 0.010 N."])
mcq(S,2,0,"A charged metal sphere (+6 µC) touches an identical neutral sphere, then they are separated. Each sphere has:",["+3 µC","+6 µC","+12 µC","0"],
 "Identical conductors share total charge equally.",["Total charge +6 µC is conserved.","Two identical spheres split it evenly.","Each gets +3 µC."])
mcq(S,2,0,"A negatively charged rod is brought near, not touching, the knob of a neutral electroscope. The leaves:",["spread apart, then collapse when the rod is removed","stay together","spread and stay spread after the rod leaves","collapse and stay that way"],
 "Charge is only shifted, not added.",["The rod pushes electrons down to the leaves.","The leaves repel, so they spread.","Remove the rod and the electrons return, so they collapse."])
mcq(S,2,0,"A positive rod touches a neutral metal sphere on an insulating stand, then is removed. The sphere is:",["positively charged","negatively charged","neutral","positive on one side only"],
 "Conduction gives the same sign as the rod.",["Electrons flow from the sphere to the rod.","The sphere loses electrons.","So it ends positive."])
mcq(S,2,0,"One of two point charges is cut to half its value. The distance stays the same. The force becomes:",["half","a quarter","double","unchanged"],
 "Force ∝ q₁q₂.",["Force is proportional to each charge.","Half a charge gives half the force.","Only distance has the squared effect."])
mcq(S,2,0.2,"On a conductor in equilibrium, excess charge sits:",["on the outer surface","evenly throughout the inside","only at the center","nowhere"],
 "Like charges repel and spread out as far as possible.",["Free charges repel each other.","They move to the outside surface.","Inside a conductor in equilibrium the field is zero."])
mcq(S,2,0,"An electron is placed in an electric field that points east. The force on the electron points:",["west","east","north","nowhere, force is zero"],
 "Force on a negative charge is opposite to the field.",["Field direction = force on a positive test charge.","An electron is negative.","So its force is opposite: west."])
mcq(S,2,0.2,"Why can electric field lines never cross?",["The field has one direction at any point","Lines stop at conductors","Positive lines are heavier","Crossing would make them reverse"],
 "At a crossing, the field would have two directions at once.",["Each point has a single field direction.","Crossing lines would give two.","So lines never cross."])
mcq(S,2,0,"Why are fuel trucks grounded or bonded to the tank when they fuel?",["To drain static charge so a spark cannot ignite fuel vapor","To make the fuel flow faster","To magnetize the nozzle","To warm the fuel"],
 "Sparks can ignite vapor; grounding drains the charge.",["Flow can build static charge.","A spark may ignite vapor.","Grounding lets charge leak away safely."])
mcq(S,2,0.3,"Which charge could exist on an object? (e = 1.602×10⁻¹⁹ C)",["3.204×10⁻¹⁹ C","2.403×10⁻¹⁹ C","0.801×10⁻¹⁹ C","4.5×10⁻²⁰ C"],
 "Charge is quantized: a whole number times e.",["3.204×10⁻¹⁹ = 2e.","2.403×10⁻¹⁹ = 1.5e, not allowed.","Fractions of e do not appear."])
num(S,2,0.3,"A body has a charge of −4.806×10⁻¹⁹ C. How many excess electrons does it have? (e = 1.602×10⁻¹⁹ C)",3,"electrons","N = Q/e.",
 ["N = 4.806×10⁻¹⁹ / 1.602×10⁻¹⁹.","= 3.","Charge comes in whole electrons."])
txt(S,2,0,"A charged object comes near a neutral insulator, shifting its charges slightly without a net charge change. What is this called?",["polarization","polarisation","polarized","polarizing"],
 "The nearer opposite charge pulls harder than the farther like charge pushes.",["Insulator charges cannot flow, only shift.","This shift is polarization.","It explains why balloons stick to walls."])
mcq(S,2,0.3,"Why does a charged balloon on a wall fall after a while?",["Charge leaks away through the air and wall","The balloon gains weight","Gravity gets stronger","Protons leave the balloon"],
 "Moist air and surfaces slowly drain charge.",["Charge is not permanent on an insulator in air.","Water vapor lets it leak.","Less charge means weaker attraction, so gravity wins."])
mcq(S,2,0.3,"Why does a pointed lightning rod help protect a building?",["Charge concentrates at points, bleeding off gently or giving lightning a safe path to ground","It attracts no charge at all","It stores the lightning","It is a good insulator"],
 "Sharp points concentrate field and lead charge safely to ground.",["Charge crowds at sharp points.","A conducting path to ground carries the current away.","This keeps it from going through the building."])
mcq(S,2,0.4,"A car is hit by lightning. Why are the passengers usually safe?",["Charge flows along the metal outside, and the field inside is near zero","Rubber tires insulate the car from the strike","Cars repel lightning","Lightning cannot carry current"],
 "A conducting shell shields its inside.",["Charge spreads on the outer surface.","The field inside a conductor shell is about zero.","Tires alone cannot stop a lightning strike."])
match(S,2,0.2,"Match each charging process to its description.",
 [["Friction","Electrons move between two rubbed materials"],["Conduction","Touching shares charge, giving the same sign"],["Induction","Charge separated by a nearby rod and then grounded"],["Polarization","Charges in an insulator shift, with no net change"]],
 "Four ways to move or rearrange charge.",["Friction transfers electrons.","Conduction needs contact.","Induction needs grounding; polarization leaves net charge zero."])
order(S,2,0.3,"Put the steps of safely handling a static-sensitive chip in order.",
 ["Put on a wrist strap connected to ground","Touch the grounded antistatic mat","Take the chip out of its antistatic bag","Place the chip in the socket"],
 "Ground yourself before touching the chip.",["Drain your own charge first.","Work on a grounded mat.","Only then handle the chip."])
mcq(S,2,0,"Distance between two charges is halved. The force becomes:",["4 times larger","2 times larger","half","a quarter"],
 "Force ∝ 1/r².",["r → r/2.","(1/(1/2))² = 4.","So 4 times larger."])
# L3 challenge
num(S,3,1.0,"Charges 1.5 µC and 2.5 µC are 3.0 cm apart. Find the force in newtons. (k = 8.99×10⁹)",round(k*1.5e-6*2.5e-6/0.03**2,3),"N","Convert cm to m before squaring.",
 ["3.0 cm = 0.030 m.","F = (8.99×10⁹)(1.5×10⁻⁶)(2.5×10⁻⁶)/0.030².","≈ 37 N; forgetting to convert gives a nonsense number."])
num(S,3,1.1,"Two charges exert 9.0 N on each other at 0.10 m. At what distance would the force be 1.0 N? Answer in meters.",0.30,"m","Force ∝ 1/r².",
 ["Force drops by 9.","So distance rises by √9 = 3.","0.10 × 3 = 0.30 m."])
num(S,3,1.2,"A 40 N force acts at distance r. Charge 1 triples, charge 2 is halved, and the distance doubles. New force in newtons?",15,"N","Multiply the factors.",
 ["Charges: 3 × ½ = 1.5.","Distance: 1/2² = 1/4.","40 × 1.5 / 4 = 15 N."])
mcq(S,3,1.0,"Distance tripled and both charges doubled. The new force is:",["4/9 of the original","4/3 of the original","12 times the original","2/3 of the original"],
 "Charges give 2 × 2 = 4; distance gives 1/9.",["F ∝ q₁q₂/r².","Factor = (2×2)/3².","= 4/9."])
mcq(S,3,1.3,"q₁ is halved, q₂ is tripled, and the distance is halved. The force becomes:",["6 times larger","3/4 as large","3/2 as large","12 times larger"],
 "Factor = (½ × 3)/(½)².",["Charges: ½ × 3 = 3/2.","Distance: 1/(½)² = 4.","3/2 × 4 = 6."])
mcq(S,3,1.0,"A +4q sphere and a +q sphere repel. Which statement is right?",["The forces on the two spheres are equal in size and opposite in direction","The +4q sphere feels 4 times more force","The +q sphere feels 4 times more force","Only the smaller sphere feels a force"],
 "Newton's third law: they act on each other with equal forces.",["Coulomb's force is mutual.","Each charge's field acts on the other.","Bigger charge does not mean bigger force on it."])
mcq(S,3,1.5,"Two identical-mass balls on strings repel; one has charge +4q, the other +q. Both hang at rest. Compared with each other, the string angles are:",["equal","the +4q ball hangs at a larger angle","the +q ball hangs at a larger angle","not determined"],
 "Equal forces on equal masses give equal angles.",["The Coulomb forces are equal (third law).","Equal masses, equal gravity.","Same force balance means same angle."])
mcq(S,3,1.0,"A neutral metal ball hangs near a positive rod. It swings in, touches the rod, then:",["swings away","stays stuck","feels no force","swings in again"],
 "After touching, it has the same sign as the rod, so it is repelled.",["First, polarization pulls it in.","Contact shares charge.","Now both positive, so it is repelled."])
mcq(S,3,1.1,"A negatively charged electroscope has spread leaves. A positive rod is brought near the knob (no contact). The leaves:",["move closer together","spread more","stay the same","fall and then spread again"],
 "The rod pulls electrons up toward the knob, leaving the leaves less negative.",["Positive rod attracts electrons.","They move up, so the leaves hold less charge.","Less repulsion, so they close up."])
mcq(S,3,1.0,"A positive rod is brought near a neutral metal sphere on an insulator. The sphere is grounded briefly, then the ground is removed, then the rod is removed. The sphere is now:",["negatively charged","positively charged","neutral","negative on one side only"],
 "Induction leaves the opposite sign.",["The rod attracts electrons from ground.","Ground removed first traps them.","So the sphere ends negative."])
mcq(S,3,1.0,"Two identical positive charges are fixed. Along the line between them, where could a third negative charge feel zero net force?",["At the midpoint","Closer to either one","Anywhere on the line","Nowhere"],
 "Equal pulls cancel only at the midpoint.",["Nearer charge pulls harder.","Only at the midpoint are distances equal.","So net force is zero only there."])
mcq(S,3,1.6,"A +q and a −q are fixed 1 m apart. On the straight line through them, where can a small positive test charge feel zero net force?",["Nowhere","At the midpoint","Beyond the +q","Beyond the −q"],
 "Between them the forces add; outside, the nearer charge always wins.",["At the midpoint both forces point the same way, so they add.","Outside, the nearer charge exerts the stronger force.","The charges are equal in size, so they never cancel."])
mcq(S,3,0.8,"At the midpoint between +q and −q, the electric field points:",["toward −q, and is twice one charge's field","toward +q, and is zero","away from both","toward −q, and is zero"],
 "Both fields point the same way there.",["+q pushes away from itself.","−q pulls toward itself.","Same direction, so they add."])
mcq(S,3,0.8,"At the midpoint between two equal positive charges, the electric field is:",["zero","double one charge's field","pointing toward either charge","infinite"],
 "The two fields point in opposite directions with equal size.",["Each pushes away from itself.","At the midpoint the pushes are opposite.","Equal sizes cancel."])
mcq(S,3,1.1,"A charged comb picks up a bit of paper. Soon the paper jumps off. Why?",["It gained the comb's charge by contact, so it is repelled","It became heavy","The comb lost its charge","The paper became magnetic"],
 "Polarization first, then conduction.",["Polarization attracted the paper.","Contact shared some charge.","Now the same sign, so repulsion."])
mcq(S,3,0.8,"Why do paint droplets from an electrostatic sprayer spread out evenly and coat the object's back?",["Droplets have like charge so they repel; the grounded object attracts them","They are heavier","Gravity pulls them sideways","The air blows them"],
 "Like charges repel; opposite (or induced) attract.",["Droplets all carry the same sign.","So they spread apart.","The object attracts them, even to its back."])
mcq(S,3,1.0,"A wrist strap for electronics work has a 1 MΩ resistor in it. Why is that resistor there?",["To limit current if the wearer touches a live circuit","To build up charge on the wearer","To speed up discharge to zero seconds","To make the strap a perfect insulator"],
 "It still drains static slowly but limits dangerous current.",["Static charge is tiny and drains fine through 1 MΩ.","A direct wire would be a shock hazard.","So the resistor keeps it safe."])
multi(S,3,1.0,"Select ALL true statements about a conductor in electrostatic equilibrium.",
 ["The field inside is zero","Excess charge is on the surface","Field lines meet the surface at right angles","Charge spreads perfectly evenly on every shape"],[0,1,2],
 "Charge crowds at sharp points, so it is not uniform.",["Free charges stop moving when the field inside is zero.","They sit on the surface; the field at the surface is perpendicular.","On pointed shapes charge is denser at the tips."])
multi(S,3,0.8,"Select ALL actions that reduce static buildup.",
 ["Raising the humidity","Wearing a grounded wrist strap","Using an antistatic mat","Walking on carpet in rubber-soled shoes"],[0,1,2],
 "Rubber-soled shoes on carpet help build charge.",["Moist air drains charge.","Grounding paths drain it directly.","Rubber on carpet insulates and charges you."])
num(S,3,1.2,"A 3.0 nC point charge. Use E = F/q with Coulomb's law to find the field at 0.30 m from it, in N/C. (k = 8.99×10⁹)",round(k*3e-9/0.09,1),"N/C","E = kq/r².",
 ["Place a test charge q₀ there: F = kqq₀/r².","E = F/q₀ = kq/r².","= 8.99×10⁹ × 3.0×10⁻⁹ / 0.090 ≈ 300 N/C."])
num(S,3,1.2,"A 1.0 mA current flows for 3.2 ms. How many electrons pass a point? (e = 1.602×10⁻¹⁹ C)",round(1e-3*3.2e-3/e,-9),"electrons","Q = It, then N = Q/e.",
 ["Q = 1.0×10⁻³ × 3.2×10⁻³ = 3.2×10⁻⁶ C.","N = Q/e.","≈ 2.0×10¹³ electrons."])
num(S,3,1.0,"Air breaks down and sparks when the field reaches about 3×10⁶ V/m. About how many volts across a 1.0 mm gap before a spark? (field × gap)",3000,"V","V = E × d.",
 ["Convert 1.0 mm to 0.0010 m.","V = 3×10⁶ × 0.0010.","≈ 3000 V."])
num(S,3,0.8,"A rod loses 3.0×10¹² electrons. What is its charge in µC? (e = 1.602×10⁻¹⁹ C; give the magnitude)",round(3e12*e*1e6,3),"µC","Q = ne.",
 ["Losing electrons leaves the rod positive.","Q = 3.0×10¹² × 1.602×10⁻¹⁹ C = 4.8×10⁻⁷ C.","= 0.48 µC."])
num(S,3,1.4,"Two equal charges repel with 0.90 N at 0.10 m. Find each charge, in µC. (k = 8.99×10⁹)",round(math.sqrt(0.9*0.01/k)*1e6,3),"µC","q² = Fr²/k.",
 ["F = kq²/r², so q² = Fr²/k.","q² = 0.90 × 0.010 / 8.99×10⁹ ≈ 1.0×10⁻¹².","q = 1.0×10⁻⁶ C = 1.0 µC."])
num(S,3,1.4,"Two +2.0 µC charges repel with 0.20 N. How far apart are they, in meters? (k = 8.99×10⁹)",round(math.sqrt(k*4e-12/0.2),3),"m","r² = kq₁q₂/F.",
 ["r² = (8.99×10⁹)(2.0×10⁻⁶)²/0.20.","r² ≈ 0.180 m².","r ≈ 0.42 m."])
num(S,3,1.3,"+8.0 µC and −2.0 µC identical spheres attract. They touch and are returned to 0.30 m apart. What is the new force in newtons? (k = 8.99×10⁹)",round(k*3e-6*3e-6/0.09,3),"N","Total charge splits evenly after touching.",
 ["Total = +6.0 µC, so each sphere has +3.0 µC.","Now they repel.","F = (8.99×10⁹)(3.0×10⁻⁶)²/0.30² ≈ 0.90 N."])
num(S,3,1.0,"Identical spheres of −10 µC and +6.0 µC touch and are separated. What is the charge on each, in µC?",-2.0,"µC","Total is conserved and shared.",
 ["Total = −10 + 6 = −4.0 µC.","Split between two identical spheres.","−2.0 µC each."],tol=0.02)
num(S,3,1.4,"Sphere A has charge Q. It touches identical neutral sphere B, is separated, then touches identical neutral sphere C. What fraction of Q does A end with? (decimal)",0.25,"×Q","Each touch splits A's charge in half.",
 ["After B: Q/2.","After C: half of Q/2.","= Q/4 = 0.25 Q."])
num(S,3,1.5,"An electron (m = 9.11×10⁻³¹ kg) sits in a field of 2.0×10³ N/C. What is its acceleration in m/s²? (e = 1.602×10⁻¹⁹ C)",round(e*2e3/9.11e-31,-11),"m/s²","F = eE, a = F/m.",
 ["F = 1.602×10⁻¹⁹ × 2.0×10³ = 3.2×10⁻¹⁶ N.","a = F/m = 3.2×10⁻¹⁶ / 9.11×10⁻³¹.","≈ 3.5×10¹⁴ m/s²: huge, since electrons are so light."])
# very hard
num(S,3,1.5,"A −2.0 µC charge sits between +4.0 µC (0.20 m to its left) and +1.0 µC (0.30 m to its right). Find the net force magnitude in newtons. (k = 8.99×10⁹)",
 round(abs(k*8e-12/0.04-k*2e-12/0.09),2),"N","Both attract, in opposite directions.",
 ["Left pull: kq₁q₂/r² = (8.99×10⁹)(8.0×10⁻¹²)/0.040 ≈ 1.80 N.","Right pull: (8.99×10⁹)(2.0×10⁻¹²)/0.090 ≈ 0.20 N.","Opposite directions, so subtract: ≈ 1.6 N toward the +4.0 µC."])
num(S,3,1.5,"A +2.0 µC charge sits midway between +4.0 µC and +1.0 µC charges 0.60 m apart. What is the net force in newtons? (k = 8.99×10⁹)",
 round(abs(k*8e-12/0.09-k*2e-12/0.09),3),"N","Both repel; the pushes oppose.",
 ["Each distance is 0.30 m.","Pushes: 0.80 N and 0.20 N in opposite directions.","Net ≈ 0.60 N toward the +1.0 µC charge."])
num(S,3,1.3,"Charges +4q and +q are 0.90 m apart. How far from the +4q is the point on the line between them where the net field is zero? (meters)",0.60,"m","Equal fields: 4/x² = 1/(d−x)².",
 ["Set 4kq/x² = kq/(0.90−x)².","Take square roots: 2(0.90−x) = x.","x = 0.60 m from +4q."])
num(S,3,2.0,"+4.0 µC and −1.0 µC are 0.50 m apart. On the line beyond the −1.0 µC (away from the +4.0 µC), where is the net field zero? Give the distance from the −1.0 µC in meters.",0.50,"m","Equal and opposite fields: 4/(0.5+x)² = 1/x².",
 ["Zero-field point lies on the weaker-charge side, outside.","4/(0.50+x)² = 1/x² gives 2x = 0.50 + x.","x = 0.50 m."])
num(S,3,1.8,"Three +3.0 µC charges sit at corners of a right angle: one at the corner, one 0.30 m along x, one 0.30 m along y. What is the net force magnitude on the corner charge in newtons? (k = 8.99×10⁹)",
 round(math.sqrt(2)*k*9e-12/0.09,2),"N","Add the two perpendicular forces as vectors.",
 ["Each force: (8.99×10⁹)(9.0×10⁻¹²)/0.090 ≈ 0.90 N.","They are at right angles.","Net = 0.90 × √2 ≈ 1.27 N at 45°."])
num(S,3,1.5,"By what factor must you multiply the distance between two charges to make the force twice as large? (decimal)",round(2**-0.5,3),"×","F ∝ 1/r², so r ∝ 1/√F.",
 ["Need F × 2.","r factor = 1/√2.","≈ 0.707."])
num(S,3,1.3,"By what factor must you multiply the distance to make the force 9 times smaller?",3,"×","F ∝ 1/r².",
 ["Factor 1/9 = 1/r².","r² = 9.","r × 3."])
mcq(S,3,1.6,"Two identical hollow metal spheres carry +10 µC and −2 µC. They touch and are separated. Compared with before, the force between them at the same distance:",["changes from attractive to repulsive","stays attractive and is weaker","stays attractive and is the same","stays repulsive"],
 "After touching each has +4 µC.",["Total +8 µC, so +4 µC each.","Both are now positive.","So they repel."])
mcq(S,3,1.6,"Why does the force between two charges not simply add the effect of a third charge nearby? Which description is right?",["Each charge's force on a given charge is found separately, then added as vectors (superposition)","The third charge cancels the second","Forces from charges multiply","Only the nearest charge matters"],
 "Superposition: add vector forces from each source.",["Pairwise Coulomb forces do not interfere.","Net force = vector sum.","Directions matter."])
mcq(S,3,1.8,"A positive point charge Q sits at the center of a thin neutral metal shell. Compared with an empty region, the field just outside the shell is:",["the same as if Q were alone, pointing outward","zero","reversed","doubled"],
 "Induced surface charges −Q inside and +Q outside restore the outside field.",["Inner surface gets −Q.","Outer surface gets +Q.","Outside, the field looks like Q alone."])
mcq(S,3,1.8,"A neutral metal sphere on a stand is near a +Q charge. Which is true?",["The sphere is attracted even though it has no net charge","The sphere is repelled","No force acts","Its net charge becomes +Q"],
 "Induction/polarization puts opposite charge nearer.",["Nearer −charge pulls harder than the farther +charge pushes.","Net force is attraction.","No net charge was added."])
mcq(S,3,2.2,"A +3q and a −q are fixed apart. A third charge is placed so net force on it is zero. It must be:",["outside, closer to the smaller (−q) charge","between them","outside, closer to the larger (+3q) charge","anywhere on the line"],
 "Outside, the weaker charge must be the nearer one to balance it.",["Between: both forces point the same way.","Outside near +3q: +3q is both nearer and larger, so it wins.","Outside near −q: nearer balances the smaller size."])
mcq(S,3,2.0,"Charge Q = 4 µC is shared between two spheres with radius ratio 1:2 by contact at large separation. The bigger sphere ends with the larger charge. Which concept explains it?",["Charge spreads so both reach the same electric potential","Charge divides equally","The smaller sphere keeps all of it","Charge goes to the smaller sphere only"],
 "Connected conductors reach equal potential, and bigger spheres hold more.",["Equal charges apply only to identical spheres.","Potential, not charge, equalizes.","A bigger sphere holds more at the same potential."])
mcq(S,3,2.0,"A spark between a charged person and a doorknob is brief and harmless. Which fact best explains why static shocks do not cause lasting current?",["The charge is tiny, so only a short burst can flow","Static has no voltage","The doorknob is an insulator","Current needs magnetic fields"],
 "Static has high voltage but very little charge.",["Thousands of volts can build up.","Only a tiny amount of charge is stored.","The burst ends in a fraction of a second."])
mcq(S,3,1.3,"Which situation requires the most care about static sparks?",["Pumping fuel on a dry day","Reading under a lamp","Charging a phone","Boiling water"],
 "Fuel vapor can be ignited by a spark.",["Dry air builds charge.","Flowing fuel and clothing add charge.","A spark near vapor can start a fire."])
mcq(S,3,1.2,"A student measures force at several distances and plots F versus 1/r². The graph is a straight line through the origin. This shows:",["F is proportional to 1/r²","F is proportional to r","F does not depend on distance","F ∝ r²"],
 "A straight line through the origin means direct proportion.",["Plot F against 1/r².","Straight line through 0 means F ∝ 1/r².","This is Coulomb's inverse-square law."])
data=json.load(open(OUT)) if False else None
drop=("Why does the force between two charges not simply","Charge Q = 4 µC is shared")
new=[q for q in new if not q['q'].startswith(drop)]
for q in new:
    if q['q'].startswith("A positive point charge Q sits at the center"):
        q['q']="A +Q point charge sits at the center of a thin, neutral metal shell. Just outside the shell, the field is:"
    if q['q'].startswith("Which situation requires the most care"):
        q['l']=1; q['b']=-0.4
    if q['q'].startswith("Which pair is matched correctly with the unit"):
        q['q']="Which scientist is matched with the quantity their unit measures?"
    if q['q'].startswith("A 10 kW load is fed"):
        q['sol']=["I = 10 000 W / 1000 V = 10 A.","Loss = I²R = 10² × 2.0 = 200 W.","Do not use V²/R: 1000 V is the supply voltage, not the voltage across the line."]
fix={
"static-013":{"text":["positively charged","positive","positively","net positive"]},
"static-017":{"l":2,"b":0.2},
"static-082":{"text":["repel","repels","repulsion"]},
"static-084":{"text":["repel","repels","repulsion"]},
"static-085":{"text":["attract","attracts","attraction"]},
"static-021":{"text":["repel","repel each other","repulse"]},
"static-008":{"text":["toward the charge","toward","inward","into the charge"]},
"static-012":{"text":["dry","dry air","low humidity"]},
"static-083":{"q":"What is the magnitude of the charge of one electron, in coulombs? (Type like 1.6e-19)"},
"hist-040":{"q":"Which unit is used to measure electric charge?"},
"hist-041":{"q":"Which unit measures electric current, the flow of charge per second?","text":["ampere","amp","amps","amperes","a"]},
"hist-038":{"text":["watt","watts","w"]},
"hist-039":{"text":["ohm","ohms"]},
"hist-042":{"text":["volt","volts","v"]},
"hist-031":{"text":["ampere","amp","amps","amperes"]},
"hist-019":{"text":["georg ohm","ohm","georg simon ohm","georg s ohm"]},
"hist-020":{"text":["alessandro volta","volta"]},
"hist-021":{"text":["heinrich hertz","hertz"]},
"hist-022":{"text":["george boole","boole"]},
"hist-023":{"text":["gustav kirchhoff","kirchhoff"]},
"hist-001":{"text":["magnetism","magnetic","magnetic effects","magnetic fields"]},
"hist-002":{"text":["torsion balance","torsion"]},
}
dele=["hist-011","hist-032","hist-033","hist-034","hist-035","hist-036","hist-037","hist-043","hist-044","static-051","static-035","static-036","static-037","static-140","static-141","static-142"]
rep=("Reviewed all 44 hist and 151 static items. Facts/numerics verified in python: no wrong answers found in the shown items (e.g. 1.50 N, 2.70e-4 N, 6.2e12 e, 3.6 N all correct). "
"Fixes: %d (added accepted text aliases for short-answer items so spelling/phrasing variants are marked right; reworded hist-040/041 whose stems were awkward or imprecise; static-017 re-leveled to core since it is one division; static-083 now says magnitude and a typing format). "
"Deleted %d: hist-011 (dup of hist-019), hist-032..037 (verbatim lookalikes of hist-024..030), hist-043/044 (dup of hist-031/039 and 027), static-051 (history question inside the charge topic, dup of hist), "
"static-035..037 and static-140..142 (lookalike scaling templates; the shown static-045..047 mcq family and static-026..028 already cover them). "
"Remaining doubts: families show only 3 variants, so the full static families 'q1 x# and distance x#' (id 035) and 'cou-scale' (id 140) probably still have more hidden variants that duplicate static-045 family; I could not see their fp keys, so I did not use del_family. Original bank skewed heavily to level 1-2 recall; hist had 36 of 44 level-1 items mostly 'who did X'. "
"New: %d questions (%d hist, %d static), about half level 3, including 60 Hz/period, AC line-loss, induction, Maxwell/Hertz, Boolean eval, and superposition, charge sharing, zero-field point, electron acceleration problems. All numerics computed in python (c1_build.py). Static air-breakdown (3e6 V/m) and 1 MΩ wrist strap items are textbook approximations worded as 'about'.")
nh=sum(1 for q in new if q['t']=='hist'); ns=len(new)-nh
out={"fix":fix,"del":dele,"del_family":[],"new":new,"report":rep%(len(fix),len(dele),len(new),nh,ns)}
json.dump(out,open(OUT,"w"),ensure_ascii=False,indent=1)
print(len(new),nh,ns)
