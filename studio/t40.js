const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:880}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message+' '+(x.stack||'').split('\n').slice(0,3).join('|')));
await p.goto('file://'+process.cwd()+'/out/axiom/app/apex/index.html');await p.waitForTimeout(500);
// policy sample
const pol=await p.evaluate(()=>{const c={0:0,1:0,2:0};QS.forEach(q=>c[calcPolicy(q)]++);return c});console.log('apex policy',pol);
// start a practice with a tg question
await p.evaluate(()=>{const q=QS.find(q=>calcPolicy(q)===2);startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(400);
console.log('buttons',await p.evaluate(()=>[...document.querySelectorAll('#tbar button,#tbar .tnone')].map(b=>b.id||b.className)));
await p.click('#tgraph');await p.waitForTimeout(300);await p.fill('[data-f="0"]','sin(x)');await p.fill('[data-f="1"]','a*x^2/10');await p.waitForTimeout(200);await p.screenshot({path:'shots/calc_graph.png'});
await p.click('[data-tab=calc]');await p.waitForTimeout(150);await p.fill('#tin','sqrt(2)*3+2^3');await p.waitForTimeout(150);await p.screenshot({path:'shots/calc_sci.png'});console.log(await p.textContent('#tres'),e);
await b.close()})()
