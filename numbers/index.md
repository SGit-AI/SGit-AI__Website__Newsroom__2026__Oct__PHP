# The numbers: 70%, 30 million, 2.6 million, 6,000, 674

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Every scale figure in circulation about php2shell, with what it measures, who said it, whether anyone checked it, and why they differ by four orders of magnitude.

# The numbers, and what each one measures

In plain English The big numbers in the headlines measure different things. 70% is a share of websites, not of the Internet; 2.6 million is a count of servers.

The editor's starting point for this site was a figure that did not add up: *70% of the internet*. It turns out to be a headline's restatement of a share-of-websites statistic that nobody on this beat sources, sitting next to a host count a thousand times smaller and a national count a thousand times smaller again. None of them is wrong on its own terms. The table says what each one counts.

| Figure | What it measures | Who said it | Status | Note | Sources |
|---|---|---|---|---|---|
| 70% the Internet | Not stated. The headline is a restatement of the body's figure for websites. | Wiz (headline and X post) | unverified | The BBC says it could not independently verify this figure. The body of the same Wiz post says PHP 'powers 70% of all websites in the world' and cites no measurement. | [Wiz](../sources/wiz-blog-php2shell/index.html) [Wiz on X](../sources/x-wiz-io-php2shell/index.html) |
| almost 70% websites | The share of websites whose server-side language is PHP, as commonly published by web-technology surveys. Neither page names the survey. | Cloudflare; OpenAI ('an estimated 70% of websites') | reported | A share of websites is not a share of the Internet, and a site that uses PHP is not a site that is reachable, unpatched and exploitable. | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html) |
| about 30 million websites | Not stated. | Alan Woodward, Surrey Centre for Cyber Security, on the BBC | reported | Second-hand through the BBC. No basis given. | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2,608,039 internet-facing hosts running PHP | Hosts observed on the internet that expose PHP, as counted by one scanning vendor. | VulnCheck, via The Hacker News | reported | A host count, far smaller than any websites figure, because one host serves many sites and most sites are behind hosts that do not expose PHP directly. | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| about 6,000 potentially affected resources in Latvia, a few hundred in the public sector | Resources identified by the national CERT as potentially affected, in one country. | CERT.LV | reported | The one national-scale count from a primary source, and the only one that says 'potentially'. | [CERT.LV](../sources/certlv-php-preventive/index.html) |
| 674 software entries in the NCSC-NL php2shell inventory | Rows in the inventory: 206 marked Vulnerable, 46 Fix, 418 Investigation, 3 Not vulnerable, 1 without a status. | NCSC-NL, counted from the file at commit cca173c64ec5 | confirmed | NCSC-NL calls the entries investigation leads until a vendor backs them. Counted by this site's export script, not copied from a page. | [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell/index.html) |
| 9.2 CVSS v4.0, each CVE | CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | PHP Group as CNA; GitHub advisories; CERT-EU; ACN | confirmed | The 10.0 that circulated on 20 October is wrong, per the PHP Foundation; a PHP security team member traces it to a social post relayed by a vendor and a news site. | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [CERT-EU](../sources/certeu-sa-2026-018/index.html) [ACN / CSIRT Italia](../sources/acn-it-php2shell/index.html) |
| 10.1 million views of the NSA Cyber post, at capture | The view counter X displayed when the post was captured. | X, as displayed at 2026-10-22T08:09Z | confirmed | A capture-time number; it will be higher now. | [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) |
| 4 days before disclosure, an exploit attempt hit an Amazon honeypot | 17 October 2026, MadPot honeypot, one attempt from an anonymisation network. | CJ Moses, Amazon, via The Hacker News | reported | Amazon's own post has not been found; the quote is as The Hacker News printed it. | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| about 9 hours before disclosure, Cloudflare's WAF rules went live for all customers | 21 October 2026 03:02 UTC against the 14:00 UTC release. | Cloudflare | confirmed | Primary party. No attack volumes are in the post. | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| more than 6 hours before the coordinated release, Chainguard published built images with the fix | 21 October 2026 07:41 UTC. | The PHP Foundation | reported | Chainguard reportedly does not dispute the time but denies leaking; that article is blocked from this environment. | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 1.57 million internet-facing hosts with an identifiable PHP version that were unpatched on 21 October, of 2.58 million seen | Hosts whose HTTP response announces a PHP version below the fixed one. Hosts that hide the version (a million of them) are not counted either way. | Censys, via SecurityWeek | reported | Censys's own post was not found; nearly 3 million hosts by 22 October per the same report. | [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) |
| millions exploit attempts seen across Cloudflare's network by 22 October 01:25 UTC | Requests matching Cloudflare's rules, across all customers. Not compromises, not unique attackers, not unique targets. | Matthew Prince, Cloudflare | reported | Thousands in the ten hours before the announcement. | [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) |
| 22.6 million internet-facing systems that 'could be vulnerable' | Not stated. | Palo Alto Networks Unit 42, via Insurance Business | reported | Nine times Censys's host count; the method is not given. | [Insurance Business](../sources/insurancebusiness-uk-councils-met/index.html) |
| 94% Weird Gloop's wiki page views still served during its 13-hour shutdown | Page views served from cache with no PHP or database running, as measured by the operator. | Weird Gloop | confirmed | The one number on this page that measures the cost of taking a system offline. | [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) |
| 389 files changed by the fix commit, 10,689 lines added | git show --shortstat on commit 3584a98bd; 113 of the files are not tests. | php/php-src, counted by this site from a clone | confirmed | The 7.4 backport changes 17 files. | [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |
| 270 CVEs added to CISA's Known Exploited Vulnerabilities catalog in 2026 so far; 0 of them php2shell | Entries with dateAdded in 2026 in catalog version 2026.10.21. | CISA KEV, counted by this site | confirmed | Three PHP core CVEs are in the catalog from earlier years. | [CISA](../sources/cisa-kev-json/index.html) |

## Why they differ by four orders of magnitude

- **A share of websites that use PHP** (about 70%) is the population a survey counts by looking at response headers and page markup across a sample of the web. It includes every site on a shared host that patched hours ago, every site behind a CDN, and every site that has not been touched since 2019. It is an upper bound on exposure.

- **Internet-facing hosts that expose PHP** (2.6 million, one scanner's count) is a count of machines, not sites. One host serves many sites; most sites sit behind hosts that do not announce PHP at all. It is a lower bound on the machines an attacker could reach directly.

- **Websites that could be affected** (30 million) has no stated basis. It may be a fraction of a websites total; it may be a guess.

- **Resources potentially affected in one country** (about 6,000 in Latvia) is the only figure from a body that could inventory what it counts. Scaled naively by population it would put the EU in the low millions, which is a different number from any of the above and is not offered here as one.

- **Products in an inventory** (674) counts software, not deployments: one row is WordPress, another is a Linux distribution's package.

The number a reader actually wants, how many systems were exploitable at a given hour and how many were exploited, does not exist in any captured source. What exists is a set of signals, on [the exploitation page](../exploitation/index.html).


---
site v0.5.4 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/numbers/index.html
