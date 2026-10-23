# ISO/IEC 29147 and 30111: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each ISO/IEC 29147 and 30111 clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / ISO/IEC 29147 and 30111

# ISO/IEC 29147 and 30111: the php2shell risks it governs

The standards for exactly what broke on 20 and 21 October: receiving reports from several finders, keeping an embargo, coordinating a release and publishing the advisory.

**Full name** ISO/IEC 29147:2018 Vulnerability disclosure and ISO/IEC 30111:2019 Vulnerability handling processes · **Publisher** ISO and IEC · **Version** 2018 and 2019 · [the official text](https://www.iso.org/standard/72311.html)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **29147:receipt** | Receiving vulnerability reports and acknowledging the finder | [R08-2 Several finders, one small team](../../../grc/risks/r08-2/index.html) **12** high | [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) |
| **29147:coordination** | Coordinating disclosure with other vendors and parties under embargo | [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) **20** critical [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) **20** critical [R02-2 Early mitigation advice to a few providers leaked](../../../grc/risks/r02-2/index.html) **9** medium [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) **16** high | [The PHP security team](../../../grc/stakeholders/php-security-team/index.html), [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) |
| **29147:advisory** | Publishing the advisory: affected versions, remediation, credit | *no risk mapped* |  |
| **30111:handling** | Investigating, remediating and releasing the fix, and learning from it | [R01-4 The fix is incomplete, or a third flaw follows](../../../grc/risks/r01-4/index.html) **15** high | [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) |


---
site v0.9.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/iso29147/index.html
