const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const only=process.argv[2];
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']]){ if(only&&only!==nm)continue;
 const p=await (await b.newContext({viewport:{width:430,height:900}})).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(500);
 await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(200);
 await p.evaluate(()=>{const u=UN[1]||UN[0];startLesson(u.id,u.lessons[0].id)});await p.waitForTimeout(500);
 for(let i=0;i<3;i++){await p.screenshot({path:`shots/ls-${nm}-${i}.png`});await p.evaluate(()=>{const b=[...document.querySelectorAll('button')].find(x=>/^(Next|Continue|Got it|Check)/i.test(x.textContent.trim()));b&&b.click()});await p.waitForTimeout(400)}
 await p.reload();await p.waitForTimeout(500);await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(200);
 await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(250);
 await p.evaluate(()=>{const e=document.querySelector('[data-nav="lib:labs"]');e&&e.click()});await p.waitForTimeout(300);
 await p.screenshot({path:`shots/lbl-${nm}.png`});
 await p.evaluate(()=>{const e=document.querySelector('[data-lab]');e&&e.click()});await p.waitForTimeout(700);
 await p.screenshot({path:`shots/lb-${nm}.png`,fullPage:true});console.log(nm,'ok');await p.close()}
await b.close()})()
