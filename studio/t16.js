const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const solvers={
mystery:s=>{s.m={k:s.Vs*s.Rk/(s.Rk+s.Rx),x:s.Vs*s.Rx/(s.Rk+s.Rx)};s.in.rx=String(s.Rk*s.m.x/s.m.k)},
target:s=>{s.sawOff=true;const P=s.parts,perms=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];for(const t of['s','p','m'])for(const q of perms){if(Math.abs(spReq(t,q.map(i=>P[i]))-s.T)<=s.T*.03){s.parts=q.map(i=>P[i]);s.topo=t;return}}},
trouble:s=>{s.dx=s.f;s.n=2},
led:s=>{const Rc=(s.Vs-s.c[1])/(s.If/1000);s.in.rc=String(Rc);let b=0,bd=1e9;ESER.forEach((r,i)=>{const I=(s.Vs-s.c[1])/r*1000;if(I<=25&&Math.abs(I-s.If)<bd){bd=Math.abs(I-s.If);b=i}});s.idx=b},
logic:s=>{s.u=Object.assign({},s.t)},
power:s=>{const P=s.lv[2][0]*s.lv[2][1],Wh=s.bv*s.mah/1000;s.in.p1=String(P);s.in.wh=String(Wh);s.in.hr=String(Wh/(P*s.eff/100))},
threeway:s=>{s.pick={A:1,B:1}},
board:s=>{const c=s.col;if(s.rail){for(let k=1;k<=12;k++){if(k===c)continue;if(s.split&&((k<=6)!==(c<=6)))continue;s.sel['r'+s.rrow+'-'+k]=1}}else(s.top?['a','b','c','d','e']:['f','g','h','i','j']).forEach(r=>{if(r!==s.row)s.sel[r+c]=1});s.dial=s.sc[1];s.port=s.sc[2]},
magnet:s=>{s.N=s.maxN;s.B=s.maxB;s.core=2;s.rec=[1,2]},
smodel:s=>{s.in={T:String(s.T),Td:String(s.Td),p:String(s.p),dir:String(s.dir),spd:String(s.spd),sky:s.sky[0],fc:(s.kind==='ts'?'ts':(s.kind==='rain'||s.kind==='snow')?'rain':(s.T-s.Td<=2&&s.spd<=5)?'fog':'clear')}},
metar:s=>{s.in={dir:String(s.dir),spd:String(s.spd),gust:String(s.gust),vis:s.vis,wx:s.wx[0]||'none',ceil:String(s.ceil),T:String(s.T),Td:String(s.Td),alt:s.alt.toFixed(2)}},
scale:s=>{if(s.hur){const w=s.w;s.in={cat:ssCat(w),maj:w>=111?'Yes':'No'}}else{const t=(s.pre?FF:EF).filter(t=>s.w>=t[0]&&s.w<=t[1])[0][2];s.in={sc:s.pre?'F':'EF',r:t.replace('EF','').replace('F','')}}},
radar:s=>{const A=RANS[s.k];s.in={sig:A[0],hz:A[1],pr:A[2]}},
sounding:s=>{const d=SND[s.k];const sp=LVL.map((p,i)=>d.T[i]-d.D[i]);let inv='none';for(let i=0;i<LVL.length-1;i++)if(d.T[i+1]>d.T[i]){inv=LVL[i]+'-'+LVL[i+1];break}s.in={moist:String(LVL[sp.indexOf(Math.min(...sp))]),inv:inv,lcl:String(125*(d.sfc[0]-d.sfc[1])),con:d.ans}},
case:s=>{s.in={ty:s.k,hz:s.k,ac:s.k};s.all.forEach((a,i)=>{if(a[1])s.pick[i]=true})}};
for(const [n,f] of [['circ','skyvolt/app/circuit/index.html'],['met','skyvolt/app/meteorology/index.html']]){
const p=await b.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/'+f.replace(/^(skyvolt|axiom)\//,'$1/app/'));await p.waitForTimeout(400);
const ids=await p.evaluate(()=>STN.list.map(o=>o.id));
for(const id of ids){let low=0;for(let k=0;k<12;k++){const r=await p.evaluate(([id,sv])=>{stnOpen(id);const s=STN.st;eval('('+sv+')')(s);try{const r=STN.cur.check(s);return r.score}catch(x){return 'ERR '+x.message}},[id,solvers[id].toString()]);if(r!==1){low++;if(low<3)console.log(' ',id,'score',r)}}
console.log(n,id,low?'LOW '+low+'/12':'ok')}
console.log(n,e);await p.close()}
await b.close()})()
