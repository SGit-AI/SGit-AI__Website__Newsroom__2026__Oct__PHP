# Source: PHP: Global scramble to fix critical cyber-security flaws as many websites taken offline - follow live

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

BBC News: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news-live · secondary · captured

# PHP: Global scramble to fix critical cyber-security flaws as many websites taken offline - follow live

**BBC News** · [https://www.bbc.co.uk/news/live/ckgel5xp2xv9t](https://www.bbc.co.uk/news/live/ckgel5xp2xv9t) · published 2026-10-22T06:16:24Z · added by `claude-newsroom-lead` · slug `bbc-live-ckgel5xp2xv9t`

Live page; bbc.co.uk redirects to bbc.com. raw/ holds a curl copy at 07:55Z and its __INITIAL_DATA__. Captures 080453Z and 080526Z have no raw body (the tool's first fallback was blocked by egress); 080559Z is complete. Edited by Kieran Kelly and Imogen James.

## What it says, as the collector read it

#### BBC News live page: notes

- URL: https://www.bbc.co.uk/news/live/ckgel5xp2xv9t, which redirects to https://www.bbc.com/news/live/ckgel5xp2xv9t

- Live since 2026-10-22T06:16Z (seoTimestamps.firstPublished 06:16:24.321Z); edited by Kieran Kelly and Imogen James

- First copy at 07:55Z (curl): 12 posts, 07:15 to 08:50 BST. See `extracted-text.md`.

- The 08:00 BST post appeared after 07:55Z: "No evidence that hackers have exploited flaw so far, says researcher" (Ryan Austin, Calif).

#### Claims attributed here (follow each to its primary source)

- PHP Foundation: coordinated disclosure "worked well" until a leak; Calif "mistakenly published a video". Find the foundation's statement.

- OpenAI "Patch the Planet" initiative; the PHP Foundation was accepted in July 2026. Find OpenAI's blog post.

- Calif found the flaw in August; OpenAI and Wiz found it independently shortly after. Find the Calif and Wiz posts.

- Wiz: "roughly 70%" of the internet affected. The BBC could not verify this.

- Woodward: "something like 30 million websites"

- NSA cyber (X post): "two critical vulnerabilities". Take offline if an update is not feasible.

- NCSC note: "Where immediate remediation is not feasible, organisations should consider taking the system offline". Also EU and Australian counterparts.

- Amazon and Cloudflare saw probing (Woodward). Find Cloudflare's or AWS's own statement.

- Affected: Wikipedia (parts taken down), Edinburgh council, French government sites, the University of Geneva (header image), online shops, the BBC.

- In 2024 PHP Foundation researchers found a theoretical flaw they could not exploit.

- Not in the blog: CVE IDs, affected versions or SAPIs, the patched releases. Get these from php.net.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. [fact timeline →](../../facts/scale-70pc-internet/index.html) | Wiz (headline, X post); the BBC, which reports it as Wiz's 'roughly 70%' | unverified | **A1** Weak signal●○○○○○ measures differently | 2/3 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Something like 30 million websites could be affectedNo basis given. [fact timeline →](../../facts/scale-30m/index.html) | Alan Woodward, via the BBC | reported | **A2** Reported●●○○○○ | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. [fact timeline →](../../facts/ai-found/index.html) | BBC; OpenAI; Calif; Wiz | reported | **A3** Echoed●●●○○○ opinion measures differently | 3/4 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| The most severe flaws ever detected by AIWiz's own wording is 'among the most severe vulnerabilities discovered in PHP, and arguably in software history'. OpenAI: 'one of the most impactful vulnerabilities in recent memory'. [fact timeline →](../../facts/most-severe/index.html) | BBC attributing Wiz | reported | **A2** Reported●●○○○○ opinion measures differently | 1/2 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'Calif's own page does not mention a leak or a deleted video; it embeds two demo videos. Whether one of them is the deleted video is unknown. [fact timeline →](../../facts/leak-video/index.html) | PHP Foundation | reported | **A3** Echoed●●●○○○ | 3/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../sources/calif-php2shell/index.html) |
| The flaws were disclosed on 22 October 2026Primary sources put the release at 21 October: GHSAs 13:34Z, tags 13:35Z, CVE records 13:48Z and 13:54Z, GitHub release 14:06Z. [fact timeline →](../../facts/disclosure-22oct/index.html) | BBC framing (UK morning coverage) | contradicted | refuted measures differently | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) |
| There is no evidence yet that hackers have exploited the flaw [fact timeline →](../../facts/no-exploitation/index.html) | Ryan Austin, Calif, on Radio 4, 08:00 BST 22 October | reported | **A2** Reported●●○○○○ disputed | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | **A5** Confirmed●●●●●○ | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| Criminals are using AI to 'vibe code' an attack method [fact timeline →](../../facts/vibe-code/index.html) | unnamed researchers, via the BBC | unverified | **A1** Weak signal●○○○○○ opinion | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. [fact timeline →](../../facts/offline-ncsc/index.html) | UK NCSC, as quoted by the BBC | disputed | **A2** Reported●●○○○○ disputed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CCCS](../../sources/cccs-al26-026/index.html) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | **A1** Weak signal●○○○○○ | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. [fact timeline →](../../facts/affected-sites/index.html) | BBC | reported | **A2** Reported●●○○○○ | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2024 | Quarkslab audits PHP (funded through OSTIF and the Sovereign Tech Agency). While fixing one of its findings a PHP core developer finds the first signs of the out-of-memory problem behind CVE-2026-109618; an exploit is theorised but no vector found, so it is not fixed. | stated |
| 2026-10-22 06:16:24 UTC | BBC News opens its live page: 'Global scramble to fix critical cyber-security flaws as many websites taken offline'. | stated |
| 2026-10-22 06:55:50 UTC | The BBC reports the NSA's X post. | stated |
| 2026-10-22 07:00 UTC | Ryan Austin on BBC Radio 4: no evidence of exploitation yet. | stated |
| 2026-10-22 08:03 UTC | The evidence vault behind this site is opened; the first capture of the BBC live page is at 08:04:53Z. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| about 30 million | websites | reported |

### Exploitation signals from this source
- [2026-10-22 07:00 UTC](../../exploitation/index.html): No evidence of exploitation yet: 'Not at the moment'.
- [2026-10-22](../../exploitation/index.html): Amazon and Cloudflare saw sites being probed for the flaw.
- [2026-10-22](../../exploitation/index.html): Criminals are using AI to 'vibe code' an attack method.

## The bytes
capture 20261022T080453Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` 6f92f9cc2df7e178c6a5480cde0a0d07eaa057374c17573ed0539cd2ec5e4f76 5,640 bytes
- `page.html` dc9a4c45bac2ffecb6c3904ab17c14f29288f0928f0247acd449f62d0b715981 24 bytes
- `provenance.json` de7ccc50e0cd85c96d0c814a87e22d61df580452ccc7cc08bec00fe2acb36000 1,094 bytes
- `rendered.html` e9ae7f01673df9b32a99007f255c2106bc6f4179841891af83732ce54cac1bde 500,416 bytes
- `screenshot.png` a466ce380b452e0a851e07db1d769f1ccb1b41391a8bf001b5febe1a6b0a8352 2,737,568 bytes
- `text.txt` df1dbe6b553a8c004f6d950a1d606138f2795062d3225feaa37043d24343bc99 14,389 bytes
capture 20261022T080526Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` d63c60c458f9e0144dfc1ec7336b7e7eb13ac35383008623841bf01030b99175 5,690 bytes
- `page.html` dc9a4c45bac2ffecb6c3904ab17c14f29288f0928f0247acd449f62d0b715981 24 bytes
- `provenance.json` b0b6c73c98d7b9af8e3cea8a007eb2212d89e38f80d8fdcb1c99b32cac545a18 1,094 bytes
- `rendered.html` b42a90b0ed17266eac83cb8bc81fc6e2321285b3b3dd01c15aed55411ec51255 511,866 bytes
- `screenshot.png` 65eb8a2dd5d93f8ef2399b62dd91d4bae200c41997a77ccae9b9388d33c505bf 3,587,122 bytes
- `text.txt` 9ae96265aa96cff67f4da71f5ed410376023b17283d83b617eab7e98d2602738 14,501 bytes
capture 20261022T080559Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` adef455045234df0fcb6936e0b86ce89d83c6b68719892c1e08bc498d0704517 5,647 bytes
- `page.html` 50bc0fc20681b834b1a40742cf921b27ceb5356d5ab38b417c7e53513016eefd 501,921 bytes
- `provenance.json` b62c78eb8ac92bd2d3d7bbd6749e8f0c24519b5d2edac76d107af558eaf78d2f 1,092 bytes
- `rendered.html` 8ae9c4bca9c7ff8b5037ffa58536c2b75c45efdee1f851d583a80ac5cd05ff5c 501,515 bytes
- `screenshot.png` f3cf0359a5f9aec2edf5dfa6cd060f55f94aa3c64b90f7e260edec02180a434c 2,685,632 bytes
- `text.txt` c88b8c5f4c6bc07d2ef85b78d0d66482f0322075621abb0631ef4352932aa97d 14,389 bytes
raw, 2 files with SHA256SUMS- `initial-data.json` ee7445a58187bcd67df827007a8100941993a24dc3e7eea7e8a45f723a9e3305
- `page.2026-10-22T0755Z.html` fe32274b64ee109a7e37fc4c26e37e793dc22481a6122888782c393e01102488

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/bbc-live-ckgel5xp2xv9t/index.html
