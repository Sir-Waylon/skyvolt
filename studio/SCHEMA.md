# scioly-pack/1 — one JSON file per event
Build any event by filling this file; the engine (engine.html) and print builder read it unchanged.

meta: {id,title,division,year,org,facts:[[big,small]],intro}
topics: [{id,name,area,note}]            note = id of a notes entry (or "bench")
notes: [{id,title,html}]                 html is trusted, simple tags (p,ul,table,.card,.trap)
plan: [{t,focus,drill:{topics,n,mode?,min?},learn:[noteIds],tasks:[[kind,text]]}]   kind: warm|learn|drill|bench|wrap
cards: [[front,back]]
written: [[prompt,model answer]]         open response, self-checked
bench: [[title,html]]                    hands-on station
questions (ids are stable; progress export keys on them):
  mcq    {id,t,l,type,q,o:[correct,...wrong],w}       correct answer stored FIRST; engine shuffles
  multi  {…,o,a:[correct indexes]}
  short  {…,type:'short',q,num:{v,tol,unit?,units?:[...]} | text:[accepted strings/regex], w}
  order  {…,type:'order',q,items:[in correct order],w}
  match  {…,type:'match',q,pairs:[[left,right]],w}
  optional fig:{k:'S|P|SP|PS',r:[ohms],v}            circuit diagram
l = level 1 easy, 2 medium, 3 hard
Learner progress is separate (localStorage key = meta.id) and exported/imported as JSON text.
