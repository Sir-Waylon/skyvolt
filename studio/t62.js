const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:640}})).newPage();
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
console.log(await p.evaluate(()=>{const o=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.right>innerWidth+1&&r.width>0)o.push(e.tagName+'.'+e.className+' '+Math.round(r.right)+' '+(e.textContent||'').slice(0,30))});return o.slice(0,8)}));await b.close();process.exit(0)})()
