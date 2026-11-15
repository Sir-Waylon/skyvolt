const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const apps=process.argv[2]?[process.argv[2]]:['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta'];
for(const app of apps){
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);const errs=[];
p.on('pageerror',x=>errs.push('PE '+x.message));p.on('console',m=>{if(m.type()==='error'&&!/api\/config|ERR_FAILED/.test(m.text()))errs.push('C:'+m.text())});
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const L=[];const tab=async t=>{await p.evaluate(t=>{document.querySelectorAll('.modal').forEach(m=>m.remove());var x=document.getElementById('sx');if(x){x.click();var ok=document.querySelector('[data-ok="1"]');ok&&ok.click()}document.querySelectorAll('.modal').forEach(m=>m.remove());document.querySelector('#nav button[data-t="'+t+'"]').click()},t);await p.waitForTimeout(250)};
const txt=()=>p.evaluate(()=>document.getElementById('main').innerText.length);
const step=async(n,f)=>{try{const r=await f();L.push(n+':'+(r===undefined?'ok':r))}catch(e){L.push(n+' FAIL '+e.message.split('\n')[0])}};
await step('today',async()=>{await tab('learn');return (await p.$$('[data-og]')).length+' og'});
await step('og-host',async()=>{await p.click('[data-og="host"]');await p.waitForTimeout(300);const t=await p.evaluate(()=>document.body.innerText.slice(0,0)+document.querySelectorAll('.modal,.sheet,[role=dialog]').length);await p.keyboard.press('Escape');return t});
await step('og-solo',async()=>{await tab('learn');await p.click('[data-og="solo"]');await p.waitForTimeout(300);const n=(await p.$$('[data-solo]')).length;await p.keyboard.press('Escape');return n+' solo opts'});
for(const m of ['flash','match','blitz','mock']) await step('solo-'+m,async()=>{await tab('learn');await p.click('[data-og="solo"]');await p.waitForTimeout(200);await p.click('[data-solo="'+m+'"]');await p.waitForTimeout(500);return (await txt())+'ch'});
for(const t of ['practice','library','me','course']) await step(t,async()=>{await tab(t);const n=await p.evaluate(()=>document.querySelectorAll('#main [data-nav]').length);let ok=0;
 for(let i=0;i<Math.min(n,8);i++){await tab(t);await p.evaluate(i=>document.querySelectorAll('#main [data-nav]')[i].click(),i);await p.waitForTimeout(200);if(await txt()>20)ok++;
  const bk=await p.$('#main [data-back]');if(bk)await bk.click()}return ok+'/'+Math.min(n,8)+' nav'});
await step('search',async()=>{await tab('library');const s=await p.$('#main input[type=search],#main input[data-sq]');if(!s)return 'no input';await s.fill('a');await p.waitForTimeout(200);return 'ok'});
await step('flashview',async()=>{await tab('library');await p.evaluate(()=>{const e=document.querySelector('[data-nav^="flash:"]');e&&e.click()});await p.waitForTimeout(300);
 for(const m of ['learn','write','match']){const e=await p.$('[data-fl="mode:'+m+'"]');if(e){await e.click();await p.waitForTimeout(300);const bk=await p.$('[data-fl="menu"]');if(bk)await bk.click()}}return await txt()});
await step('labs',async()=>{await tab('library');await p.evaluate(()=>{const e=document.querySelector('[data-nav^="lab"],[data-nav="lib:labs"]');e&&e.click()});await p.waitForTimeout(300);const labs=await p.$$eval('[data-lab]',a=>a.map(x=>x.dataset.lab));
 for(const l of labs){if(!l)continue;await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),l);await p.waitForTimeout(300);
  for(const a of ['run','fire','reset']){const e=await p.$('[data-la="'+a+'"]');if(e){await e.click().catch(()=>{});await p.waitForTimeout(150)}}
  await p.evaluate(()=>{const e=document.querySelector('[data-lab=""]');e&&e.click()});await p.waitForTimeout(100)}return labs.join(',')});
await step('dropdown',async()=>p.evaluate(()=>!!document.querySelector('#acct,.acct,[data-acct]')));
console.log(app+'\n  '+L.join('\n  ')+'\n  ERRS:',errs.slice(0,6));await p.close()}
await b.close();process.exit(0)})()
