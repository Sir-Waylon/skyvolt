globalThis.__mail=[];globalThis.fetch=async(u,o)=>{u=String(u);if(u.includes("mailtrap")){__mail.push(JSON.parse(o.body));return new Response("{\"success\":true}")}if(u.includes("siteverify")){const tk=new URLSearchParams(o.body.toString()).get("response");return new Response(JSON.stringify({success:tk==="good",hostname:"x.test"}))}if(u.includes("pwnedpasswords")){return new Response("0000000000000000000000000000000000A:0\n")}throw new Error("offline")};
import {DatabaseSync} from 'node:sqlite';import fs from 'node:fs';import {onRequest} from './route.mjs';
const db=new DatabaseSync(':memory:');db.exec(fs.readFileSync('../schema.sql','utf8'));
const stmt=(sql)=>{let a=[];const o={bind(...x){a=x;return o},async first(){return db.prepare(sql).get(...a)||null},async all(){return {results:db.prepare(sql).all(...a)}},async run(){const r=db.prepare(sql).run(...a);return {meta:{last_row_id:Number(r.lastInsertRowid)}}}};return o};
const env={DB:{prepare:stmt},PEPPER:"testpepper",MAILTRAP_API_TOKEN:"tok",MAIL_FROM:"Voltaxis <hello@x.test>",TURNSTILE_SECRET:"sec",TURNSTILE_SITE_KEY:"site"};const O='https://x.test';
class U{constructor(){this.c={}}
 async call(m,p,b,opt={}){const h={'content-type':'application/json',origin:O,'cf-connecting-ip':opt.ip||'1.1.1.1'};const ck=Object.entries(this.c).map(([k,v])=>k+'='+v).join('; ');if(ck)h.cookie=ck;if(this.c['__Host-csrf']&&!opt.nocsrf)h['x-csrf']=this.c['__Host-csrf'];
  const r=await onRequest({request:new Request(O+'/api'+p,{method:m,headers:h,body:m==='POST'?JSON.stringify(b||{}):undefined}),env});
  for(const c of r.headers.getSetCookie()){const [kv,...rest]=c.split(';'),[k,v]=kv.split('=');if(/Max-Age=0/.test(c))delete this.c[k];else this.c[k]=v;if(k==='__Host-sid'&&!(/HttpOnly/.test(c)&&/Secure/.test(c)&&/SameSite=Strict/.test(c)))throw new Error('cookie flags')}
  return [r.status,await r.json()]}}
let fail2=0;const T=(n,c)=>{console.log(c?'ok  ':'FAIL',n);if(!c)fail2++};
const lastCode=()=>{const m=__mail[__mail.length-1];return m&&/(\d{6})/.exec(m.text)[1]};
const P='correct horse 42 battery';
const u=new U();let s,j;
[s,j]=await u.call('GET','/config');T('config exposes turnstile + verify',j.turnstile==='site'&&j.verify===true&&j.tfa===true);
for(const [pw,why] of [['short1',' short'],['abcdefghijkl','no number'],['aaaaaa123456','repeat/low variety'],['qwerty123456x','keyboard run'],['myvoltaxis2026a','site word'],['password12345','password word']])[s,j]=await u.call('POST','/signup',{email:'k@x.com',username:'kid_1',password:pw,cf:'good'},{ip:'7.7.'+Math.random()}),T('weak pw rejected: '+why,s===400);
[s,j]=await u.call('POST','/signup',{email:'k@x.com',username:'kid_1',password:P},{ip:'7.8.8.8'});T('signup needs captcha',s===400&&/security check/.test(j.error));
[s,j]=await u.call('POST','/signup',{email:'k@x.com',username:'kid_1',password:P,cf:'bad'},{ip:'7.8.8.9'});T('bad captcha rejected',s===400);
[s,j]=await u.call('POST','/signup',{email:'k@x.com',username:'kid_1',password:P,cf:'good'});T('signup ok, unverified',s===200&&j.verified===false);
T('verification code emailed via Mailtrap',__mail.length===1&&__mail[0].to[0].email==='k@x.com'&&__mail[0].from.email==='hello@x.test'&&/^\d{6}$/.test(lastCode()));
[s,j]=await u.call('POST','/sync',{pack:'p-1',state:{xp:10}});T('unverified blocked from sync',s===403&&j.verify===true);
[s,j]=await u.call('GET','/me');T('me works while unverified',s===200&&j.verified===false);
[s,j]=await u.call('POST','/verify',{code:'000000'});T('wrong code rejected',s===400);
[s,j]=await u.call('POST','/verify/resend');T('resend cooldown',s===429);
const good=lastCode();
[s,j]=await u.call('POST','/verify',{code:good});T('right code verifies',s===200);
[s,j]=await u.call('GET','/me');T('now verified',j.verified===true&&j.canTfa===true&&j.tfa===false);
[s,j]=await u.call('POST','/sync',{pack:'p-1',state:{xp:10}});T('sync allowed after verify',s===200);
[s,j]=await u.call('POST','/verify',{code:good});T('code single use (already verified ok)',s===200);
// 2FA enable
[s,j]=await u.call('POST','/2fa/start');T('2fa start sends code',s===200&&__mail.length===2);
[s,j]=await u.call('POST','/2fa/confirm',{code:'123456'});T('2fa wrong code',s===400);
[s,j]=await u.call('POST','/2fa/confirm',{code:lastCode()});T('2fa enabled',s===200);
// login with 2fa
const v=new U();
[s,j]=await v.call('POST','/login',{id:'kid_1',password:P});T('login needs captcha',s===400);
[s,j]=await v.call('POST','/login',{id:'kid_1',password:P,cf:'good'});T('login asks for emailed code',s===200&&j.need2fa===true&&/^[a-f0-9]{32}$/.test(j.ch)&&!v.c['__Host-sid']);
const ch=j.ch,c1=lastCode();
[s,j]=await v.call('POST','/login/2fa',{ch,code:'111111'});T('2fa wrong code',s===401);
[s,j]=await v.call('POST','/login/2fa',{ch:'0'.repeat(32),code:c1});T('2fa wrong challenge',s===401);
[s,j]=await v.call('POST','/login/2fa',{ch,code:c1});T('2fa success signs in',s===200&&j.username==='kid_1'&&v.c['__Host-sid']);
[s,j]=await v.call('POST','/login/2fa',{ch,code:c1});T('2fa code is single use',s===401);
// brute force: 5 tries kills the code
const w=new U();[s,j]=await w.call('POST','/login',{id:'kid_1',password:P,cf:'good'});const ch2=j.ch,c2=lastCode();
for(let i=0;i<5;i++)await w.call('POST','/login/2fa',{ch:ch2,code:'99999'+i});
[s,j]=await w.call('POST','/login/2fa',{ch:ch2,code:c2});T('5 wrong tries lock the code',s===401);
// disable
[s,j]=await v.call('POST','/2fa/off',{password:'wrong wrong 1234'});T('2fa off needs password',s===401);
[s,j]=await v.call('POST','/2fa/off',{password:P});T('2fa off',s===200);
const x=new U();[s,j]=await x.call('POST','/login',{id:'kid_1',password:P,cf:'good'});T('login without 2fa is direct',s===200&&j.username==='kid_1');
// csp report endpoint
{const r=await onRequest({request:new Request(O+'/api/csp-report',{method:'POST',headers:{'content-type':'application/csp-report'},body:'{"csp-report":{"blocked-uri":"inline"}}'}),env});T('csp report accepted (204)',r.status===204)}
// no mail configured -> accounts are auto verified (feature fails open, not locked)
{const e2={DB:env.DB,PEPPER:'testpepper'};const r=await onRequest({request:new Request(O+'/api/signup',{method:'POST',headers:{'content-type':'application/json',origin:O,'cf-connecting-ip':'5.5.5.5'},body:JSON.stringify({email:'z@x.com',username:'zed_9',password:P})}),env:e2});const jj=await r.json();T('without mail config signup is verified',r.status===200&&jj.verified===true)}
console.log(fail2?'FAILURES: '+fail2:'ALL NEW TESTS PASS');
