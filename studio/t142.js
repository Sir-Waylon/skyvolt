const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const sv=spawn('node',['server.mjs','../../out/skyvolt',8832],{cwd:'backend/test'});await new Promise(r=>setTimeout(r,700));
const p=await(await b.newContext({viewport:{width:360,height:700}})).newPage();await p.goto('http://skyvolt.localhost:8832/privacy/');await p.waitForTimeout(300);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.wrap,.in,h1,.crumbs')].map(e=>e.className+' '+e.tagName+' pad='+getComputedStyle(e).paddingLeft+' left='+Math.round(e.getBoundingClientRect().left)+' w='+Math.round(e.getBoundingClientRect().width)).join('\n')));
sv.kill();await b.close()})()
