# Fact: The UK's NCSC, the NSA and their counterparts in the EU and Australia advise tak

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasible Who says it, its status (contradicted), its sources, and its timeline from publication to this site.

Fact · advice · contradicted

# The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasible

**Who says it:** BBC · **Sources:** [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html)

Australia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice.

## Fact-check

**A1** Weak signal●○○○○○ · Advice · verdict: **holds in part** · the status word understates the evidence

The captured BBC page does not say this: it says the NCSC 'as well as its counterparts in the EU and Australia' urged users 'to apply the fixes', and attributes the offline quote to the NCSC alone. On the substance, NCSC (after mitigations) and NSA advise offline, CERT-EU and CERT-FR advise isolation, and Italy's ACN advises taking sites offline; only Australia is not shown (ACSC's page as captured has no offline advice). 'Contradicted' overstates an absence for one of four parties and mislabels the BBC's statement.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [bbc-live-ckgel5xp2xv9t](../../sources/bbc-live-ckgel5xp2xv9t/index.html) | partial | *its counterparts in the EU and Australia, earlier urged those who use PHP to apply the fixes.* | c88b8c5f4c6bc07d |
| [acsc-alert-php](../../sources/acsc-alert-php/index.html) | absent | *Apply available security updates and other appropriate mitigations* | 9370af142ded6de9 |
| [certeu-sa-2026-018](../../sources/certeu-sa-2026-018/index.html) | carries | *Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified.* | c65c95cf165d9ed7 |
| [ncsc-nl-php2shell](../../sources/ncsc-nl-php2shell/index.html) | absent | *If immediate patching is not possible, follow PHP's temporary mitigations, including disabling session.upload_progress, restarting workers,* | f3eec24a226910fb |
| [acn-it-php2shell](../../sources/acn-it-php2shell/index.html) | carries | *si raccomanda di valutare di porre offline i siti e i servizi web che utilizzano versioni vulnerabili di PHP* | 19fac2edc25161cd |
| [jpcert-at260033](../../sources/jpcert-at260033/index.html) | absent | *十分なテストを実施の上、速やかに修正済みバージョンを適用してください。* | 1fea87241b307f92 |
| [ncsc-news-php](../../sources/ncsc-news-php/index.html) | carries | *or applying them would take too long, you should consider taking the system offline until it can be fully mitigated.* | a18ceeb011a3fe6f |
| [nsa-press-php-4630238](../../sources/nsa-press-php-4630238/index.html) | carries | *If an immediate update is not feasible, it is recommended that organizations take the system offline until it can be fully mitigated.* | 8a8553ea1ffcd794 |
| [certfr-2026-ale-014](../../sources/certfr-2026-ale-014/index.html) | carries | *Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue* | f9e9557ab49ddb95 |

Open tickets: [Finding-43](../../factcheck/index.html#Finding-43), [Finding-44](../../factcheck/index.html#Finding-44), [Finding-45](../../factcheck/index.html#Finding-45), [Finding-87](../../factcheck/index.html#Finding-87).

Graded in Run-1, resting on captures up to 2026-10-22 08:48 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21ACSC publishes [Critical vulnerabilities in PHP](../../sources/acsc-alert-php/index.html)
- 2026-10-21ACN / CSIRT Italia publishes [PHP2Shell: sanate vulnerabilità critiche in PHP (AL07/261021/CSIRT-ITA)](../../sources/acn-it-php2shell/index.html)
- 2026-10-21 15:20 UTCCERT-EU publishes [Security Advisory 2026-018: Critical Vulnerabilities in PHP](../../sources/certeu-sa-2026-018/index.html)
- 2026-10-21 15:25 UTCNCSC-NL publishes [NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities](../../sources/ncsc-nl-php2shell/index.html)
- 2026-10-22JPCERT/CC publishes [PHPにおける複数の脆弱性（CVE-2026-109618、CVE-2026-109619）に関する注意喚起 (JPCERT-AT-2026-0033)](../../sources/jpcert-at260033/index.html)
- 2026-10-22 06:16 UTCBBC News publishes [PHP: Global scramble to fix critical cyber-security flaws as many websites taken offline - follow live](../../sources/bbc-live-ckgel5xp2xv9t/index.html)
- 2026-10-22 08:04 UTCSaved into the evidence vault: BBC News, then 2 more captures
- 2026-10-22 08:09 UTCSaved into the evidence vault: NCSC-NL, then 1 more capture
- 2026-10-22 08:13 UTCSaved into the evidence vault: CERT-EU
- 2026-10-22 08:13 UTCSaved into the evidence vault: ACN / CSIRT Italia
- 2026-10-22 08:16 UTCSaved into the evidence vault: ACSC
- 2026-10-22 08:17 UTCSaved into the evidence vault: JPCERT/CC
- 2026-10-22Enters this site as contradicted in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerTTaylorProject or programme managerJJordanBoard member or executiveSSamSecurity leadRRowanJournalistRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecRRileyCommunications team
And on [every claim](../../claims/index.html#offline-allies).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · contradicted
```
The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasible
Who says it: BBC
Status: contradicted
Topic: advice
Sources: bbc-live-ckgel5xp2xv9t, acsc-alert-php, certeu-sa-2026-018, ncsc-nl-php2shell, acn-it-php2shell, jpcert-at260033
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/offline-allies/index.html
