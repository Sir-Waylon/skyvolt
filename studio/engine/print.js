/* ===== print documents (black and white, US Letter) — reads PACK ===== */
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function rng(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;var t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
var QS=P.questions,TOP={};P.topics.forEach(function(t){TOP[t.id]=t});
function hdr(sub){return '<div class="hdr"><div><h1>'+esc(P.meta.title)+' '+esc(P.meta.division)+'</h1><div class="sub">'+esc(P.meta.org)+' · '+P.meta.year+'</div></div><div class="sub">'+esc(sub)+'</div></div>'}
function shufS(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
/* test generation */
var TEST={};
function mkTest(set){
 if(TEST[set])return TEST[set];
 var r=rng(set==='A'?11:set==='B'?29:47),used={};
 Object.keys(TEST).forEach(function(k){TEST[k].forEach(function(x){used[x.q.id]=1})});
 var core=QS.filter(function(q){return TOP[q.t].tier==='core'&&!used[q.id]});
 var quota=[['mcq',22],['multi',2],['short',12],['order',2],['match',2]],out=[],tc={};
 quota.forEach(function(qt){
  var cand=shufS(core.filter(function(q){return q.type===qt[0]}),r);
  for(var k=0;k<qt[1]&&cand.length;k++){
   cand.sort(function(a,b){return (tc[a.t]||0)-(tc[b.t]||0)});
   var q=cand.shift();tc[q.t]=(tc[q.t]||0)+1;
   var it={q:q};
   if(q.type==='mcq'||q.type==='multi')it.perm=shufS(q.o.map(function(_,i){return i}),r);
   if(q.type==='order')it.perm=shufS(q.items.map(function(_,i){return i}),r);
   if(q.type==='match')it.perm=shufS(q.pairs.map(function(_,i){return i}),r);
   out.push(it)}});
 TEST[set]=out;return out;
}
var PTS={mcq:1,multi:2,short:2,order:2,match:2};
function qNo(){var n=0;return function(){return ++n}}
function renderQ(it,n,star){
 var q=it.q,h='<div class="q"><div class="ab"></div><div><span class="n">'+n+'.</span> '+(star?'★ ':'')+'<span class="pt">'+PTS[q.type]+' pt</span>'+esc(q.q);
 if(q.num&&q.num.u)h+=' <i>(answer in '+esc(q.num.u)+')</i>';
 if(q.type==='multi')h+=' <i>(write all letters)</i>';
 if(q.fig)h+=figSVG(q.fig);if(q.svg)h+='<div class="figw">'+q.svg+'</div>';
 if(q.type==='mcq'||q.type==='multi'){var one=it.perm.some(function(i){return q.o[i].length>34});h+='<div class="opts'+(one?' one':'')+'">'+it.perm.map(function(oi,k){return '<div>'+'ABCD'[k]+'. '+esc(q.o[oi])+'</div>'}).join('')+'</div>'}
 else if(q.type==='short'){h+=q.num?'<div class="line"></div><div class="line"></div>':'<div class="line"></div>'}
 else if(q.type==='order'){h+='<div class="opts one">'+it.perm.map(function(oi,k){return '<div>'+'ABCD'[k]+'. '+esc(q.items[oi])+'</div>'}).join('')+'</div><p>Order (first to last): '+it.perm.map(function(){return '<span class="box"></span>'}).join('')+'</p>'}
 else if(q.type==='match'){h+='<div class="opts">'+'<div>'+q.pairs.map(function(p,i){return '<div>'+(i+1)+'. '+esc(p[0])+' &nbsp; <span class="box"></span></div>'}).join('')+'</div><div>'+it.perm.map(function(pi,k){return '<div>'+'ABCDE'[k]+'. '+esc(q.pairs[pi][1])+'</div>'}).join('')+'</div></div>'}
 return h+'</div></div>';
}
function docTest(set){
 var T=mkTest(set),n=qNo(),h=hdr('Practice test '+set+' · 40 questions · 50 minutes · Class III calculator, binder allowed');
 h+='<div class="meta"><span>Team</span><span>Names</span><span>Score ___ / '+T.reduce(function(a,x){return a+PTS[x.q.type]},0)+'</span></div>';
 var secs=[['Part I — Multiple choice',function(x){return x.q.type==='mcq'||x.q.type==='multi'}],['Part II — Short answer and calculations. Metric units, sensible significant figures.',function(x){return x.q.type==='short'}],['Part III — Ordering and matching',function(x){return x.q.type==='order'||x.q.type==='match'}]];
 var shorts=T.filter(function(x){return x.q.type==='short'}).length,si=0;
 secs.forEach(function(s){h+='<h2>'+s[0]+'</h2>';T.filter(s[1]).forEach(function(it){var star=it.q.type==='short'&&si++>=shorts-3;h+=renderQ(it,n(),star)})});
 return h+'<p class="foot">★ = tiebreaker questions, in this order.</p>';
}
function docKey(set){
 var T=mkTest(set),n=qNo(),h=hdr('Answer key · Test '+set),rows='';
 var order=[];['mcq,multi','short','order,match'].forEach(function(g){T.forEach(function(it){if(g.split(',').indexOf(it.q.type)>-1)order.push(it)})});
 h+='<div class="key two">';
 order.forEach(function(it){var q=it.q,a='';
  if(q.type==='mcq'){var k=it.perm.indexOf(0);a='ABCD'[k]+'. '+q.o[0]}
  else if(q.type==='multi'){a=q.a.map(function(i){return 'ABCD'[it.perm.indexOf(i)]}).sort().join(', ')+' ('+q.a.map(function(i){return q.o[i]}).join('; ')+')'}
  else if(q.type==='short')a=q.num?numAns(q.num):q.text[0]+(q.text.length>1?' (also: '+q.text.slice(1,3).join(', ')+')':'');
  else if(q.type==='order')a=q.items.map(function(x,i){return 'ABCD'[it.perm.indexOf(i)]}).join(' → ')+'  ('+q.items.join(' → ')+')';
  else if(q.type==='match')a=q.pairs.map(function(p,i){return (i+1)+'–'+'ABCDE'[it.perm.indexOf(i)]}).join(', ');
  h+='<div class="q"><div class="n">'+n()+'.</div><div><span class="a">'+esc(a)+'</span><br><small>'+esc(q.w||'')+'</small></div></div>'});
 return h+'</div>';
}
function fmtN(x){var s=Number(x.toPrecision(3));return String(s)}
var PRE={'n':1e-9,'µ':1e-6,'m':1e-3,'k':1e3,'M':1e6};
function uf(u){if(u==='Wh')return 3600;if(u==='kWh')return 3.6e6;if(u==='h')return 3600;if(u==='%'||u==='N/C')return 1;if(u.length>1&&PRE[u[0]]&&u!=='min'&&u!=='Hz')return PRE[u[0]];return 1}
function numAns(n){return fmtN(n.v/(n.u?uf(n.u):1))+(n.u?' '+n.u:'')}
function docNotes(ids,sub){
 var h=hdr(sub);h+='<div class="two">';
 P.notes.filter(function(n){return !ids||ids.indexOf(n.id)>-1}).forEach(function(n){h+='<h2>'+esc(n.title)+'</h2>'+n.html});
 return h+'</div>';
}
function docPlan(){
 var h=hdr('7-day plan, stations and checklist');
 h+='<p>'+P.meta.facts.map(function(f){return '<b>'+esc(f[0])+'</b> '+esc(f[1])}).join(' · ')+'</p>';
 var sc=P.meta.scope;
 if(sc){h+='<h2>Scope</h2><div class="two"><h3>Core areas</h3><ul>'+sc.core.map(function(a){return '<li><b>'+a[0]+'.</b> '+esc(a[1])+'</li>'}).join('')+'</ul><h3>Adjacent (other years or states)</h3><p>'+sc.adjacent.map(esc).join('; ')+'.</p><h3>Not tested</h3><p>'+sc.skip.map(esc).join('; ')+'.</p><h3>Hands-on stations</h3><ul>'+sc.stations.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul></div>'}
 h+='<h2>Week plan</h2>';
 P.plan.forEach(function(d,i){h+='<div class="day"><h3>Day '+(i+1)+' — '+esc(d.t)+' <small>('+esc(d.focus)+')</small></h3>'+d.tasks.map(function(t){return '<div class="task"><span class="tk"></span><small>'+t[0]+'</small>'+esc(t[1])+'</div>'}).join('')+'<div class="task"><span class="tk"></span><small>drill</small>'+d.drill.n+' practice questions · score ____ / '+d.drill.n+'</div></div>'});
 h+='<h2>Hands-on stations</h2>';P.bench.forEach(function(b){h+='<div class="card"><b>'+esc(b[0])+'.</b> '+b[1]+'</div>'});
 if(P.safety)h+='<h2>Safety</h2><ul>'+P.safety.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul>';
 if(P.checklist)h+='<h2>Test-day checklist</h2>'+P.checklist.map(function(s){return '<div class="task"><span class="tk"></span>'+esc(s)+'</div>'}).join('');
 return h;
}
function docCards(){
 var C=P.cards,h='',per=10;
 for(var s=0;s<C.length;s+=per){var chunk=C.slice(s,s+per);
  h+='<div class="cardsheet">'+chunk.map(function(c){return '<div class="cc">'+esc(c[0])+'</div>'}).join('')+'</div>';
  var rows=[];for(var i=0;i<chunk.length;i+=2)rows.push([chunk[i],chunk[i+1]]);
  h+='<div class="cardsheet">'+rows.map(function(r){return '<div class="cc b">'+(r[1]?esc(r[1][1]):'')+'</div><div class="cc b">'+esc(r[0][1])+'</div>'}).join('')+'</div>'}
 return h;
}
var DOCS={notes:function(){return docNotes(null,'Study notes')},quick:function(){return docNotes(P.meta.quick||[P.notes[0].id],'Quick reference')},plan:docPlan,cards:docCards,testA:function(){return docTest('A')},testB:function(){return docTest('B')},keyA:function(){return docKey('A')},keyB:function(){return docKey('B')}};
function render(name){mkTest('A');mkTest('B');document.body.innerHTML='<div class="doc">'+DOCS[name]()+'</div>';document.title=name}
