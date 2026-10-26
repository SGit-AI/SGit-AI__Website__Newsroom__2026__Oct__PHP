# Who is reading? The readers of this site, mapped

> About this site: how the site works, kept by the agents that run it.

16 kinds of reader, from someone who has never heard of PHP to the people who maintain it, mapped by what they need to do and how technical they want it, each with a thirty-second answer and a reading path.

Start here

# Who is reading? The site's readers, mapped

A story like this one is read by people who have never heard of PHP and by people who maintain it. A page written for one of them fails the other. So before anything else, this site names its readers: 16 of them, by what they need to do and how much technical language they can take. Every reader gets a briefing that opens with a thirty-second answer, and a reading path through the rest of the site.

## The map

Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.
Plain EnglishNo technical background assumed. Every term is explained on first use.Some technicalComfortable with the idea of servers, versions and patches; does not need the internals.Deeply technicalWants versions, settings, code paths and the primary records verbatim.I want to understand itYou heard about this on the news or from a colleague and want to know what it is and whether it touches you.AAlexCurious readerPlain EnglishCCaseyWebsite ownerPlain EnglishI make the decisionsYou own a budget, a plan or a risk, and need what to decide, in what order, and what to ask your team.JJordanBoard member or executivePlain EnglishTTaylorProject or programme managerPlain EnglishQQuinnCFOPlain EnglishMMorganData protection officerSome technicalRRobinCISOSome technicalAAveryCTOSome technicalI tell othersYou write or speak about this, and need what is true, what is not, and who said it first.RRileyCommunications teamPlain EnglishRRowanJournalistSome technicalI run or build systemsYou patch, configure, monitor or write code, and need versions, settings and signals.SSamSecurity leadSome technicalLLeeDeveloperSome technicalJJamieHead of AppSecDeeply technicalDDrewPHP or platform engineerDeeply technicalI study itYou research vulnerabilities or advise on policy, and need the evidence, the open questions and the precedent.BBlakeAnalyst or policy advisorSome technicalAAshSecurity researcherDeeply technical

## How the site changes once you pick

- **A briefing written for you.** The thirty-second answer first, then what to decide or do, then the evidence. For plain-English readers the evidence is folded away until asked for.

- **A reading path that follows you.** Choose *read as* and a bar under the menu shows where you are on your path, what you have read and what to read next, on every page. It is kept in this browser only; nothing is sent anywhere.

- **Every term explained where it appears.** The first use of each specialist word on a page is underlined; hover or tap it for a one-line definition, or follow it to [the glossary](../glossary/index.html). Every CVE number links to what it is.

- **A plain-English line at the top of every technical page**, so a reader who lands on the code or the inventory knows in one sentence what it is and whether they need it.

- **The same evidence for everyone.** No briefing adds a claim. Each selects and orders the same rows, with the same status words and sources, so two readers can disagree about what to do and not about what happened.

## The readers, one by one

A
### Alex, curious reader

I want to understand it · ******Plain English

**Who.** Saw the headlines (websites offline, governments warning) and wants to know what happened and whether to worry.

**Their question.** *What happened, does it affect me, and should I worry?*

#### Needs
- what PHP is, in one sentence
- whether their own phone or laptop is at risk
- why websites went offline
- whether anyone was actually hacked

#### Can skip
- version numbers
- server settings
- the code

The answer in thirty seconds

Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. As of 16:05 UTC on 24 October, the latest capture in the evidence vault, no named organisation has said it was compromised through php2shell.

#### Reading path
- [Your briefing](../briefings/everyone/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [The numbers](../numbers/index.html) 2 min

About 14 minutes in all. Choose *read as Alex* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[php2shell](../glossary/index.html#php2shell)[Evidence vault](../glossary/index.html#vault)[Primary source](../glossary/index.html#primary)[Web server](../glossary/index.html#web-server)[Exploit, exploitation](../glossary/index.html#exploit)[Remote code execution (RCE)](../glossary/index.html#rce)[Honeypot](../glossary/index.html#honeypot)[NCSC](../glossary/index.html#ncsc)[Patch](../glossary/index.html#patch)

[Read as Alex →](../briefings/everyone/index.html)

C
### Casey, website owner

I want to understand it · ******Plain English

**Who.** Runs a small business, charity or club website (often WordPress) on a hosting plan, and is not a developer.

**Their question.** *My website runs on WordPress or similar: am I affected, and what do I ask my host?*

#### Needs
- am I affected
- is it my job or my host's
- exactly what to ask the host
- whether updating WordPress plugins helps

#### Can skip
- the code
- the disclosure politics
- the agency comparison

The answer in thirty seconds

If your website runs on WordPress, Drupal, Joomla or anything else written in PHP, it is in scope: the flaw is in PHP itself, underneath your site. Updating plugins does not fix it. If someone hosts the site for you, ask them in writing whether PHP has been updated to a fixed version and restarted. If you run the server yourself, update PHP today.

#### Reading path
- [Your briefing](../briefings/site-owner/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [If you run PHP](../playbook/index.html) 3 min
- [Affected systems](../affected/index.html) 1 min

About 14 minutes in all. Choose *read as Casey* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Primary source](../glossary/index.html#primary)[CVSS](../glossary/index.html#cvss)[Vulnerability](../glossary/index.html#vulnerability)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[Remote code execution (RCE)](../glossary/index.html#rce)[mod_php](../glossary/index.html#mod-php)[Out of memory (OOM)](../glossary/index.html#oom)[longjmp](../glossary/index.html#longjmp)[CVE](../glossary/index.html#cve)

[Read as Casey →](../briefings/site-owner/index.html)

J
### Jordan, board member or executive

I make the decisions · ******Plain English

**Who.** Sits on a board or leadership team; will be asked whether the organisation is exposed and must not repeat a wrong number.

**Their question.** *Are we exposed, what is it costing us, and who owns the decision to pull a system?*

#### Needs
- are we exposed
- who owns the decision to take a system offline
- what to ask the CISO
- which headline figures not to use

#### Can skip
- SAPIs and settings
- the C code
- the leak forensics

The answer in thirty seconds

A critical flaw in software that runs many websites, fixed on 21 October. Every agency says update first; some say take systems offline if you cannot. As of 16:05 UTC on 24 October, the latest capture in the evidence vault, no named organisation has said it was broken into through this flaw, though attempts are widespread. Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast.

#### Reading path
- [Your briefing](../briefings/board/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [The agencies](../agencies/index.html) 3 min
- [If you run PHP](../playbook/index.html) 3 min

About 18 minutes in all. Choose *read as Jordan* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Evidence vault](../glossary/index.html#vault)[Patch](../glossary/index.html#patch)[Exploit, exploitation](../glossary/index.html#exploit)[SAPI](../glossary/index.html#sapi)[Primary source](../glossary/index.html#primary)[CVE](../glossary/index.html#cve)[KEV](../glossary/index.html#kev)[CISA](../glossary/index.html#cisa)[NCSC](../glossary/index.html#ncsc)

[Read as Jordan →](../briefings/board/index.html)

T
### Taylor, project or programme manager

I make the decisions · ******Plain English

**Who.** Runs a delivery plan that depends on websites or web apps, and needs to know what this does to the schedule.

**Their question.** *What unplanned work does this create, who do I chase, and what do I tell stakeholders?*

#### Needs
- what unplanned work this creates
- which systems and owners to chase
- what to tell stakeholders about downtime
- what changes after the fix

#### Can skip
- the code
- the bug classes
- the detection rules

The answer in thirty seconds

Expect unplanned work this week: updating PHP on every system that uses it, restarting, and re-testing. Some teams may take systems offline for hours as a precaution. Anything still on PHP 8.1 or older has no ready-made fix and becomes a migration project. Ask each system owner for a patch date and a test plan.

#### Reading path
- [Your briefing](../briefings/pm/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [If you run PHP](../playbook/index.html) 3 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [Timeline](../timeline/index.html) 1 min

About 16 minutes in all. Choose *read as Taylor* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Patch](../glossary/index.html#patch)[Primary source](../glossary/index.html#primary)[NSA](../glossary/index.html#nsa)[CISA](../glossary/index.html#cisa)[NCSC](../glossary/index.html#ncsc)[Web server](../glossary/index.html#web-server)[php2shell](../glossary/index.html#php2shell)[Exploit, exploitation](../glossary/index.html#exploit)[Remote code execution (RCE)](../glossary/index.html#rce)

[Read as Taylor →](../briefings/pm/index.html)

Q
### Quinn, cfo

I make the decisions · ******Plain English

**Who.** Owns the money: the cost of downtime, the cost of a breach, and whether insurance responds.

**Their question.** *What is the financial exposure, what does downtime cost against breach cost, and will insurance respond?*

#### Needs
- cost of acting against cost of not acting
- whether a precautionary shutdown is covered
- which figures are safe in a forecast

#### Can skip
- versions and settings
- the code

The answer in thirty seconds

The documented cost so far is precaution, not breach: hours to a day of downtime for organisations that pulled sites, and engineering time to update. As of 16:05 UTC on 24 October, the latest capture in the evidence vault, no named organisation has said it was compromised through this flaw. Ask your broker now, in writing, whether a precautionary shutdown with no breach is covered. Do not use 70% of the Internet in any forecast.

#### Reading path
- [Your briefing](../briefings/cfo/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [The numbers](../numbers/index.html) 2 min
- [In context: 2008 to 2026](../context/index.html) 3 min

About 17 minutes in all. Choose *read as Quinn* and the bar under the menu keeps your place on every page.

#### Words they will meet

[Evidence vault](../glossary/index.html#vault)[Patch](../glossary/index.html#patch)[Unauthenticated](../glossary/index.html#unauthenticated)[Primary source](../glossary/index.html#primary)[Web server](../glossary/index.html#web-server)[php2shell](../glossary/index.html#php2shell)[Exploit, exploitation](../glossary/index.html#exploit)[PHP](../glossary/index.html#php)[Remote code execution (RCE)](../glossary/index.html#rce)[Honeypot](../glossary/index.html#honeypot)

[Read as Quinn →](../briefings/cfo/index.html)

M
### Morgan, data protection officer

I make the decisions · ******Some technical

**Who.** Advises the controller on GDPR; decides with it whether an incident is a personal data breach, whether the 72-hour clock has started, and what goes on the record.

**Their question.** *Was personal data exposed, does this start a GDPR breach assessment or a 72-hour notification, and what do I document?*

#### Needs
- was personal data exposed
- whether this is a breach yet, and when the 72-hour clock starts
- what to ask the host and the other processors
- what to document, breach or no breach

#### Can skip
- the C code
- server settings

The answer in thirty seconds

A flaw is not a breach. An unpatched, internet-facing PHP application holding personal data is a risk to record and treat; it becomes a breach to assess when there is a sign of compromise on it. No named organisation has said it was compromised through php2shell as of the last check. Ask your hosts in writing, review from 17 October, and document the assessment either way.

#### Reading path
- [Your briefing](../briefings/dpo/index.html) 5 min
- [No named compromise: the evidence](../compromise/index.html) 3 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [grc/risks/r06-1/index.html](../grc/risks/r06-1/index.html) 1 min
- [grc/frameworks/gdpr/index.html](../grc/frameworks/gdpr/index.html) 1 min
- [If you run PHP](../playbook/index.html) 3 min

About 15 minutes in all. Choose *read as Morgan* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[php2shell](../glossary/index.html#php2shell)[Vulnerability](../glossary/index.html#vulnerability)[Exploit, exploitation](../glossary/index.html#exploit)[Shell](../glossary/index.html#shell)[Patch](../glossary/index.html#patch)[Primary source](../glossary/index.html#primary)[Web server](../glossary/index.html#web-server)[Remote code execution (RCE)](../glossary/index.html#rce)[Honeypot](../glossary/index.html#honeypot)

[Read as Morgan →](../briefings/dpo/index.html)

R
### Robin, ciso

I make the decisions · ******Some technical

**Who.** Accountable for security risk; must report exposure and evidence of non-compromise to the board.

**Their question.** *What is our exposure, what is our evidence we were not hit, and what do I tell the board?*

#### Needs
- exposure as a list
- evidence we were not hit, from which date
- the board line
- where agencies disagree

#### Can skip
- the C code

The answer in thirty seconds

The flaw is in the PHP runtime, so exposure is every internet-facing system running PHP, including vendor appliances. Review logs from 17 October (the earliest reported attempt), not from the fix. Attempts are reported at scale; no named victim is confirmed. Patch first, isolate where you cannot.

#### Reading path
- [Your briefing](../briefings/ciso/index.html) 4 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [Exploitation signals](../exploitation/index.html) 2 min
- [Detection and defence](../defence/index.html) 3 min
- [The agencies](../agencies/index.html) 3 min
- [If you run PHP](../playbook/index.html) 3 min

About 17 minutes in all. Choose *read as Robin* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Patch](../glossary/index.html#patch)[CDN](../glossary/index.html#cdn)[SAPI](../glossary/index.html#sapi)[Shell](../glossary/index.html#shell)[WAF](../glossary/index.html#waf)[Primary source](../glossary/index.html#primary)[CVE](../glossary/index.html#cve)[Exploit, exploitation](../glossary/index.html#exploit)[KEV](../glossary/index.html#kev)

[Read as Robin →](../briefings/ciso/index.html)

A
### Avery, cto

I make the decisions · ******Some technical

**Who.** Owns the platform and the engineering time; needs the patch order, what breaks, and what to change next.

**Their question.** *What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?*

#### Needs
- patch order
- what the fix changes in behaviour
- the end-of-life versions
- time-to-pull-the-plug as a platform property

#### Can skip
- the disclosure politics

The answer in thirty seconds

Patch internet-facing mod_php first, then FPM, then the rest; restart every worker and rebuild every image. The fix changes how PHP behaves when memory runs out, so test under load. 7.4 to 8.1 have no release. Afterwards, invest in an inventory that answers 'where is PHP' in minutes.

#### Reading path
- [Your briefing](../briefings/cto/index.html) 4 min
- [The two flaws](../flaws/index.html) 4 min
- [The code](../code/index.html) 7 min
- [If you run PHP](../playbook/index.html) 3 min
- [Detection and defence](../defence/index.html) 3 min

About 21 minutes in all. Choose *read as Avery* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[mod_php](../glossary/index.html#mod-php)[PHP-FPM](../glossary/index.html#fpm)[Patch](../glossary/index.html#patch)[Backport](../glossary/index.html#backport)[Shell](../glossary/index.html#shell)[End of life](../glossary/index.html#eol)[Primary source](../glossary/index.html#primary)[CVSS](../glossary/index.html#cvss)[Vulnerability](../glossary/index.html#vulnerability)

[Read as Avery →](../briefings/cto/index.html)

R
### Rowan, journalist

I tell others · ******Some technical

**Who.** Reporting the story; needs numbers that hold up, quotes that are on the page they are attributed to, and the order of events.

**Their question.** *Which numbers hold up, who said what first, and what is still unverified?*

#### Needs
- which numbers hold up
- who said what first
- quotes checked against their source
- what is unverified

#### Can skip
- server settings

The answer in thirty seconds

The 70% figure is a share of websites that use PHP, restated as a share of the Internet. The release was 21 October, not 22. Three parties claim the discovery; their dates do not conflict, their framing does. No agency has confirmed a successful compromise, and CISA has not listed either flaw as exploited.

#### Reading path
- [Your briefing](../briefings/journalist/index.html) 4 min
- [The numbers](../numbers/index.html) 2 min
- [Every claim](../claims/index.html) 1 min
- [Who found it](../discovery/index.html) 2 min
- [How disclosure broke](../leak/index.html) 1 min
- [The agencies](../agencies/index.html) 3 min

About 13 minutes in all. Choose *read as Rowan* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Exploit, exploitation](../glossary/index.html#exploit)[CISA](../glossary/index.html#cisa)[NCSC](../glossary/index.html#ncsc)[Primary source](../glossary/index.html#primary)[Patch](../glossary/index.html#patch)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[Out of memory (OOM)](../glossary/index.html#oom)[Vulnerability](../glossary/index.html#vulnerability)[Honeypot](../glossary/index.html#honeypot)

[Read as Rowan →](../briefings/journalist/index.html)

R
### Riley, communications team

I tell others · ******Plain English

**Who.** Writes the organisation's statement and answers the press; needs what is safe to say and what will be asked.

**Their question.** *What can we say that is true, what should we not say, and what will we be asked?*

#### Needs
- the safe statement
- the phrases to avoid
- the questions coming
- where to point people

#### Can skip
- the code
- the settings

The answer in thirty seconds

Safe to say: two critical flaws in PHP were fixed on 21 October; we updated or isolated our systems; we have no evidence of compromise and review continues. Do not say '70% of the Internet', 'the most severe ever' or 'exploited everywhere'. Point people to php.net and your national agency.

#### Reading path
- [Your briefing](../briefings/comms/index.html) 4 min
- [Explained from the start](../explained/index.html) 6 min
- [The numbers](../numbers/index.html) 2 min
- [Impact: offline vs compromised](../impact/index.html) 2 min
- [The agencies](../agencies/index.html) 3 min

About 17 minutes in all. Choose *read as Riley* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Exploit, exploitation](../glossary/index.html#exploit)[Patch](../glossary/index.html#patch)[CDN](../glossary/index.html#cdn)[Honeypot](../glossary/index.html#honeypot)[Primary source](../glossary/index.html#primary)[Web server](../glossary/index.html#web-server)[php2shell](../glossary/index.html#php2shell)[Remote code execution (RCE)](../glossary/index.html#rce)[Evidence vault](../glossary/index.html#vault)

[Read as Riley →](../briefings/comms/index.html)

S
### Sam, security lead

I run or build systems · ******Some technical

**Who.** Runs the response: patch order, mitigations, monitoring and the offline call.

**Their question.** *What do I patch first, what do I watch for, and when do I take something offline?*

#### Needs
- patch order
- temporary mitigations and what each misses
- what to alert on
- the offline threshold

#### Can skip
- the leak forensics

The answer in thirty seconds

Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when.

#### Reading path
- [Your briefing](../briefings/security/index.html) 3 min
- [If you run PHP](../playbook/index.html) 3 min
- [Exploitation signals](../exploitation/index.html) 2 min
- [Detection and defence](../defence/index.html) 3 min
- [The agencies](../agencies/index.html) 3 min

About 14 minutes in all. Choose *read as Sam* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[Shell](../glossary/index.html#shell)[Patch](../glossary/index.html#patch)[mod_php](../glossary/index.html#mod-php)[PHP-FPM](../glossary/index.html#fpm)[Multipart](../glossary/index.html#multipart)[Exploit, exploitation](../glossary/index.html#exploit)[KEV](../glossary/index.html#kev)[Primary source](../glossary/index.html#primary)[CVSS](../glossary/index.html#cvss)

[Read as Sam →](../briefings/security/index.html)

J
### Jamie, head of appsec

I run or build systems · ******Deeply technical

**Who.** Owns application security across many teams; needs scope, settings and the pipeline change.

**Their question.** *Which of our applications are in scope, which settings matter, and what do we add to the pipeline?*

#### Needs
- which applications are in scope
- settings in order of least breakage
- what to add to the pipeline
- where detection belongs

#### Can skip
- the disclosure politics

The answer in thirty seconds

Every application on an affected runtime is in scope, including ones with no uploads or sessions: the demonstrated paths run before application code. Add the running PHP version to the SBOM and fail the pipeline on an unfixed one. Detection belongs at the edge and on the host, not in the app.

#### Reading path
- [Your briefing](../briefings/appsec/index.html) 4 min
- [The two flaws](../flaws/index.html) 4 min
- [Affected systems](../affected/index.html) 1 min
- [Detection and defence](../defence/index.html) 3 min
- [If you run PHP](../playbook/index.html) 3 min

About 15 minutes in all. Choose *read as Jamie* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[SBOM](../glossary/index.html#sbom)[Patch](../glossary/index.html#patch)[PHP-FPM](../glossary/index.html#fpm)[Shell](../glossary/index.html#shell)[Multipart](../glossary/index.html#multipart)[Proof of concept (PoC)](../glossary/index.html#poc)[Primary source](../glossary/index.html#primary)[CVSS](../glossary/index.html#cvss)[Vulnerability](../glossary/index.html#vulnerability)

[Read as Jamie →](../briefings/appsec/index.html)

D
### Drew, php or platform engineer

I run or build systems · ******Deeply technical

**Who.** Runs the servers and containers; needs versions, SAPIs, ini settings and commands.

**Their question.** *Which versions, which SAPIs, which settings, which commands?*

#### Needs
- fixed versions
- which SAPI is how exposed
- the exact settings and where they must be set
- how to verify the running version

#### Can skip
- the board line
- the money

The answer in thirty seconds

Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker and rebuild images. Until then: session.upload_progress.enabled=0 in php.ini or the pool, low post_max_size, fatal_error_backtraces=0 on 8.5, pm.max_requests=1 on FPM. Verify with php -v inside the running container. Keep session.upload_progress.enabled=0 after the update as well: CVE-2026-115560, published by PHP on 23 October (as Cloudflare and SOCRadar report), affects the fixed releases under a rare session setting and is fixed only in the next regular release.

#### Reading path
- [Your briefing](../briefings/engineer/index.html) 3 min
- [The two flaws](../flaws/index.html) 4 min
- [If you run PHP](../playbook/index.html) 3 min
- [Affected systems](../affected/index.html) 1 min
- [The code](../code/index.html) 7 min

About 18 minutes in all. Choose *read as Drew* and the bar under the menu keeps your place on every page.

#### Words they will meet

[PHP](../glossary/index.html#php)[PHP-FPM](../glossary/index.html#fpm)[SAPI](../glossary/index.html#sapi)[CVE](../glossary/index.html#cve)[Backport](../glossary/index.html#backport)[Primary source](../glossary/index.html#primary)[CVSS](../glossary/index.html#cvss)[Vulnerability](../glossary/index.html#vulnerability)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[Remote code execution (RCE)](../glossary/index.html#rce)

[Read as Drew →](../briefings/engineer/index.html)

L
### Lee, developer

I run or build systems · ******Some technical

**Who.** Writes PHP applications; wants to know whether their code is the problem and what they can do.

**Their question.** *Is my code the problem, what do I change, and how do I check the box I deployed to?*

#### Needs
- is my code the problem
- what I can and cannot do in userland
- how to check the box I deploy to

#### Can skip
- the agency comparison
- the money

The answer in thirty seconds

Your code is not the problem and cannot be the fix: the flaw is in the engine beneath it. ini_set, .user.ini and auto_prepend_file all run too late. Check the running version where the code runs, after the restart, and tell the platform owner today if your target is 8.1 or older.

#### Reading path
- [Your briefing](../briefings/developer/index.html) 4 min
- [The two flaws](../flaws/index.html) 4 min
- [The code](../code/index.html) 7 min
- [If you run PHP](../playbook/index.html) 3 min

About 18 minutes in all. Choose *read as Lee* and the bar under the menu keeps your place on every page.

#### Words they will meet

[Patch](../glossary/index.html#patch)[Out of memory (OOM)](../glossary/index.html#oom)[Primary source](../glossary/index.html#primary)[PHP](../glossary/index.html#php)[CVSS](../glossary/index.html#cvss)[Vulnerability](../glossary/index.html#vulnerability)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[Remote code execution (RCE)](../glossary/index.html#rce)[mod_php](../glossary/index.html#mod-php)[longjmp](../glossary/index.html#longjmp)

[Read as Lee →](../briefings/developer/index.html)

A
### Ash, security researcher

I study it · ******Deeply technical

**Who.** Studies vulnerabilities; wants the bug classes, what was demonstrated against what, and the open technical questions.

**Their question.** *What are the bug classes, what was demonstrated, and what is still open?*

#### Needs
- the two bug classes
- what was demonstrated against which SAPI
- the fix in the code
- the open questions

#### Can skip
- the board line

The answer in thirty seconds

Two classes: an out-of-memory longjmp leaving request memory uninitialised, and worker global state pointing at freed request memory across requests. mod_php was exploited before application code; FPM for the first flaw is disputed. The fix removes longjmp for OOM. A report of an incomplete fix is open.

#### Reading path
- [Your briefing](../briefings/researcher/index.html) 3 min
- [The code](../code/index.html) 7 min
- [The two flaws](../flaws/index.html) 4 min
- [Who found it](../discovery/index.html) 2 min
- [In context: 2008 to 2026](../context/index.html) 3 min

About 19 minutes in all. Choose *read as Ash* and the bar under the menu keeps your place on every page.

#### Words they will meet

[Exploit, exploitation](../glossary/index.html#exploit)[mod_php](../glossary/index.html#mod-php)[PHP-FPM](../glossary/index.html#fpm)[Out of memory (OOM)](../glossary/index.html#oom)[longjmp](../glossary/index.html#longjmp)[CWE](../glossary/index.html#cwe)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[SAPI](../glossary/index.html#sapi)[Primary source](../glossary/index.html#primary)[PHP](../glossary/index.html#php)

[Read as Ash →](../briefings/researcher/index.html)

B
### Blake, analyst or policy advisor

I study it · ******Some technical

**Who.** Advises on policy or markets; wants what this says about disclosure, AI-assisted discovery and how agencies responded.

**Their question.** *How did coordinated disclosure fail, and what does AI-assisted discovery change?*

#### Needs
- how coordinated disclosure failed
- what AI-assisted discovery changes
- why agencies diverged
- the precedent

#### Can skip
- server settings
- the code

The answer in thirty seconds

A bug class seen and shelved in 2024 was turned into working exploits by three AI-assisted teams within three weeks in August 2026. The disclosure leaked 22.5 hours early. Agencies split on the hardest question, offline or not, along lines that look institutional rather than technical.

#### Reading path
- [Your briefing](../briefings/analyst/index.html) 4 min
- [Who found it](../discovery/index.html) 2 min
- [How disclosure broke](../leak/index.html) 1 min
- [In context: 2008 to 2026](../context/index.html) 3 min
- [The agencies](../agencies/index.html) 3 min
- [The numbers](../numbers/index.html) 2 min

About 15 minutes in all. Choose *read as Blake* and the bar under the menu keeps your place on every page.

#### Words they will meet

[Exploit, exploitation](../glossary/index.html#exploit)[Patch](../glossary/index.html#patch)[Proof of concept (PoC)](../glossary/index.html#poc)[Coordinated disclosure](../glossary/index.html#disclosure)[Honeypot](../glossary/index.html#honeypot)[WAF](../glossary/index.html#waf)[Primary source](../glossary/index.html#primary)[PHP](../glossary/index.html#php)[GitHub advisory (GHSA)](../glossary/index.html#ghsa)[Out of memory (OOM)](../glossary/index.html#oom)

[Read as Blake →](../briefings/analyst/index.html)

## Why name readers at all

The first version of this site opened with a sentence that was accurate and unreadable to most of the people who arrived on it: two CVE numbers, a nickname, and the words unauthenticated remote code execution. Accuracy is necessary and not sufficient. A board member who cannot tell what a CVE is will repeat the headline instead; a website owner who does not know the fix is in PHP rather than in WordPress will update the wrong thing. The readers on this page are the editor's working list, and the list will change as readers write in.


---
site v0.22.18 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/start/index.html
