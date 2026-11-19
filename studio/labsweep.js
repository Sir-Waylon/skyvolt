const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});let tot=0;
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']]){
 const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(400);
 await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(200);
 await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);
 const has=await p.evaluate(()=>{const e=document.querySelector('[data-nav="lib:labs"]');if(e){e.click();return 1}return 0});await p.waitForTimeout(250);
 const ids=await p.evaluate(()=>[...document.querySelectorAll('[data-lab]')].map(e=>e.dataset.lab));const bad=[];
 for(const id of ids){await p.evaluate(i=>{const e=document.querySelector('[data-lab="'+i+'"]');e&&e.click()},id);await p.waitForTimeout(250);
  for(const ext of ['min','max','min']){await p.evaluate(x=>{document.querySelectorAll('.lpanel input[type=range]').forEach(i=>{i.value=i[x];i.dispatchEvent(new Event('input',{bubbles:true}))})},ext);await p.waitForTimeout(60);
   const r=await p.evaluate(()=>{const h=(document.getElementById('labroot')||document.body).innerHTML;return {nan:/NaN|Infinity|undefined/.test(h.replace(/data-[a-z]+="[^"]*"/g,'')),box:!!document.querySelector('.lbx')}});if(r.nan||!r.box)bad.push(id+':'+ext+(r.nan?' NaN':' nobox'))}
  await p.evaluate(()=>{const b=document.querySelector('[data-lab-back],#labback,.labbar [data-nav]');b&&b.click()});await p.waitForTimeout(80)}
 console.log(nm,'labs',ids.length,'bad',bad.slice(0,8),E.slice(0,2));tot+=bad.length+E.length;await p.close()}
console.log('lab issues',tot);await b.close()})()
