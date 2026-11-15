const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:800}});await p.goto('file://'+process.argv[2]);await p.waitForTimeout(500);
await p.screenshot({path:'ck/n_learn.png'});
await p.evaluate(()=>{startLesson(UN[0].id,UN[0].lessons[0].id)});await p.waitForTimeout(400);await p.screenshot({path:'ck/n_card.png'});
const d=await b.newPage({viewport:{width:1280,height:800}});await d.goto('file://'+process.argv[2]);await d.waitForTimeout(500);await d.screenshot({path:'ck/n_desk.png'});
await b.close()})();
