const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/index.html');await p.waitForTimeout(500);
const ids=await p.evaluate(()=>{const o={};QS.forEach(q=>{if(!o[q.type]&&['slider','angle','point','chips','proof'].includes(q.type))o[q.type]=q.id});return o});console.log(ids);
for(const [t,id] of Object.entries(ids)){
 await p.evaluate(i=>{startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(i)}]})},id);await p.waitForTimeout(300);
 await p.screenshot({path:'ck/it_'+t+'.png'});
 await p.evaluate(()=>{document.body.classList.remove('insess');Z=null;route&&route()});}
console.log(e);await b.close()})()
