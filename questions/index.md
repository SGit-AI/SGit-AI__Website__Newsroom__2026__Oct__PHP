# Questions readers ask about php2shell

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Can anything be done or do we wait for updates? Has anyone been hacked? Is it really most websites? Short answers to paste back, the sources behind them, and the pages that carry each one.

# Questions readers ask

The questions people ask about php2shell when they see the headline, each with a short answer that can be pasted back where it was asked, the longer answer with its sources, and the pages that carry it. Kept by the librarian, `librarian@php.newsroom`: the catalogue: which page answers which question, the questions readers actually ask, and the articles readers have seen that the vault has not captured yet.

## The questions

| Question | The short answer | Read |
|---|---|---|
| [Can anything be done to fix it, or do we just have to wait for updates?](fix-or-wait/index.html) | The updates already exist: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 were released on 21 October and fix both flaws. Nobody is waiting on PHP; the wait is for whoever runs each server to install them and restart. If that is you, update now; if you cannot today, there are temporary settings and, as a last resort, taking the site offline. If a hosting company runs your site, ask them whether it is patched. | [If you run PHP: the steps, in order, with their sources](../playbook/index.html) [The two flaws: CVE-2026-109618 and CVE-2026-109619](../flaws/index.html#mitigations) [Detection and defence: what blocks php2shell and what shows it](../defence/index.html) |
| [Is PHP really the software behind most websites?](most-websites/index.html) | Roughly, if you count websites, not the Internet. About 69% of the websites whose server-side language can be identified run PHP, and the share is falling; on every site the HTTP Archive crawls, PHP is detected on about half (the fact-check desk's investigation). Wiz's '70% of the Internet' is that website figure restated: nobody measures a share of 'the Internet'. Internet-facing PHP hosts number in the low millions: VulnCheck counts about 2.6 million, and Censys counted 1.57 million unpatched on 21 October among the 1.58 million whose version it could read. | [The numbers: 70%, 30 million, 2.6 million, 6,000, 674](../numbers/index.html) [Every claim, with its status and sources](../claims/index.html#scale-70pc-internet) [Affected systems: versions, deployments, applications, inventory](../affected/index.html) |
| [Has anyone actually been hacked?](been-hacked/index.html) | Not that any named organisation has said, as of 16:04 UTC on 23 October, the latest capture in the evidence vault. Attack attempts are real and in the millions at Cloudflare alone, Amazon saw one on a honeypot four days before disclosure, and two security vendors are reported as saying it is being exploited, without naming any victim (other reports of the same vendors describe attempts). CISA had not added it to its exploited-vulnerabilities list when last checked, and the sites that went offline say they did it as a precaution. | [Exploitation signals, in order](../exploitation/index.html) [Impact: taken offline versus compromised](../impact/index.html) [Every claim, with its status and sources](../claims/index.html#no-confirmed-compromise) |
| [Do I need to change my passwords?](passwords/index.html) | Not because of this, as things stand. The flaw is on web servers, not on your devices, and no named site has announced a breach through it, as of the latest check. If a site you use announces one, follow its instructions. Using a different password on every site is the protection that holds whatever the next flaw is. | [The two flaws: CVE-2026-109618 and CVE-2026-109619](../flaws/index.html#blast) [Impact: taken offline versus compromised](../impact/index.html) [Briefing for a media and communications team: What can we say that is true, what should we not say, and what will we be asked?](../briefings/comms/index.html) |
| [How do I know whether my site is affected?](am-i-affected/index.html) | If the site runs on PHP (WordPress, Drupal, Joomla, Magento, MediaWiki, and Laravel all do) and the running PHP version is older than 8.5.12, 8.4.27, 8.3.36 or 8.2.35 without a distribution backport, it is affected. Check the version where the code runs, after the restart, not the package list. For bought-in products, the Dutch NCSC keeps an inventory of 674 products and their status. | [Affected systems: versions, deployments, applications, inventory](../affected/index.html) [The NCSC-NL inventory: 674 products](../affected/software.html) [If you run PHP: the steps, in order, with their sources](../playbook/index.html) |
| [Should we take our site offline?](take-offline/index.html) | Only if you cannot patch or apply the temporary mitigations in time. That is the advice from the NSA, CISA and the UK NCSC, and it is the last step on every agency's list. If the site is patched and the workers restarted, the advice is to keep it up and watch it. | [If you run PHP: the steps, in order, with their sources](../playbook/index.html) [What sixteen agencies actually advise](../agencies/index.html) [Impact: taken offline versus compromised](../impact/index.html) |
| [Why is this such big news?](why-big-news/index.html) | Four things at once: the flaws are in PHP itself, which runs a large share of the web; they were found with AI help; the coordinated disclosure leaked a day early, so the fix shipped under pressure; and the NSA, CISA and NCSC told organisations that could not patch to take systems offline, which is why government, council and police sites went dark. | [PHP in October 2026: two critical security flaws, tracked as evidence](../index.html) [Who found php2shell, and what the AI did](../discovery/index.html) [How the coordinated disclosure broke](../leak/index.html) |
| [We are on PHP 7.4, 8.0 or 8.1. Is there a patch?](old-php/index.html) | Not a release. PHP 8.1 and older are out of support; the project published source backport branches for 7.4, 8.0 and 8.1, which someone has to build. CISA says systems on 8.1 or older should be taken offline. Plan the migration to 8.2 or later now; in the meantime a distribution or vendor that backports, the temporary mitigations and isolation are the options. | [The two flaws: CVE-2026-109618 and CVE-2026-109619](../flaws/index.html#versions) [If you run PHP: the steps, in order, with their sources](../playbook/index.html) [Briefing for a CTO: What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?](../briefings/cto/index.html) |
| [We are behind Cloudflare (or another firewall). Are we safe?](waf-enough/index.html) | Safer, not safe. Cloudflare's rules were live about nine hours before disclosure, on every plan including Free, and Akamai, Fastly, Imperva and Fortinet followed. Every one of them calls it a stopgap and says patch anyway: attackers mutate payloads, and the rules only see traffic that goes through the firewall. | [Detection and defence: what blocks php2shell and what shows it](../defence/index.html) [Every claim, with its status and sources](../claims/index.html#waf) |
| [Do our developers need to change our code?](change-code/index.html) | No. Both bugs are in the C engine that runs PHP, not in PHP code, and the demonstrated attack runs before any application code. The fix is updating the PHP runtime and restarting it. What developers can do is check the version on the machines they deploy to and rebuild container images. | [Briefing for a developer: Is my code the problem, what do I change, and how do I check the box I deployed to?](../briefings/developer/index.html) [The code: where php2shell lives and what the fix does](../code/index.html) [The fix, mapped to the code](../review/index.html) |

## Seen by readers, not yet in the vault

| Seen | What | State | Answered by |
|---|---|---|---|
| 2026-10-22, shared in a group chat | **The Times**: [Race to fix PHP security issue in software behind most websites](https://www.thetimes.com/article/624a88e5-8d6b-43fc-af01-a1988c7ea9d9)Hackers could seize control of online stores and steal passwords after the discovery of a critical vulnerability in programming | not captured: paywalled, and a reader's share link is personal, so the token was dropped from the URL. Queued for the researcher and vendor collector. | [Can anything be done to fix it, or do we just have to wait for updates?](fix-or-wait/index.html) [Is PHP really the software behind most websites?](most-websites/index.html) [Has anyone actually been hacked?](been-hacked/index.html) [Do I need to change my passwords?](passwords/index.html) [Why is this such big news?](why-big-news/index.html) |

An article a reader has seen is listed here until a collector captures it into the evidence vault. Until then it is not cited anywhere on this site; the answers above rest on what is captured.

## The catalogue: every page, and what it answers

### Updates
- [Every update, newest first](../updates/index.html):
- [Daily: 22 Oct 20:03 UTC](../updates/2026-10-22T2003Z/index.html):
- [How an update is written](../updates/readme/index.html):

### Start here
- [Who is reading? The readers of this site, mapped](../start/index.html): 16 kinds of reader, from someone who has never heard of PHP to the people who maintain it, mapped by what they need to do and how technical they want it, each with a thirty-second answer and a reading path.
- [Operations: what changed, what to do next, how sure we are](../ops/index.html): The home for people who patch and defend: the next three actions, everything that changed newest first with what you have read marked, and the state of the evidence as charts: facts by status, events per day, exploitation signals, fixed versions.
- [Analysis: how sure we are, and where the sources disagree](../analysis/index.html): The home for people who weigh the evidence: every fact by status and topic, the numbers in the news with how far each holds, where governments disagree, and what is still contested, each linked to its saved sources.
- [The PHP security flaws, explained from the start](../explained/index.html): No technical background assumed: what PHP is, what went wrong, why it is called php2shell, what the CVE numbers mean, why websites went offline, whether anyone was hacked, and what to do now.
- [Glossary: every php2shell term in plain English](../glossary/index.html): 40 terms from the php2shell story (PHP, CVE, CVSS, remote code execution, WAF, KEV and more), each explained in plain English, in the sense it has in this story.

### Briefings
- [Briefing for a curious reader: What happened, does it affect me, and should I worry?](../briefings/everyone/index.html): The php2shell story for a curious reader: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a website owner: My website runs on WordPress or similar: am I affected, and what do I ask my host?](../briefings/site-owner/index.html): The php2shell story for a website owner: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a project or programme manager: What unplanned work does this create, who do I chase, and what do I tell stakeholders?](../briefings/pm/index.html): The php2shell story for a project or programme manager: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a board member or executive: Are we exposed, what is it costing us, and who owns the decision to pull a system?](../briefings/board/index.html): The php2shell story for a board member or executive: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a security lead: What do I patch first, what do I watch for, and when do I take something offline?](../briefings/security/index.html): The php2shell story for a security lead: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a PHP or platform engineer: Which versions, which SAPIs, which settings, which commands?](../briefings/engineer/index.html): The php2shell story for a PHP or platform engineer: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a journalist: Which numbers hold up, who said what first, and what is still unverified?](../briefings/journalist/index.html): The php2shell story for a journalist: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a security researcher: What are the bug classes, what was demonstrated, and what is still open?](../briefings/researcher/index.html): The php2shell story for a security researcher: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for an analyst or advisor: How did coordinated disclosure fail, and what does AI-assisted discovery change?](../briefings/analyst/index.html): The php2shell story for an analyst or advisor: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a CISO: What is our exposure, what is our evidence we were not hit, and what do I tell the board?](../briefings/ciso/index.html): The php2shell story for a CISO: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a CTO: What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?](../briefings/cto/index.html): The php2shell story for a CTO: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a CFO: What is the financial exposure, what does downtime cost against breach cost, and will insurance respond?](../briefings/cfo/index.html): The php2shell story for a CFO: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a data protection officer: Was personal data exposed, does this start a GDPR breach assessment or a 72-hour notification, and what do I document?](../briefings/dpo/index.html): The php2shell story for a data protection officer: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a head of AppSec: Which of our applications are in scope, which settings matter, and what do we add to the pipeline?](../briefings/appsec/index.html): The php2shell story for a head of AppSec: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a developer: Is my code the problem, what do I change, and how do I check the box I deployed to?](../briefings/developer/index.html): The php2shell story for a developer: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.
- [Briefing for a media and communications team: What can we say that is true, what should we not say, and what will we be asked?](../briefings/comms/index.html): The php2shell story for a media and communications team: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.

### Yours
- [Power users: start here](../collaborators/index.html): Where a power user of PHP October 2026 starts: the first fifteen minutes, the latest ask (what is new, what to do, the questions), the messages for the email list and the WhatsApp group, a form to join and a form for feedback, both encrypted in your browser.
- [Join: a key for this device, in one tap](../join/index.html): Open the invitation the editor sent you and this page makes a key on your device, so the feedback you send from any page is signed as yours; the enrolled keys, as handles and fingerprints.
- [Feedback from collaborators](../feedback/index.html):
- [Invite someone: a link and a QR code, signed on this device](../join/invite/index.html): For the editor: make an invitation to give signed feedback on this site, as a QR code, a link and a share button, signed in the browser with an enrolled key.
- [Now: the phone app](../now/index.html):
- [Your desk: what is new to you, and what changed](../you/index.html): What is new to you on this site and what changed since you read it, by part of the site; what you put aside; your notes; all kept in your browser, exportable.
- [Your stack: what php2shell can reach in it](../stack/index.html): Describe what you run, the internet, the edge, the applications, the PHP and where it comes from, and what each can reach; see which runtimes the two flaws affect, the blast radius, what to do first and what on this site is about your stack. In your browser and your own vault.
- [The feed viewer: this site, the records, and your own feeds](../reader/index.html): Read this site's feeds, the CVE records, NVD, OSV, CISA KEV, GitHub, Wikipedia, Hacker News and Mastodon, and any feed you add, in your browser, with what you have read marked and only what is new shown next time.
- [Feeds: what is new and what changed](../feeds/index.html): RSS feeds for everything new and changed on this site and for each of its parts: an entry for every new item and every change, and where to read them.
- [Subscribe: what changed, sent to you](../subscribe/index.html): Follow the PHP flaws story by email: everything or one part of the site, as it changes or as a digest; the address encrypted in your browser and confirmed before anything is sent.

### The incident
- [PHP in October 2026: two critical security flaws, tracked as evidence](../index.html): PHP news for October 2026, led by the month's big story: two critical security flaws in PHP (CVE-2026-109618 and CVE-2026-109619, nicknamed php2shell). The current situation in plain words, the core facts with their evidence, what to do, and a briefing for every kind of reader.
- [What's new: every change, release by release](../whatsnew/index.html): What changed on this site in each release: new facts, facts whose status changed, the briefings that moved for each reader and the sections that were rewritten.
- [The specialist summary: CVE-2026-109618 and CVE-2026-109619](../summary/index.html): The technical summary of the two PHP flaws of October 2026: what is established with its sources, the six scale figures, the open questions and the last 48 hours.
- [The two flaws: CVE-2026-109618 and CVE-2026-109619](../flaws/index.html): What the CVE records, the GitHub advisories and the PHP security team say about php2shell: the bug classes, what was demonstrated, which deployments, which versions, the fix and the temporary mitigations, with the blast-radius questions.
- [The code: where php2shell lives and what the fix does](../code/index.html): Read from a clone of php/php-src: the fix commit (389 files, authored 18 October, public 21 October 14:06 UTC), the engine mechanism it replaces, the hunks that matter, and the end-of-life backport.
- [The timeline, 2024 to the latest capture](../timeline/index.html): 68 dated events in the php2shell story, from the 2024 audit through discovery, coordinated disclosure, the leak, the release and the response, every one tied to a captured source.
- [Who found php2shell, and what the AI did](../discovery/index.html): Calif, OpenAI and Wiz each claim the discovery of php2shell; their own timelines side by side, the 2024 audit that saw it first, the credits on the advisories, and what the sources do and do not say about the models.
- [How the coordinated disclosure broke](../leak/index.html): Hour by hour from the first circulation of the CVE IDs on 20 October to the release on 21 October: the pre-announcement, the deleted video, the early WAF rules, the embargo break, the first attempts, and the three accounts that disagree on what leaked.
- [Exploitation signals, in order](../exploitation/index.html): Every signal of php2shell exploitation in the captured sources, from an Amazon honeypot hit on 17 October to the KEV catalog, with what exploitation would look like on a host.
- [No named organisation has said it was compromised through php2shell: the evidence](../compromise/index.html): The evidence behind one statement, as of 2026-10-23 16:04 UTC: attempts, vendor reports, statements that no success is known, named organisations, allegations and official lists, each with its source.
- [The fix, mapped to the code](../review/index.html): The php2shell fix as layered graphs: the two flaws, the design of the patch, and the php-src files and functions it changed, derived from the diff.
- [Walk the graph: the fix and the code](../review/ui/index.html): A navigator over the php2shell review graph: the fix, the flaws it closes, and the files and functions it changed, each a link.
- [Impact: taken offline versus compromised](../impact/index.html): Two ledgers for php2shell: every system reported taken offline with who said so, and every claim of compromise with its basis. As of the latest capture, no named organisation has confirmed a compromise.
- [Detection and defence: what blocks php2shell and what shows it](../defence/index.html): What Cloudflare, Akamai, Fastly, Imperva, AWS and Fortinet deployed and what each says it cannot do; the community Suricata, Sigma, Falco and ModSecurity rules; the host signals; and how hard the exploit is according to the vendors who tried.
- [In context: php2shell against Kaminsky, Heartbleed, Shellshock, Log4Shell and the last PHP RCE](../context/index.html): Ten landmark vulnerabilities with their CVE records and KEV rows, the KEV catalog counted, and what the comparison says about severity, exposure, urgency and the discovery pipeline.
- [If you run PHP: the steps, in order, with their sources](../playbook/index.html): Inventory, patch, mitigate, shield, isolate or take offline, look for compromise, verify: every agency's php2shell advice merged into one ordered list with the sentence each step comes from.
- [Patching: who gets a fix](../patching/index.html):
- [The inventory, hour by hour](../patching/inventory/index.html):
- [The second stories: signals](../signals/index.html):

### The analysis
- [Every claim, with its status and sources](../claims/index.html): 70 claims about php2shell, each with who makes it, a status (confirmed, reported, disputed, contradicted or unverified) and the captured sources behind it.
- [Claims waiting for review](../claims/review/index.html): 86 claims from the evidence vault that are not in the site claim table yet, each with the agent that recorded it, its sources, and the journalist's verdict or "not yet reviewed".
- [Fact-check: how sure we are](../factcheck/index.html):
- [Corrections we have asked for](../outreach/index.html):
- [The numbers: 70%, 30 million, 2.6 million, 6,000, 674](../numbers/index.html): Every scale figure in circulation about php2shell, with what it measures, who said it, whether anyone checked it, and why they differ by four orders of magnitude.
- [What sixteen agencies actually advise](../agencies/index.html): The NSA, CISA, the UK NCSC, CERT-EU, ENISA, CERT-FR, Canada, Australia, New Zealand, the Netherlands, Italy, Switzerland, Latvia, Japan, Spain and Portugal on php2shell: who says take it offline, who says isolate, who says patch and nothing more, and who has seen exploitation.
- [Affected systems: versions, deployments, applications, inventory](../affected/index.html): Which PHP versions and SAPIs php2shell affects, which applications had RCE demonstrated, and the NCSC-NL inventory of 674 products counted by status.
- [Who says what: every party and its claims](../actors/index.html): 27 parties in the php2shell story, each with the claims this site attributes to it and the sources behind them.
- [The story as a graph: who states what, who relays it, and what it rests on](../graph/index.html): 1049 nodes and 1527 typed edges: every claim, number, event, signal, advice, party, source and capture on the PHP flaws story, walkable, with the independent origins of each claim.
- [Every party on the story: who states, who relays, who publishes](../graph/parties/index.html): 243 parties resolved from 249 spellings, with the claims each one states and passes on.
- [From a line of code to a stakeholder: the fractal graph](../fractal/index.html): One graph for php2shell: 359 changed lines of php-src, up through functions, files, the fix and the flaws, the claims and sources, the story arcs and the risks, to the fifteen kinds of reader who face them.
- [Walk the whole graph: stakeholders to lines of code](../fractal/ui/index.html): A navigator over the php2shell fractal graph: stakeholders, risks, story arcs, claims, sources, the flaws, the fix, files, functions and changed lines, each node a link.
- [From outside: other models and sites](../readings/index.html):
- [Perplexity's notes, in full](../readings/perplexity-2026-10-22/index.html):

### The evidence
- [Every source: 295 pages, 290 captures, 1761 hashes](../sources/index.html): The manifest of the php2shell evidence vault: every captured source with its publisher, kind, publication time, capture times, HTTP status and the SHA-256 of every captured file.
- [The NCSC-NL inventory: 674 products](../affected/software.html): Every row of the NCSC-NL php2shell software inventory at commit cca173c64ec5, with its status per CVE.
- [The evidence vault, opened](../admin/vault/index.html): The read key to the evidence vault behind this site, the link that opens it in the browser, and what is in it.
- [Evidence, derived, authored](../layers/index.html):
- [The fact pipeline: from a web page to a reader](../pipeline/index.html): How a source becomes a fact and a fact reaches a reader on this site: found, saved, read, cited, given a status, built into versioned sections and selected per reader, with counts at every stage and the facts by status in every release.
- [How the story changed, release by release](../versions/index.html): Every section of the site, every reader's briefing and every fact, versioned across every release: what changed, when, and in which release.
- [The vaults behind this site](../vaults/index.html): Every vault this site is built from: the evidence vault and the source watch, both public with their read keys, and the private telemetry vault with its write-only lane; what each holds, who writes to it and how to open it.
- [The evidence vault, opened](../admin/vault/index.html): The read key to the evidence vault behind this site, the link that opens it in the browser, and what is in it.
- [Pack mode, measured on the source watch](../admin/pack-mode/index.html): One vault as a normal sgit vault and as a pack vault: a fresh clone in 95 s against 13 min 47 s, the whole history pushed in 96 s, and why the normal vault has hit a wall.
- [The source watch: every outside source on php2shell, watched and snapshotted](../vaults/source-watch/index.html): The public source-watch vault: 913 pages from 597 publishers in 59 countries, re-read on a schedule, a snapshot kept on every change and every snapshot a graph. Its read key, the vault embedded, and what is in it.
- [Who reads this site: anonymous telemetry over an append lane](../admin/telemetry/index.html): What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.
- [Who reads this site: anonymous telemetry over an append lane](../admin/telemetry/index.html): What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.
- [Subscribe: what changed, sent to you](../subscribe/index.html): Follow the PHP flaws story by email: everything or one part of the site, as it changes or as a digest; the address encrypted in your browser and confirmed before anything is sent.
- [The vaults behind this site](../vaults/index.html#coverage):
- [How the team talks: three vaults and one run](../team/channels/index.html#conductor):
- [How the team talks: three vaults and one run](../team/channels/index.html#issues):
- [How the team talks: three vaults and one run](../team/channels/index.html#mail):
- [Who reads this site: anonymous telemetry over an append lane](../admin/telemetry/index.html): What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.
- [Who reads this site: anonymous telemetry over an append lane](../admin/telemetry/index.html): What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.
- [Power users: start here](../collaborators/index.html): Where a power user of PHP October 2026 starts: the first fifteen minutes, the latest ask (what is new, what to do, the questions), the messages for the email list and the WhatsApp group, a form to join and a form for feedback, both encrypted in your browser.
- [Schedule: every agent that runs on its own](../team/schedule/index.html): Every scheduled agent on one day, its objective, its instructions, every run and the messages between agents, built from the repository.

### GRC
- [GRC: risks, owners, standards](../grc/index.html):
- [The risk register](../grc/risks/index.html):
- [Stakeholders and their registers](../grc/stakeholders/index.html):
- [Frameworks: GDPR, NIS2, CRA, ISO, NIST](../grc/frameworks/index.html):
- [The risk graph](../grc/graph/index.html):
- [Explore the graph: from any node](../grc/explore/index.html):
- [What the graph is missing](../grc/gaps/index.html):
- [From the sgit network](../grc/network/index.html):

### Views
- [Views: the journalist's reading](../views/index.html):
- [The state of affairs, now](../views/state/index.html):
- [Every version, and what changed](../views/state/history/index.html):
- [The journalist's desk: what is still stale](../views/desk/index.html):

### Stories
- [All stories, written here](../articles/index.html):
- [House · Journalist: What changed in a day](../articles/what-changed-in-a-day/index.html):
- [House · Dev desk: Who reads this site, and what works on it](../articles/the-telemetry-tools/index.html):
- [House · Dev desk: The risk graph, before and after](../articles/the-risk-graph-before-and-after/index.html):
- [House · Journalist: Why can't every version of PHP just be patched](../articles/why-not-patch-every-version/index.html):
- [House · Journalist: Where php2shell stands](../articles/where-php2shell-stands/index.html):
- [House · Journalist and historian: Exposed is not exploited](../articles/exposed-is-not-exploited/index.html):
- [House · Historian: php2shell in perspective](../articles/php2shell-in-perspective/index.html):
- [House · Cyber desk: Patch at the speed of Metasploit](../articles/patch-at-the-speed-of-metasploit/index.html):
- [The editor, interviewed: Dinis Cruz on why this site exists](../interview/index.html): Dinis Cruz, the editor of PHP October 2026, on why he started tracking the PHP flaws, the 70% figure, what remote code execution does and does not mean, pulling the plug, and why every section of the site is versioned. In his own words.

### About
- [The method: capture, hash, claim, build, gate](../method/index.html): How this site keeps evidence: the private vault and its protocol, the five status words, the deterministic build, the gate, and how an agent adds a source or replicates the whole thing for the next incident.
- [Design: the redesign, in mockups](../admin/design/index.html):
- [The team: the people, the agents and how they work together](../team/index.html): Every member of the team that runs this site, 2 people and 19 agents and roles, with a page each: role, what they own, their tasks and what they shipped; how a run works, the pipeline and the 16 audiences.
- [The billing model: what runs and what is designed](../billing/index.html): How this site is paid for: the reading meter that runs (pence per page, kept in your browser, never blocking), the provenance pricing that is designed (per claim, with a share for the fact creator), and a counted model of what the story cost to assemble.
- [Your reading account](../account/index.html): The balance, history and receipts of your reading on this site, kept in your browser.
- [The brief: a written request and two voice memos](../brief/index.html): The brief this site was built from, published in full: the editor's written request and two transcribed voice memos on mapping the PHP vulnerability as evidence.
- [Corrections](../corrections/index.html): Where the brief or a page of this site was wrong, what was found and what was done instead.
- [Release history](../admin/versions.html): Every release of this site, with what changed, why, and the vault commit it was built from.
- [The pipeline: what is live, what is deploying](../status/index.html): Each newsroom site's deploy runs, read in your browser from GitHub's public API with no credential, beside the version the site serves now: what is live, what is deploying, what was superseded, what failed.
- [Admin and engineering](../admin/index.html): How this site is built, the checks in its gate, where things are, the reality file and the honest column.
- [How to work on this site: guidance for every agent](../admin/agents/index.html): Push to your own branch early and often and let dev@php.newsroom carry it into dev; quality from coding.sgit.ai, non-functional requirements from nfrs.sgit.ai, and the security requirements.
- [The graph component: one way to draw every graph on this site](../graph/component/index.html): sg-graph, the web component every agent uses to put a graph on a page: the views, the data contract, the build helper, and the hashes of its files.
- [status.json: the feed for other sites](../admin/status-json/index.html):
- [The board](../admin/board/index.html): The work on this site and its vault, as rows: what is open, who owns it, what shipped it.
- [Roles and responsibilities](../admin/roles/index.html): The roles on this site and its vault, who fills each, what it owns and the rules it enforces; how a new agent joins.
- [Briefs](../admin/briefs/index.html): The build briefs for this site, published in full before the work, newest first.
- [Pack mode, measured on the source watch](../admin/pack-mode/index.html): One vault as a normal sgit vault and as a pack vault: a fresh clone in 95 s against 13 min 47 s, the whole history pushed in 96 s, and why the normal vault has hit a wall.
- [Who reads this site: anonymous telemetry over an append lane](../admin/telemetry/index.html): What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.
- [Synthetic readers: six test readers who read the live site](../admin/synthetic/index.html): A board member, a CTO, a project manager, a security lead, a developer and a designer read the live site in a real browser and say what works, what does not and what to change; every review is published here and every run is kept in that reader's own vault.
- [Every member: who owns what](../admin/agents/roles/index.html):
- [Every round: what each member did](../admin/agents/rounds/index.html):

### Elsewhere
- [What else is going on: Pulse](../pulse/index.html):

Every page also has a markdown twin, listed in [llms.txt](../llms.txt); the questions themselves are [data/questions.json](../data/questions.json).

## Asking a new question

Answer a question with a page, not a paragraph. If no page answers it, the answer is written here with its sources, and the gap goes to the editor. A question that is asked twice gets a page. The librarian's role, rules and the mistake behind them are on [the team page](../team/index.html#librarian).


---
site v0.14.10 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/questions/index.html
