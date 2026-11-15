const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{const ids=QS.filter(q=>q.type==='mcq'&&q.l>=2).slice(0,6).map(q=>({k:'try',it:mkItem(q.id)}));startSess({kind:'practice',title:'t',steps:ids})});await p.waitForTimeout(300);
console.log('conf row',!!(await p.$('.conf')),'rw',!!(await p.$('.rwtag')));
for(let i=0;i<3;i++){await p.click('[data-cf="3"]');await p.evaluate(()=>{const it=Z.steps[Z.i].it;it.jd.forEach((_,k)=>it.jd[k]=(k===0))});await p.evaluate(()=>drawSess());await p.waitForTimeout(100);
 await p.evaluate(()=>{document.getElementById('chk').click()});await p.waitForTimeout(250);if(i===1)await p.screenshot({path:'shots/meta.png'});
 console.log(i,'cfb',!!(await p.$('.cfb')),'xpl',!!(await p.$('.xpl')));
 await p.evaluate(()=>{const n=document.getElementById('go')||document.getElementById('nx');if(n)n.click()});await p.waitForTimeout(250)}
console.log(await p.evaluate(()=>JSON.stringify(S.cal)),e);await b.close()})()
