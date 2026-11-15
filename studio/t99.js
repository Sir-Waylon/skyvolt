const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['circuit','meteorology']){
let n=0;
for(let i=0;i<12;i++){
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/_app_skyvolt/${app}/index.html`);await p.waitForTimeout(300);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.click('#nav button[data-t="library"]');await p.waitForTimeout(150);
await p.click('[data-nav="lib:stations"]');await p.waitForTimeout(250);
const bs=await p.$$('.list2 button, .stn-list button, [data-stn]');const ct=await p.evaluate(()=>[...document.querySelectorAll('button')].filter(b=>b.querySelector('small,.small')&&!b.dataset.nav&&!b.closest('#nav')).length);
const cand=await p.$$('button:has(small), button:has(.small)');const use=cand.filter(Boolean);
if(i>=use.length){await p.close();break}
await use[i].click();await p.waitForTimeout(300);
const r=await p.evaluate(()=>({segs:document.querySelectorAll('.segs').length,sel:document.querySelectorAll('select').length,hid:document.querySelectorAll('select[hidden]').length,h:document.querySelector('h2,h3')?.textContent}));
console.log(app,i,JSON.stringify(r),E.slice(0,1));
if(r.segs){await p.screenshot({path:`shots/t99_${app}_${i}.png`});}
await p.close()}}
await b.close()})()
