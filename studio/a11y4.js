const {chromium}=require('playwright');const {CHECK}=require('./a11y.js');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});let bad=0;
for(const f of ['circuit','meteorology']){for(const cs of ['light','dark']){const c=await b.newContext({viewport:{width:390,height:844},colorScheme:cs});const p=await c.newPage();await p.goto('file://'+process.cwd()+'/out/skyvolt/app/'+f+'/index.html');await p.waitForTimeout(400);
 await p.evaluate(()=>{sub.lib='stations';go('library')});await p.waitForTimeout(200);
 const ids=await p.evaluate(()=>STN.list.map(o=>o.id));
 for(const id of ids){await p.evaluate(i=>stnOpen(i),id);await p.waitForTimeout(150);let r=await p.evaluate(CHECK);r=r.filter(x=>x[0]!=='live');
  await p.evaluate(()=>stnCheck());await p.waitForTimeout(100);let r2=await p.evaluate(CHECK);r2=r2.filter(x=>x[0]!=='live');r=r.concat(r2);
  if(r.length){bad+=r.length;console.log(f,cs,id,JSON.stringify(r.slice(0,3)))}}
 await c.close()}}
console.log('TOTAL',bad);await b.close()})();
