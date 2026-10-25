# Can anything be done to fix it, or do we just have to wait for updates?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The updates already exist: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 were released on 21 October and fix both flaws. Nobody is waiting on PHP; the wait is for whoever runs each server to install them and restart. If that is you, update now; if you cannot today, there are temporary settings and, as a last resort, taking the site offline. If a hosting company runs your site, ask them whether it is patched.

Question · kept by the librarian · `librarian@php.newsroom`

# Can anything be done to fix it, or do we just have to wait for updates?

How it was asked: In a group chat on the morning of 22 October, under a link to The Times' story 'Race to fix PHP security issue in software behind most websites'.

## The short answer

The updates already exist: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 were released on 21 October and fix both flaws. Nobody is waiting on PHP; the wait is for whoever runs each server to install them and restart. If that is you, update now; if you cannot today, there are temporary settings and, as a last resort, taking the site offline. If a hosting company runs your site, ask them whether it is patched.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/fix-or-wait/index.html`

## What it means for you

| If | Then |
|---|---|
| you run your own server or VPS | update the PHP package, restart PHP-FPM or Apache, check `php -v` where the code actually runs. |
| a hosting company or agency runs your site | ask them in writing whether PHP is on 8.5.12, 8.4.27, 8.3.36 or 8.2.35 (or a distribution backport) and when the workers were restarted. |
| you use a hosted service such as a shop platform or a SaaS product | there is nothing to install; the provider patches. Check its status page. |
| you only visit websites | there is nothing to update on your computer or phone for this one; the flaw is on web servers. |

## The answer, with its sources

**The fix is out.** The PHP project released fixed versions on 21 October 2026: 8.5.12, 8.4.27, 8.3.36 and 8.2.35. php.net says *All PHP users are strongly encouraged to update immediately*, and that only an update is a complete solution. [php.net](../../sources/php-net-advisory/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html)

**So the wait is not for PHP, it is for whoever runs the server.** Installing the package is not enough on its own: every PHP worker has to be restarted and every container image rebuilt, and the running version checked afterwards. Linux distributions ship their own backported packages; at least one third-party repository had none on release day. [php.net](../../sources/php-net-advisory/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html)

**If you cannot update today**, php.net lists temporary settings that each block a known attack path (for example `session.upload_progress.enabled=0`, a low `post_max_size`, and on 8.5 `fatal_error_backtraces=0`). Its own words: they *reduce exposure to specific attack paths but do not make an installation safe*. [php.net](../../sources/php-net-advisory/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

**A web application firewall in front helps, and is not enough.** Cloudflare, Akamai, Fastly, Imperva and Fortinet shipped rules, and every one of them calls it a stopgap and says patch anyway. [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html)

**If none of that can be done in time**, the NSA, CISA and the UK NCSC say take the system offline until it is fixed. That is the last step on every agency's list, not the first. [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)

**Two exceptions.** PHP 8.1 and older get no release: the project published source backports for 7.4, 8.0 and 8.1, so for those the answer is a migration plan, or a vendor that backports. And a report that the 8.5.12 fix may be incomplete reached the oss-security list within hours; it is unverified, carried second-hand, and PHP is reported second-hand to have called it unrelated. Keep watching php.net for a follow-up release anyway. [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html)

## The pages that carry it
- [If you run PHP: the steps, in order, with their sources](../../playbook/index.html)
- [The two flaws: CVE-2026-109618 and CVE-2026-109619](../../flaws/index.html#mitigations)
- [Detection and defence: what blocks php2shell and what shows it](../../defence/index.html)
- [Affected systems: versions, deployments, applications, inventory](../../affected/index.html)
- [Briefing for a developer: Is my code the problem, what do I change, and how do I check the box I deployed to?](../../briefings/developer/index.html)

Next question: [Is PHP really the software behind most websites?](../most-websites/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.21.2 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/questions/fix-or-wait/index.html
