const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext()).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>new Promise(()=>{}));// CDN hangs forever
const t=Date.now();await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html',{waitUntil:"domcontentloaded"});await p.waitForFunction(()=>document.querySelector('#nav button'),null,{timeout:8000});
console.log('app interactive with a hanging CDN after',Date.now()-t,'ms; css media now',await p.evaluate(()=>document.getElementById('katexcss').media));await b.close()})()
