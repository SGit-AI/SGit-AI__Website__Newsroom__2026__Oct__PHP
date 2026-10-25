# Source: Commit 3584a98bd: Avoid state corruption via bailout (the php2shell fix) and the PHP-7.4 backport 712e60f9e

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

php/php-src (git), read from a clone: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · primary · captured

# Commit 3584a98bd: Avoid state corruption via bailout (the php2shell fix) and the PHP-7.4 backport 712e60f9e

**php/php-src (git), read from a clone** · [https://github.com/php/php-src/commit/3584a98bda0f2c0d367255b046798b0d3a221a19](https://github.com/php/php-src/commit/3584a98bda0f2c0d367255b046798b0d3a221a19) · published 2026-10-18T15:26:39Z (authored); 2026-10-21T14:06:22Z (committed) · added by `claude-story-site` · slug `github-php-src-fix-commit-3584a98bd`

git show output of the fix commit (stat, file list, engine/main/session hunks), the 7.4 backport commit and patch, and the merge path to PHP-8.5, from a shallow clone made 22 Oct 2026. SHA256SUMS in raw/. 389 files, +10689/-976; authors Arnaud Le Blanc with Ilija Tovilo, Jakub Zelenka, Nora Dossche, Nicolas Grekas.

## What it says, as the collector read it

#### The fix commit, read from the repository

- Clone: `git clone --depth 1 https://github.com/php/php-src`, then tags php-8.5.11, php-8.5.12, php-8.4.26, php-8.4.27 and branches PHP-8.5, PHP-8.4 (depth 80) and PHP-7.4-CVE-2026-109618-109619 (depth 50).

- Fix: 3584a98bda0f2c0d367255b046798b0d3a221a19, "Avoid state corruption via bailout", author Arnaud Le Blanc, authored 2026-10-18T17:26:39+02:00, committed 2026-10-21T16:06:22+02:00, parent 512c04e39f. Co-authors Ilija Tovilo, Jakub Zelenka, Nora Dossche, Nicolas Grekas. Body: "Replace bailout on OOM with UnwindExit; Properly reset various globals that may be accessed during startup; Fix GHSA-w8hw-w9fx-j79w; Fix GHSA-6wmf-4rv5-p3rp".

- 389 files, 10689 insertions, 976 deletions; 113 non-test files; Zend/ 96, ext/standard 52, tests 34, ext/mbstring 30, ext/gd 19, ext/date 17, ext/soap 14, main/ 7, ext/session 5, sapi/ 5.

- Merge path on PHP-8.5: Ilija Tovilo merges PHP-8.2 into PHP-8.3 at 2026-10-21T14:12:35Z, PHP-8.3 into PHP-8.4 at 14:27:03Z, PHP-8.4 into PHP-8.5 at 14:30:04Z; NEWS entry a34a205c2 authored 2026-10-18T15:34:31Z.

- 7.4 backport: 712e60f9edfd03f0960fc4fc3c2c375f42b90aa2, same title, authored 2026-10-18T18:09:54Z, "Minimal mitigation for EOL version", 17 files (Zend/zend_alloc.c +68, main/rfc1867.c +39, Zend/zend_types.h, Zend/zend_execute_API.c, Zend/zend_hash.c, Zend/zend_vm_def.h, main/php_variables.c, main/main.c, main/SAPI.c, ext/session/session.c, and headers).

- Mechanism (from the diff): zend_mm_check_limit replaces the bailout; a soft limit queues a delayed OOM (zend_mm_delayed_error) handled at the next VM safe point by zend_handle_delayed_oom via zend_throw_unwind_exit; a hard limit (memory_hard_limit_percent) ends the process with _exit; fallible allocations return NULL; globals reset in shutdown_executor, php_request_shutdown and sapi_deactivate; new ini max_multipart_body_parts; rfc1867 keeps only Content-Disposition and Content-Type headers and ignores duplicates.

- rjmendez's repository names the fix commit as 82f8f31b16a; not reconciled with 3584a98bd (possibly the PHP-8.2 commit before merge, or a cherry-pick).

- Not reached: 2024 history (shallow clone).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The fix was authored on 18 October at 15:26 UTC and entered the public branches at 14:06 UTC on 21 October, with merges into 8.3, 8.4 and 8.5 between 14:12 and 14:30 UTCCounted from the repository, not from a page. Five authors; 389 files; 10,689 insertions. [fact timeline →](../../facts/fix-authored/index.html) | php/php-src commit 3584a98bd, read from a clone | confirmed | **A6** Established●●●●●● | 2/2 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) |
| Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed requestThe fix replaces bailout with a delayed error and an UnwindExit at a safe point, adds a hard limit that _exits, and resets the globals. See the code page. [fact timeline →](../../facts/fix-engine/index.html) | php/php-src fix commit; the GitHub advisories | confirmed | **A6** Established●●●●●● | 3/3 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-18 15:26:39 UTC | Arnaud Le Blanc authors the fix, 'Avoid state corruption via bailout', with Ilija Tovilo, Jakub Zelenka, Nora Dossche and Nicolas Grekas; the 7.4 minimal backport is authored at 18:09 UTC. | stated |
| 2026-10-21 14:06:22 UTC | The fix commit enters the public php-src branches (commit timestamp); merged into 8.3 at 14:12, 8.4 at 14:27 and 8.5 at 14:30 UTC. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 389 | files changed by the fix commit, 10,689 lines added | confirmed |

## The bytes

No browser capture; see raw.
raw, 7 files with SHA256SUMS- `commit-3584a98bd.NEWS.diff` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- `commit-3584a98bd.engine-main-session.patch` 26bed812bcc7c89ea684f52d0a2e2a09f7bf516296f31b7065387c3c85013d84
- `commit-3584a98bd.files.txt` d9b8465ccfbd22fa5bcd5f1a8c58c11b4af70befe488051f843fd4f45bf559b5
- `commit-3584a98bd.stat.txt` 0d696e59634f83a4040532d4c6e4ac9cb5319e1c6e81ac2c76f3b7e9257f2b4b
- `commit-712e60f9e-PHP-7.4-backport.patch` 307e49f52c4f3829e75ce82697b81c6ab771deb7ce0c8ce961159e40026866da
- `commit-712e60f9e-PHP-7.4-backport.stat.txt` 7f5e6289ca2d1a14b2be78ca230e2077f3d5f695bb9d52087773e3df2633e7f0
- `merge-path-3584a98bd-to-PHP-8.5.txt` 81c3025511c2f4744d1fcbe1d18fe7da97cfd68b005a6a883efc229a3c91193f

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-php-src-fix-commit-3584a98bd/index.html
