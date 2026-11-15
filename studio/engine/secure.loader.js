/* secure loader: passcode -> AES-GCM unlock -> engine runs inside a closure (no globals) */
(function(){
var E=__ENC__,te=new TextEncoder(),td=new TextDecoder(),sub=crypto.subtle;
function u8(b){var s=atob(b),a=new Uint8Array(s.length);for(var i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a}
function b64(a){a=new Uint8Array(a);var s='';for(var i=0;i<a.length;i++)s+=String.fromCharCode(a[i]);return btoa(s)}
function b64u(a){return b64(a).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
function unb64u(s){s=s.replace(/-/g,'+').replace(/_/g,'/');while(s.length%4)s+='=';return u8(s)}
var $=function(i){return document.getElementById(i)};
function idb(){return new Promise(function(res,rej){var r=indexedDB.open('scioly-keys',1);r.onupgradeneeded=function(){r.result.createObjectStore('k')};r.onsuccess=function(){res(r.result)};r.onerror=rej})}
function idbGet(k){return idb().then(function(d){return new Promise(function(res){var q=d.transaction('k').objectStore('k').get(k);q.onsuccess=function(){res(q.result)};q.onerror=function(){res(null)}})}).catch(function(){return null})}
function idbSet(k,v){return idb().then(function(d){d.transaction('k','readwrite').objectStore('k').put(v,k)}).catch(function(){})}
function idbDel(k){return idb().then(function(d){d.transaction('k','readwrite').objectStore('k').delete(k)}).catch(function(){})}
function keyFromPass(p){return sub.importKey('raw',te.encode(p.trim().toLowerCase()),'PBKDF2',false,['deriveKey']).then(function(m){return sub.deriveKey({name:'PBKDF2',salt:u8(E.s),iterations:E.i,hash:'SHA-256'},m,{name:'AES-GCM',length:256},false,['decrypt'])})}
function gunzip(buf){var ds=new DecompressionStream('gzip');var w=ds.writable.getWriter();w.write(buf);w.close();return new Response(ds.readable).arrayBuffer()}
function open(key){return sub.decrypt({name:'AES-GCM',iv:u8(E.n)},key,u8(E.c)).then(gunzip).then(function(b){return JSON.parse(td.decode(b))})}
function hkdf(sec,info,usage,alg){return sub.importKey('raw',u8(sec),'HKDF',false,['deriveKey']).then(function(m){return sub.deriveKey({name:'HKDF',hash:'SHA-256',salt:te.encode('scioly/1'),info:te.encode(info)},m,alg,false,usage)})}
function devSalt(){var k='scioly:dev:'+E.id,v=null;try{v=localStorage.getItem(k);if(!v){v=b64(crypto.getRandomValues(new Uint8Array(16)));localStorage.setItem(k,v)}}catch(e){v=b64(new Uint8Array(16))}return v}
function buildSEC(P){
 var sec=P._sec,SK='scioly:st:'+P.meta.id,q=Promise.resolve(),pend=null;
 var stK=hkdf(sec,'state/'+devSalt(),['encrypt','decrypt'],{name:'AES-GCM',length:256});
 var mac=hkdf(sec,'mac',['sign','verify'],{name:'HMAC',hash:'SHA-256',length:256});
 function enc(s){return stK.then(function(k){var iv=crypto.getRandomValues(new Uint8Array(12));return sub.encrypt({name:'AES-GCM',iv:iv},k,te.encode(s)).then(function(c){return 'E1.'+b64u(iv)+'.'+b64u(c)})})}
 function dec(t){var p=t.split('.');if(p[0]!=='E1')return Promise.reject();return stK.then(function(k){return sub.decrypt({name:'AES-GCM',iv:unb64u(p[1])},k,unb64u(p[2]))}).then(function(b){return td.decode(b)})}
 function sign(pre,s){return mac.then(function(k){return sub.sign('HMAC',k,te.encode(pre+'.'+s))}).then(function(sg){return pre+'.'+s+'.'+b64u(sg).slice(0,32)})}
 function verify(pre,t){var i=t.lastIndexOf('.'),body=t.slice(0,i),tag=t.slice(i+1);if(body.indexOf(pre+'.')!==0)return Promise.reject();var s=body.slice(pre.length+1);return sign(pre,s).then(function(x){if(x!==body+'.'+tag)throw 0;return s})}
 function j(o){return b64u(te.encode(JSON.stringify(o)))}function uj(s){return JSON.parse(td.decode(unb64u(s)))}
 var api={state:null,
  save:function(s){pend=s;q=q.then(function(){var x=pend;if(x==null)return;pend=null;return enc(x).then(function(t){try{localStorage.setItem(SK,t)}catch(e){}})}).catch(function(){})},
  clear:function(){try{localStorage.removeItem(SK)}catch(e){}pend=null},
  pack:function(S){return sign('SCP1',j(S))},unpack:function(t){return verify('SCP1',t).then(uj)},
  share:function(o){return sign('SCI1',j(o))},open:function(t){return verify('SCI1',t.trim()).then(uj)},
  forget:function(){return idbDel(E.id)}};
 var raw=null;try{raw=localStorage.getItem(SK)}catch(e){}
 return (raw?dec(raw).then(JSON.parse).catch(function(){return null}):Promise.resolve(null)).then(function(s){api.state=s;return api})}
function boot(P){return buildSEC(P).then(function(api){document.body.classList.add('ok');var L=$('lock');if(L)L.remove();(function(P0,__SEC){__ENGINE__})(P,api)})}
var fails=0;
function ui(){$('lock').hidden=false;var f=$('lf'),pi=$('lp'),er=$('le'),bt=$('lb');
 f.onsubmit=function(e){e.preventDefault();if(bt.disabled)return;bt.disabled=true;er.textContent='Unlocking...';
  keyFromPass(pi.value).then(function(k){return open(k).then(function(P){if($('lr').checked)idbSet(E.id,k);return P})}).then(boot).catch(function(){fails++;er.textContent='Wrong passcode. Ask your coach.';var w=Math.min(30,Math.pow(2,fails))*500;setTimeout(function(){bt.disabled=false},w)})};
 pi.focus()}
idbGet(E.id).then(function(k){if(k)return open(k).then(boot).catch(function(){idbDel(E.id);ui()});ui()}).catch(ui);
})();
