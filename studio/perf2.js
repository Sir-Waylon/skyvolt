const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']]){
 const ctx=await b.newContext({viewport:{width:390,height:800}});const p=await ctx.newPage();const c=await ctx.newCDPSession(p);await c.send('Emulation.setCPUThrottlingRate',{rate:4});await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(500);
 await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route();window.__lt=[];new PerformanceObserver(l=>l.getEntries().forEach(e=>window.__lt.push(Math.round(e.duration)))).observe({entryTypes:['longtask']})});
 const t0=Date.now();
 const r=await p.evaluate(async()=>{const times=[];const ids=QS.filter(q=>q.type==='short'&&q.num).slice(0,6).map(q=>q.id);
  for(const id of ids){const q=QS.find(x=>x.id===id);q.keep=true;let t=performance.now();startSess({kind:'practice',title:'P',steps:[{k:'try',it:mkItem(id)}]});const a=performance.now()-t;
   await new Promise(r=>setTimeout(r,60));const inp=document.getElementById('sv');t=performance.now();if(inp){inp.value=String(q.num.v);inp.dispatchEvent(new Event('input',{bubbles:true}));const bt=document.getElementById('chk');bt&&bt.click()}const c2=performance.now()-t;times.push([Math.round(a),Math.round(c2)])}
  return {times,lt:window.__lt}});
 console.log(nm,'x4 start/check ms',JSON.stringify(r.times),'longtasks',JSON.stringify(r.lt));await ctx.close()}await b.close()})()
