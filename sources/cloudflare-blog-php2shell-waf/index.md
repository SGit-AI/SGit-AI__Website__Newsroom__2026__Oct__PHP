# Source: Cloudflare deploys protections against php2shell vulnerability

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Cloudflare: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Cloudflare deploys protections against php2shell vulnerability

**Cloudflare** · [https://blog.cloudflare.com/php-vulnerabilities-waf-protection/](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/) · published 2026-10-21 · added by `collector-researchers` · slug `cloudflare-blog-php2shell-waf`

Dated OCTOBER 21, 2026. Says the vulnerability 'was leaked before the official release date and we observed attack traffic targeting our customers'. WAF protection live from Oct 21 03:02 UTC (~9h before disclosure). Lists disclosers as 'Calif.io, Wiz, OpenAI and Quarkslab'. 'PHP is used by almost 70% of websites.'

## What it says, as the collector read it

#### Cloudflare blog: "Cloudflare deploys protections against php2shell vulnerability"

- URL https://blog.cloudflare.com/php-vulnerabilities-waf-protection/ ; dated "OCTOBER 21, 2026". Captured 2026-10-22T08:12:16Z.

- Disclosers: "Today, Calif.io, Wiz, OpenAI and Quarkslab disclosed two vulnerabilities" — the only researcher-beat source naming Quarkslab as a 2026 discloser (others credit Quarkslab for the 2024 audit only).

- Probing / leak: "Cloudflare successfully deployed multiple mitigations for all its customers while the vulnerability was leaked before the official release date and we observed attack traffic targeting our customers. We observed how attackers were mutating the attack payload to try to bypass our protections".

- Timing: WAF protections developed "since early October 2026", "deployed about 9 hours ahead of public disclosure. Starting on October 21 3:02 am UTC".

- 70%: "PHP is used by almost 70% of websites." (websites, not "the internet").

- No attack volumes in the post. Volumes attributed to Matthew Prince (thousands -> millions) in secondary coverage are NOT in this post — find his X post.

- Partners: "working with PHP foundation, OpenAI and Wiz among others".

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. [fact timeline →](../../facts/waf/index.html) | CISA | disputed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| PHP is used by almost 70% of websites whose server-side language is knownNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. [fact timeline →](../../facts/scale-70pc-websites/index.html) | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | **A2** Reported●●○○○○ measures differently | 3/3 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloadsPrimary party, no volumes. [fact timeline →](../../facts/cloudflare-traffic/index.html) | Cloudflare | reported | **A2** Reported●●○○○○ | 1/1 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | **A5** Confirmed●●●●●○ | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 OctoberEvery vendor says the same two things: it is a stopgap, and patch anyway. [fact timeline →](../../facts/waf-nine-hours/index.html) | the vendors | confirmed | **A2** Reported●●○○○○ status overstated | 5/5 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10 | Cloudflare starts developing WAF protections 'since early October 2026'. | stated |
| 2026-10-21 03:02 UTC | Cloudflare's WAF protections go live for all customers, about nine hours ahead of disclosure. | stated |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| almost 70% | websites | reported |
| about 9 hours | before disclosure, Cloudflare's WAF rules went live for all customers | confirmed |

### Exploitation signals from this source
- [2026-10-20 to 21](../../exploitation/index.html): 'We observed attack traffic targeting our customers' after the leak, and attackers 'mutating the attack payload to try to bypass our protections'. No volumes gi
- [2026-10-22](../../exploitation/index.html): Amazon and Cloudflare saw sites being probed for the flaw.

## The bytes
capture 20261022T081216Z · HTTP 200 · https://blog.cloudflare.com/php-vulnerabilities-waf-protection/- `headers.json` 904849b322ddad92fccc55d4ce8527d9c4138d07d61937ce1da5602ea2bef244 7,260 bytes
- `page.html` 421005107f81d30d16850fdbf830446d6fd544746dfa7d201be9b4bd3f656e72 301,730 bytes
- `provenance.json` 7f98162527014e2989dfaa73146a26c079c634ddf24eff95ae99fad7ea43beb0 1,045 bytes
- `rendered.html` a0d3c37cde7c1721a08b028748a412672817c45958d05cc7fedaede582b5537b 373,881 bytes
- `screenshot.png` 1784904e6fdda092941881d0e5c85d73801054f216295ca43b17f76e7f5cd34b 989,488 bytes
- `text.txt` 302408765abf45e3ae84473d9050c1c65b35c2858e5b53be4fee29dda4de2823 10,205 bytes
capture 20261023T160435Z · HTTP 200 · https://blog.cloudflare.com/php-vulnerabilities-waf-protection/- `headers.json` c8d1046d5e15ec072fa3f8200f1b2e9345d25f2fa5c1ce0a5d50de4bc57c2434 7,335 bytes
- `page.html` 172e5df835d69af6d6694fe84442639f792a58b8925a1408e8d68921824a7d97 306,061 bytes
- `provenance.json` b55c9fe97424debdba98dc1c1dca272d72f5ad2ff601542c5dfaa934de7ce34e 1,798 bytes
- `rendered.html` 9375a77287688e3c1d8718c25ce857c25caf62db2c3630e19d21da1c5bf24c48 373,128 bytes
- `screenshot.jpg` 16e9126356ed130c33ba0896333af9953971a4c4a4b31ad6f4823d6590d4d895 639,665 bytes
- `text.txt` 94476de6ec0b31e035ef97a1dbf9607bc81e7ddbb479c2d5217b8e8b0207ec02 11,328 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/cloudflare-blog-php2shell-waf/index.html
