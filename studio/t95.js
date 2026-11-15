const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(4000);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;QS.slice(0,6).forEach((q,i)=>{S.mem[q.id]=[i%3,dayN()-2+BOX[i%3],2]});route();startMission()});await p.waitForTimeout(900);
await p.waitForTimeout(900);await p.screenshot({path:'shots/t95_a.png'});
// run through remaining quickly answering first option sure
for(let g=0;g<250;g++){const r=await p.evaluate(()=>{if(!Z||Z.fin)return 'fin';const s=Z.steps[Z.i];return s.k});if(r==='fin')break;
 await p.evaluate(()=>{const s=Z.steps[Z.i];if(s.k==='card'){document.getElementById('go').click();return}if(s.k==='explain'){const e=document.querySelector('#exf,#exb,#exs,#exq,#exn');e&&e.click();return}
  const it=s.it;if(!it.done){const cf=document.querySelector('[data-cf="s"]');cf&&cf.click();const q=it.q;if(q.type==='mcq'){const o=document.querySelector('[data-oi]');o&&o.click()}else{const i=document.getElementById('sv');if(i){i.value='0';i.dispatchEvent(new Event('input',{bubbles:true}))}}const c=document.getElementById('chk');if(c&&!c.disabled)c.click()}else{const n=document.getElementById('nx');n&&n.click()}});await p.waitForTimeout(30)}
console.log(await p.evaluate(()=>JSON.stringify({rqflag:Z.rq,kind:Z.kind,st:Z.steps.map(s=>s.k[0]+(s.it?(s.it.done?(s.it.ok?'+':'-'):'.'):'')+(s.lock||'')+(s.follow?'f':'')).join(' ')})));console.log(await p.evaluate(()=>JSON.stringify({cal:S.cal,hyper:Object.keys(S.hyper).length,rq:Z.steps.filter(s=>s.lock===2).length,n:Z.steps.length,pct:Z.pct})));await p.screenshot({path:'shots/t95_c.png'});console.log(E.slice(0,3));await b.close()})()
