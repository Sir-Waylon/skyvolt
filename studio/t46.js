const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const a of ['_app_axiom/apex','_app_axiom/geometry','_app_axiom/quanta','_app_skyvolt/circuit','_app_skyvolt/meteorology']){
const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+a+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const S2=QS.filter(q=>q.type==='sim'),bad=[],tot=S2.length;let hits=0;const per={};
 S2.forEach(q=>{const g=q.sim,pm=g.params[0],ok=[];const it=mkItem(q.id);
  for(let v=pm.min;v<=pm.max+1e-9;v+=pm.step){it.v[pm.n]=+v.toFixed(6);if(IT.sim.ok(it))ok.push(+v.toFixed(3))}
  per[q.fp]=(per[q.fp]||0)+1;
  if(!ok.length)bad.push(q.id+' '+q.q.slice(0,60));else{hits++;if(ok.length>6&&g.goal.lo===undefined)bad.push('wide '+q.id+' '+ok.length)}
 });
 // play one end-to-end
 const q=S2[0];let res='none';if(q){startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]});}
 return {tot,hits,bad:bad.slice(0,6),per}});
await p.waitForTimeout(300);
const ui=await p.evaluate(async()=>{const it=Z.steps[0].it;const pm=it.q.sim.params[0];let best=null;for(let v=pm.min;v<=pm.max+1e-9;v+=pm.step){it.v[pm.n]=+v.toFixed(6);if(IT.sim.ok(it)){best=+v.toFixed(6);break}}
 const r=document.querySelector('.simr');r.value=best;r.dispatchEvent(new Event('input',{bubbles:true}));await new Promise(x=>setTimeout(x,100));document.querySelector('[data-simtest]').click();await new Promise(x=>setTimeout(x,150));const chk=document.getElementById('chk');chk.click();await new Promise(x=>setTimeout(x,200));return [it.ok,!!document.querySelector('.rwtag')]});
console.log(a.split('/').pop(),JSON.stringify(r),ui,e.slice(0,2));
if(a.includes('circuit')){await p.evaluate(()=>closeSess());await p.evaluate(()=>{const q=QS.find(q=>q.type==='sim');startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(300);await p.screenshot({path:'shots/sim.png'})}
}
await b.close()})()
