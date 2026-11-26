# -*- coding: utf-8 -*-
"""Interactive homepage cards (predict, manipulate, explain). Cards per site, plus the JS and CSS. Written to the question-design rules in src/docs/QUESTION_RULES.md."""
import json,html,random,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','src_geo'))
def _opts(good,bad,seed):
    o=[good]+bad;random.Random(seed).shuffle(o);return o
# id: (track index, topic label, tier tag, question, good, [diagnostic distractors], explanation, sliders desc handled in JS)
DEMOS={
'ohm':(0,'Ohm’s law','Tier 11',"A battery drives a current through a resistor. You swap in a resistor with TWICE the resistance and keep the same battery. Predict the current, then drag R to check.",
 'It halves',['It doubles','It stays the same','It drops to one quarter'],
 "Current = voltage ÷ resistance, so doubling R halves I. Trap: ‘it quarters’ confuses current with power, which also depends on I (P = V²/R halves too here, because V is fixed)."),
'par':(0,'Parallel resistors','Tier 7',"Two resistors are connected in parallel. You add a third path by raising R2 to a very large value, then lower it. Predict: how does the total resistance compare with the SMALLEST single resistor?",
 'Always smaller than the smallest one',['Equal to the sum of them','Equal to the average of them','Larger than the smallest one'],
 "Every extra parallel path gives current one more route, so the total resistance falls below the smallest branch. Trap: adding resistances is the SERIES rule."),
'hov':(0,'Hovercraft lift','Tier 12',"A hovercraft hull has a fixed cushion area. You load it with more nickels. Predict: what happens to the air pressure the lift fan must supply?",
 'It must increase in proportion to the total mass',['It stays the same because the area is the same','It decreases because there is more weight on the skirt','It depends only on fan speed, not mass'],
 "Pressure to float = weight ÷ cushion area. Same area, more weight means more pressure. Trap: pressure is set by weight and area together, so a bigger area lowers it."),
'lcl':(1,'Cloud base height','Tier 11',"On a hot, dry afternoon the temperature is far above the dew point. On a humid morning the two are almost equal. Predict: where will rising surface air first form cloud?",
 'Much higher on the dry afternoon',['Lower on the dry afternoon','At the same height both times','Only on the humid morning, never on the dry afternoon'],
 "Rising air cools about 9.8 °C per km, and the dew point falls about 1.8 °C per km, so the gap closes at roughly 8 °C per km. Cloud base is about 125 m for every degree of gap. Trap: a big gap means the air must climb further to saturate."),
'quad':(0,'Quadratics and the discriminant','Tier 14',"The parabola y = x² + bx + c has two sliders. Predict: which condition makes it touch the x-axis at exactly ONE point?",
 'b² − 4c = 0',['c = 0','b = c','b = 0'],
 "One touching point means the quadratic has a double root, which happens exactly when the discriminant b² − 4c is zero. Trap: c = 0 puts one intercept at the origin but the other is at x = −b, so there are usually two."),
'pyth':(0,'Pythagorean theorem','Tier 12',"A right triangle has legs a and b. Predict: if BOTH legs are doubled, what happens to the hypotenuse?",
 'It doubles',['It quadruples','It increases by 2 units','It increases by √2 times'],
 "c = √(a² + b²). Doubling both legs gives √(4a² + 4b²) = 2c, so the whole triangle just scales by 2. Trap: the AREA quadruples, but lengths only double."),
'lever':(1,'Levers and torque','Tier 12',"A heavy load sits near a lever’s pivot. You can only push with a small force. Predict: where should you push to balance it?",
 'Far from the pivot',['Close to the pivot','Directly at the pivot','Anywhere, because force is all that matters'],
 "Balance needs force × distance equal on both sides. A small force needs a long distance. Trap: forces alone do not balance a lever, the turning effect (force × distance) does."),
'proj':(1,'Projectile range','Tier 16',"A ball is launched from the ground at a fixed speed. Ignore air. Predict: which launch angle sends it farthest across level ground?",
 '45°',['30°','60°','90°'],
 "Range = v² sin 2θ ÷ g, which is biggest when sin 2θ = 1, at θ = 45°. Trap: 90° goes highest but not far; 30° and 60° travel the same distance as each other."),
}
SITE={'Skyvolt':['ohm','par','hov','lcl'],'Axiom':['quad','pyth','lever','proj']}
def demo_cards(site):
    out=[]
    for d in SITE[site]:
        pi,topic,tier,q,good,bad,why=DEMOS[d]
        bt=''.join(f'<button type="button" class="tqb"{" data-ok=1" if x==good else ""}>{html.escape(x)}</button>' for x in _opts(good,bad,d))
        out.append((pi,f'<article class="tq tqd" data-demo="{d}" aria-label="Interactive: {html.escape(topic)}"><p class="tqm"><span class="pill tr{pi}">{html.escape(topic)}</span> <span class="pill">Interactive</span> <span class="pill">{tier}</span></p><p class="tqq">{html.escape(q)}</p><div class="tqo" role="group" aria-label="Predict">{bt}</div><div class="dm" data-for="{d}"><noscript><p class="small mute">Turn on JavaScript to use the sliders.</p></noscript></div><div class="tqf" role="status" aria-live="polite" hidden><b></b> <span>{html.escape(why)}</span></div></article>'))
    return out
# ---- interactive proofs (Axiom) ----
PROOFS=[
dict(title='Vertical angles are equal',given='Lines ℓ and m cross. ∠1 and ∠3 are vertical angles, ∠2 lies between them.',prove='∠1 ≅ ∠3',
 rows=[('∠1 and ∠2 form a linear pair','Definition of linear pair'),('m∠1 + m∠2 = 180°','Linear pair postulate'),('∠3 and ∠2 form a linear pair','Definition of linear pair'),('m∠3 + m∠2 = 180°','Linear pair postulate'),('m∠1 + m∠2 = m∠3 + m∠2','Substitution'),('m∠1 = m∠3','Subtraction property of equality')],
 h1='Both angles are supplements of the SAME angle. What fact about that angle can you use twice?',h2='Use the linear-pair postulate for ∠1 with ∠2, and for ∠3 with ∠2, then compare.',trap='Do not use “vertical angles are equal” as a reason, because that is what you are proving.'),
dict(title='Base angles of an isosceles triangle are equal',given='△ABC with AB = AC, and D is the midpoint of BC.',prove='∠B ≅ ∠C',
 rows=[('Draw segment AD','Two points determine a line'),('BD = DC','Definition of midpoint'),('AB = AC','Given'),('AD = AD','Reflexive property'),('△ABD ≅ △ACD','SSS'),('∠B ≅ ∠C','CPCTC')],
 h1='To show two angles equal, put them in two triangles you can prove congruent.',h2='Three pairs of sides match. Which congruence rule uses three sides?',trap='CPCTC is the LAST step. You may use it only after the triangles are proven congruent.'),
dict(title='The sum of two even numbers is even',given='a and b are even integers.',prove='a + b is even',
 rows=[('a = 2m and b = 2n for some integers m and n','Definition of an even number'),('a + b = 2m + 2n','Substitution'),('a + b = 2(m + n)','Distributive property'),('m + n is an integer','Closure of the integers under addition'),('a + b is even','Definition of an even number')],
 h1='Turn the word “even” into an equation you can work with.',h2='An even number is 2 times an integer. Write each number that way, add, and factor out the 2.',trap='Picking two example numbers like 4 + 6 shows it can work. It does not prove it for every pair.'),
]
POOL=['Definition of linear pair','Linear pair postulate','Substitution','Subtraction property of equality','Reflexive property','Definition of midpoint','Given','SSS','SAS','CPCTC','Two points determine a line','Distributive property','Definition of an even number','Closure of the integers under addition','Transitive property','Addition property of equality','Vertical angles theorem','Alternate interior angles are congruent']
def proof_cards():
    out=[]
    for k,p in enumerate(PROOFS):
        rows=[]
        for i,(s,r) in enumerate(p['rows']):
            bad=[x for x in POOL if x!=r];random.Random(f'{k}{i}').shuffle(bad)
            # the circular reason is a diagnostic trap for the first proof
            if p['title'].startswith('Vertical') and 'Vertical angles theorem' not in bad[:3]:bad=['Vertical angles theorem']+bad
            o=_opts(r,bad[:3],f'{k}-{i}');rows.append(dict(s=s,o=o,a=o.index(r)))
        d=dict(t=p['title'],g=p['given'],p=p['prove'],r=rows,h1=p['h1'],h2=p['h2'],trap=p['trap'])
        out.append(f'<article class="tq tqd tqp" data-demo="proof" data-proof="{html.escape(json.dumps(d,ensure_ascii=False),quote=True)}" aria-label="Interactive proof: {html.escape(p["title"])}"><p class="tqm"><span class="pill tr0">Proof</span> <span class="pill">Interactive</span> <span class="pill">Tier {8+k*3}</span></p><div class="dm" data-for="proof"><noscript><p class="small mute">Turn on JavaScript to build this proof.</p></noscript></div></article>')
    return out
CSS='''
.tqd .dm{margin:6px 0 4px}.dm svg{display:block;width:100%;max-width:420px;height:auto;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:12px}
.dm .dsl{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px 16px;margin:10px 0}.dm .dsl label{display:block;font-weight:600;font-size:.9rem}.dm .dsl output{font-weight:700;color:var(--pri)}.dm input[type=range]{display:block;width:100%;min-height:44px;margin:2px 0 0;accent-color:var(--pri)}
.dm .dro{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}.dm .dro div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:6px 10px;font-size:.9rem}.dm .dro b{font-size:1.1rem}.dm .dhint{font-size:.9rem;color:var(--mut)}
.dm .pf{list-style:none;margin:8px 0;padding:0}.dm .pf li{display:grid;grid-template-columns:1.6rem 1fr;gap:4px 8px;padding:8px;border-bottom:1px solid var(--line)}.dm .pf .pn{font-weight:700;color:var(--mut)}.dm .pf select{grid-column:2;min-height:44px;width:100%;box-sizing:border-box;border:2px solid var(--line);border-radius:10px;background:var(--card);color:var(--tx);font:inherit;padding:6px 8px}
.dm .pf li.good select{border-color:#1a7f4b}.dm .pf li.bad select{border-color:#b3261e}.dm .pbt{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}.dm .pbt .btn{font:inherit;font-weight:700;min-height:44px}.dm .pm{margin:6px 0;font-size:.95rem;line-height:1.5}
.dm .gp{stroke:var(--pri)}
'''
JS=r'''(function(){"use strict";var NS="http://www.w3.org/2000/svg";
function E(t,a,p,x){var e=document.createElementNS(NS,t);for(var k in a)e.setAttribute(k,a[k]);if(x!=null)e.textContent=x;if(p)p.appendChild(e);return e}
function H(t,a,p,x){var e=document.createElement(t);for(var k in a)e.setAttribute(k,a[k]);if(x!=null)e.textContent=x;if(p)p.appendChild(e);return e}
var W=320,Hh=170;
function lin(g,x1,y1,x2,y2,c,w){return E("line",{x1:x1,y1:y1,x2:x2,y2:y2,stroke:c||"currentColor","stroke-width":w||2,"stroke-linecap":"round"},g)}
function tx(g,x,y,s,a,sz){return E("text",{x:x,y:y,"text-anchor":a||"middle","font-size":sz||12,fill:"currentColor"},g,s)}
var D={
ohm:{s:[["V","Battery voltage","V",1,24,1,12],["R","Resistance","Ω",10,200,10,60]],f:function(v){var I=v.V/v.R;return{o:[["Current",(I*1000).toFixed(0)+" mA"],["Power",(v.V*I).toFixed(2)+" W"]],d:function(g){
 E("rect",{x:20,y:50,width:30,height:70,rx:4,fill:"none",stroke:"currentColor","stroke-width":2},g);tx(g,35,90,v.V+" V");lin(g,35,50,35,30);lin(g,35,30,285,30);lin(g,285,30,285,60);lin(g,285,110,285,140);lin(g,285,140,35,140);lin(g,35,140,35,120);
 var p="285,60 275,68 295,76 275,84 295,92 275,100 285,108";E("polyline",{points:p,fill:"none",stroke:"currentColor","stroke-width":2},g);tx(g,230,88,v.R+" Ω","end");
 var n=Math.max(1,Math.round(I*18));for(var i=0;i<n;i++)E("circle",{cx:60+(i+0.5)*(210/n),cy:30,r:4,fill:"#e0a800"},g);tx(g,160,20,"Current flow: more dots = more current")}}}},
par:{s:[["R2","Second resistor R2","Ω",20,400,10,100]],f:function(v){var r1=100,q=r1*v.R2/(r1+v.R2);return{o:[["R1","100 Ω"],["R2",v.R2+" Ω"],["Total (parallel)",q.toFixed(1)+" Ω"]],d:function(g){
 var bars=[["R1",r1],["R2",v.R2],["Total",q]],cs=["#2D6A4F","#0077B6","#e0a800"];bars.forEach(function(b,i){var w=b[1]/400*220;E("rect",{x:60,y:25+i*42,width:w,height:26,fill:cs[i],rx:3},g);tx(g,52,43+i*42,b[0],"end");tx(g,66+w,43+i*42,Math.round(b[1])+" Ω","start")});}}}},
hov:{s:[["m","Total mass","g",300,1200,10,640],["A","Cushion area","cm²",400,1600,50,1024]],f:function(v){var P=v.m/1000*9.81/(v.A/10000);return{o:[["Pressure needed",P.toFixed(0)+" Pa"],["Weight",(v.m/1000*9.81).toFixed(2)+" N"]],d:function(g){
 var x=Math.min(P,500)/500*240;E("rect",{x:40,y:70,width:240,height:22,fill:"none",stroke:"currentColor","stroke-width":1.5},g);E("rect",{x:40,y:70,width:x,height:22,fill:P>370?"#b3261e":"#2D6A4F"},g);
 lin(g,40+68/500*240,60,40+68/500*240,104,"#b3261e",2);tx(g,40+68/500*240,54,"weak fan 68 Pa");lin(g,40+370/500*240,60,40+370/500*240,104,"#0077B6",2);tx(g,40+370/500*240,54,"blower 370 Pa");tx(g,160,130,"Pressure to float = weight ÷ area");tx(g,160,150,"0 Pa .......................... 500 Pa")}}}},
lcl:{s:[["T","Air temperature","°C",10,40,1,32],["Td","Dew point","°C",0,30,1,8]],f:function(v){var T=v.T,Td=Math.min(v.Td,v.T),sp=T-Td,h=125*sp;return{o:[["Gap",sp+" °C"],["Cloud base",Math.round(h)+" m"]],d:function(g){
 var y=Math.max(18,150-h/4000*125);E("rect",{x:0,y:150,width:W,height:20,fill:"#7aa66a"},g);lin(g,0,150,W,150,"currentColor",1);
 [[120,y],[160,y-6],[205,y],[150,y+6]].forEach(function(c){E("ellipse",{cx:c[0],cy:c[1],rx:38,ry:13,fill:"#cfd8dc",stroke:"#78909c"},g)});
 lin(g,40,148,40,y+14,"#b3261e",2);tx(g,40,y+8,"↑ rising air","start",11);tx(g,285,100,Math.round(h)+" m","end",14);tx(g,285,118,"cloud base","end",11)}}}},
quad:{s:[["b","b (x coefficient)","",-6,6,0.5,0],["c","c (constant)","",-4,8,0.5,-4]],f:function(v){var D2=v.b*v.b-4*v.c,n=D2>1e-9?2:(Math.abs(D2)<1e-9?1:0);return{o:[["Discriminant b² − 4c",D2.toFixed(2)],["x-intercepts",n+""]],d:function(g){
 var X=function(x){return 160+x*24},Y=function(y){return 150-(y+3)*13};lin(g,0,Y(0),W,Y(0),"#888",1);lin(g,X(0),0,X(0),Hh,"#888",1);var pts=[];for(var x=-6.5;x<=6.5;x+=0.25){var y=x*x+v.b*x+v.c;if(y<-3.2||y>9.8)continue;pts.push(X(x).toFixed(1)+","+Y(y).toFixed(1))}
 E("polyline",{points:pts.join(" "),fill:"none",stroke:"#BC4749","stroke-width":2.5},g);if(n>0){var r=[(-v.b-Math.sqrt(Math.max(D2,0)))/2,(-v.b+Math.sqrt(Math.max(D2,0)))/2];r.forEach(function(x){E("circle",{cx:X(x),cy:Y(0),r:5,fill:"#e0a800",stroke:"#000"},g)})}}}}},
pyth:{s:[["a","Leg a","",1,12,1,3],["b","Leg b","",1,12,1,4]],f:function(v){var c=Math.sqrt(v.a*v.a+v.b*v.b),k=Math.min(12,150/Math.max(v.a,v.b,1))*0.8;return{o:[["Hypotenuse c",c.toFixed(2)],["a² + b²",(v.a*v.a+v.b*v.b)+""]],d:function(g){
 var x0=60,y0=150,pa=[x0,y0],pb=[x0+v.b*k,y0],pc=[x0,y0-v.a*k];E("polygon",{points:pa+" "+pb+" "+pc,fill:"rgba(188,71,73,.15)",stroke:"currentColor","stroke-width":2},g);E("polyline",{points:(x0+10)+","+y0+" "+(x0+10)+","+(y0-10)+" "+x0+","+(y0-10),fill:"none",stroke:"currentColor"},g);tx(g,x0-8,y0-v.a*k/2,"a="+v.a,"end");tx(g,x0+v.b*k/2,y0+14,"b="+v.b);tx(g,x0+v.b*k/2+16,y0-v.a*k/2-4,"c="+c.toFixed(1),"start")}}}},
lever:{s:[["F","Your push","N",10,120,5,40],["d","Distance from pivot","m",0.2,4,0.1,1]],f:function(v){var L=60*2,R=v.F*v.d,diff=R-L,bal=Math.abs(diff)/L<0.03,ang=Math.max(-14,Math.min(14,diff/L*20));return{o:[["Load turning effect","60 N × 2 m = 120 N·m"],["Your turning effect",R.toFixed(0)+" N·m"],["Result",bal?"Balanced":(diff<0?"Load wins":"You win")]],d:function(g){
 E("polygon",{points:"160,150 148,166 172,166",fill:"currentColor"},g);var gg=E("g",{transform:"rotate("+ang+" 160 148)"},g);lin(gg,40,148,280,148,"currentColor",5);E("rect",{x:85,y:118,width:30,height:30,fill:"#0077B6"},gg);tx(gg,100,136,"60 N","middle",10);tx(gg,160+Math.min(v.d,4)*30,138,v.F+" N","middle",11);lin(gg,160+v.d*30,120,160+v.d*30,146,"#BC4749",3)}}}},
proj:{s:[["a","Launch angle","°",5,85,1,30]],f:function(v){var u=20,g=10,r=u*u*Math.sin(2*v.a*Math.PI/180)/g,hm=Math.pow(u*Math.sin(v.a*Math.PI/180),2)/(2*g);return{o:[["Range",r.toFixed(1)+" m"],["Max height",hm.toFixed(1)+" m"]],d:function(g2){
 var k=250/40;lin(g2,30,150,290,150,"currentColor",1.5);var pts=[];for(var t=0;t<=3;t+=0.05){var x=u*Math.cos(v.a*Math.PI/180)*t,y=u*Math.sin(v.a*Math.PI/180)*t-5*t*t;if(y<0)break;pts.push((30+x*k).toFixed(1)+","+(150-y*k*0.9).toFixed(1))}
 E("polyline",{points:pts.join(" "),fill:"none",stroke:"#0F4C5C","stroke-width":2.5},g2);E("circle",{cx:30+r*k,cy:150,r:5,fill:"#e0a800",stroke:"#000"},g2);tx(g2,160,168,"Same launch speed (20 m/s). Distance scale: 40 m across.","middle",10)}}}}
};
function build(c){var id=c.getAttribute("data-demo"),box=c.querySelector(".dm");if(!box||box.dataset.b)return;box.dataset.b=1;
 if(id==="proof"){proof(c,box);return}
 var cfg=D[id];if(!cfg)return;var svg=E("svg",{viewBox:"0 0 "+W+" "+Hh,role:"img","aria-label":"Interactive diagram"},null);box.appendChild(svg);var ro=H("div",{"class":"dro","aria-live":"polite"},box),sl=H("div",{"class":"dsl"},box),val={};
 cfg.s.forEach(function(s,i){var lb=H("label",{"for":id+"s"+i},sl,s[1]+" ");var o=H("output",{},lb,s[6]+" "+s[2]);var inp=H("input",{type:"range",id:id+"s"+i,min:s[3],max:s[4],step:s[5],value:s[6]},sl);val[s[0]]=s[6];
  inp.addEventListener("input",function(){val[s[0]]=Number(inp.value);o.textContent=inp.value+" "+s[2];draw()})});
 H("p",{"class":"dhint"},box,"Drag the sliders. The picture and numbers change at once.");
 function draw(){var r=cfg.f(val);while(svg.firstChild)svg.removeChild(svg.firstChild);var g=E("g",{},svg);r.d(g);while(ro.firstChild)ro.removeChild(ro.firstChild);r.o.forEach(function(x){var d=H("div",{},ro,x[0]+": ");H("b",{},d,x[1])})}draw()}
function proof(c,box){var d=JSON.parse(c.getAttribute("data-proof")),sel=[];
 H("h3",{"class":"tqh"},box,d.t);H("p",{"class":"pm"},box,"Given: "+d.g);H("p",{"class":"pm"},box,"Prove: "+d.p);H("p",{"class":"dhint"},box,"Pick the reason that justifies each step.");
 var ol=H("ol",{"class":"pf"},box);d.r.forEach(function(r,i){var li=H("li",{},ol);H("span",{"class":"pn"},li,(i+1)+".");var l=H("label",{"for":"pf"+i+d.t.length},li,r.s);var s=H("select",{id:"pf"+i+d.t.length,"aria-label":"Reason for step "+(i+1)},li);H("option",{value:""},s,"Choose a reason…");r.o.forEach(function(o,j){H("option",{value:j},s,o)});sel.push([s,li,r])});
 var bt=H("div",{"class":"pbt"},box),ck=H("button",{type:"button","class":"btn"},bt,"Check my proof"),h=H("button",{type:"button","class":"btn sec"},bt,"Hint"),msg=H("p",{"class":"pm",role:"status","aria-live":"polite"},box),lv=0;
 h.addEventListener("click",function(){lv=Math.min(2,lv+1);msg.textContent="Hint "+lv+": "+(lv===1?d.h1:d.h2);if(lv===2)h.disabled=true});
 ck.addEventListener("click",function(){var ok=0;sel.forEach(function(x){var v=x[0].value,good=v!==""&&Number(v)===x[2].a;x[1].className=v===""?"":(good?"good":"bad");if(good)ok++});
  msg.textContent=ok===sel.length?"Complete proof! Watch out: "+d.trap:ok+" of "+sel.length+" reasons are right. Fix the red ones, or ask for a hint. Errors are useful clues, not failures."});}
[].forEach.call(document.querySelectorAll(".tqd"),build)})();
'''
