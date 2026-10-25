# From a line of code to a stakeholder: the fractal graph

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

One graph for php2shell: 359 changed lines of php-src, up through functions, files, the fix and the flaws, the claims and sources, the story arcs and the risks, to the fifteen kinds of reader who face them.

# From a line of code to a stakeholder

One graph for the whole story. At the bottom, the 359 changed hunks of the php2shell fix, each a line range in php-src; above them the functions and files they sit in, the parts of the fix, the two flaws; then the claims and events that talk about them and the sources those cite; then the story arcs those claims carry, the risks the arcs describe, and at the top the fifteen kinds of reader who face those risks. 901 nodes, 1236 edges. Every node opens into its own neighbourhood: [walk it](ui/index.html), from the top or from a line.

## The layers

| Layer | Nodes | Where it comes from |
|---|---|---|
| **Stakeholders** | 16 | the fifteen readers in data/personas.json |
| **Risks** | 9 | authored in data/arcs.json, each resting on claims |
| **Story arcs** | 7 | authored in data/arcs.json, each carrying risks and resting on claims and events |
| **Claims and events** | 138 | data/claims.json and data/timeline.json, each with a status or a date |
| **Sources** | 97 | the captured, hashed sources the claims and events cite |
| **The flaws** | 2 | the two CVEs, from data/review.json |
| **The fix** | 7 | the commit and what it does, from data/review.json |
| **Areas and files** | 73 | php-src areas and files the fix changed, from review/code/files.json |
| **Functions** | 193 | the C functions the fix changed, from the diff |
| **Lines** | 359 | every changed hunk, with its line range in php-src |

The top three layers and the joins from a claim to a flaw or a part of the fix are written by the librarian in [data/arcs.json](../data/arcs.json); everything else is derived by the build from files the site already publishes. The assembled graph is [data/fractal.json](../data/fractal.json).

## What is joined, and what is not

- **359 of 359** changed hunks reach a stakeholder by walking up the graph.

- **215 of 359** reach a *named* part of the fix (a soft limit, an unwind, globals reset and so on). The rest reach the fix only as "the commit touched this area": the review joined nine files to what the fix does, and the other files of the engine wait for that join.

- **15 of 16** stakeholders reach a changed line by walking down.

- Not here yet: the 352 files outside the engine and bundled extensions the fix also touched (mostly tests), and the lines of the PHP 7.4 backport.

- Not here by design: the vulnerable code before the fix. The graph maps the lines the fix wrote, never a trigger path (the site's security requirements, [AGENTS.md](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/AGENTS.md)).

## Five threads, top to bottom

Each is the shortest path down the ladder from one reader to a changed line, computed by the build. Click any rung.

### Website owner, down to a line
- Stakeholders [Website owner](../briefings/site-owner/index.html)
- Risks Your version gets no fix
- Story arcs [The bug is in the engine, not in your code](../flaws/index.html)
- Claims and events [Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe](../claims/index.html#only-update) confirmed
- The flaws [CVE-2026-109619: RCE via stale global state](../review/ui/index.html#cve-109619)
- The fix [Bounded, deduplicated request parsing](../review/ui/index.html#fix-bounded-parsing)
- Areas and files [main/rfc1867.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/main/rfc1867.c)
- Lines [rfc1867.c:54](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/main/rfc1867.c#L54-L54)

[Walk it from the top](ui/index.html#who:site-owner) · [walk it up from the line](ui/index.html#line:main/rfc1867.c:54)

### Board member or executive, down to a line
- Stakeholders [Board member or executive](../briefings/board/index.html)
- Risks What the server holds is taken
- Story arcs [The bug is in the engine, not in your code](../flaws/index.html)
- Claims and events [In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS](../claims/index.html#wordpress-drupal) reported
- The flaws [CVE-2026-109618: RCE via OOM corruption](../review/ui/index.html#cve-109618)
- The fix [A soft memory limit that no longer jumps](../review/ui/index.html#fix-soft-limit)
- Areas and files [Zend/zend_alloc.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_alloc.c)
- Lines [zend_alloc.c:1149-1153](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_alloc.c#L1149-L1153)

[Walk it from the top](ui/index.html#who:board) · [walk it up from the line](ui/index.html#line:Zend/zend_alloc.c:1149)

### Journalist, down to a line
- Stakeholders [Journalist](../briefings/journalist/index.html)
- Risks Deciding on the wrong numbers
- Story arcs [The numbers do not measure the same thing](../numbers/index.html)
- Claims and events [The flaws are CVSS 10.0](../claims/index.html#cvss-10) contradicted
- The flaws [CVE-2026-109618: RCE via OOM corruption](../review/ui/index.html#cve-109618)
- The fix [Allocations that may fail instead of abort](../review/ui/index.html#fix-fallible)
- Areas and files [Zend/zend_hash.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_hash.c)
- Lines [zend_hash.c:1095-1099](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_hash.c#L1095-L1099)

[Walk it from the top](ui/index.html#who:journalist) · [walk it up from the line](ui/index.html#line:Zend/zend_hash.c:1095)

### Developer, down to a line
- Stakeholders [Developer](../briefings/developer/index.html)
- Risks Your version gets no fix
- Story arcs [The bug is in the engine, not in your code](../flaws/index.html)
- Claims and events [Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe](../claims/index.html#only-update) confirmed
- The flaws [CVE-2026-109619: RCE via stale global state](../review/ui/index.html#cve-109619)
- The fix [Bounded, deduplicated request parsing](../review/ui/index.html#fix-bounded-parsing)
- Areas and files [ext/session/session.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/ext/session/session.c)
- Functions [PHP_GINIT_FUNCTION()](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/ext/session/session.c)
- Lines [session.c:2804](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/ext/session/session.c#L2804-L2804)

[Walk it from the top](ui/index.html#who:developer) · [walk it up from the line](ui/index.html#line:ext/session/session.c:2804)

### Curious reader, down to a line
- Stakeholders [Curious reader](../briefings/everyone/index.html)
- Risks What the server holds is taken
- Story arcs [The bug is in the engine, not in your code](../flaws/index.html)
- Claims and events [In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS](../claims/index.html#wordpress-drupal) reported
- The flaws [CVE-2026-109618: RCE via OOM corruption](../review/ui/index.html#cve-109618)
- The fix [Allocations that may fail instead of abort](../review/ui/index.html#fix-fallible)
- Areas and files [Zend/zend_hash.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_hash.c)
- Lines [zend_hash.c:1095-1099](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_hash.c#L1095-L1099)

[Walk it from the top](ui/index.html#who:everyone) · [walk it up from the line](ui/index.html#line:Zend/zend_hash.c:1095)

## The edges

| Edge | Count |
|---|---|
| changed at | 359 |
| cites | 299 |
| changes | 193 |
| rests on | 124 |
| dated by | 67 |
| faces | 44 |
| contains | 37 |
| about | 36 |
| touches | 36 |
| told in | 18 |
| realised in | 9 |
| closed by | 8 |
| introduces | 6 |

Edges are read top down: a stakeholder *faces* a risk, a risk is *told in* an arc and *rests on* claims, a claim *cites* sources and is *about* a flaw or a part of the fix, a flaw is *closed by* the fix, which is *realised in* files, which *change* functions, which are *changed at* lines. The navigator walks them both ways.

The fix-only version of this graph is [the fix mapped to the code](../review/index.html); the citation graph alone is [as a graph](../graph/index.html). This answers the second memo's ask for the semantic fractal graph; what it still lacks is on [corrections](../corrections/index.html).


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/fractal/index.html
