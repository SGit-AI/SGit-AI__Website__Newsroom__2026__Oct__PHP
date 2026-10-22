---
slug: why-not-patch-every-version
title: Why can't every version of PHP just be patched?
dek: The second story inside php2shell. The fix exists for four versions of PHP; everyone else depends on who they buy PHP from. What the project shipped, what it did not, who filled the gap and for whom, and the editor's argument that patching should be a relationship, not a chore.
role: journalist
origin: house
author: claude-journalist
written: 2026-10-22
as_of_version: 0.4.0
vault_commit: 200d08971937
data_as_of: 2026-10-22T11:34Z
---

**22 October 2026.** The first story about php2shell is the flaw: how bad, who found it, who is attacking. The second story is the fix, and the editor put its question plainly in his brief this afternoon: if the bug sits below the application, in PHP itself, "why can't we patch every single version of PHP very straightforwardly?" The evidence has an answer, and it is not mainly technical. It is about who is responsible for a given copy of PHP, and whether anybody is paid to be. The facts this story rests on are laid out, row by row, on [Patching](/patching/index.html).

## The bug is below the code, so the fix has to be compiled in

Both flaws are in PHP's engine, the C program that runs every PHP website, in how it handles running out of memory and what it leaves behind after a failed request. A site's own code can be flawless and still be exposed. [[github-ghsa-w8hw-w9fx-j79w, github-ghsa-6wmf-4rv5-p3rp]] That is what makes the editor's question sharp: no application developer can fix this. Whoever builds the PHP binary has to.

## What the PHP project shipped

For the four supported branches, 8.2 to 8.5, the project shipped releases: 8.2.35, 8.3.36, 8.4.27 and 8.5.12, tagged and signed, with Windows binaries. [[php-net-advisory, github-php-src-tags, ncsc-nl-php2shell-software-list]] For the three branches it no longer supports, 8.1, 8.0 and 7.4, it published source code on separate branches, which nobody can install without building PHP themselves. [[php-net-advisory, github-php-src-branch-7.4-backport]] For everything older, from 7.3 back to 5.x, it published nothing, although agencies and the researchers say those versions are affected too. [[ncsc-nl-advisories, x-wiz-io-php2shell, certfr-2026-ale-014]]

There is a trap in the records. The CVE entries list only 8.2 to 8.5 and default to "unaffected" for everything else, so a vulnerability scanner that reads them will report a server on 7.4 or 8.1 as safe. [[cve-cve-2026-109618, openwall-oss-security-109619-thread]]

## Why it is not straightforward

The fix is not a line or two. It is a change to how the whole engine handles memory errors: 389 files, 113 of them outside the tests, touching the engine and extensions that most sites load without thinking, from text handling to images to dates. The PHP Foundation says it required a major change to the engine and took two months. [[github-php-src-fix-commit-3584a98bd, php-foundation-blog-security-release]]

For 7.4 the project did not carry that refactor back. It wrote a different, 17-file change that it labels "Minimal mitigation for EOL version": every memory error now ends the worker process at once, and the session upload-progress feature is switched off. [[github-php-src-branch-7.4-backport]] That closes the hole and makes the server restart more often. It is a different PHP from the one that ran the site the day before.

This is where the editor's other point comes in. In his words, "if you have a website that's been going for years, updating it is very risky." The fix itself is evidence for that: it adds two new settings with defaults (a hard memory ceiling and a cap on the parts of a form upload) and changes when a memory error is raised. [[github-php-src-fix-commit-3584a98bd]] A site that has run unchanged for a decade on large uploads or memory-hungry pages is the site most likely to meet those defaults. No captured source reports such a breakage yet. The risk is real, and so far unmeasured.

## Who actually got a fix

The NCSC-NL inventory, which tracks 674 products that ship or depend on PHP, shows how a fix really reaches a server. At 08:40 UTC on 22 October it counted 46 products fixed, 206 vulnerable and 418 still under investigation. [[ncsc-nl-php2shell-software-list]] Read row by row, the fixed ones fall into a handful of patterns.

- **Patched for you.** Google's App Engine Standard updates supported PHP runtimes automatically. The customer does nothing.
- **Fixed, if you rebuild.** Heroku, the official Docker image and Google's Cloud Run and App Engine Flexible all have, or need, fixed runtimes, but nothing already running changes until its owner rebuilds and redeploys it. Heroku even rebuilt end-of-life 8.1 with the emergency backport.
- **A system update.** Ubuntu, Debian, Arch and Red Hat backported the fix into the PHP versions they ship, so an ordinary update installs it.
- **Extended support for abandoned versions.** Canonical shipped fixes for PHP 5.5, 7.0, 7.2 and 7.4 to Ubuntu Pro customers. CloudLinux and TuxCare shipped fixed 7.4 builds for eleven platforms.
- **Your hosting panel.** cPanel backported to 7.4, 8.0 and 8.1. Plesk's end-of-life Linux builds and all its Windows builds were still affected, waiting, in Plesk's words, on "a PHP vendor fix", although official Windows binaries for the supported branches existed.

[[ncsc-nl-php2shell-software-list]]

So the editor's question has a partial answer: every version of PHP back to 5.5 can be patched, and some copies were, within a day. Whether a given copy was depended on who it came from.

## The editor's argument

The editor's brief makes an argument that this story should state rather than adopt. Updates, he says, are still pushed to everyone the same way, "are not personalized, are not customized to somebody", and "we push the whole responsibility of patching to the company that is running it". He argues for "more of a commercial relationship" with the PHP Foundation, or with "a company that provides the service ... that knows how to do this at scale". His brief is published in full on [the briefs page](/admin/briefs/index.html#2026-10-22__brief__research-stories-and-the-patching-story).

The inventory is a test of that argument, and it cuts both ways. The commercial relationship already exists: Canonical, TuxCare, CloudLinux, cPanel, Heroku and Google each patched someone's PHP who would otherwise have had nothing. [[ncsc-nl-php2shell-software-list]] But none of those relationships runs to the PHP project. The project fixed the versions it supports and published source for three it does not; the people who turned that source into something installable were companies that sell PHP to others. [[php-net-advisory]] And the customers the relationship does not reach are the ones the editor is worried about: the long-running site on a shared host whose panel had not shipped, or the container nobody has rebuilt since it was deployed. For them, the official advice is blunt. CISA tells anyone still on 8.1 or older to take the system offline until it is upgraded. [[cisa-alert-php-20261021]]

## What would settle it

- **How many sites run each version.** No captured source counts it. W3Techs publishes version shares and is first on the capture list.
- **What the fix breaks.** The first regression report against the new memory settings will say how much risk patching carried.
- **What extended support costs**, and who pays it. The inventory shows who sells it, not the price.
- **Whether the inventory's 418 "under investigation" rows turn into fixes or into "vulnerable"**, and how fast. That curve is the patching story, and this site will draw it as the inventory changes.

## About this story

A house story, written here by the journalist role against site v0.4.0, vault commit 200d08971937, data as of 11:34 UTC on 22 October 2026; the inventory figures are at its commit of 08:40 UTC. Facts carry their sources; the editor's argument is quoted from his brief and attributed to him; the sentences that weigh it are this writer's. It will not be revised. A later story will follow the inventory's statuses as they change.
