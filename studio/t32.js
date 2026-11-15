const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const e=[];const p=await (await b.newContext({viewport:{width:1000,height:900}})).newPage();p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{const d=document.createElement('div');d.id='sheet';d.style.cssText='position:fixed;inset:0;z-index:999;background:#222;overflow:auto;padding:10px;display:flex;flex-wrap:wrap;gap:8px';d.innerHTML=AV.slice(0,23).map(a=>'<div style="background:#f4f6fb;border-radius:10px;padding:6px;text-align:center;font:12px sans-serif;width:150px">'+mascot(a[0],'happy',190)+'<div>'+a[1]+'</div></div>').join('');document.body.appendChild(d)});
await p.waitForTimeout(400);await p.screenshot({path:process.env.OUT+'/q_chars.png'});await p.evaluate(()=>document.getElementById('sheet').remove());
await p.evaluate(()=>{S.coins=2000;S.mins[today()]=10;save();cur='me';sub.me='shop';route()});await p.waitForTimeout(300);
await p.screenshot({path:process.env.OUT+'/q_shop.png',fullPage:true});
await p.click('[data-ro="pk:elite"]');await p.waitForTimeout(300);await p.screenshot({path:process.env.OUT+'/q_pack.png'});
await p.click('[data-ro="go:elite"]');await p.waitForTimeout(700);await p.screenshot({path:process.env.OUT+'/q_open1.png'});await p.waitForTimeout(1200);await p.screenshot({path:process.env.OUT+'/q_reveal.png'});
console.log('text has %',await p.evaluate(()=>/\d%/.test(document.body.innerText)));
console.log('errors',JSON.stringify(e));await b.close()})()
