const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const sites=[['skyvolt',8851],['axiom',8852]];const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [s,port] of sites){const hdr={};fs.readFileSync('out/'+s+'/_headers','utf8').split('\n\n')[0].split('\n').slice(1).forEach(l=>{const i=l.indexOf(':');if(i>0)hdr[l.slice(0,i).trim().toLowerCase()]=l.slice(i+1).trim()});const sv=spawn('node',['server.mjs','../../out/'+s,String(port)],{cwd:'backend/test',stdio:'ignore'});await new Promise(r=>setTimeout(r,1000));
 for(const [w,h] of [[1280,900],[390,844]]){const ctx=await b.newContext({viewport:{width:w,height:h}});await ctx.route('**/*',async r=>{const u=r.request().url();if(!u.includes('.localhost')){return r.abort()}const f=await r.fetch({url:u.replace(/[a-z]+\.localhost/,'127.0.0.1'),headers:{...r.request().headers(),host:new URL(u).host}});r.fulfill({response:f,headers:{...f.headers(),...hdr}})});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(/Content Security Policy|Refused/.test(m.text()))errs.push(m.text().slice(0,160))});
  await p.goto('http://'+s+'.localhost:'+port+'/');await p.waitForTimeout(700);
  const n=await p.evaluate(()=>document.querySelectorAll('.tq').length);
  // interact: first card
  const r={n};
  const first=p.locator('.tq').first();
  if(await first.locator('.tqb').count()){await first.locator('.tqb').nth(1).click()}else{await first.locator('input').fill('1');await first.locator('.tqc').click()}
  await p.waitForTimeout(200);r.fb=await first.locator('.tqf').innerText();
  await p.click('#tryn');await p.waitForTimeout(700);r.c=await p.innerText('#tryc');
  await p.screenshot({path:`shots/land-${s}-${w}.png`});
  const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  console.log(s,w,JSON.stringify(r),'overflow',ov,errs.join('|'));await ctx.close()}
 sv.kill()}
await b.close()})()
