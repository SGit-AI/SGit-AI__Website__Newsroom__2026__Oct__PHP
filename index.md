# php2shell: the two PHP flaws of October 2026, tracked as evidence

A fact-driven, agent-run tracker for CVE-2026-109618 and CVE-2026-109619: what is established, who said what and when, which numbers add up, what to do about a vulnerable system, and the captured, hashed evidence behind every line.

Developing · CVE-2026-109618 and CVE-2026-109619 · updated with the vault, 2026-10-22T11:34Z

# php2shell: the two PHP flaws of October 2026, tracked as evidence

On 21 October 2026 at 14:00 UTC the PHP project released fixes for two critical flaws, **CVE-2026-109618** and **CVE-2026-109619**, nicknamed *php2shell*. Either can give an unauthenticated attacker remote code execution on a web server running PHP, the language behind WordPress, Drupal, Wikipedia and a large share of the web. The flaws were found with AI help, the coordinated disclosure broke down two days early, and by the morning of 22 October the NSA, CISA and the UK's NCSC were telling organisations that could not patch to take systems offline. This site follows the story as evidence: every claim points to a captured, dated and hashed source, every number says what it measures, and every contradiction between sources is left visible.

  144sources in the evidence vault137dated captures, each file hashed70claims with a status: 22 confirmed, 11 disputed or contradicted, 4 unverified68dated events on the timeline16national agencies compared10operators reported offline, 0 confirmed compromises674products in the NCSC-NL inventory

**Developing, and agent-produced.** Software agents assemble this site from sources captured into a private evidence vault; the editor is Dinis Cruz. Nothing here is advice on what to patch in your environment. For that, read the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national cyber-security agency. Where this site says a thing is *confirmed*, it means two or more primary sources agree, or the fact was counted from a captured file; *reported* means one party says so; *disputed* means the sources disagree; *unverified* means even the reporting outlet could not check it.

## Articles, signed and dated
Where php2shell stands: many sites dark, millions of attempts, no confirmed breachJournalist · 2026-10-22 · written against v0.2.5php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proofHistorian · 2026-10-22 · written against v0.2.5
[All articles →](articles/index.html) The pages of this site are rebuilt from the vault on every release; an article is written once, against the evidence as it stood, and says which version that was.

## Six numbers, and what each one measures
70%the Internetunverifiedalmost 70%websitesreportedabout 30 millionwebsitesreported2,608,039internet-facing hosts running PHPreportedabout 6,000potentially affected resources in Latvia, a few hundred in the public sectorreported674software entries in the NCSC-NL php2shell inventoryconfirmed
The figures in circulation range from 2.6 million hosts to 70% of the Internet. They are not contradictory so much as incommensurable: each measures a different thing. [The numbers page](numbers/index.html) says what each one counts, who said it, and whether anyone has checked it.

## What is established
- There are two flaws, both in the PHP engine, both rated CVSS v4.0 9.2, both fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. The CVE records, the GitHub advisories and the php.net advisory agree on this. [CVE record](sources/cve-cve-2026-109618/index.html) [CVE record](sources/cve-cve-2026-109619/index.html) [PHP](sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](sources/php-net-advisory/index.html)
- Unauthenticated remote code execution was demonstrated against Apache with mod_php before any application code runs. PHP-FPM is susceptible; the two primary accounts differ on whether a complete FPM exploit exists. [PHP](sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](sources/openwall-oss-security-2026-10-21-6/index.html) [PHP Foundation](sources/php-foundation-blog-security-release/index.html)
- The flaws are old. The out-of-memory problem behind CVE-2026-109618 was first seen during a 2024 audit (Quarkslab, funded through OSTIF) and left unfixed because nobody could prove exploitation. PHP 8.1 and older are out of support; the project published minimal source backports for 7.4, 8.0 and 8.1, but the CVE records list only 8.2 to 8.5. [PHP Foundation](sources/php-foundation-blog-security-release/index.html) [Calif](sources/calif-php2shell/index.html) [php-src](sources/github-php-src-branch-7.4-backport/index.html) [CVE record](sources/cve-cve-2026-109618/index.html)
- Discovery was AI-assisted and three parties claim it. Calif reported first (hash on 5 August, report on 11 August); OpenAI reported the same root cause the same day; Wiz found it independently on 19 August and reported on 24 August. The GitHub advisories credit four reporters. [Calif](sources/calif-php2shell/index.html) [Ryan Austin , Calif on X](sources/x-lcfr-hax-hash-tweet/index.html) [PHP Foundation](sources/php-foundation-blog-security-release/index.html) [Wiz](sources/wiz-blog-php2shell/index.html) [PHP](sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- Disclosure broke down on 20 October around 15:00 UTC, when the CVE IDs circulated with a wrong CVSS of 10.0. The release moved forward a day; Calif published, then deleted, a demonstration video; Chainguard shipped patched images six hours before the embargo lifted. [PHP Foundation](sources/php-foundation-blog-security-release/index.html) [Daubois](sources/daubois-blog-php2shell-rumors/index.html) [PHP Foundation](sources/phpfoundation-blog-security-release-leak/index.html)
- The scale figures do not measure the same thing. *70% of the Internet* is a Wiz headline; the body of the same post, Cloudflare and OpenAI say 70% of *websites*; VulnCheck counts 2.6 million internet-facing hosts; Alan Woodward said *something like 30 million websites*; Latvia counted about 6,000 potentially affected resources in one country. [Wiz](sources/wiz-blog-php2shell/index.html) [Wiz on X](sources/x-wiz-io-php2shell/index.html) [Cloudflare](sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](sources/x-openai-php2shell/index.html) [THN](sources/thehackernews-php2shell-4days/index.html) [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html) [CERT.LV](sources/certlv-php-preventive/index.html)
- Exploitation attempts are reported from several directions, but no agency has confirmed a successful compromise. Amazon says a honeypot was hit on 17 October, four days before disclosure. Cloudflare saw attack traffic after the leak. Latvia saw automated attempts, none successful. CISA has not listed either CVE as known-exploited. New Zealand's NCSC alone says it is *aware of reports of active exploitation*. [THN](sources/thehackernews-php2shell-4days/index.html) [Cloudflare](sources/cloudflare-blog-php2shell-waf/index.html) [CERT.LV](sources/certlv-php-preventive/index.html) [CISA](sources/cisa-kev-json/index.html) [NCSC New Zealand](sources/ncsc-nz-alert-php/index.html)
- The agencies do not agree on taking systems offline. The NSA and CISA say take them offline if you cannot patch; the UK NCSC puts that fourth, after patching and temporary mitigations; CERT-EU, Canada and France say isolate; Australia, the Netherlands, Italy, Japan and New Zealand give no offline advice at all. [NSA Cyber on X](sources/nsa-x-2112903220209098897/index.html) [CISA](sources/cisa-alert-php-20261021/index.html) [NCSC UK](sources/ncsc-news-php/index.html) [CERT-EU](sources/certeu-sa-2026-018/index.html) [CCCS](sources/cccs-al26-026/index.html) [CERT-FR](sources/certfr-2026-ale-014/index.html) [ACSC](sources/acsc-alert-php/index.html) [NCSC-NL](sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](sources/acn-it-php2shell/index.html) [JPCERT/CC](sources/jpcert-at260033/index.html) [NCSC New Zealand](sources/ncsc-nz-alert-php/index.html)

## What is not

Open questions, stated rather than papered over. Each one names what would close it.
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.
- What the 70% figure is measured from. None of the three pages that carry it names the measurement.
- The model and the method. Calif says no special harness and names no model; OpenAI's blog, which we could not capture, reportedly names GPT-5.6 Sol; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas. What did the models do and what did the people do?
- OpenAI's own blog post, the Patch the Planet launch post, the Spanish and Portuguese advisories and the Techzine piece on Chainguard are all blocked by bot challenges from this capture environment. The block is recorded; the content is not read.

## The last 48 hours

| When (UTC) | What | Source |
|---|---|---|
| 2026-10-22 05:20 UTC | JVN publishes its note (14:20 JST); JPCERT/CC alert JPCERT-AT-2026-0033 is dated 22 October. | [JPCERT/CC](sources/jpcert-home/index.html) [JPCERT/CC](sources/jpcert-at260033/index.html) |
| 2026-10-22 06:16:24 UTC | BBC News opens its live page: 'Global scramble to fix critical cyber-security flaws as many websites taken offline'. | [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 06:45:47 UTC | Greenbone on oss-security: the backports imply versions down to 7.4 are affected, whatever the subject line says. | [oss-security](sources/openwall-oss-security-109619-thread/index.html) |
| 2026-10-22 06:55:50 UTC | The BBC reports the NSA's X post. | [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 07:00 UTC | Ryan Austin on BBC Radio 4: no evidence of exploitation yet. | [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 07:30:02 UTC | The UK NCSC page is modified (HTTP last-modified). | [NCSC UK](sources/ncsc-news-php/index.html) |
| 2026-10-22 08:03 UTC | The evidence vault behind this site is opened; the first capture of the BBC live page is at 08:04:53Z. | [BBC News](sources/bbc-live-ckgel5xp2xv9t/index.html) |
| 2026-10-22 08:40:58 UTC | NCSC-NL merges pull request 10; the inventory has 674 entries at commit cca173c64ec5. | [NCSC-NL](sources/ncsc-nl-php2shell-software-list/index.html) [NCSC-NL](sources/ncsc-nl-php2shell/index.html) |

[The whole timeline →](timeline/index.html) runs from the 2024 audit to the latest capture, with every time stated as its source states it and every conversion marked.

## Questions readers ask

Asked in group chats, newsrooms and boardrooms; each answer is short enough to paste back, and points at the pages and sources behind it.
- [Can anything be done to fix it, or do we just have to wait for updates?](questions/fix-or-wait/index.html) The updates already exist: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 were released on 21 October and fix both flaws.
- [Is PHP really the software behind most websites?](questions/most-websites/index.html) Roughly, if you count websites, not servers or the internet.
- [Has anyone actually been hacked?](questions/been-hacked/index.html) Not that anyone has confirmed.
- [Do I need to change my passwords?](questions/passwords/index.html) Not because of this, as things stand.
- [How do I know whether my site is affected?](questions/am-i-affected/index.html) If the site runs on PHP (WordPress, Drupal, Joomla, Magento, MediaWiki, and Laravel all do) and the running PHP version is older than 8.5.12, 8.4.27, 8.3.36 or 8.2.35 without a distribution backport, it is affected.

[Every question, and the page that answers it →](questions/index.html)

## Read it for your job

12 briefings from the same claims. None adds a claim; each selects, orders and keeps every source.
Board member or executiveAre we exposed, what is it costing us, and who owns the decision to pull a system?Security leadWhat do I patch first, what do I watch for, and when do I take something offline?PHP or platform engineerWhich versions, which SAPIs, which settings, which commands?JournalistWhich numbers hold up, who said what first, and what is still unverified?Security researcherWhat are the bug classes, what was demonstrated, and what is still open?Analyst or advisorHow did coordinated disclosure fail, and what does AI-assisted discovery change?CISOWhat is our exposure, what is our evidence we were not hit, and what do I tell the board?CTOWhat does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?CFOWhat is the financial exposure, what does downtime cost against breach cost, and will insurance respond?Head of AppSecWhich of our applications are in scope, which settings matter, and what do we add to the pipeline?DeveloperIs my code the problem, what do I change, and how do I check the box I deployed to?Media and communications teamWhat can we say that is true, what should we not say, and what will we be asked?

## How this site works

### Capture, don't paraphrase

Every source is captured into a private, encrypted vault: the page as served, as rendered, its text, a screenshot and its headers, each file hashed at capture time. Captures are only ever added, so a page that changes leaves a series. The captures are third-party pages and are not republished; [their hashes are](sources/index.html).

### Claims carry a status

Five words, each defined: confirmed, reported, disputed, contradicted, unverified. A claim is a row pointing at the sources that give it that status, and the page never upgrades a claim its sources do not support.

### Rebuilt, never edited

The site is a deterministic function of the vault and a version number: the same data produces byte-identical pages, there is no clock in the build, and a gate refuses to release a broken link, an orphan page, an unsourced claim or a credential. [The method](method/index.html), [the team](team/index.html) and [the billing model](billing/index.html) are published.


---
site v0.2.11 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/index.html
