const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--no-sandbox']});const out=[];
for(const [w,h] of [[1280,900],[390,800]]){const p=await b.newPage({viewport:{width:w,height:h}});const err=[];p.on('pageerror',e=>err.push(e.message));p.on('console',m=>{if(m.type()==='error')err.push(m.text())});
await p.goto('http://127.0.0.1:8811/guides/hovercraft/');
const g=async id=>(await p.textContent('#'+id)).trim();
const r={ds:await g('o_ds'),ts:await g('o_ts'),ms:await g('o_ms'),rs:await g('o_rs'),lp:await g('lf_p'),bt:await g('bt_r'),btv:await g('bt_ok'),tc:await g('rl_tc'),td:await g('rl_td'),du:await g('rl_du')};
await p.selectOption('#sc_p','1');r.ramp=[await g('o_ds'),await g('o_ms')];
const ov=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
await p.screenshot({path:'shots/hc_'+w+'.png',fullPage:true});
out.push({w,r,ov,err});await p.close()}
console.log(JSON.stringify(out,null,1));await b.close()})();
