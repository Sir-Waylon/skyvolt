const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);p.on('pageerror',x=>console.log('PE',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
for(const t of ['library','me']){
await p.evaluate(t=>document.querySelector('#nav button[data-t="'+t+'"]').click(),t);await p.waitForTimeout(300);
console.log(t,await p.evaluate(()=>[...document.querySelectorAll('#main [data-nav]')].map(e=>e.dataset.nav).join(' ')));
const n=await p.evaluate(()=>document.querySelectorAll('#main [data-nav]').length);
for(let i=0;i<n;i++){await p.evaluate(()=>document.querySelector('#nav button[data-t="'+document.querySelector('#nav .on,#nav [aria-current]')?.dataset.t+'"]'));
 const nav=await p.evaluate(i=>{const e=document.querySelectorAll('#main [data-nav]')[i];if(!e)return null;const k=e.dataset.nav;e.click();return k},i);
 await p.waitForTimeout(250);
 const info=await p.evaluate(()=>({len:document.getElementById('main').innerText.length,back:!!document.querySelector('#main [data-back]'),h:document.querySelector('#main h2,#main h3')?.innerText}));
 console.log('  ',nav,JSON.stringify(info));
 await p.evaluate(()=>{const e=document.querySelector('#main [data-back]');e&&e.click()});await p.waitForTimeout(150);
}}
await b.close()})()
