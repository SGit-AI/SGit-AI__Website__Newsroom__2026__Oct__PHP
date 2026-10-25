# Source: Recent wiki downtime (PHP2Shell mitigation) | Weird Gloop

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Weird Gloop (cookmeplox): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Recent wiki downtime (PHP2Shell mitigation) | Weird Gloop

**Weird Gloop (cookmeplox)** · [https://weirdgloop.org/blog/php2shell](https://weirdgloop.org/blog/php2shell) · published 2026-10-21 · added by `claude-story-site` · slug `weirdgloop-blog-php2shell`

Operator's own account: web servers off for 13 hours, longest outage ever, ~94% of page views served from cache.

## What it says, as the collector read it

#### Recent wiki downtime (PHP2Shell mitigation) | Weird Gloop

Captured by claude-story-site. Status: captured. Operator's own account: web servers off for 13 hours, longest outage ever, ~94% of page views served from cache.

- 'we turned off the webservers for all of the wikis hosted by Weird Gloop, until a patch was released 2 hours ago. This 13-hour downtime was the longest outage we've ever had'; 'about 94% of wiki pageviews serving correctly, even with no database or PHP running'.

- Opinion: 'probably the most significant security vulnerability in the history of the internet'; expects old PHP forums to have been compromised (no case named).

- About 500 million page views a month, 8 staff.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |
| Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of page views from cachePrimary, and the one outage with a measured cost. [fact timeline →](../../facts/weirdgloop-13h/index.html) | Weird Gloop | confirmed | **A2** Reported●●○○○○ status overstated | 1/1 | [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 94% | Weird Gloop's wiki page views still served during its 13-hour shutdown | confirmed |

## The bytes
capture 20261022T111827Z · HTTP 200 · https://weirdgloop.org/blog/php2shell- `headers.json` 037e837186e2c7a0cba07dfd9d40f13048c890bbaadc11f106846fa944a5be77 1,399 bytes
- `page.html` a3e0b5fe5b1aa03d078a69481cdf944185f03e1dc6c03dc0691a3e5efc114ea3 13,477 bytes
- `provenance.json` fe3b34860b94853f39a64f8004b2d23fc9efb14b15b7b3ea51cfd4a71b44c2f9 966 bytes
- `rendered.html` d5e9b3b80f7c33d96ece63b4e16e9256bc7f05dc61993a9ed6673d64d898e28a 13,486 bytes
- `screenshot.png` 8014b0889ab8777b9c1ef8b2562da1fe3f4c2d0d858c2727dfe7d79acae1ceaa 369,760 bytes
- `text.txt` 6bd492a6220e8eea4b3f89a098f09f546ccd4df2f38848c651a016aa215ae962 4,262 bytes
capture 20261023T080157Z · HTTP 200 · https://weirdgloop.org/blog/php2shell- `headers.json` c5dd775f0cfc5e09754017b41f0ac823475353d4cfd52237b146ed48608d8371 1,461 bytes
- `page.html` d974a801e093822c24a502653b6df2c3dec5197feba2f37adf88049822948d3d 13,480 bytes
- `provenance.json` 455402873ad13afe50b64e46dd937b476e49ec4dddd3e42daa108cacfd2f9fea 1,546 bytes
- `text.txt` 52f0a619f6b077916c97436152c0dbf919eb15c18f189672a30fcecee0827038 4,265 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/weirdgloop-blog-php2shell/index.html
