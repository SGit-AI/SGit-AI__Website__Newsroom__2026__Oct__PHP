# Do our developers need to change our code?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

No. Both bugs are in the C engine that runs PHP, not in PHP code, and the demonstrated attack runs before any application code. The fix is updating the PHP runtime and restarting it. What developers can do is check the version on the machines they deploy to and rebuild container images.

Question · kept by the librarian · `librarian@php.newsroom`

# Do our developers need to change our code?

How it was asked: Asked by managers handed the headline.

## The short answer

No. Both bugs are in the C engine that runs PHP, not in PHP code, and the demonstrated attack runs before any application code. The fix is updating the PHP runtime and restarting it. What developers can do is check the version on the machines they deploy to and rebuild container images.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/change-code/index.html`

## The answer, with its sources

**The bugs are in the engine.** The fix commit changes the allocator's out-of-memory handling and the request globals in php-src, 389 files. [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

**Before your code runs.** The mod_php exploit was demonstrated with default settings before any application code runs. [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html)

## The pages that carry it
- [Briefing for a developer: Is my code the problem, what do I change, and how do I check the box I deployed to?](../../briefings/developer/index.html)
- [The code: where php2shell lives and what the fix does](../../code/index.html)
- [The fix, mapped to the code](../../review/index.html)

Next question: [Can anything be done to fix it, or do we just have to wait for updates?](../fix-or-wait/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.12.0 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/questions/change-code/index.html
