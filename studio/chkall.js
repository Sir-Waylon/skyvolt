const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const bad=[];let n=0;
QS.forEach(q=>{try{
 if(q.type==='short'){n++;const a=shortAnswer(q);const g=gradeShort(q,String(a));if(!(g.ok||g===true))bad.push(['selfgrade',q.id,a,q.q.slice(0,60)]);
   if(q.num&&q.num.pi){const g2=gradeShort(q,String(q.num.v)+'π');if(!(g2.ok))bad.push(['pi',q.id,q.num.v])}}
 const it=mkItem(q.id);const h=qBody(it,false);if(!h||h.length<10)bad.push(['empty',q.id]);
 if(!q.sol&&!q.w)bad.push(['nosol',q.id]);
 if(q.bld){const i3=mkItem(q.id),D=['N','NE','E','SE','S','SW','W','NW'];if(q.type==='resnet')i3.o=q.rn.sol.slice();else if(q.type==='barb'){i3.d=D.indexOf(q.bb.d);const k=q.bb.kt;i3.n=[Math.floor(k/50),Math.floor(k%50/10),k%10/5]}else if(q.type==='xform')i3.mv=q.xf.sol.slice();else if(q.type==='ucirc'){i3.a=q.uc.a;i3.t=true}else if(q.type==='fitc'){i3.p=Object.assign({},q.fc.t);i3.t=true}else if(q.type==='frbal'){i3.T=q.fr.sol.slice();i3.t=true}else if(q.type==='lgate')i3.g=q.lg.sol.slice();else if(q.type==='sbx')__sbxSolve(i3);else if(q.type==='lab'){i3.v=Object.assign({},q.lab.sv);i3.t=true}else if(q.type==='balance'||q.type==='machine'||q.type==='mistake')__gmSolve(i3);if(!IT[q.type].ok(i3))bad.push(['unsolvable',q.id,q.type]);const h4=qBody(i3,true);if(!h4||h4.length<20)bad.push(['revempty',q.id])}
 else if(q.type==='sim'){const i3=mkItem(q.id),pm=q.sim.params[0];let f=false;for(let v=pm.min;v<=pm.max+1e-9;v+=pm.step){i3.v[pm.n]=+v.toFixed(6);if(IT.sim.ok(i3)){f=true;break}}if(!f)bad.push(['unsolvable',q.id,'sim']);i3.touched=true;const h3=qBody(i3,true);if(!h3||h3.length<20)bad.push(['revempty',q.id])}
 else if(IT[q.type]){const t=IT[q.type];const i2=mkItem(q.id);const b=q.type==='chips'||q.type==='proof'?bankOf(q):0;
  if(q.type==='slider'||q.type==='angle')i2.val=q.type==='slider'?q.sl.target:q.ang.target;else if(q.type==='point')i2.pt=[q.pt.x,q.pt.y];else if(q.type==='compass')i2.val=q.cmp.target;else if(q.type==='graph')i2.pt=q.gr.t;
  else{const c=blanksOf(q);const used={};i2.bl=c.map(x=>{for(let k=0;k<b.length;k++)if(b[k]===x&&!used[k]){used[k]=1;return k}return null})}
  if(!t.ok(i2))bad.push(['unsolvable',q.id,q.type]);
  const h2=qBody(i2,true);if(!h2||h2.length<20)bad.push(['revempty',q.id]);
  if(q.type==='chips'||q.type==='proof'){const ct=blanksOf(q).length;if(!ct||new Set(b).size<b.length-ct)bad.push(['bank',q.id]);if(q.type==='chips'){const ids=(q.tpl.match(/\{\d+\}/g)||[]);if(ids.length!==ct||new Set(ids).size!==ct)bad.push(['tpl',q.id])}}
  if((q.type==='slider')&&(q.sl.target<q.sl.min||q.sl.target>q.sl.max||(q.sl.target-q.sl.min)%q.sl.step))bad.push(['slrange',q.id])}
 if(q.type==='mcq'&&new Set(q.o).size<q.o.length)bad.push(['dupopt',q.id]);
 if(q.type==='mcq'&&q.o.length!==4)bad.push(['not4',q.id,q.o.length]);
}catch(e){bad.push(['err',q.id,String(e).slice(0,80)])}});
return {n,bad:bad.length,sample:bad.slice(0,12)}});
console.log(JSON.stringify(r));console.log('pageerrors',errs.slice(0,3));await b.close()})();
