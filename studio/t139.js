const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const s of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){const p=await(await b.newContext()).newPage();
await p.goto('file://'+process.cwd()+'/out/'+s+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{let n=0;const bad=[];P.questions.forEach(q=>{if(!q.num||q.num.v===undefined)return;n++;let t=ansText(q),g;try{g=gradeNum(q.num,t)}catch(e){g={ok:false,msg:String(e)}}if(!g.ok)bad.push(q.id+' "'+t+'"');
 // also: a wrong answer 1000x off must be rejected
 if(q.num.v){let w;try{w=gradeNum(q.num,String(parseFloat(t)*1000)+(q.num.u?' '+q.num.u:''))}catch(e){w={ok:false}}if(w.ok&&!q.num.free)bad.push(q.id+' ACCEPTS 1000x')}});return{n,bad}});
console.log(s,r.n,'round-trip failures',r.bad.length,r.bad.slice(0,12));await p.close()}await b.close()})()
