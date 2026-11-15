const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const O=process.env.SC||process.cwd();const apps=[['voltaic','/out/skyvolt/app/circuit/index.html'],['stratus','/out/skyvolt/app/meteorology/index.html'],['axiom','/out/axiom/app/index.html']];
const e=[];
for(const [n,u] of apps){
 const p=await (await b.newContext({viewport:{width:1100,height:900}})).newPage();p.on('pageerror',x=>e.push(n+': '+x.message));p.on('console',m=>{if(m.type()==='error')e.push(n+' console: '+m.text())});
 await p.goto('file://'+process.cwd()+u);await p.waitForTimeout(500);
 await p.evaluate(()=>{const d=document.createElement('div');d.id='sheet';d.style.cssText='position:fixed;inset:0;z-index:999;background:#222;overflow:auto;padding:10px;display:flex;flex-wrap:wrap;gap:8px';d.innerHTML=AV.map(a=>'<div style="background:#f4f6fb;border-radius:10px;padding:6px;text-align:center;font:12px sans-serif;width:112px">'+mascot(a[0],'happy',140)+'<div>'+a[1]+'</div></div>').join('')+AV.slice(0,6).map(a=>'<div style="background:#f4f6fb;border-radius:10px;padding:6px">'+mascot(a[0],'cheer',48)+mascot(a[0],'oops',48)+mascot(a[0],'think',48)+'</div>').join('');document.body.appendChild(d)});
 await p.waitForTimeout(300);await p.screenshot({path:`${process.env.OUT}/chars_${n}.png`});
 await p.evaluate(()=>document.getElementById('sheet').remove());
 await p.evaluate(()=>{S.coins=900;S.mins[today()]=12;save();cur='me';sub.me='shop';route()});await p.waitForTimeout(300);
 await p.screenshot({path:`${process.env.OUT}/shop_${n}.png`,fullPage:true});
 if(n==='voltaic'){
  await p.evaluate(()=>{const o=Math.random;});
  await p.click('[data-ro="open"]');await p.waitForTimeout(1600);await p.screenshot({path:`${process.env.OUT}/reveal_${n}.png`});
  const r=await p.evaluate(()=>({odds:oddsNow().reduce((a,b)=>a+b,0),pity:S.cos.pity,coins:S.coins}));console.log(JSON.stringify(r));
  // simulate 200000 rolls distribution at zero and full luck
  const sim=await p.evaluate(()=>{const res={};[0,30].forEach(m=>{S.mins[today()]=m;const c=[0,0,0,0,0,0];const sv=S.cos.pity;for(let i=0;i<200000;i++){S.cos.pity={e:0,l:0,n:0};S.cos.own={};const x=rollBox();c[x.r]++}res[m]=c.map(v=>+(v/2000).toFixed(2))});return res});console.log(JSON.stringify(sim));
 }
 await p.close()}
console.log('errors',JSON.stringify(e));await b.close()})()
