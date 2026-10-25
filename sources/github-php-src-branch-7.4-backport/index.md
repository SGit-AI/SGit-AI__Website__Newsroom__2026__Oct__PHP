# Source: Branch PHP-7.4-CVE-2026-109618-109619

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

php/php-src on GitHub: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · primary · captured

# Branch PHP-7.4-CVE-2026-109618-109619

**php/php-src on GitHub** · [https://github.com/php/php-src/tree/PHP-7.4-CVE-2026-109618-109619](https://github.com/php/php-src/tree/PHP-7.4-CVE-2026-109618-109619) · published 2026-10-18T18:10:24Z · added by `collector-primary` · slug `github-php-src-branch-7.4-backport`

Unofficial minimal source backport for EOL 7.4. '1 commit ahead of ... master'; latest commit 'Avoid state corruption via bailout', commit date 2026-10-18T18:10:24Z. The 8.0 and 8.1 branches are not captured (same naming pattern).

## What it says, as the collector read it

#### php-src branch PHP-7.4-CVE-2026-109618-109619: notes

- Linked from the php.net advisory as a "minimal source-backport" for PHP 7.4 (EOL). The branch is "1 commit ahead of and 34022 commits behind master". Latest commit "Avoid state corruption via bailout", dated 2026-10-18T18:10:24Z.

- The PHP-8.0- and PHP-8.1-CVE-2026-109618-109619 branches are linked the same way but were not captured.

- Implication: PHP 7.4-8.1 are affected but are not listed in the CVE records (defaultStatus "unaffected").

- curl to github.com returned 403 from the egress proxy. Playwright worked.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' [fact timeline →](../../facts/fix-bailout/index.html) | PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-18 | The final fix commit is authored; the 7.4 backport branch's commit is dated 18:10:24Z. | stated |

## The bytes
capture 20261022T081558Z · HTTP 200 · https://github.com/php/php-src/tree/PHP-7.4-CVE-2026-109618-109619- `headers.json` a849a6e452711b855043ae9fe1fd0982b11d14633681acc628fa56e60ceb8323 5,439 bytes
- `page.html` 04dcda73bc626ce33da19b196795fd7c00b63b030f9fd6a530acedcbbe4f2b77 363,416 bytes
- `provenance.json` b879f4cb8fe1d72fc30175af0e12496f9df0b4e09ce90b1de15b99d1e8ed29fc 1,040 bytes
- `rendered.html` f6eba14e4661be71a25a3f70b5e988478a727cc6ea78f657fe86284d54d727fd 412,706 bytes
- `screenshot.png` 6a7c4e4d30f1cb137b32490feb57c7053ca293f0f59d4aada14082309c525f0a 759,378 bytes
- `text.txt` bd71e98ee89b7c6ca97f0ec6029e0200f86d26f2528387a96c99ac93ea63dc1f 6,550 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-php-src-branch-7.4-backport/index.html
