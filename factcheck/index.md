# Fact-check: how sure can you be of each claim

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Every claim on the PHP flaws site graded independently by the fact-check desk on a spectrum of evidence from A0 to A6, with a filter for only what can be relied on, the contradiction ledger, and the open tickets.

# Fact-check: how sure can you be of each claim

Every claim on this site has a status word chosen by the agent that wrote it. The fact-check desk grades each one again, independently, by opening the captures it cites and reading them: what kind of statement it is (a record, a count, a quote, an opinion), how strong the evidence is on a scale from A0 to A6, whether anything contradicts it, and whether the status word claims more than the evidence carries. Where the answer is "not as far as the site says", it opens a ticket. It highlights; it does not fix.

**0 of 70 claims graded**. **0** can be relied on without reservation (A5 or A6, holding as worded, uncontested, not an opinion). **0** carry a status word stronger than their evidence. **0** tickets are open.

## The spectrum of evidence

| Level | Means | Claims now |
|---|---|---|
| **A0** Unsupported○○○○○○ | No capture carries it, or the cited capture does not say it | 0 |
| **A1** Weak signal●○○○○○ | Second hand, unnamed, blocked, or only partly carried by its capture | 0 |
| **A2** Reported●●○○○○ | One named party says it, in a capture this desk checked | 0 |
| **A3** Echoed●●●○○○ | Several outlets say it, tracing to one origin | 0 |
| **A4** Corroborated●●●●○○ | Two or more independent parties say it, at least one checked in a capture | 0 |
| **A5** Confirmed●●●●●○ | Two or more independent primary sources say it, each checked in a capture | 0 |
| **A6** Established●●●●●● | The authoritative primary record carries it, or this site counted it from a captured file | 0 |
| refuted | A stronger source says otherwise | 0 |

A level is earned from captures the desk opened and read, never from how often a thing is repeated: ten outlets restating one headline are one source. An open contradiction caps a claim at A1 and a dispute at A2 until it is explained. An opinion is shown as an opinion and never rises above A3 as a fact; the facts under it are graded in its note. Absence of evidence is *not shown*, which is not the same as false.

## Every claim, graded

Pick how sure you need to be. "Only what I can be very sure of" shows claims at A5 or A6 that hold as worded, are not contested, and are not opinions.
Show claims graded at least everything, refuted tooA0A2 ReportedA4 CorroboratedA5 ConfirmedA6 Established
 include opinions  include contested Only what I can be very sure of

| Claim, and why it is graded so | Fact-check | Kind | Verdict | Site status | Tickets |
|---|---|---|---|---|---|

## The contradiction ledger

Where the reporting disagrees. Each record keeps every statement, who made it and when, what each actually measures, and the desk's reading of why they differ. A contradiction is not resolved by picking a winner; it is explained, or it stays open.

None recorded yet.

## Runs

Each run is checked against a stated site version and vault commit, so its grades can be repeated by anyone with the vault's read key.

| Run | Against | Checked | Opened | Summary |
|---|---|---|---|---|

## How the desk works

The desk is `factcheck@php.newsroom`. Its role, the full model and the runbook a scheduled run follows are in [admin/factcheck/README.md](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/factcheck/README.md); its tickets are an [Issues-FS](https://issues-fs.sgit.ai/) graph in `admin/factcheck/.issues/`, typed nodes and typed edges in plain JSON files; its grades are [data/factcheck.json](../data/factcheck.json). Mode one checks every claim against the evidence vault. Mode two goes outside for the weak and the contested, and records what it finds as a request to capture, never as a citation.


---
site v0.5.4 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/factcheck/index.html
