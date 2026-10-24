# The synthetic security lead: every run and its latest review

> About this site: how the site works, kept by the agents that run it.

A synthetic security lead reads the live site on its own device with its own question; its latest review in full and every run before it.

# The synthetic security lead

Head of security operations at a bank. Expert. Needs detection, exploitation status and sources that can be cited to the CISO.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

**Question** Is it exploited in the wild, how do I detect it, what do the agencies say, and how good is the evidence? · **time** 10 minutes · **device** 1680×1050, desktop, dark · **vault** `vjsqjhvp` · **runs** 1

## What this reader judges
- Is every claim traceable to a captured source?
- Are exploitation claims graded honestly?
- Is detection guidance specific enough to act on?
- Is anything overstated?

Reading path after the front page: [briefings/security/index.html](../../../briefings/security/index.html), [exploitation/index.html](../../../exploitation/index.html), [defence/index.html](../../../defence/index.html), [agencies/index.html](../../../agencies/index.html), [claims/index.html](../../../claims/index.html), [sources/index.html](../../../sources/index.html).

## The latest review: 2026-10-22T1754Z on v0.4.3
This is the most useful single place I have seen for php2shell: attempts are kept apart from compromises, the detection guidance is specific enough to turn into alerts today, and the agency table is something I can put in front of the CISO, but the status labels are not applied consistently, and that stops me citing the grading as it stands.
**Got the answer** yes · The short answer was on the security briefing (step 2); the full answer, with sources I could brief from, came on exploitation, defence and agencies (steps 3 to 5), about six minutes in.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 4 | 3 | 4 | 4 |

### What works
- Attempts, honeypot hits and compromises are separated in every exploitation row, and the KIND column (attempt, negative finding, claim, second-hand) is exactly the distinction I have to make to the CISO. ([exploitation/index.html](../../../exploitation/index.html))
- The KEV negative finding is dated to the catalog version, release time, fetch time and entry count, and is called a point-in-time finding. I can cite that as written. ([exploitation/index.html](../../../exploitation/index.html))
- Host signals are given by layer (access log, PHP error log, kernel, process tree, network), with literal strings such as 'in Unknown on line 0' and 'exit signal Segmentation fault (11)'. My SOC can build alerts from that table. ([defence/index.html](../../../defence/index.html))
- The 'What the log cannot show' row and the closing 'So: can it be detected?' section say plainly where telemetry goes blind (nginx default format, no worker id). That is honest and it changes what I ask my team for. ([defence/index.html](../../../defence/index.html))
- The WAF table puts each vendor's own caveat next to its rule, including Fortinet shipping alert-only by default and Fastly's rule needing to be enabled. That is operationally useful. ([defence/index.html](../../../defence/index.html))
- The agency table quotes each body verbatim on the offline question, records the two it could not read, and shows that the BBC's NCSC quote is not on the captured NCSC page. That is the kind of checking I need before I quote an agency upwards. ([agencies/index.html](../../../agencies/index.html))
- The thirty-second answer and 'What to decide or do' list is a usable runbook skeleton: patch order by SAPI, mitigations recorded as partial, process-tree alerting, a named owner for the offline call. ([briefings/security/index.html](../../../briefings/security/index.html))
- Overstatements are called out with evidence: the CVSS 10.0 is marked CONTRADICTED, '70% of the Internet' is marked UNVERIFIED, and the CVE record's 8.2 to 8.5 range is flagged as missing 7.4 to 8.1 for scanners. ([claims/index.html](../../../claims/index.html))

### What does not
- **high** The site contradicts itself about whether Amazon's own post was captured, while still grading the claim built on it as CONFIRMED. ([exploitation/index.html](../../../exploitation/index.html))The exploitation row for Alan Woodward reads 'Cloudflare's own post confirms attack traffic, Amazon's own post not found', but claims/index.html grades 'Amazon and Cloudflare saw sites being probed' CONFIRMED with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog' (capture 20261022T111755Z).
- **high** CONFIRMED is used for single-source items although the site's own definition requires two or more primary sources or a count from a captured file. ([claims/index.html](../../../claims/index.html))The legend says 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file', yet the CISA offline-advice claim is 'CONFIRMED 1/1', Latvia's restrictions 'CONFIRMED 1/1' and Weird Gloop 'CONFIRMED 1/1'. On exploitation/index.html, CCCS, CERT.LV and the CISA ADP row are each 'CONFIRMED (PRIMARY)' on one source.
- **medium** The same CERT.LV statement carries different grades on different pages. ([exploitation/index.html](../../../exploitation/index.html))exploitation/index.html: CERT.LV 'Automated exploitation attempts seen in Latvia; no reports of successful attacks' graded 'CONFIRMED (PRIMARY)'. claims/index.html and briefings/security/index.html: 'Automated exploitation attempts were seen in Latvia; none succeeded' graded 'REPORTED 1/1'.
- **medium** The front page tally of statuses does not match the claims page, and its legend has four statuses where the rest of the site uses five. ([index.html](../../../index.html))index.html: '70 statements checked: 22 confirmed, 11 disputed, 4 unverified' and a legend without CONTRADICTED. claims/index.html: '70 claims: 22 confirmed, 33 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **medium** The headline count of exploitation signals counts the same Amazon honeypot event twice. ([exploitation/index.html](../../../exploitation/index.html))'What the captured sources carry is 20 signals', but the first two rows are the same 17 October MadPot attempt, once from the AWS blog and once 'via The Hacker News'.
- **medium** The banner on every page promises a saved copy behind every fact, but the sources page says the copies are private, so I can cite a hash but not show the captured text to anyone. ([sources/index.html](../../../sources/index.html))Banner: 'every fact links to a saved copy of its source'. sources/index.html: 'The captures are third-party pages held privately and are not republished; this page links to the originals'.
- **low** Amazon's own wording, 'broadly exploited in the wild', appears only deep in the claims rows. The at-a-glance block reads as calmer than the primary vendor source does. ([index.html](../../../index.html))index.html at a glance: 'ARE ATTACKERS TRYING? Yes ... seen by one internet security company', with no mention of Amazon's 'PHP2Shell is now being broadly exploited in the wild' (claims/index.html, REPORTED 1/2).
- **low** A Log4j 2021 source page is reachable from the evidence list but has no claim or event attached, so it looks like noise in a php2shell evidence trail. A 404 page is also logged as a captured primary source. ([sources/cisa-alert-log4j-2021/index.html](../../../sources/cisa-alert-log4j-2021/index.html))'No claim cites this source yet.' 'No timeline event cites this source yet.' On sources/index.html: 'Page Not Found | CISA ... primary · CAPTURED ... HTTP 404'.
- **low** One Fortinet signature ID looks malformed, and I would paste these straight into a ticket. ([defence/index.html](../../../defence/index.html))'Three FortiGuard signatures (090502648, 090502651, 09052654)': the third has eight digits where the other two have nine.
- **low** An unexplained price pill in the header changes from page to page, which is odd on a site I am meant to trust. ([index.html](../../../index.html))The header shows '£4.99' on index.html, '£4.98' on briefings/security, '£4.97' on exploitation and '£4.92' on the source page, with no label.

### What this reader would change, in order
- Re-run the status rules across every table so that a one-source primary item is REPORTED (or add a named 'PRIMARY, single source' grade to the legend), and use one grade per claim on every page. ([claims/index.html](../../../claims/index.html), medium)I cannot hand the CISO a grading scheme that breaks its own definition. Consistency is what makes the labels citable.
- Fix the Woodward row to say Amazon's own post was captured, and link the Amazon claim to the aws-security-blog-madpot capture. ([exploitation/index.html](../../../exploitation/index.html), small)This is the single clearest self-contradiction on the exploitation question, which is the question I most need to get right.
- Make the signal count 19 distinct events (or say '20 rows, 19 events'), merging the two Amazon 17 October rows. ([exploitation/index.html](../../../exploitation/index.html), small)Double counting weakens a page whose whole value is careful counting.
- Bring the front page tally and legend into line with the claims page (five statuses: 33 reported, 8 disputed, 3 contradicted). ([index.html](../../../index.html), small)The first numbers I saw did not match the later ones, which made me doubt the rest until I checked.
- Add a short 'copy into your SIEM' block with the actual Sigma, Falco and ModSecurity rule snippets, or direct links to the specific rule files, beside the host-signal table. ([defence/index.html](../../../defence/index.html), medium)The signals are right, but my team still has to go and find the rule text. One click less saves an hour on day two.
- Change the banner wording to 'every fact links to its source and a hash of the saved copy', or publish the captured text for public government advisories. ([sources/index.html](../../../sources/index.html), small)The promise and the practice should match. Advisories from CISA and the NCSC carry no republication risk and are the ones I would cite.
- Add Amazon's 'broadly exploited in the wild' wording, graded, to the at-a-glance exploitation tile. ([index.html](../../../index.html), small)A board member will see that headline elsewhere. The front page should show it and its grade, not only the calmer KEV view.
- Check the third Fortinet signature ID and either label or remove the £ pill in the header. ([defence/index.html](../../../defence/index.html), small)Small things, but I paste IDs into tickets, and unexplained numbers in the chrome erode trust.

### Lines this reader reacted to
- [exploitation/index.html](../../../exploitation/index.html): *A remote code execution bug is not an invisibility cloak.*Good framing, and the page earns it by listing the signals. I will borrow this line.
- [exploitation/index.html](../../../exploitation/index.html): *This is a point-in-time negative finding; the vault keeps the file and its hash so that the time can be proven later.*Exactly how I want a KEV absence stated: dated, bounded, provable.
- [defence/index.html](../../../defence/index.html): *with the known exploits no application code runs, so a shell from a worker is the exploit*The most actionable sentence on the site. That is a high-fidelity alert with almost no false positives.
- [defence/index.html](../../../defence/index.html): *An organisation whose only telemetry is the access log cannot answer "were we hit" from it*Honest, and exactly the point I need to make to justify EDR coverage on web tiers.
- [briefings/security/index.html](../../../briefings/security/index.html): *Every claim of exploitation so far is of attempts, probes or honeypot hits.*This is the line I will give the CISO. It is careful without being complacent.
- [exploitation/index.html](../../../exploitation/index.html): *REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found*This lost me: the sources page lists Amazon's own post as captured, and the claims page says both companies confirmed it.
- [claims/index.html](../../../claims/index.html): *CONFIRMED two or more primary sources agree, or the fact was counted from a captured file*A good definition, but then 'CONFIRMED 1/1' appears several times below it. Hold yourselves to it.
- [agencies/index.html](../../../agencies/index.html): *The sentence the BBC quotes from the NCSC is not on the NCSC page as captured; its opening matches the Canadian text.*This kind of checking is why I would come back to the site. It saves me from repeating a misquote upwards.

### Since the last run

First run: there is no previous review to compare against.

Reviewer: agent-session.

[The whole run: the journey, the measurements and every flag](../../../admin/synthetic/security/2026-10-22T1754Z/index.html).

## Every run

Scores are 0 to 5 from this reader's point of view.

| Run (UTC) | Site | Answered | Answered | Clarity | Trust | Design | Navigation | Fails (high / medium / low) | Pages |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-22T1754Z](../../../admin/synthetic/security/2026-10-22T1754Z/index.html) | v0.4.3 | yes | 4 | 4 | 3 | 4 | 4 | 2 / 4 / 4 | 9 |


---
site v0.10.18 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/security/index.html
