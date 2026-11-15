const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{const base=QS[0];const mk=(id,o)=>{const q=Object.assign({},base,{id:id,type:o.type,q:o.q,sol:['Step one.','Step two.'],w:'Because.'},o);delete q.o;delete q.text;delete q.num;QS.push(q);QI[id]=QS.length-1};
 mk('c1',{type:'compass',q:'The wind is blowing FROM the southwest. Drag the pointer to the direction the wind comes from.',cmp:{target:225,tol:10}});
 mk('g1',{type:'graph',q:'A capacitor charges through a resistor. Tap the point where the voltage reaches 63% of the 10 V supply.',gr:{xl:'Time (ms)',yl:'Voltage (V)',x:[0,50],y:[0,10],lines:[{l:'Vc',pts:[0,5,10,15,20,25,30,35,40,45,50].map(t=>[t,10*(1-Math.exp(-t/10))])}],hl:[{y:10,l:'supply'}],t:[10,6.32],tx:3,ty:.6,desc:'Capacitor voltage rising from 0 to 10 volts over 50 milliseconds'}})});
for(const id of ['c1','g1']){await p.evaluate(i=>{startSess({kind:'practice',title:'Practice',steps:[{k:'try',it:mkItem(i)}]})},id);await p.waitForTimeout(150);
 if(id==='c1'){await p.focus('#cpsv');for(let i=0;i<5;i++)await p.keyboard.press('ArrowRight');await p.fill('#cpin','222');}
 else{await p.fill('#grx','10');await p.fill('#gry','6.3');await p.click('#grset');await p.waitForTimeout(100)}
 console.log(id,await p.evaluate(()=>{const it=Z.steps[0].it;return [it.val,it.pt,IT[it.q.type].ok(it)]}));await p.screenshot({path:'ck/it2_'+id+'.png'});await p.evaluate(()=>closeSess())}
console.log(e);await b.close()})()
