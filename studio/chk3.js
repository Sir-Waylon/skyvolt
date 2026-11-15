const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:800}});
const errs=[];p.on('pageerror',e=>errs.push('PAGE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CON '+m.text())});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(500);
// grader self-test
const r=await p.evaluate(()=>{const bad=[];
 QS.filter(q=>q.type==='short').forEach(q=>{
  const ans=shortAnswer(q);
  if(!gradeShort(q,ans).ok)bad.push(['self',q.id,ans,JSON.stringify(gradeShort(q,ans))]);
  if(q.num){const v=q.num.v,u=q.num.u;
    // SI-with-base unit variant
    const base={mA:'A',mW:'W',mC:'C',mJ:'J',ms:'s','µF':'F','kΩ':'Ω',kWh:'Wh',Wh:'Wh','N/C':'N/C',V:'V',A:'A','Ω':'Ω',W:'W',C:'C',N:'N',h:'h',s:'s','%':'%'}[u];
    if(u&&base&&['mA','mW','mC','mJ','ms','µF','kΩ'].includes(u)){const f=unitInfo(u).f;const s=(v)+' '+base;if(!gradeShort(q,s).ok)bad.push(['siunit',q.id,s]);}
    if(gradeShort(q,String(Number(fmt(v/(u?unitInfo(u).f:1)))*1.2+(u?' '+u:'')).replace('×10^','e')).ok)bad.push(['tolfail',q.id]);
  }});
 return {bad,tests:[gradeShort({num:{v:0.02,u:'mA'}},'20 mA').ok,gradeShort({num:{v:0.02,u:'mA'}},'0.02 A').ok,gradeShort({num:{v:0.02,u:'mA'}},'20').ok,gradeShort({num:{v:0.02,u:'mA'}},'20 V').ok,gradeShort({num:{v:1.08e6,u:'kWh'}},'0.3').ok,gradeShort({num:{v:2e13}},'2.0 x 10^13').ok,gradeShort({text:['gfci','ground fault circuit interrupter']},'The GFCI').ok,gradeShort({text:['neutral']},'netural').ok]}});
console.log(JSON.stringify(r));
// UI flow
await p.click('#tabs button[data-v=home]');
await p.click('[data-go=learn]');await p.waitForTimeout(200);
const types=new Set();
for(let k=0;k<10;k++){
 const t=await p.evaluate(()=>Z.items[Z.i].q.type);types.add(t);
 if(t==='mcq'){await p.click('.opt');}
 else if(t==='short'){await p.fill('#sv','abc');await p.click('#chk');}
 else if(t==='multi'){await p.click('.opt');await p.click('#chk');}
 else if(t==='order'){const n=await p.evaluate(()=>Z.items[Z.i].q.items.length);for(let i=0;i<n;i++)await p.click('[data-po]');await p.click('#chk');}
 else if(t==='match'){const n=await p.evaluate(()=>Z.items[Z.i].q.pairs.length);for(let i=0;i<n;i++){await p.click('[data-ml]:not([data-p])');await p.click('[data-mr]:not([data-p])');}await p.click('#chk');}
 await p.click('#nx');await p.waitForTimeout(50);
}
console.log('types',[...types],'results visible',await p.isVisible('#again'));
await p.screenshot({path:'ck/res.png'});
// force each type visually
for(const ty of ['mcq','short','order','match']){
 await p.evaluate((ty)=>{const ids=QS.filter(q=>q.type===ty).slice(0,3).map(q=>q.id);start({mode:'learn',ids:ids})},ty);
 await p.waitForTimeout(150);await p.screenshot({path:'ck/q_'+ty+'.png'});
}
// blitz
await p.evaluate(()=>go('blitz'));await p.waitForTimeout(200);await p.screenshot({path:'ck/blitz.png'});
// each tab screenshot + overflow
for(const v of ['home','plan','notes','cards','bench','stats']){
 await p.evaluate((v)=>{Z=null;show(v)},v);await p.waitForTimeout(100);
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
 console.log(v,'overflow',ov);await p.screenshot({path:'ck/t_'+v+'.png'});
}
// match game
await p.evaluate(()=>{show('cards');startMatch()});await p.waitForTimeout(100);await p.screenshot({path:'ck/match.png'});
// dark mode
await p.emulateMedia({colorScheme:'dark'});await p.evaluate(()=>{mg=null;show('home')});await p.screenshot({path:'ck/dark.png'});
console.log('errors',errs);
await b.close()})();
