const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,slug] of [['_app_skyvolt','circuit'],['_app_axiom','apex']]){
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${app}/${slug}/index.html`);await p.waitForTimeout(400);
const r=await p.evaluate(()=>{S.coins=400;var sh=shopHTML();var res=[];for(var i=0;i<60;i++){var x=rollBox(PACKS[2]);res.push(x.ch[0])}var ok=res.every(isSeason);var nrm=[];for(i=0;i<60;i++){nrm.push(rollBox(PACKS[0]).ch[0])}
return{packs:packList().length,seasonOnly:ok,normalClean:nrm.every(function(x){return !isSeason(x)}),odds:(sh.match(/class="odds"/g)||[]).length,pc:packCard().slice(0,60),AV:AV.length}});
console.log(slug,JSON.stringify(r),E.slice(0,2));
await p.evaluate(()=>{S.coins=400;S.cu=null;route()});await p.click('#nav button[data-t="me"]');await p.waitForTimeout(300);
const sb=await p.$('[data-nav="me:shop"],[data-nav*="shop"]');if(sb){await sb.click();await p.waitForTimeout(400)}
await p.screenshot({path:`shots/t101_${slug}.png`,fullPage:false});await p.close()}
await b.close()})()
