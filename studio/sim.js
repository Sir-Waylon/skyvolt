const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.argv[2]);await p.waitForTimeout(300);
const out=await p.evaluate(()=>{
 const res=[];
 function hash(s){let h=0;for(const c of s)h=(h*31+c.charCodeAt(0))|0;return h}
 for(const thTrue of [-1.2,-0.3,0.5,1.5]){
  // reset learner
  S.mem={};S.th={};S.rn={};S.stat={};S.seen={};S.miss={};S.xp=0;S.total=0;DOFF=0;
  const log=[];let sessions=0;
  for(let day=0;day<14;day++){DOFF=day;
   for(let s=0;s<2;s++){const used=[],last=[],dset={};
    for(let n=0;n<15;n++){
     const dl=Math.ceil(15*.35)-used.filter(u=>dset[u]).length;const id=coachPick({topics:ALL,exclude:used,last:last.slice(-3),target:n===0?.93:.85,dueLeft:dl});{const mm=S.mem[id];if(mm&&mm[1]<=dayN())dset[id]=1}used.push(id);
     const q=QS[QI[id]],m=S.mem[id],wasDue=m?m[1]<=dayN():false,fresh=!m;
     const bTrue=LB[q.l]+((hash(id)%100)/100-.5)*.8;const p=1/(1+Math.exp(-(thTrue-bTrue)));
     const ok=Math.random()<p;
     const st=S.stat[q.t]||[0,0];st[1]++;if(ok)st[0]++;S.stat[q.t]=st;S.seen[id]=(S.seen[id]||0)+1;
     coachUpdate(q,ok,false);
     log.push({day,ok,t:q.t,l:q.l,wasDue,fresh,adj:last.length&&last[last.length-1]===q.t,rep:0});last.push(q.t)}}}
  const L=log.filter(x=>x.day>=10),all=log;
  const acc=a=>a.filter(x=>x.ok).length/a.length;
  res.push({thTrue,accLast4days:+acc(L).toFixed(2),accFirst2:+acc(log.filter(x=>x.day<2)).toFixed(2),dueShare:+(all.filter(x=>x.wasDue).length/all.length).toFixed(2),adjSame:+(all.filter(x=>x.adj).length/all.length).toFixed(2),topics:new Set(all.map(x=>x.t)).size,lvDist:[1,2,3].map(l=>+(L.filter(x=>x.l===l).length/L.length).toFixed(2)),thEst:+(Object.values(S.th).reduce((a,b)=>a+b,0)/Math.max(1,Object.keys(S.th).length)).toFixed(2)})}
 return res});
console.log(JSON.stringify(out,null,1));console.log('errs',errs);await b.close()})();
