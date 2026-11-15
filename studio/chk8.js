const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const root=process.argv[2],slug=process.argv[3]||'circuit';
const csp=fs.readFileSync(root+'/_headers','utf8').match(/Content-Security-Policy: (.*)/)[1];
const mt={'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.webmanifest':'application/manifest+json'};
const srv=http.createServer((q,r)=>{let p=q.url.split('?')[0];if(p.endsWith('/'))p+='index.html';const f=path.join(root,p);if(!fs.existsSync(f)){r.writeHead(404);return r.end()}r.writeHead(200,{'content-type':mt[path.extname(f)]||'text/plain','content-security-policy':csp});r.end(fs.readFileSync(f))}).listen(0,async()=>{
const port=srv.address().port;const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:800}});const pg=await ctx.newPage();
const errs=[];pg.on('console',m=>{if(['error','warning'].includes(m.type())&&!/fonts|ERR_|proxy/i.test(m.text()))errs.push(m.text().slice(0,200))});pg.on('pageerror',e=>errs.push('PE '+e.message));
await pg.goto(`http://localhost:${port}/${slug==="."?"":slug+"/"}`);await pg.waitForTimeout(1200);
console.log('title',await pg.title(),'tabs',await pg.locator('nav button, nav a').count());
// start first lesson node
await pg.screenshot({path:'ck/o1.png'});
const n=await pg.evaluate(()=>({sw:!!navigator.serviceWorker.controller,len:document.body.innerText.length}));
await pg.waitForTimeout(1500);const reg=await pg.evaluate(()=>navigator.serviceWorker.getRegistrations().then(r=>r.length));
console.log(n,'swregs',reg);
await pg.evaluate(()=>{S.total=10;S.xp=123;save()});await pg.reload();await pg.waitForTimeout(800);
console.log('xp after reload',await pg.evaluate(()=>S.xp));
await pg.evaluate(()=>{var k='scioly:'+P.meta.id;var o=JSON.parse(localStorage.getItem(k));o.d=o.d.replace('"xp":123','"xp":99999');window.save=function(){};localStorage.setItem(k,JSON.stringify(o))});await pg.close();const p2=await ctx.newPage();await p2.goto(`http://localhost:${port}/${slug==="."?"":slug+"/"}`);await p2.waitForTimeout(800);
console.log('xp after tamper',await p2.evaluate(()=>S.xp));
console.log('errors',errs.length,errs.slice(0,5));await b.close();srv.close()});
