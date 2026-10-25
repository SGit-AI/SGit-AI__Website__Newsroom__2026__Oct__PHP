# National agencies (NSA, CISA, NCSC UK, CERT-EU, CERT-FR, CCCS, ACSC, NCSC NZ, NCSC-NL, ACN, BACS, CERT.LV, JPCERT): what they say

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

National agencies (NSA, CISA, NCSC UK, CERT-EU, CERT-FR, CCCS, ACSC, NCSC NZ, NCSC-NL, ACN, BACS, CERT.LV, JPCERT): advisories; see the agency table; the claims this site attributes to them and their sources.

Party

# National agencies (NSA, CISA, NCSC UK, CERT-EU, CERT-FR, CCCS, ACSC, NCSC NZ, NCSC-NL, ACN, BACS, CERT.LV, JPCERT)

advisories; see the agency table

## Claims this site attributes to this party

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. [fact timeline →](../../facts/waf/index.html) | CISA | disputed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. [fact timeline →](../../facts/scale-latvia/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerableCounted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'. [fact timeline →](../../facts/scale-ncsc-nl/index.html) | NCSC-NL, counted by this site from the file at commit cca173c64ec5 | confirmed | **A1** Weak signal●○○○○○ contradicted status overstated | 1/1 | [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html) |
| watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release [fact timeline →](../../facts/leak-watchtowr/index.html) | Daubois; CERT-EU lists a watchTowr X post among public reports | reported | **A4** Corroborated●●●●○○ | 1/2 | [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. [fact timeline →](../../facts/cisa-none/index.html) | CISA | confirmed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. [fact timeline →](../../facts/latvia-attempts/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline [fact timeline →](../../facts/offline-cisa/index.html) | CISA | confirmed | **A6** Established●●●●●● | 1/1 | [CISA](../../sources/cisa-alert-php-20261021/index.html) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. [fact timeline →](../../facts/latvia-offline/index.html) | CERT.LV | confirmed | **A6** Established●●●●●● | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayThe KEV dates are counted from the captured catalog; 'exploited in the wild one day after disclosure' rests on Akamai alone. [fact timeline →](../../facts/kev-precedent/index.html) | CISA KEV catalog; Akamai (2024) | reported | **A2** Reported●●○○○○ | 3/3 | [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |

## Its sources in the vault
- [NSA Advisory: Critical Patches Recommended for PHP Vulnerabilities](../../sources/nsa-press-php-4630238/index.html) US National Security Agency (NSA)
- [Critical Vulnerabilities in PHP Require Immediate Patching](../../sources/cisa-alert-php-20261021/index.html) US Cybersecurity and Infrastructure Security Agency (CISA)
- [Critical security issue affecting PHP](../../sources/ncsc-news-php/index.html) UK National Cyber Security Centre (NCSC)

[Every party →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/actors/agencies/index.html
