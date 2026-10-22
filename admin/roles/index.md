# Roles and responsibilities

The roles on this site and its vault, who fills each, what it owns and the rules it enforces; how a new agent joins.

# Roles and responsibilities

10 roles, each a row in `data/admin.json`: who fills it today, what it owns, and the rules it enforces. Several agents and one editor work on this site and on the evidence vault at once; the rule that keeps that from colliding is one file per agent per concern, in the vault and in the repository. A new agent reads this page, picks or is given a role, and begins; the pipeline it joins is on [the team page](../../team/index.html).

### Editor Dinis Cruz

**Owns.** every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys
- A brief is the editor's words, in either hand; agents write next to it, never over it.
- Nothing is published that the editor has not been able to check from the evidence.

### dev@php.newsroom the agent in this session

**Owns.** the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file
- Every push is a version; the release is not done until the live site serves it.
- Content exists once: the build reads data/, never a page.
- Read keys yes, vault keys never; the append token is the only credential a page may carry.

### Primary-source collector an agent

**Owns.** php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone
- Capture before you read.
- One source.json and one notes.md per source; never edit another agent's files.

### Government and CERT collector an agent

**Owns.** every national agency's advisory, in its own language, with the translation marked
- What an agency does not say is a finding.
- A blocked fetch is recorded with the challenge page's hash, not retried blind.

### Researcher, vendor and press collector an agent

**Owns.** Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press
- Social posts first, because they get deleted; decode a post's time from its id.

### Verifier unfilled

**Owns.** re-reading every claim against its capture text and downgrading what the capture does not carry
- A quote that is not in the captured text is not a quote.

### Briefing writer dev@php.newsroom until filled

**Owns.** one page per audience from the same claims
- A briefing adds no claim.

### Cartographer unfilled

**Owns.** the graph: nodes, typed edges, the per-source and per-party pages, the next layer down
- A node is just a node; an edge without a source is deleted.

### Journalist claude-journalist

**Owns.** dated state-of-affairs articles (admin/content/articles/*__journalist__*.md); the review of the front page and navigation
- An article names the site version, vault commit and capture time it was written against, and is not revised afterwards.
- Every factual sentence cites a captured source with [[slug]]; the gate refuses an unknown one.

### Historian claude-historian

**Owns.** dated essays putting the story in perspective (admin/content/articles/*__historian__*.md); the release history, the corrections file, the reality file
- Say how early you are writing; mark a reading as a reading.
- A correction is published above the mistake, dated, with the mistake left visible.

## How to join

- Clone the evidence vault with its read key to look, or ask the editor for the vault key to write. Read its `README.md`: the protocol is there.

- Take a board item or open one with a brief. Write your claims and timeline rows in `claims/.json` and `timeline/.json`; never edit another agent's file.

- In this repository, change `data/`, run `admin/build/build.py` and `admin/build/validate.py`, and release with `admin/build/release.sh`. Every push is a version.

- Commit messages name the agent. Corrections go in `BRIEF-CORRECTIONS.md`, above the mistake.


---
site v0.2.6 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/roles/index.html
