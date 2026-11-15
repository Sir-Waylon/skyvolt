const {chromium}=require('playwright');const {CHECK}=require('./a11y.js');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});let bad=0;
for(const url of process.argv.slice(2)){for(const cs of ['light','dark']){const c=await b.newContext({viewport:{width:390,height:844},colorScheme:cs});const p=await c.newPage();const er=[];p.on('pageerror',e=>er.push(e.message));await p.goto(url);await p.waitForTimeout(500);
 for(const v of ['learn','practice','library','me']){await p.evaluate(v=>go(v),v);await p.waitForTimeout(120);
  const n=await p.evaluate(()=>document.querySelectorAll('#main .seg button').length);
  for(let i=-1;i<n;i++){if(i>=0){await p.evaluate(i=>document.querySelectorAll('#main .seg button')[i].click(),i);await p.waitForTimeout(150)}
   let r=await p.evaluate(CHECK);r=r.filter(x=>x[0]!=='live');if(r.length){bad+=r.length;console.log(url.split('/').slice(-3,-1).join('/'),cs,v,i,JSON.stringify(r.slice(0,3)))}}}
 if(er.length)console.log('ERR',er.slice(0,3));await c.close()}}
console.log('TOTAL',bad);await b.close()})();
