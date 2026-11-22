# Security setup guide (Voltaxis: Skyvolt + Axiom)

Everything here is either already in the code or is a step only the site owner can do (DNS, registrar, dashboards). Nothing below is a certification claim: it describes controls and how to verify them.

## 1. Stack

| Layer | What we use |
|---|---|
| Front end | Vanilla JavaScript engine (`engine3/*.js`), generated static HTML/CSS, no framework, no build-time bundler on the client |
| Build tooling | Python 3 scripts (`mksite.py`, `build_open.py`, pack pipelines), `rebuild.sh`, `publish.py` |
| Hosting | Cloudflare Workers with static assets; Workers Builds auto-deploys from GitHub |
| Backend | One Worker per site (`backend/functions/api/[[route]].js`), shared Cloudflare D1 database |
| Auth | Email + password (PBKDF2-SHA-256 with per-user salt and a `PEPPER` secret), Google sign-in, `__Host-` cookies |
| Anti-abuse | Cloudflare Turnstile CAPTCHA, hashed-key rate limits, Have I Been Pwned range check |
| Email | Mailtrap Email API (verification and optional sign-in codes) |
| Tests / CI | Playwright (Chromium locally; Chromium, Firefox, WebKit on Ubuntu/Windows/macOS via GitHub Actions), axe-core |

## 2. What the code now does

- **Passwords:** 12+ characters; must contain a number or be 16+ characters; at least 6 different characters; no 4 identical characters in a row; no 5-character runs (`12345`, `abcde`); no site name; not on a common-password list; not built from the email or username; checked against Have I Been Pwned (k-anonymity, fails open if unreachable). Stored as PBKDF2-SHA-256 (100,000 iterations, the Workers maximum) with per-user salt and secret pepper.
- **Email verification:** new password sign-ups get a 6-digit code (10 min, 5 tries, 60 s resend wait, stored only as a peppered hash). Unconfirmed accounts are deleted after 7 days. Existing accounts and Google sign-ins count as verified.
- **Optional 2-step sign-in:** Me → Friends → Sign-in codes. After the password, an emailed code is required. Opt-in to protect the free email quota.
- **CAPTCHA:** Cloudflare Turnstile on sign-up and sign-in. The server fails closed once `TURNSTILE_SECRET` is set; the page shows a retry message if the script cannot load.
- **Cookies:** `__Host-sid` (HttpOnly, Secure, Path=/, SameSite=Strict, no Max-Age, 8 h server TTL) and `__Host-csrf`.
- **Headers (`_headers` and Worker responses):** enforced CSP; a stricter **Report-Only** CSP (`style-src-attr 'none'`, `require-trusted-types-for 'script'`) reporting to `/api/csp-report`; HSTS; `X-Content-Type-Options`; `Referrer-Policy`; `Permissions-Policy`; COOP/CORP; `Origin-Agent-Cluster`; `X-Permitted-Cross-Domain-Policies`; `Reporting-Endpoints`.
- **Report-Only noise:** the report-only policy intentionally flags inline `style=""` attributes and `<style>` elements the apps inject. Treat these as a to-do list for tightening, not as breakage. The enforced policy shows zero violations in `t140.js`.

## 3. Mailtrap + Turnstile setup (do on BOTH Workers: skyvolt and axiom)

1. Create a Mailtrap account → **Sending Domains → Add Domain** (use a domain you own, e.g. `voltaxis.example`).
2. Add the DNS records Mailtrap shows (SPF include, DKIM CNAMEs, tracking/return-path if offered, DMARC). Wait until the domain shows **Verified**.
3. **Settings → API Tokens**: create a token for that domain (transactional stream).
4. In each Worker project directory:
   ```
   npx wrangler secret put MAILTRAP_API_TOKEN
   npx wrangler secret put MAIL_FROM     # e.g.  Voltaxis <no-reply@voltaxis.example>   (must be on the verified domain)
   ```
   Optional: `BRAND` variable (defaults to "Voltaxis").
5. Turnstile: Cloudflare dashboard → **Turnstile → Add widget**, add both site hostnames, mode Managed. Put the **site key** in `wrangler.jsonc` under `vars` as `TURNSTILE_SITE_KEY`, and the **secret key** with `npx wrangler secret put TURNSTILE_SECRET`.
6. Redeploy (push to GitHub, or `npx wrangler deploy`). `/api/config` reports `verify`, `tfa` and `turnstile` as true when set.
7. Free Mailtrap limits are about 150 emails/day and 4,000/month. Verification and optional 2FA stay inside that for a team; if you need more, upgrade the plan.
8. Until the secrets exist, nothing breaks: accounts are auto-verified, 2FA is hidden and the CAPTCHA is off. There is no password-reset flow yet (planned).

## 4. DNS and email security (owner steps)

Replace `example.com` with your domain. Verify each with the `dig` command shown.

- **DNSSEC:** Cloudflare DNS → Settings → DNSSEC → Enable, then copy the **DS record** to your registrar. Check: `dig +dnssec example.com SOA` (look for the `ad` flag) or dnsviz.net.
- **CAA:** limit who may issue certificates. Cloudflare issues from Google Trust Services and others. Add: `0 issue "pki.goog"`, `0 issue "letsencrypt.org"`, `0 issue "digicert.com"`, `0 iodef "mailto:security@example.com"`. Cloudflare's Universal SSL may add its own CAA records automatically; do not delete those. Check: `dig CAA example.com`.
- **SPF** (one TXT at the root, one only): use the exact include Mailtrap gives, e.g. `v=spf1 include:_spf.smtp.mailtrap.live ~all`. Start with `~all`, move to `-all` once mail flows. If you also send through Cloudflare Email Routing/other tools, add their include to the same record (max 10 DNS lookups).
- **DKIM:** add the DKIM CNAME/TXT records exactly as Mailtrap displays. Check selector: `dig CNAME <selector>._domainkey.example.com`. Rotate if Mailtrap prompts.
- **DMARC:** TXT at `_dmarc.example.com`. Roll out: `v=DMARC1; p=none; rua=mailto:dmarc@example.com; adkim=s; aspf=s` for two to four weeks → `p=quarantine; pct=25` → `p=quarantine` → `p=reject`. Read the aggregate reports before each step.
- **MX:** if the domain receives no mail, publish a **null MX**: `0 .` (stops spoofed bounces). If you want an inbox, use Cloudflare Email Routing (it sets the MX for you) and keep SPF consistent.
- **NS:** use only your DNS host's two nameservers; turn on **registrar lock** and two-factor on the registrar and Cloudflare accounts; keep WHOIS contact current. Check: `dig NS example.com`.
- **Optional:** MTA-STS and TLS-RPT TXT/policy files for inbound mail (only if you receive mail); add a `/.well-known/security.txt` (Contact + Expires) once you have a public security contact address; none is published yet.
- **Cloudflare TLS:** SSL/TLS mode Full (strict); Minimum TLS 1.2; TLS 1.3 on; Always Use HTTPS; Automatic HTTPS Rewrites; HSTS on (max-age 6 months+, includeSubDomains once every subdomain is HTTPS). Do not submit to the HSTS preload list unless you accept it is hard to undo.
- **Quick check:** hardenize.com, internet.nl, mxtoolbox.com (SPF/DKIM/DMARC), securityheaders.com, ssllabs.com.

## 5. PCI DSS 4.0, Requirement 4 (protect cardholder data in transit)

Voltaxis processes **no payment-card data**: the shop is cosmetic, uses earned coins only and has no payments, so no cardholder data environment exists. Requirement 4 is nonetheless met by design for all data in transit: TLS 1.2+ only (Cloudflare edge, HTTPS-only with HSTS), certificates issued and renewed by Cloudflare with a certificate inventory in the dashboard (Req. 4.2.1.1), no end-user messaging used to send sensitive data. **If payments are ever added**, use a hosted checkout from a PCI-validated provider (Stripe Checkout, PayPal) so card numbers never touch these Workers, and complete the matching self-assessment (SAQ A). This is a description of design, not a compliance certificate.

## 6. GDPR checklist

- Data minimised: email, username, hashed password, progress; no analytics or ad trackers.
- Lawful bases, rights, transfers, children's age (13+ with permission below), retention and 72-hour breach notice are in the Privacy Policy.
- Owner to do: name the controller and contact address in the policy (`site.config.json`), keep a processor list (Cloudflare, Mailtrap, Google if used), sign each provider's DPA (accept Cloudflare's and Mailtrap's online DPA), keep a simple record of processing, and answer rights requests within one month.
- Account deletion in the app erases the account, progress, friend links and codes.
- Have a lawyer review before wider public launch.
