const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:1})).newPage();
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(600);
await p.evaluate(()=>{S.stat={};S.un={};const u=UN[1];startLesson(u.id,u.lessons[0].id);Z.i=1;drawSess()});await p.waitForTimeout(500);await p.screenshot({path:'/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/ex.png'});
await p.evaluate(()=>{closeSess();S.stat[UN[1].id]=[18,20];const u=UN[1];startLesson(u.id,u.lessons[0].id);const it=Z.steps[0].it;it.done=true;it.ok=false;advance()});await p.waitForTimeout(500);await p.screenshot({path:'/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/rf.png'});await b.close()})()
