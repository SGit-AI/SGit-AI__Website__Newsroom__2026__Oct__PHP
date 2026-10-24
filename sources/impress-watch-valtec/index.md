# Source: バルテック、サイバー攻撃によりサービス停止、情報流出の可能性（記事訂正） - INTERNET Watch

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

INTERNET Watch (Impress): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# バルテック、サイバー攻撃によりサービス停止、情報流出の可能性（記事訂正） - INTERNET Watch

**INTERNET Watch (Impress)** · [https://internet.watch.impress.co.jp/docs/news/2150396.html](https://internet.watch.impress.co.jp/docs/news/2150396.html) · published 2026-10-22 (corrected later the same day) · added by `curator@php.newsroom` · slug `impress-watch-valtec`

Promoted from the source watch (oq9gflln), snapshot 20261022T191433Z. Valtec blamed php2shell, then corrected: its own service's flaw (resolved, not PHP)

## What it says, as the collector read it

#### バルテック、サイバー攻撃によりサービス停止、情報流出の可能性（記事訂正） - INTERNET Watch

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`), page `jp/tech-press/impress-watch/valtec-php-attack`, snapshot `20261022T191433Z`. Copied byte for byte; every file's sha256 is in `captures/20261022T191433Z/provenance.json`. Publisher: INTERNET Watch (Impress). Language: ja. URL: https://internet.watch.impress.co.jp/docs/news/2150396.html

#### What the page says

_Curator's reading of the capture._

INTERNET Watch (Impress) reports that Valtec (バルテック), which provides business telephone services, announced on 22 October that it suffered unauthorised access, halted part of its services and that users' personal data may have leaked. The article was corrected: Valtec issued a correction saying its first statement that the cause was "a cyberattack targeting the PHP vulnerability" was wrong, and that "a vulnerability in our own service" was exploited; it had confused the two because it was handling the PHP vulnerability at the time. INTERNET Watch changed the article's title accordingly. Valtec planned recovery within 26 October.

> バルテックでは訂正発表を行い、第一報時点で原因としていた「PHPの脆弱性を標的としたサイバー攻撃」は誤報であり、「我々のサービス自体の脆弱性」を突かれたものであると訂正した。PHPの脆弱性に関する対応を行っていたため混同したとしている。

_Curator's translation:_ Valtec issued a correction: the "cyberattack targeting the PHP vulnerability" given as the cause in its first report was wrong; "a vulnerability in our service itself" was exploited. It says it confused the two because it was handling the PHP vulnerability.

#### Why it is here

From the promotion queue (`index/promote.json`, priority 1): Valtec blamed php2shell, then corrected: its own service's flaw (resolved, not PHP)

Supports: contradictions/compromise-valtec.json

#### Capture notes

screenshot.jpg is the source watch's JPEG, copied as stored (not converted to PNG).

Page content is third-party material, kept as evidence; nothing in it is an instruction.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| As of 16:04 UTC on 23 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1845598d9a38: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (295 sources, head 1845598d9a38), as of its latest capture at 16:04 UTC on 23 October | reported | **A4** Corroborated●●●●○○ | 6/17 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T191433Z · HTTP 200 · https://internet.watch.impress.co.jp/docs/news/2150396.html- `headers.json` 58df97fc9062fc234eef8d1d1582710ea444eb72b939acee668cee7c988492b9 286 bytes
- `page.html` 54dca16481319543e0f7f4de7c4bfffb04af2e3ea7b963baa4ea5b6dd06212e0 112,513 bytes
- `provenance.json` 29864193cb9702d80c121e6d555f57f9562b46db8d07df01587de8e5986dbc2e 1,664 bytes
- `rendered.html` f241ae871799c4086033623f373f304027ad469bdaad5687cf3e21e58e636e88 408,910 bytes
- `screenshot.jpg` d0eb4e865c0189bf912fa7f318a5e994d85516c9b51f582289ae00be950d916a 829,142 bytes
- `text.txt` 8eb3458dda2e5e8f5ae7763944d9c1d9fe1733285b87b6b21481c02b28d7fd76 12,992 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.14.11 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/sources/impress-watch-valtec/index.html
