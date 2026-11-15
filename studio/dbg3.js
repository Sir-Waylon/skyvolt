const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});p.on('pageerror',e=>console.log('PE',e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(300);
await p.evaluate(()=>{startLesson(UN[0].id,UN[0].lessons[0].id)});
for(let i=0;i<8;i++){console.log(await p.evaluate(()=>{var s=Z.steps[Z.i];return Z.i+':'+s.k+':'+(document.getElementById('go')?'go':'')+(document.getElementById('nx')?'nx':'')+(document.querySelector('.sheet')?'sheet':'NOSHEET')}));
 const k=await p.evaluate(()=>Z.steps[Z.i].k);if(k==='card')await p.click('#go');else{await p.evaluate(()=>{var it=Z.steps[Z.i].it;solve=null;var q=it.q;if(q.type==='mcq')it.sel=[0];else it.val=shortAnswer(q);resolveIt(it);drawSess()});await p.click('#nx').catch(e=>console.log('nonx'))}await p.waitForTimeout(100)}
await b.close()})();
