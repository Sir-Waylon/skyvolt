const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const site of ['_app_skyvolt/circuit','_app_axiom/apex']){const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.xp=95;S.coins=10;save();hud();route()});
const lv0=await p.textContent('#lvn'),r0=await p.evaluate(()=>getComputedStyle(document.getElementById('lvr')).getPropertyValue('--p'));
await p.evaluate(()=>{const q=QS.find(x=>x.type==='mcq'&&x.l===1);startSess({kind:'practice',title:'P',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(400);
await p.click('#sess [data-oi="0"]');await p.waitForTimeout(900);
const modal=await p.evaluate(()=>document.querySelector('.modal h2')?document.querySelector('.modal h2').textContent:'none');
console.log(site,'| header level',lv0,'->',await p.textContent('#lvn'),'| xp',await p.evaluate(()=>S.xp),'| ring',r0,'->',await p.evaluate(()=>getComputedStyle(document.getElementById('lvr')).getPropertyValue('--p')),'| modal:',modal,errs.slice(0,2));await p.close()}await b.close()})()
