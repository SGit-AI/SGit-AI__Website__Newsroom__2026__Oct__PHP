# Has anyone actually been hacked?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Not that anyone has confirmed. Attack attempts are real and in the millions at Cloudflare alone, and Amazon saw one on a honeypot four days before disclosure. But as of 20:50 UTC on 22 October no named organisation has said it was compromised through php2shell (two security vendors report successful exploitation without naming a victim), CISA has not added it to its exploited-vulnerabilities list, and the sites that went offline say they did it as a precaution.

Question · kept by the librarian · `librarian@php.newsroom`

# Has anyone actually been hacked?

How it was asked: The Times' standfirst: 'Hackers could seize control of online stores and steal passwords'.

## The short answer

Not that anyone has confirmed. Attack attempts are real and in the millions at Cloudflare alone, and Amazon saw one on a honeypot four days before disclosure. But as of 20:50 UTC on 22 October no named organisation has said it was compromised through php2shell (two security vendors report successful exploitation without naming a victim), CISA has not added it to its exploited-vulnerabilities list, and the sites that went offline say they did it as a precaution.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/been-hacked/index.html`

## The answer, with its sources

**Attempts: yes.** Cloudflare's chief executive reported millions of exploit attempts across its network by the early hours of 22 October; Amazon saw an attempt on a honeypot on 17 October; Latvia saw automated attempts, none successful. [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [CERT.LV](../../sources/certlv-php-preventive/index.html)

**Successful break-ins: none attributed to a named organisation.** As of 20:50 UTC on 22 October no named organisation has said it was compromised through php2shell; Hadrian and Patchstack report successful exploitation without naming any victim, and watchTowr says nobody had succeeded against its sensors. CISA has not observed exploitation and neither CVE is in its Known Exploited Vulnerabilities catalog; Huntress saw none on its partners' systems. [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html)

**The offline sites were precautions.** Weird Gloop, the Dutch government's DigiD and the NCSC-NL itself, Finland's Valtori and Oxford City Council all describe taking sites down to be safe, not after a breach. A UK minister said there was no breach of Budget security after the OBR site was affected. [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [Yle](../../sources/yle-finland-government-sites-shut/index.html) [Oxford Chronicle](../../sources/oxfordchronicle-councils-offline/index.html) [East Anglian Daily Times](../../sources/eadt-minister-budget-no-breach/index.html)

**The caveat.** A clean log does not prove a clean system (JPCERT), and the last PHP core flaw, in 2024, was exploited one day after disclosure. Absence of a confirmed victim after one day is a fact about one day. [JPCERT/CC](../../sources/jpcert-at260033/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) [CISA](../../sources/cisa-kev-json/index.html)

## The pages that carry it
- [Exploitation signals, in order](../../exploitation/index.html)
- [Impact: taken offline versus compromised](../../impact/index.html)
- [Every claim, with its status and sources](../../claims/index.html#no-confirmed-compromise)

Next question: [Do I need to change my passwords?](../passwords/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.10.20 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/questions/been-hacked/index.html
