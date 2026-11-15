/* ===== quiz sessions: learn / blitz / test / review ===== */
var Z=null,tmr=null;
function mkItem(id){
 var q=QS[QI[id]],it={id:id,q:q,done:false,ok:null,gain:0};
 if(q.type==='mcq'||q.type==='multi'){it.perm=shuf(q.o.map(function(_,i){return i}));it.sel=[];it.off={}}
 else if(q.type==='short')it.val='';
 else if(q.type==='order'){it.pool=shuf(q.items.map(function(_,i){return i}));it.seq=[]}
 else if(q.type==='match'){it.rperm=shuf(q.pairs.map(function(_,i){return i}));it.mp={};it.pick=null}
 return it;
}
function pick(topics,n,types){
 var pool=QS.filter(function(q){return topics.indexOf(q.t)>-1&&(!types||types.indexOf(q.type)>-1)});
 pool=shuf(pool);
 var fresh=pool.filter(function(q){return !S.seen[q.id]}),rest=pool.filter(function(q){return S.seen[q.id]}).sort(function(a,b){return (S.miss[b.id]?1:0)-(S.miss[a.id]?1:0)||S.seen[a.id]-S.seen[b.id]});
 var out=fresh.concat(rest).slice(0,n);
 return {ids:shuf(out).map(function(q){return q.id}),fresh:Math.min(fresh.length,n)};
}
function start(o){
 if(tmr){clearInterval(tmr);tmr=null}
 var ids=o.ids;
 if(!ids){var p=pick(o.topics,o.n,o.types);ids=p.ids;o.fresh=p.fresh}
 if(!ids.length){toast('No questions for that choice');return}
 combo=0;
 Z={mode:o.mode,items:ids.map(mkItem),i:0,fin:false,right:0,earned:0,cash:0,fresh:o.fresh,label:o.label||''};
 if(o.mode==='test'||o.mode==='blitz'){var secs=o.mode==='blitz'?60:(o.min||35)*60;Z.end=Date.now()+secs*1000;Z.total=secs;tmr=setInterval(tick,250)}
 show('play');drawQ();window.scrollTo(0,0);
}
function tick(){if(!Z){clearInterval(tmr);tmr=null;return}var el=$('tm');var r=Math.max(0,Math.ceil((Z.end-Date.now())/1000));if(el)el.textContent=Math.floor(r/60)+':'+('0'+r%60).slice(-2);if(r<=0)finish()}
function isOk(it){
 var q=it.q;
 if(q.type==='mcq')return it.sel.length===1&&it.sel[0]===0;
 if(q.type==='multi'){return q.a.slice().sort().join()===it.sel.slice().sort().join()}
 if(q.type==='short'){it.res=gradeShort(q,it.val);return it.res.ok}
 if(q.type==='order')return it.seq.length===q.items.length&&it.seq.every(function(v,i){return v===i});
 if(q.type==='match')return q.pairs.every(function(_,i){return it.mp[i]===i});
 return false}
function answered(it){var q=it.q;
 if(q.type==='mcq'||q.type==='multi')return it.sel.length>0;
 if(q.type==='short')return it.val.trim().length>0;
 if(q.type==='order')return it.seq.length===q.items.length;
 if(q.type==='match')return cnt(it.mp)===q.pairs.length;return false}
function resolve(it){
 if(it.done)return;it.ok=isOk(it);it.done=true;
 if(Z.mode==='blitz'){
  var ok=it.ok;S.total++;S.seen[it.id]=(S.seen[it.id]||0)+1;var st=S.stat[it.q.t]||[0,0];st[1]++;
  if(ok){S.right++;if(it.q.type==='short')S.shorts++;st[0]++;delete S.miss[it.id];combo++;if(combo>S.best)S.best=combo;
   var m=1+Math.min(combo-1,9)*0.1,c=Math.round(10*m);it.gain=c;Z.cash+=c;S.coins+=c;var xp=Math.round(c/2);S.xp+=xp;S.dxp[today()]=(S.dxp[today()]||0)+xp;Z.earned+=xp}
  else{S.miss[it.id]=1;combo=0}
  S.stat[it.q.t]=st;S.days[today()]=1;checkBadges();save();hud();
 }else if(Z.mode!=='test'){it.gain=award(it.q,it.ok,0,it.help>0);Z.earned+=it.gain}
 if(it.ok)Z.right++;
}
function pbarHTML(){var z=Z;var n=z.mode==='blitz'?Math.min(100,(z.i/Math.max(1,z.items.length))*100):((z.i)/z.items.length)*100;return '<div class="prog"><i style="width:'+n+'%"></i></div>'}
function chipHTML(it,cls,i,txt,extra){return '<button class="ch '+cls+'" '+extra+'>'+esc(txt)+'</button>'}
function drawQ(){
 var z=Z;if(!z)return;if(z.fin)return drawResults();
 var it=z.items[z.i],q=it.q,test=z.mode==='test',blitz=z.mode==='blitz',h='',rev=it.done&&!test;
 h+='<div class="card qwrap"><div class="qtop"><span>'+(z.i+1)+' / '+z.items.length+'</span>'+pbarHTML()+(test||blitz?'<span class="timer">⏱ <span id="tm">–</span></span>':'')+(combo>1&&!test?'<span class="combo">×'+combo+'</span>':'')+'<span class="tag '+(TOP[q.t].tier==='adjacent'?'adj':'core')+'">'+esc(TOP[q.t].name)+'</span></div>';
 if(q.fig)h+=figSVG(q.fig);if(q.svg)h+='<div class="figw">'+q.svg+'</div>';
 h+='<div class="qtext">'+esc(q.q)+'</div>';
 if(q.type==='multi')h+='<p class="small mute">Select all that apply.</p>';
 if(q.type==='mcq'||q.type==='multi'){
  h+='<div class="opts">';
  it.perm.forEach(function(oi,k){
   var sel=it.sel.indexOf(oi)>-1,cls='opt',good=q.type==='multi'?q.a.indexOf(oi)>-1:oi===0;
   if(rev){if(good)cls+=' ok';else if(sel)cls+=' bad'}else if(sel)cls+=' sel';
   if(it.off[oi]&&!rev)cls+=' off';
   h+='<button class="'+cls+'" data-oi="'+oi+'"'+(rev||it.off[oi]?' disabled':'')+' aria-pressed="'+sel+'"><b>'+'ABCD'[k]+'</b><span>'+esc(q.o[oi])+'</span></button>'});
  h+='</div>';
 }else if(q.type==='short'){
  var hint=q.num?(q.num.u?'Number and unit (default '+q.num.u+')':'Number'):'Short answer';
  h+='<div class="ans"><input id="sv" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="'+esc(hint)+'" value="'+esc(it.val)+'"'+(rev?' disabled class="'+(it.ok?'ok':'bad')+'"':'')+'></div>';
 }else if(q.type==='order'){
  h+='<p class="small mute">Tap in order. Tap a placed item to remove it.</p><div class="seq">';
  it.seq.forEach(function(v,k){h+='<button class="ch '+(rev?(v===k?'ok':'bad'):'')+'" data-sq="'+k+'"'+(rev?' disabled':'')+'>'+esc(q.items[v])+'</button>'});
  h+='</div><div class="chips">';
  it.pool.forEach(function(v){if(it.seq.indexOf(v)<0)h+='<button class="ch" data-po="'+v+'">'+esc(q.items[v])+'</button>'});
  h+='</div>';
 }else if(q.type==='match'){
  h+='<p class="small mute">Tap a term, then its partner.</p><div class="mt"><div class="chips" style="flex-direction:column;margin:0">';
  q.pairs.forEach(function(p,i){var pi=it.mp[i]!==undefined;h+='<button class="ch" data-ml="'+i+'"'+(pi?' data-p="'+i+'"':'')+(it.pick===i?' style="outline:3px solid var(--sel)"':'')+(rev?' disabled':'')+'>'+esc(p[0])+'</button>'});
  h+='</div><div class="chips" style="flex-direction:column;margin:0">';
  it.rperm.forEach(function(ri){var li=-1;for(var k in it.mp)if(it.mp[k]===ri)li=+k;h+='<button class="ch" data-mr="'+ri+'"'+(li>-1?' data-p="'+li+'"':'')+(rev?' disabled':'')+'>'+esc(q.pairs[ri][1])+'</button>'});
  h+='</div></div>';
 }
 if(rev){
  h+='<div class="fb '+(it.ok?'ok':'bad')+'">'+(STUDY?'<span class="fbm">'+mascot(S.cos.on.av,it.ok?'cheer':'oops',44)+'</span>':'')+'<span class="xp">'+(it.ok?(blitz?'+$'+it.gain:'+'+it.gain+' XP'):'')+'</span><b class="h">'+(it.ok?['Correct','Nice','Right on','Exactly'][z.i%4]:(q.type==='short'&&it.res&&it.res.msg?it.res.msg+'. Not quite':'Not quite'))+'</b>';
  if(!it.ok)h+='<div><b>Answer:</b> '+esc(ansText(q))+'</div>';
  if(q.w)h+='<div>'+esc(q.w)+'</div>';
  h+='</div>';if(!it.ok&&!test&&STUDY)h+=learnHTML(q);
 }
 if(it.help&&!rev)h+=helpHTML(it);
 h+='<div class="row" style="margin-top:14px">';
 if(!rev){
  if(!test&&!blitz&&STUDY)h+='<button class="btn alt sm" id="help">Help'+(it.help?' ('+it.help+'/3)':'')+'</button>';
  if(!test&&q.type!=='mcq')h+='<button class="btn" id="chk"'+(answered(it)?'':' disabled')+'>Check</button>';
 }
 if(test){if(z.i>0)h+='<button class="btn alt" id="pv">Back</button>';if(z.i<z.items.length-1)h+='<button class="btn" id="nx">Next</button>'}
 else if(rev&&!blitz){h+='<button class="btn" id="nx">'+(z.i<z.items.length-1?'Next':'Finish')+'</button>'}
 h+='<button class="btn ghost" id="fin">'+(test?'Submit test':'End')+'</button></div>';
 if(test)h+='<div class="dots">'+z.items.map(function(x,k){return '<button data-k="'+k+'" class="'+(k===z.i?'cur ':'')+(answered(x)?'a':'')+'">'+(k+1)+'</button>'}).join('')+'</div>';
 h+='</div>';
 $('v-play').innerHTML=h;
 if(test||blitz)tick();
 var inp=$('sv');if(inp&&!rev){inp.focus();inp.setSelectionRange(inp.value.length,inp.value.length)}
}
function advance(){Z.i++;if(Z.i>=Z.items.length){if(Z.mode==='blitz'){Z.items=Z.items.concat(pick(Object.keys(TOP),20,['mcq','short']).ids.map(mkItem))}else return finish()}drawQ()}
function afterAnswer(){drawQ();if(Z.mode==='blitz'){setTimeout(function(){if(Z&&!Z.fin)advance()},Z.items[Z.i].ok?650:1500)}}
$('v-play').addEventListener('input',function(e){if(e.target.id==='sv'&&Z){var it=Z.items[Z.i];it.val=e.target.value;var b=$('chk');if(b)b.disabled=!it.val.trim()}});
$('v-play').addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.id==='sv'&&Z){var it=Z.items[Z.i];if(Z.mode==='test'){return}if(it.val.trim()&&!it.done){resolve(it);afterAnswer()}else if(it.done&&Z.mode!=='blitz')advance()}});
$('v-play').addEventListener('click',function(e){
 var z=Z;if(!z)return;var t=e.target,it=z.items[z.i],q=it&&it.q,test=z.mode==='test',blitz=z.mode==='blitz';
 var o=t.closest('.opt'),id=t.id||(t.closest('button')||{}).id;
 if(o&&!it.done){var oi=+o.dataset.oi,k=it.sel.indexOf(oi);
  if(q.type==='multi'){if(k>-1)it.sel.splice(k,1);else it.sel.push(oi);drawQ();return}
  it.sel=[oi];if(test){drawQ();return}resolve(it);afterAnswer();return}
 var sq=t.closest('[data-sq]');if(sq&&!it.done){it.seq.splice(+sq.dataset.sq,1);drawQ();return}
 var po=t.closest('[data-po]');if(po&&!it.done){it.seq.push(+po.dataset.po);drawQ();return}
 var ml=t.closest('[data-ml]');if(ml&&!it.done){var li=+ml.dataset.ml;if(it.mp[li]!==undefined)delete it.mp[li];it.pick=li;drawQ();return}
 var mr=t.closest('[data-mr]');if(mr&&!it.done){var ri=+mr.dataset.mr;for(var kk in it.mp)if(it.mp[kk]===ri)delete it.mp[kk];if(it.pick!==null){it.mp[it.pick]=ri;it.pick=null}drawQ();return}
 var dk=t.closest('[data-k]');if(dk&&test){z.i=+dk.dataset.k;drawQ();return}
 if(id==='chk'){if(q.type==='multi'||answered(it)){resolve(it);afterAnswer()}}
 else if(id==='help'){it.help=Math.min(3,(it.help||0)+1);if(it.help===3&&q.type==='mcq'&&!it.off[0]){shuf([1,2,3]).slice(0,2).forEach(function(w){it.off[w]=1})}drawQ()}
 else if(id==='nx'){advance()}
 else if(id==='pv'){z.i--;drawQ()}
 else if(id==='fin'){finish()}
});
function finish(){
 var z=Z;if(!z||z.fin)return;if(tmr){clearInterval(tmr);tmr=null}
 if(z.mode==='test'){z.items.forEach(function(it){if(!it.done){if(answered(it)){it.ok=isOk(it);it.done=true}else{it.done=true;it.ok=false;it.skipped=true}}
   if(!it.skipped)it.gain=award(it.q,it.ok,0,it.help>0);else{S.miss[it.id]=1}if(it.ok){z.right++;z.earned+=it.gain}});save()}
 z.fin=true;
 var n=z.items.filter(function(i){return i.done}).length;
 if(z.mode!=='blitz'&&n>=10&&z.right===n){S.perfect++;checkBadges()}
 save();drawResults();
}
function drawResults(){
 var z=Z,by={},h='',ans=z.items.filter(function(i){return i.done&&!i.skipped});
 ans.forEach(function(it){var t=it.q.t;by[t]=by[t]||[0,0];by[t][1]++;if(it.ok)by[t][0]++});
 var right=ans.filter(function(i){return i.ok}).length,tot=z.mode==='test'?z.items.length:ans.length,pct=tot?Math.round(100*right/tot):0;
 h+='<div class="card"><div class="row" style="justify-content:space-between"><div><div class="score">'+right+' / '+tot+'</div><div class="mute">'+pct+'%'+(z.mode==='blitz'?' · $'+z.cash+' earned':'')+' · +'+z.earned+' XP</div></div><div class="row"><button class="btn" id="again">Play again</button><button class="btn alt" id="home">Home</button></div></div>';
 h+='<h3 style="margin-top:16px">By topic</h3><div class="bars">';
 Object.keys(by).forEach(function(t){var p=by[t];h+='<div class="bar2"><span>'+esc(TOP[t].name)+'</span><span class="tr"><i style="width:'+(100*p[0]/p[1])+'%"></i></span><span>'+p[0]+'/'+p[1]+'</span></div>'});
 h+='</div></div>';
 var miss=z.items.filter(function(i){return i.done&&!i.ok});
 if(miss.length){h+='<div class="card"><h3>Review ('+miss.length+')</h3>';miss.forEach(function(it){h+='<details style="margin:8px 0"><summary>'+esc(it.q.q)+'</summary><div style="padding:6px 0">'+(it.q.fig?figSVG(it.q.fig):'')+'<div><b>Answer:</b> '+esc(ansText(it.q))+'</div>'+(it.q.w?'<div class="mute">'+esc(it.q.w)+'</div>':'')+'</div></details>'});
  h+='<button class="btn" id="retry" style="margin-top:8px">Retry these</button></div>'}
 $('v-play').innerHTML=h;
 $('again').onclick=function(){Z=null;drawPlay()};
 $('home').onclick=function(){Z=null;show('home')};
 if($('retry'))$('retry').onclick=function(){start({mode:'learn',ids:miss.map(function(i){return i.id}),label:'retry'})};
 window.scrollTo(0,0);
}
