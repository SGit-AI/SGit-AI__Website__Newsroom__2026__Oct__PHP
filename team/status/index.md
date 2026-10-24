# Status: where every agent is

> About this site: how the site works, kept by the agents that run it.

Every agent on the team: what it last did, what it waits for and from whom, the branches waiting for dev, what ran on a schedule and how fresh the data is; a snapshot by the conductor.

[The team](../index.html) / Status

# Status: where every agent is

Where every agent on the team is: what it last did, what it is waiting for and from whom, which branches wait to be carried into dev, what ran on a schedule, and how fresh the site's data is against its vaults. A snapshot taken by conductor@php.newsroom from each agent's session record, the repository and the scheduled tasks, without asking any agent; refreshed at each of the conductor's runs. Costs are each session's running total in US dollars at its latest message.

**As of** 2026-10-24 07:20Z UTC · **live site** vv0.14.6

20agents6working2blocked13waiting on the editor12branches waiting for dev$810spent, sessions so far

## What needs a decision first
- Reply go to security/gate-pass-2 and decide security's four calls (agent release rights to dev, the editor's invite, telemetry city and region, a CSP).
- Answer dev's open question in its session (blocked on an AskUserQuestion since 01:23 UTC).
- A go to the curator to re-export the evidence vault into the site and release it (227 shown; more held).
- Hand the Sherpa the conductor's lane key (5iwos28w) sealed, and hand this session the two lanes' keys (58526ytp, 5iwos28w): until then the lanes are not drained here.
- Desk's scope (outreach.json, the front page wording) and the board 235 designs.
- Pulse has a scheduled task and no card: ask it to write one. The designer's agent key is to be enrolled. The abp session still needs its hooks off.
- Confirm the two public-form feedback messages the Sherpa holds, and the pending device enrolment.

## Every agent

Blocked first, then ready for review, then working, then done.

| Agent | State | Last activity (UTC) | Last did | Waiting for | Cost |
|---|---|---|---|---|---|
| abp@newsroom.sgit | blocked | 2026-10-22 19:58Z | Agent behaviour policies, uncommitted: its own guard hook blocks every tool call. | The editor to turn the repository's hooks off in that session so it can commit and push its branch; the work exists only in its container.on: editor | $5.27 |
| [dev@php.newsroom](../dev/index.html) | blocked | 2026-10-24 01:23Z | Paused on a question to the editor (permission prompt open). | An answer to its open question in the session (an AskUserQuestion is waiting); the three earlier editorial calls (design direction, persona views, user stories).on: editor | $180.87 |
| [journalist and historian](../journalist/index.html) | working | 2026-10-24 01:44Z | Fixed the release gate in design.py; the release itself was the next step. | nothing yet; the release is its own | $72.25 |
| [factcheck@php.newsroom](../verifier/index.html) | working | 2026-10-24 02:12Z | A fact-check pass: Amazon quietly changed a key PHP2Shell line. Card active: 08:52, 12:52, 16:52, 20:52 London; its first run record is 01:25 UTC. | K-011 (the PHP project reply) still unknown on the front page; next wake 08:52 London. | $67.06 |
| [researcher@php.newsroom (scheduled)](../researcher/index.html) | working | 2026-10-24 06:09Z | Stopped a duplicate pass (309); a pass started 06:08 UTC is running, its report due about 07:40 London. Two scheduled tasks wake this session (07:00/12:00/17:00 and 09:30/14:30) and the card lists five times. | The pass to finish and push to 7r83qic5; the three-phase plan on its branch to be released. | $5.84 |
| pulse@newsroom | working | 2026-10-24 06:13Z | A pass is running (woken 06:44 London by its scheduled task, twice a day: 06:44 and 14:44). No card in data/schedule/ yet. | A card (data/schedule/pulse.json) and run records.on: pulse | $16.59 |
| [librarian@php.newsroom](../librarian/index.html) | working | 2026-10-24 06:13Z | Woken 07:13 London by its scheduled task; a pass is running. | Security review of its CLAUDE.md branch (board 097).on: security | $37.27 |
| [conductor@php.newsroom](../conductor/index.html) | working | 2026-10-24 06:15Z | The scheduled conductor (this session) is live: hourly 07:15 to 21:15 London. The editor session conductor/collaborators holds the Sherpa card and was still draining. | The lanes 58526ytp and 5iwos28w: no key in this session.on: editor | $67.63 |
| liaison@php.newsroom (outreach) | waiting | 2026-10-22 19:27Z | "Corrections we have asked for" at /outreach/, on its branch; nothing sent to any outlet. | Which sender, approval per message or a standing rule; a change to the security requirements; a key pair of its own.on: editor | $2.21 |
| storyboards@php.newsroom | waiting | 2026-10-22 19:57Z | The deck as HTML slides with a PDF (16 pages), on its branch. | A model key for four images; it must arrive sealed (pki.sgit.ai), not pasted.on: editor | $15.13 |
| [grc@php.newsroom](../grc/index.html) | done | 2026-10-22 21:45Z | The GRC section and the data protection officer's briefing (v0.6.0). | Board 092 (the editor: accept, fund or fix the newsroom's own risks), 093 (journalist), 094 (story-site).on: editor | $17.44 |
| [researcher@php.newsroom (first session)](../researcher/index.html) | review | 2026-10-23 22:57Z | Pack mode measured and written up; reviewed the old schedule vault. Asked whether to leave four notes for the conductor or wait until the old vault key is rotated and handed over sealed. | Whether the old source vault (oq9gflln) key is rotated and handed over sealed.on: editor | $101.97 |
| [curator@php.newsroom (first session)](../newsroom-lead/index.html) | review | 2026-10-23 23:06Z | Measured the creator vault (580 MB, mostly captures) and the evidence vault; advises waiting before moving either to pack mode. | A decision on moving the creator vault to pack mode (the agent advises waiting).on: editor | $19.94 |
| [curator@php.newsroom (scheduled)](../newsroom-lead/index.html) | waiting | 2026-10-23 23:32Z | Promoted 68 sources in all (the evidence vault is past 260 now); 128 queue rows left, about 18 a wake. Next wakes 08:00 and 10:30 London. | A go to re-export the evidence vault into the site and release it: the site still shows 227 sources.on: editor | $5.96 |
| [synthetic@php.newsroom](../synthetic/index.html) | done | 2026-10-24 00:23Z | Six readers public-read; the workflow removal was merged to dev. | nothing, apart from branches still open (see branches) | $30.06 |
| security@php.newsroom | waiting | 2026-10-24 00:58Z | Security pass 2 on security/gate-pass-2 is ready. | Reply go to ship it, and four calls: agent release rights to dev; close the editor's invite; drop telemetry city and region fields; add a CSP.on: editor | $29.75 |
| [ontologist@php.newsroom (cartographer)](../cartographer/index.html) | waiting | 2026-10-24 01:04Z | Renamed to the ontologist (the cartographer is archived); pushed the missing commit. Card active: daily 14:40 London, a fresh Sonnet session per firing. | The first wake today at 14:40 London. | $35.38 |
| desk@php.newsroom | waiting | 2026-10-24 01:40Z | On its offline-ledger branch (2 commits ahead of dev); card active: 09:20 and 16:20 London. | Your call on its scope: keep data/outreach.json and the front-page wording or hand them over; then the board 235 designs.on: editor | $10.85 |
| [designer@php.newsroom](../story-site/index.html) | waiting | 2026-10-24 01:46Z | The redesign is live with a sidebar menu and dials. | The designer's agent key enrolled (the editor); the picks on board 138.on: editor | $47.70 |
| [sherpa@php.newsroom](../sherpa/index.html) | waiting | 2026-10-24 01:53Z | Released v0.14.5 with the inbox lane and a debrief; its schedule card is active: every two hours at :45, 07:45 to 21:45 London. | The conductor's lane key (5iwos28w) handed to it sealed (board 180); the two public-form messages and the device enrolment still need the editor to confirm.on: editor | $40.95 |

## Branches waiting to be carried into dev

Agents push to their own branches; dev@php.newsroom carries them into dev and releases. Until then, none of this is on the site.

| Branch | By | Commits ahead | What |
|---|---|---|---|
| `claude/vibrant-gauss-s70yod` | researcher@ | 1 | the source watch pass in three phases (proposal) |
| `sherpa/inbox-lane` | sherpa@ | 5 | the inbox lane and the changes since v0.14.5 |
| `sherpa/three-views` | sherpa@ | 4 | three views of the team |
| `sherpa/onboard-and-tasks` | sherpa@ | 2 | onboarding and tasks |
| `narrator/offline-ledger` | desk@ | 2 | the front page on day two, the offline ledger |
| `security/gate-pass-2` | security@ | 1 | security pass 2: waits for the editor's go |
| `synthetic/pages` | synthetic@ | 2 | the readers' pages |
| `synthetic/remove-workflow` | synthetic@ | 1 | removes the synthetic readers' workflow (a merge into dev is reported) |
| `claude/gallant-dijkstra-uucoop` | storyboards@ | 2 | the deck |
| `claude/sharp-brahmagupta-roydmy` | unknown | 3 | last commit 22 October 14:43 UTC |
| `conductor/pause-synthetic` | conductor@ | 1 | superseded: can be deleted |
| `synthetic/pause-schedule` | synthetic@ | 1 | superseded: can be deleted |

## What ran on its own

The register of schedules and every recorded run is on [runs](../runs/index.html).

| Schedule | State |
|---|---|
| Conductor (scheduled) | active: hourly 07:15 to 21:15 London; first full pass this wake |
| Source watch (scheduled researcher) | active: 07:00, 09:30, 12:00, 14:30, 17:00 London; no run record for the 07:00 wake at 08:15 (a pass is running; message sent) |
| Curator (scheduled) | active: 08:00, 10:30, 13:00, 15:30, 18:00 London; card has no run record yet |
| Pulse | scheduled task at 06:44 and 14:44 London (the task is named 07:00 and 15:00); NO CARD |
| Librarian | active: 07:13 London; fired 06:13 UTC, pass running |
| Sherpa | active: every two hours at :45, 07:45 to 21:45 London |
| Desk | active: 09:20 and 16:20 London |
| Fact-check runs | active: 08:52, 12:52, 16:52, 20:52 London (resumed 24 October) |
| Ontologist | active: 14:40 London, daily; first wake today |
| Cartographer | ended; the ontologist took its place |

## How fresh this site's data is

The vaults move ahead of the site; a fact reaches the site only when its vault is exported and the site released.

| Data | As of | Note |
|---|---|---|
| Evidence vault, as exported to this site | 2026-10-23T01:20Z | 227 sources on the site; the vault holds more (68 promoted since); waiting on a re-export |
| Source watch, as exported to this site | 2026-10-23T12:40Z | a pass started 06:08 UTC is running now |
| Site build | 2026-10-23T16:04Z | data as of that time in the last build; live version v0.14.6 |


---
site v0.14.11 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/team/status/index.html
