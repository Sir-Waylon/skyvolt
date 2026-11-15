const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:380,height:1500},deviceScaleFactor:1.5})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/apex/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{const root=document.createElement('div');root.style.cssText='position:fixed;inset:0;z-index:999;background:var(--bg);overflow:hidden;padding:8px';document.body.appendChild(root);
 const want=[['fn','Transformations'],['tc','The unit circle'],['tc','Sine, cosine and tangent']];
 want.forEach(([t,h])=>{P.units.forEach(u=>u.lessons.forEach(L=>L.cards.forEach(c=>{if(u.id===t&&c.h===h){const d=document.createElement('div');d.className='lab';root.appendChild(d);labInit(d,c.lab);const pb=d.querySelector('.wpre button');if(pb)pb.click()}})))})});
await p.waitForTimeout(300);await p.screenshot({path:'shots/wid_look.png'});console.log(e);await b.close()})()
