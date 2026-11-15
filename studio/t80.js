const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,vw] of [['_app_axiom/apex',[1280,800]],['_app_axiom/apex',[390,844]],['_app_axiom/quanta',[390,844]]]){
const p=await (await b.newContext({viewport:{width:vw[0],height:vw[1]}})).newPage();p.setDefaultTimeout(3000);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(250);
await p.evaluate(()=>document.querySelector('[data-nav="lib:graph"]').click());await p.waitForTimeout(500);
const n0=await p.evaluate(()=>document.querySelectorAll('.ginp').length);
await p.fill('.ginp[data-gi="0"]','y=x^2-2');await p.waitForTimeout(100);
await p.click('.gex summary');await p.click('[data-gr="ex:7"]');await p.click('[data-gr="ex:6"]');await p.waitForTimeout(200);
const px=await p.evaluate(()=>{const c=document.getElementById('gcv'),x=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let i=0;i<x.length;i+=4)if(x[i]!==x[0]||x[i+1]!==x[1])n++;return n});
const box=await p.$eval('#gcv',e=>{const r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]});
await p.mouse.move(box[0]+box[2]/2,box[1]+box[3]/2);await p.mouse.down();await p.mouse.move(box[0]+box[2]/2+50,box[1]+box[3]/2+20,{steps:4});await p.mouse.up();
await p.click('[data-gr="zi"]');await p.waitForTimeout(150);
await p.fill('.ginp[data-gi="0"]','y=foo(');await p.waitForTimeout(100);const err=await p.$('.gerr');
const sl=await p.$$('[data-gs]');
const over=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
await p.screenshot({path:'shots/t80_'+vw[0]+app.split('/')[1]+'.png'});
console.log(app,vw[0],'rows',n0,'ink px',px,'err shown',!!err,'sliders',sl.length,'overflow',over,E);await p.close()}
await b.close()})()
