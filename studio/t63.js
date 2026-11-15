const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();p.on('pageerror',x=>console.log('ERR',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const c={};QS.forEach(q=>{if(q.bld||q.type==='sim')c[q.type]=(c[q.type]||0)+1});return JSON.stringify({c,topics:ALL.length,units:UN.length,title:document.getElementById('ttl').textContent,ref:Object.keys(P.meta.refresh||{}).length,tabs:[...document.querySelectorAll('.tracks a')].map(a=>a.textContent)})}));
await p.click('#dgs');await p.waitForTimeout(500);console.log('diag steps',await p.evaluate(()=>Z.steps.length+' topics covered '+new Set(Z.steps.map(s=>s.it.q.t)).size));
await b.close();process.exit(0)})()
