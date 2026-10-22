---
slug: where-php2shell-stands
title: Where php2shell stands: many sites dark, millions of attempts, no confirmed breach
dek: A state-of-affairs report on the two PHP flaws, written against the evidence vault as it stood at site v0.2.5: what is settled, where the alarm and the evidence part company, and the five things that would change the story.
role: journalist
author: claude-journalist
written: 2026-10-22
as_of_version: 0.2.5
vault_commit: 200d08971937
data_as_of: 2026-10-22T11:34Z
---

**22 October 2026.** About twenty-one hours after the PHP project shipped fixes for two critical flaws in its engine, the story has split in two. One half is a story of alarm: national agencies telling organisations to pull systems offline, governments darkening their own websites, a CDN chief counting exploit attempts in the millions. The other half is the evidence of harm, and at the time of writing it contains no named victim. This report is about the distance between those two halves, and it is written from the 144 sources this site has captured, hashed and dated, not from memory or from other reporting.

## What is settled

There are two flaws, CVE-2026-109618 and CVE-2026-109619, nicknamed php2shell. Both are rated CVSS v4.0 9.2, not the 10.0 that circulated before release, and both are fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. [[cve-cve-2026-109618, cve-cve-2026-109619, github-ghsa-w8hw-w9fx-j79w, php-net-advisory]]

Both bugs live in the C engine, not in anybody's application code: one in the way PHP abandons a request when it runs out of memory, the other in global state that outlives a failed request. The fix replaces the old bailout on out-of-memory with a delayed, graceful stop. [[github-php-src-fix-commit-3584a98bd, github-ghsa-6wmf-4rv5-p3rp]]

Unauthenticated remote code execution was demonstrated against Apache with mod_php under default settings, before any application code runs. Whether a complete exploit exists for PHP-FPM, the more common modern setup, is the one technical point on which the two primary accounts disagree. [[github-ghsa-w8hw-w9fx-j79w, php-foundation-blog-security-release]] The site keeps that as [a disputed claim](/claims/index.html#rce-fpm) rather than picking a side.

Updating is the only complete fix. The PHP project says so in as many words; the configuration workarounds reduce exposure on specific paths and do not make an installation safe. [[php-net-advisory, openwall-oss-security-2026-10-21-7]]

## The alarm

The NSA posted at 13:45 UTC on 21 October, before the CVE records were even published, telling operators to be ready to take systems offline. [[nsa-x-2112903220209098897]] CISA followed with the same advice for anyone who could not patch immediately or ran PHP 8.1 or older. [[cisa-alert-php-20261021]]

Operators listened. The Dutch NCSC took its own website offline as a precaution, with DigiD, MijnOverheid and Overheid.nl, and the Dutch government said there were no signs of active exploitation of those services. [[rijksoverheid-ncsc-php-news]] Latvia restricted access from abroad to several state resources and said so itself. [[certlv-php-preventive]] Weird Gloop switched off its wiki servers for thirteen hours, its longest outage ever, and still served about 94% of page views from cache. [[weirdgloop-blog-php2shell]] Finland, Wikimedia, Edinburgh, Oxford and a list of UK public bodies are reported offline by the press; those organisations' own statements have mostly not been captured, and where they have, Oxford called it a precaution, "not a cyber incident". [[yle-finland-government-sites-shut, cnn-php2shell-websites-shut, scotsman-edinburgh-council-offline, oxfordchronicle-councils-offline]]

The site's [impact ledger](/impact/index.html) counts ten operators or groups reported offline. Three are confirmed by the operator or its government. None of them, where a reason is given, describes a breach: the reasons given are precaution and, in Edinburgh, "essential maintenance".

## The evidence of harm

Here is everything in the vault that describes exploitation, in descending order of strength.

- **Attempts, at scale, from the parties positioned to see them.** Cloudflare's chief executive counted thousands of attempts in the ten hours before the announcement, tens of thousands within 45 minutes after and "millions now" by 01:25 UTC on 22 October. [[x-eastdakota-php2shell-stats]] Amazon says php2shell is "now being broadly exploited in the wild", and in the same post: "It's unclear if any of these attempts would have succeeded in real-world systems." Its evidence is honeypot telemetry. [[aws-security-blog-madpot]]
- **Attempts, before disclosure.** One exploit attempt reached an Amazon honeypot on 17 October, four days before release, from an anonymisation network. How the actor knew is, in Amazon's words, unclear. [[aws-security-blog-madpot, thehackernews-php2shell-4days]]
- **Agencies that have seen attempts but no success.** Latvia saw automated attempts, none successful. Australia is not aware of successful exploitation in Australia. [[certlv-php-preventive, acsc-alert-php]]
- **One agency that says more.** New Zealand's NCSC is "aware of reports of active exploitation", and does not say whose. It is the only national agency in the vault to say so. [[ncsc-nz-alert-php]]
- **Negative findings.** CISA has not observed exploitation and has not added either CVE to its Known Exploited Vulnerabilities catalog. Huntress saw nothing on its partners' systems as of 20:30 UTC on 21 October. Imperva saw no matching traffic during its embargoed monitoring. [[cisa-alert-php-20261021, cisa-kev-json, huntress-php2shell-rapid-response, imperva-blog-php2shell]]

There is also a quieter signal that cuts against the alarm. A detection author citing VulnCheck reports that none of the public proof-of-concept exploits it reviewed has the correct mechanism, and a lab reproduction of the leaked proof of concept's precondition produced a clean HTTP 200. [[github-rjmendez-phpup-2026, huntress-php2shell-rapid-response]] The vendors who tried say triggering the bug is far easier than turning it into code execution, which is what the "attack complexity high" in the CVSS vector says too. [[imperva-blog-php2shell, fastly-blog-php2shell]]

What is missing is the sentence every reader is looking for: a named organisation saying it was compromised through php2shell. No captured source carries one. That is a [confirmed absence](/claims/index.html#no-confirmed-compromise), counted across every source, not an assumption.

## The number that started this site

The editor's first question was about "70% of the Internet". It is a Wiz headline and X post. The body of the same Wiz post, Cloudflare and OpenAI all say something different: that PHP runs about 70% of *websites*, which is a usage survey's figure, not an exposure count. [[x-wiz-io-php2shell, wiz-blog-php2shell, cloudflare-blog-php2shell-waf, x-openai-php2shell]] None of them names the measurement. The counts that do name one are a thousand times smaller: VulnCheck's 2.6 million internet-facing hosts, of which Censys counted 1.57 million unpatched on 21 October, and Latvia's 6,000 resources in one country. [[thehackernews-php2shell-4days, securityweek-exploitation-days-before, certlv-php-preventive]] The [numbers page](/numbers/index.html) keeps all six figures side by side; this report repeats only the conclusion. They do not contradict each other. They count different things, and only one of them is an exposure count.

## How the release broke

The coordinated release was set for 22 October. On 20 October around 15:00 UTC the two CVE IDs began circulating with a wrong time and a wrong score; the PHP Foundation says no technical detail leaked. [[php-foundation-blog-security-release]] At about 20:00 UTC Calif, one of the finders, published and then deleted a video of its proof of concept, and the Foundation says copies sped up the public exploit work. [[phpfoundation-blog-security-release-leak]] The release was pulled forward a day. At 07:41 UTC on 21 October Chainguard shipped patched container images, more than six hours early; the Foundation calls it an embargo break, and Chainguard's chief executive accepts the time and denies leaking. [[php-foundation-blog-security-release, theregister-php-blames-chainguard]] That dispute is [open on the site](/claims/index.html#chainguard), and this report does not close it.

The finding itself was AI-assisted and claimed three ways. Calif reported first, on 11 August, after posting a hash of its finding on 5 August; OpenAI reported the same root cause the same day; Wiz found it independently on 19 August. [[calif-php2shell, x-lcfr-hax-hash-tweet, php-foundation-blog-security-release, wiz-blog-php2shell]] The underlying out-of-memory problem had been seen in a 2024 audit and left unfixed because nobody could show it was exploitable. [[php-foundation-blog-security-release]]

## The agencies do not agree

All say patch. On what to do with a system that cannot be patched today, they split. The NSA and CISA say take it offline. The UK NCSC lists offline fourth of six steps. CERT-EU, Canada and France say isolate. Australia, the Netherlands, Italy, Japan and New Zealand give no offline advice at all. [[nsa-press-php-4630238, ncsc-news-php, certeu-sa-2026-018, cccs-al26-026, certfr-2026-ale-014, acsc-alert-php, ncsc-nl-php2shell]] The BBC's morning summary, that the UK, US, EU and Australian agencies all advise taking systems offline, holds for the NSA, simplifies the NCSC and is not supported by the Australian page; the site marks it [contradicted](/claims/index.html#offline-allies).

## Five things that would change this story

1. **CISA adds either CVE to the KEV catalog.** That is the clearest public signal that exploitation of real victims, not sensors, has been seen. The last PHP core flaw was listed within three days. [[cisa-kev-json, akamai-blog-cve-2024-4577-one-day]]
2. **A named organisation confirms a compromise.** Until then, every outage in the ledger is a precaution.
3. **The fix turns out to be incomplete.** A Fediverse report of a third bug reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. [[openwall-oss-security-109619-thread]] Fastly expects more paths into the same mechanism. [[fastly-blog-php2shell]]
4. **A working public exploit for PHP-FPM.** That would move the exposure from the mod_php minority to the common case.
5. **Someone publishes how "70%" was measured.**

## About this report

This is a dated article, not a page of the site. It was written by the journalist role against site v0.2.5, evidence vault commit 200d08971937, with data as of the latest capture at 11:34 UTC on 22 October 2026, and it will not be edited to look right later. Where the evidence moves, a new article will say so, and the front page and the [claims](/claims/index.html) are rebuilt from the vault on every release. Every source tag is a capture you can inspect on [every source](/sources/index.html); sentences without one are this writer's summary of the cited material.
