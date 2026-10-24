# PHP in October 2026: two critical security flaws, tracked as evidence

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

PHP news for October 2026, led by the month's big story: two critical security flaws in PHP (CVE-2026-109618 and CVE-2026-109619, nicknamed php2shell). The current situation in plain words, the core facts with their evidence, what to do, and a briefing for every kind of reader.

PHP news · October 2026 · Developing · [last checked 23 October 2026, 16:04 UTC](#checked)

# Two serious security flaws in PHP, the software behind many of the world's websites

PHP is the software that WordPress and millions of other websites run on. A fix came out on 21 October 2026. Government cyber agencies have told organisations to install it now, or to take websites offline if they cannot. Phones and personal computers are not affected.

  What is happening nowThe briefing for youExplain it from the startCheck your stackOn your phone: Now →

You may also see this called php2shell, or by its two official reference numbers, CVE-2026-109618 and CVE-2026-109619.

Last checked: [the evidence vault](sources/index.html), latest capture 23 October 2026, 16:04 UTC · [the source watch](vaults/source-watch/index.html), latest run 23 October 2026, 12:40 UTC · [the NCSC-NL inventory](patching/inventory/index.html), latest change read 23 October 2026, 12:50 UTC.

## Right now

As of 23 October 2026, 16:04 UTC, the time of the latest page this site saved.
- A fix has been available since 21 October. Organisations that run websites on PHP are installing it. [php.net](sources/php-net-advisory/index.html)
- Government cyber agencies in the US, the UK, the EU and elsewhere say: install the fix now, and take a website offline if you cannot. [CISA](sources/cisa-alert-php-20261021/index.html) [NCSC UK](sources/ncsc-news-php/index.html) [CERT-EU](sources/certeu-sa-2026-018/index.html) [NSA Cyber on X](sources/nsa-x-2112903220209098897/index.html)
- Attackers are trying to use the flaws, in large numbers: millions of attempts by one internet security company's count. As of 23 October, no named organisation has said it was compromised through php2shell. [Matthew Prince, Cloudflare CEO on…](sources/x-eastdakota-php2shell-stats/index.html) [CISA](sources/cisa-kev-json/index.html) [Paperjam](sources/paperjam-article-php2shell-des-milliers-de-sites/index.html)
- The advice is moving from 'install the fix' to 'and check whether you were already broken into'. Singapore's and Luxembourg's authorities now say so. [CNA](sources/channelnewsasia-singapore-php-vulnerabilities-csa-singapore-firms-cybersecur/index.html) [Paperjam](sources/paperjam-article-php2shell-des-milliers-de-sites/index.html)
- Some organisations took websites offline as a precaution, among them Dutch government services such as the DigiD login. Almost all of them are back. [Rijksoverheid / NCSC-NL](sources/rijksoverheid-ncsc-php-news/index.html) [PHPocalypse Tracker](sources/phpocalypse-tracker-sites-csv/index.html) [Security.NL](sources/securitynl-misbruik-gemeld/index.html)

This section v3 written in site [v0.10.19](admin/versions.html#v0.10.19) on 23 October 2026 · [history and changes, 2 earlier](versions/front-now/index.html)

## At a glance
Is there a fix?Yesinstall PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35How serious?Critical9.2 out of 10, both flawsDoes it reach you?Check your stackdescribe what you run and see what an attacker could reach in itAre attackers trying?Yesmillions of attempts, seen by one internet security companyAnyone confirmed hacked?Not yetno organisation, as of the latest checkWebsites taken offline10 organisationsreported, as a precautionOn the US 'used in attacks' list?Not yetthe US government's official list of flaws known to be used by attackersWhat do governments say?Update nowor take the website offline if you cannot; 16 agencies compared
This section v2 written in site [v0.8.2](admin/versions.html#v0.8.2) on 23 October 2026 · [history and changes, 1 earlier](versions/front-glance/index.html)

## The core facts, and the evidence for each

Each fact links to the original pages it rests on: the PHP project, government agencies, the researchers. Click a source to see when it was saved and its fingerprint.
- confirmed two or more original sources agree
- reported one party says so; nobody has contradicted it
- disputed sources disagree
- unverified nobody has been able to check it
- confirmedThere are two flaws. Both are in PHP itself, underneath every website that uses it, and both are rated critical: 9.2 out of 10.[CVE record](sources/cve-cve-2026-109618/index.html) [CVE record](sources/cve-cve-2026-109619/index.html) [php.net](sources/php-net-advisory/index.html) [More →](flaws/index.html)
- confirmedSomeone anywhere on the internet, with no password, can use them against a website that has not installed the fix, and make its server run their own commands. Researchers proved this on the most traditional way of running PHP; for other setups it is likely but less certain.[PHP](sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP Foundation](sources/php-foundation-blog-security-release/index.html) [More →](flaws/index.html)
- confirmedThe fix is in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October 2026. Websites on PHP 8.1 or older have no ready-made fix.[php.net](sources/php-net-advisory/index.html) [php-src](sources/github-php-src-branch-7.4-backport/index.html) [More →](affected/index.html)
- reportedThe weak spot was first noticed in 2024 and left alone, because nobody could show it was dangerous. In August 2026, three research teams using AI tools showed that it was, and told the PHP project.[PHP Foundation](sources/php-foundation-blog-security-release/index.html) [Calif](sources/calif-php2shell/index.html) [Wiz](sources/wiz-blog-php2shell/index.html) [More →](discovery/index.html)
- confirmedThe plan was to announce the fix on 22 October. Word leaked out on 20 October, so it was released a day early.[PHP Foundation](sources/php-foundation-blog-security-release/index.html) [Daubois](sources/daubois-blog-php2shell-rumors/index.html) [More →](leak/index.html)
- reportedAttackers are trying. One internet security company reports millions of attempts; Amazon reports a decoy server was hit four days before the announcement.[Matthew Prince, Cloudflare CEO on…](sources/x-eastdakota-php2shell-stats/index.html) [THN](sources/thehackernews-php2shell-4days/index.html) [More →](exploitation/index.html)
- confirmedAttackers are trying, in large numbers. No organisation has said it was broken into through this flaw, as of the evening of 22 October, and the US government's official list of flaws known to be used in attacks did not include these two when last checked.[CISA](sources/cisa-kev-json/index.html) [CISA](sources/cisa-kev-catalog/index.html) [More →](impact/index.html)
- confirmedEvery agency says install the fix. They disagree on what to do if you cannot: the US says take the website offline, the UK lists that as a last resort, several European agencies say cut it off from the public internet, and some say nothing about it.[CISA](sources/cisa-alert-php-20261021/index.html) [NCSC UK](sources/ncsc-news-php/index.html) [CERT-EU](sources/certeu-sa-2026-018/index.html) [ACSC](sources/acsc-alert-php/index.html) [More →](agencies/index.html)
- confirmedThe headline '70% of the Internet' is not what it sounds like. It is roughly the share of websites built with PHP, which is what the same company's own article says; nobody has measured how many are actually at risk.[Wiz](sources/wiz-blog-php2shell/index.html) [Wiz on X](sources/x-wiz-io-php2shell/index.html) [Cloudflare](sources/cloudflare-blog-php2shell-waf/index.html) [More →](numbers/index.html)

This section v2 written in site [v0.5.8](admin/versions.html#v0.5.8) on 22 October 2026 · [history and changes, 1 earlier](versions/front-facts/index.html)

## What nobody knows yet

Stated, not papered over. This site will update each one when the evidence does.
- [Whether any website was actually broken into before it installed the fix.](impact/index.html)
- [Whether the fix is complete. A report on 21 October suggested it may not be; the PHP project has not answered it publicly yet.](code/index.html)
- [Who leaked the news on 20 October, and where.](leak/index.html)
- [Exactly which websites went offline, and why. Most of the list comes from one news live page and has not been confirmed by the organisations named.](impact/index.html)
- [Where the 70% figure comes from. None of the pages that use it says how it was measured.](numbers/index.html)

This section v1 written in site [v0.3.2](admin/versions.html#v0.3.2) on 22 October 2026 · [history](versions/front-unknown/index.html)

## Latest
- 22 OctKorea's science ministry raises the private-sector cyber crisis alert from 'interest' to 'caution', as reported. [신아일보](sources/shinailbo-news-articleview-html/index.html)
- 22 OctSingapore's Cyber Security Agency tells organisations to patch now and to check whether they were already compromised. [CNA](sources/channelnewsasia-singapore-php-vulnerabilities-csa-singapore-firms-cybersecur/index.html)
- 22 OctA count in Switzerland finds just over 23,000 of nearly 690,000 servers, about 3.5%, still affected a day after the fix. [ICTjournal](sources/ictjournal-news-2026-10-22-deux-failles-critiques-d/index.html)
- 22 OctAhnLab, as reported, classes 27 of 100 php2shell repositories on GitHub as proof-of-concept exploits. [合同会社ロケットボーイズ](sources/rocket-boys-security-measures-lab-php2shell-poc-expl/index.html)
- 23 Oct, 07:58 UTCIT Social: the update closes the flaw, but obliges a hunt for possible compromises; the published figures count attempts, not intrusions. [IT Social](sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html)

[Everything, in order, on the timeline →](timeline/index.html) · [What changed on this site, release by release →](whatsnew/index.html)

This section v2 written in site [v0.10.19](admin/versions.html#v0.10.19) on 23 October 2026 · [history and changes, 1 earlier](versions/front-latest/index.html)

What else is going on Other vulnerabilities in the news this month, with the evidence that each is exploited beside the attention it gets: the SGit newsroom's Pulse, in a separate section, not about PHP. Pulse →

## The briefing for you

The same evidence, put in order for 16 kinds of reader. Each starts with a thirty-second answer in plain words. [How the readers are mapped](start/index.html).

### I want to understand it

You heard about this on the news or from a colleague and want to know what it is and whether it touches you.
ACurious readerAlex · Plain EnglishWhat happened, does it affect me, and should I worry?4 reads · about 14 min Start →CWebsite ownerCasey · Plain EnglishMy website runs on WordPress or similar: am I affected, and what do I ask my host?4 reads · about 14 min Start →
### I make the decisions

You own a budget, a plan or a risk, and need what to decide, in what order, and what to ask your team.
JBoard member or executiveJordan · Plain EnglishAre we exposed, what is it costing us, and who owns the decision to pull a system?5 reads · about 15 min Start →TProject or programme managerTaylor · Plain EnglishWhat unplanned work does this create, who do I chase, and what do I tell stakeholders?5 reads · about 16 min Start →QCFOQuinn · Plain EnglishWhat is the financial exposure, what does downtime cost against breach cost, and will insurance respond?5 reads · about 16 min Start →MData protection officerMorgan · Some technicalWas personal data exposed, does this start a GDPR breach assessment or a 72-hour notification, and what do I document?6 reads · about 15 min Start →RCISORobin · Some technicalWhat is our exposure, what is our evidence we were not hit, and what do I tell the board?6 reads · about 14 min Start →ACTOAvery · Some technicalWhat does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?5 reads · about 20 min Start →
### I tell others

You write or speak about this, and need what is true, what is not, and who said it first.
RJournalistRowan · Some technicalWhich numbers hold up, who said what first, and what is still unverified?6 reads · about 10 min Start →RCommunications teamRiley · Plain EnglishWhat can we say that is true, what should we not say, and what will we be asked?5 reads · about 14 min Start →
### I run or build systems

You patch, configure, monitor or write code, and need versions, settings and signals.
SSecurity leadSam · Some technicalWhat do I patch first, what do I watch for, and when do I take something offline?5 reads · about 12 min Start →JHead of AppSecJamie · Deeply technicalWhich of our applications are in scope, which settings matter, and what do we add to the pipeline?5 reads · about 14 min Start →DPHP or platform engineerDrew · Deeply technicalWhich versions, which SAPIs, which settings, which commands?5 reads · about 18 min Start →LDeveloperLee · Some technicalIs my code the problem, what do I change, and how do I check the box I deployed to?4 reads · about 17 min Start →
### I study it

You research vulnerabilities or advise on policy, and need the evidence, the open questions and the precedent.
ASecurity researcherAsh · Deeply technicalWhat are the bug classes, what was demonstrated, and what is still open?5 reads · about 19 min Start →BAnalyst or policy advisorBlake · Some technicalHow did coordinated disclosure fail, and what does AI-assisted discovery change?6 reads · about 12 min Start →

## How it unfolded
- [2024An audit spots the out-of-memory weakness. Nobody can show it is exploitable, so it is left.](context/index.html)[PHP Foundation](sources/php-foundation-blog-security-release/index.html)
- [Aug 2026Three teams using AI turn it into working attacks within three weeks and report them to PHP.](discovery/index.html)[Calif](sources/calif-php2shell/index.html) [Wiz](sources/wiz-blog-php2shell/index.html) [PHP Foundation](sources/php-foundation-blog-security-release/index.html)
- [20 OctThe secret leaks: the CVE numbers circulate two days early, with a wrong severity score.](leak/index.html)[PHP Foundation](sources/php-foundation-blog-security-release/index.html)
- [21 OctPHP releases the fix a day ahead of plan. Firewall vendors already have rules live.](flaws/index.html)[php.net](sources/php-net-advisory/index.html) [Cloudflare](sources/cloudflare-blog-php2shell-waf/index.html)
- [22 OctAgencies warn: update, or take systems offline. Sites go dark as a precaution.](agencies/index.html)[NSA Cyber on X](sources/nsa-x-2112903220209098897/index.html) [CISA](sources/cisa-alert-php-20261021/index.html) [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html)

## Stories: written here

Everything above is research: collected from outside sources, each fact linked to a saved copy. These are written here, signed and dated, and kept as written.
What changed in a day: no victim yet, four named cases tested, a patch moving through the supply chain, and firewalls on the listHouse story · Journalist · 2026-10-23Who reads this site, and what works on it: the tools we built to find out, and what they say on day twoHouse story · Dev desk · 2026-10-23The risk graph, before and after: what changed from one reader's five ideasHouse story · Dev desk · 2026-10-23The editor, interviewed: Dinis Cruz on why this site existsInterview · the editor, in his own words
[All stories →](articles/index.html)

## How this site knows
295web pages saved as evidence, each with the time it was saved70statements checked: 21 confirmed, 11 disputed, 4 unverified68dated events, from 2024 to today16government agencies' advice compared
Every page this site relies on was saved at the moment it was read, with a fingerprint that proves it has not been altered since, so a fact can be checked even if the original page changes or disappears. Nothing here is advice for your own systems; for that, read [the PHP project's announcement](https://www.php.net/archive/2026.php#2026-10-21-5) and your national cyber agency. The site is put together by software agents working for one editor, Dinis Cruz; [how it works](method/index.html).

Already know the vocabulary? [The specialist summary](summary/index.html) has the technical version of this page, with every number and the full last 48 hours.


---
site v0.11.6 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/index.html
