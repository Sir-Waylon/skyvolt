const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){
const ctx=await b.newContext({viewport:{width:390,height:844}});ctx.setDefaultTimeout(3000);const p=await (await Promise.resolve(ctx)).newPage();const _x=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',x=>errs.push(x.message));p.on('console',m=>{if(m.type()==='error')errs.push('C:'+m.text())});
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
const step=async(n,f)=>{try{await f()}catch(e){errs.push(n+': '+e.message.split('\n')[0])}};
await step('skipgate',()=>p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()}));
for(const t of ['today','practice','library','me','course']){
 await step('tab '+t,async()=>{const bt=await p.$('#nav button[data-t="'+t+'"]');if(!bt){errs.push('no tab '+t);return}await bt.click();await p.waitForTimeout(250);
  const n=await p.evaluate(()=>document.querySelectorAll('#app [data-nav]').length);
  for(let i=0;i<Math.min(n,6);i++){await p.evaluate(i=>document.querySelectorAll('#app [data-nav]')[i]&&document.querySelectorAll('#app [data-nav]')[i].click(),i);await p.waitForTimeout(150);
   const bk=await p.$('#app [data-back]');if(bk){await bk.click();await p.waitForTimeout(100)}}
 })}
// today play panel
await step('play',async()=>{await p.click('#nav button[data-t="today"]');await p.waitForTimeout(200);const tiles=await p.evaluate(()=>[...document.querySelectorAll('[data-og]')].map(e=>e.dataset.og));console.log(app,'og tiles',tiles.join(','));
 for(const el of await p.$$('[data-og]')){await el.click().catch(()=>{});await p.waitForTimeout(250);await p.keyboard.press('Escape');}});
// flashcards & labs
await step('flash',async()=>{const r=await p.evaluate(()=>typeof window.flashView+'/'+typeof window.labsView);console.log(app,r)});
console.log(app,errs.length?errs.slice(0,8):'OK');await p.screenshot({path:'shots/t70_'+app.split('/')[1]+'.png'});await p.close()}
await b.close();process.exit(0)})()
