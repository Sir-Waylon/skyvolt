# -*- coding: utf-8 -*-
"""Hovercraft B guide page (Skyvolt site): rules in brief, score/lift/battery/relay calculators, team build notes."""
CSS='''.hc{max-width:880px;margin:0 auto;padding:32px 0 56px}.hc h1{font-size:2.1rem;margin:0 0 8px}.hc h2{margin:40px 0 10px;font-size:1.5rem}.hc h3{margin:22px 0 6px;font-size:1.15rem}.hc p,.hc li{max-width:68ch;line-height:1.55}
.hc .tbl{overflow-x:auto;margin:12px 0}.hc table{border-collapse:collapse;width:100%;min-width:560px;font-size:.95rem}.hc th,.hc td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}.hc th{background:var(--card)}
.hc .calc{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;margin:14px 0}.hc .cg{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}.hc label{display:block;font-weight:600;font-size:.92rem}.hc input,.hc select{display:block;width:100%;box-sizing:border-box;margin-top:4px;padding:9px 10px;border:1px solid var(--line);border-radius:10px;font:inherit;background:var(--bg);color:var(--tx);min-height:44px}
.hc .out{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:14px}.hc .out div{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:10px 12px}.hc .out b{display:block;font-size:1.35rem}.hc .out span{font-size:.85rem;color:var(--mut)}
.hc .note{border-left:5px solid var(--pri);background:var(--card);padding:10px 14px;border-radius:0 12px 12px 0;margin:14px 0}.hc .warn{border-left-color:#b45309}.hc .toc{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}.hc .toc a{border:1px solid var(--line);border-radius:999px;padding:6px 14px;text-decoration:none}
'''
BODY='''<div class="wrap hc"><h1>Hovercraft B guide</h1>
<p class="lead">A plain-language guide for Division B teams: what the rules ask for, how the score is built, the physics of floating and pushing, and the electrical side (batteries, fans and a relay speed controller). It is based on the 2027 Division B rules and on one team’s own build notes and measurements. The rulebook always wins if anything here disagrees with it.</p>
<nav class="toc" aria-label="On this page"><a href="#rules">Rules in brief</a><a href="#score">Score calculator</a><a href="#lift">Lift and thrust</a><a href="#power">Battery and fans</a><a href="#relay">Relay timing</a><a href="#build">Build notes</a><a href="#plan">Run-day plan</a></nav>
<div class="note"><b>Linked to Voltaic.</b> Ohm’s law, series and parallel batteries, power, and RC charging from the Voltaic trainer are exactly what the electrical sections use.</div>

<h2 id="rules">Rules in brief</h2>
<ul><li><b>Goal:</b> a vehicle on a cushion of air carries nickels down a 185 cm timed section of a 45 cm wide track and tries to arrive as close as possible to a Target Time (6 to 18 s, same for every team).</li>
<li><b>Size:</b> fits in a 40 × 40 × 40 cm box while floating. A 1/4 inch or larger wooden dowel stands within 3 cm of the front, at least 20 cm above the track, and must be the first part to break the timing beam.</li>
<li><b>Electrical parts allowed:</b> batteries, wires, mechanical switches, relays, resistors (including potentiometers), capacitors and up to two motors. No integrated circuits (so no 555 timer), no lasers.</li>
<li><b>Batteries:</b> store-bought, original labels visible, no lithium or lead. Total label voltage between any two points must not exceed 12.0 V.</li>
<li><b>Safety:</b> shields so a 3/8 inch dowel cannot touch any fan or impeller, and a manual switch for every motor. Failing these means you only get participation points.</li>
<li><b>Competition:</b> 8 minutes total, two runs, no practice runs. You choose the nickel load for each run. You may touch the vehicle only until you let go at the start line.</li>
<li><b>Nickels:</b> the supervisor provides 4 full rolls (40 nickels, about 200 g each), 1 half roll and 20 loose nickels. About 5 g per nickel. Rolls cannot be taped or opened.</li>
<li><b>Ramp:</b> optional 5 cm high ramp. Using it halves the Distance Score and makes the Mass Score zero for that run.</li></ul>

<h2 id="score">Score calculator</h2>
<p>Run Score = Distance Score (up to 40) + Time Score (up to 40) + Mass Score (up to 20). The best run counts. Complete runs get the full 40 for distance, so almost all of your points are won by hitting the Target Time and carrying nickels all the way.</p>
<form class="calc" id="sc" aria-label="Run score calculator"><div class="cg">
<label>Run finished?<select id="sc_c"><option value="1">Complete</option><option value="0">Incomplete</option></select></label>
<label>Run time (s)<input id="sc_t" type="number" step="0.01" min="0" value="10.2"></label>
<label>Target Time (s)<input id="sc_tt" type="number" step="0.5" min="6" max="18" value="10"></label>
<label>If incomplete: distance from finish (cm)<input id="sc_d" type="number" step="1" min="0" max="185" value="0"></label>
<label>Full nickel rolls (0 to 4)<input id="sc_r" type="number" step="1" min="0" max="4" value="2"></label>
<label>Half roll used?<select id="sc_h"><option value="0">No</option><option value="1">Yes</option></select></label>
<label>Loose nickels (0 to 20)<input id="sc_n" type="number" step="1" min="0" max="20" value="10"></label>
<label>Used the ramp?<select id="sc_p"><option value="0">No</option><option value="1">Yes</option></select></label>
<label>Construction violations<input id="sc_cv" type="number" step="1" min="0" value="0"></label>
<label>Competition violations<input id="sc_pv" type="number" step="1" min="0" value="0"></label>
<label>Missed impound?<select id="sc_m"><option value="0">No</option><option value="1">Yes</option></select></label></div>
<div class="out" aria-live="polite"><div><b id="o_ds">–</b><span>Distance Score</span></div><div><b id="o_ts">–</b><span>Time Score</span></div><div><b id="o_ms">–</b><span>Mass Score</span></div><div><b id="o_rs">–</b><span>Run Score</span></div><div><b id="o_g">–</b><span>Nickel mass</span></div></div></form>
<p class="small">Formulas: Time Score = 40 × (1 − |time − Target| ÷ Target), minimum 0. Mass Score = (4 × rolls + 0.1 × loose nickels) × (185 − distance from finish) ÷ 185, so a complete run with 4.5 rolls and 20 nickels reaches the 20-point maximum. Each construction violation multiplies the run by 0.8, each competition violation by 0.9, and missing impound by 0.7.</p>
<div class="note"><b>What the numbers say.</b> A 10 s Target Time missed by 1 s costs 4 points. Carrying one full roll (about 200 g) is worth 4 points, but only if the heavier vehicle still arrives on time, so test your time at each load.</div>

<h2 id="lift">Lift and thrust</h2>
<h3>Floating</h3>
<p>The lift fan fills a space under the hull, and a flexible skirt keeps the air from escaping too fast. The cushion pressure must equal the vehicle’s weight divided by the area of the cushion: <b>P = m × g ÷ A</b>. If the fan cannot make that pressure, the hull does not rise. If it only just manages, the skirt will not hold its shape and the craft drags.</p>
<p>Fan data sheets list <b>airflow (CFM)</b> and <b>static pressure (Pa)</b>. Axial case fans move lots of air at low pressure; blowers push less air at higher pressure. For lift you want pressure, with enough airflow to keep leaking air replaced.</p>
<form class="calc" id="lf" aria-label="Lift pressure calculator"><div class="cg">
<label>Hull mass with fans and battery (g)<input id="lf_m" type="number" step="1" min="0" value="417"></label>
<label>Nickel load (g)<input id="lf_n" type="number" step="1" min="0" value="226"></label>
<label>Dowel and extras (g)<input id="lf_d" type="number" step="1" min="0" value="8"></label>
<label>Cushion area (cm²)<input id="lf_a" type="number" step="1" min="1" value="1024"></label></div>
<div class="out" aria-live="polite"><div><b id="lf_w">–</b><span>Total mass (g)</span></div><div><b id="lf_p">–</b><span>Pressure to float (Pa)</span></div><div><b id="lf_f">–</b><span>Weight (N)</span></div></div></form>
<p class="small">The default numbers are the team’s example: a 32 cm square hull (1024 cm²), 417 g vehicle, half roll plus 20 nickels, and the dowel. Real skirts waste pressure, so choose a fan whose rated pressure is several times higher than this number (this team’s two failed fans were rated about 51 to 68 Pa and could not lift their own craft, while the blower they chose is rated 370 to 460 Pa).</p>
<h3>Pushing</h3>
<p>A second fan, mounted level and pointed backward, gives thrust. The vehicle floats on almost no friction, so even small thrust accelerates it, and it speeds up until air drag balances thrust. That is why a <b>speed controller</b> matters: the track is short (185 cm) and the score depends on the time, so you need to be able to set the average thrust to hit an exact target such as 10.0 s.</p>
<div class="note warn"><b>Check your numbers.</b> Tune on a hard, smooth floor, wearing eye protection, with the same nickel load you plan to run.</div>

<h2 id="power">Battery and fans</h2>
<p>Batteries in series add voltage; in parallel they add capacity. Two 6 V NiMH packs in series make a 12 V pack, exactly at the rule limit. A fan draws current when it runs, so battery life in hours is about capacity (Ah) ÷ current (A). Real packs give less than that, especially when fans start.</p>
<form class="calc" id="bt" aria-label="Battery calculator"><div class="cg">
<label>Packs in series<input id="bt_s" type="number" step="1" min="1" value="2"></label>
<label>Label voltage of each pack (V)<input id="bt_v" type="number" step="0.1" min="0" value="6"></label>
<label>Capacity (mAh)<input id="bt_c" type="number" step="10" min="1" value="1600"></label>
<label>Lift fan current (A)<input id="bt_l" type="number" step="0.1" min="0" value="3.8"></label>
<label>Thrust fan current (A, at full on)<input id="bt_t" type="number" step="0.1" min="0" value="1.6"></label>
<label>Thrust duty (% of time on)<input id="bt_d" type="number" step="1" min="0" max="100" value="100"></label></div>
<div class="out" aria-live="polite"><div><b id="bt_vo">–</b><span>Pack voltage (V)</span></div><div><b id="bt_i">–</b><span>Average current (A)</span></div><div><b id="bt_r">–</b><span>Ideal run time (min)</span></div><div><b id="bt_ok">–</b><span>Rule limit 12.0 V</span></div></div></form>
<p class="small">Wire thickness matters too. 18 AWG wire carries these currents safely over short runs, and switches should be rated well above the total current (the team used 10 A switches).</p>

<h2 id="relay">Relay timing (speed control without a chip)</h2>
<p>Integrated circuits are banned, but a relay, a resistor and a capacitor can chop the thrust fan on and off several times a second. The capacitor charges through the potentiometer R1 and discharges through the relay coil. The relay clicks over when the capacitor voltage crosses a pull-in level and back at a lower drop-out level. Turning R1 changes how long the relay stays released, which changes the <b>duty cycle</b> (the fraction of time the fan is pushing) and so the average speed.</p>
<div class="tbl"><table><caption class="sr">Relay timing formulas</caption><tr><th>Step</th><th>Formula</th></tr>
<tr><td>Thevenin resistance while charging</td><td>R<sub>Th</sub> = R1 × R<sub>coil</sub> ÷ (R1 + R<sub>coil</sub>)</td></tr>
<tr><td>Voltage ceiling</td><td>V<sub>Th</sub> = V<sub>S</sub> × R<sub>coil</sub> ÷ (R1 + R<sub>coil</sub>)</td></tr>
<tr><td>Released (charging) time</td><td>t<sub>charge</sub> = −R<sub>Th</sub> C ln((V<sub>Th</sub> − V<sub>pull-in</sub>) ÷ (V<sub>Th</sub> − V<sub>drop-out</sub>))</td></tr>
<tr><td>Energised (discharging) time</td><td>t<sub>discharge</sub> = −R<sub>coil</sub> C ln(V<sub>drop-out</sub> ÷ V<sub>pull-in</sub>)</td></tr>
<tr><td>Peak current through R1</td><td>I<sub>peak</sub> = (V<sub>S</sub> − V<sub>drop-out</sub>) ÷ R1</td></tr></table></div>
<form class="calc" id="rl" aria-label="Relay timing calculator"><div class="cg">
<label>Battery voltage V<sub>S</sub> (V)<input id="rl_v" type="number" step="0.1" min="0" value="12"></label>
<label>Potentiometer R1 (Ω)<input id="rl_r" type="number" step="1" min="1" value="40"></label>
<label>Relay coil resistance (Ω, measure it)<input id="rl_c" type="number" step="1" min="1" value="385"></label>
<label>Capacitor C (µF, measure it)<input id="rl_u" type="number" step="1" min="1" value="187"></label>
<label>Pull-in voltage (V, measure it)<input id="rl_p" type="number" step="0.01" min="0" value="7.67"></label>
<label>Drop-out voltage (V, measure it)<input id="rl_d" type="number" step="0.01" min="0" value="2.451"></label></div>
<div class="out" aria-live="polite"><div><b id="rl_tc">–</b><span>Released time (ms)</span></div><div><b id="rl_td">–</b><span>Energised time (ms)</span></div><div><b id="rl_f">–</b><span>Cycles per second</span></div><div><b id="rl_du">–</b><span>Duty (energised share)</span></div><div><b id="rl_ip">–</b><span>Peak current in R1 (A)</span></div></div>
<p id="rl_msg" class="small" aria-live="polite"></p></form>
<div class="note"><b>Units.</b> Resistance in ohms times capacitance in microfarads gives microseconds, so 40 Ω × 187 µF is 7.5 ms. The team’s spreadsheet lists C as 0.187, which only makes sense as millifarads (187 µF), and its outputs are milliseconds. The team’s formula sheet lists a nominal 220 µF while its spreadsheet uses 187 µF, which shows how far a real part can sit from its label, so <b>measure your own parts</b> and re-run the table whenever you change the battery, because a lower battery voltage changes both V<sub>Th</sub> and the timing.</div>
<div class="note warn"><b>Check which phase pushes.</b> Decide whether your fan runs while the relay is energised or while it is released, and read “duty” accordingly. Also make sure the relay contacts and the fan switch can handle the fan’s current, and keep the manual switch required by the rules.</div>

<h2 id="build">Build notes from one team</h2>
<p>These notes come from a team’s parts list and test results. Treat them as ideas to try, not requirements.</p>
<div class="tbl"><table><caption class="sr">Fans tried</caption><tr><th>Role</th><th>Fan</th><th>Airflow</th><th>Pressure</th><th>Speed</th><th>Mass</th><th>Current</th><th>Result</th></tr>
<tr><td>Lift (blower)</td><td>12 V centrifugal blower</td><td>190 CFM</td><td>370 to 460 Pa</td><td>7,000 rpm</td><td>226 g</td><td>3.8 A</td><td>Chosen</td></tr>
<tr><td>Thrust</td><td>THB1212B-AXHF</td><td>185.2 CFM</td><td>223 Pa</td><td>5,300 rpm</td><td>198 g</td><td>1.6 A</td><td>Chosen</td></tr>
<tr><td>Tried</td><td>P12 Pro</td><td>77 CFM</td><td>68 Pa</td><td>3,000 rpm</td><td>183 g</td><td>0.33 A</td><td>Too little airflow to move; poor lift</td></tr>
<tr><td>Tried</td><td>P14</td><td>110 CFM</td><td>51 Pa</td><td>2,500 rpm</td><td>240 g</td><td>0.33 A</td><td>Not enough pressure to fill the skirt and lift itself</td></tr>
<tr><td>Other options</td><td>Large 120 mm thrust fans, a 1,020 Pa blower</td><td>60 to 253 CFM</td><td>102 to 1,020 Pa</td><td>3,000 to 5,500 rpm</td><td>200 to 380 g</td><td>0.5 to 4.8 A</td><td>Not tested here</td></tr></table></div>
<ul><li><b>Power:</b> two 6 V, 1600 mAh NiMH packs in series (12 V), a battery extension lead, a dual charger and the matching charger adapter. Wire connectors (Wago style) make quick, tool-free joints that are easy to change between tests. 18 AWG wire, 10 A switches, and a fan guard on each fan.</li>
<li><b>Hull:</b> 5 mm corrugated plastic is stronger and lighter but hard to cut across the grain with a craft knife. Mat board cuts easily and is good for fan mounts but is heavier and bendier. A 32 × 32 cm hull fits the 40 cm box with room for the skirt.</li>
<li><b>Skirt:</b> thin clear film, like a trash bag, with seams fused using a small sewing or craft iron, attached around the hull edge. Light film inflates easily, so the lift fan does not need as much pressure. Test for leaks and torn seams after every run.</li>
<li><b>Mass:</b> in the example, hull and parts 417 g, one half roll plus 20 nickels about 226 g, dowel 8 g. Weigh your own and use the lift calculator.</li>
<li><b>Tools:</b> a multimeter (to measure coil resistance, capacitor value, voltages), wire stripper, screwdriver, craft knife.</li></ul>

<h2 id="plan">Run-day plan</h2>
<ol><li>At impound: batteries stored separately, one vehicle, your notes. Missing impound costs 30%.</li>
<li>Read the Target Time. Use the timing table to choose the R1 setting before the first run.</li>
<li>Pick the nickel load from your own tests, then check the 3-second rule: it must start moving or the run is incomplete.</li>
<li>Run 1 is your measurement. Compare the time to the target, then adjust R1 and the load for run 2. You only get two runs.</li>
<li>Check for anything that fell off: any lost part or nickel is a construction penalty, and lost nickels do not count.</li></ol>
</div>'''
JS=r'''(function(){"use strict";
function $(i){return document.getElementById(i)}function n(i){var v=parseFloat($(i).value);return isFinite(v)?v:0}
function t(i,s){$(i).textContent=s}function f(x,d){return isFinite(x)?x.toFixed(d):"–"}
function score(){var c=$("sc_c").value==="1",rt=n("sc_t"),tt=Math.max(n("sc_tt"),0.1),d=c?0:Math.min(Math.max(n("sc_d"),0),185),R=Math.min(Math.max(n("sc_r"),0),4)+($("sc_h").value==="1"?0.5:0),N=Math.min(Math.max(n("sc_n"),0),20),ramp=$("sc_p").value==="1";
var ds=c?40:40*(185-d)/185;if(ramp)ds*=0.5;var ts=c?Math.max(0,40*(1-Math.abs(rt-tt)/tt)):0;var ms=ramp?0:(4*R+0.1*N)*(185-d)/185;
var k=Math.pow(0.8,Math.max(0,n("sc_cv")))*Math.pow(0.9,Math.max(0,n("sc_pv")))*($("sc_m").value==="1"?0.7:1);ds*=k;ts*=k;ms*=k;
t("o_ds",f(ds,1));t("o_ts",f(ts,1));t("o_ms",f(ms,1));t("o_rs",f(ds+ts+ms,1));t("o_g",ramp?"0 g (ramp)":f(R*200+N*5,0)+" g")}
function lift(){var m=n("lf_m")+n("lf_n")+n("lf_d"),a=n("lf_a")/10000;t("lf_w",f(m,0));t("lf_f",f(m/1000*9.81,2));t("lf_p",a>0?f(m/1000*9.81/a,0):"–")}
function batt(){var s=Math.max(1,n("bt_s")),v=s*n("bt_v"),i=n("bt_l")+n("bt_t")*Math.min(Math.max(n("bt_d"),0),100)/100,r=i>0?n("bt_c")/1000/i*60:NaN;t("bt_vo",f(v,1));t("bt_i",f(i,2));t("bt_r",f(r,1));t("bt_ok",v<=12.0001?"OK ("+f(v,1)+" V)":"Too high")}
function relay(){var V=n("rl_v"),R1=n("rl_r"),Rc=n("rl_c"),C=n("rl_u")/1e6,Vp=n("rl_p"),Vd=n("rl_d"),msg="";
var Rth=R1*Rc/(R1+Rc),Vth=V*Rc/(R1+Rc),a=(Vth-Vp)/(Vth-Vd);var tc=NaN;
if(Vd<=0||Vp<=Vd){msg="Pull-in voltage must be higher than drop-out voltage."}else if(Vth<=Vp){msg="With these values the capacitor can never reach the pull-in voltage (V_Th "+f(Vth,2)+" V is not above "+f(Vp,2)+" V), so the relay will not cycle. Lower R1 or raise the battery voltage."}else{tc=-Rth*C*Math.log(a)*1000}
var td=-Rc*C*Math.log(Vd/Vp)*1000,per=tc+td;
t("rl_tc",f(tc,1));t("rl_td",f(td,1));t("rl_f",per>0?f(1000/per,1):"–");t("rl_du",per>0?f(td/per*100,0)+"%":"–");t("rl_ip",R1>0?f((V-Vd)/R1,2):"–");$("rl_msg").textContent=msg}
var map={sc:score,lf:lift,bt:batt,rl:relay};Object.keys(map).forEach(function(k){var fm=$(k);if(!fm)return;fm.addEventListener("input",map[k]);fm.addEventListener("submit",function(e){e.preventDefault()});map[k]()})})();
'''
