const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const ctx=await b.newContext({viewport:{width:390,height:800}});const p=await ctx.newPage();const c=await ctx.newCDPSession(p);
await c.send('Emulation.setCPUThrottlingRate',{rate:4});await c.send('Profiler.enable');await c.send('Profiler.setSamplingInterval',{interval:200});await c.send('Profiler.start');
await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
await p.goto('file://'+process.cwd()+`/out/${process.argv[2]||'_app_axiom/apex'}/index.html`);await p.waitForFunction(()=>typeof route==='function'&&document.querySelector('#nav button'));await p.waitForTimeout(500);
const {profile}=await c.send('Profiler.stop');const self={};const dt=profile.timeDeltas;const idIdx={};profile.nodes.forEach(n=>idIdx[n.id]=n);
profile.samples.forEach((id,i)=>{const n=idIdx[id];const k=(n.callFrame.functionName||'(anon)')+' '+(n.callFrame.url.split('/').pop()||'')+':'+n.callFrame.lineNumber;self[k]=(self[k]||0)+(dt[i]||0)});
const tot=Object.values(self).reduce((a,b)=>a+b,0);console.log('total ms (4x)',Math.round(tot/1000));
Object.entries(self).sort((a,b)=>b[1]-a[1]).slice(0,14).forEach(([k,v])=>console.log(Math.round(v/1000)+'ms',k));await b.close()})()
