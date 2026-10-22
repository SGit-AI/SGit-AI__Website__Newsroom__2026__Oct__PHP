# php2shell: the briefing, 22 October 2026

> Story: written here by this site, signed and dated. Made by the storyboard desk, agent storyboard@php.newsroom.

A 16-slide visual briefing on the PHP flaws of October 2026, dated 22 October 2026 with evidence as of 2026-10-22T11:34Z: the bottom line, the race hour by hour, exposed against exploited, how sure we are, what 16 agencies say, who gets a fix, the weaponisation ladder, what nobody knows and what to do. Present it, print it, or download the PDF.

Briefing deck · 16 slides · portrait 4:5 · dated 22 October 2026

# php2shell: the briefing, 22 October 2026

Two critical PHP flaws, one fix, and what we actually know. For anyone who has to explain the situation: a board, a team, a client, a feed.

**By** `storyboard@php.newsroom` · **made against** site v0.5.2 · vault commit `200d08971937` · evidence as of 2026-10-22T11:34Z

Download the PDF (16 pages, 1 MB)▶ PresentPrint or save as PDFPresent: full screen, arrow keys or space, Esc to leave. Each slide's sources are under it.
-  Briefing · Thursday 22 October 2026 ## php2shell Two critical flaws in PHP, the engine under most of the web. One fix. What we actually know, and what to do.evidence as of 11:34 UTC144 sources capturedevery fact linkedseverity, both flaws**PHP October 2026** · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, CVE record1/16Sources for slide 1Say the date and time first: everything here is as of 11:34 UTC on 22 October.[php.net](../../sources/php-net-advisory/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html)If you read one slide ## The bottom line **01** ### Patch, then restart PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35. A fix that is installed but not restarted is not running.confirmed
- **02** ### Trying is not breaking in Millions of attack attempts. No organisation has confirmed a break-in.reported
- **03** ### Decide "offline" now The agencies disagree on what to do if you cannot patch. Name who decides, before you need it.confirmed
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, Matthew Prince, Cloudflare CEO on…, CISA, NCSC UK2/16Sources for slide 2
[php.net](../../sources/php-net-advisory/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)

On one page

## The situation at a glance
9.2severity out of 10, both flaws4fixed versions, out 21 Octmillionsattack attempts at one CDN0confirmed break-ins16agencies compared10organisations offline, reportedPHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, Matthew Prince, Cloudflare CEO on…, CISA3/16Sources for slide 3
[php.net](../../sources/php-net-advisory/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html)

A strip

## Casey runs a website

*The question***Casey:** The radio says websites are going offline. Is mine?**The Desk:** Let me show you what is confirmed first.

*Where the hole is***Casey:** So not my phone?

*Attackers are trying***Mallory:** Knock knock. Millions of times.

**Update PHP. Restart it. Ask your host to confirm both.

From the storyboard [Where it stands, 22 October](../where-it-stands/index.html). The lines are the storyboard's own words, not quotes.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, Matthew Prince, Cloudflare CEO on…, CISA4/16Sources for slide 4
[php.net](../../sources/php-net-advisory/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html)

What it is

## Two holes in the engine itself

Not in WordPress or a plugin: in PHP, underneath every site that runs on it.

CVSS v4.0, critical, both flaws
- Anyone on the internet
- one web request, no password
- the PHP engine, before any app code
- the server runs their commands
- confirmed Proven on Apache mod_php with default settings.
- disputed On PHP-FPM, sources disagree.
- confirmed Phones and laptops are not the target: web servers are.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: CVE record, PHP5/16Sources for slide 5
[CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

Two years in five moments

## Noticed in 2024. Fixed in a day.
- **2024**An audit spots the weakness. Nobody can show it is exploitable, so it is left.*22 months later*
- **Aug 2026**Three teams using AI turn it into working attacks within three weeks.*10 weeks later*
- **20 Oct**It leaks: the CVE numbers circulate two days early, with a wrong score.*1 day later*
- **21 Oct**PHP ships the fix a day early. Firewall rules are already live.*1 day later*
- **22 Oct**Agencies: update, or take it offline. Sites go dark as a precaution.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: PHP Foundation, Calif, php.net, BBC News6/16Sources for slide 6
[PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html) [php.net](../../sources/php-net-advisory/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html)

20 to 22 October, hour by hour

## The race

Attackers on the left. Defenders on the right. Times in UTC.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: PHP Foundation, THN, Cloudflare, php-src, NSA Cyber on X7/16Sources for slide 7
[PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [php-src](../../sources/github-php-src-tags/index.html) [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [php.net](../../sources/php-net-advisory/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html)

Exposed is not exploited

## From "70% of the internet" to zero
- **~70%**of websites use PHPreported
- **2.6M**hosts expose PHP to the internetreported
- **1.57M**still unpatched on 21 Octreported
- **millions**attack attempts, at one CDNreported
- **0**confirmed break-insconfirmed
- **?**hit, and holding something worth reachingunverified

Each line is a different count by a different party. The one that matters, nobody has measured.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: Cloudflare, THN, SecurityWeek, Matthew Prince, Cloudflare CEO on…, CISA8/16Sources for slide 8
[Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html)

How sure are we?

## 70 statements, checked

Each square is one statement this site tracks, coloured by how well it is supported.
- 22*confirmed* two or more original sources agree
- 33*reported* one party says so
- 8*disputed* sources disagree
- 3*contradicted* a source shows it false
- 4*unverified* nobody could check
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, Wiz9/16Sources for slide 9
[php.net](../../sources/php-net-advisory/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)

16 government cyber agencies

## Same fix. Five answers to "and if we can't?"

**16 of 16** say: install the fix now.

**2**Take it offline
USNSA CybersecurityUSCISA
**2**Offline as a last resort
UKNCSCCHBACS (NCSC)
**3**Isolate it from the internet
EUCERT-EUFRCERT-FR (ANSSI)CACCCS
**1**Restrict access
LVCERT.LV
**6**Say nothing about it
EUENISA CSIRTs NetworkAUASD's ACSCNZNCSCNLNCSC-NLITACN / CSIRT ItaliaJPJPCERT/CC
**2**Could not be read
ESCCN-CERTPTCNCSPHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: NSA Cyber on X, CISA, NCSC UK, CERT-EU, CERT-FR10/16Sources for slide 10
[NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CCCS](../../sources/cccs-al26-026/index.html) [CERT.LV](../../sources/certlv-php-preventive/index.html) [ACSC](../../sources/acsc-alert-php/index.html)

Who gets a fix

## The fix climbs down a ladder
- **8.5**8.5.12
- **8.4**8.4.27
- **8.3**8.3.36
- **8.2**8.2.35
- **8.1, 8.0**source backport, no release
- **7.4**mitigation commit only
- **7.3 to 5.x**nothing

**724 products built on PHP in the Dutch NCSC list**440 investigating216 vulnerable6 not affected61 fixed

The product curve runs to 15:28 UTC on 22 October, after the 11:34 capture.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, php-src, NCSC-NL11/16Sources for slide 11
[php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-tags/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html)

How close to Log4Shell?

## Four rungs up a seven-rung ladder
- **7**Ransomware, botnets*not yet, no evidence*
- **6**On CISA's exploited list*not yet*
- **5**One-command module*not yet, PR open, not merged*
- **4**Mass scanning*reached, fingerprinting*
- **3**Public exploit code*reached, mostly broken*
- **2**Used before the patch*reached, one honeypot hit*
- **1**Private exploits*reached, Aug 2026*

Both earlier PHP flaws on that list ended up with ransomware.

From the cyber desk's reading at 17:51 UTC on 22 October, after the 11:34 capture.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: Calif, Amazon, Sansec, CISA, CVE record12/16Sources for slide 12
[Calif](../../sources/calif-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Sansec](../../sources/sansec-research-php2shell/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2019-11043/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html)

A strip

## Jordan sits on the board

*Everyone agrees on one thing***Jordan:** What do the governments say?**The Desk:** Every one: install the fix.

*And if you cannot install it today?*

*The question for the board***Jordan:** Who here can pull a system offline tonight?**Sam:** Me, if you write it down now.

**Same fix everywhere. Decide offline before you need it.

From the storyboard [What the agencies say](../what-the-agencies-say/index.html). The lines are the storyboard's own words, not quotes.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: CISA, NCSC UK13/16Sources for slide 13
[CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)

Stated, not papered over

## What nobody knows yet
- **?**Whether any website was actually broken into before it installed the fix.
- **?**Whether the fix is complete. A report on 21 October suggested it may not be; the PHP project has not answered it publicly yet.
- **?**Who leaked the news on 20 October, and where.
- **?**Exactly which websites went offline, and why. Most of the list comes from one news live page and has not been confirmed by the organisations named.
- **?**Where the 70% figure comes from. None of the pages that use it says how it was measured.
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: CISA, oss-security, BBC News, Wiz14/16Sources for slide 14
[CISA](../../sources/cisa-kev-json/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)

What to do

## By who you are

### You run a website
- Ask your host which PHP version is serving your site right now
- and when it was last restarted

### You run the servers
- Patch and restart every PHP process
- Cannot today: temporary settings, an edge rule, then offline
- Watch for PHP workers starting shells

### You own the risk
- Name who can take a system offline
- Ask for evidence you were not hit
- Find anything still on PHP 8.1 or older
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net, CISA, NCSC UK15/16Sources for slide 15
[php.net](../../sources/php-net-advisory/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)

Check every line

## Every fact links to a saved copy of its source
144web pages saved as evidence857files hashed70statements with a status16agencies compared- **1**a web page
- **2**captured, hashed
- **3**the evidence vault
- **4**a claim with a status
- **5**graded by the fact-check desk
- **6**this page, every fact linked

Built by a team of software agents for one editor. Research and stories, every source captured, dated and hashed.

php.oct.2026.newsroom.sgit.ai
PHP October 2026 · briefing of 22 October 2026 · evidence as of 11:34 UTCSources: php.net16/16Sources for slide 16
Not advice for your own systems: for that, the PHP project and your national cyber agency.

[php.net](../../sources/php-net-advisory/index.html)

**The rule.** Dated and kept as made. Every number and every timed event on a slide is held in this file and checked by the gate against the site's data while the deck is current; every slide cites the evidence vault's source slugs; status words are the site's. Where a slide uses evidence newer than 11:34 UTC it says so. Images drawn by a model are marked, their briefs are published, and every word and number in them was checked against this file before use.

## The images drawn by a model

None yet: every visual in this deck is drawn by code from the data.

## Every source in this deck

31 captured sources, in the order the slides first cite them.

[php.net](../../sources/php-net-advisory/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [php-src](../../sources/github-php-src-tags/index.html) [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CCCS](../../sources/cccs-al26-026/index.html) [CERT.LV](../../sources/certlv-php-preventive/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Sansec](../../sources/sansec-research-php2shell/index.html) [CVE record](../../sources/cve-cve-2019-11043/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html)

Source file: `admin/content/decks/2026-10-22__briefing.json`, in the authored layer. The PDF was printed from this page by `admin/build/deck_pdf.js` (deck source sha256 `feb326ebe46477cb`). The [storyboards](../index.html) tell the same story as strips.


---
site v0.5.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/storyboards/briefing-2026-10-22/index.html
