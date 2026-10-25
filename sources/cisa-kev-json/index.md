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
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |
| The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayThe KEV dates are counted from the captured catalog; 'exploited in the wild one day after disclosure' rests on Akamai alone. [fact timeline →](../../facts/kev-precedent/index.html) | CISA KEV catalog; Akamai (2024) | reported | **A2** Reported●●○○○○ | 3/3 | [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |

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
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/cisa-kev-json/index.html
