const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>go('learn'));await p.click('#dgs');await p.waitForTimeout(300);
let n=0;while(await p.$('#dkip')&&n<80){await p.click('#dkip');await p.waitForTimeout(30);n++}
await p.waitForTimeout(300);
if(await p.$('#sumc'))await p.click('#sumc');await p.waitForTimeout(300);
console.log('plan card on results',!!(await p.$('.plc [data-plan="go"]')),'cu',await p.evaluate(()=>S.cu&&Object.values(S.cu.base).join('')));
await p.screenshot({path:'shots/plan_res.png'});
await p.click('.plc [data-plan="view"]');await p.waitForTimeout(200);console.log('sheet rows',(await p.$$('.plr')).length);await p.screenshot({path:'shots/plan_sheet.png'});
await p.click('#plgo');await p.waitForTimeout(300);console.log('start -> kind',await p.evaluate(()=>Z&&Z.kind));
await p.evaluate(()=>closeSess());await p.waitForTimeout(200);
// simulate progress: first topic learned+practiced, second strong, third stuck
const r=await p.evaluate(()=>{const U=UN.map(u=>u.id);const t0=U[0],t1=U[1],t2=U[2];
 S.cu.base[t1]='s';const u0=UN[0];u0.lessons.forEach(l=>{S.un[t0]=S.un[t0]||{d:{}};S.un[t0].d[l.id]=1});
 const u2=UN[2];S.un[t2]=S.un[t2]||{d:{}};u2.lessons.forEach(l=>S.un[t2].d[l.id]=1);S.stat[t2]=[2,12];S.ema[t2]=.3;S.cu.base[t2]='f';
 S.stat[t0]=[7,9];S.ema[t0]=.7;
 return {t0,t1,t2}});
await p.evaluate(()=>{window.__ids={}});

await p.evaluate(()=>go('learn'));await p.waitForTimeout(200);await p.click('.plc [data-plan="go"]');await p.waitForTimeout(400);
const z=await p.evaluate(()=>({k:Z&&Z.kind,plan:!!(Z&&Z.plan),topics:Z&&Z.topics,first:Z&&Z.steps[0]&&Z.steps[0].it.q.t}));console.log('practice',z,'expect back-up of',r.t1,'and stuck',r.t2);
const picks=await p.evaluate(()=>{const c={};for(let i=0;i<30;i++){const id=nextAdaptive();if(id){const t=QS[QI[id]].t;c[t]=(c[t]||0)+1;Z.seenQ.push(id)}}return c});console.log('picks',picks);
await p.screenshot({path:'shots/plan_prac.png'});
// answer a few right, finish, check update card
await p.evaluate(()=>{Z.steps.forEach(s=>{if(s.k==='try'){s.it.done=true;s.it.ok=true}});S.stat[UN[0].id]=[17,19];S.ema[UN[0].id]=.9;finishSess()});await p.waitForTimeout(300);
if(await p.$('#sumc'))await p.click('#sumc');await p.waitForTimeout(300);
console.log('update card',(await p.textContent('.plc')).slice(0,200));await p.screenshot({path:'shots/plan_upd.png'});
console.log('errs',e);await b.close();process.exit(0)})()
