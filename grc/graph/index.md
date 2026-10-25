# The risk graph: php2shell stakeholders, risks, weaknesses, vulnerabilities and code

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

727 nodes and 1357 typed edges joining every php2shell risk to its stakeholders, weaknesses, vulnerabilities, fixes, code, claims, stories, roles and controls.

[GRC](../../grc/index.html) · [Risks](../../grc/risks/index.html) · [Stakeholders](../../grc/stakeholders/index.html) · [Frameworks](../../grc/frameworks/index.html) · [The graph](../../grc/graph/index.html) · [Explore](../../grc/explore/index.html) · [Gaps](../../grc/gaps/index.html) · [Changes](../../grc/changes/index.html) · [From the network](../../grc/network/index.html)

# The risk graph: stakeholders, risks, weaknesses, vulnerabilities, code

727 nodes and 1357 edges, built from the register on every release and joined to the graphs already on this site: the claims and their sources ([the story graph](../../graph/index.html)) and the fix and the code it changed ([the code review graph](../../review/index.html)). One graph, no copies: a claim, a source or a file is the same node here as there. The JSON is [data/grc-graph.json](../../data/grc-graph.json).

A line from a stakeholder group to a risk means someone in the group carries part of it or of a risk beneath it; a line from a risk to a weakness means the risk, or one beneath it, arises from it; the weaknesses on the two CVEs reach the fix and the code on [the code review graph](../../review/index.html). Each risk's own page draws its whole path.

## The weaknesses

What the risks arise from. Two are the CVEs themselves; the rest are conditions of the ecosystem, the disclosure process and this newsroom, each joined to the risks it gives rise to and, where there is one, to the code.

### The allocator's longjmp-based bailout on out-of-memory

An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.

Gives rise to: [R01 Remote code execution on internet-facing PHP servers](../../grc/risks/r01/index.html), [R01-1 Default Apache mod_php installations exploited before application code runs](../../grc/risks/r01-1/index.html), [R01-5 Popular applications compromised before authentication](../../grc/risks/r01-5/index.html), [R03 Exploitation outpaces patching](../../grc/risks/r03/index.html), [R06 A compromise becomes a reportable breach](../../grc/risks/r06/index.html), [R06-1 Personal data taken from a compromised PHP application](../../grc/risks/r06-1/index.html), [R08-1 A known bug left unexploited, then unfixed, for two years](../../grc/risks/r08-1/index.html) Arises from: CVE-2026-109618: RCE via OOM corruption

### Request globals that survive a failed request

State from a request that failed is still there when the next one starts.

Gives rise to: [R01 Remote code execution on internet-facing PHP servers](../../grc/risks/r01/index.html), [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../grc/risks/r01-2/index.html), [R01-5 Popular applications compromised before authentication](../../grc/risks/r01-5/index.html), [R06 A compromise becomes a reportable breach](../../grc/risks/r06/index.html) Arises from: CVE-2026-109619: RCE via stale global state

### Bailout as a class of bug

Patching the demonstrated paths does not make the mechanism safe: other paths to the same bailout should be expected.

Gives rise to: [R01-4 The fix is incomplete, or a third flaw follows](../../grc/risks/r01-4/index.html) Arises from: CVE-2026-109618: RCE via OOM corruption, CVE-2026-109619: RCE via stale global state

### PHP versions the project no longer fixes

8.1 and older get no upstream fix; reaching them needs a distribution backport, paid support or an upgrade.

Gives rise to: [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../grc/risks/r01-3/index.html), [R04 Services lost to precautionary shutdowns](../../grc/risks/r04/index.html), [R04-2 Councils and police offline without saying why](../../grc/risks/r04-2/index.html) Arises from: CVE-2026-109618: RCE via OOM corruption, CVE-2026-109619: RCE via stale global state

### One embargo shared by many parties

Four independent finders, a coalition, early advice to critical infrastructure and image builders: every party is a place the secret can leave by.

Gives rise to: [R02 The coordinated disclosure broke before the fix was ready](../../grc/risks/r02/index.html), [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../grc/risks/r02-1/index.html), [R02-2 Early mitigation advice to a few providers leaked](../../grc/risks/r02-2/index.html), [R02-3 Patched builds published before the embargo lifted](../../grc/risks/r02-3/index.html)

### Not knowing where PHP runs

PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.

Gives rise to: [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../grc/risks/r01-6/index.html), [R04 Services lost to precautionary shutdowns](../../grc/risks/r04/index.html), [R04-1 National government services offline](../../grc/risks/r04-1/index.html), [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../grc/risks/r06-3/index.html), [R09 Not knowing where PHP runs](../../grc/risks/r09/index.html)

### A filter in front of an unpatched engine

Rules match the payload shapes seen so far; attackers mutate payloads, and only traffic routed through the filter is covered.

Gives rise to: [R03-2 Mass scanning and mutated payloads after the leak](../../grc/risks/r03-2/index.html), [R03-4 Detections built on a proof of concept with the wrong mechanism](../../grc/risks/r03-4/index.html), [R05 A web application firewall taken for a patch](../../grc/risks/r05/index.html)

### Exploitation that cannot yet be seen

Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.

Gives rise to: [R03 Exploitation outpaces patching](../../grc/risks/r03/index.html), [R03-1 Attempts before disclosure](../../grc/risks/r03-1/index.html), [R03-3 Exploited in the wild without anyone being able to show it](../../grc/risks/r03-3/index.html), [R03-4 Detections built on a proof of concept with the wrong mechanism](../../grc/risks/r03-4/index.html), [R06-2 Essential and financial entities miss their reporting clocks](../../grc/risks/r06-2/index.html), [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../grc/risks/r06-3/index.html)

### Numbers and ratings repeated without their source

70% of the Internet, CVSS 10, 30 million sites: figures that measure different things, carried from post to post until they read as fact.

Gives rise to: [R04-3 The agencies' advice disagrees](../../grc/risks/r04-3/index.html), [R07 Decisions made on numbers that measure something else](../../grc/risks/r07/index.html)

### Frontier models that find memory-safety bugs in widely used C

The capability that found these flaws ahead of most attackers is available to attackers too, and finds more than maintainers can fix in a week.

Gives rise to: [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../grc/risks/r08/index.html)

### A small, thinly funded maintainer team at the base of the web

An audit found the bug in 2024; the fix took until 2026. Four reports in a month land on the same handful of people.

Gives rise to: [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../grc/risks/r08/index.html), [R08-1 A known bug left unexploited, then unfixed, for two years](../../grc/risks/r08-1/index.html), [R08-2 Several finders, one small team](../../grc/risks/r08-2/index.html)

### Agents that read the open web and can publish

Nine capabilities in the newsroom's agent grant have no boundary in the way (admin/security/abp/DELTA.md); the gate that guards publishing lives in the repository the agents can edit.

Gives rise to: [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html), [R10-2 A vault key or token published](../../grc/risks/r10-2/index.html) In this repository: [admin/build/release.sh](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/build/release.sh), [admin/build/validate.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/build/validate.py), [admin/build/security_check.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/build/security_check.py), [.github/workflows/pages.yml](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/.github/workflows/pages.yml)

### Third-party text inside the agents' context

Captured pages, feeds, tips and other models' output are read by agents that hold credentials; one sentence addressed to a model is enough to try.

Gives rise to: [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html), [R10-1 Prompt injection through captured material](../../grc/risks/r10-1/index.html) In this repository: [admin/build/security_check.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/build/security_check.py), [admin/security/injection-allowlist.json](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/security/injection-allowlist.json)

### A status word chosen by the agent that wrote the claim

The fact-check desk found eleven claims whose status word is stronger than their evidence.

Gives rise to: [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html), [R10-3 A status word stronger than its evidence](../../grc/risks/r10-3/index.html) In this repository: [admin/factcheck/fc.py](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/admin/factcheck/fc.py), [data/claims.json](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/blob/dev/data/claims.json)

## What is in it

| Kind of node | How many |
|---|---|
| test | 270 |
| control | 95 |
| source | 85 |
| claim | 62 |
| stakeholder | 43 |
| treatment | 41 |
| risk | 34 |
| page | 26 |
| code | 16 |
| weakness | 14 |
| role | 10 |
| briefing | 9 |
| member | 8 |
| remediation | 7 |
| story | 5 |
| vulnerability | 2 |

## The verbs

Every edge is a verb read from the first node to the second; its inverse is read back. No edge says only that two things are related.

| Verb | Inverse | Edges |
|---|---|---|
| `part_of` | `has_part` | 76 |
| `arises_from` | `gives_rise_to` | 51 |
| `backed_by` | `evidences` | 91 |
| `fixed_by` | `fixes` | 8 |
| `realised_in` | `realises` | 9 |
| `located_in` | `location_of` | 8 |
| `protected_by` | `protects` | 41 |
| `governed_by` | `governs` | 139 |
| `concerns` | `concerned_in` | 12 |
| `told_in` | `tells` | 26 |
| `tracked_by` | `tracks` | 45 |
| `briefed_by` | `briefs` | 9 |
| `cites` | `cited_by` | 164 |
| `shown_on` | `shows` | 58 |
| `tests` | `tested_by` | 502 |
| `owned_by` | `owns` | 40 |
| `borne_by` | `bears` | 22 |
| `treated_by` | `treats` | 24 |
| `raised_by` | `raises` | 11 |
| `informed_by` | `informs` | 15 |
| `regulated_by` | `regulates` | 6 |

## How each edge is known

Every edge says how it is known: read from a capture (with its slug), read from the fix commit, inferred by an agent (with the agent), or confirmed by a person (data/grc-basis.json). The drawing above shows the register's own joins, which are the GRC desk's inferences. To walk the graph one node at a time, with inferred edges dashed, use [explore](../explore/index.html); for what is missing, [the gaps](../gaps/index.html).

| How it is known | Edges | Verbs |
|---|---|---|
| **source**: read from a capture | 255 | cites 164, backed_by 91 |
| **code**: read from the fix commit | 287 | tests 270, realised_in 9, fixed_by 8 |
| **inferred**: inferred by an agent, not yet checked | 815 | tests 232, governed_by 139, part_of 76, shown_on 58, arises_from 51, tracked_by 45, protected_by 41, owned_by 40, told_in 26, treated_by 24, borne_by 22, informed_by 15, concerns 12, raised_by 11, briefed_by 9, located_in 8, regulated_by 6 |


---
site v0.22.6 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/graph/index.html
