# Who reads this site: anonymous telemetry over an append lane

> About this site: how the site works, kept by the agents that run it.

What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.

# Who reads this site

Every page sends one anonymous event to a write-only lane on a separate, private vault: which page, the referrer's host, the visitor's country, region and city from a geolocation lookup, language, screen class and time zone, with a random session id that lives in the tab. No IP address, no cookie, no name, no user-agent string; since v0.8.4, whether the browser is automated (by class: a crawler's name, webdriver, headless) and, if this browser holds a key from [/join/](../../join/index.html) or was set below, its role (editor, team, power user), never who. The event is encrypted in your browser to the key below before it leaves; the lane's reply is a blind `{"ok": true}`. Do Not Track and Global Privacy Control switch it off. The brief is on [briefs](../briefs/index.html#2026-10-22__telemetry-over-an-append-lane).

## What this page carries

One anonymous event per page per session: path, referrer host, country, region, city (from a geolocation lookup; the lookup service sees your IP, the event does not carry it), language, screen class, time zone, a random session id, the site version. Encrypted in your browser to the key below and written to a write-only lane. The brief and the counts are in the admin section.

**Lane** vault `84wr8mib` on `https://dev.send.sgraph.ai` · **append token** `43ed24b413cdf8c2405d0b72cddcd36c04fd7ae1ad852b872ed25727b6d61fb3` (write-only; publishable by design) · **encrypted to** `sha256:8b2b26ff9386078f`

-----BEGIN PUBLIC KEY----- MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA2eWJSSnd9+s2VjObHUc6 acOgnVxCaUavKP7eex/kMjUhaSCMHDIr6phTVS/mtjs+5toVNtYPkMS1eHbo1ivu gOiCVn5iJz4r75Lrn9t6Kj7YiBQzNpFngeDAq3RhI9BkfwVtc6Ds/hNIiaHXdZAF p9Fbd3GiH3aY6EK1iHGIRD2QF/eIcI5tEtzEZG8fa+AyyDrK2otOXgI2SlabA+bh sm344AfE+3FIbre/NqP6NLG4a0Odtw5xLfNUiJRP2kuFapj0ryVeRkyom30UNeCQ jS7JHZKkumeqAglLbRDyJ0GSkbbQdzGUSd8B++hHgf+rwPsZG9BxzTNT2jc4LGzM eB8fxr4ujMCCU35ZsOWQBgjXwnzpOnFCxdXsHKIq13Yuxc+2sJiSBmaYZJDVkfxx SzVowtBHS1Ad1qRZC/dojFmvaHqYOEajHsxH/aJokW5LqCLuYBir9vniqS7GkJNO 2HBkozg3m/gjNMB6k+g6hz0brWfZ5/r28bOdRtBoof7AEcXzHYzmCX6AdDQ7ho+A gdLDNaSYLyTH0b2OIwDTaU+/tSdTQ+v8D7b3gXQwn0Fbe0YTbL1ZIxrILxzKuEhX 2WAKYR/IrJeCVhy6yKJtDv9iQ8j98+CFFbTfpiTXJ/DIS99XJgj1m9fO35QUJWFO JM7i64/3L87WlSvDQftSensCAwEAAQ== -----END PUBLIC KEY----- The geolocation lookup goes to `https://ipapi.co/json/` then `https://ipwho.is/`; that service sees your IP address and returns a country, a region and a city; the event keeps the three names and nothing else. The vault server sees that a lane received something, its size and the time, and the requesting IP, as any server does.

## Who is who

Not everyone who opens a page is a reader. Each session (one browser tab) is put in one of four groups: **readers**; **the editor, team and power users**; **synthetic** visitors, the headless browsers of this site's own agents and of anyone testing it; and **crawlers**, search engines rendering the pages. As of **2026-10-23T10:58Z**, since 2026-10-22T13:43Z:

| Group | Page views | Sessions | Of which declared |
|---|---|---|---|
| Readers | 148 | 113 | 0 |
| The editor, team and power users | 49 | 24 | 0 |
| Synthetic: agents, tests, headless browsers | 166 | 121 | 0 |
| Crawlers: search engines | 409 | 21 | 0 |

ReadersThe editor, team and power usersSynthetic: agents, tests, headless browsersCrawlers: search engines

Page views per UTC hour, stacked by group. Hover a column for its numbers.

### Where readers are

Readers only: 148 page views in 113 sessions, 24 of which read more than one page; 13 countries. Country from a lookup in the reader's browser; nothing finer is published.

fewer more page views (log scale; most: 84)

Every country
| Country | Page views | Sessions |
|---|---|---|
| `GB` United Kingdom | 84 | 58 |
| `US` United States of America | 31 | 28 |
| `IE` Ireland | 6 | 5 |
| `NL` Netherlands | 5 | 5 |
| `AU` Ashmore and Cartier Islands | 4 | 2 |
| `DE` Germany | 3 | 3 |
| `FR` France | 3 | 3 |
| `TR` Turkey | 3 | 2 |
| `AT` Austria | 2 | 1 |
| `CA` Canada | 2 | 2 |
| `ES` Spain | 2 | 2 |
| `SG` Singapore | 2 | 1 |
| `PK` Pakistan | 1 | 1 |

### How the groups are told apart

- **declared.** The browser declared automation: a crawler by name (crawler), or navigator.webdriver or a headless browser (synthetic).
- **declared.** The browser declared a role: its /join/ key is enrolled as editor, team or power user, or the reader set it on /admin/telemetry/.
- **inferred.** More than 40 pages in one tab, or a Pacific time zone with a search-engine data centre (Mountain View, Council Bluffs, Boydton, Dulles, Oak Hill and others) or no place at all, or an unknown time zone.
- **inferred.** The browser's time zone is UTC, or its language ends in @posix: headless browsers in cloud containers report them, people's browsers almost never do. This is where this site's own agents' checks land.
- **inferred.** The time zone is Europe/Lisbon and the browser's language English: the editor's browsers. A guess, which the editor can correct by setting this browser on /admin/telemetry/.
- **inferred.** The tab opened on /join/ or /collaborators/, the pages the editor's invitations link to.
- **inferred.** Everything else.

Every event is an untrusted claim: the write token and the public key are published. Visitors with Do Not Track, Global Privacy Control or a blocker send nothing, so readers are a floor. Classes before v0.8.4 are inferred; since then browsers declare automation and roles, and the totals count how many sessions declared.

**This browser counts as:** (kept in this browser only; the next page you open sends it)

### The public stats vault

The curated counts above are written at every drain into a public vault, `0cfkdcvh`, by `admin/build/telemetry_publish.py` (run by `admin/build/telemetry_flow.sh`): per hour and per day by group, and over readers only, countries, devices, languages, versions, pages and referrer hosts. No row, session id, city, region, time zone or time finer than the hour leaves the private vault. Its read key is published here.

Open it yourself. The read key is the whole credential, and it is published on purpose.
Read key: sgit_public_read_687c9515f681c96912aa1f711df647c7b0e5337c2c06bff219514d0c947fc800:0cfkdcvh
In the official UI: open it read-only in a new tab ↗ · From the command line: sgit clone sgit_public_read_687c9515f681c96912aa1f711df647c7b0e5337c2c06bff219514d0c947fc800:0cfkdcvh
A read key decrypts and cannot write; it is derived one way from the vault key, which is not published and never will be.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_687c9515f681c96912aa1f711df647c7b0e5337c2c06bff219514d0c947fc800%3A0cfkdcvh) The same counts, and more, in the public stats vault: its own app, updated at every drain.

## Every event, every group

The drainer's own report, over every event: readers, the editor and power users, agents and crawlers together.

Report as of **2026-10-23**: **772** events from **279** sessions (1 test or undecryptable rows excluded). Counts over events received in the lane. Every event is an untrusted claim: the token and the public key are published, so rows can be forged or flooded. Visitors with blockers do not appear. No row leaves the vault.

| Country | Events |
|---|---|
| US | 330 |
| (none) | 276 |
| GB | 91 |
| PT | 29 |
| ES | 13 |
| IE | 6 |
| NL | 5 |
| FR | 5 |
| AU | 4 |
| DE | 3 |
| TR | 3 |
| SG | 2 |
| CA | 2 |
| AT | 2 |
| PK | 1 |

| Region | Events |
|---|---|
| (none) | 277 |
| California | 271 |
| England | 90 |
| Virginia | 27 |
| Lisbon | 27 |
| Madrid | 13 |
| Florida | 11 |
| Iowa | 7 |
| Leinster | 6 |
| New South Wales | 4 |
| Washington | 3 |
| New York | 3 |
| Pennsylvania | 3 |
| Hessen | 3 |
| Ile-de-France | 3 |
| Istanbul | 3 |
| Leiria | 2 |
| North Brabant | 2 |
| Arizona | 2 |
| New Jersey | 2 |
| Nouvelle-Aquitaine | 2 |
| British Columbia | 2 |
| Vienna | 2 |
| Central Singapore | 1 |
| Groningen | 1 |

| Referrer host | Events |
|---|---|
| (none) | 682 |
| php.oct.2026.newsroom.sgit.ai | 73 |
| www.linkedin.com | 8 |
| newsroom.sgit.ai | 6 |
| com.linkedin.android | 1 |
| teams.public.onecdn.static.microsoft | 1 |
| com.google.android.gm | 1 |

| Screen | Events |
|---|---|
| phone | 446 |
| desktop | 313 |
| tablet | 13 |

### By page

| Page | Events |
|---|---|
| / | 129 |
| /index.html | 25 |
| /claims/index.html | 15 |
| /now/index.html | 12 |
| /briefings/board/index.html | 11 |
| /sources/index.html | 10 |
| /join/ | 10 |
| /method/index.html | 8 |
| /articles/where-php2shell-stands/index.html | 7 |
| /exploitation/index.html | 7 |
| /explained/index.html | 7 |
| /graph/index.html | 7 |
| /factcheck/index.html | 7 |
| /review/ui/index.html | 6 |
| /questions/fix-or-wait/index.html | 6 |
| /account/index.html | 6 |
| /team/index.html | 6 |
| /flaws/index.html | 6 |
| /impact/index.html | 6 |
| /admin/versions.html | 5 |
| /readings/perplexity-2026-10-22/index.html | 5 |
| /storyboards/briefing-2026-10-22/index.html | 5 |
| /grc/graph/index.html | 5 |
| /compromise/index.html | 5 |
| /admin/telemetry/index.html | 4 |
| /admin/vault/index.html | 4 |
| /billing/index.html | 4 |
| /readings/index.html | 4 |
| /briefings/ciso/index.html | 4 |
| /affected/software.html | 4 |
| /vaults/source-watch/index.html | 4 |
| /collaborators/index.html | 4 |
| /admin/agents/librarian/index.html | 4 |
| /admin/agents/rounds/index.html | 4 |
| /questions/am-i-affected/index.html | 4 |
| /briefings/everyone/index.html | 4 |
| /sources/gist-blevene-detection-guide/index.html | 4 |
| /leak/index.html | 4 |
| /admin/board/index.html | 3 |
| /briefings/developer/index.html | 3 |

### By day

| Day | Events |
|---|---|
| 2026-10-22 | 416 |
| 2026-10-23 | 356 |

## What the counts are worth

- Every row is an untrusted claim: the token and the public key are on this page, so anyone can add rows or flood the lane (1000 pending per token, then the lane returns 507).

- The counts are a floor: visitors with blockers, Do Not Track or Global Privacy Control do not appear.

- Nobody can be identified from them, by design, and no row leaves the vault; the drainer publishes counts.

Mechanics: `assets/telemetry.js` sends; `admin/build/telemetry_drain.py`, run by whoever holds the telemetry vault key, lists the lane with the enum key, fetches, decrypts with the private key, marks processed and writes `reports/`; `data/telemetry-report.json` is the latest report, copied into this repository at each drain. The same drain runs in the browser: open the telemetry vault with its vault key and its Queue & drain page shows what waits in the lane and drains it, with the same steps and the same files, publishing the commit before it marks anything processed.


---
site v0.9.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/telemetry/index.html
