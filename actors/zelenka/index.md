# Jakub Zelenka (bukka), PHP security team: what they say

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Jakub Zelenka (bukka), PHP security team: published both GitHub advisories and the oss-security announcements; the claims this site attributes to them and their sources.

Party

# Jakub Zelenka (bukka), PHP security team

published both GitHub advisories and the oss-security announcements

## Claims this site attributes to this party

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs [fact timeline →](../../facts/rce-modphp/index.html) | PHP security team (GHSA, oss-security), php.net | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' [fact timeline →](../../facts/fix-bailout/index.html) | PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe [fact timeline →](../../facts/only-update/index.html) | php.net; PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| The leak started with an anonymous Hacker News post citing a reliable source, which came down after screenshots spread; a screenshot of the 'PHP2Shell tool' credited to Calif.io and a short exploitation video also went up and came downContradicts the Foundation's 'no technical details leaked' and The Hacker News's 'a proof-of-concept exploit leaked'. No copy of the post, screenshot or video is in the vault. [fact timeline →](../../facts/leak-hn/index.html) | Alexandre Daubois (PHP security team, personal blog) | reported | **A4** Corroborated●●●●○○ disputed | 0/1 | [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |

## Its sources in the vault
- [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) PHP (php/php-src GitHub security advisory, published by bukka)
- [CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption](../../sources/openwall-oss-security-2026-10-21-6/index.html) oss-security list (Jakub Zelenka, PHP security team)

[Every party →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/actors/zelenka/index.html
