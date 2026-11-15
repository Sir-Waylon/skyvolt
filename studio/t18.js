const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const jobs=[['8801','sky','/',1280,900,'light'],['8801','sky','/',390,844,'dark'],['8802','ax','/',1280,900,'light'],['8802','ax','/account/',390,844,'light'],['8801','sky','/science/',1000,800,'dark'],['8802','ax','/privacy/',390,844,'light']];
for(const [pt,n,path,w,h,cs] of jobs){const c=await b.newContext({viewport:{width:w,height:h},colorScheme:cs});const p=await c.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));p.on('console',m=>{if(m.type()==='error')e.push(m.text())});
await p.goto('http://localhost:'+pt+path);await p.waitForTimeout(400);
await p.screenshot({path:`ck/site_${n}_${path.replace(/\//g,'')||'home'}_${w}_${cs}.png`,fullPage:path==='/'});console.log(n,path,w,cs,e.slice(0,3));await c.close()}
await b.close()})()
