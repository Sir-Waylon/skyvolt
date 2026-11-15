const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [w,h] of [[360,640],[1280,800]]){
const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.waitForTimeout(300);await p.screenshot({path:`shots/t82_${w}_today.png`});
await p.evaluate(()=>startMission());await p.waitForTimeout(400);await p.screenshot({path:`shots/t82_${w}_sess.png`});
await p.evaluate(()=>{let g=0;while(Z&&!Z.fin&&g++<40){const st=Z.steps[Z.i];if(st.k==='card'&&!window.__shown){window.__shown=1;break}advance()}});await p.waitForTimeout(300);await p.screenshot({path:`shots/t82_${w}_card.png`});
await p.evaluate(()=>{let g=0;while(Z&&!Z.fin&&Z.steps[Z.i].k!=='try'&&g++<40)advance();const it=Z.steps[Z.i].it;if(it&&it.q.type==='mcq'){it.sel=[it.q.a===0?1:0];}});
await p.evaluate(()=>{window.__x=1});
await p.evaluate(()=>{let g=0;while(Z&&!Z.fin&&g++<60){const st=Z.steps[Z.i];if(st.it&&!st.it.done)try{resolveIt(st.it)}catch(e){}advance()}});await p.waitForTimeout(500);await p.screenshot({path:`shots/t82_${w}_sum.png`});
console.log(w,E);await p.close()}
await b.close()})()
