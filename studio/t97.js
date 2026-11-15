const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [slug,app] of [['circuit','_app_skyvolt'],['meteorology','_app_skyvolt'],['apex','_app_axiom']]){
const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${app}/${slug}/index.html`);await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.click('#nav button[data-t="library"]');await p.waitForTimeout(300);
const r=await p.$('[data-nav="act:print"]');if(!r){console.log(slug,'no row');continue}
await r.scrollIntoViewIfNeeded();await r.click();await p.waitForTimeout(300);
console.log(slug,'overlay',!!await p.$('#prt'),'formula chips',await p.evaluate(()=>document.querySelectorAll('#prt .fl>div').length));
await p.setViewportSize({width:900,height:900});
for(const s of['n','c','p']){await p.click(`[data-s="${s}"]`)}
await p.waitForTimeout(200);
await p.pdf({path:`shots/print_${slug}.pdf`,format:'Letter',printBackground:true});
await p.screenshot({path:`shots/print_${slug}.png`});console.log(E.slice(0,2));await p.close()}
await b.close()})()
