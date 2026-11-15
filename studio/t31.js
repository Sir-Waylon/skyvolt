const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:420,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/index.html');await p.waitForTimeout(500);
const r=await p.evaluate(()=>{
 // simulated student: strong at typing, weak at choosing
 const skill={short:.9,proof:.8,mcq:.55,multi:.5,slider:.8,angle:.8,point:.75,compass:.7,graph:.7,order:.7,match:.7,chips:.7};
 const seen={};let n=0;
 for(let i=0;i<400;i++){const id=coachPick({topics:ALL,exclude:[],last:[]});if(!id)break;const q=QS[QI[id]];seen[q.type]=(seen[q.type]||0)+1;
  const ok=Math.random()<skill[q.type];coachUpdate(q,ok,false);if(i%20===0)S.mem={};n++}
 return {n,seen,fm:Object.fromEntries(Object.entries(S.fm).map(([k,v])=>[k,[v.n,+v.res.toFixed(2),+fmAdj(k).toFixed(2)]]))}});
console.log(JSON.stringify(r));
await p.evaluate(()=>{cur='me';sub.me='profile';route()});await p.screenshot({path:process.env.OUT+'/style.png',fullPage:true});
console.log('errors',JSON.stringify(e));await b.close()})()
