# -*- coding: utf-8 -*-
"""helpers for authoring interactive lesson widgets (see engine3/widgets.js)"""
def P(n,l,mn,mx,st,v,u=''):return [n,l,mn,mx,st,v,u]
def plot(hook,f,p,x=(-5,5),y=(-5,5),out='',pre=None,take=None,pts=None,xl='x',yl='y',vl=None):
    d=dict(k='plot',hook=hook,f=f,p=p,x=list(x),y=list(y),out=out,xl=xl,yl=yl)
    if pre:d['pre']=dict(q=pre[0],o=pre[1],a=pre[2],why=pre[3])
    if take:d['take']=take
    if pts:d['pts']=pts
    if vl:d['vl']=vl
    return d
def calc(hook,p,o,eq='',note='',pre=None,take=None):
    d=dict(k='calc',hook=hook,p=p,o=o,eq=eq,note=note)
    if pre:d['pre']=dict(q=pre[0],o=pre[1],a=pre[2],why=pre[3])
    if take:d['take']=take
    return d
def O(l,e,m=1,u='',d=2,c=None):
    r=dict(l=l,e=e,m=m,u=u,d=d)
    if c:r['c']=c
    return r
def steps(hook,s,take=None,pre=None):
    d=dict(k='steps',hook=hook,s=[dict(t=t) if isinstance(t,str) else t for t in s])
    if take:d['take']=take
    if pre:d['pre']=dict(q=pre[0],o=pre[1],a=pre[2],why=pre[3])
    return d
def predict(hook,q,o,a,why,k='steps',s=None,take=None):
    return steps(hook,s or [why],take=take,pre=(q,o,a,why))
def wave(hook,p,out,pre=None,take=None):
    d=dict(k='wave',hook=hook,p=p,out=out)
    if pre:d['pre']=dict(q=pre[0],o=pre[1],a=pre[2],why=pre[3])
    if take:d['take']=take
    return d
def simple(k,hook,pre=None,take=None,**kw):
    d=dict(k=k,hook=hook,**kw)
    if pre:d['pre']=dict(q=pre[0],o=pre[1],a=pre[2],why=pre[3])
    if take:d['take']=take
    return d
