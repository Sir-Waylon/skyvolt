const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:700}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
let inc=[];const calls=[];
await p.route(/file:\/\/\/api\/.*/,r=>{const u=r.request().url().replace('file:///api','');calls.push(u.split('?')[0]);const J=o=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(o)});
 if(u.startsWith('/config'))return J({google:null});if(u.startsWith('/me'))return J({username:'tester',csrf:'c',shared:{}});if(u.startsWith('/save'))return J({state:null});
 if(u.startsWith('/friends/ping'))return J({inc,n:0});if(u.startsWith('/friends/suggest'))return J({names:['bob_2','bobby']});
 if(u.startsWith('/friends'))return J({league:[],incoming:inc.map(x=>({username:x})),outgoing:[]});return J({ok:1})});
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.waitForTimeout(3600);inc=['alice_1'];
await p.waitForSelector('#frq',{timeout:14000});console.log('banner',await p.textContent('#frq'));await p.screenshot({path:'shots/t106.png'});
await p.click('#frq [data-qa]');await p.waitForTimeout(300);console.log('calls',[...new Set(calls)].join(' '),E);
await b.close()})()
