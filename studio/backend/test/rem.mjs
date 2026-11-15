import fs from 'node:fs';import {DatabaseSync} from 'node:sqlite';import {runReminders,onRequest} from './route.mjs';
const db=new DatabaseSync(':memory:');db.exec(fs.readFileSync('../schema.sql','utf8'));
const stmt=(sql)=>{let a=[];const o={bind(...x){a=x;return o},async first(){return db.prepare(sql).get(...a)||null},async all(){return {results:db.prepare(sql).all(...a)}},async run(){const r=db.prepare(sql).run(...a);return {meta:{last_row_id:Number(r.lastInsertRowid),changes:Number(r.changes)}}}};return o};
const sent=[];const env={DB:{prepare:stmt},PEPPER:'x',EMAIL:{send:async m=>{sent.push(m)}},MAIL_FROM:'a@b.co',SITE_URL:'https://x.dev',BRAND:'Voltaic'};
const cols=db.prepare("pragma table_info(users)").all().map(c=>c.name);console.log(cols.join());
const hrNow=tz=>+new Intl.DateTimeFormat('en-US',{timeZone:tz,hour:'2-digit',hourCycle:'h23'}).format(new Date());
const tz='America/Los_Angeles',h=hrNow(tz);
const ins=(id,pub)=>db.prepare("insert into users(id,email,username,created,pub) values(?,?,?,?,?)").run(id,'u'+id+'@x.com','u'+id,1,pub);
ins(1,'{"st":5}');ins(2,'{"st":0}');ins(3,'{"st":4}');ins(4,'{"st":7}');
const nt=(u,hr,on,t)=>db.prepare("insert into notify(uid,on_,hr,tz,tok) values(?,?,?,?,?)").run(u,on,hr,tz,t.padEnd(32,'a'));
nt(1,h,1,'1');nt(2,h,1,'2');nt(3,(h+5)%24,1,'3');nt(4,h,0,'4');
db.prepare("insert into saves values(5,'p','{}',1,?)").run(Date.now()); // unrelated
let r=await runReminders(env);console.log('first',r,sent.map(m=>m.to));
r=await runReminders(env);console.log('second (no dup)',r);
// studied today skip
db.prepare("update notify set sent=null").run();db.prepare("insert into saves values(1,'q','{}',1,?)").run(Date.now());
r=await runReminders(env);console.log('studied-today skip',r);
console.log(sent[0].subject,sent[0].headers['List-Unsubscribe'].slice(0,40));
// unsub
const t='1'.padEnd(32,'a');const u=await onRequest({request:new Request('https://x.dev/api/unsub?t='+t),env});console.log('unsub',u.status,db.prepare('select on_ from notify where uid=1').get().on_);
const bad=await onRequest({request:new Request('https://x.dev/api/unsub?t=zzz'),env});console.log('bad',bad.status);
r=await runReminders({...env,EMAIL:undefined});console.log('unconfigured',r);
