const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [site,port] of [['skyvolt',8821],['axiom',8822]]){const sv=spawn('node',['server.mjs','../../out/'+site,port],{cwd:'backend/test'});await new Promise(r=>setTimeout(r,700));
 const base='http://'+site+'.localhost:'+port;
 let p=await(await b.newContext({viewport:{width:1280,height:900}})).newPage();await p.goto(base+'/');await p.waitForTimeout(600);await p.screenshot({path:`../shots/${site}-landing.png`});
 p=await(await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();await p.goto(base+'/app/'+(site=='skyvolt'?'circuit':'apex')+'/');await p.waitForTimeout(900);
 await p.evaluate(()=>{document.getElementById('gate')&&document.getElementById('gate').remove();document.querySelectorAll('[inert]').forEach(e=>e.removeAttribute('inert'))});await p.waitForTimeout(300);await p.screenshot({path:`../shots/${site}-home.png`});
 await p.evaluate(()=>{const t=document.querySelector('#nav button[data-t="play"]');t&&t.click()});await p.waitForTimeout(400);await p.screenshot({path:`../shots/${site}-play.png`});sv.kill()}
await b.close()})()
