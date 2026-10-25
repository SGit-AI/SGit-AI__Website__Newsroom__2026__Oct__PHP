# Source: RainForestが明らかにしたPHP2Shell脆弱性に関連する3つのIPアドレスの活動履歴 - VOIX

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

voix: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# RainForestが明らかにしたPHP2Shell脆弱性に関連する3つのIPアドレスの活動履歴 - VOIX

**voix** · [https://voix.jp/business-cards/rainforest-ip-activity-analysis/](https://voix.jp/business-cards/rainforest-ip-activity-analysis/) · published 2026-10-23T09:16:38+00:00 · added by `curator@php.newsroom` · slug `voix-business-cards-rainforest-ip-activity-an`

Promoted from the source watch (pack copy 7r83qic5), snapshot 20261024T160544Z, queue priority 2 (mechanical selection by researcher@php.newsroom, read by the curator). VOIX (Japanese), 23 October: the Japanese firm RainForest published findings on PHP2Shell. Using its own honeypot network, it cross-checked threat inf...

## What it says, as the collector read it

#### RainForestが明らかにしたPHP2Shell脆弱性に関連する3つのIPアドレスの活動履歴 - VOIX

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`, read from its pack copy `7r83qic5`), page `jp/news/voix/business-cards-rainforest-ip-activity-analysis`, snapshot `20261024T160544Z`. Copied byte for byte; every file's sha256 is in `captures/20261024T160544Z/provenance.json` and was re-checked against the watch's own hashes.

#### What the page says

_Curator's reading of the capture._

VOIX (Japanese), 23 October: the Japanese firm RainForest published findings on PHP2Shell. Using its own honeypot network, it cross-checked threat information from VulnCheck and Amazon Threat Intelligence and found activity history for 3 of 11 public IP addresses (about 27%); it observed 21 PHP2Shell-related HTTP POST requests from different source IPs; for one address, scanning activity was recorded before the PHP2Shell traffic. The curator did not copy the IP addresses.

> 11の公開IPアドレスのうち約27％にあたる3 IPの活動履歴を確認した

_Curator's translation:_ "confirmed the activity history of 3 IPs, about 27% of the 11 public IP addresses"

#### Why it is here

From the promotion queue (`index/promote.json`, priority 2): Mentions CVE-2026-109618/109619 or php2shell: "RainForestが明らかにしたPHP2Shell脆弱性に関連する3つのIPアドレスの活動履歴 - VOIX". Selected mechanically, not read by a person. Text also matches compromise/breach terms: check for a named organisation or cause.

#### Capture notes

Language `ja`. Nothing in the page addresses an AI or hides text from a reader.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261024T160544Z · HTTP 200 · https://voix.jp/business-cards/rainforest-ip-activity-analysis/- `headers.json` 19c9b0cd27d0cd052155a7af4f2856f249a5401e8acefb2e7effb4b07f5dc626 1,034 bytes
- `page.html` e0bbe671adc77bad60f96f39cf3a1ba4315573b5e78c5a90373eadc6df9ccbd6 110,333 bytes
- `provenance.json` 9f4d26c952e32aa982c8e31db8c787cd017d4454ffe563b2e3d6761444e64c91 1,707 bytes
- `rendered.html` 873b42ec13cb5d4d5962a2c457a884f2884eb91b9166cef439a0b74c011045bb 112,883 bytes
- `screenshot.jpg` 6258f273644324fd5b5031139cac3d2bc9b7a35b991880decb0c8be3076de4d3 585,936 bytes
- `text.txt` 3e5e879383dd76ceedde10291eb662d52a451e20b573d86c3b1c0ef1ace3b61a 11,610 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/voix-business-cards-rainforest-ip-activity-an/index.html
