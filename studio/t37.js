const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const u of ['out/axiom/app/apex/index.html','out/skyvolt/app/circuit/index.html','out/axiom/app/geometry/index.html']){
const p=await (await b.newContext({viewport:{width:420,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/'+u);await p.waitForTimeout(500);
await p.evaluate(()=>{cur='learn';route()});await p.waitForTimeout(200);
const has=await p.$('#dgs');if(has)await has.click();await p.waitForTimeout(300);
const r=await p.evaluate(()=>{if(!Z)return null;const t={};Z.steps.forEach(s=>{t[s.it.q.type]=(t[s.it.q.type]||0)+1});return {n:Z.steps.length,t}});
console.log(u,has?'clicked':'nobtn',JSON.stringify(r),e);}
await b.close()})()
