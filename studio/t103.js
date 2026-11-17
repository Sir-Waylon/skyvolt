const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [w,h] of [[360,700],[1000,760]]){
const p=await (await b.newContext({viewport:{width:w,height:h},hasTouch:false})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/meteorology/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{startFromIds(['obs-001'],'t')});await p.waitForTimeout(500);
for(let i=0;i<4&&!(await p.$('.slots'));i++){await p.evaluate(()=>{var e=document.getElementById('go');e&&e.click()});await p.waitForTimeout(200)}
console.log(w,'slots',await p.evaluate(()=>document.querySelectorAll('.slot').length),'bank',await p.evaluate(()=>document.querySelectorAll('.oi').length));
await p.screenshot({path:`shots/t103_${w}_a.png`});
// tap first bank item
await p.click('.oi >> nth=0');await p.waitForTimeout(100);
// drag second bank item's grip into slot 3
const g=await p.$('.oi [data-dragpo] >> nth=0');const gb=await g.boundingBox();const sl=await p.$('.slot >> nth=2');const sb=await sl.boundingBox();
await p.mouse.move(gb.x+8,gb.y+8);await p.mouse.down();await p.mouse.move(gb.x+30,gb.y-30,{steps:4});await p.mouse.move(sb.x+80,sb.y+20,{steps:6});await p.mouse.up();await p.waitForTimeout(150);
console.log('seq',await p.evaluate(()=>JSON.stringify(Z.steps[Z.i].it.seq)));
// up/down
await p.click('[data-dn="0"]');await p.waitForTimeout(100);console.log('after dn',await p.evaluate(()=>JSON.stringify(Z.steps[Z.i].it.seq)));
await p.screenshot({path:`shots/t103_${w}_b.png`});
// arrangement avoidance
const arr=await p.evaluate(()=>{var o=[];for(var i=0;i<30;i++){var it=mkItem(QS.filter(q=>q.type==='mcq'||q.type==='multi')[3].id);o.push(it.perm.join(''))}var c=0;for(i=1;i<o.length;i++)if(o[i]===o[i-1])c++;return c});console.log('repeat arrangements',arr,E.slice(0,2));
await p.close()}
await b.close()})()
