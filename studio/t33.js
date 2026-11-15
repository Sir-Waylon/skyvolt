const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:1100,height:520},deviceScaleFactor:2})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/skyvolt/app/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{const d=document.createElement('div');d.style.cssText='position:fixed;inset:0;z-index:999;background:#f4f6ff;display:flex;flex-wrap:wrap;gap:8px;padding:8px';
const ids=[1,2,4,8,13,15,19,22].map(i=>AV[i][0]);['idle','cheer','oops','think'].forEach(m=>ids.forEach(id=>{d.innerHTML+='<div style="width:125px;text-align:center;font:11px sans-serif">'+mascot(id,m,72)+m+'</div>'}));document.body.appendChild(d)});
await p.waitForTimeout(300);await p.screenshot({path:'shots/faces.png'});console.log(e);await b.close()})()
