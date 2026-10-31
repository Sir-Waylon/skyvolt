# Skyvolt

Part of **Voltaxis**, a family of free study trainers (Skyvolt and Axiom). Free, open study trainers for Science Olympiad Division B students and anyone learning along: **Voltaic** (Science Olympiad Circuit Lab B) and **Stratus** (Meteorology B).

Short lessons, typed answers, worked solutions, interactive question types, and practice that adapts to each student. Everything runs in the browser. Progress and personalization stay on the device unless the student signs in to sync.

> **AI-generated content.** The lessons, questions and code were produced with AI assistance and checked with automated tests, but they may still contain mistakes. Please read the [AI disclosure](<Skyvolt_repo/ai-disclosure/index.html>) and report errors through Issues.

## Layout
- `Skyvolt_repo/` the static site (the folder Cloudflare serves)
- `backend/` optional account API (`functions/`, `worker.js`, `wrangler.jsonc`) and the D1 `schema.sql`
- `docs/` deployment, accounts, security, learning design, accessibility
- `source/` question-bank and engine sources used to build the site

## Deploy (free)
1. Create a GitHub repository and upload this folder.
2. Cloudflare dashboard, Workers & Pages, Create, Pages, connect the repo.
3. Build command: none. Output/asset directory: `Skyvolt_repo`.
4. Optional accounts: see `docs/ACCOUNTS.md`.

## Contributing and safety
See `CONTRIBUTING.md` and `SECURITY.md`. Questions about a wrong answer? Open an issue using the template.

## License
Code MIT, content CC BY-NC (proposed; see `LICENSE`).
