const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const root=process.argv[2];const mt={'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml'};
const srv=http.createServer((q,r)=>{let p=q.url.split('?')[0];if(p.endsWith('/'))p+='index.html';const f=path.join(root,p);if(!fs.existsSync(f)){r.writeHead(404);return r.end()}r.writeHead(200,{'content-type':mt[path.extname(f)]||'text/plain'});r.end(fs.readFileSync(f))}).listen(0,async()=>{
const b=await chromium.launch();const pg=await b.newPage({viewport:{width:400,height:760}});const o=`http://localhost:${srv.address().port}`;
await pg.goto(o+'/');await pg.waitForTimeout(500);await pg.screenshot({path:'ck/s_hub.png'});
await pg.goto(o+'/meteorology/');await pg.waitForTimeout(700);await pg.screenshot({path:'ck/s_met.png'});
await pg.evaluate(()=>{const q=QS.find(q=>q.svg&&q.type==='short');startFromIds([q.id])});await pg.waitForTimeout(400);await pg.screenshot({path:'ck/s_metq.png'});
await pg.goto(o+'/circuit/');await pg.waitForTimeout(700);await pg.evaluate(()=>{for(const u of UN)for(const L of u.lessons)for(const c of L.cards)if(c.lab==='ohm'){startLesson(u.id,L.id);Z.i=Z.steps.findIndex(s=>s.k==='card'&&s.c.lab==='ohm');drawSess();return}});await pg.waitForTimeout(500);await pg.screenshot({path:'ck/s_ohm.png'});
await b.close();srv.close()});
