# Every claim, with its status and sources

49 claims about php2shell, each with who makes it, a status (confirmed, reported, disputed, contradicted or unverified) and the captured sources behind it.

# Every claim, and who makes it

49 claims: 13 confirmed, 22 reported, 8 disputed, 3 contradicted, 3 unverified. A claim is a sentence somebody said, with the party that said it, the captured sources it comes from, and one of five words for how far it can be trusted. The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.

- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it

## The flaws themselves

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 | PHP Group (CNA), GitHub advisories, php.net | confirmed | [CVE record](../sources/index.html#cve-cve-2026-109618) [CVE record](../sources/index.html#cve-cve-2026-109619) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [php.net](../sources/index.html#php-net-advisory) |
| The flaws are CVSS 10.0The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily. | social posts on 20 October, relayed by a vendor and a news site | contradicted | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) |
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs | PHP security team (GHSA, oss-security), php.net | confirmed | [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [oss-security](../sources/index.html#openwall-oss-security-2026-10-21-6) [php.net](../sources/index.html#php-net-advisory) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. | PHP Foundation blog; GHSA-6wmf for the session path | disputed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [oss-security](../sources/index.html#openwall-oss-security-2026-10-21-6) |
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' | PHP security team | confirmed | [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [php.net](../sources/index.html#php-net-changelog-8) [php-src](../sources/index.html#github-php-src-branch-7.4-backport) |
| The 8.5.12 fix may be incomplete, or there is a third, different bugPer a Matrix channel, Canonical asked PHP and 'was told that it's unrelated and not a real issue'. Second-hand. Nothing from PHP on the list at capture. | Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez | unverified | [oss-security](../sources/index.html#openwall-oss-security-109619-thread) |
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | [NCSC-NL](../sources/index.html#ncsc-nl-advisories) [Wiz on X](../sources/index.html#x-wiz-io-php2shell) [CERT-FR](../sources/index.html#certfr-2026-ale-014) [oss-security](../sources/index.html#openwall-oss-security-109619-thread) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe | php.net; PHP security team | confirmed | [php.net](../sources/index.html#php-net-advisory) [oss-security](../sources/index.html#openwall-oss-security-2026-10-21-7) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) |
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. | CISA | disputed | [CISA](../sources/index.html#cisa-alert-php-20261021) [BACS](../sources/index.html#ch-bacs-warnung-php) [Cloudflare](../sources/index.html#cloudflare-blog-php2shell-waf) |
| Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCSTwo researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded. | Calif; Wiz for WordPress and Drupal | reported | [Calif](../sources/index.html#calif-php2shell) [Wiz](../sources/index.html#wiz-blog-php2shell) |

## How big it is

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| Roughly 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. | Wiz (headline, X post); BBC attributing Wiz | unverified | [Wiz](../sources/index.html#wiz-blog-php2shell) [Wiz on X](../sources/index.html#x-wiz-io-php2shell) [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| PHP is used by almost 70% of websitesNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | [Cloudflare](../sources/index.html#cloudflare-blog-php2shell-waf) [OpenAI on X](../sources/index.html#x-openai-php2shell) [Wiz](../sources/index.html#wiz-blog-php2shell) |
| Something like 30 million websites could be affectedNo basis given. | Alan Woodward, via the BBC | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| PHP is exposed on 2,608,039 internet-facing hosts | VulnCheck, via The Hacker News | reported | [THN](../sources/index.html#thehackernews-php2shell-4days) |
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. | CERT.LV | reported | [CERT.LV](../sources/index.html#certlv-php-preventive) |
| 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerableCounted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'. | NCSC-NL, counted by this site from the file at commit cca173c64ec5 | confirmed | [NCSC-NL](../sources/index.html#ncsc-nl-php2shell-software-list) |

## Who found it, and how

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. | BBC; OpenAI; Calif; Wiz | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [OpenAI on X](../sources/index.html#x-openai-php2shell) [Calif](../sources/index.html#calif-php2shell) [Wiz](../sources/index.html#wiz-blog-php2shell) |
| Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 AugustThe hash tweet is dated 5 August 2026 on X; its pre-image has not been published, so what it commits to cannot be checked. | Calif; PHP Foundation (report date) | confirmed | [Calif](../sources/index.html#calif-php2shell) [Ryan Austin , Calif on X](../sources/index.html#x-lcfr-hax-hash-tweet) [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) |
| OpenAI independently reported the same root cause on 11 August, with further vectors on 18 SeptemberThe GitHub advisories credit amyb-oai among four reporters. OpenAI's own post credits Calif's discovery 'using GPT-5.6 Sol' and Wiz; an X Community Note disputes OpenAI's role. | PHP Foundation | reported | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) |
| Wiz Research independently discovered the first flaw on 19 August and reported on 24 AugustWiz's X post says 'Wiz Research uncovers' with no credit to Calif or OpenAI; the blog thanks both. | Wiz; PHP Foundation (24 August) | reported | [Wiz](../sources/index.html#wiz-blog-php2shell) [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. | GitHub security advisories | confirmed | [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) |
| The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixedTwo parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does. | PHP Foundation; Calif | confirmed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [Calif](../sources/index.html#calif-php2shell) |
| Frontier AI found the flaw ahead of attackers, giving defenders time to prepareAmazon reports an exploit attempt against a honeypot on 17 October, four days before disclosure, from an actor whose source of exploit information is unknown. | OpenAI | disputed | [OpenAI on X](../sources/index.html#x-openai-php2shell) [THN](../sources/index.html#thehackernews-php2shell-4days) |
| The most severe flaws ever detected by AIWiz's own wording is 'among the most severe vulnerabilities discovered in PHP, and arguably in software history'. OpenAI: 'one of the most impactful vulnerabilities in recent memory'. | BBC attributing Wiz | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [Wiz](../sources/index.html#wiz-blog-php2shell) |

## The leak

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong release time and a wrong CVSS score; no technical details leakedPrimary party. The Foundation does not say who or where. | PHP Foundation | reported | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [PHP Foundation](../sources/index.html#phpfoundation-blog-security-release-leak) |
| The leak started with an anonymous Hacker News post citing a reliable source, which came down after screenshots spread; a screenshot of the 'PHP2Shell tool' credited to Calif.io and a short exploitation video also went up and came downContradicts the Foundation's 'no technical details leaked' and The Hacker News's 'a proof-of-concept exploit leaked'. No copy of the post, screenshot or video is in the vault. | Alexandre Daubois (PHP security team, personal blog) | reported | [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) |
| watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release | Daubois; CERT-EU lists a watchTowr X post among public reports | reported | [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) [CERT-EU](../sources/index.html#certeu-sa-2026-018) |
| Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'Calif's own page does not mention a leak or a deleted video; it embeds two demo videos. Whether one of them is the deleted video is unknown. | PHP Foundation | reported | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [PHP Foundation](../sources/index.html#phpfoundation-blog-security-release-leak) [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [Calif](../sources/index.html#calif-php2shell) |
| Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on 20 October may have leaked | PHP Foundation | reported | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) |
| Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the fixChainguard reportedly does not dispute the time but denies leaking (Techzine, blocked by a bot challenge; snippet only). | PHP Foundation | disputed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [Techzine](../sources/index.html#techzine-php-chainguard) |
| The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leakThe php.net ChangeLog still dates all four releases 22 October. Wiz's X thread still says 22 October. | PHP Foundation; php.net pre-announcement; Wiz thread ('Apply the Oct 22 security release') | confirmed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [oss-security](../sources/index.html#openwall-oss-security-2026-10-20-34) [Wiz on X](../sources/index.html#x-wiz-io-php2shell) [php.net](../sources/index.html#php-net-changelog-8) |

## When things happened

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| The flaws were disclosed on 22 October 2026Primary sources put the release at 21 October: GHSAs 13:34Z, tags 13:35Z, CVE records 13:48Z and 13:54Z, GitHub release 14:06Z. | BBC framing (UK morning coverage) | contradicted | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [php.net](../sources/index.html#php-net-advisory) [php-src](../sources/index.html#github-php-src-tag-php-8.5.12) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | [oss-security](../sources/index.html#openwall-oss-security-2026-10-20-34) [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) [CERT-FR](../sources/index.html#certfr-2026-ale-014) [CERT-EU](../sources/index.html#certeu-sa-2026-018) [php-src](../sources/index.html#github-php-src-tags) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [php-src](../sources/index.html#github-php-src-tag-php-8.5.12) [php.net](../sources/index.html#php-net-advisory) |
| The pre-announcement was published at 19:30 UTC on 20 OctoberThe php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC, so it was public by then. | PHP Foundation | disputed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [oss-security](../sources/index.html#openwall-oss-security-2026-10-20-34) [php.net](../sources/index.html#php-net-advisory) |

## Exploitation

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| There is no evidence yet that hackers have exploited the flaw | Ryan Austin, Calif, on Radio 4, 08:00 BST 22 October | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. | CISA | confirmed | [CISA](../sources/index.html#cisa-alert-php-20261021) [CISA](../sources/index.html#cisa-kev-json) [CVE record](../sources/index.html#cve-cve-2026-109618) |
| Reports of active exploitation existThe only agency saying so, and it does not say whose reports. | NCSC New Zealand | reported | [NCSC New Zealand](../sources/index.html#ncsc-nz-alert-php) |
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, and proof-of-concept attempts started about 02:00 UTC on 21 OctoberAmazon's own post has not been found. | CJ Moses, Amazon, via The Hacker News | reported | [THN](../sources/index.html#thehackernews-php2shell-4days) |
| Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloadsPrimary party, no volumes. | Cloudflare | reported | [Cloudflare](../sources/index.html#cloudflare-blog-php2shell-waf) |
| Amazon and Cloudflare saw sites being probed for the flawSecond-hand, but consistent with what both companies have said themselves. | Alan Woodward, via the BBC | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [Cloudflare](../sources/index.html#cloudflare-blog-php2shell-waf) [THN](../sources/index.html#thehackernews-php2shell-4days) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. | CERT.LV | reported | [CERT.LV](../sources/index.html#certlv-php-preventive) |
| Criminals are using AI to 'vibe code' an attack method | unnamed researchers, via the BBC | unverified | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) |

## What the agencies advise

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| If an immediate update is not feasible, take the system offline until it can be fully mitigatedX post 13:45:58Z 21 October (10.1 million views at capture) and the press release. | NSA Cybersecurity | confirmed | [NSA Cyber on X](../sources/index.html#nsa-x-2112903220209098897) [NSA](../sources/index.html#nsa-press-php-4630238) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline | CISA | confirmed | [CISA](../sources/index.html#cisa-alert-php-20261021) |
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. | UK NCSC, as quoted by the BBC | disputed | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [NCSC UK](../sources/index.html#ncsc-news-php) [CCCS](../sources/index.html#cccs-al26-026) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. | BBC | contradicted | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [ACSC](../sources/index.html#acsc-alert-php) [CERT-EU](../sources/index.html#certeu-sa-2026-018) [NCSC-NL](../sources/index.html#ncsc-nl-php2shell) [ACN / CSIRT Italia](../sources/index.html#acn-it-php2shell) [JPCERT/CC](../sources/index.html#jpcert-at260033) |
| The risks require immediate patching across United States Government departments and agenciesNo CISA emergency directive was visible on the CISA home page at capture. | NSA | reported | [NSA](../sources/index.html#nsa-press-php-4630238) [CISA](../sources/index.html#cisa-home) |

## What was taken offline

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. | BBC | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. | CERT.LV | confirmed | [CERT.LV](../sources/index.html#certlv-php-preventive) |

The newsroom's own twelve claims, seeded from the BBC live page on the morning of 22 October, are in the vault as `claims/claude-newsroom-lead.json` and are superseded by the rows above, which trace each of them to primary sources. The raw rows are in [data/claims.json](../data/claims.json).


---
site v0.1.0 · data as of 2026-10-22T08:48Z · vault commit 379e3d7f172a · https://php.oct-2026.story.sgit.ai/claims/index.html
