# Fact: None of the public proof-of-concept exploits reviewed by VulnCheck has the corre

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200 Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · technical · reported

# None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200

**Who says it:** rjmendez (detection author) citing VulnCheck; Huntress · **Sources:** [rjmendez, GitHub](../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html)

The Hacker News says the same of the public code. Fastly: working RCE needs knowledge of the running binary's layout on x86_64.

## Fact-check

**A1** Weak signal●○○○○○ status overstated · Attribution · verdict: **holds** · the status word overstates the evidence

rjmendez's README carries both halves, but the VulnCheck half is second-hand (VulnCheck's review is not captured), so A1; the lab half is rjmendez's own (A2). Huntress, the second cited source, does not carry either half. 'Reported' implies one named party checked first-hand, which only the lab half has.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [github-rjmendez-phpup-2026](../../sources/github-rjmendez-phpup-2026/index.html) | carries | *a clean 200 OK, and VulnCheck independently reports that none of the public PoCs they reviewed have the correct mechanism.* | 84742b6e86fb259d |
| [huntress-php2shell-rapid-response](../../sources/huntress-php2shell-rapid-response/index.html) | absent | *We have not built or reproduced a proof of concept for these vulnerabilities, and we're not aware of public exploit code as of this writing.* | a83d744768109a61 |
| [fastly-blog-php2shell](../../sources/fastly-blog-php2shell/index.html) | partial | *the existing PoCs require knowledge of the specific, running PHP binary and address space layout on the server* | bacf27615fe1180a |
| [thehackernews-what-protects-you](../../sources/thehackernews-what-protects-you/index.html) | partial | *the public exploit code going around has not been shown to work* | 2301d254784fd661 |

Open tickets: [Finding-52](../../factcheck/index.html#Finding-52), [Finding-91](../../factcheck/index.html#Finding-91), [Gap-3](../../factcheck/index.html#Gap-3).

Graded in Run-1, resting on captures up to 2026-10-22 11:28 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21rjmendez, GitHub publishes [GitHub - rjmendez/phpup-2026: IOCs and detection rules for CVE-2026-109618 / CVE-2026-109619 (PHP session.uplo](../../sources/github-rjmendez-phpup-2026/index.html)
- 2026-10-21Huntress publishes [Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress](../../sources/huntress-php2shell-rapid-response/index.html)
- 2026-10-22 11:20 UTCSaved into the evidence vault: rjmendez, GitHub
- 2026-10-22 11:28 UTCSaved into the evidence vault: Huntress
- 2026-10-22Enters this site as reported in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#pocs-wrong).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · reported
```
None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200
Who says it: rjmendez (detection author) citing VulnCheck; Huntress
Status: reported
Topic: technical
Sources: github-rjmendez-phpup-2026, huntress-php2shell-rapid-response
```


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/pocs-wrong/index.html
