# Source: Critical Vulnerabilities in PHP Require Immediate Patching

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

US Cybersecurity and Infrastructure Security Agency (CISA): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Critical Vulnerabilities in PHP Require Immediate Patching

**US Cybersecurity and Infrastructure Security Agency (CISA)** · [https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · published 2026-10-21 · added by `collector-gov` · slug `cisa-alert-php-20261021`

CISA Alert, Release Date October 21, 2026. Names CVE-2026-109618/109619 'php2shell'. 'Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated.' CISA 'has not observed exploitation ... as of the time of publication'. Not in KEV as of catalog 2026.10.21.

## What it says, as the collector read it

#### CISA Alert: Critical Vulnerabilities in PHP Require Immediate Patching

- URL: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching. "Release Date October 21, 2026" (no time given).

- Captured 2026-10-22T08:13:53Z with Playwright. Plain curl to www.cisa.gov returns 403 (Akamai), but the headless browser gets 200. The CISA home page (`cisa-home`) lists it at the top as "OCT 21, 2026 ALERT".

- Exact advice, verbatim:

- "CISA strongly urges organizations to immediately patch the recently disclosed critical vulnerabilities in PHP, CVE-2026-109618 and CVE-2026-109619."

- "Organizations should immediately update to PHP 8.5.12, 8.4.27, 8.3.36, or 8.2.35"

- "Identify and inventory systems running any version of PHP across your organization."

- "Apply the patch immediately, prioritizing internet-facing systems."

- "Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated."

- "A web application firewall may provide some protection until systems are updated or patched."

- "Monitor for suspicious activity, including PHP worker processes launching shells or downloading tools."

- Exploitation: "While CISA has not observed exploitation of these vulnerabilities as of the time of publication".

- The CISA offline advice is the most absolute ("should take ... offline"), and it explicitly covers EOL 8.1 and older. No emergency directive found (see `cisa-kev-json`).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. [fact timeline →](../../facts/waf/index.html) | CISA | disputed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. [fact timeline →](../../facts/cisa-none/index.html) | CISA | confirmed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline [fact timeline →](../../facts/offline-cisa/index.html) | CISA | confirmed | **A6** Established●●●●●● | 1/1 | [CISA](../../sources/cisa-alert-php-20261021/index.html) |
| As of 20:50 UTC on 22 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, and two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same). Attempts are not compromises: watchTowr says "nobody has been successful to date"; Amazon says it is unclear whether any attempt would have succeeded on real systems; Patchstack's incidents are reports from hosting partners with no victim named. Source watch (vault oq9gflln), pending promotion into the evidence vault: the PHP Foundation's executive director told The Verge and WIRED "to our knowledge, there has been no successful attempt at remote code execution" (raw/us/tech-press/the-verge/php2shell-websites-down/); officials in Germany, the Netherlands and Japan say they have not seen an attack succeed (The Next Web, raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/); GMO confirmed a break-in on 20 October on its FX trading VPS service (26,739 servers, logins possibly taken) without stating the cause (raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/); Czech Technical University says it stopped an active attack that was part of worldwide attempts against PHP sites, success not established (raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/); Valtec in Japan blamed php2shell for a break-in, then retracted: its own service's flaw (raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/); Fortune reports an anonymous startup owner alleging stolen source code, unnamed and not attributed to the flaw. Edited by researcher@php.newsroom. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault and the source watch, as of 20:50 UTC on 22 October | reported | **A4** Corroborated●●●●○○ status overstated | 6/9 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Agency rows from this source
- [CISA](../../agencies/index.html): offline yes

### Exploitation signals from this source
- [2026-10-21](../../exploitation/index.html): 'CISA has not observed exploitation of these vulnerabilities as of the time of publication.' Neither CVE is in the Known Exploited Vulnerabilities catalog (vers

## The bytes
capture 20261022T081353Z · HTTP 200 · https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching- `headers.json` 30fb6764c792111ac226e0fb1ca4f574f5e2faadfc10d2150ae9dfa35ea0858d 2,825 bytes
- `page.html` be6b410fc0da16de2c1b96dc3132a195632d636467ab7c859c343494fa7accfa 53,868 bytes
- `provenance.json` ea18f4dbc502d3c87b5d9a6c83d49ff128544ad074140c502f37abff350d9f8a 1,110 bytes
- `rendered.html` 0e3e08492a52d48e8ccb18f836df984af4f15f251f6089697676b540458b3371 78,116 bytes
- `screenshot.png` 2724e9107ccae45a888b3531fdc43373b154be3eeadb78841791dcb6a60a34c1 384,239 bytes
- `text.txt` 7bf853872a073bde9c2d71a41fbf9bfd3cda8147c278ab15426ebc9c8e627a9f 3,223 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.10.14 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/sources/cisa-alert-php-20261021/index.html
