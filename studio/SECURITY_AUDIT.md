# Security audit: Circuit Lab B trainer (v4)
Threat: students editing XP/coins, reading answers, or cheating on friend boards. Static page, no server.

| Control | Status |
|---|---|
| Pack (questions, answers, study text) | AES-256-GCM over gzip; key = PBKDF2-SHA256 600k iterations from class passcode; random salt/IV. Verified: ciphertext only in the HTML |
| Wrong-passcode attempts | Exponential delay; GCM auth failure reveals nothing |
| Remember on device | Non-extractable CryptoKey in IndexedDB; passcode never stored |
| Saved progress | AES-GCM encrypted + authenticated, key via HKDF(class secret, per-device salt). Edited/corrupt data is rejected and resets. Tested |
| Plausibility check | XP bounded by answers given, coins bounded by XP; impossible saves reset |
| Console cheating | Engine runs in a closure; no globals (S, award, QS undefined in console). Tested |
| Share/backup codes | HMAC-SHA256 signed (SCI1/SCP1), class-scoped; forged friend code rejected. Tested |
| CSP | Script locked to the page's SHA-256 hash; connect-src none; no eval, no forms, no framing (header), no referrer |
| Economy | Coins buy cosmetics only; help costs XP only; no practical advantage to farm |

Honest limits: anyone with the passcode can decrypt the bank in their own code, and a determined student could rebuild a valid save with that knowledge. A static site cannot fully prevent this; real protection needs a server that scores answers (e.g. a Cloudflare Worker). Cosmetic-only coins remove most reason to try. Rotate the passcode (rebuild) each season or if it leaks.
