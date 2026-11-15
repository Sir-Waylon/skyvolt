import http from 'node:http';import fs from 'node:fs';import path from 'node:path';import {DatabaseSync} from 'node:sqlite';import {onRequest} from './route.mjs';
const db=new DatabaseSync(':memory:');db.exec(fs.readFileSync('../schema.sql','utf8'));
const stmt=(sql)=>{let a=[];const o={bind(...x){a=x;return o},async first(){return db.prepare(sql).get(...a)||null},async all(){return {results:db.prepare(sql).all(...a)}},async run(){const r=db.prepare(sql).run(...a);return {meta:{last_row_id:Number(r.lastInsertRowid)}}}};return o};
const env={DB:{prepare:stmt},PEPPER:'x'};const root=process.argv[2],port=+process.argv[3]||8791;
const MT={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.webmanifest':'application/json'};
http.createServer(async(q,s)=>{try{const u=new URL(q.url,'http://localhost:'+port);
 if(u.pathname.startsWith('/api/')){const chunks=[];for await(const c of q)chunks.push(c);const r=await onRequest({request:new Request(u,{method:q.method,headers:q.headers,body:q.method==='POST'?Buffer.concat(chunks):undefined}),env});const h={};r.headers.forEach((v,k)=>{h[k]=v});const sc=r.headers.getSetCookie();if(sc.length)h['set-cookie']=sc;s.writeHead(r.status,h);s.end(Buffer.from(await r.arrayBuffer()));return}
 let p=path.join(root,u.pathname);if(fs.existsSync(p)&&fs.statSync(p).isDirectory())p=path.join(p,'index.html');if(!fs.existsSync(p)){s.writeHead(404);s.end();return}
 s.writeHead(200,{'content-type':MT[path.extname(p)]||'application/octet-stream'});s.end(fs.readFileSync(p))}catch(e){s.writeHead(500);s.end(String(e))}}).listen(port);
