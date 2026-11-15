const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:1100,height:1050},deviceScaleFactor:2})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/skyvolt/app/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{const d=document.createElement('div');d.style.cssText='position:fixed;inset:0;z-index:999;background:#f4f6ff;display:flex;flex-wrap:wrap;gap:8px;padding:8px';
const ids=[2,4,13,19].map(i=>AV[i][0]);['idle','cheer','oops','think'].forEach(m=>ids.forEach(id=>{d.innerHTML+='<div style="width:240px;text-align:center;font:11px sans-serif">'+mascot(id,m,200)+m+'</div>'}));document.body.appendChild(d)});
await p.waitForTimeout(300);await p.screenshot({path:'shots/faces_big.png'});console.log(e);await b.close()})()
