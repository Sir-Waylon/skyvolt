const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const out=[];QS.filter(q=>q.id.indexOf('xh1')>0&&q.type==='short'&&q.t==='ti').slice(0,6).forEach(q=>{const v=q.num.v;const fr=(()=>{for(let d=2;d<=50;d++){const n=Math.round(v*d);if(Math.abs(n/d-v)<1e-9)return n+'/'+d}return null})();out.push([q.id,v,fr,fr?!!gradeShort(q,fr).ok:null,!!gradeShort(q,String(v.toFixed(3))).ok])});return JSON.stringify(out)}));
await b.close()})()
