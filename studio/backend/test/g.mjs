import {DatabaseSync} from 'node:sqlite';import fs from 'node:fs';import {onRequest} from './route.mjs';
const db=new DatabaseSync(':memory:');db.exec(fs.readFileSync('../schema.sql','utf8'));
const stmt=(sql)=>{let a=[];const o={bind(...x){a=x;return o},async first(){return db.prepare(sql).get(...a)||null},async all(){return {results:db.prepare(sql).all(...a)}},async run(){const r=db.prepare(sql).run(...a);return {meta:{last_row_id:Number(r.lastInsertRowid)}}}};return o};
const env={DB:{prepare:stmt},PEPPER:'p',GOOGLE_CLIENT_ID:'cid.apps.googleusercontent.com'};
const kp=await crypto.subtle.generateKey({name:'RSASSA-PKCS1-v1_5',modulusLength:2048,publicExponent:new Uint8Array([1,0,1]),hash:'SHA-256'},true,['sign','verify']);
const jwk={...await crypto.subtle.exportKey('jwk',kp.publicKey),kid:'k1',alg:'RS256',use:'sig'};
globalThis.fetch=async()=>new Response(JSON.stringify({keys:[jwk]}));
const u=(o)=>Buffer.from(JSON.stringify(o)).toString('base64url');
async function tok(pl,kid='k1'){const h=u({alg:'RS256',kid}),p=u(pl),s=Buffer.from(await crypto.subtle.sign('RSASSA-PKCS1-v1_5',kp.privateKey,new TextEncoder().encode(h+'.'+p))).toString('base64url');return h+'.'+p+'.'+s}
const call=async(c)=>{const r=await onRequest({request:new Request('https://x.test/api/google',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({credential:c})}),env});return [r.status,await r.json()]};
const now=Math.floor(Date.now()/1000),good={iss:'https://accounts.google.com',aud:env.GOOGLE_CLIENT_ID,exp:now+600,sub:'123',email:'kid@gmail.com',email_verified:true};
let r=await call(await tok(good));console.log('valid',r[0],r[1].needUsername);
console.log('wrong aud',(await call(await tok({...good,aud:'other'})))[0]);
console.log('expired',(await call(await tok({...good,exp:now-5})))[0]);
console.log('unverified email',(await call(await tok({...good,email_verified:false})))[0]);
console.log('bad sig',(await call((await tok(good)).slice(0,-6)+'AAAAAA'))[0]);
console.log('unknown kid',(await call(await tok(good,'zz')))[0]);
