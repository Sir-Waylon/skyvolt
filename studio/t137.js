const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const s of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){const p=await(await b.newContext()).newPage();
await p.goto('file://'+process.cwd()+'/out/'+s+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const N=/-?\d[\d,]*\.?\d*/g;const out=[];let n=0;
 P.questions.forEach(q=>{if(!q.num||q.num.v===undefined)return;n++;const t=ansText(q);const a=parseFloat((t.replace(/,/g,'').match(/-?\d+\.?\d*(e[+-]?\d+)?/)||[])[0]);if(!isFinite(a)||!a)return;
  const txt=((q.sol||[]).join(' ')+' '+(q.w||'')).replace(/−/g,'-').replace(/,/g,'');const nums=(txt.match(/-?\d+\.?\d*/g)||[]).map(Number);
  if(!nums.length)return;if(nums.some(x=>Math.abs(x-a)<=Math.abs(a)*0.03+1e-9))return;
  const sc=[1e3,1e-3,1e6,1e-6,1e2,1e-2].find(k=>nums.some(x=>Math.abs(x-a*k)<=Math.abs(a*k)*0.03));if(sc)out.push(q.id+' ans="'+t+'" scale '+sc)});
 return {n,out}});
console.log(s,r.n,r.out.length);r.out.slice(0,40).forEach(x=>console.log('  ',x));await p.close()}await b.close()})()
