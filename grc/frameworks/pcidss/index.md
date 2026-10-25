# PCI DSS: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each PCI DSS clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / PCI DSS

# PCI DSS: the php2shell risks it governs

Online shops were among the sites taken offline; most run PHP (Magento, WooCommerce) and take cards.

**Full name** Payment Card Industry Data Security Standard v4.0.1 · **Publisher** PCI Security Standards Council · **Version** 4.0.1 · [the official text](https://www.pcisecuritystandards.org/document_library/)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **6.3.1** | Security vulnerabilities are identified, risk-ranked and managed | [R01-5 Popular applications compromised before authentication](../../../grc/risks/r01-5/index.html) **15** high | [Website owner](../../../grc/stakeholders/site-owner/index.html) |
| **6.3.3** | Critical security patches are installed within one month of release | [R01-1 Default Apache mod_php installations exploited before application code runs](../../../grc/risks/r01-1/index.html) **15** high [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) **20** critical | [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html), [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **6.4.2** | An automated technical solution that detects and prevents web attacks protects public-facing web applications | [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) **16** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **12.10.1** | An incident response plan exists and is ready to be activated | [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) **15** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |


---
site v0.21.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/pcidss/index.html
