const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [w,h] of [[390,844],[1280,800]]){
const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();p.setDefaultTimeout(2500);
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(300);
await p.evaluate(()=>document.querySelector('[data-nav="lib:notes"]').click());await p.waitForTimeout(300);
try{await p.click('#main [data-back]');console.log(w,'back ok')}catch(e){console.log(w,'back FAIL',await p.evaluate(()=>{const e=document.querySelector('#main [data-back]');const r=e.getBoundingClientRect();const t=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);return JSON.stringify(r)+' covered by '+t.tagName+'.'+t.className})) }
await p.evaluate(()=>document.querySelector('[data-nav="lib:guide"]')&&0);
}await b.close()})()
