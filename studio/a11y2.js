const {chromium}=require('playwright');const {CHECK}=require('./a11y.js');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const url=process.argv[2];let bad=0;
for(const cs of ['light','dark']){const c=await b.newContext({viewport:{width:390,height:844},colorScheme:cs});const p=await c.newPage();const er=[];p.on('pageerror',e=>er.push(e.message));await p.goto(url);await p.waitForTimeout(500);
 const ids=await p.evaluate(()=>{const o={};QS.forEach(q=>{const k=q.type+(q.num?'n':'');if(!o[k])o[k]=q.id});return o});
 for(const [k,id] of Object.entries(ids)){await p.evaluate(i=>{startSess({kind:'practice',title:'Practice',steps:[{k:'try',it:mkItem(i)}]})},id);await p.waitForTimeout(150);
  let r=await p.evaluate(CHECK);r=r.filter(x=>!['h1','live'].includes(x[0]));if(r.length){bad+=r.length;console.log(cs,k,id,JSON.stringify(r.slice(0,3)))}
  // reveal state
  await p.evaluate(()=>{const it=Z.steps[Z.i].it;it.done=true;it.ok=false;drawSess()});await p.waitForTimeout(100);
  r=await p.evaluate(CHECK);r=r.filter(x=>!['h1','live'].includes(x[0]));if(r.length){bad+=r.length;console.log(cs,k,'rev',JSON.stringify(r.slice(0,3)))}
  await p.evaluate(()=>{const it=Z.steps[Z.i].it;it.done=true;it.ok=true;drawSess()});await p.waitForTimeout(100);
  r=await p.evaluate(CHECK);r=r.filter(x=>!['h1','live'].includes(x[0]));if(r.length){bad+=r.length;console.log(cs,k,'ok',JSON.stringify(r.slice(0,3)))}
  await p.evaluate(()=>{closeSess&&closeSess()});}
 // lesson card + explain + results
 await p.evaluate(()=>{const u=UN[0];const L=u.lessons[0];startSess({kind:'lesson',title:u.title,unit:u,steps:lessonSteps?lessonSteps(u,L):[]})});await p.waitForTimeout(200);
 let r=await p.evaluate(CHECK);r=r.filter(x=>!['h1','live'].includes(x[0]));console.log(cs,'lesson',JSON.stringify(r.slice(0,3)));bad+=r.length;
 console.log(cs,'pageerrors',er.slice(0,3));await c.close()}
console.log('TOTAL',bad);await b.close()})();
