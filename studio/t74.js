const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);p.on('pageerror',x=>console.log('PE',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
for(const k of ['blitz','mock']){
 await p.click('[data-og="solo"]');await p.click('[data-solo="'+k+'"]');await p.waitForTimeout(500);
 console.log(k,'sx?',await p.evaluate(()=>!!document.getElementById('sx')));
 await p.click('#sx');await p.waitForTimeout(400);
 console.log(' after close: og',await p.evaluate(()=>{const e=document.querySelector('[data-og="solo"]');if(!e)return 'none';const r=e.getBoundingClientRect();const t=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);return r.y+' top='+(t&&t.className+'/'+t.id+'/'+t.tagName)}))}
await b.close()})()
