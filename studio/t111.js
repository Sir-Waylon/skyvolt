const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const ctx=await b.newContext({viewport:{width:390,height:844},hasTouch:true});const p=await ctx.newPage();const E=[];p.on('pageerror',x=>E.push(x.stack.split('\n').slice(0,4).join(' | ')));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(300);
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(250);
await p.evaluate(()=>document.querySelector('[data-lab="ohm"]').click());await p.waitForTimeout(500);
const rd=()=>p.evaluate(()=>[document.querySelector('#lo_V').textContent,document.querySelector('.ltot').textContent.slice(0,60)]);
console.log('start',await rd());
const plus=(await p.$$('.lstb'))[1];await plus.click();await plus.click();console.log('after +2',await rd());
const tr=await p.$('.ltrk');const bb=await tr.boundingBox();await p.mouse.click(bb.x+bb.width*0.9,bb.y+bb.height/2);await p.waitForTimeout(100);console.log('tap track 90%',await rd());
await (await p.$('.lpanel')).scrollIntoViewIfNeeded();await p.screenshot({path:'shots/t111.png'});console.log(E);await b.close()})()
