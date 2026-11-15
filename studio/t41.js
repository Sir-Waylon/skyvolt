const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
const p=await (await b.newContext({viewport:{width:400,height:800}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/apex/index.html');await p.waitForTimeout(400);
const n=await p.evaluate(()=>{window.sfxList.forEach(k=>sfx(k));return window.sfxList.length});
await p.evaluate(()=>{const q=QS.find(q=>q.num);startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(300);
console.log('sounds',n,'errors',e);await b.close()})()
