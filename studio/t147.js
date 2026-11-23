const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [s,port,paths] of [['skyvolt',8871,['/app/','/app/circuit/','/app/meteorology/']],['axiom',8872,['/app/','/app/apex/','/app/quanta/']]]){
 const sv=spawn('node',['server.mjs','../../out/'+s,String(port)],{cwd:'backend/test',stdio:'ignore'});await new Promise(r=>setTimeout(r,900));
 const ctx=await b.newContext({viewport:{width:1100,height:800}});
 await ctx.route('**/*',async r=>{const u=r.request().url();if(!u.includes('.localhost'))return r.abort();const f=await r.fetch({url:u.replace(/[a-z]+\.localhost/,'127.0.0.1'),headers:{...r.request().headers(),host:new URL(u).host}});r.fulfill({response:f})});
 for(const pa of paths){const p=await ctx.newPage();await p.goto('http://'+s+'.localhost:'+port+pa);await p.waitForTimeout(1200);
  const icons=await p.evaluate(()=>[...document.querySelectorAll('link[rel*=icon],link[rel=manifest]')].map(l=>l.rel+':'+l.getAttribute('href')));
  console.log(s,pa,p.url().slice(-30),JSON.stringify(icons),await p.title());
  await p.screenshot({path:`shots/tp-${s}-${pa.replace(/\W/g,'_')}.png`});await p.close()}
 sv.kill()}
await b.close()})()
