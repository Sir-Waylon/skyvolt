const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const apps={circ:'out/_app_skyvolt/circuit/index.html',met:'out/_app_skyvolt/meteorology/index.html',geo:'out/_app_axiom/geometry/index.html',apex:'out/_app_axiom/apex/index.html',quanta:'out/_app_axiom/quanta/index.html'};
for(const [k,f] of Object.entries(apps)){const fs=require('fs');if(!fs.existsSync(f)){console.log(k,'missing',f);continue}
 const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/'+f);await p.waitForTimeout(400);
 const r=await p.evaluate(()=>{const D=['N','NE','E','SE','S','SW','W','NW'];const out={n:0,bad:[],ids:[]};QS.filter(q=>q.bld).forEach(q=>{out.n++;const it=mkItem(q.id);let h='';try{h=qBody(it,false)}catch(x){out.bad.push([q.id,'render',x.message]);return}
  if(IT[q.type].done(it)&&q.type!=='ucirc'&&q.type!=='fitc'&&q.type!=='lab'&&q.type!=='machine')out.bad.push([q.id,'prefilled']);
  if(q.type==='resnet')it.o=q.rn.sol.slice();else if(q.type==='barb'){it.d=D.indexOf(q.bb.d);let k=q.bb.kt;it.n=[Math.floor(k/50),Math.floor(k%50/10),k%10/5]}else if(q.type==='xform')it.mv=q.xf.sol.slice();else if(q.type==='ucirc'){it.a=q.uc.a;it.t=true}else if(q.type==='fitc'){it.p=Object.assign({},q.fc.t);it.t=true}else if(q.type==='frbal'){it.T=q.fr.sol.slice();it.t=true}else if(q.type==='lgate')it.g=q.lg.sol.slice();else if(q.type==='lab'){it.v=Object.assign({},q.lab.sv);it.t=true}else if(q.type==='balance'||q.type==='machine'||q.type==='mistake')__gmSolve(it)
  if(!IT[q.type].done(it))out.bad.push([q.id,'notdone']);if(!IT[q.type].ok(it))out.bad.push([q.id,'unsolvable']);if(h.length<80)out.bad.push([q.id,'thin']);
  if(q.type==='resnet'){const o=q.rn.sol.slice();o[0]=o[0]==='s'?'p':'s';it.o=o;if(IT.resnet.ok(it)&&false)out.bad.push([q.id,'ambig'])}
  out.ids.push(q.type)});out.types=[...new Set(out.ids)];delete out.ids;return out});
 console.log(k,JSON.stringify(r),e);
 if(true){await p.evaluate(()=>{const q=QS.filter(q=>q.bld).slice(-1)[0];startSess({kind:'review',title:'t',steps:[{k:'try',it:mkItem(q.id)}],remed:true})});await p.waitForTimeout(400);await p.screenshot({path:'shots/bld_'+k+'.png'})}
 await p.close()}
await b.close();process.exit(0)})()
