import os,shutil,subprocess,sys
K=os.getcwd();msg=sys.argv[1] if len(sys.argv)>1 else 'Update'

# continuity bundle: whole working kit (minus build outputs) so work can resume if the sandbox is lost
def bundle():
    R='/home/claude/skyvolt';dst=os.path.join(R,'studio');shutil.rmtree(dst,ignore_errors=True)
    ign=shutil.ignore_patterns('out','shots','node_modules','*.png','*.zip','__pycache__','HANDOFF*','*.private*')
    shutil.copytree(K,dst,ignore=ign)
    shutil.copytree(os.path.join(os.path.dirname(K),'audit'),os.path.join(dst,'audit'),ignore=shutil.ignore_patterns('__pycache__'))

subprocess.check_call(['python3','mkrepo.py'],stdout=subprocess.DEVNULL)
for k,R,sub in [('skyvolt','/home/claude/skyvolt','Skyvolt_repo'),('axiom','/home/claude/axiom','Axiom_repo(1)')]:
    subprocess.check_call("git fetch -q origin main && git reset -q --hard origin/main",shell=True,cwd=R)
    if k=='skyvolt':bundle()
    old=os.path.join(R,sub);w=os.path.join(R,'site')
    if os.path.isdir(old):subprocess.check_call(['git','mv',sub,'site'],cwd=R)
    shutil.rmtree(w,ignore_errors=True);shutil.copytree(os.path.join(K,'out',k),w)
    wr=os.path.join(R,'wrangler.jsonc');t=open(wr).read().replace('./'+sub,'./site');open(wr,'w').write(t)
    rd=os.path.join(R,'README.md');t=open(rd).read().replace(sub+'/','site/').replace(sub,'site').replace('**Vertex** (Algebra 1 to Honors Geometry), **Apex** (Algebra 2, Trigonometry, Precalculus, Intro Calculus)','**Apex** (Algebra 1 through Geometry, Algebra 2, Trigonometry, Precalculus and Calculus)');open(rd,'w').write(t)
    S=os.path.join(K,'out','repo-'+k)
    for f in('tests','.github/workflows'):
        dst=os.path.join(R,f);shutil.rmtree(dst,ignore_errors=True);shutil.copytree(os.path.join(S,f),dst)
    for f in('package.json','LICENSE-CONTENT.md','LICENSE'):shutil.copy(os.path.join(S,f),R)
    for f in('docs','source'):
        dst=os.path.join(R,f);shutil.rmtree(dst,ignore_errors=True);shutil.copytree(os.path.join(S,f),dst)
    d=os.path.join(R,'backend');shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    for f in('functions','worker.js','schema.sql'):
        t=os.path.join(S,f);(shutil.copytree if os.path.isdir(t) else shutil.copy)(t,os.path.join(d,f))
    m=msg.replace("'","")
    subprocess.check_call(f"git add -A && (git diff --cached --quiet || git -c user.name='Claude' -c user.email='noreply@anthropic.com' commit -qm '{m}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_017iesXiQn9bwgQuZ5Gqpfja' && git push -q origin HEAD:main && echo pushed {k})",shell=True,cwd=R)
