const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,labs] of [['_app_skyvolt/circuit',['ohm','rc','net','mag','bulb']],['_app_skyvolt/meteorology',['wind','front','hum','stn','parcel']],['_app_axiom/apex',[]],['_app_axiom/quanta',['ohm','rc','proj']]]){
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const go=async()=>{await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(200)};
await go();console.log(app,'labs:',await p.$$eval('[data-lab]',a=>a.map(x=>x.dataset.lab).join(',')),'| presets:',await p.$$eval('[data-gpre]',a=>a.map(x=>x.dataset.gpre).join(',')));
for(const l of labs){await go();await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),l);await p.waitForTimeout(500);
 const n=await p.evaluate(()=>{const r=document.getElementById('labroot');return r.querySelectorAll('svg *').length+'/'+(r.querySelector('.labr')||{innerText:''}).innerText.slice(0,70)});
 for(const sel of await p.$$('[data-ls]')){await sel.evaluate(e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))});}
 for(const c of (await p.$$('#labroot [data-lc]')).slice(0,6)){await c.evaluate(e=>e.click())}
 await p.waitForTimeout(300);
 const n2=await p.evaluate(()=>(document.querySelector('#labroot .labr')||{innerText:''}).innerText.slice(0,90));
 console.log('  ',l,n,'=>',n2);await p.screenshot({path:'shots/t85_'+l+'.png'})}
for(const g of await p.$$eval('[data-gpre]',a=>a.map(x=>x.dataset.gpre))){await go();await p.evaluate(g=>document.querySelector('[data-gpre="'+g+'"]').click(),g);await p.waitForTimeout(500);
 const o=await p.evaluate(()=>({rows:document.querySelectorAll('.ginp').length,err:document.querySelectorAll('.gerr').length,ink:(()=>{const c=document.getElementById('gcv'),x=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let i=0;i<x.length;i+=16)if(x[i]!==x[0]||x[i+1]!==x[1])n++;return n})(),info:(document.querySelector('.ginfo')||{innerText:''}).innerText.slice(0,50)}));console.log('   preset',g,JSON.stringify(o));if(g==='triangle')await p.screenshot({path:'shots/t85_tri.png'})}
console.log(E);await p.close()}
await b.close()})()
