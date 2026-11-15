const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [n,f] of [['circ','skyvolt/app/circuit/index.html'],['met','skyvolt/app/meteorology/index.html']]){
const p=await b.newPage({viewport:{width:420,height:1000}});const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+f);await p.waitForTimeout(500);
await p.evaluate(()=>{sub.lib='stations';go('library')});await p.waitForTimeout(300);
await p.screenshot({path:'ck/stn_hub_'+n+'.png'});
const ids=await p.evaluate(()=>STN.list.map(o=>o.id));console.log(n,ids);
for(const id of ids){await p.evaluate(i=>stnOpen(i),id);await p.waitForTimeout(250);
 await p.evaluate(()=>{const s=document.querySelector('.stn-sim');if(s)s.scrollIntoView()});
 await p.screenshot({path:'ck/stn_'+id+'.png'});
 const r=await p.evaluate(()=>{try{stnCheck();return [STN.res.score,STN.res.lines.length,STN.res.steps.length]}catch(x){return 'ERR '+x.message}});
 console.log(id,JSON.stringify(r));await p.waitForTimeout(100)}
console.log(n,'pageerrors',e);await p.close()}
await b.close()})()
