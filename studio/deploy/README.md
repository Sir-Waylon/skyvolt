# Circuit Lab B Trainer: free hosting (pick ONE)

The site is one file (`index.html`). Nothing to install. The question bank is encrypted; students need the class passcode (kept separately, never upload it).

## Easiest: Cloudflare Pages (free, supports security headers)
1. dash.cloudflare.com > Workers & Pages > Create > Pages > Upload assets.
2. Drag in `index.html` and `_headers`. Deploy. You get a `*.pages.dev` link.

## Also easy: Netlify Drop (free)
1. app.netlify.com/drop, drag in this folder. Link appears at once. (`_headers` is honored.)

## GitHub Pages (free)
1. New public repo, upload these files, Settings > Pages > Source: GitHub Actions.
2. GitHub Pages ignores `_headers`; the page's built-in CSP tag still applies.

Update the trainer later by uploading the new `index.html` the same way.
Give students the link and the passcode separately. Tick "Remember on this device" once.
