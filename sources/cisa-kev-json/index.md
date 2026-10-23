# Source: CISA Known Exploited Vulnerabilities catalog (JSON feed)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

CISA: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# CISA Known Exploited Vulnerabilities catalog (JSON feed)

**CISA** · [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) · published 2026-10-21T14:04:39Z (catalogVersion 2026.10.21) · added by `collector-gov` · slug `cisa-kev-json`

At 08:15Z on 22 Oct: catalogVersion 2026.10.21, dateReleased 2026-10-21T14:04:39.8983Z, 1754 entries. CVE-2026-109618/109619 NOT in KEV. Raw JSON + headers + SHA256SUMS in raw/.

## What it says, as the collector read it

#### CISA KEV catalog (JSON)

- Fetched with curl about 08:15Z on 22 Oct 2026 and saved in raw/ (headers, JSON, SHA256SUMS).

- `catalogVersion` 2026.10.21, `dateReleased` 2026-10-21T14:04:39.8983Z, `count` 1754; last-modified Wed, 21 Oct 2026 14:04:39 GMT.

- **Neither CVE-2026-109618 nor CVE-2026-109619 is in the catalog.** That fits CISA alert text "has not observed exploitation". The latest additions are dated 2026-10-20 (Plex, SiteGuard, Siemens).

- Older PHP entries in the catalog: CVE-2024-4577, CVE-2019-11043, CVE-2012-1823.

- No CISA emergency directive for PHP was found (the home page lists none). Re-check KEV later today.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. [fact timeline →](../../facts/cisa-none/index.html) | CISA | confirmed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| As of 20:50 UTC on 22 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, and two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same). Attempts are not compromises: watchTowr says "nobody has been successful to date"; Amazon says it is unclear whether any attempt would have succeeded on real systems; Patchstack's incidents are reports from hosting partners with no victim named. Source watch (vault oq9gflln), pending promotion into the evidence vault: the PHP Foundation's executive director told The Verge and WIRED "to our knowledge, there has been no successful attempt at remote code execution" (raw/us/tech-press/the-verge/php2shell-websites-down/); officials in Germany, the Netherlands and Japan say they have not seen an attack succeed (The Next Web, raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/); GMO confirmed a break-in on 20 October on its FX trading VPS service (26,739 servers, logins possibly taken) without stating the cause (raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/); Czech Technical University says it stopped an active attack that was part of worldwide attempts against PHP sites, success not established (raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/); Valtec in Japan blamed php2shell for a break-in, then retracted: its own service's flaw (raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/); Fortune reports an anonymous startup owner alleging stolen source code, unnamed and not attributed to the flaw. Edited by researcher@php.newsroom. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault and the source watch, as of 20:50 UTC on 22 October | reported | **A4** Corroborated●●●●○○ status overstated | 6/9 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayCounted from the captured catalog. [fact timeline →](../../facts/kev-precedent/index.html) | CISA KEV catalog; Akamai (2024) | confirmed | **A2** Reported●●○○○○ status overstated | 3/3 | [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 14:04:39 UTC | CISA releases KEV catalog version 2026.10.21; neither PHP CVE is in it. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 270 | CVEs added to CISA's Known Exploited Vulnerabilities catalog in 2026 so far; 0 of them php2shell | confirmed |

### Agency rows from this source
- [CISA](../../agencies/index.html): offline yes

### Exploitation signals from this source
- [2026-10-21](../../exploitation/index.html): 'CISA has not observed exploitation of these vulnerabilities as of the time of publication.' Neither CVE is in the Known Exploited Vulnerabilities catalog (vers

## The bytes

No browser capture; see raw.
raw, 2 files with SHA256SUMS- `headers.20261022T0816Z.txt` e3a7dc7610f87ca2b7829303cd01ef65a3d0d08be833334024807456cc943db9
- `known_exploited_vulnerabilities.20261022T0816Z.json` ef8fffede5c472001da046c7751beb2a3242458896d0ce08da52b30968b8b56b

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.10.15 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/sources/cisa-kev-json/index.html
