const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(300);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.click('#nav button[data-t="library"]');await p.click('[data-nav="lib:stations"]');await p.waitForTimeout(250);
await (await p.$$('button:has(small), button:has(.small)'))[4].click();await p.waitForTimeout(300);
const before=await p.evaluate(()=>[...document.querySelectorAll('select')].map(s=>s.value).join());
await p.click('.segs >> nth=0 >> button >> nth=2');await p.waitForTimeout(300);
const after=await p.evaluate(()=>[...document.querySelectorAll('select')].map(s=>s.value).join()+' | on='+[...document.querySelectorAll('.segs')][0].querySelector('.on')?.textContent);
console.log(before,'->',after,E);await b.close()})()
