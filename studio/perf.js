// node perf.js [cpuSlowdown]  -> load timings per trainer under CPU throttle (file://)
const {chromium}=require('playwright');const slow=+process.argv[2]||4;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']]){
 const runs=[];for(let i=0;i<3;i++){const ctx=await b.newContext({viewport:{width:390,height:800}});const p=await ctx.newPage();const c=await ctx.newCDPSession(p);await c.send('Emulation.setCPUThrottlingRate',{rate:slow});
  await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
  await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`,{waitUntil:'load'});
  await p.waitForFunction(()=>typeof route==='function'&&document.querySelector('#nav button'));
  const m=await p.evaluate(()=>{const n=performance.getEntriesByType('navigation')[0];const fcp=(performance.getEntriesByType('paint').find(e=>e.name==='first-contentful-paint')||{}).startTime;const sc=performance.getEntriesByType('resource').filter(r=>/\.js/.test(r.name)).map(r=>Math.round(r.duration));return {dcl:Math.round(n.domContentLoadedEventEnd),load:Math.round(n.loadEventEnd),fcp:Math.round(fcp||0),ready:Math.round(performance.now()),heap:Math.round((performance.memory||{}).usedJSHeapSize/1048576)}});runs.push(m);await ctx.close()}
 runs.sort((a,b)=>a.ready-b.ready);console.log(nm,'x'+slow,JSON.stringify(runs[1]))}
await b.close()})()
