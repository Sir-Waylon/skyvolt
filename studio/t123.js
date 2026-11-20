const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const site of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){
const p=await (await b.newContext()).newPage();await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(500);
const r=await p.evaluate(()=>{let cs=[];UN.forEach(u=>u.lessons.forEach(l=>l.cards.forEach(c=>cs.push({u:u.id,t:(c.t||'').length,f:!!c.f,dd:!!c.dd,q:!!c.q}))));
 const L=cs.map(c=>c.t).sort((a,b)=>a-b);let noex=0,noQ=0;UN.forEach(u=>{const have=new Set(QS.filter(q=>q.t===u.id&&q.sol&&q.sol.length>=2).map(q=>q.id));if(have.size<3)noex++});
 return{units:UN.length,lessons:UN.reduce((a,u)=>a+u.lessons.length,0),cards:cs.length,med:L[L.length>>1],short:L.filter(x=>x<80).length,nof:cs.filter(c=>!c.f).length,dd:cs.filter(c=>c.dd).length,unitsFewWorked:noex}});
console.log(site,JSON.stringify(r));await p.close()}await b.close()})()
