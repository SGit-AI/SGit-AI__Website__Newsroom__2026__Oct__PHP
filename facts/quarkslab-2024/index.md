# Fact: The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through O

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixed Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · discovery · confirmed

# The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixed

**Who says it:** PHP Foundation; Calif · **Sources:** [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html)

Two parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does.

## Fact-check

**A2** Reported●●○○○○ disputed status overstated · Attribution · verdict: **holds in part** · the status word overstates the evidence

Calif says Quarkslab's audit 'rediscovered the same OOM issue' and 'exploitation was not proven, hence the bug was not fixed', but Calif says it confirmed this 'from PHP', so it is not independent of the Foundation. The Foundation says something different: a PHP core developer found the OOM signs while fixing a Quarkslab finding, and the fix stalled over trade-offs and resources, not only unproven exploitation. Quarkslab's own summary describes no OOM finding. Run 6: Cloudflare's post was edited on 23 October ('Today,' became 'October 21,'); Quarkslab is still named, so the grade stands.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [php-foundation-blog-security-release](../../sources/php-foundation-blog-security-release/index.html) | partial | *While fixing one of the issues Quarkslab reported, a PHP core developer contracted by the PHP Foundation found the first signs of the OOM problem* | a1be057adc1c5bfa |
| [calif-php2shell](../../sources/calif-php2shell/index.html) | carries | *OSTIF and Quarkslab performed an audit of PHP and rediscovered the same OOM issue. However, exploitation was not proven, hence the bug was not fixed.* | 23afef81971778f9 |
| [quarkslab-blog-php-src-audit](../../sources/quarkslab-blog-php-src-audit/index.html) | absent | *This audit report contains two security issues currently redacted while PHP maintainers are actively working on the fixes.* | cd5ccdaf99da0be1 |
| [imperva-blog-php2shell](../../sources/imperva-blog-php2shell/index.html) | partial | *Reported by: Calif, Wiz, OpenAI, and Quarkslab.* | 3da873bdb21219a6 |
| [cloudflare-blog-php2shell-waf](../../sources/cloudflare-blog-php2shell-waf/index.html) | partial | *Today, Calif.io, Wiz, OpenAI and Quarkslab disclosed two* | 302408765abf45e3 |
| [cloudflare-blog-php2shell-waf](../../sources/cloudflare-blog-php2shell-waf/index.html) | carries | *October 21, Calif.io, Wiz, OpenAI and Quarkslab disclosed two vulnerabilities in PHP* | 94476de6ec0b31e0 |

Open tickets: [Finding-5](../../factcheck/index.html#Finding-5), [Finding-6](../../factcheck/index.html#Finding-6), [Finding-94](../../factcheck/index.html#Finding-94).

Graded in Run-1, resting on captures up to 2026-10-22 11:30 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21PHP Foundation publishes [Today's PHP Security Release, and How We're Strengthening PHP Security](../../sources/php-foundation-blog-security-release/index.html)
- 2026-10-21Calif publishes [php2shell by Calif Research — A tale of two PHP remote vulnerabilities](../../sources/calif-php2shell/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP Foundation
- 2026-10-22 08:10 UTCSaved into the evidence vault: Calif, then 1 more capture
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
RRowanJournalistAAshSecurity researcherBBlakeAnalyst or policy advisorRRileyCommunications team
And on [every claim](../../claims/index.html#quarkslab-2024).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixed
Who says it: PHP Foundation; Calif
Status: confirmed
Topic: discovery
Sources: php-foundation-blog-security-release, calif-php2shell
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/quarkslab-2024/index.html
