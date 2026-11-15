const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
for(const kind of ['mission','mock','practice']){
await p.evaluate(k=>{if(k==='practice')startPractice(ALL,8);else if(k==='mock')startMock();else startMission()},kind);await p.waitForTimeout(400);
const ws=[];for(let k=0;k<80;k++){const r=await p.evaluate(()=>{if(!Z)return 'end';if(Z.fin)return 'fin';const st=Z.steps[Z.i];if(st.it&&!st.it.done&&Z.kind!=='mock'){try{st.it.q.type==='mcq'&&(st.it.sel=[0]);resolveIt(st.it)}catch(x){}}advance();return (document.querySelector('.prog i')||{style:{}}).style.width});
 if(r==='end'||r==='fin'){ws.push(r+':'+await p.evaluate(()=>Z&&document.querySelector('.prog i').style.width));break}ws.push(Math.round(parseFloat(r)||0))}
console.log(kind,ws.join(','));await p.evaluate(()=>{Z=null;document.getElementById('sess')&&document.getElementById('sess').remove()})}
console.log(e.slice(0,3));await b.close();process.exit(0)})()
