const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(200);
await p.evaluate(()=>document.querySelector('[data-lab="bread"]').click());await p.waitForTimeout(400);
await p.evaluate(()=>document.querySelector('[data-la="ex"]').click());await p.waitForTimeout(200);
console.log('example:',await p.evaluate(()=>document.querySelector('#lro').innerText));await p.locator('#lsvw').screenshot({path:'shots/t91_a.png'});
// tap holes to place a bare LED between rail + and rail -: tool LED
async function tap(x,y){const bb=await p.locator('#lsv').boundingBox();await p.mouse.click(bb.x+x/320*bb.width,bb.y+y/288*bb.height)}
await p.evaluate(()=>document.querySelector('[data-la="clr"]').click());
await p.evaluate(()=>document.querySelector('[data-lc="tool:LED"]').click());
await tap(38+26*2,22);await tap(38+26*2+0,74);// P2 -> T2r0 : LED with anode on + via... 
await p.evaluate(()=>document.querySelector('[data-lc="tool:wire"]').click());
await tap(38+26*2,106);await tap(38+26*5,38); // T2r2 ... wire to N5 (note LED cathode is at T2r0 same column)
await p.waitForTimeout(200);console.log('bare LED:',await p.evaluate(()=>document.querySelector('#lro').innerText));await p.locator('#lsvw').screenshot({path:'shots/t91_b.png'});
console.log(E);await b.close()})()
