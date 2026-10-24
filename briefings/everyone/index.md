# Briefing for a curious reader: What happened, does it affect me, and should I worry?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell story for a curious reader: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.

Briefing for Alex, curious reader · ******Plain English · from the same 70 claims, selected and ordered for one reader

# What happened, does it affect me, and should I worry?

A
The answer in thirty seconds

Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. As of the evening of 22 October, no named organisation has said it was compromised through php2shell.

[Read the site as Alex →](../../explained/index.html)

You do not need to know anything about computers to follow this. Below are the five things worth knowing, then the evidence behind them, folded away until you want it.

## What to decide or do
- **PHP is not on your phone or laptop.** It runs on the servers that build websites. This is a problem for the organisations that run those websites, and it is theirs to fix.
- **Nothing to install, nothing to change** on your own devices because of this. Be wary of any message that says otherwise and asks you to click or download something: scammers use headlines like this one.
- **If a website you use was down on 21 or 22 October, it was most likely a precaution.** Dutch government services such as DigiD were taken offline on purpose, as a precaution; that is a decision, not a sign of a break-in.
- **Nobody has confirmed being hacked through this yet.** Attackers have been trying, in large numbers, and that may change; this site will say so when the evidence does.
- **The big numbers in the headlines are not what they sound like.** 70% is roughly the share of websites built with PHP, not a share of the Internet that is broken. [The numbers page](../../numbers/index.html) explains each one.

## Your reading path
- [Your briefing](../../briefings/everyone/index.html) 4 min
- [Explained from the start](../../explained/index.html) 6 min
- [Impact: offline vs compromised](../../impact/index.html) 2 min
- [The numbers](../../numbers/index.html) 2 min

About 14 minutes in all. Choose *read as Alex* and the bar under the menu keeps your place on every page.

### What this briefing covers
- what PHP is, in one sentence
- whether their own phone or laptop is at risk
- why websites went offline
- whether anyone was actually hacked

### What you can skip
- version numbers
- server settings
- the code

## Words you will meet

[PHP](../../glossary/index.html#php)[php2shell](../../glossary/index.html#php2shell)[Primary source](../../glossary/index.html#primary)[Exploit, exploitation](../../glossary/index.html#exploit)[NCSC](../../glossary/index.html#ncsc)[Web server](../../glossary/index.html#web-server)[Remote code execution (RCE)](../../glossary/index.html#rce)[Evidence vault](../../glossary/index.html#vault)[Patch](../../glossary/index.html#patch)[CVE](../../glossary/index.html#cve)[KEV](../../glossary/index.html#kev)[CISA](../../glossary/index.html#cisa)[Proof of concept (PoC)](../../glossary/index.html#poc)[Honeypot](../../glossary/index.html#honeypot)

Each is underlined where it first appears; hover or tap for a one-line definition, or open [the glossary](../../glossary/index.html).

## The facts this rests on
Show the 29 claims behind this briefing, each with its status and sources- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. [fact timeline →](../../facts/latvia-offline/index.html) | CERT.LV | confirmed | **A6** Established●●●●●● | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| The Dutch NCSC took its own site offline as a precaution, as did DigiD, MijnOverheid and Overheid.nl, with no signs of active exploitation of those servicesPrimary statement. [fact timeline →](../../facts/nl-offline/index.html) | the Dutch government | confirmed | **A3** Echoed●●●○○○ status overstated | 1/2 (1 blocked) | [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [Dutch IT Leaders](../../sources/dutchitleaders-websites-offline/index.html) |
| Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of page views from cachePrimary, and the one outage with a measured cost. [fact timeline →](../../facts/weirdgloop-13h/index.html) | Weird Gloop | confirmed | **A2** Reported●●○○○○ status overstated | 1/1 | [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. [fact timeline →](../../facts/affected-sites/index.html) | BBC | reported | **A2** Reported●●○○○○ | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| As of 20:50 UTC on 22 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, and two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same). Attempts are not compromises: watchTowr says "nobody has been successful to date"; Amazon says it is unclear whether any attempt would have succeeded on real systems; Patchstack's incidents are reports from hosting partners with no victim named. Source watch (vault oq9gflln), pending promotion into the evidence vault: the PHP Foundation's executive director told The Verge and WIRED "to our knowledge, there has been no successful attempt at remote code execution" (raw/us/tech-press/the-verge/php2shell-websites-down/); officials in Germany, the Netherlands and Japan say they have not seen an attack succeed (The Next Web, raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/); GMO confirmed a break-in on 20 October on its FX trading VPS service (26,739 servers, logins possibly taken) without stating the cause (raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/); Czech Technical University says it stopped an active attack that was part of worldwide attempts against PHP sites, success not established (raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/); Valtec in Japan blamed php2shell for a break-in, then retracted: its own service's flaw (raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/); Fortune reports an anonymous startup owner alleging stolen source code, unnamed and not attributed to the flaw. Edited by researcher@php.newsroom. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault and the source watch, as of 20:50 UTC on 22 October | reported | **A4** Corroborated●●●●○○ status overstated | 6/9 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time on 21 October as a precaution [fact timeline →](../../facts/fi-offline/index.html) | Yle; Helsinki Times, quoting Valtori | reported | **A2** Reported●●○○○○ | 0/2 | [Yle](../../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../../sources/helsinkitimes-finland-shutdown/index.html) |
| The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely patched'No Wikimedia-published statement captured. [fact timeline →](../../facts/wikimedia-precaution/index.html) | the Foundation, as quoted by CNN and The Cyber Express | reported | **A4** Corroborated●●●●○○ | 0/2 | [CNN](../../sources/cnn-php2shell-websites-shut/index.html) [The Cyber Express](../../sources/cyberexpress-php2shell-gov-sites/index.html) |
| Edinburgh council's site went offline late on 21 October; the council called it 'essential maintenance' and did not confirm a link [fact timeline →](../../facts/edinburgh/index.html) | The Scotsman quoting the council | reported | **A3** Echoed●●●○○○ | 0/1 | [The Scotsman](../../sources/scotsman-edinburgh-council-offline/index.html) |
| Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident' [fact timeline →](../../facts/oxford/index.html) | the council's social post, via Oxford Chronicle | reported | **A2** Reported●●○○○○ | 0/1 | [Oxford Chronicle](../../sources/oxfordchronicle-councils-offline/index.html) |
| Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility were unavailable; Bristol, Lambeth and Barnet council sites showed errors [fact timeline →](../../facts/uk-list/index.html) | LBC; Insurance Business | reported | **A3** Echoed●●●○○○ | 0/2 | [LBC](../../sources/lbc-uk-websites-offline/index.html) [Insurance Business](../../sources/insurancebusiness-uk-councils-met/index.html) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. [fact timeline →](../../facts/cisa-none/index.html) | CISA | confirmed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | **A5** Confirmed●●●●●○ | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayCounted from the captured catalog. [fact timeline →](../../facts/kev-precedent/index.html) | CISA KEV catalog; Akamai (2024) | confirmed | **A2** Reported●●○○○○ status overstated | 3/3 | [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |
| There is no evidence yet that hackers have exploited the flaw [fact timeline →](../../facts/no-exploitation/index.html) | Ryan Austin, Calif, on Radio 4, 08:00 BST 22 October | reported | **A2** Reported●●○○○○ disputed | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Reports of active exploitation existThe only agency saying so, and it does not say whose reports. [fact timeline →](../../facts/nz-active/index.html) | NCSC New Zealand | reported | **A2** Reported●●○○○○ disputed | 1/1 | [NCSC New Zealand](../../sources/ncsc-nz-alert-php/index.html) |
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims. [fact timeline →](../../facts/amazon-honeypot/index.html) | Amazon (CJ Moses, AWS Security Blog) | reported | **A2** Reported●●○○○○ disputed | 1/2 | [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |
| Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloadsPrimary party, no volumes. [fact timeline →](../../facts/cloudflare-traffic/index.html) | Cloudflare | reported | **A2** Reported●●○○○○ | 1/1 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. [fact timeline →](../../facts/latvia-attempts/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Exploit attempts across Cloudflare's network: thousands in the ten hours before announcement, tens of thousands within 45 minutes after, hundreds of thousands within two hours, millions by 22 October 01:25 UTCPrimary party. Attempts, not compromises; no blocked count; 1.4 million views at capture. [fact timeline →](../../facts/cf-millions/index.html) | Matthew Prince, Cloudflare CEO, on X | reported | **A2** Reported●●○○○○ measures differently | 1/1 | [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) |
| No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosure monitoringA negative finding from a party that had the details under embargo. [fact timeline →](../../facts/imperva-none/index.html) | Imperva Threat Research | reported | **A2** Reported●●○○○○ measures differently | 1/1 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) |
| No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code known to Huntress [fact timeline →](../../facts/huntress-none/index.html) | Huntress | reported | **A2** Reported●●○○○○ disputed | 1/1 | [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |
| Criminals are using AI to 'vibe code' an attack method [fact timeline →](../../facts/vibe-code/index.html) | unnamed researchers, via the BBC | unverified | **A1** Weak signal●○○○○○ opinion | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| watchTowr sees active exploitation attempts and lists the flaws as exploited in the wildwatchtowr.com returns HTTP 403 to this site's capture tool; known only from search summaries. [fact timeline →](../../facts/watchtowr-itw/index.html) | watchTowr | unverified | **A4** Corroborated●●●●○○ superseded | 2/2 | [watchTowr](../../sources/watchtowr-php2shell/index.html) [watchTowr](../../sources/watchtowr-php2shell-faq/index.html) |
| 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerableCounted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'. [fact timeline →](../../facts/scale-ncsc-nl/index.html) | NCSC-NL, counted by this site from the file at commit cca173c64ec5 | confirmed | **A1** Weak signal●○○○○○ contradicted status overstated | 1/1 | [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html) |
| PHP is used by almost 70% of websitesNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. [fact timeline →](../../facts/scale-70pc-websites/index.html) | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | **A2** Reported●●○○○○ measures differently | 3/3 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Something like 30 million websites could be affectedNo basis given. [fact timeline →](../../facts/scale-30m/index.html) | Alan Woodward, via the BBC | reported | **A2** Reported●●○○○○ | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| PHP is exposed on about 2.6 million internet-facing hosts, of which Censys counted 1.57 million unpatched on 21 OctoberCensys: 2.58 million hosts seen, 1.58 million reporting a version, 1.57 million not patched; nearly 3 million by 22 October. VirusTotal: 5.1 million IPs running PHP, 1.1 million announcing a version. Unit 42: 22.6 million systems that 'could be vulnerable' (via Insurance Business). Censys's own post was not found. [fact timeline →](../../facts/scale-2.6m-hosts/index.html) | VulnCheck and Censys, via The Hacker News and SecurityWeek | reported | **A2** Reported●●○○○○ measures differently | 0/2 | [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) |
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. [fact timeline →](../../facts/scale-latvia/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Roughly 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. [fact timeline →](../../facts/scale-70pc-internet/index.html) | Wiz (headline, X post); BBC attributing Wiz | unverified | **A1** Weak signal●○○○○○ measures differently | 2/3 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |

Every sentence above rests on these rows. They are folded away because they are written in the sources' own vocabulary; the glossary explains each term.

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other readers: [Website owner](../site-owner/index.html) · [Project or programme manager](../pm/index.html) · [Board member or executive](../board/index.html) · [Security lead](../security/index.html) · [PHP or platform engineer](../engineer/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or policy advisor](../analyst/index.html) · [CISO](../ciso/index.html) · [CTO](../cto/index.html) · [CFO](../cfo/index.html) · [Data protection officer](../dpo/index.html) · [Head of AppSec](../appsec/index.html) · [Developer](../developer/index.html) · [Communications team](../comms/index.html).


---
site v0.11.1 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/index.html
