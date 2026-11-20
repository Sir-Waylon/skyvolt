const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext()).newPage();const seen=[];await p.route('**/cdn.jsdelivr.net/**',r=>{seen.push(r.request().url().split('/').pop());r.abort()});
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(1500);console.log('requested:',seen.join(','));await b.close()})()
