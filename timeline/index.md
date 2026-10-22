# The timeline, 2024 to the latest capture

68 dated events in the php2shell story, from the 2024 audit through discovery, coordinated disclosure, the leak, the release and the response, every one tied to a captured source.

# The timeline

68 events from the 2024 audit to the latest capture, each dated as its source states it. Times are UTC; where this site converted from a local time, or inferred a date from a phrase such as *two days ago*, the row says so. A row that lists several sources is one that at least two accounts carry; a row with one source is that party's account.

- stated the source states this date or time
- inferred this site worked it out, and the note says how
- disputed the sources give different times

## Origins, 2024 to mid-2026

| When | What | Time is | Sources |
|---|---|---|---|
| 2024 | Quarkslab audits PHP (funded through OSTIF and the Sovereign Tech Agency). While fixing one of its findings a PHP core developer finds the first signs of the out-of-memory problem behind CVE-2026-109618; an exploit is theorised but no vector found, so it is not fixed. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Calif](../sources/calif-php2shell/index.html) [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-06 | OpenAI launches Patch the Planet (a Daybreak initiative with Trail of Bits, HackerOne and Calif).The launch post is blocked; the June date is from a search snippet. The BBC says the PHP Foundation 'joined' in July; the Foundation says it 'got the PHP project into' the programme; Calif says OpenAI invited them. | inferred | [OpenAI](../sources/openai-patch-the-planet-launch/index.html) [OpenAI](../sources/patchtheplanet-org/index.html) |

## Discovery, August 2026

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-07-30 | Calif begins an audit of PHP under Patch the Planet; Volker Dusch accepts the invitation. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Calif](../sources/calif-php2shell/index.html) |
| 2026-08-01 | Calif discovers 'multiple different paths independently leading to RCE that resurfaced the 2024 issues and new trigger points'. | stated | [Calif](../sources/calif-php2shell/index.html) |
| 2026-08-05 15:54 UTC | Ryan Austin (@lcfr_hax) posts a SHA-256 hash on X as a commitment to one finding.Time as displayed in a UTC browser. The pre-image has not been published. | stated | [Ryan Austin , Calif on X](../sources/x-lcfr-hax-hash-tweet/index.html) [Calif](../sources/calif-php2shell/index.html) |
| 2026-08-19 | Wiz Research discovers the first vulnerability using Wiz Atlas, Gemini 4 Argon and GPT-5.6 Sol; confirms RCE against Drupal on 20 August and WordPress on 21 August. | stated | [Wiz](../sources/wiz-blog-php2shell/index.html) |

## Coordinated disclosure, August to 19 October

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-08-11 | Calif reports the first bug to PHP and coordinated disclosure begins. OpenAI independently reports the same root cause the same day. | stated | [Calif](../sources/calif-php2shell/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 2026-08-14 | Calif shares an RCE proof of concept with PHP; PHP confirms it works on 15 August. | stated | [Calif](../sources/calif-php2shell/index.html) |
| 2026-08-21 | Calif reports the second bug to PHP. | stated | [Calif](../sources/calif-php2shell/index.html) |
| 2026-08-24 | Wiz reports to the PHP security team. | stated | [Wiz](../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 2026-08-27 | The GitHub security advisory is opened, credited to lcfr-hax, sagitzadik-wiz, amyb-oai and tomash-areion. | stated | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| 2026-09-18 | Further attack vectors reported by OpenAI. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 2026-09-21 | PHP acknowledges Wiz's reports 'and begins developing a coordinated fix'.Conflicts with the Foundation's account that the fix was the top priority from 11 August. | stated | [Wiz](../sources/wiz-blog-php2shell/index.html) |
| 2026-09-25 | The fix pull request is opened. | stated | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| 2026-10 | Cloudflare starts developing WAF protections 'since early October 2026'. | stated | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| 2026-10-12 21:03:58 UTC | CVE-2026-109618 and CVE-2026-109619 are reserved. | stated | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) |
| 2026-10-18 | The final fix commit is authored; the 7.4 backport branch's commit is dated 18:10:24Z. | stated | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) [php-src](../sources/github-php-src-branch-7.4-backport/index.html) |
| 2026-10-18 15:26:39 UTC | Arnaud Le Blanc authors the fix, 'Avoid state corruption via bailout', with Ilija Tovilo, Jakub Zelenka, Nora Dossche and Nicolas Grekas; the 7.4 minimal backport is authored at 18:09 UTC.Author timestamps from the commits. | stated | [php/php-src , read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |
| 2026-10-19 14:00 UTC | Release commits for 8.5.12, 8.4.27, 8.3.36 and 8.2.35 are made under embargo (14:00 to 17:04 UTC). | stated | [php-src](../sources/github-php-src-tags/index.html) [php-src](../sources/github-php-src-tag-php-8.5.12/index.html) |

## The leak, 17 to 21 October

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-10-17 | An exploit attempt from an anonymisation-network IP hits an Amazon MadPot honeypot.As Amazon's CISO told The Hacker News; no primary Amazon post found. | stated | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| 2026-10-20 | Qualys publishes on the pre-announcement. | stated | [Qualys](../sources/qualys-blog-php-preannounce/index.html) |
| 2026-10-20 15:00 UTC | The two CVE IDs begin circulating on forums and social media with a wrong release time and a wrong CVSS of 10.0. Per Daubois: an anonymous Hacker News post, then screenshots, a 'PHP2Shell tool' screenshot credited to Calif.io, a short exploitation video, and watchTowr posting both CVE numbers.'around 15:00 UTC' per the Foundation. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| 2026-10-20 19:30 UTC | php.net publishes the pre-announcement: release moved to 21 October 14:00 UTC, two critical vulnerabilities, CVSS v4.0 9.2, 'we reserve the right to release earlier'.19:30 UTC per the Foundation; the php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC. | disputed | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [oss-security](../sources/openwall-oss-security-2026-10-20-34/index.html) [php.net](../sources/php-net-advisory/index.html) |
| 2026-10-20 20:00 UTC | Calif 'mistakenly published a video' showing its proof of concept against several targets; copies circulate after it is deleted.'around 20:00 UTC'. Calif's page does not mention it. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../sources/phpfoundation-blog-security-release-leak/index.html) |
| 2026-10-20 20:22:51 UTC | Alan Coopersmith relays the php.net pre-announcement to oss-security. | stated | [oss-security](../sources/openwall-oss-security-2026-10-20-34/index.html) |
| 2026-10-20 23:00 UTC | The PHP project starts giving mitigation advice to a few critical-infrastructure providers; it 'may have leaked as well'. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 2026-10-21 02:00 UTC | Amazon sees proof-of-concept attempts, then six hours of attempts from anonymised infrastructure. | stated | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| 2026-10-21 07:41 UTC | Chainguard publishes built images containing the fix, 'more than six hours before the coordinated release'.Chainguard reportedly denies leaking; that article is blocked. | stated | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Techzine](../sources/techzine-php-chainguard/index.html) |
| 2026-10-21 07:43 UTC | Cloudflare's CTO reports early attacks emerging, before the release.Second-hand; the post itself is not captured. | stated | [Insurance Business](../sources/insurancebusiness-uk-councils-met/index.html) [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) |
| 2026-10-21 08:36 UTC | ELLIO records its first sensor hit. | stated | [THN](../sources/thehackernews-php2shell-4days/index.html) [PHP Foundation](../sources/phpfoundation-blog-security-release-leak/index.html) |

## The release, 21 October 13:30 to 14:44 UTC

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-10-21 13:30 UTC | CERT-EU's stated release time for the PHP fixes.Differs from the planned 14:00 UTC and from the 13:35 UTC tags. | stated | [CERT-EU](../sources/certeu-sa-2026-018/index.html) |
| 2026-10-21 13:32 UTC | Wiz posts 'BREAKING ... #PHP2SHELL ... impacting 70% of the Internet', 28 minutes before the planned release; the thread still says 'Apply the Oct 22 security release'. | stated | [Wiz on X](../sources/x-wiz-io-php2shell/index.html) |
| 2026-10-21 13:34:13 UTC | GHSA-6wmf-4rv5-p3rp (CVE-2026-109619) and, twelve seconds later, GHSA-w8hw-w9fx-j79w (CVE-2026-109618) are published by bukka. | stated | [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| 2026-10-21 13:35:38 UTC | Signed tags php-8.5.12, php-8.4.27, php-8.3.36 and php-8.2.35 are created. | stated | [php-src](../sources/github-php-src-tags/index.html) |
| 2026-10-21 13:48:34 UTC | The CVE record for CVE-2026-109618 is published; CVE-2026-109619 follows at 13:54:43Z. | stated | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) |
| 2026-10-21 14:00 UTC | The planned release time. php.net's advisory 'Critical remote code execution vulnerabilities, update now' and the four release posts go up. | stated | [php.net](../sources/php-net-advisory/index.html) [oss-security](../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| 2026-10-21 14:04 UTC | OpenAI posts: models 'helped researchers ... discover critical security flaws in PHP ... used to run an estimated 70% of websites'. An X Community Note later disputes OpenAI's role. | stated | [OpenAI on X](../sources/x-openai-php2shell/index.html) |
| 2026-10-21 14:06:22 UTC | The fix commit enters the public php-src branches (commit timestamp); merged into 8.3 at 14:12, 8.4 at 14:27 and 8.5 at 14:30 UTC. | stated | [php/php-src , read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |
| 2026-10-21 14:06:46 UTC | GitHub release php-8.5.12 is published by adoy. | stated | [php-src](../sources/github-php-src-tag-php-8.5.12/index.html) |
| 2026-10-21 14:17:09 UTC | NVD publishes both CVEs with the CNA's CVSS v4.0 9.2 and no NIST score. | stated | [NVD](../sources/nvd-cve-2026-109618/index.html) [NVD](../sources/nvd-cve-2026-109619/index.html) |
| 2026-10-21 14:41:54 UTC | Jakub Zelenka announces CVE-2026-109618 on oss-security; CVE-2026-109619 at 14:44:06Z. | stated | [oss-security](../sources/openwall-oss-security-2026-10-21-6/index.html) [oss-security](../sources/openwall-oss-security-2026-10-21-7/index.html) |

## The response, 20 to 22 October

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-10-20 | Swiss BACS posts a warning (home-page teaser dated 20 October; the page itself now says 21 October). | inferred | [Swiss BACS](../sources/ch-ncsc-home/index.html) [BACS](../sources/ch-bacs-warnung-php/index.html) |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts.Date only; none of these pages carries a time. | stated | [CISA](../sources/cisa-alert-php-20261021/index.html) [NSA](../sources/nsa-press-php-4630238/index.html) [NCSC UK](../sources/ncsc-news-php/index.html) [CCCS](../sources/cccs-al26-026/index.html) [CERT-FR](../sources/certfr-2026-ale-014/index.html) [ACN / CSIRT Italia](../sources/acn-it-php2shell/index.html) [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) [Calif](../sources/calif-php2shell/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated | [Rijksoverheid / NCSC-NL](../sources/rijksoverheid-ncsc-php-news/index.html) [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) [Amazon](../sources/aws-security-blog-madpot/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) [Fastly](../sources/fastly-blog-php2shell/index.html) [Akamai Security Research](../sources/akamai-blog-php-core-rce/index.html) [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| 2026-10-21 03:02 UTC | Cloudflare's WAF protections go live for all customers, about nine hours ahead of disclosure. | stated | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| 2026-10-21 09:45 UTC | Finland's Valtori begins restricting public traffic to government web services (12:45 local).Converted from Finnish time. | inferred | [Helsinki Times](../sources/helsinkitimes-finland-shutdown/index.html) [Yle](../sources/yle-finland-government-sites-shut/index.html) |
| 2026-10-21 13:45:58 UTC | NSA Cybersecurity posts on X: 'Effective Immediately ... be prepared for an update addressing two critical vulnerabilities ... take the system offline'.Time decoded from the post's ID; the page shows 13:45. | stated | [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) |
| 2026-10-21 14:04:39 UTC | CISA releases KEV catalog version 2026.10.21; neither PHP CVE is in it. | stated | [CISA](../sources/cisa-kev-json/index.html) |
| 2026-10-21 14:34 UTC | CISA's ADP assessment on both CVE records: exploitation none, automatable no, technical impact total. | stated | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) |
| 2026-10-21 15:20 UTC | CERT-EU Security Advisory 2026-018 (stated 15:20:18, timezone not given). | inferred | [CERT-EU](../sources/certeu-sa-2026-018/index.html) |
| 2026-10-21 15:25 UTC | NCSC-NL's php2shell README last significant change (17:25 CEST). CERT.LV publishes: Latvia restricts access to several state digital resources from abroad (18:25 EEST).Both converted to UTC by this site. | stated | [NCSC-NL](../sources/ncsc-nl-php2shell/index.html) [CERT.LV](../sources/certlv-php-preventive/index.html) |
| 2026-10-21 20:00 UTC | CERT.LV update: the unified state website platform is patched; lsm.lv and 112.lv restored; about 6,000 potentially affected resources in Latvia; automated attempts seen, none successful. | stated | [CERT.LV](../sources/certlv-php-preventive/index.html) |
| 2026-10-21 20:15 UTC | NCSC New Zealand: 'aware of reports of active exploitation' (09:15 NZDT 22 October; updated 21:20Z).Converted from NZDT. | stated | [NCSC New Zealand](../sources/ncsc-nz-alert-php/index.html) |
| 2026-10-22 00:43:58 UTC | NSA Cybersecurity posts 'UPDATE: Specific mitigation guidance ... is now available', linking the press release. | stated | [NSA Cyber on X](../sources/nsa-x-2113068811058622971/index.html) [NSA](../sources/nsa-press-php-4630238/index.html) |
| 2026-10-22 05:20 UTC | JVN publishes its note (14:20 JST); JPCERT/CC alert JPCERT-AT-2026-0033 is dated 22 October. | stated | [JPCERT/CC](../sources/jpcert-home/index.html) [JPCERT/CC](../sources/jpcert-at260033/index.html) |

## Aftermath, 21 to 22 October

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-10-21 15:24:37 UTC | Aaron Rainbolt relays to oss-security a Fediverse report that the 8.5.12 fix may be incomplete; a Debian maintainer adds that the poster called it a different bug. | stated | [oss-security](../sources/openwall-oss-security-109619-thread/index.html) |
| 2026-10-21 17:29 UTC | Per a Matrix channel, Canonical asked PHP about the Fediverse report and was told it is 'unrelated and not a real issue'.Second-hand. | stated | [oss-security](../sources/openwall-oss-security-109619-thread/index.html) |
| 2026-10-21 20:30 UTC | Huntress: no exploitation observed on partner systems (16:30 ET).Converted from Eastern time. | stated | [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| 2026-10-22 | The Hacker News publishes Amazon's account of the 17 October honeypot attempt and VulnCheck's count of 2,608,039 hosts. | stated | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| 2026-10-22 | The Register carries Dan Lorenc's reply to the PHP Foundation; Fortinet publishes FortiWeb signatures; The Record carries the Foundation's account of the 2024 signs. | stated | [The Register](../sources/theregister-php-blames-chainguard/index.html) [Fortinet Community](../sources/fortinet-fortiweb-php2shell/index.html) [The Record](../sources/therecord-php-foundation-statement/index.html) |
| 2026-10-22 01:25 UTC | Matthew Prince posts Cloudflare's attempt counts: thousands before, millions after. | stated | [Matthew Prince , Cloudflare CEO on](../sources/x-eastdakota-php2shell-stats/index.html) |
| 2026-10-22 06:16:24 UTC | BBC News opens its live page: 'Global scramble to fix critical cyber-security flaws as many websites taken offline'. | stated | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 06:45:47 UTC | Greenbone on oss-security: the backports imply versions down to 7.4 are affected, whatever the subject line says. | stated | [oss-security](../sources/openwall-oss-security-109619-thread/index.html) |
| 2026-10-22 06:55:50 UTC | The BBC reports the NSA's X post. | stated | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 07:00 UTC | Ryan Austin on BBC Radio 4: no evidence of exploitation yet.08:00 BST post. | stated | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 07:30:02 UTC | The UK NCSC page is modified (HTTP last-modified). | stated | [NCSC UK](../sources/ncsc-news-php/index.html) |
| 2026-10-22 08:40:58 UTC | NCSC-NL merges pull request 10; the inventory has 674 entries at commit cca173c64ec5. | stated | [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell/index.html) |

## This site

| When | What | Time is | Sources |
|---|---|---|---|
| 2026-10-22 08:03 UTC | The evidence vault behind this site is opened; the first capture of the BBC live page is at 08:04:53Z. | stated | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |

The sequence as a graph of who said what first is on [Who found it](../discovery/index.html); the leak alone is on [How disclosure broke](../leak/index.html).


---
site v0.2.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/timeline/index.html
