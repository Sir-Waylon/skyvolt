import os,shutil,sys,subprocess
K=os.getcwd();O=os.path.join(K,'out')
cfg={'skyvolt':dict(name='Skyvolt',tracks='**Voltaic** (Science Olympiad Circuit Lab B) and **Stratus** (Meteorology B)',other='Axiom'),
     'axiom':dict(name='Axiom',tracks='**Apex** (Algebra 1 through Geometry readiness, Algebra 2, Trigonometry, Precalculus and Calculus) and **Quanta** (electrical engineering and physics)',other='Skyvolt')}
LIC="""MIT License\n\nCopyright (c) 2026 Sebastian de Lecea\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. These are proposed defaults; choose the license you want before publishing.\n"""
ONL="""# Online play (class and versus)

Two modes run on the same Worker and D1 database as accounts, with no account required.

- **Class game:** a host creates a game and shares a 6-letter code. Players join with a nickname. The host controls the pace (start, show answer, next).
- **Versus:** a player waits about 10 seconds for another student; if nobody is waiting they may choose a practice bot. Bots are always labelled "bot".

## How it works
Browsers poll `/api/room/state` about once a second. Rooms live in D1 and are deleted after 3 hours. Nicknames are filtered, and creating and joining are rate limited per IP.

## Honest limits
The question bank ships in the browser, so the server cannot know the right answer. The server bounds what a client can claim: capped points per question, answer times clamped to what the server measured, one answer per player per question, and late answers rejected. A determined cheater can still report every answer as correct. Use these modes for fun and class review, not for grades. Coins earned online are cosmetic.

## Data
Per game: nickname, avatar id, and for each question whether the answer was right and how long it took. See the privacy page.
"""
def readme(k,c):
    return f"""# {c['name']}

Part of **Voltaxis**, a family of free study trainers (Skyvolt and Axiom). Free, open study trainers for Science Olympiad Division B students and anyone learning along: {c['tracks']}.

Short lessons, typed answers, worked solutions, interactive question types, and practice that adapts to each student. Everything runs in the browser. Progress and personalization stay on the device unless the student signs in to sync.

> **AI-generated content.** The lessons, questions and code were produced with AI assistance and checked with automated tests, but they may still contain mistakes. Please read the [AI disclosure](public/ai-disclosure/index.html) and report errors through Issues.

## Layout
- `public/` the static site (deploy this folder)
- `functions/` optional account API (Cloudflare Pages Functions); `worker.js` and `wrangler.jsonc` for Worker deploys
- `schema.sql` database schema for accounts (Cloudflare D1)
- `docs/` deployment, accounts, security, learning design, accessibility
- `source/` question-bank and engine sources used to build the site

## Deploy (free)
1. Create a GitHub repository and upload this folder.
2. Cloudflare dashboard, Workers & Pages, Create, Pages, connect the repo.
3. Build command: none. Output directory: `public`.
4. Optional accounts: see `docs/ACCOUNTS.md`.

## Contributing and safety
See `CONTRIBUTING.md` and `SECURITY.md`. Questions about a wrong answer? Open an issue using the template.

## License
Code MIT, content CC BY-NC (proposed; see `LICENSE`).
"""
ACC="""# Accounts (optional)\n\nThe trainers work fully without accounts. To enable sign-in and friends:\n\n1. Cloudflare dashboard, Storage & Databases, D1, create a database.\n2. Run `schema.sql` in the D1 console.\n3. Bind the database as `DB` in the Pages project (Settings, Functions, D1 bindings).\n4. Add a secret named `PEPPER` (a long random string).\n5. For Google sign-in, create an OAuth client ID, add each site origin as an authorized origin, and set the client ID in the site configuration.\n6. Set `repo` and `site_url` in `site.config.json` and rebuild to show the repository link.\n\nPasswords are hashed server-side with PBKDF2 and a pepper. Session cookies are `__Host-` prefixed with CSRF protection. Rotate any secret that has been shared in chat or email.\n"""
SEC="""# Security\n\nHonest summary: a static site cannot be made unhackable. What we do:\n- Strict Content-Security-Policy, HSTS, COOP/CORP and related headers (`_headers`).\n- No third-party trackers. Practice data and personalization stay on the device.\n- Account passwords are hashed server-side (PBKDF2 plus pepper); cookies are `__Host-`, HttpOnly, SameSite.\n- Google ID tokens are verified for audience.\n\nReport vulnerabilities privately through GitHub Security Advisories. Do not post secrets in issues.\n"""
GAP="""# Gap analysis against popular learning apps\n\n| Area | Common approach | Here |\n|---|---|---|\n| Bite-size lessons | Duolingo, Brilliant | Short cards then practice |\n| Interactive questions | Brilliant | Graphs, sliders, angles, compass, ordering, proofs |\n| Adaptive practice | Khan, Duolingo | On-device model that tracks topic and question format strength |\n| Game loop | Blooket | Coins, packs, characters (cosmetic only) |\n| Worked solutions | Khan | Every question has steps |\n| Where others are better | Large video libraries (Khan), live multiplayer (Blooket) | Not duplicated; link to references |\n"""
LEARN="""# Learning design\n\nPractice testing, spaced and interleaved review, worked examples before problems, immediate corrective feedback, and desirable difficulty. Questions come in four tiers (Foundation, Bridge, Core, Mastery), each adjusted by question format because typing an answer is harder than choosing one. Adaptation happens on the device and is never shown as odds or hidden experiments. Rewards are cosmetic and never gate learning.\n"""
ACCESS="""# Accessibility\n\nKeyboard operable, visible focus, semantic landmarks, dark mode, reduced-motion support, text scaling. Automated axe-style checks pass on all apps; manual screen-reader testing with several browsers is still recommended. Not tested live on Firefox, Safari or iOS in the build environment.\n"""
LICC="""# Content license\n\nThe question banks, lessons, explanations, proofs and written documents in this repository are licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.\n\nFull legal text: https://creativecommons.org/licenses/by-nc/4.0/legalcode\n\nIn short: you may copy, share and adapt the content for non-commercial purposes if you credit the project and say what you changed. Classroom and school use is non-commercial.\n\nThe source code is licensed separately under the MIT License (see LICENSE).\n\nThis file is a notice, not the license text itself; the link above is the authoritative license.\n"""
CONTR="""# Contributing\n\nFound a wrong answer or unclear explanation? Open an issue with the question text and the topic. Pull requests that fix content are welcome; include a source for factual changes.\n"""
ISS="""---\nname: Wrong or unclear question\nabout: Report a content error\n---\nTopic and question text:\n\nWhat is wrong:\n\nSource that shows the correct answer:\n"""
for k,c in cfg.items():
    R=os.path.join(O,'repo-'+k)
    shutil.rmtree(R,ignore_errors=True);os.makedirs(R)
    shutil.copytree(os.path.join(O,k),os.path.join(R,'public'))
    b=os.path.join(K,'backend')
    shutil.copytree(os.path.join(b,'functions'),os.path.join(R,'functions'))
    for f in('worker.js','wrangler.jsonc','schema.sql'):shutil.copy(os.path.join(b,f),R)
    d=os.path.join(R,'docs');os.makedirs(d)
    for n,t in(('ACCOUNTS.md',ACC),('LEARNING_DESIGN.md',LEARN),('GAP_ANALYSIS.md',GAP),('ACCESSIBILITY.md',ACCESS),('SECURITY.md',SEC),('ONLINE_PLAY.md',ONL)):open(os.path.join(d,n),'w').write(t)
    open(os.path.join(R,'SECURITY.md'),'w').write(SEC)
    for n in('RESEARCH.md','AUDIT.md'):shutil.copy(os.path.join(K,'src','docs',n),d)
    open(os.path.join(R,'README.md'),'w').write(readme(k,c))
    open(os.path.join(R,'LICENSE'),'w').write(LIC);open(os.path.join(R,'LICENSE-CONTENT.md'),'w').write(LICC)
    open(os.path.join(R,'CONTRIBUTING.md'),'w').write(CONTR)
    os.makedirs(os.path.join(R,'.github','ISSUE_TEMPLATE'))
    open(os.path.join(R,'.github','ISSUE_TEMPLATE','content-error.md'),'w').write(ISS)
    open(os.path.join(R,'.gitignore'),'w').write("node_modules/\n.wrangler/\n.dev.vars\n*.log\n.DS_Store\n")
    open(os.path.join(R,'.gitattributes'),'w').write("* text=auto\n*.pdf binary\n")
    os.makedirs(os.path.join(R,'tests'));os.makedirs(os.path.join(R,'.github','workflows'),exist_ok=True)
    shutil.copy(os.path.join(K,'src','repo_tests','compat.mjs'),os.path.join(R,'tests','compat.mjs'))
    shutil.copy(os.path.join(K,'src','repo_tests','package.json'),os.path.join(R,'package.json'))
    shutil.copy(os.path.join(K,'src','repo_tests','compat.yml'),os.path.join(R,'.github','workflows','compat.yml'))
    src=os.path.join(R,'source');os.makedirs(src)
    packs={'skyvolt':['circuit-lab-b','meteorology-b'],'axiom':['geometry-readiness','apex-math','apex-merged','quanta-physics']}[k]
    for p in packs:
        shutil.copy(os.path.join(K,'events',p,'pack.json'),os.path.join(src,p+'.json'))
    for f in('engine3','src_adv','src_geo','src_met','build_open.py','mksite.py','rebuild.sh'):
        pth=os.path.join(K,f)
        if os.path.isdir(pth):shutil.copytree(pth,os.path.join(src,f),ignore=shutil.ignore_patterns('__pycache__'))
        elif os.path.exists(pth):shutil.copy(pth,src)
    z=os.path.join(K,'..',{'skyvolt':'Skyvolt','axiom':'Axiom'}[k]+'_repo.zip')
    if os.path.exists(z):os.remove(z)
    subprocess.check_call(['zip','-qr',z,'.'],cwd=R)
    print(k,os.path.getsize(z)//1024,'KB')
