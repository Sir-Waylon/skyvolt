# Design inspiration notes (Nov 17 2026)

Sources: seven reference screenshots supplied by the coach (Amplify-style science simulations: malaria drug design, baby warmer/phase-change materials, cargo pod design), plus the project index of juliangonzalez.design.

Not retrievable (do not retry blindly): rexcreations.com (robots.txt disallows automated access), artstation.com (client error), coolors.co (page needs JS). The sandbox shell cannot download from the portfolio host (proxy 403), and the fetch tool returns text only, so no images were scraped. Reference images are for inspiration only; none are copied into the apps. Character designs must be original.

## Patterns observed (to apply in Labs)
1. Workbench layout: left control panel, large central diagram, running totals bar at the bottom (mass, cost, score).
2. Category accordion in the panel (Shell, Padding, Add-ons): one open at a time, green header, rows with swatch, name and values in aligned columns.
3. Cards with large numbered circles, one colour per option (pastel on dark), a dashed empty slot, and a pointer-hand hint for the first drag.
4. Graph view with a playback slider under the chart, coloured bands for safe/unsafe zones, and a "Return to design" button.
5. Results card on dark: big headline numbers, small labels, a single primary button.
6. Muted grey stage, one saturated accent, lots of whitespace, rounded cards.
7. Always-visible running cost/limit readout, so trade-offs are felt.

## Plan for Labs
- Lab shell component: panel (accordion) + stage + totals bar + results card.
- Lab-specific controls only inside the panel (sliders, chips, component pickers).
- Playback slider for time-based labs (RC charging, fronts moving).
- Coach-approved fonts: Inter now; Josefin Sans, Ubuntu, Open Sans pending font files.

## Portfolio projects worth reviewing by hand
Baby Warmer /phase-change-incubator, Light Waves /light-waves, Soundwaves /sound-waves-visualizer, Math Workspace /math-workspace (toolbar plus tools launcher).

## Brand system (Nov 17, single source: src/brand.json)
- Sites: Skyvolt = green #2D6A4F + blue #0077B6 (gold #FFB703); Axiom = red #BC4749 + teal #0F4C5C (gold #E9B44C). Dark-mode primaries are lighter tints; mksite.py asserts AA contrast.
- Trainers: Voltaic green, Stratus blue, Apex red, Quanta teal. Roster/avatar backgrounds use the same hues.
- Icons: rounded-square glyphs (bolt, cloud+bolt, triangle, atom) as SVG plus 180/192/512 PNGs via icons_png.js (apple-touch, manifest).
- Cosmetic direction from the 16 character references (Fortnite art): turnaround sheets (front/back), one outfit in several colourways, a limited palette with a single metallic accent, strong silhouettes. Used as principles only; avatars stay original and no reference character is reproduced.

## Security stance (accurate wording)
- Passwords are not used (Google sign-in). Data is encrypted in transit (HTTPS) and at rest by Cloudflare. It is NOT end-to-end encrypted: friends, leaderboards and username suggestions need the server to read usernames and public progress.
- Possible later: optional client-side (WebCrypto AES-GCM) encryption of private progress backups with a passphrase the server never sees; trade-off is that a lost passphrase cannot be recovered.
