const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const V=[[320,568],[360,640],[390,844],[640,360],[768,1024],[1024,768],[1280,800],[1920,600],[2560,1080]];
for(const app of ['_app_skyvolt/circuit','_app_axiom/quanta']){for(const [w,h] of V){
const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();p.on('pageerror',x=>console.log('ERR',x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const r=await p.evaluate(()=>{const bad=[];const dw=document.documentElement.scrollWidth>innerWidth+1;
 document.querySelectorAll('#nav button').forEach(b=>{const s=b.querySelector('svg').getBoundingClientRect(),br=b.getBoundingClientRect(),sp=b.querySelector('span');if(s.width<16||s.left<br.left-1||s.right>br.right+1||s.top<br.top-1||s.bottom>br.bottom+1||sp.scrollWidth>b.clientWidth+1)bad.push(['nav',b.dataset.t,Math.round(s.width),Math.round(br.width),sp.scrollWidth,b.clientWidth])});
 const lg=document.querySelector('.logo'),ls=lg.querySelector('svg').getBoundingClientRect(),lr=lg.getBoundingClientRect();if(ls.left<lr.left-1||ls.right>lr.right+1||ls.width<14)bad.push(['logo',ls.width,lr.width]);
 const nav=document.getElementById('nav').getBoundingClientRect();if(nav.right>innerWidth+1)bad.push(['navwide']);
 return{dw,bad}});
if(r.dw||r.bad.length)console.log(app,w+'x'+h,JSON.stringify(r));
if(w===320||w===1920)await p.screenshot({path:`shots/t61_${app.split('/')[1]}_${w}.png`})}}
console.log('done');await b.close();process.exit(0)})()
