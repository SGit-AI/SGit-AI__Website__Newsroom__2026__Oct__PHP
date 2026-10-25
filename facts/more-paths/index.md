# Fact: Patching the demonstrated paths does not make the bailout mechanism safe; more p

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expected Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · technical · reported

# Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expected

**Who says it:** Fastly · **Sources:** [Fastly](../../sources/fastly-blog-php2shell/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html)

A position, from a vendor; consistent with the Fediverse report of a third bug.

## Fact-check

**A2** Reported●●○○○○ opinion · Opinion · verdict: **holds**

Fastly's post says nearly these words; it is one vendor's position (a reading), so A2. The second cited source (the oss-security thread) does not carry it. 'Reported' fits.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [fastly-blog-php2shell](../../sources/fastly-blog-php2shell/index.html) | carries | *Patching the specific paths that researchers demonstrated does not make the mechanism safe.* | bacf27615fe1180a |
| [fastly-blog-php2shell](../../sources/fastly-blog-php2shell/index.html) | carries | *Expect in-the-wild attacks and novel variants to emerge this week and next at minimum.* | bacf27615fe1180a |
| [openwall-oss-security-109619-thread](../../sources/openwall-oss-security-109619-thread/index.html) | absent | *While not yet fully confirmed, the Fediverse is reporting that the fix to at least PHP 8.5.12 may be incomplete:* | 6a76141ae5a06584 |
| [github-php-src-fix-commit-3584a98bd](../../sources/github-php-src-fix-commit-3584a98bd/index.html) | partial | *- Replace bailout on OOM with UnwindExit* | 26bed812bcc7c89e |

Open tickets: [Contradiction-11](../../factcheck/index.html#Contradiction-11), [Evidence-7](../../factcheck/index.html#Evidence-7), [Finding-54](../../factcheck/index.html#Finding-54), [Finding-55](../../factcheck/index.html#Finding-55).

Graded in Run-1, resting on captures up to 2026-10-22 11:19 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Fastly publishes [Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly](../../sources/fastly-blog-php2shell/index.html)
- 2026-10-21 15:24 UTCoss-security publishes [Re: CVE-2026-109619 thread (21/16, 21/17, 21/23, 22/2)](../../sources/openwall-oss-security-109619-thread/index.html)
- 2026-10-22 11:19 UTCSaved into the evidence vault: Fastly, then 1 more capture
- 2026-10-22Enters this site as reported in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#more-paths).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · reported
```
Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expected
Who says it: Fastly
Status: reported
Topic: technical
Sources: fastly-blog-php2shell, openwall-oss-security-109619-thread
```


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/more-paths/index.html
