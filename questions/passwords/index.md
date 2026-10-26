# Do I need to change my passwords?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Not because of this, as things stand. The flaw is on web servers, not on your devices, and no named site has announced a breach through it, as of the latest check. If a site you use announces one, follow its instructions. Using a different password on every site is the protection that holds whatever the next flaw is.

Question · kept by the librarian · `librarian@php.newsroom`

# Do I need to change my passwords?

How it was asked: The Times' standfirst mentions stolen passwords.

## The short answer

Not because of this, as things stand. The flaw is on web servers, not on your devices, and no named site has announced a breach through it, as of the latest check. If a site you use announces one, follow its instructions. Using a different password on every site is the protection that holds whatever the next flaw is.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/passwords/index.html`

## The answer, with its sources

**The flaw is on the server.** Both bugs are in the PHP engine that runs on web servers; nothing on a reader's computer or phone is affected or needs updating for this. [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [php.net](../../sources/php-net-advisory/index.html)

**What an attacker could reach** on a compromised server is whatever that server holds, which can include a site's user database. That is why the agencies treat it as urgent. But no named organisation has said it was compromised through php2shell, as of the latest check. [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html)

**This is the site's reading, not an agency's advice:** none of the captured advisories tells the public to change passwords. If a service you use announces a breach, its notice is what to act on. [NCSC UK](../../sources/ncsc-news-php/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html)

## The pages that carry it
- [The two flaws: CVE-2026-109618 and CVE-2026-109619](../../flaws/index.html#blast)
- [Impact: taken offline versus compromised](../../impact/index.html)
- [Briefing for a media and communications team: What can we say that is true, what should we not say, and what will we be asked?](../../briefings/comms/index.html)

Next question: [How do I know whether my site is affected?](../am-i-affected/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.22.16 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/questions/passwords/index.html
