# Briefing for a board member or executive: Are we exposed, what is it costing us, and who owns the decision to pull a system?

The php2shell story for a board member or executive: what to decide, the claims it rests on with their status and sources, and what is still open.

Briefing · Board member or executive · from the same 49 claims, selected and ordered for one reader

# Are we exposed, what is it costing us, and who owns the decision to pull a system?

Three decisions sit with you: whether the organisation is exposed, what it costs to find out, and who may pull a system. The facts below are the ones those decisions turn on. Everything marked *reported* is one party's word; nothing below is a confirmed compromise anywhere.

## What to decide or do
- Do we have an inventory of every system serving PHP, including vendor products? If not, that is the first spend.
- Has every internet-facing system been patched and restarted, and has the running version been checked after the restart?
- Who is authorised to take a system offline, how long does it take, and has it been rehearsed?
- What would a compromise of our most exposed PHP system reach: which data, which credentials, which other systems?
- What is our evidence that we were not exploited between the leak on 20 October and our patch?

## The facts this rests on
- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerableCounted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'. | NCSC-NL, counted by this site from the file at commit cca173c64ec5 | confirmed | [NCSC-NL](../../sources/index.html#ncsc-nl-php2shell-software-list) |
| PHP is used by almost 70% of websitesNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | [Cloudflare](../../sources/index.html#cloudflare-blog-php2shell-waf) [OpenAI on X](../../sources/index.html#x-openai-php2shell) [Wiz](../../sources/index.html#wiz-blog-php2shell) |
| Something like 30 million websites could be affectedNo basis given. | Alan Woodward, via the BBC | reported | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| PHP is exposed on 2,608,039 internet-facing hosts | VulnCheck, via The Hacker News | reported | [THN](../../sources/index.html#thehackernews-php2shell-4days) |
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. | CERT.LV | reported | [CERT.LV](../../sources/index.html#certlv-php-preventive) |
| Roughly 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. | Wiz (headline, X post); BBC attributing Wiz | unverified | [Wiz](../../sources/index.html#wiz-blog-php2shell) [Wiz on X](../../sources/index.html#x-wiz-io-php2shell) [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalogCatalog version 2026.10.21 fetched 2026-10-22T08:15Z, 1,754 entries. A point-in-time negative finding. | CISA | confirmed | [CISA](../../sources/index.html#cisa-alert-php-20261021) [CISA](../../sources/index.html#cisa-kev-json) [CVE record](../../sources/index.html#cve-cve-2026-109618) |
| There is no evidence yet that hackers have exploited the flaw | Ryan Austin, Calif, on Radio 4, 08:00 BST 22 October | reported | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| Reports of active exploitation existThe only agency saying so, and it does not say whose reports. | NCSC New Zealand | reported | [NCSC New Zealand](../../sources/index.html#ncsc-nz-alert-php) |
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, and proof-of-concept attempts started about 02:00 UTC on 21 OctoberAmazon's own post has not been found. | CJ Moses, Amazon, via The Hacker News | reported | [THN](../../sources/index.html#thehackernews-php2shell-4days) |
| Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloadsPrimary party, no volumes. | Cloudflare | reported | [Cloudflare](../../sources/index.html#cloudflare-blog-php2shell-waf) |
| Amazon and Cloudflare saw sites being probed for the flawSecond-hand, but consistent with what both companies have said themselves. | Alan Woodward, via the BBC | reported | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) [Cloudflare](../../sources/index.html#cloudflare-blog-php2shell-waf) [THN](../../sources/index.html#thehackernews-php2shell-4days) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. | CERT.LV | reported | [CERT.LV](../../sources/index.html#certlv-php-preventive) |
| Criminals are using AI to 'vibe code' an attack method | unnamed researchers, via the BBC | unverified | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) |
| If an immediate update is not feasible, take the system offline until it can be fully mitigatedX post 13:45:58Z 21 October (10.1 million views at capture) and the press release. | NSA Cybersecurity | confirmed | [NSA Cyber on X](../../sources/index.html#nsa-x-2112903220209098897) [NSA](../../sources/index.html#nsa-press-php-4630238) |
| Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline | CISA | confirmed | [CISA](../../sources/index.html#cisa-alert-php-20261021) |
| The risks require immediate patching across United States Government departments and agenciesNo CISA emergency directive was visible on the CISA home page at capture. | NSA | reported | [NSA](../../sources/index.html#nsa-press-php-4630238) [CISA](../../sources/index.html#cisa-home) |
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. | UK NCSC, as quoted by the BBC | disputed | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) [NCSC UK](../../sources/index.html#ncsc-news-php) [CCCS](../../sources/index.html#cccs-al26-026) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. | BBC | contradicted | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) [ACSC](../../sources/index.html#acsc-alert-php) [CERT-EU](../../sources/index.html#certeu-sa-2026-018) [NCSC-NL](../../sources/index.html#ncsc-nl-php2shell) [ACN / CSIRT Italia](../../sources/index.html#acn-it-php2shell) [JPCERT/CC](../../sources/index.html#jpcert-at260033) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. | CERT.LV | confirmed | [CERT.LV](../../sources/index.html#certlv-php-preventive) |
| Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offlineNot captured from any of the named organisations. | BBC | reported | [BBC News](../../sources/index.html#bbc-live-ckgel5xp2xv9t) |

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other briefings: [Security lead](../security/index.html) · [PHP or platform engineer](../engineer/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or advisor](../analyst/index.html).


---
site v0.1.0 · data as of 2026-10-22T08:48Z · vault commit 379e3d7f172a · https://php.oct-2026.story.sgit.ai/briefings/board/index.html
