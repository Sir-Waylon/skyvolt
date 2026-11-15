const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,vp] of [['_app_axiom/apex',{width:360,height:640}],['_app_skyvolt/circuit',{width:360,height:640}],['_app_skyvolt/meteorology',{width:320,height:568}]]){
const p=await (await b.newContext({viewport:vp})).newPage();p.setDefaultTimeout(3000);const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>startPractice(ALL,12));await p.waitForTimeout(400);
let worst=0,n=0,hits=[];
for(let k=0;k<12;k++){
 for(const phase of ['ask','fb']){
  if(phase==='fb')await p.evaluate(()=>{const st=Z.steps[Z.i];if(st&&st.it&&!st.it.done){try{if(st.it.q.type==='mcq')st.it.sel=[0];resolveIt(st.it)}catch(x){}}});
  await p.waitForTimeout(450);
  const r=await p.evaluate(()=>{const s=document.getElementById('sess');if(!s)return null;s.scrollTo(0,s.scrollHeight);const vh=innerHeight;
   const cover=[...document.querySelectorAll('.sheet,.tbar,.devchip')].filter(e=>e.getBoundingClientRect().height>0).map(e=>({c:e.className,top:e.getBoundingClientRect().top,h:e.getBoundingClientRect().height}));
   const body=s.querySelector('.s-body');const kids=[...body.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().height>0&&!e.closest('.sheet'));const lb=Math.max(...kids.map(e=>e.getBoundingClientRect().bottom));
   const sheet=document.querySelector('.sheet');const st=sheet?sheet.getBoundingClientRect().top:vh;
   const sb=sheet?[...sheet.querySelectorAll('button')].map(x=>x.getBoundingClientRect().bottom).reduce((a,c)=>Math.max(a,c),0):0;
   return {lb:Math.round(lb),sheetTop:Math.round(st),sheetBtnBottom:Math.round(sb),vh,cover:cover.map(c=>c.c+':'+Math.round(c.top))}});
  if(r){n++;if(r.lb>r.sheetTop+1)hits.push(phase+' last content '+r.lb+' under sheet top '+r.sheetTop);if(r.sheetBtnBottom>r.vh+1)hits.push('sheet buttons off-screen '+r.sheetBtnBottom);if(k===0)console.log(app,phase,JSON.stringify(r))}
 }
 await p.evaluate(()=>{if(Z&&!Z.fin)advance()});
}
console.log(app,'checked',n,'hits',hits.slice(0,6),e.slice(0,2));await p.close()}
await b.close()})()
