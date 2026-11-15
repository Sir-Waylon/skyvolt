const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push((x.stack||x.message).split('\n').slice(0,3).join(' | ')));await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>startMission());await p.waitForTimeout(400);
const log=[];let last=-1;
for(let k=0;k<60;k++){const r=await p.evaluate(()=>{if(typeof Z==='undefined'||!Z)return {end:1};if(Z.fin)return {fin:1,w:document.querySelector('.prog i')?.style.width};
 const st=Z.steps[Z.i];const o={k:st.k,i:Z.i,d:Z.doneM,m:Z.mains,w:document.querySelector('.prog i')?.style.width};
 for(const id of ['go','exs','exb','exf','exq','nx']){const el=document.getElementById(id);if(el&&!el.disabled&&id!=='exq'){el.click();o.c=id;return o}}
 const it=st.it;if(it&&it.q){try{if(it.q.type==='mcq'){it.sel=[0];resolveIt(it)}else if(window.__sbxSolve&&it.q.type==='sbx')__sbxSolve(it);else if(window.__gmSolve)__gmSolve(it);drawSess();o.s=it.q.type}catch(x){o.err=x.message}}return o});
 log.push(JSON.stringify(r));if(r.end||r.fin)break;await p.waitForTimeout(120)}
console.log(log.join('\n'));console.log(e.slice(0,4));await b.close();process.exit(0)})()
