const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const sv=spawn('node',['server.mjs','../../out/skyvolt',8831],{cwd:'backend/test'});await new Promise(r=>setTimeout(r,700));
for(const w of [360,1280]){const p=await(await b.newContext({viewport:{width:w,height:700}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://skyvolt.localhost:8831/privacy/');await p.fill('#sq','diod');await p.waitForTimeout(500);
 const r=await p.evaluate(()=>({n:document.querySelectorAll('#sres li').length,first:(document.querySelector('#sres li')||{}).textContent,hidden:document.getElementById('sres').hidden,ow:document.documentElement.scrollWidth>innerWidth,crumb:(document.querySelector('.crumbs')||{}).textContent,r:document.querySelector('.srch').getBoundingClientRect().toJSON()}));
 console.log(w,JSON.stringify(r),errs);await p.screenshot({path:`../shots/search-${w}.png`})}
sv.kill();await b.close()})()
