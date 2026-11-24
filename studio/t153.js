const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:430,height:900},deviceScaleFactor:3})).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(600);
console.log(await p.evaluate(()=>{const r=document.querySelector('.lvring'),s=r.querySelector('span');const a=r.getBoundingClientRect(),c=s.getBoundingClientRect(),cs=getComputedStyle(s);return JSON.stringify({tag:r.tagName,ring:[a.x,a.y,a.width,a.height],span:[c.x,c.y,c.width,c.height],pad:cs.padding,mar:cs.margin,pos:cs.position,html:r.outerHTML.slice(0,300)})}));
const el=await p.$('.lvring');await el.screenshot({path:'shots/ring.png'});await b.close()})()
