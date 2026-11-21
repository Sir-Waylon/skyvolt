const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const s of ['_app_skyvolt/circuit','_app_axiom/quanta']){const p=await(await b.newContext()).newPage();
await p.goto('file://'+process.cwd()+'/out/'+s+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const out=[];
 P.questions.forEach(q=>{if(!q.num||q.num.v===undefined||!q.num.u)return;const n=q.num;const txt=((q.sol||[]).join(' ')+' '+(q.w||'')).replace(/−/g,'-').replace(/,/g,'');
  const m=txt.match(/=\s*(-?\d+\.?\d*)\s*([a-zA-ZµΩ°/·²³]+)/g)||[];const last=m[m.length-1];if(!last)return;const mm=last.match(/=\s*(-?\d+\.?\d*)\s*(\S+)/);if(!mm)return;
  const typed=mm[1]+' '+mm[2].replace(/[.,;]$/,'');let g;try{g=gradeNum(n,typed)}catch(e){g={ok:false}}
  const shown=ansText(q);
  if(!g.ok)out.push(q.id+' typed "'+typed+'" -> '+JSON.stringify(g)+' | v='+n.v+' u='+n.u+' shown="'+shown+'"')});
 return out});
console.log(s,r.length);r.slice(0,60).forEach(x=>console.log('  ',x));await p.close()}await b.close()})()
