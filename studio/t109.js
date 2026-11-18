const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [u,n,ids] of [['_app_skyvolt/circuit','c',['ohm','rc','net','bulb']],['_app_skyvolt/meteorology','m',['front','hum','stn']],['_app_axiom/quanta','q',['proj','coll','swing']]]){
for(const vw of [[390,800],[1100,800]]){const p=await (await b.newContext({viewport:{width:vw[0],height:vw[1]}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${u}/index.html`);await p.waitForTimeout(600);await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(300);
for(const id of ids){await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(250);
 const ok=await p.evaluate(i=>{const b=document.querySelector('[data-lab="'+i+'"]');if(b){b.click();return 1}return 0},id);await p.waitForTimeout(500);
 const r=await p.evaluate(()=>({lbx:!!document.querySelector('.lbx'),pn:document.querySelectorAll('.lpanel [data-ls],.lpanel [data-lc],.lpanel button').length,sv:!!document.querySelector('.lstage #lsv'),tot:(document.querySelector('.ltot')||{}).textContent?.length}));
 const sl=await p.$('.lpanel input[type=range]');if(sl){await sl.focus();await p.keyboard.press('ArrowRight');await p.waitForTimeout(100)}
 console.log(n,vw[0],id,ok,JSON.stringify(r));
 if(id===ids[0])await p.screenshot({path:`shots/t109_${n}_${vw[0]}.png`});
 await p.evaluate(()=>{const e=document.querySelector('[data-lab=""]');e&&e.click()});await p.waitForTimeout(150)}
console.log(n,vw[0],'errors',E.slice(0,2))}}
await b.close()})()
