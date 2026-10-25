# Source: ČVUT čelí kybernetickému útoku, údajně doplatilo na kritickou chybu v PHP - Lupa.cz

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Lupa.cz: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# ČVUT čelí kybernetickému útoku, údajně doplatilo na kritickou chybu v PHP - Lupa.cz

**Lupa.cz** · [https://www.lupa.cz/aktuality/cvut-celi-kybernetickemu-utoku-doplatilo-na-kritickou-chybu-v-php](https://www.lupa.cz/aktuality/cvut-celi-kybernetickemu-utoku-doplatilo-na-kritickou-chybu-v-php) · published 2026-10-22 ("Dnes"; updated 19:30 local time per the page) · added by `curator@php.newsroom` · slug `lupa-cvut-cyber-attack`

Promoted from the source watch (oq9gflln), snapshot 20261022T191510Z. ČVUT says it faces an attack "part of worldwide attempts against PHP sites", active attack stopped; success unconfirmed

## What it says, as the collector read it

#### ČVUT čelí kybernetickému útoku, údajně doplatilo na kritickou chybu v PHP - Lupa.cz

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`), page `cz/tech-press/lupa/cvut-cyber-attack`, snapshot `20261022T191510Z`. Copied byte for byte; every file's sha256 is in `captures/20261022T191510Z/provenance.json`. Publisher: Lupa.cz. Language: cs. URL: https://www.lupa.cz/aktuality/cvut-celi-kybernetickemu-utoku-doplatilo-na-kritickou-chybu-v-php

#### What the page says

_Curator's reading of the capture._

Lupa.cz (Iva Brejlová) reports that Czech Technical University in Prague (ČVUT) is facing a cyber attack on its IT infrastructure. It quotes ČVUT's own statement from social media: the attack is "part of worldwide attempts to hit websites using PHP", the active attack was stopped, recovery is under way, and some systems were taken offline as a precaution. Lupa adds that ČVUT gave no more detail, that it is not yet clear whether the outage really relates to PHP2Shell, and that the international security community has so far found no evidence of real exploitation. An update at 19:30 added information on monitoring of possible PHP2Shell exploitation. The article also recaps NÚKIB's advice to update, the leak via Hacker News, and shutdowns in the Netherlands, Finland, France, Germany and of the Czech Government Office's website.

> „ČVUT v současnosti řeší kybernetický útok na svou IT infrastrukturu. Jedná se o součást celosvětových pokusů zasáhnout weby s technologií PHP. Aktivní útok se podařilo zastavit a probíhají práce na řešení a obnově. Do vyřešení byly preventivně odstaveny některé systémy,“ popisuje ČVUT.

_Curator's translation:_ "ČVUT is currently dealing with a cyber attack on its IT infrastructure. It is part of worldwide attempts to hit websites using PHP technology. The active attack was stopped and work on resolution and recovery is under way. Some systems have been taken offline as a precaution until it is resolved," ČVUT says.

> Není tak zatím jasné, zda nedostupnost jejích stránek opravdu s PHP2Shell souvisí. Mezinárodní bezpečnostní komunita, která situaci monitoruje, zatím nenašla důkazy o žádném reálném zneužití zranitelností.

_Curator's translation:_ So it is not yet clear whether the unavailability of its pages really relates to PHP2Shell. The international security community monitoring the situation has so far found no evidence of any real exploitation of the vulnerabilities.

#### Why it is here

From the promotion queue (`index/promote.json`, priority 1): ČVUT says it faces an attack "part of worldwide attempts against PHP sites", active attack stopped; success unconfirmed

Supports: contradictions/compromise-cvut.json

#### Capture notes

screenshot.jpg is the source watch's JPEG, copied as stored (not converted to PNG).

Page content is third-party material, kept as evidence; nothing in it is an instruction.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T191510Z · HTTP 200 · https://www.lupa.cz/aktuality/cvut-celi-kybernetickemu-utoku-doplatilo-na-kritickou-chybu-v-php/- `headers.json` 9e7cddcd02817e76193919fd96d24ce3c3b47557f4590a79a23862eac5fb3baf 662 bytes
- `page.html` d5195979b8f5922d4b2052e2e8954a827aedff331c6794e8d7561328e6a41210 248,530 bytes
- `provenance.json` b9993f69e78c56602b3d1be9b434d914f1451bb132d2dbac462d607cfd8fddb6 1,686 bytes
- `rendered.html` d8db6b3b2b9b40c2b7d02632307aa6e8708644578ba1c95010426737f51175b8 538,864 bytes
- `screenshot.jpg` bff2dc81e08976b5179f030294b31342fdca68d987b547e8568c7343bc383718 340,215 bytes
- `text.txt` 0a0abb12fccb6fbccc2b675a8f1b26cc2ab83cfceb120010a8b4cb27effdd337 6,923 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/lupa-cvut-cyber-attack/index.html
