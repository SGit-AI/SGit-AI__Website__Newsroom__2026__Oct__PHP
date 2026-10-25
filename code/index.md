# The code: where php2shell lives and what the fix does

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Read from a clone of php/php-src: the fix commit (389 files, authored 18 October, public 21 October 14:06 UTC), the engine mechanism it replaces, the hunks that matter, and the end-of-life backport.

# The code: where the bug is, and what the fix does

In plain English Where exactly the bug sits in PHP's own source code, and what the fix changed. Technical; the short version is that PHP used to abandon work mid-way when memory ran out, and now it stops safely.

The editor's question was where the flaw actually lives: in PHP, in C, in the engine? The answer, read from the repository rather than from any article, is the Zend engine's memory manager and request lifecycle, in C, below every PHP application. This page is built from a clone of php/php-src: the fix commit, its parent, the branch it landed on, the end-of-life backport, and the diff between the last vulnerable and first fixed release. The patches and the commit metadata are in the vault with their hashes. [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../sources/php-net-advisory/index.html) [php-src](../sources/github-php-src-branch-7.4-backport/index.html) [php.net](../sources/php-net-changelog-8/index.html) [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) [Fastly](../sources/fastly-blog-php2shell/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) [OpenAI / Wiz / Calif joint…](../sources/php2shell-com/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html)

## The fix commit

`3584a98bda0f2c0d367255b046798b0d3a221a19`, **Avoid state corruption via bailout**, by Arnaud Le Blanc with Ilija Tovilo, Jakub Zelenka (bukka), Nora Dossche, Nicolas Grekas. Authored **2026-10-18 15:26:39 UTC**; committed to the public branch **2026-10-21 14:06:22 UTC**, six minutes after the planned release time. Parent `512c04e39f67`. The commit message, in full:
- Replace bailout on OOM with UnwindExit
- Properly reset various globals that may be accessed during startup
- Fix GHSA-w8hw-w9fx-j79w (CVE-2026-109618)
- Fix GHSA-6wmf-4rv5-p3rp (CVE-2026-109619)

389 files changed, 10,689 insertions, 976 deletions; 113 of the files are not tests.

| Area | Files in the fix |
|---|---|
| Zend/ (the engine) | 96 |
| ext/standard | 52 |
| tests/ | 34 |
| ext/mbstring | 30 |
| ext/gd | 19 |
| ext/date | 17 |
| ext/soap | 14 |
| ext/zlib | 11 |
| ext/session | 5 |
| main/ (request lifecycle, input parsing) | 7 |
| sapi/ | 5 |

Timing, from the commit and merge timestamps:

| When (UTC) | What |
|---|---|
| 2026-10-21 14:06:22 UTC | commit date: the fix enters the public PHP-8.2 branch (committer time; author time is 18 October 15:26 UTC) |
| 2026-10-21 14:12:35 UTC | Ilija Tovilo merges PHP-8.2 into PHP-8.3 |
| 2026-10-21 14:27:03 UTC | merges PHP-8.3 into PHP-8.4 |
| 2026-10-21 14:30:04 UTC | merges PHP-8.4 into PHP-8.5 |
| 2026-10-21 15:34:31 UTC | NEWS entry added (author time 18 October) |

## Where the bug is
- **The language a site is written in (PHP code)** ✗ not where the bug is: Not where the bug is. A site's own PHP code can be perfect; php2shell.com's phrase is that a 'Hello World' application on an affected version is affected.
- **The Zend engine (C): memory manager, request start-up and shutdown** ✓ in scope: Where both bugs are. Zend/zend_alloc.c is PHP's allocator; main/main.c runs a request's start-up and shutdown; main/rfc1867.c parses multipart bodies; main/php_variables.c registers $_GET, $_POST and friends; ext/session/session.c hooks the multipart parser for upload progress. All C.
- **The SAPI (how PHP is attached to the web server)** ✓ in scope: Where exploitability differs. mod_php runs request shutdown even when start-up failed, 'before any application-specific code begins execution'; FPM is susceptible by source analysis; the fix touches sapi/ in five files.
- **The web server, the WAF, the operating system** ✗ not where the bug is: Not where the bug is, but where the controls are: a WAF matches the request shape, the OS limits what the worker can do once it is code execution.

## What the fix does, step by step

The site's reading of the diff, checked against the two GitHub advisories. Each step names the function or file it comes from; the hunks below are verbatim.
- **Before the fix.** When a request pushed PHP past memory_limit, the allocator called zend_mm_safe_error, which raised a fatal error inside a zend_try and then called zend_bailout(): a C longjmp back to the request's top-level handler. The jump abandons whatever function was half-way through building request state. On mod_php the request shutdown then runs anyway and reads that half-built state. That is CVE-2026-109618, 'RCE via OOM corruption'. The same longjmp, or any fatal error, could leave global state pointing into request memory that is about to be freed; the next request on the same worker reads it. That is CVE-2026-109619, 'RCE via stale global state'.
- **The attacker's lever.** The attacker needs to make the allocator fail at a moment of their choosing. The confirmed ways are request-shaped: a multipart body with many parts or long headers (rfc1867.c), deeply nested form field names (php_variables.c and the hash table), and the session upload-progress feature, which is on by default and does work inside the multipart parser before the application runs. Several vendors say the exploit also needs to know the running binary's layout on x86_64, which is why the CVSS vector says attack complexity high.
- **After the fix: the soft limit.** zend_mm_check_limit no longer jumps. If an allocation would exceed memory_limit (now the soft limit), it queues a 'delayed OOM' error and lets the allocation succeed. At the next VM safe point zend_handle_delayed_oom runs, throws an UnwindExit that unwinds the PHP frames in an orderly way, and raises the fatal error with the request's state intact. The commit's own comment: 'When the soft limit is to be exceeded, a delayed OOM error is queued. When the hard limit is to be exceeded, the function does not return.'
- **After the fix: the hard limit.** A new memory_hard_limit_percent setting defines a ceiling above memory_limit. Reaching it calls zend_mm_hard_limit_error and the process ends with _exit(), with no cleanup to corrupt. Allocations that callers can tolerate failing become 'fallible' and return NULL instead of jumping. zend_mm_panic now also uses _exit rather than exit.
- **After the fix: the globals.** shutdown_executor, php_request_shutdown and sapi_deactivate set the pointers they free to NULL or UNDEF ('may be accessed before php_request_startup()'), so a later request cannot find stale state. A new max_multipart_body_parts setting bounds the number of parts the parser will accept; the multipart header parser keeps only Content-Disposition and Content-Type and ignores duplicates; the session upload-progress callback is changed.
- **Why it touched 389 files.** Every place in the engine and the bundled extensions that used to say 'allocation failed, bail out' had to be rewritten to the new contract: queue the error, fail the allocation, or hit the hard limit. That is why ext/standard, mbstring, gd, date and soap are in the diff, and why the PHP Foundation says the fix 'required a major change to the PHP engine' and took two months.
- **The 7.4 branch.** The end-of-life backport is a different, smaller change (17 engine files): it makes every memory error exit the process immediately (zend_mm_safe_error_ex calling _exit) instead of unwinding, resets the same globals, caps multipart parts and disables the session upload-progress callback outright. It is labelled 'Minimal mitigation for EOL version' in the commit. A worker that _exits on every OOM is safe from this bug class and worse at availability.

## The hunks that matter

/* Zend/zend_alloc.c, the fix: the allocator no longer jumps */ static zend_always_inline zend_result zend_mm_check_limit(zend_mm_heap *heap, size_t add_size, bool gc, bool *did_gc ...) { /* Is the soft limit exceeded or going to be exceeded? */ if (UNEXPECTED(heap->limit real_size || add_size > heap->limit - heap->real_size)) { if (gc && zend_mm_gc(heap)) { ... } if (!heap->fallible && add_size > heap->hard_limit - heap->real_size) { zend_mm_hard_limit_error(heap, add_size ...); /* does not return: _exit() */ } if (!gc || (heap->limit real_size || add_size > heap->limit - heap->real_size)) { if (!ZEND_HAS_OOM()) { zend_mm_delayed_error("Allowed memory size of %zu bytes exhausted (tried to allocate %zu bytes)", ...); } return heap->fallible ? FAILURE : SUCCESS; /* the allocation goes ahead, or fails cleanly */ } } return SUCCESS; } /* and what used to be there (the 7.4 branch shows the old shape being replaced) */ - heap->overflow = 1; - zend_try { - zend_error_noreturn(E_ERROR, format, limit, ... size); - } zend_catch { - } zend_end_try(); - heap->overflow = 0; - zend_bailout(); /* longjmp out of the allocation */ - exit(1); /* Zend/zend_execute_API.c: the delayed error is handled at a safe point */ ZEND_API void ZEND_FASTCALL zend_handle_delayed_oom(void) { ... if (execute_data) { EG(exception) = NULL; /* Object allocation should succeed unless it trips the hard limit */ zend_throw_unwind_exit(); /* unwind PHP frames in order */ } zend_try { zend_error_zstr_at(E_ERROR, info->filename, info->lineno, info->message); } zend_catch { } zend_end_try(); ... /* No userland frame to unwind: ... Let it propagate and abort the request, the way an immediate OOM does. */ if (!execute_data) { zend_bailout(); } } /* main/main.c: two settings that did not exist before */ + PHP_INI_ENTRY("max_multipart_body_parts", "-1", PHP_INI_SYSTEM|PHP_INI_PERDIR, NULL) + PHP_INI_ENTRY("memory_hard_limit_percent", NULL, PHP_INI_ALL, OnChangeMemoryHardLimitPercent) /* main/main.c: the stale-state class, in one line */ for (i=0; i

## The end-of-life backport, and how it differs

Branch `PHP-7.4-CVE-2026-109618-109619`, commit `712e60f9e`, same title, same author, authored 2026-10-18 18:09:54 UTC. The commit says *Minimal mitigation for EOL version.*. 17 files: `Zend/zend_alloc.c (+68)`, `Zend/zend_execute_API.c (+13)`, `Zend/zend_hash.c (+13)`, `Zend/zend_types.h (26)`, `Zend/zend_vm_def.h (+11)`, `main/rfc1867.c (+39)`, `main/php_variables.c (8)`, `main/main.c (+6)`, `main/SAPI.c (+5)`, `ext/session/session.c (2)`, `Zend/zend_API.h, zend_alloc.h, zend_hash.h, zend_llist.c, zend_multiply.h, zend_strtod.c, zend_vm_execute.h`. Instead of the delayed error and the unwind, every memory error calls a new `zend_mm_safe_error_ex` that prints the fatal and `_exit`s the process; the same globals are reset; a `max_multipart_body_parts` cap is added; the multipart header parser keeps only the two headers it uses; and the session upload-progress callback is disabled with a one-line `|| true`. A worker that dies on every out-of-memory cannot be exploited this way and will be worse at staying up.

## What the code does not tell us
- Which of the 389 files are the security fix and which are the refactor the fix needed is not separable from the diff alone; the GHSA text and the commit body are the only guide.
- The 2024 trail: the Foundation says a core developer saw the first signs of the OOM problem while fixing a 2024 audit finding. That developer, that fix and that issue are not named in any captured source, and this site's shallow clone does not reach 2024 history.
- Whether the Fediverse report of an incomplete fix in 8.5.12 concerns one of these paths.

How the bug is reached from a request is on [the two flaws](../flaws/index.html); what to watch for on a host is on [detection and defence](../defence/index.html).


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/code/index.html
