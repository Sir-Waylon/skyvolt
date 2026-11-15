const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const p=await (await b.newContext({viewport:{width:420,height:1000}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.route('**/api/config',r=>r.fulfill({json:{google:'x.apps.googleusercontent.com'}}));await p.route('**/api/me',r=>r.fulfill({status:401,json:{}}));
const fake="window.google={accounts:{id:{initialize(){},renderButton(el,o){el.innerHTML='<div style=\"border:1px solid #888;border-radius:20px;padding:10px 24px\">G '+o.text+'</div>'}}}}";
await p.route('https://accounts.google.com/**',r=>r.fulfill({contentType:'text/javascript',body:fake}));
await p.goto('http://localhost:8765/account/');await p.waitForTimeout(600);await p.screenshot({path:'shots/acct1.png'});await p.click('#mUp');await p.waitForTimeout(300);await p.screenshot({path:'shots/acct2.png'});console.log(e);await b.close()})()
