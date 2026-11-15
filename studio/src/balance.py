import json,re,sys
def trim(c,limit):
    # shorten correct option by cutting trailing clauses
    for pat in (r'\s*\([^)]*\)\s*$',r'\s*[;—–]\s.*$',r',\s(?:and|but|so|because|which|while|where|with|even)\b.*$',r',\s.*$',r'\s(?:because|so that|which|while|where|since)\s.*$'):
        n=re.sub(pat,'',c).strip()
        if n and n!=c and len(n)>=3 and len(n)<=limit:return n
        if n and n!=c and len(n)>3:c2=n
    return None
def run(path):
    p=json.load(open(path,encoding='utf8'));fixed=0;left=0
    for q in p['questions']:
        if q['type']!='mcq':continue
        o=q['o'];c=o[0];L=sorted((len(x) for x in o[1:]),reverse=True)[0]
        if len(c)>16 and len(c)>=1.25*L:
            n=trim(c,max(int(1.2*L),12))
            if n:
                extra=c[len(n):].strip(' ,;—–()')
                q['o'][0]=n
                if extra and extra.lower() not in q.get('w','').lower():q['w']=(q.get('w','')+' ('+extra+')').strip()
                fixed+=1
            else:left+=1
    json.dump(p,open(path,'w'),ensure_ascii=False,separators=(',',':'));return fixed,left
if __name__=='__main__':
    for f in sys.argv[1:]:print(f,run(f))
