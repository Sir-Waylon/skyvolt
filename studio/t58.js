const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
for(const kind of ['practice','mission','plan']){
await p.evaluate(k=>{if(k==='practice')startPractice(ALL,6);else if(k==='mission')startMission();else document.querySelector('[data-plan="go"]').click()},kind);await p.waitForTimeout(500);
const out=[];for(let k=0;k<5;k++){const r=await p.evaluate(()=>{if(!Z||Z.fin)return null;const st=Z.steps[Z.i];if(st.k==='card'){document.getElementById('nx')&&document.getElementById('nx').click();return 'card'}const it=st.it;if(it.q.type==='mcq'){it.sel=[0];resolveIt(it);drawSess();}else{ if(window.__sbxSolve&&it.q.type==='sbx')__sbxSolve(it);else it.done=true;resolveIt&&it.done!==true&&resolveIt(it);drawSess()}return it.q.type});
 if(!r)break;await p.waitForTimeout(150);await p.evaluate(()=>{const n=document.getElementById('nx');if(n&&!n.disabled)n.click()});await p.waitForTimeout(250);
 out.push(await p.evaluate(()=>[Z.doneM,Z.mains,(document.querySelector('.prog i')||{style:{}}).style.width]).catch(()=>'x'))}
console.log(kind,JSON.stringify(out));await p.evaluate(()=>{window.closeSess&&closeSess()});await p.waitForTimeout(200)}
console.log(e);await b.close();process.exit(0)})()
