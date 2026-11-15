# Brief: lesson "Go deeper" authoring (Voltaxis study apps)
Audience: PAUSD 8th graders (Science Olympiad Division B / math), many with ADHD. Reading level ~grade 7. Short sentences, concrete nouns, no jargon without a plain definition.
Goal: for EVERY lesson card in your files write an optional deep-dive that truly explains the CONCEPT, not just restates the formula, and shows it several ways.
Input: audit/lessons/<event>_<unit>.txt. Lines: `KEY <lessonId>#<cardIdx> | heading | text | FORMULA: ... | CHECK Q: ...`. One output entry per KEY line.
Output: ../kit/src/dd/<TAG>.json = {"<lessonId>#<idx>": {dd}} (write with a python script; valid JSON, UTF-8, plain text only: NO HTML, NO LaTeX; write math in plain text like x^2, 1/2, sqrt(x), theta, and keep units).
dd fields (all strings unless noted; omit a field only if it truly does not apply):
- why: 3-6 sentences on the mechanism: WHY it is true, cause and effect, what would break if it were different.
- pic: 2-4 sentences describing a mental picture or sketch the student can draw (say what to draw and where).
- analogy: an everyday comparison (water, traffic, school, sports, food) with the mapping stated (what plays the role of what) and where the analogy stops working.
- ways: list of 2-3 pairs [label, text] showing the same idea in other representations: In words / In numbers (a small table-like example) / As a graph or diagram / As a rule of thumb.
- ex: {"q": a worked example question, "steps": [4-7 short steps, each says what is done AND why]} with a numeric answer verified in python.
- trap: the most common mistake and how to avoid it.
- tip: one memory hook (mnemonic, rhyme, story).
Rules: factual accuracy is the priority (verify numbers in python; do not invent facts; Science Olympiad context: Circuit Lab B and Meteorology B 2026-27 rules). Original wording. Each dd 120-220 words total. No filler like "In this lesson".
COST LIMITS (shared usage budget is tight): do not browse the web or fetch PDFs; write all entries via ONE or TWO python build scripts; do not re-read files; keep your final message under 60 words.
