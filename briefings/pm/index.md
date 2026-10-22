# Briefing for a project or programme manager: What unplanned work does this create, who do I chase, and what do I tell stakeholders?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell story for a project or programme manager: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.

Briefing for Taylor, project or programme manager · ******Plain English · from the same 70 claims, selected and ordered for one reader

# What unplanned work does this create, who do I chase, and what do I tell stakeholders?

T
The answer in thirty seconds

Expect unplanned work this week: updating PHP on every system that uses it, restarting, and re-testing. Some teams may take systems offline for hours as a precaution. Anything still on PHP 8.1 or older has no ready-made fix and becomes a migration project. Ask each system owner for a patch date and a test plan.

[Read the site as Taylor →](../../explained/index.html)

This is a platform event, not an application bug, so it lands on every team that ships anything running on PHP at once. Plan for it the way you would plan for a datacentre move: an inventory, an owner per system, a date, a test.

## What to decide or do
- **Get the list.** Which systems run PHP, who owns each, and which are on the internet. Vendor products and hosting panels count. Without the list nothing else can be scheduled.
- **Get a date per system.** Updating PHP means installing the fixed version, restarting, rebuilding containers and re-testing. Internet-facing systems first.
- **Budget for regression testing.** The fix changes how PHP behaves when it runs short of memory: a system that used to limp along may now stop cleanly. Load tests are worth running before the release, not after.
- **Plan for precautionary downtime.** Agencies advise isolating or taking offline what cannot be updated in time. Agree with stakeholders now who can make that call, how long it may last, and what users see meanwhile.
- **Treat PHP 8.1 and older as a project.** There is no ready-made release for them. Moving to a supported version is a migration with its own scope and schedule.
- **Expect a second round.** A report that the first fix may be incomplete is open. Keep a slot free in the next fortnight.

## Your reading path
- [Your briefing](../../briefings/pm/index.html) 4 min
- [Explained from the start](../../explained/index.html) 6 min
- [If you run PHP](../../playbook/index.html) 3 min
- [Impact: offline vs compromised](../../impact/index.html) 2 min
- [Timeline](../../timeline/index.html) 1 min

About 16 minutes in all. Choose *read as Taylor* and the bar under the menu keeps your place on every page.

### What this briefing covers
- what unplanned work this creates
- which systems and owners to chase
- what to tell stakeholders about downtime
- what changes after the fix

### What you can skip
- the code
- the bug classes
- the detection rules

## Words you will meet

[PHP](../../glossary/index.html#php)[Patch](../../glossary/index.html#patch)[Primary source](../../glossary/index.html#primary)[NSA](../../glossary/index.html#nsa)[CISA](../../glossary/index.html#cisa)[NCSC](../../glossary/index.html#ncsc)[php2shell](../../glossary/index.html#php2shell)[CVE](../../glossary/index.html#cve)[Exploit, exploitation](../../glossary/index.html#exploit)[Web server](../../glossary/index.html#web-server)[GitHub advisory (GHSA)](../../glossary/index.html#ghsa)[Honeypot](../../glossary/index.html#honeypot)[Remote code execution (RCE)](../../glossary/index.html#rce)[Unauthenticated](../../glossary/index.html#unauthenticated)

Each is underlined where it first appears; hover or tap for a one-line definition, or open [the glossary](../../glossary/index.html).

## The facts this rests on
Show the 20 claims behind this briefing, each with its status and sources- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| If an immediate update is not feasible, take the system offline until it can be fully mitigatedX post 13:45:58Z 21 October (10.1 million views at capture) and the press release. [fact timeline →](../../facts/offline-nsa/index.html) | NSA Cybersecurity | confirmed | not checked | 2/2 | [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [NSA](../../sources/nsa-press-php-4630238/index.html) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline [fact timeline →](../../facts/offline-cisa/index.html) | CISA | confirmed | not checked | 1/1 | [CISA](../../sources/cisa-alert-php-20261021/index.html) |
| Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 OctoberEvery vendor says the same two things: it is a stopgap, and patch anyway. [fact timeline →](../../facts/waf-nine-hours/index.html) | the vendors | confirmed | not checked | 5/5 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html) |
| The risks require immediate patching across United States Government departments and agenciesNo CISA emergency directive was visible on the CISA home page at capture. [fact timeline →](../../facts/gov-patch-required/index.html) | NSA | reported | not checked | 1/2 | [NSA](../../sources/nsa-press-php-4630238/index.html) [CISA](../../sources/cisa-home/index.html) |
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. [fact timeline →](../../facts/offline-ncsc/index.html) | UK NCSC, as quoted by the BBC | disputed | not checked | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CCCS](../../sources/cccs-al26-026/index.html) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | not checked | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. [fact timeline →](../../facts/latvia-offline/index.html) | CERT.LV | confirmed | not checked | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| No named organisation has confirmed a compromise through php2shellA negative finding as of the latest capture. Amazon says 'broadly exploited' against sensors; Weird Gloop expects old forums to have been hit; CISA has not listed either CVE. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source | confirmed | not checked | 5/5 | [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| The Dutch NCSC took its own site offline as a precaution, as did DigiD, MijnOverheid and Overheid.nl, with no signs of active exploitation of those servicesPrimary statement. [fact timeline →](../../facts/nl-offline/index.html) | the Dutch government | confirmed | not checked | 1/2 (1 blocked) | [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [Dutch IT Leaders](../../sources/dutchitleaders-websites-offline/index.html) |
| Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of page views from cachePrimary, and the one outage with a measured cost. [fact timeline →](../../facts/weirdgloop-13h/index.html) | Weird Gloop | confirmed | not checked | 1/1 | [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. [fact timeline →](../../facts/affected-sites/index.html) | BBC | reported | not checked | 0/1 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time on 21 October as a precaution [fact timeline →](../../facts/fi-offline/index.html) | Yle; Helsinki Times, quoting Valtori | reported | not checked | 0/2 | [Yle](../../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../../sources/helsinkitimes-finland-shutdown/index.html) |
| The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely patched'No Wikimedia-published statement captured. [fact timeline →](../../facts/wikimedia-precaution/index.html) | the Foundation, as quoted by CNN and The Cyber Express | reported | not checked | 0/2 | [CNN](../../sources/cnn-php2shell-websites-shut/index.html) [The Cyber Express](../../sources/cyberexpress-php2shell-gov-sites/index.html) |
| Edinburgh council's site went offline late on 21 October; the council called it 'essential maintenance' and did not confirm a link [fact timeline →](../../facts/edinburgh/index.html) | The Scotsman quoting the council | reported | not checked | 0/1 | [The Scotsman](../../sources/scotsman-edinburgh-council-offline/index.html) |
| Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident' [fact timeline →](../../facts/oxford/index.html) | the council's social post, via Oxford Chronicle | reported | not checked | 0/1 | [Oxford Chronicle](../../sources/oxfordchronicle-councils-offline/index.html) |
| Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility were unavailable; Bristol, Lambeth and Barnet council sites showed errors [fact timeline →](../../facts/uk-list/index.html) | LBC; Insurance Business | reported | not checked | 0/2 | [LBC](../../sources/lbc-uk-websites-offline/index.html) [Insurance Business](../../sources/insurancebusiness-uk-councils-met/index.html) |
| The fix was authored on 18 October at 15:26 UTC and entered the public branches at 14:06 UTC on 21 October, with merges into 8.3, 8.4 and 8.5 between 14:12 and 14:30 UTCCounted from the repository, not from a page. Five authors; 389 files; 10,689 insertions. [fact timeline →](../../facts/fix-authored/index.html) | php/php-src commit 3584a98bd, read from a clone | confirmed | not checked | 2/2 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | not checked | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The pre-announcement was published at 19:30 UTC on 20 OctoberThe php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC, so it was public by then. [fact timeline →](../../facts/preannounce-time/index.html) | PHP Foundation | disputed | not checked | 3/3 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The flaws were disclosed on 22 October 2026Primary sources put the release at 21 October: GHSAs 13:34Z, tags 13:35Z, CVE records 13:48Z and 13:54Z, GitHub release 14:06Z. [fact timeline →](../../facts/disclosure-22oct/index.html) | BBC framing (UK morning coverage) | contradicted | not checked | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) |

Every sentence above rests on these rows. They are folded away because they are written in the sources' own vocabulary; the glossary explains each term.

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other readers: [Curious reader](../everyone/index.html) · [Website owner](../site-owner/index.html) · [Board member or executive](../board/index.html) · [Security lead](../security/index.html) · [PHP or platform engineer](../engineer/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or policy advisor](../analyst/index.html) · [CISO](../ciso/index.html) · [CTO](../cto/index.html) · [CFO](../cfo/index.html) · [Head of AppSec](../appsec/index.html) · [Developer](../developer/index.html) · [Communications team](../comms/index.html).


---
site v0.4.7 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/briefings/pm/index.html
