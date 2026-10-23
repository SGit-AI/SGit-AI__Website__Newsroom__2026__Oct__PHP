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
| As of 20:50 UTC on 22 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, and two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same). Attempts are not compromises: watchTowr says "nobody has been successful to date"; Amazon says it is unclear whether any attempt would have succeeded on real systems; Patchstack's incidents are reports from hosting partners with no victim named. Source watch (vault oq9gflln), pending promotion into the evidence vault: the PHP Foundation's executive director told The Verge and WIRED "to our knowledge, there has been no successful attempt at remote code execution" (raw/us/tech-press/the-verge/php2shell-websites-down/); officials in Germany, the Netherlands and Japan say they have not seen an attack succeed (The Next Web, raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/); GMO confirmed a break-in on 20 October on its FX trading VPS service (26,739 servers, logins possibly taken) without stating the cause (raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/); Czech Technical University says it stopped an active attack that was part of worldwide attempts against PHP sites, success not established (raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/); Valtec in Japan blamed php2shell for a break-in, then retracted: its own service's flaw (raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/); Fortune reports an anonymous startup owner alleging stolen source code, unnamed and not attributed to the flaw. Edited by researcher@php.newsroom. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault and the source watch, as of 20:50 UTC on 22 October | reported | **A4** Corroborated●●●●○○ status overstated | 6/9 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
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

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.8.4 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/sources/imperva-blog-php2shell/index.html
