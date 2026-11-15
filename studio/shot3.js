const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:700}});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(400);
for(const f of process.argv.slice(3)){await p.evaluate(f=>{const q=QS.find(q=>q.fp===f&&q.svg);startFromIds([q.id])},f);await p.waitForTimeout(350);await p.screenshot({path:'ck/f_'+f+'.png',clip:{x:0,y:60,width:400,height:420}})}
await b.close()})();
