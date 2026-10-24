# Synthetic readers: what they said about each page

> About this site: how the site works, kept by the agents that run it.

Every page of the site named in the synthetic readers' latest reviews, with what fails, what to change, what works and the lines they reacted to, from all six readers.

# What the synthetic readers said, page by page

Every page of this site that a synthetic reader named in its latest review, with what does not work, what to change, what works and the lines it reacted to, from all six readers at once. Pages are ordered by how much the readers found wrong with them: a high-severity failure counts five, a medium two, a low one, a requested change one.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

## The pages

| Page | Readers | Fails (high) | Changes asked | Works |
|---|---|---|---|---|
| [index.html](#index-html) | 5 | 10 (1) | 9 | 8 |
| [patching/index.html](#patching-index-html) | 3 | 7 (2) | 5 | 4 |
| [briefings/board/index.html](#briefings-board-index-html) | 1 | 5 (1) | 5 | 2 |
| [briefings/cto/index.html](#briefings-cto-index-html) | 1 | 5 (1) | 5 | 2 |
| [briefings/pm/index.html](#briefings-pm-index-html) | 1 | 3 (2) | 3 | 3 |
| [claims/index.html](#claims-index-html) | 2 | 3 (2) | 2 | 3 |
| [exploitation/index.html](#exploitation-index-html) | 1 | 3 (1) | 2 | 2 |
| [briefings/developer/index.html](#briefings-developer-index-html) | 1 | 1 (1) | 1 | 1 |
| [impact/index.html](#impact-index-html) | 1 | 2 (0) | 2 | 1 |
| [playbook/index.html](#playbook-index-html) | 2 | 2 (0) | 2 | 2 |
| [code/index.html](#code-index-html) | 1 | 3 (0) | 1 | 1 |
| [flaws/index.html](#flaws-index-html) | 2 | 2 (0) | 1 | 8 |
| [defence/index.html](#defence-index-html) | 2 | 1 (0) | 2 | 4 |
| [glossary/index.html](#glossary-index-html) | 1 | 1 (0) | 1 | 0 |
| [sources/index.html](#sources-index-html) | 1 | 1 (0) | 1 | 0 |
| [status.json](#status-json) | 1 | 1 (0) | 1 | 0 |
| [timeline/index.html](#timeline-index-html) | 1 | 1 (0) | 1 | 0 |
| [admin/versions.html](#admin-versions-html) | 1 | 1 (0) | 0 | 0 |
| [articles/index.html](#articles-index-html) | 1 | 1 (0) | 1 | 0 |
| [llms.txt](#llms-txt) | 1 | 1 (0) | 1 | 1 |
| [questions/index.html](#questions-index-html) | 1 | 1 (0) | 1 | 1 |
| [start/index.html](#start-index-html) | 1 | 1 (0) | 1 | 1 |
| [sources/cisa-alert-log4j-2021/index.html](#sources-cisa-alert-log4j-2021-index-html) | 1 | 1 (0) | 0 | 0 |
| [agencies/index.html](#agencies-index-html) | 1 | 0 (0) | 0 | 1 |
| [briefings/everyone/index.html](#briefings-everyone-index-html) | 1 | 0 (0) | 0 | 1 |
| [briefings/security/index.html](#briefings-security-index-html) | 1 | 0 (0) | 0 | 1 |
| [explained/index.html](#explained-index-html) | 2 | 0 (0) | 0 | 2 |
| [questions/old-php/index.html](#questions-old-php-index-html) | 1 | 0 (0) | 0 | 1 |
| [review/index.html](#review-index-html) | 1 | 0 (0) | 0 | 1 |

## [index.html](../../../index.html)

5 of 6 readers: Board member, CTO, Designer, Project manager, Security lead

### What does not work
- **low** An unexplained price badge in the header ticks down as I read, which I cannot interpret and which makes me wonder whether I am being charged. ([CTO](../../../admin/synthetic/cto/index.html))Header badge reads '£4.99' on index.html, '£4.98' on briefings/cto, then down to '£4.90' on the glossary; nothing on the pages explains it.
- **low** The header has a price-like badge that went down as I moved between pages, with no explanation; it made me wonder whether I was being charged. ([Project manager](../../../admin/synthetic/pm/index.html))Badge reads '£5.00' on the front page, '£4.97' on the PM briefing, '£4.95' on the playbook and '£4.91' on the old-PHP question.
- **low** The navigation wraps onto a second line at my desktop width, which pushes 'About' onto a line of its own, and the reading bar and the research banner take most of the first screen before any content. ([Project manager](../../../admin/synthetic/pm/index.html))fold.png: 'About' sits alone under 'FOR YOU'; the headline starts about 315px down at 1280x800.
- **medium** The front page tally of statuses does not match the claims page, and its legend has four statuses where the rest of the site uses five. ([Security lead](../../../admin/synthetic/security/index.html))index.html: '70 statements checked: 22 confirmed, 11 disputed, 4 unverified' and a legend without CONTRADICTED. claims/index.html: '70 claims: 22 confirmed, 33 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **low** Amazon's own wording, 'broadly exploited in the wild', appears only deep in the claims rows. The at-a-glance block reads as calmer than the primary vendor source does. ([Security lead](../../../admin/synthetic/security/index.html))index.html at a glance: 'ARE ATTACKERS TRYING? Yes ... seen by one internet security company', with no mention of Amazon's 'PHP2Shell is now being broadly exploited in the wild' (claims/index.html, REPORTED 1/2).
- **low** An unexplained price pill in the header changes from page to page, which is odd on a site I am meant to trust. ([Security lead](../../../admin/synthetic/security/index.html))The header shows '£4.99' on index.html, '£4.98' on briefings/security, '£4.97' on exploitation and '£4.92' on the source page, with no label.
- **high** An unlabelled money figure sits in the masthead and changes from page to page with no explanation, which reads as a charge and undermines trust for a newcomer. ([Designer](../../../admin/synthetic/designer/index.html))Desktop pill shows '£4.99' on index.html, '£4.96' on briefings/everyone, '£4.95' on claims and glossary, '£4.94' on explained; the phone shows '£5.00', '£4.98' and '£4.97'. Nothing on the visible page says what it is.
- **medium** Desktop navigation wraps: 'About' drops alone onto a second row under 'SITE', which looks like a layout bug at 1440px. ([Designer](../../../admin/synthetic/designer/index.html))fold.png on every page: the 'SITE' label ends row one and 'About ▾' sits by itself on row two at y=99.
- **medium** The reading-tracker panel ('Your reading: on this page 9 new, 0 changed, 0 read', fade / hide / show) is the first thing on every page, above the headline, and means nothing to a first-time visitor. ([Designer](../../../admin/synthetic/designer/index.html))It is the first block of fold text on all seven pages, ahead of the h1; 'Read items: fade hide show' has no explanation.
- **low** Counts on the front page do not match the status scheme used on the claims page. ([Designer](../../../admin/synthetic/designer/index.html))index.html: '70 statements checked: 22 confirmed, 11 disputed, 4 unverified'; claims: '22 confirmed, 33 reported, 8 disputed, 3 contradicted, 4 unverified'. The front page legend also lists four status words, claims lists five.

### What to change
- Explain or remove the '£4.99' header badge. ([CTO](../../../admin/synthetic/cto/index.html), small)An unexplained, falling price next to a security briefing makes me doubt what I am looking at.
- Offer a printable or forwardable one-page version of the At a glance block plus the core facts with their status labels. ([CTO](../../../admin/synthetic/cto/index.html), medium)That block is the closest thing to something I can send to the board, but the page around it is not forwardable.
- Label or remove the '£5.00' header badge. ([Project manager](../../../admin/synthetic/pm/index.html), small)An unexplained falling money figure distracts and makes me doubt the site.
- Bring the front page tally and legend into line with the claims page (five statuses: 33 reported, 8 disputed, 3 contradicted). ([Security lead](../../../admin/synthetic/security/index.html), small)The first numbers I saw did not match the later ones, which made me doubt the rest until I checked.
- Add Amazon's 'broadly exploited in the wild' wording, graded, to the at-a-glance exploitation tile. ([Security lead](../../../admin/synthetic/security/index.html), small)A board member will see that headline elsewhere. The front page should show it and its grade, not only the calmer KEV view.
- On phone, move the 'Your reading' panel and the RESEARCH / ABOUT band below the h1 and standfirst (or collapse them into one line), so the headline is in the top third of the first screen. ([Designer](../../../admin/synthetic/designer/index.html), medium)The headline is the one thing to read first and on a phone it currently starts two-thirds of the way down on every page.
- Label the pound pill in the masthead (for example 'Reading credit: £4.95, free') or hide it until the reader opens the account menu. ([Designer](../../../admin/synthetic/designer/index.html), small)An unexplained, falling money figure is the single biggest trust risk for a newcomer.
- Fit the desktop navigation on one row at 1440px (tighten spacing or fold 'About' into the masthead). ([Designer](../../../admin/synthetic/designer/index.html), small)The orphaned 'About' makes every page look slightly broken on the main desktop size.
- Align the front-page counts with the claims page's five statuses, including reported. ([Designer](../../../admin/synthetic/designer/index.html), small)A designer notices when two summaries of the same numbers disagree, and so will a sceptical reader.

### What works, so do not break it
- The 'At a glance' tiles (Is there a fix? Yes. Anyone confirmed hacked? Not yet.) tell me in seconds how worried to be. ([Board member](../../../admin/synthetic/board/index.html))
- The opening paragraph is plain and reassuring in the right way: it says what PHP is, that a fix exists and that phones and laptops are not affected. ([Board member](../../../admin/synthetic/board/index.html))
- The status words (confirmed, reported, unverified) and the sources under each fact make me trust that I am not repeating a rumour to the board. ([Board member](../../../admin/synthetic/board/index.html))
- The At a glance block answers fix, severity, attackers, confirmed hacks, KEV status and agency advice in seven tiles: that is most of my first board slide. ([CTO](../../../admin/synthetic/cto/index.html))
- 'Last checked 22 October 2026, 11:34 UTC' in the header and UTC times throughout make the currency of the information unambiguous. ([Project manager](../../../admin/synthetic/pm/index.html))
- Strong serif headline, a generous sans-serif standfirst and one filled teal call to action beside two outlined ones: on desktop the one thing to read first is unmistakable. ([Designer](../../../admin/synthetic/designer/index.html))
- Dark mode is a real theme, not an inversion: the teal shifts to a brighter mint, the red rules soften, and the instruments found 0 low-contrast pairs in dark on every page. ([Designer](../../../admin/synthetic/designer/index.html))
- The 'Right now' cards with a red left rule and small grey source chips make every sentence look sourced at a glance; it is the most trustworthy visual pattern on the site. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *Phones and personal computers are not affected.* ([Board member](../../../admin/synthetic/board/index.html))Useful straight away: it tells me this is about our servers, not our staff laptops.
- *Phones and personal computers are not affected.* ([Designer](../../../admin/synthetic/designer/index.html))Placed last in the standfirst at a large size: the reassurance a newcomer needs, exactly where they look.
- *Your reading: on this page 9 new, 0 changed, 0 read; across the site 340 new and 0 changed of 340.* ([Designer](../../../admin/synthetic/designer/index.html))The first words on the page, before the headline. As a first-time visitor this is noise.

## [patching/index.html](../../../patching/index.html)

3 of 6 readers: CTO, Developer, Project manager

### What does not work
- **medium** Containers are my estate, but the container guidance stops at 'Docker Official Image: php fixed' with no tags or digest, and 'rebuild every image' with no way to tell which base images carry the fix. ([CTO](../../../admin/synthetic/cto/index.html))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version string, unlike the Ubuntu and Red Hat rows.
- **medium** The cPanel row under the 7.4 and 8.0 branches shows only 8.2, 8.3 and 8.4 packages, which contradicts the text saying cPanel backported to 7.4, 8.0 and 8.1. Many of my client sites are on cPanel, so this is the row I most need to trust. ([Project manager](../../../admin/synthetic/pm/index.html))Under 7.4: 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27' against 'cPanel backported to 7.4, 8.0 and 8.1'.
- **medium** The patching page is hard going for me: inventory commit hashes, 'the gate' and long package version strings before I reach the plain grouping by hosting type. ([Project manager](../../../admin/synthetic/pm/index.html))'each named exactly so the gate can check it is there and has the status quoted'; Flesch 34.4 from the instruments.
- **high** Comparing the php -v output with the fixed version list gives the wrong answer for distro backports, and the site itself lists them as fixed. An Ubuntu Noble box reports 8.3.6, which is below 8.3.36, yet the site marks that package as fixed. ([Developer](../../../admin/synthetic/developer/index.html))'fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13' against the briefing's 'Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35'. No version-independent check is offered, such as testing whether the new max_multipart_body_parts setting exists.
- **high** The Docker Official Image row, the one I care most about, has no tag, version or digest, so I cannot tell which php:* tags are fixed or whether my pinned digest is. ([Developer](../../../admin/synthetic/developer/index.html))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version text, while the Debian, Red Hat and Bref rows all carry versions.
- **medium** Downstream rows on the version ladder do not back up the branch they sit under: the cPanel row under 8.1, 8.0 and 7.4 lists only ea-php82, 83 and 84 packages. ([Developer](../../../admin/synthetic/developer/index.html))Under 8.1, 8.0 and 7.4: 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27'.
- **low** Several downstream rows are cut off mid-word. ([Developer](../../../admin/synthetic/developer/index.html))'Bref 3: php-85:21, php-84:24, php-83:24, php-82:26; Bref 2 l', 'Cloud Run customer containers with unpatched PHP on their re', 'fix still bei'.

### What to change
- Give the Docker Official Image row the fixed tags or the date the images were rebuilt, and add one line on how to verify the PHP version inside a running container. ([CTO](../../../admin/synthetic/cto/index.html), small)We run a dozen microservices on containers and 'rebuild every image' is only useful if I know which base image is safe.
- Fix or explain the cPanel row under the 7.4, 8.0 and 8.1 branches so the package names match the claim that cPanel backported to those versions. ([Project manager](../../../admin/synthetic/pm/index.html), small)Agency client sites are mostly on panels; I need to know which clients wait on cPanel and which on Plesk.
- Give the Docker Official Image row the fixed tags (8.5.12, 8.4.27, 8.3.36, 8.2.35 for each variant: cli, fpm, apache, alpine) and the date the images were rebuilt. ([Developer](../../../admin/synthetic/developer/index.html), small)I run on php:*-fpm and php:*-apache bases; without tags I cannot check my Dockerfiles or pinned digests.
- Apply the 675 correction everywhere 674 still appears, or say on the page which number is right and why. ([Developer](../../../admin/synthetic/developer/index.html), small)The site's own release notes contradict its pages, which undercuts the precision everything else is built on.
- Put each downstream row only under the branch its versions support (or explain the cPanel row), and show untruncated product text. ([Developer](../../../admin/synthetic/developer/index.html), small)A row under 8.1 that lists only 8.2 to 8.4 packages makes me doubt the whole ladder.

### What works, so do not break it
- What the fix changes (deferred OOM, memory_hard_limit_percent, max_multipart_body_parts, 389 files) is the side-effect list I need to plan regression testing, and it honestly says no regression has been reported yet. ([CTO](../../../admin/synthetic/cto/index.html))
- The section on how a fix reaches a server (patched for you, rebuild and redeploy, OS update, extended support, hosting panel, waiting on supplier) lets me sort client sites into workstreams by hosting type. ([Project manager](../../../admin/synthetic/pm/index.html))
- It says plainly what the patch changes at runtime (delayed OOM, new memory_hard_limit_percent and max_multipart_body_parts). That is what I need to warn the team about test changes. ([Developer](../../../admin/synthetic/developer/index.html))
- 'How a fix reaches a server' splits patched-for-you from rebuild-and-redeploy, and quotes 'Existing deployments are not automatically patched'. This is the line that matters for container users. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *The downstream rows are the NCSC-NL inventory's own rows at commit cca173c64ec5 (22 October, 08:40 UTC), each named exactly so the gate can check it is there and has the status quoted.* ([CTO](../../../admin/synthetic/cto/index.html))Lost me: 'the gate' is the site's internal plumbing, not something I need in the opening paragraph.
- *each named exactly so the gate can check it is there and has the status quoted* ([Project manager](../../../admin/synthetic/pm/index.html))I do not know what 'the gate' is, and I do not need to know in order to plan.
- *fixed Docker Official Images maintainers: Docker Official Image: php* ([Developer](../../../admin/synthetic/developer/index.html))Fixed which tags? This row is where I needed detail and got none.
- *fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13* ([Developer](../../../admin/synthetic/developer/index.html))So php -v on this box says 8.3.6 and the site says it is fixed; the briefing's check does not account for this.

## [briefings/board/index.html](../../../briefings/board/index.html)

1 of 6 readers: Board member

### What does not work
- **high** On a phone the first screen of every page is site machinery, not the story: version badge, a £ meter, a reading tracker with 'fade / hide / show' buttons and a 'Research' box. On the board briefing the thirty-second answer only begins at the very bottom of the first screen. ([Board member](../../../admin/synthetic/board/index.html))fold.png shows 'Your reading: on this page 35 new, 0 changed, 0 read', 'Mark this page read', 'Mark everything read', 'Read items: fade hide show', the RESEARCH box and the 'New to this story?' banner before 'THE ANSWER IN THIRTY SECONDS' appears at the bottom edge.
- **medium** The briefing promises to cover 'what is it costing us' but never gives me any sense of cost, for downtime or for a breach; it only points me to other readers' briefings. ([Board member](../../../admin/synthetic/board/index.html))Heading question 'Are we exposed, what is it costing us...' while the body says 'what it costs to find out' and nothing more; the CFO briefing is only listed under 'Other readers'.
- **medium** Nothing speaks to my kind of business. Online shops are mentioned only in passing in a list of things the BBC reported offline; there is no line saying what an e-commerce site on PHP stands to lose (card data, customer accounts). ([Board member](../../../admin/synthetic/board/index.html))The only shop reference I found is 'French government services; the University of Geneva; the BBC; online shops' in the impact table; the Questions page says Magento runs on PHP but the board briefing does not.
- **medium** The 'What is still open' section in my briefing is written for a journalist, not a director: deleted videos, Fediverse reports and oss-security mean nothing to me. ([Board member](../../../admin/synthetic/board/index.html))'Whether the deleted Calif video is the one now embedded on Calif's own write-up.' and 'A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October'.
- **low** Words listed for me to 'meet' include terms the briefing itself tells me to skip, which is confusing. ([Board member](../../../admin/synthetic/board/index.html))'What you can skip: SAPIs and settings' but 'Words you will meet' lists 'SAPI', 'KEV', 'Honeypot'.

### What to change
- Move the reading tracker, £ meter and Research box below the article on phones (or collapse them into one line), so the thirty-second answer is the first thing on the first screen. ([Board member](../../../admin/synthetic/board/index.html), medium)Between meetings I have seconds; today I scroll past controls I never use before I learn whether to worry.
- Add two or three sentences on cost: what downtime has looked like for organisations so far (for example Weird Gloop's 13 hours) and what a breach would put at risk, with a link to the CFO briefing. ([Board member](../../../admin/synthetic/board/index.html), small)The headline asks 'what is it costing us' and the page never answers it.
- Add one line for organisations that sell online: shop platforms such as Magento and WordPress shops run on PHP, and a compromise could reach customer data and payment settings. ([Board member](../../../admin/synthetic/board/index.html), small)It would tell me in one sentence that my company is squarely in scope and why it matters to us.
- Rewrite 'What is still open' for a director: keep 'nobody confirmed hacked yet' and 'the fix may not be complete', drop the video and Fediverse details or move them to the journalist briefing. ([Board member](../../../admin/synthetic/board/index.html), small)The two open points that change my board questions are buried among forensics I cannot judge.
- Add a 'What to ask management' heading wording (instead of 'What to decide or do') and number the questions. ([Board member](../../../admin/synthetic/board/index.html), small)Numbered questions are easier to read out in a meeting and to tick off as management answers.

### What works, so do not break it
- The thirty-second answer in the board briefing is exactly the shape I need: what happened, what agencies say, no confirmed break-in, and the three questions to ask. ([Board member](../../../admin/synthetic/board/index.html))
- 'What to decide or do' is a ready-made list of board questions (inventory including vendor products, patched and restarted, who can pull a system, what a compromise would reach, evidence we were not hit). I can copy these straight into my notes. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast.* ([Board member](../../../admin/synthetic/board/index.html))This is what I came for. I could read this sentence aloud at the board meeting.
- *What is our evidence that we were not exploited between the leak on 20 October and our patch?* ([Board member](../../../admin/synthetic/board/index.html))A good, pointed question I would not have thought to ask on my own.
- *Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.* ([Board member](../../../admin/synthetic/board/index.html))I have no idea who Calif is or why this matters to my company; it lost me.

## [briefings/cto/index.html](../../../briefings/cto/index.html)

1 of 6 readers: CTO

### What does not work
- **high** No board-ready summary anywhere on my path: the CTO briefing headline question drops 'what do I tell the board', and the Board member briefing is a separate path. ([CTO](../../../admin/synthetic/cto/index.html))Headline: 'What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?' No section addresses board messaging; the board appears only as 'Board member or executive' in the Other readers list at the foot.
- **medium** The CTO path is far longer than my time: the briefing itself is 2,093 words and 6.5 screens, and the reading path is quoted as 20 minutes. ([CTO](../../../admin/synthetic/cto/index.html))'About 20 minutes in all.' and 'Your briefing 3 min', while the instruments measured 2,093 words on this page alone.
- **medium** The claims table is long and chronologically mixed: disclosure-timing disputes (pre-announcement at 19:30 vs 20:32 UTC, release time) sit alongside the facts I need to act on, with no grouping. ([CTO](../../../admin/synthetic/cto/index.html))'The pre-announcement was published at 19:30 UTC on 20 October' DISPUTED and 'The fixes were released at 14:00 UTC on 21 October' DISPUTED appear in the same table as patch and FPM claims, even though the briefing says I can skip 'the disclosure politics'.
- **low** The top ~200px of every page is taken by the reading tracker and the research banner before any content, which pushes the answer below the fold on a 900px screen. ([CTO](../../../admin/synthetic/cto/index.html))fold.png: 'Your reading: on this page 24 new...', 'Mark this page read', 'Read items: fade hide show', 'RESEARCH collected from outside sources...' and a 'New to this story?' bar all precede the headline.
- **low** The briefing's 'Read the site as Avery' and persona names add a layer I do not need; I am the CTO, not Avery. ([CTO](../../../admin/synthetic/cto/index.html))'BRIEFING FOR AVERY, CTO' and 'Read the site as Avery →'.

### What to change
- Add a 'What to tell the board' box of four or five sentences (severity and evidence, our likely exposure class, the fix and its risk, the timeline, what is still unknown) just under the thirty-second answer. ([CTO](../../../admin/synthetic/cto/index.html), small)It is a quarter of my question and the one I have to answer in person, and right now I have to assemble it myself.
- Split the claims table into 'Decide on these' (severity, fix, FPM, EOL, WAF, side effects) and 'Background' (timing and attribution disputes), collapsing the second. ([CTO](../../../admin/synthetic/cto/index.html), small)The briefing tells me to skip the disclosure politics, then makes me read them to find the FPM and EOL rows.
- Add a one-line exposure guide by SAPI for planning (mod_php: demonstrated, today; FPM: susceptible and disputed, this week at latest) to the thirty-second answer. ([CTO](../../../admin/synthetic/cto/index.html), small)It turns 'how fast' into a schedule I can commit to and defend.
- Collapse the reading tracker and research banner into a single thin line on desktop, or show them below the page headline. ([CTO](../../../admin/synthetic/cto/index.html), medium)On a 900px screen they cost me the first third of every page before I see the answer.
- State honestly that the CTO path is 20 minutes and offer an 8-minute route (briefing top, flaws versions table, patching 'What the fix changes'). ([CTO](../../../admin/synthetic/cto/index.html), small)I have eight minutes and need to know which sections are the minimum.

### What works, so do not break it
- The thirty-second answer is exactly the right shape for me: patch order by SAPI, restart and rebuild, test under load, EOL versions have no release, then the inventory lesson. ([CTO](../../../admin/synthetic/cto/index.html))
- Every claim carries a status (confirmed, reported, disputed, contradicted, unverified) and a primary-source count like 5/5 or 0/1, so I can see at a glance what I can repeat and what I must caveat. ([CTO](../../../admin/synthetic/cto/index.html))

### Lines readers reacted to
- *Patch internet-facing mod_php first, then FPM, then the rest; restart every worker and rebuild every image. The fix changes how PHP behaves when memory runs out, so test under load.* ([CTO](../../../admin/synthetic/cto/index.html))This is the answer I came for, in two sentences. I can hand this to my platform lead as is.
- *7.4, 8.0 and 8.1 have a source backport and no release: that is a migration you are now doing, not a patch.* ([CTO](../../../admin/synthetic/cto/index.html))Blunt and correct framing for budgeting; this is the line that changes engineering time.
- *a system that used to survive on the edge of memory_limit may now _exit instead.* ([CTO](../../../admin/synthetic/cto/index.html))Concrete side effect, phrased so I know what to load-test. Good.
- *About 20 minutes in all.* ([CTO](../../../admin/synthetic/cto/index.html))More than double my time; I need to know what to skip, not just how long the whole thing is.

## [briefings/pm/index.html](../../../briefings/pm/index.html)

1 of 6 readers: Project manager

### What does not work
- **high** No deadline anywhere. The guidance says 'now', 'this week' and 'the next fortnight' but never states whether any agency set a due date, so I cannot put a hard date on the plan or tell a client how late is too late. ([Project manager](../../../admin/synthetic/pm/index.html))'Expect unplanned work this week' and 'Keep a slot free in the next fortnight'; the playbook steps carry no dates at all.
- **high** Nothing on how to report progress, although the briefing's own question promises 'what do I tell stakeholders'. There is no status template, no suggested measures (systems inventoried, patched, verified, offline) and no wording for a client update. ([Project manager](../../../admin/synthetic/pm/index.html))'What this briefing covers' lists 'what to tell stakeholders about downtime', but the page body only says 'Agree with stakeholders now who can make that call'.
- **low** The PM briefing was written in an older site version than the one I was reading, and the page does not say whether its advice still holds against the 11:34 data. ([Project manager](../../../admin/synthetic/pm/index.html))'This briefing v2 written in site v0.3.1' while the header says 'v0.4.3'.

### What to change
- Add a 'Deadlines' line at the top of the PM briefing stating whether any agency set a due date (and that CISA has not listed these flaws in KEV, so no federal due date), plus a recommended internal target such as internet-facing patched within N days. ([Project manager](../../../admin/synthetic/pm/index.html), small)I plan against dates; 'this week' and 'next fortnight' cannot go in a programme plan or a client SLA conversation.
- Add a 'How to report progress' section with a copyable status table (system, owner, PHP version, hosting route, patched yes/no, verified running version, offline yes/no, next date) and a two-line stakeholder update template. ([Project manager](../../../admin/synthetic/pm/index.html), medium)Reporting is half my question and the briefing title promises it; with forty clients I need one consistent format.
- Make the PM briefing actions a downloadable or copyable checklist with tick boxes. ([Project manager](../../../admin/synthetic/pm/index.html), small)I would drop it straight into our tracker for each client.

### What works, so do not break it
- The thirty-second answer is exactly the stand-up summary I need: unplanned work this week, possible downtime, 8.1 and older becomes a migration, ask each owner for a patch date and a test plan. ([Project manager](../../../admin/synthetic/pm/index.html))
- 'What to decide or do' is six numbered actions in a sensible order that map straight onto a plan: inventory, date per system, regression budget, downtime decision, migration project, second round. ([Project manager](../../../admin/synthetic/pm/index.html))
- The datacentre-move framing (inventory, owner, date, test) gives me a planning shape I can explain to forty clients. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *Ask each system owner for a patch date and a test plan.* ([Project manager](../../../admin/synthetic/pm/index.html))Exactly the instruction I needed; this goes straight into my email to client leads.
- *Plan for it the way you would plan for a datacentre move: an inventory, an owner per system, a date, a test.* ([Project manager](../../../admin/synthetic/pm/index.html))Landed. It gives me a plan shape I already know how to run.
- *Expect a second round. A report that the first fix may be incomplete is open. Keep a slot free in the next fortnight.* ([Project manager](../../../admin/synthetic/pm/index.html))Useful warning, but 'next fortnight' is too loose to schedule against.

## [claims/index.html](../../../claims/index.html)

2 of 6 readers: Designer, Security lead

### What does not work
- **high** CONFIRMED is used for single-source items although the site's own definition requires two or more primary sources or a count from a captured file. ([Security lead](../../../admin/synthetic/security/index.html))The legend says 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file', yet the CISA offline-advice claim is 'CONFIRMED 1/1', Latvia's restrictions 'CONFIRMED 1/1' and Weird Gloop 'CONFIRMED 1/1'. On exploitation/index.html, CCCS, CERT.LV and the CISA ADP row are each 'CONFIRMED (PRIMARY)' on one source.
- **high** On a phone the site chrome eats most of the first screen: masthead, a theme dot, a price pill, the 'New to this story?' banner, the 'Your reading' panel and the RESEARCH band all come before the headline. ([Designer](../../../admin/synthetic/designer/index.html))Phone metrics put the h1 at 590px on claims and 550px on index.html in an 812px-tall screen; on briefings/everyone the thirty-second answer box only starts at the very bottom edge of fold-phone.png.
- **medium** Small, glyph-only controls repeat across the site and fail the tap-target check on phone. ([Designer](../../../admin/synthetic/designer/index.html))147 targets under 24px on claims at phone width; examples include the '○' and '⋯' buttons on every claim row (they do carry aria-labels, but visually they are bare symbols), and the theme switcher on phone is a lone teal dot with no visible label.

### What to change
- Re-run the status rules across every table so that a one-source primary item is REPORTED (or add a named 'PRIMARY, single source' grade to the legend), and use one grade per claim on every page. ([Security lead](../../../admin/synthetic/security/index.html), medium)I cannot hand the CISO a grading scheme that breaks its own definition. Consistency is what makes the labels citable.
- Give the '○' and '⋯' row controls and the read-state pills a 24px minimum hit area, and give the phone theme switcher a visible text label. ([Designer](../../../admin/synthetic/designer/index.html), small)147 undersized targets on the one page where readers most need to tap sources.

### What works, so do not break it
- Overstatements are called out with evidence: the CVSS 10.0 is marked CONTRADICTED, '70% of the Internet' is marked UNVERIFIED, and the CVE record's 8.2 to 8.5 range is flagged as missing 7.4 to 8.1 for scanners. ([Security lead](../../../admin/synthetic/security/index.html))
- Status badges are consistent between the front page and the claims table (CONFIRMED in green, UNVERIFIED in red, REPORTED and DISPUTED neutral) and each is defined once above the table. ([Designer](../../../admin/synthetic/designer/index.html))
- No horizontal overflow on any page at phone, tablet or desktop, and no images missing alt text. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *CONFIRMED two or more primary sources agree, or the fact was counted from a captured file* ([Security lead](../../../admin/synthetic/security/index.html))A good definition, but then 'CONFIRMED 1/1' appears several times below it. Hold yourselves to it.
- *The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.* ([Designer](../../../admin/synthetic/designer/index.html))Trust-building idea, but 'the build' and 'the manifest' are internal words in the intro paragraph of a page also flagged at reading ease 27.8.

## [exploitation/index.html](../../../exploitation/index.html)

1 of 6 readers: Security lead

### What does not work
- **high** The site contradicts itself about whether Amazon's own post was captured, while still grading the claim built on it as CONFIRMED. ([Security lead](../../../admin/synthetic/security/index.html))The exploitation row for Alan Woodward reads 'Cloudflare's own post confirms attack traffic, Amazon's own post not found', but claims/index.html grades 'Amazon and Cloudflare saw sites being probed' CONFIRMED with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog' (capture 20261022T111755Z).
- **medium** The same CERT.LV statement carries different grades on different pages. ([Security lead](../../../admin/synthetic/security/index.html))exploitation/index.html: CERT.LV 'Automated exploitation attempts seen in Latvia; no reports of successful attacks' graded 'CONFIRMED (PRIMARY)'. claims/index.html and briefings/security/index.html: 'Automated exploitation attempts were seen in Latvia; none succeeded' graded 'REPORTED 1/1'.
- **medium** The headline count of exploitation signals counts the same Amazon honeypot event twice. ([Security lead](../../../admin/synthetic/security/index.html))'What the captured sources carry is 20 signals', but the first two rows are the same 17 October MadPot attempt, once from the AWS blog and once 'via The Hacker News'.

### What to change
- Fix the Woodward row to say Amazon's own post was captured, and link the Amazon claim to the aws-security-blog-madpot capture. ([Security lead](../../../admin/synthetic/security/index.html), small)This is the single clearest self-contradiction on the exploitation question, which is the question I most need to get right.
- Make the signal count 19 distinct events (or say '20 rows, 19 events'), merging the two Amazon 17 October rows. ([Security lead](../../../admin/synthetic/security/index.html), small)Double counting weakens a page whose whole value is careful counting.

### What works, so do not break it
- Attempts, honeypot hits and compromises are separated in every exploitation row, and the KIND column (attempt, negative finding, claim, second-hand) is exactly the distinction I have to make to the CISO. ([Security lead](../../../admin/synthetic/security/index.html))
- The KEV negative finding is dated to the catalog version, release time, fetch time and entry count, and is called a point-in-time finding. I can cite that as written. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *A remote code execution bug is not an invisibility cloak.* ([Security lead](../../../admin/synthetic/security/index.html))Good framing, and the page earns it by listing the signals. I will borrow this line.
- *This is a point-in-time negative finding; the vault keeps the file and its hash so that the time can be proven later.* ([Security lead](../../../admin/synthetic/security/index.html))Exactly how I want a KEV absence stated: dated, bounded, provable.
- *REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found* ([Security lead](../../../admin/synthetic/security/index.html))This lost me: the sources page lists Amazon's own post as captured, and the claims page says both companies confirmed it.

## [briefings/developer/index.html](../../../briefings/developer/index.html)

1 of 6 readers: Developer

### What does not work
- **high** There is no real verification step for container images: one sentence about php -v, no docker run command, no image tags, no check that works on a distro backport. ([Developer](../../../admin/synthetic/developer/index.html))The only instruction is 'Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.' Nothing on the page or the reading path adds to it.

### What to change
- Add a 'Verify your image' block with copy-paste commands: docker run --rm  php -v, plus a check that does not depend on the version number (for example whether php -r 'var_dump(ini_get("max_multipart_body_parts"));' returns a value, if the site can confirm it marks a patched build) and the distro changelog check for backports. ([Developer](../../../admin/synthetic/developer/index.html), medium)This is the half of my question the site does not answer, and php -v alone gives the wrong result on the Ubuntu and Red Hat backports the site lists as fixed.

### What works, so do not break it
- The thirty-second answer is right for a developer: the flaw is in the C engine, ini_set, .user.ini and auto_prepend_file run too late, check the running version after the restart. It stopped me wasting time on app-level fixes. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Nothing in userland blocks the demonstrated paths: ini_set() runs too late, .user.ini runs too late, auto_prepend_file runs too late.* ([Developer](../../../admin/synthetic/developer/index.html))Exactly what I needed to hear first; it kills the idea of a code-side hotfix.
- *Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.* ([Developer](../../../admin/synthetic/developer/index.html))Right instinct, but this is the whole verification guidance, and it is not enough for images or backports.
- *After the patch, out-of-memory behaves differently: a delayed fatal at the next safe point instead of an abort, and a hard limit that ends the process.* ([Developer](../../../admin/synthetic/developer/index.html))Useful and rarely said; I will tell QA about it.

## [impact/index.html](../../../impact/index.html)

1 of 6 readers: Board member

### What does not work
- **medium** The impact page tables are squeezed into six narrow columns on a phone, so each row becomes a tall stack of two- or three-word lines and the page runs to more than nine screens. ([Board member](../../../admin/synthetic/board/index.html))full.jpg shows the 'Taken offline' table with columns WHO, WHAT HAPPENED, WHEN, WHO SAYS SO, STATUS, SOURCES each a sliver wide; instruments: 9.4 screens, reading ease 8.9.
- **medium** The closing summary of the impact page drops straight into technical jargon I cannot get past. ([Board member](../../../admin/synthetic/board/index.html))'how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell'.

### What to change
- On phones, turn the two impact tables into stacked cards (who, what happened, who says so, status) instead of six narrow columns. ([Board member](../../../admin/synthetic/board/index.html), medium)The page is the evidence that offline is a precaution, but on my phone it is unreadable slivers.
- Replace the mod_php and x86_64 sentence at the end of the impact page with a plain version: nobody yet knows how many unpatched sites were actually broken into. ([Board member](../../../admin/synthetic/board/index.html), small)It is the conclusion of the page and I could not follow it.

### What works, so do not break it
- The 'IN PLAIN ENGLISH' line at the top of the impact page saves a non-technical reader: two lists, many offline as a precaution, nobody confirmed broken into. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *the reported cost of php2shell so far is the cost of precaution.* ([Board member](../../../admin/synthetic/board/index.html))The single best line for a board: so far the damage is downtime, not breaches.
- *how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell.* ([Board member](../../../admin/synthetic/board/index.html))Complete jargon. I gave up on this paragraph.

## [playbook/index.html](../../../playbook/index.html)

2 of 6 readers: CTO, Project manager

### What does not work
- **medium** The playbook steps have no owner or role column, so I have to work out myself which steps are mine, the client's, the host's or the developer's. ([Project manager](../../../admin/synthetic/pm/index.html))Steps 0 to 6 list actions and agency chips only, e.g. step 2 is a string of settings ('memory_limit=-1 ... pm.max_requests=1 on FPM') with no 'who'.
- **low** The opening sentence about where 'offline' sits in the order lost me, and the order matters for my plan. ([Project manager](../../../admin/synthetic/pm/index.html))'Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.'

### What to change
- Add a 'Who does this' label to each playbook step (inventory owner, host or platform, developer, security, decision-maker). ([Project manager](../../../admin/synthetic/pm/index.html), small)Lets me turn the steps straight into assigned tasks instead of translating each one.
- Rewrite the playbook's opening sentence on where 'offline' falls into one plain line, for example 'Most agencies put taking a site offline last; CERT-EU, Canada and France put isolation earlier.' ([Project manager](../../../admin/synthetic/pm/index.html), small)The order is what I am planning; a sentence I had to read three times undermines the list.

### What works, so do not break it
- Numbered steps 0 to 6 with the agencies behind each step shown as chips; I can cite the source of every line of my plan. ([Project manager](../../../admin/synthetic/pm/index.html))
- 'Decide who can make that call and how fast it can be executed, and write it down before you need it' is a clear action for me, not just for engineers. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *a system that cannot is one you take offline early, because you will not be able to later.* ([CTO](../../../admin/synthetic/cto/index.html))A sharp decision rule I can actually apply to our services list.
- *Decide who can make that call and how fast it can be executed, and write it down before you need it.* ([Project manager](../../../admin/synthetic/pm/index.html))Good: a governance action I own, not an engineering one.
- *Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.* ([Project manager](../../../admin/synthetic/pm/index.html))Lost me. I could not tell whether offline is early or late in the order.
- *memory_limit=-1 where applications cannot override it; low post_max_size with proxy-level request limits; a cgroup memory limit instead of RLIMIT* ([Project manager](../../../admin/synthetic/pm/index.html))Not for me; fine to hand to engineers, but I need a one-line plain summary above it.

## [code/index.html](../../../code/index.html)

1 of 6 readers: Developer

### What does not work
- **low** The hunks are called verbatim but contain elisions, so I cannot paste them into a grep against the source. ([Developer](../../../admin/synthetic/developer/index.html))'the hunks below are verbatim' followed by 'bool *did_gc ...)', 'if (gc && zend_mm_gc(heap)) { ... }' and a bare '...' line in zend_handle_delayed_oom.
- **low** The code block has no diff colouring: '+' and '-' lines look the same as context in dark mode, so the old and new shapes blur together. ([Developer](../../../admin/synthetic/developer/index.html))full.jpg: the removed zend_bailout() block and the added PHP_INI_ENTRY and ZVAL_UNDEF lines are the same white monospace on the same background.
- **low** About 300px of site chrome (reading bar, research strip, two-row nav, banner) sits above every H1 at 1440x900, so the first screen of a technical page is mostly furniture. ([Developer](../../../admin/synthetic/developer/index.html))fold.png: the H1 'The code: where the bug is, and what the fix does' starts at roughly y=340 of 900. The same happens on flaws, patching, affected and review.

### What to change
- Mark the elisions in the hunks as elided (or drop the word verbatim), colour the + and - lines, and link the commit hash to the upstream php-src commit. ([Developer](../../../admin/synthetic/developer/index.html), small)I want to grep and diff these myself, and in dark mode the removed and added lines are hard to tell apart.

### What works, so do not break it
- The fix commit hash, parent, authors, merge times into each branch, the step-by-step before and after, and readable C hunks for zend_mm_check_limit, zend_handle_delayed_oom and the http_globals reset. I can go and diff this myself. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Each step names the function or file it comes from; the hunks below are verbatim.* ([Developer](../../../admin/synthetic/developer/index.html))Then the hunks contain '...'. Small, but it is the kind of claim I check.

## [flaws/index.html](../../../flaws/index.html)

2 of 6 readers: CTO, Developer

### What does not work
- **low** How fast must we move is stated as agencies saying 'now', but there is no concrete risk framing for an FPM-and-containers estate beyond 'susceptible' and a disputed FPM claim. ([CTO](../../../admin/synthetic/cto/index.html))'PHP-FPM susceptible ... the GitHub advisory says no complete FPM exploit has been demonstrated; the PHP Foundation blog says RCE was confirmed on FPM through application-level paths.'
- **medium** The SAPI table stops at FrankenPHP and LSAPI. It does not cover long-running worker servers (Octane with Swoole or RoadRunner), which many Laravel deployments use and where the stale-global-state bug between requests seems most relevant. ([Developer](../../../admin/synthetic/developer/index.html))SAPI rows: Apache mod_php, PHP-FPM, php-cgi, FrankenPHP, LiteSpeed (LSAPI), CLI/cron/queue workers. No row and no 'not covered by sources' note for Swoole or RoadRunner.

### What to change
- Add rows for Swoole, RoadRunner and Octane workers to the SAPI table, saying 'not covered by the primary sources' if that is the truth. ([Developer](../../../admin/synthetic/developer/index.html), small)Long-running workers are exactly where the stale-state bug across requests should worry a Laravel team, and silence reads as 'not affected'.

### What works, so do not break it
- Severity is stated with its evidence and its tempering: 9.2 with the full CVSS vector, AC:H and AT:P explained, and the 10.0 figure explicitly marked contradicted. ([CTO](../../../admin/synthetic/cto/index.html))
- The affected and fixed versions table, with the warning that scanners reading the CVE record will call 7.4 to 8.1 unaffected, is directly actionable for my vulnerability management. ([CTO](../../../admin/synthetic/cto/index.html))
- The mitigations table pairs each setting with what it does not do, from the same source; that stops my team over-trusting a php.ini change. ([CTO](../../../admin/synthetic/cto/index.html))
- The blast radius section frames the question as a property of our system, which is the right way to brief my architects on microservices. ([CTO](../../../admin/synthetic/cto/index.html))
- Each CVE gets its GHSA ID, the full CVSS 4.0 vector, CWEs, timestamps and the record's description verbatim, kept apart from what was demonstrated and what the fix does. Exactly how I want a bug described. ([Developer](../../../admin/synthetic/developer/index.html))
- The SAPI table separates mod_php (demonstrated), FPM (disputed between GHSA and the Foundation, shown as such), FrankenPHP, LSAPI and CLI. The FPM disagreement is shown, not smoothed over. ([Developer](../../../admin/synthetic/developer/index.html))
- The warning that CVE records say defaultStatus 'unaffected' and list only 8.2 to 8.5, so scanners will clear 7.4 to 8.1. That is something I would actually have been caught by in CI. ([Developer](../../../admin/synthetic/developer/index.html))
- The mitigations table puts each setting next to its own caveat, including where it must be set (php_admin_value, pool, php.ini) and the RLIMIT_AS warning. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.* ([CTO](../../../admin/synthetic/cto/index.html))This is the most useful single warning on the site for my security team: our scanner dashboard would have lied to us.
- *Remote code execution as the web worker is the floor, not the ceiling, and not yet a breach.* ([CTO](../../../admin/synthetic/cto/index.html))Good line for the board, and the right mental model for blast radius.
- *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.* ([Developer](../../../admin/synthetic/developer/index.html))The most practically valuable sentence on the site for anyone with a scanner in the pipeline.

## [defence/index.html](../../../defence/index.html)

2 of 6 readers: CTO, Security lead

### What does not work
- **low** One Fortinet signature ID looks malformed, and I would paste these straight into a ticket. ([Security lead](../../../admin/synthetic/security/index.html))'Three FortiGuard signatures (090502648, 090502651, 09052654)': the third has eight digits where the other two have nine.

### What to change
- Add a short 'copy into your SIEM' block with the actual Sigma, Falco and ModSecurity rule snippets, or direct links to the specific rule files, beside the host-signal table. ([Security lead](../../../admin/synthetic/security/index.html), medium)The signals are right, but my team still has to go and find the rule text. One click less saves an hour on day two.
- Check the third Fortinet signature ID and either label or remove the £ pill in the header. ([Security lead](../../../admin/synthetic/security/index.html), small)Small things, but I paste IDs into tickets, and unexplained numbers in the chrome erode trust.

### What works, so do not break it
- The process-tree signal (a PHP worker spawning a shell) and the plain statement that nginx default logs cannot answer 'were we hit' tell me what to ask my SRE lead today. ([CTO](../../../admin/synthetic/cto/index.html))
- Host signals are given by layer (access log, PHP error log, kernel, process tree, network), with literal strings such as 'in Unknown on line 0' and 'exit signal Segmentation fault (11)'. My SOC can build alerts from that table. ([Security lead](../../../admin/synthetic/security/index.html))
- The 'What the log cannot show' row and the closing 'So: can it be detected?' section say plainly where telemetry goes blind (nginx default format, no worker id). That is honest and it changes what I ask my team for. ([Security lead](../../../admin/synthetic/security/index.html))
- The WAF table puts each vendor's own caveat next to its rule, including Fortinet shipping alert-only by default and Fastly's rule needing to be enabled. That is operationally useful. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *An organisation whose only telemetry is the access log cannot answer "were we hit" from it* ([CTO](../../../admin/synthetic/cto/index.html))Uncomfortable and useful: this tells me what to say if the board asks whether we were compromised.
- *with the known exploits no application code runs, so a shell from a worker is the exploit* ([Security lead](../../../admin/synthetic/security/index.html))The most actionable sentence on the site. That is a high-fidelity alert with almost no false positives.
- *An organisation whose only telemetry is the access log cannot answer "were we hit" from it* ([Security lead](../../../admin/synthetic/security/index.html))Honest, and exactly the point I need to make to justify EDR coverage on web tiers.

## [glossary/index.html](../../../glossary/index.html)

1 of 6 readers: Designer

### What does not work
- **medium** Page labels contradict each other: the band, the kicker and the highlighted menu item disagree about which part of the site a page belongs to. ([Designer](../../../admin/synthetic/designer/index.html))glossary: band 'ABOUT THIS SITE', kicker 'START HERE', menu highlights 'Start here'. explained: band 'RESEARCH' but kicker 'START HERE'. articles: band 'ABOUT THIS SITE' on the Stories page, while articles itself says 'Every page on the site says at its top which half it belongs to'.

### What to change
- Make the band, kicker and highlighted menu item come from one source, so glossary and explained both say the same section, and the Stories page says STORIES. ([Designer](../../../admin/synthetic/designer/index.html), small)The site promises each page states which half it belongs to; inconsistent labels break that promise visibly.

## [sources/index.html](../../../sources/index.html)

1 of 6 readers: Security lead

### What does not work
- **medium** The banner on every page promises a saved copy behind every fact, but the sources page says the copies are private, so I can cite a hash but not show the captured text to anyone. ([Security lead](../../../admin/synthetic/security/index.html))Banner: 'every fact links to a saved copy of its source'. sources/index.html: 'The captures are third-party pages held privately and are not republished; this page links to the originals'.

### What to change
- Change the banner wording to 'every fact links to its source and a hash of the saved copy', or publish the captured text for public government advisories. ([Security lead](../../../admin/synthetic/security/index.html), small)The promise and the practice should match. Advisories from CISA and the NCSC carry no republication risk and are the ones I would cite.

## [status.json](../../../status.json)

1 of 6 readers: Developer

### What does not work
- **medium** status.json has no machine-readable affected or fixed versions, so a tool cannot use it to gate a build; the versions appear only as prose inside a headline fact. ([Developer](../../../admin/synthetic/developer/index.html))Keys are schema, site, status, version, counts, headline_facts, latest_story, links; the versions appear only in headline_facts[0].text. links has no entry for data/affected.json.

### What to change
- Add a fixed_versions map per branch and an affected_ranges field to status.json, and link data/affected.json from its links block. ([Developer](../../../admin/synthetic/developer/index.html), small)Then a CI step or an LLM tool can gate on the data instead of parsing a prose headline.

## [timeline/index.html](../../../timeline/index.html)

1 of 6 readers: Project manager

### What does not work
- **medium** I cannot tell what changed since yesterday. Every page shows everything as new on my first visit, and the timeline has no 'since' filter or 'last 24 hours' block, so tomorrow I would have to re-read 68 rows. ([Project manager](../../../admin/synthetic/pm/index.html))'on this page 68 new, 0 changed, 0 read; across the site 340 new and 0 changed of 340'; timeline is 8.1 screens.

### What to change
- Add a 'Changed in the last 24 hours' block at the top of the timeline and the PM briefing, listing only rows added or changed since the previous day. ([Project manager](../../../admin/synthetic/pm/index.html), medium)My daily routine is 'what moved since yesterday'; the read-tracking bar does not help on a first visit or on a new device.

## [admin/versions.html](../../../admin/versions.html)

1 of 6 readers: Developer

### What does not work
- **medium** The release notes correct the inventory count to 675, but the pages and llms.txt still say 674, so I do not know which figure to cite. ([Developer](../../../admin/synthetic/developer/index.html))v0.4.3: 'a correction: the inventory had 675 rows at the captured commit, not 674'; patching/index.html still says 'of 674 products in the NCSC-NL inventory at commit cca173c64ec5', and so do affected/index.html and llms.txt.

### Lines readers reacted to
- *a correction: the inventory had 675 rows at the captured commit, not 674* ([Developer](../../../admin/synthetic/developer/index.html))Good that it is corrected, bad that the pages I read still say 674.

## [articles/index.html](../../../articles/index.html)

1 of 6 readers: Designer

### What does not work
- **low** Machine provenance is shown at reader level on story cards and section footers, cluttering cards and contradicting the site's own version. ([Designer](../../../admin/synthetic/designer/index.html))'House · Journalist · 2026-10-22 · claude-journalist · site v0.4.0 · vault commit 200d08971937 · data as of 2026-10-22T11:34Z'; front-page sections say 'This section v1 written in site v0.3.2' while the masthead says v0.4.3.

### What to change
- Move vault commit, agent name and 'written in site vX' lines into the history link, leaving date and author on the card. ([Designer](../../../admin/synthetic/designer/index.html), small)The cards read as build logs; the provenance is good but it is not reader-level information.

### Lines readers reacted to
- *Every page on the site says at its top which half it belongs to.* ([Designer](../../../admin/synthetic/designer/index.html))A good promise that the page itself breaks: this Stories page is labelled ABOUT THIS SITE.

## [llms.txt](../../../llms.txt)

1 of 6 readers: Developer

### What does not work
- **low** Pages that llms.txt does not list are cited as data sources, and the markdown twin's links point back to HTML, so a tool following them leaves the markdown. ([Developer](../../../admin/synthetic/developer/index.html))patching/index.html cites 'data/patching.json' and review/index.html cites 'data/review.json', and neither is in llms.txt's Data list. flaws/index.md links to '../sources/cve-cve-2026-109618/index.html' rather than .md.

### What to change
- List data/patching.json and data/review.json in llms.txt and make the markdown twins link to .md siblings. ([Developer](../../../admin/synthetic/developer/index.html), small)So a tool can walk the site in markdown and JSON without falling back to HTML.

### What works, so do not break it
- llms.txt exists, is well organised and points at a markdown twin for every page plus data/*.json; the flaws markdown twin renders clean pipe tables a tool can parse. ([Developer](../../../admin/synthetic/developer/index.html))

## [questions/index.html](../../../questions/index.html)

1 of 6 readers: Board member

### What does not work
- **low** The Questions page opens with a paragraph about a librarian and an email address before any question, and is 18.6 screens long, mostly a site catalogue I had no use for. ([Board member](../../../admin/synthetic/board/index.html))'Kept by the librarian, librarian@php.newsroom: the catalogue: which page answers which question...'; instruments: 18.6 screens.

### What to change
- Put the questions first and move the librarian paragraph and the page catalogue to the bottom or another page. ([Board member](../../../admin/synthetic/board/index.html), small)The useful short answers are hidden behind an introduction about how the site is run.

### What works, so do not break it
- The Questions page answers 'Should we take our site offline?' and 'We are behind Cloudflare. Are we safe?' in short pasteable paragraphs, which are both questions I expect to hear in the boardroom. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *Safer, not safe.* ([Board member](../../../admin/synthetic/board/index.html))Three words I will use if someone tells me our firewall provider has it covered.

## [start/index.html](../../../start/index.html)

1 of 6 readers: Designer

### What does not work
- **low** Smallest text is just under 12px on six of seven pages. ([Designer](../../../admin/synthetic/designer/index.html))min_font_px 11.84 with 16 blocks below 12px on start; the metadata lines ('This page v4 written in site v0.3.1') are visibly the faintest, smallest text on the page.

### What to change
- Show only the reader's 'Read items' controls after the first page mark, with a one-line hint the first time ('Mark what you have read; we keep it in this browser'). ([Designer](../../../admin/synthetic/designer/index.html), medium)Fade, hide and show mean nothing before a newcomer has read anything.

### What works, so do not break it
- The reader map is a genuine piece of information design: two axes, dot-scale depth markers (one, two, three dots) and coloured initial avatars by role group. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.* ([Designer](../../../admin/synthetic/designer/index.html))A clear instruction for a two-axis chart; the visual delivers on it.

## [sources/cisa-alert-log4j-2021/index.html](../../../sources/cisa-alert-log4j-2021/index.html)

1 of 6 readers: Security lead

### What does not work
- **low** A Log4j 2021 source page is reachable from the evidence list but has no claim or event attached, so it looks like noise in a php2shell evidence trail. A 404 page is also logged as a captured primary source. ([Security lead](../../../admin/synthetic/security/index.html))'No claim cites this source yet.' 'No timeline event cites this source yet.' On sources/index.html: 'Page Not Found | CISA ... primary · CAPTURED ... HTTP 404'.

## [agencies/index.html](../../../agencies/index.html)

1 of 6 readers: Security lead

### What works, so do not break it
- The agency table quotes each body verbatim on the offline question, records the two it could not read, and shows that the BBC's NCSC quote is not on the captured NCSC page. That is the kind of checking I need before I quote an agency upwards. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *The sentence the BBC quotes from the NCSC is not on the NCSC page as captured; its opening matches the Canadian text.* ([Security lead](../../../admin/synthetic/security/index.html))This kind of checking is why I would come back to the site. It saves me from repeating a misquote upwards.

## [briefings/everyone/index.html](../../../briefings/everyone/index.html)

1 of 6 readers: Designer

### What works, so do not break it
- The boxed 'The answer in thirty seconds' panel with the reader's avatar and a single 'Read the site as Alex' button is the clearest hand-hold for a newcomer anywhere on the site. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *You do not need to know anything about computers to follow this.* ([Designer](../../../admin/synthetic/designer/index.html))Lands well, set right under the answer box.

## [briefings/security/index.html](../../../briefings/security/index.html)

1 of 6 readers: Security lead

### What works, so do not break it
- The thirty-second answer and 'What to decide or do' list is a usable runbook skeleton: patch order by SAPI, mitigations recorded as partial, process-tree alerting, a named owner for the offline call. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *Every claim of exploitation so far is of attempts, probes or honeypot hits.* ([Security lead](../../../admin/synthetic/security/index.html))This is the line I will give the CISO. It is careful without being complacent.

## [explained/index.html](../../../explained/index.html)

2 of 6 readers: Board member, Designer

### What works, so do not break it
- The kitchen analogy and the 'What that can reach' list finally made the risk concrete for me: database passwords and other systems that trust the server. ([Board member](../../../admin/synthetic/board/index.html))
- Pill-shaped jump links (letters on the glossary, questions on the explainer) give long pages a visible table of contents in the first screen. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *it does not matter how well a website is written; if PHP underneath it is unpatched, it is in scope.* ([Board member](../../../admin/synthetic/board/index.html))Clear and alarming in the right way: I cannot be told 'our code is fine' as an answer.
- *Taking a site offline is a decision an organisation makes, not evidence it was attacked.* ([Board member](../../../admin/synthetic/board/index.html))Reassuring and worth repeating to colleagues who will see the headlines.
- *Words in the dotted underline are explained when you hover or tap them.* ([Designer](../../../admin/synthetic/designer/index.html))Good, and the dotted underline is consistent everywhere, though the underlined terms are small tap targets on a phone.

## [questions/old-php/index.html](../../../questions/old-php/index.html)

1 of 6 readers: Project manager

### What works, so do not break it
- A short, pasteable answer with a URL for the 'we are on 7.4' question; I can forward it to a client as is. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *To paste back where it was asked: the paragraph above and https://php.oct.2026.newsroom.sgit.ai/questions/old-php/index.html* ([Project manager](../../../admin/synthetic/pm/index.html))Very handy; I can send this to the clients still on 7.4 without rewriting it.

## [review/index.html](../../../review/index.html)

1 of 6 readers: Developer

### What works, so do not break it
- The review page says the code layer comes from git show -U0 by a parser, not a model, and gives per-area added and removed counts. That is a provenance claim I can check. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Never a model, so it cannot invent a function that is not in the diff.* ([Developer](../../../admin/synthetic/developer/index.html))The right provenance claim for a code map, and one I can check against git show.


---
site v0.10.18 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/pages/index.html
