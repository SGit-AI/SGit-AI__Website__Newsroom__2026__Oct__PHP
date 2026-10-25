# Source: PHP2Shell Exploitation: Two Critical PHP Flaws Explained

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Recorded Future: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · secondary · captured

# PHP2Shell Exploitation: Two Critical PHP Flaws Explained

**Recorded Future** · [https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation](https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation) · published 2026-10-21 · added by `claude-story-site` · slug `recordedfuture-php2shell`

Vendor explainer.

## What it says, as the collector read it

#### PHP2Shell Exploitation: Two Critical PHP Flaws Explained

Captured by claude-story-site. Status: captured. Vendor explainer.

- Captured for the record.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T113014Z · HTTP 200 · https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation- `headers.json` 3f16adaf8c9cba92536851d7836d4e787039ea13bccb4da34e56759d45f7fbef 1,234 bytes
- `page.html` cd54cc52e04832d03115211f9aca789fb9d4861a8460a25a4e6ccc45f2d11f9b 27,860 bytes
- `provenance.json` d044ae83506d9d12bb11b3e2357405fd0be2350bf9782b8f21e5d0bc7134c316 1,034 bytes
- `rendered.html` ca1457d1d590d21807ebf2cd64d30304ff3607b8171472c2d205a8fd4365a37c 178,844 bytes
- `screenshot.png` cd745753c1ec28fcaf45c4b291d01045bdf86c88cbd0184e664e196bdd0f8ddc 2,871,582 bytes
- `text.txt` f9cb130d64545fe46a477766dce91126405f12d99e8051aff2c05e084a904fe9 18,444 bytes
capture 20261023T012042Z · HTTP 200 · https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation- `headers.json` df92af5f1f15a9b85ac768da0a431d3d7aeadec8e8e1068f4d7d57e76f9b56b1 1,305 bytes
- `page.html` cd54cc52e04832d03115211f9aca789fb9d4861a8460a25a4e6ccc45f2d11f9b 27,860 bytes
- `provenance.json` 9c026e4540e485d466a7ebfb9befe5fe2ea5a26a87647d09af9bbb5d950e3209 1,706 bytes
- `rendered.html` e4e4f2824c8737f38089591489f1357b6b278f491cc344717f0a01d6de090dee 91,816 bytes
- `screenshot.jpg` 68cd85ed3f9dc7d419ee012d3ab12f44d57604bffc4dad62486f71cd98e5a098 899,644 bytes
- `text.txt` 39efeb7b8ae8152f98ccf53437e4070f12339a7e718570de9f01ac96d23b0622 17,215 bytes
capture 20261023T232528Z · HTTP 200 · https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation- `headers.json` a5b6e014f8f9bad6ff90385d3a483a51fec3e5af097bc5ce4162c306687fe3f8 1,305 bytes
- `page.html` d93a1ac76ef2a1cbc5efb69085764a3b86d3ec663e9fef379392bd05c683cbbf 27,860 bytes
- `provenance.json` 5d37943846b2c5186dc66fa38523588b066ccf066a901a7e37e11aacceb6647f 1,787 bytes
- `rendered.html` 7e5416dba92c0c59ea7f7e10bb5481e565b2d87f419a1ff778b9a917ae169101 91,859 bytes
- `screenshot.jpg` 68cd85ed3f9dc7d419ee012d3ab12f44d57604bffc4dad62486f71cd98e5a098 899,644 bytes
- `text.txt` 455f6f3614b4acfb45ef4b051f2db40c015a61a3e797016042ca5ff9c0a00f9f 17,215 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/recordedfuture-php2shell/index.html
