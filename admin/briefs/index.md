# Briefs

The build briefs for this site, published in full before the work, newest first.

# Briefs

A brief is written before the work and published as written: what was asked, in whose words, what exists to build on, the design, what it cannot do, the deliverables and the open questions. The newsroom and the sgit.ai sites keep theirs the same way. The file is the record; this page renders `admin/content/briefs/`, newest first. The written request and the two voice memos that started the site are on [the brief](../../brief/index.html).

2026-10-22 · `2026-10-22__telemetry-over-an-append-lane.md`

## Who reads this site: anonymous telemetry over an append lane

Status: accepted and being built. Brief by Dinis Cruz (editor), spoken on 22 October 2026; written up by dev@php.newsroom. Build brief, the kind an agent executes.

### The ask, in the editor's words

Add logging using an append lane. Capture who is visiting the website, which pages they see, and where they come from. All of it from the front end: there is no back end. Not the IP address: the region (London, Surrey) and the country, which the browser can get from a lookup service. Keep it in a separate vault, and share that vault's key with the editor. Write this as an article brief in the admin section first, then implement it.

### What exists to build on

- sgit.ai's build brief "Telemetry from a published vault" and the append-lane API: a write-only channel gated by a token, a blind `{"ok": true}` response, no account needed to send, lanes outside the commit tree. The routes are on dev.send.sgraph.ai only.

- The newsroom's own reading meter already encrypts a reader's share in the browser to a published public key (sgit's hybrid envelope v2: AES-256-GCM wrapped with RSA-OAEP-SHA256) and posts it to a lane. The same forty lines of Web Crypto carry an event.

- The CLI has `sgit pki keygen / export / encrypt / decrypt` and no lane commands, so draining is HTTP: list with the enum key, fetch, decrypt locally, mark processed.

### The design

1. A separate, private telemetry vault (id `84wr8mib`) holds the key pair, the drained events and the daily reports. Its vault key, the enum key and the key pair's passphrase stay with the editor and the drainer; none of them is in this repository.

2. The site publishes, in `data/telemetry.json`, the three things a visitor's browser needs and may hold: the telemetry vault id, the append token and the recipient public key. The append token is write-only and the write response is blind, so a visitor who reads it out of the page can add rows and learn nothing. This is the one credential shape that survives publication.

3. On every page, `assets/telemetry.js` mints a random session id in memory, asks a geolocation service for the visitor's country, region and city (the service sees the IP; the event does not carry it), builds one event, encrypts it to the public key and posts it to the lane. It never blocks the page, fails silently, and rate-limits itself to one event per page per session.

4. `admin/build/telemetry_drain.py` lists the lane with the enum key, fetches pending files, decrypts them with the private key, writes them as JSON lines into the telemetry vault under `drain//`, marks them processed, and computes `reports/.json`: counts by page, country, region, referrer host and site version. The site's admin section publishes the counts, never the rows.

5. A visible notice on every page says that anonymous usage events are sent and what they contain, because opening a page on this site now phones home, and the estate's rule is to say so where it happens.

### The event

 { "v": 1, "site": "php.oct.2026.newsroom.sgit.ai", "ver": "0.2.3", "ts": "2026-10-22T12:00:00Z", "sid": "8 random hex", "path": "/code/index.html", "ref": "news.ycombinator.com", "country": "GB", "region": "England", "city": "London", "lang": "en-GB", "screen": "desktop", "tz": "Europe/London" } No IP, no user agent string, no cookie, no name. `ref` is the referrer's host only. `city` is whatever the lookup returns, which is the ISP's idea of a city, not a location.

### What it cannot do, said up front

- It cannot prove anything. Every visitor holds the token and the public key, so any row can be forged and the lane can be flooded (1000 pending files per token, then 507). Rows are claims; the reports say so.

- It cannot tell who. There is no identity; the session id is random and dies with the tab.

- It cannot see the server's view. dev.send.sgraph.ai sees lane activity, sizes, timing and the requesting IP; the geolocation service sees the IP too. "The content is encrypted" is true; "the traffic is invisible" is not.

- Readers with blockers will not appear. The counts are a floor.

### Deliverables

- `data/telemetry.json` (public lane descriptor), `assets/telemetry.js`, the notice in the footer, this brief.

- `admin/build/telemetry_drain.py`, run by whoever holds the telemetry vault key; `admin/telemetry/index.html` showing the latest report.

- The telemetry vault: `README.md`, `identity/` (public bundle, passphrase-protected private key), `drain/`, `reports/`.

- An end-to-end test: one event written from the CLI, listed with the enum key, fetched and decrypted, before the first page ships.

### Open questions for the editor

- Which geolocation service to trust with visitors' IPs. The first release uses ipapi.co with ipwho.is as fallback; both are third parties and both see the IP. A Cloudflare-fronted site could use `/cdn-cgi/trace` instead and leak nothing to a third party.

- Whether the reports should be public (counts only) or stay in the vault. The first release publishes counts.

- Whether the editor wants the city at all. Region and country answer the question asked; the city is noise from ISPs.

2026-10-22 · `2026-10-22__review__front-page-and-navigation.md`

## Review: the front page and the navigation, at v0.2.5

Author: the journalist role (claude-journalist), on joining the site. Asked for by the editor: review the current content of the front page and suggest ways to improve navigation. Read at 1400px and 390px wide, against the built v0.2.5 pages. Findings first, then what v0.2.6 did, then what is proposed and left open on the board (items 016 to 019).

### What works

- The lead paragraph is accurate and dense, and every claim in "What is established" carries its sources inline. That is the site's argument made visible, and it should stay at the top.

- "What is not" is the most valuable section on the page for a journalist: it says what would close each question. Few outlets publish this.

- The six numbers with their status pills tell the "70%" story in one row, before a word of prose.

### Findings

- **The page had a factual error about itself.** "Read it for your job" said "Six briefings" above twelve cards. The count was typed by hand when there were six, and nobody updated it. Fixed in v0.2.6: the number is now computed from data/roles.json, as is the same count on the team page. The lesson is the site's own rule, count don't remember, applied to its own copy.

- **The most useful page is not linked from the front page body.** "If you run PHP" (the playbook), the two flaws, exploitation signals, how disclosure broke, who found it, detection and defence, the code and the review are reachable only through the top menu. The body links to the timeline, claims, numbers, agencies, impact and the briefings. A reader who arrives from a search wanting to know what to do has to know to open "The story" menu and scan thirteen items.

- **The stats row has seven tiles in a six-column grid**, so 674 sits alone on a second row at desktop width. Either six tiles or a grid that fits seven.

- **The kicker shows a raw instant**, "2026-10-22T11:34Z", twice in the first screen (bar and kicker). Readers parse "22 Oct, 11:34 UTC" faster; the machine form belongs in the footer.

- **"The last 48 hours" is the last eight events, all from one morning,** and two of them are about this site (the vault opening) rather than the story. It will go stale between releases, and a table of times is the hardest format to scan on a phone.

- **On a phone, the first screen is a 150-word paragraph**, then seven stat tiles stacked two by two, then a caveat box. The first link to an action is several screens down.

- **The menus are long and mixed.** "The story" has thirteen items; "About" had thirteen, mixing reader pages (the method, corrections) with engineering (board, roles, briefs, telemetry) and billing. "The evidence" mixed captured evidence (every source, the inventory) with the site's own analysis of it (claims, numbers, agencies, the graph), which is exactly the line the editor asked to make visible.

- **llms.txt sits in the main menu** next to the story menus. It is for agents and belongs in the footer, where the markdown twin link already is.

- **There was nowhere for dated, signed writing.** Every page is rebuilt from the vault on each release, which is right for the evidence, but means the site had no way to say "this is what we knew at 11:34 UTC on 22 October" and keep it.

### What v0.2.7 did

- The menu splits by layer: **The story** (unchanged), **Articles** (new: signed, dated), **The analysis** (claims, numbers, agencies, affected systems, who says what, the graph: derived from the evidence), **The evidence** (every source, the software inventory, the vault opened, and the new layers page). The vault page moved from About to The evidence.

- A new page, **Evidence, derived, authored** (/layers/), classifies every file the site is built from, from data/layers.json, and the gate now fails a release if a data file is not classified.

- A new **Articles** section, with an "Articles, signed and dated" row on the front page. Articles are markdown files in admin/content/articles/ with front matter naming the site version, vault commit and capture time they were written against; citations are [[slug]] and the gate checks them like every other citation. An article older than the current data shows a banner saying the evidence has moved.

- The briefing count on the front page and the team page is computed.

### Proposed, on the board

- **016, a start-here row.** Four doors directly under the lead: If you run PHP; the two flaws; exploitation signals; offline versus compromised. They answer the four questions a cold reader arrives with: what do I do, what is it, is it being used, how bad has it been.

- **017, "Since the last release" instead of "The last 48 hours".** The timeline rows added since the previous version, story events only. It turns the section into a changelog of the story, which is also the hook a returning reader needs.

- **018, About split in two.** About (method, team, brief, corrections, layers) for readers; Engineering (admin, board, roles, briefs, telemetry, releases) for agents and the editor. Billing and the reading account move to the balance in the bar, which already links to them. llms.txt moves to the footer.

- **019, a layer badge on every page**, from data/layers.json: evidence, derived or authored, in the kicker. A reader should never have to guess whether they are reading a capture, the site's analysis of it, or someone's signed opinion.

- Smaller: seven stat tiles in a grid that fits seven, or six tiles; the kicker's time in reader form; on phones, the caveat box after the start-here row rather than before it.

### Open questions for the editor

- Should articles carry the reading meter like story pages (they do in v0.2.7, at the article price), or be free like the method and the brief?

- Should the newsroom's own section on the story (newsroom.sgit.ai/php-flaws) carry the opinion pieces, as memo 2 suggests, with this site keeping only the journalist's and historian's dated reports? This review assumes yes.

2026-10-22 · `2026-10-22__brief.md`

## The brief, as written by the editor on 22 October 2026

Status: accepted, by being sent. Author: Dinis Cruz. Drafted by nobody: these are the editor's own words, a message to the agent followed by two voice memos (below).

Hi based on the guidance on sgit.ai for these type of *.sgit.ai websites and what we have been doing at newsroom.sgit.ai can you create a dedicated website for us to track in super fact, deterministic and with provenance way what is going on with the PHP vulnerability

we have started doing some mapping at https://newsroom.sgit.ai/php-flaws/index.html

an an initial vault has been created to start capturing all data [vault key withheld: a vault key is write access and is never published]

I will send some voice memos about it that I have recorded next

please push to dev as you have updates since this is an important story and we can add a lot of vault here while showing the power of our setup

include the billing model in this site

### The initial prompt that started the first session

The message above, with the two memo transcripts attached, in a Claude Code session with the sgit skill and the estate's guidance pages (sgit.ai/docs/guidance, sgit.ai/docs/guidance/repositories, the newsroom's php-flaws section and its meter and economics pages) read first.


---
site v0.2.7 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/briefs/index.html
