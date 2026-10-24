# We are on PHP 7.4, 8.0 or 8.1. Is there a patch?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Not a release. PHP 8.1 and older are out of support; the project published source backport branches for 7.4, 8.0 and 8.1, which someone has to build. CISA says systems on 8.1 or older should be taken offline. Plan the migration to 8.2 or later now; in the meantime a distribution or vendor that backports, the temporary mitigations and isolation are the options.

Question · kept by the librarian · `librarian@php.newsroom`

# We are on PHP 7.4, 8.0 or 8.1. Is there a patch?

How it was asked: Asked by anyone with a site that has not been upgraded in a while.

## The short answer

Not a release. PHP 8.1 and older are out of support; the project published source backport branches for 7.4, 8.0 and 8.1, which someone has to build. CISA says systems on 8.1 or older should be taken offline. Plan the migration to 8.2 or later now; in the meantime a distribution or vendor that backports, the temporary mitigations and isolation are the options.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/old-php/index.html`

## The answer, with its sources

**No release for 8.1 and older.** php.net: *PHP 8.1 and older no longer receive updates from the PHP project.* Source-only backport branches exist for 7.4, 8.0 and 8.1. [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html)

**They are affected.** The CVE records list 8.2 to 8.5 only, but the backports imply at least 7.4 onward is affected, as Greenbone noted on oss-security. [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html)

**CISA's advice** is that organisations running PHP 8.1 or older should take PHP-based systems offline. [CISA](../../sources/cisa-alert-php-20261021/index.html)

## The pages that carry it
- [The two flaws: CVE-2026-109618 and CVE-2026-109619](../../flaws/index.html#versions)
- [If you run PHP: the steps, in order, with their sources](../../playbook/index.html)
- [Briefing for a CTO: What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?](../../briefings/cto/index.html)

Next question: [We are behind Cloudflare (or another firewall). Are we safe?](../waf-enough/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.14.18 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/questions/old-php/index.html
