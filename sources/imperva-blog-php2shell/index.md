# Source: PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Imperva Threat Research (Nadav Avital, Bar Menachem): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva

**Imperva Threat Research (Nadav Avital, Bar Menachem)** · [https://www.imperva.com/blog/php2shell-vulnerability-updates/](https://www.imperva.com/blog/php2shell-vulnerability-updates/) · published 2026-10-21 · added by `claude-story-site` · slug `imperva-blog-php2shell`

Five demonstrated techniques, three via session upload progress; attack complexity high; ~67 KB memory disclosure; no matching traffic in pre-disclosure monitoring; '69% of websites whose server-side language is known'.

## What it says, as the collector read it

#### PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva

Captured by claude-story-site. Status: captured. Five demonstrated techniques, three via session upload progress; attack complexity high; ~67 KB memory disclosure; no matching traffic in pre-disclosure monitoring; '69% of websites whose server-side language is known'.

- 'Researchers from Wiz, OpenAI, and Calif jointly disclosed PHP2Shell'; involves 'session handling, OPcache class caching, and fatal-error backtrace generation'.

- 'Triggering the bug is much easier than turning it into code execution.' 'A later request must reach the same Apache worker and place carefully shaped data'.

- 'Three of the five demonstrated exploitation techniques use PHP's session upload-progress feature'; 'An attack can expose approximately 67 KB of process memory'.

- 'During this pre-disclosure monitoring period, Imperva observed no traffic matching the monitored PHP2Shell exploit patterns.'

- Settings: disable OPcache and upload progress as temporary measures; least privilege; IR checklist (child processes, file changes, outbound connections).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosure monitoringA negative finding from a party that had the details under embargo. [fact timeline →](../../facts/imperva-none/index.html) | Imperva Threat Research | reported | **A2** Reported●●○○○○ measures differently | 1/1 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) |
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |
| Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity highFastly: 'most deployments may be safe from RCE. Do not assume this holds true for you.' Imperva: five demonstrated techniques, three via session upload progress; about 67 KB of memory disclosed per attack. [fact timeline →](../../facts/ac-high/index.html) | Imperva; Fastly; the CVE record | confirmed | **A3** Echoed●●●○○○ opinion status overstated | 3/3 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 OctoberEvery vendor says the same two things: it is a stopgap, and patch anyway. [fact timeline →](../../facts/waf-nine-hours/index.html) | the vendors | confirmed | **A2** Reported●●○○○○ status overstated | 5/5 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |

### Exploitation signals from this source
- [2026-10-21](../../exploitation/index.html): No traffic matching the exploit patterns during pre-disclosure monitoring of customer traffic.

## The bytes
capture 20261022T111855Z · HTTP 200 · https://www.imperva.com/blog/php2shell-vulnerability-updates/- `headers.json` fa04ad94125d615ccc22bfe0f44544c8737419ff06a9d85acf2e5e4776931849 3,102 bytes
- `page.html` b659e89f8fb17c9833c2b8d60454655d038e41bd867043684aff25984c3bf6e2 243,832 bytes
- `provenance.json` a2f25ae502d617f41375750794a46ff83e8a433361944da98d0daab48bd962ec 1,022 bytes
- `rendered.html` cb3120b21b6f0c89f3af549534f6b8ce3e381a19e5c6eecce3ec513cb1d18d5a 301,023 bytes
- `screenshot.png` 1f96ba16ce949cfd1d6f4051df3dd2b7910754612bb6fae060c14d96950f9c9e 1,932,384 bytes
- `text.txt` 3da873bdb21219a616245663c1c5bfccb9d8d5db507092c70bb2c20519e031e4 15,842 bytes
capture 20261023T080331Z · HTTP 200 · https://www.imperva.com/blog/php2shell-vulnerability-updates/- `headers.json` 007d70044b574554e6ab8cdb298d07a9ebb684af433ca2c6cddfdc30af531b23 3,175 bytes
- `page.html` 6ef087834881447bfdf1f2e5aee88bbe3672e5915fc1d25307a4873e154ef5f7 243,352 bytes
- `provenance.json` 14aafdeae68884459eb7993892c91bb643a6dd7a68ffd0f548be9d03cbc24495 1,595 bytes
- `text.txt` c8db3bc67fda0e55dd0a5434c423f099cb6872dfb584273d348f4c21e12861aa 15,819 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/imperva-blog-php2shell/index.html
