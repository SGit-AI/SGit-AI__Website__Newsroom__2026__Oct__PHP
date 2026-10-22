# Briefing for a board member or executive: Are we exposed, what is it costing us, and who owns the decision to pull a system?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell story for a board member or executive: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.

Briefing for Jordan, board member or executive · ******Plain English · from the same 70 claims, selected and ordered for one reader

# Are we exposed, what is it costing us, and who owns the decision to pull a system?

J
The answer in thirty seconds

A critical flaw in software that runs many websites, fixed on 21 October. Every agency says update first; some say take systems offline if you cannot. No named organisation has confirmed a break-in. Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast.

[Read the site as Jordan →](../../explained/index.html)

Three decisions sit with you: whether the organisation is exposed, what it costs to find out, and who may pull a system. The facts below are the ones those decisions turn on. Everything marked *reported* is one party's word; nothing below is a confirmed compromise anywhere.

## What to decide or do
- Do we have an inventory of every system serving PHP, including vendor products? If not, that is the first spend.
- Has every internet-facing system been patched and restarted, and has the running version been checked after the restart?
- Who is authorised to take a system offline, how long does it take, and has it been rehearsed?
- What would a compromise of our most exposed PHP system reach: which data, which credentials, which other systems?
- What is our evidence that we were not exploited between the leak on 20 October and our patch?

## Your reading path
- [Your briefing](../../briefings/board/index.html) 3 min
- [Explained from the start](../../explained/index.html) 6 min
- [Impact: offline vs compromised](../../impact/index.html) 2 min
- [The agencies](../../agencies/index.html) 1 min
- [If you run PHP](../../playbook/index.html) 3 min

About 15 minutes in all. Choose *read as Jordan* and the bar under the menu keeps your place on every page.

### What this briefing covers
- are we exposed
- who owns the decision to take a system offline
- what to ask the CISO
- which headline figures not to use

### What you can skip
- SAPIs and settings
- the C code
- the leak forensics

## Words you will meet

[PHP](../../glossary/index.html#php)[Patch](../../glossary/index.html#patch)[Exploit, exploitation](../../glossary/index.html#exploit)[SAPI](../../glossary/index.html#sapi)[Primary source](../../glossary/index.html#primary)[CVE](../../glossary/index.html#cve)[KEV](../../glossary/index.html#kev)[CISA](../../glossary/index.html#cisa)[php2shell](../../glossary/index.html#php2shell)[Remote code execution (RCE)](../../glossary/index.html#rce)[NCSC](../../glossary/index.html#ncsc)[Proof of concept (PoC)](../../glossary/index.html#poc)[Honeypot](../../glossary/index.html#honeypot)[Coordinated disclosure](../../glossary/index.html#disclosure)

Each is underlined where it first appears; hover or tap for a one-line definition, or open [the glossary](../../glossary/index.html).

## The facts this rests on
Show the 35 claims behind this briefing, each with its status and sources- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

| Claim | Who says it | Status | Primary | Sources |
|---|---|---|---|---|
| 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerableCounted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'. [fact timeline →](../../facts/scale-ncsc-nl/index.html) | NCSC-NL, counted by this site from the file at commit cca173c64ec5 | confirmed | 1/1 | [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html) |
| PHP is used by almost 70% of websitesNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. [fact timeline →](../../facts/scale-70pc-websites/index.html) | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | 3/3 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Something like 30 million websites could be affectedNo basis given. [fact timeline →](../../facts/scale-30m/index.html) | Alan Woodward, via the BBC | reported | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| PHP is exposed on about 2.6 million internet-facing hosts, of which Censys counted 1.57 million unpatched on 21 OctoberCensys: 2.58 million hosts seen, 1.58 million reporting a version, 1.57 million not patched; nearly 3 million by 22 October. VirusTotal: 5.1 million IPs running PHP, 1.1 million announcing a version. Unit 42: 22.6 million systems that 'could be vulnerable' (via Insurance Business). Censys's own post was not found. [fact timeline →](../../facts/scale-2.6m-hosts/index.html) | VulnCheck and Censys, via The Hacker News and SecurityWeek | reported | 0/2 | [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) |
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. [fact timeline →](../../facts/scale-latvia/index.html) | CERT.LV | reported | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Roughly 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. [fact timeline →](../../facts/scale-70pc-internet/index.html) | Wiz (headline, X post); BBC attributing Wiz | unverified | 2/3 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. [fact timeline →](../../facts/cisa-none/index.html) | CISA | confirmed | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayCounted from the captured catalog. [fact timeline →](../../facts/kev-precedent/index.html) | CISA KEV catalog; Akamai (2024) | confirmed | 3/3 | [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |
| There is no evidence yet that hackers have exploited the flaw [fact timeline →](../../facts/no-exploitation/index.html) | Ryan Austin, Calif, on Radio 4, 08:00 BST 22 October | reported | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Reports of active exploitation existThe only agency saying so, and it does not say whose reports. [fact timeline →](../../facts/nz-active/index.html) | NCSC New Zealand | reported | 1/1 | [NCSC New Zealand](../../sources/ncsc-nz-alert-php/index.html) |
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims. [fact timeline →](../../facts/amazon-honeypot/index.html) | Amazon (CJ Moses, AWS Security Blog) | reported | 1/2 | [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |
| Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloadsPrimary party, no volumes. [fact timeline →](../../facts/cloudflare-traffic/index.html) | Cloudflare | reported | 1/1 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. [fact timeline →](../../facts/latvia-attempts/index.html) | CERT.LV | reported | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Exploit attempts across Cloudflare's network: thousands in the ten hours before announcement, tens of thousands within 45 minutes after, hundreds of thousands within two hours, millions by 22 October 01:25 UTCPrimary party. Attempts, not compromises; no blocked count; 1.4 million views at capture. [fact timeline →](../../facts/cf-millions/index.html) | Matthew Prince, Cloudflare CEO, on X | reported | 1/1 | [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) |
| No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosure monitoringA negative finding from a party that had the details under embargo. [fact timeline →](../../facts/imperva-none/index.html) | Imperva Threat Research | reported | 1/1 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) |
| No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code known to Huntress [fact timeline →](../../facts/huntress-none/index.html) | Huntress | reported | 1/1 | [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |
| Criminals are using AI to 'vibe code' an attack method [fact timeline →](../../facts/vibe-code/index.html) | unnamed researchers, via the BBC | unverified | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| watchTowr sees active exploitation attempts and lists the flaws as exploited in the wildwatchtowr.com returns HTTP 403 to this site's capture tool; known only from search summaries. [fact timeline →](../../facts/watchtowr-itw/index.html) | watchTowr | unverified | 2/2 | [watchTowr](../../sources/watchtowr-php2shell/index.html) [watchTowr](../../sources/watchtowr-php2shell-faq/index.html) |
| If an immediate update is not feasible, take the system offline until it can be fully mitigatedX post 13:45:58Z 21 October (10.1 million views at capture) and the press release. [fact timeline →](../../facts/offline-nsa/index.html) | NSA Cybersecurity | confirmed | 2/2 | [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [NSA](../../sources/nsa-press-php-4630238/index.html) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline [fact timeline →](../../facts/offline-cisa/index.html) | CISA | confirmed | 1/1 | [CISA](../../sources/cisa-alert-php-20261021/index.html) |
| Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 OctoberEvery vendor says the same two things: it is a stopgap, and patch anyway. [fact timeline →](../../facts/waf-nine-hours/index.html) | the vendors | confirmed | 5/5 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html) |
| The risks require immediate patching across United States Government departments and agenciesNo CISA emergency directive was visible on the CISA home page at capture. [fact timeline →](../../facts/gov-patch-required/index.html) | NSA | reported | 1/2 | [NSA](../../sources/nsa-press-php-4630238/index.html) [CISA](../../sources/cisa-home/index.html) |
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. [fact timeline →](../../facts/offline-ncsc/index.html) | UK NCSC, as quoted by the BBC | disputed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CCCS](../../sources/cccs-al26-026/index.html) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. [fact timeline →](../../facts/latvia-offline/index.html) | CERT.LV | confirmed | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| No named organisation has confirmed a compromise through php2shellA negative finding as of the latest capture. Amazon says 'broadly exploited' against sensors; Weird Gloop expects old forums to have been hit; CISA has not listed either CVE. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source | confirmed | 5/5 | [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| The Dutch NCSC took its own site offline as a precaution, as did DigiD, MijnOverheid and Overheid.nl, with no signs of active exploitation of those servicesPrimary statement. [fact timeline →](../../facts/nl-offline/index.html) | the Dutch government | confirmed | 1/2 (1 blocked) | [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [Dutch IT Leaders](../../sources/dutchitleaders-websites-offline/index.html) |
| Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of page views from cachePrimary, and the one outage with a measured cost. [fact timeline →](../../facts/weirdgloop-13h/index.html) | Weird Gloop | confirmed | 1/1 | [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. [fact timeline →](../../facts/affected-sites/index.html) | BBC | reported | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time on 21 October as a precaution [fact timeline →](../../facts/fi-offline/index.html) | Yle; Helsinki Times, quoting Valtori | reported | 0/2 | [Yle](../../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../../sources/helsinkitimes-finland-shutdown/index.html) |
| The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely patched'No Wikimedia-published statement captured. [fact timeline →](../../facts/wikimedia-precaution/index.html) | the Foundation, as quoted by CNN and The Cyber Express | reported | 0/2 | [CNN](../../sources/cnn-php2shell-websites-shut/index.html) [The Cyber Express](../../sources/cyberexpress-php2shell-gov-sites/index.html) |
| Edinburgh council's site went offline late on 21 October; the council called it 'essential maintenance' and did not confirm a link [fact timeline →](../../facts/edinburgh/index.html) | The Scotsman quoting the council | reported | 0/1 | [The Scotsman](../../sources/scotsman-edinburgh-council-offline/index.html) |
| Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident' [fact timeline →](../../facts/oxford/index.html) | the council's social post, via Oxford Chronicle | reported | 0/1 | [Oxford Chronicle](../../sources/oxfordchronicle-councils-offline/index.html) |
| Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility were unavailable; Bristol, Lambeth and Barnet council sites showed errors [fact timeline →](../../facts/uk-list/index.html) | LBC; Insurance Business | reported | 0/2 | [LBC](../../sources/lbc-uk-websites-offline/index.html) [Insurance Business](../../sources/insurancebusiness-uk-councils-met/index.html) |

Every sentence above rests on these rows. They are folded away because they are written in the sources' own vocabulary; the glossary explains each term.

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other readers: [Curious reader](../everyone/index.html) · [Website owner](../site-owner/index.html) · [Project or programme manager](../pm/index.html) · [Security lead](../security/index.html) · [PHP or platform engineer](../engineer/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or policy advisor](../analyst/index.html) · [CISO](../ciso/index.html) · [CTO](../cto/index.html) · [CFO](../cfo/index.html) · [Head of AppSec](../appsec/index.html) · [Developer](../developer/index.html) · [Communications team](../comms/index.html).


---
site v0.4.5 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/briefings/board/index.html
