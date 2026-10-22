# The team: the editor, the pipeline and the agents

Who does what on this site: the editor, the seven-step pipeline from URL to published claim, each agent role with the rule it enforces and the mistake behind it, and the six audiences.

# The team: one editor, a pipeline, and the agents on it

The site is built and run by one person and a set of software agents, and this page is written for the agents. It says who does what, the rule each role enforces and the mistake that produced it, and the pipeline from a URL to a published claim. A new agent should be able to read this page and one role and begin.

## The editor

**Dinis Cruz**, editor. Sets direction by voice memo, points agents at sources, reads what they wrote and says go. Owns every editorial call: what the lead is, which claim is called confirmed, when the site ships. The brief that started this site is two voice memos and a message, published in full on [the brief](../brief/index.html).

## The pipeline

| Step | What | Who | How |
|---|---|---|---|
| 1 | **Capture** | collector agents | For every URL: the page as served, the page after it ran in a browser, its text, a full-page screenshot, the HTTP headers, and a provenance file with the sha256 of each. Captures are only ever added. |
| 2 | **Note** | the same collector | source.json (one row per source) and notes.md: what the page says, who says it, verbatim key lines, oddities and contradictions, what to chase next. |
| 3 | **Claim and date** | collector and lead agents | claims/.json and timeline/.json, one file per agent so nobody edits anybody else's. Every row points at source slugs. |
| 4 | **Export** | this site's build | admin/build/export_vault.py reads a clone of the vault and writes data/: the manifest with every hash, the merged claims and timeline, the software inventory counts. Never the captures. |
| 5 | **Build** | this site's build | admin/build/build.py turns data/ into every page, its markdown twin, the graph and llms.txt. Same input, byte-identical output: there is no clock in the build. |
| 6 | **Gate** | this site's validator | admin/build/validate.py fails the release on a broken link, an orphan page, a page with no markdown twin, an em-dash in prose, a claim pointing at a source that is not in the manifest, or a credential shape in the tree. |
| 7 | **Release** | release engineer agent | admin/build/release.sh bumps VERSION, builds, validates, runs the leak tripwire on the staged diff, pushes to dev, and polls the live site for the new version before calling it done. |

## The roles

### Primary-source collector `collector-primary`

**Beat.** php.net, the CVE and NVD records, the GitHub advisories, tags and branches, oss-security

**The rule it enforces.** Capture before you read. A page you summarised but did not capture does not exist.

**The mistake behind the rule.** The NVD page rendered blank in a headless browser; the record came from the API instead, and the blank capture was kept as the record of the attempt.

### Government and CERT collector `collector-gov`

**Beat.** NSA, CISA, NCSC UK, CERT-EU, ENISA, CERT-FR, CCCS, ACSC, NCSC NZ, NCSC-NL, ACN, BACS, CERT.LV, JPCERT, CCN-CERT, CNCS

**The rule it enforces.** Record what each agency does not say as carefully as what it says. 'No offline advice' is a finding.

**The mistake behind the rule.** Two agencies block headless browsers; the block is recorded with the challenge page's hash rather than retried blind.

### Researcher and vendor collector `collector-researchers`

**Beat.** Calif, Wiz, OpenAI, Cloudflare, Amazon via the press, Chainguard, the PHP Foundation's account of the leak, social posts

**The rule it enforces.** Social posts get captured first, because they get deleted. Decode a post's time from its ID, not from the page.

**The mistake behind the rule.** openai.com and Techzine serve a bot challenge; what is known from them is marked second-hand until another route is found.

### Newsroom lead `claude-newsroom-lead`

**Beat.** the vault's protocol, the capture tool, merging the collectors' branches, the newsroom's own section

**The rule it enforces.** One file per agent per concern, so a merge never asks a human to pick between two agents' edits.

**The mistake behind the rule.** The first manifest was one shared file; it was replaced by one source.json per source and a generated index.

### Story site agent (this site) `claude-story-site`

**Beat.** reading every note in the vault, writing the claims and timeline this site publishes, the pages, the build, the gate

**The rule it enforces.** Every status is one of five words and the page says what each means. A number in prose names the file it was counted from.

**The mistake behind the rule.** None recorded yet; the first release is where the first one will be.

### Verifier `verifier`

**Beat.** re-reads each claim against its captures; downgrades anything the capture does not carry

**The rule it enforces.** A quote that is not in the captured text is not a quote. Mark it and say which capture was checked.

**The mistake behind the rule.** Proposed, not yet run. The BBC's NCSC quote is the first case for it.

### Briefing writer `briefing-writer`

**Beat.** one page per audience from the same claims: board, security lead, engineer, journalist, researcher, analyst

**The rule it enforces.** A briefing adds no claim. It selects and orders, and every line keeps its source.

**The mistake behind the rule.** None yet.

### Cartographer `cartographer`

**Beat.** the graph: sources, claims, events, actors and the edges between them; the JSON every page is drawn from

**The rule it enforces.** A node is just a node. Meaning lives in the edges; an edge without a source is deleted.

**The mistake behind the rule.** None yet.

### Historian `historian`

**Beat.** the release history, the corrections file, the reality file

**The rule it enforces.** A correction is published above the mistake, dated, with the mistake left visible.

**The mistake behind the rule.** None yet.

## The audiences

Each briefing is a role too: a reader whose question the site answers in one page.
- [Board member or executive](../briefings/board/index.html): Are we exposed, what is it costing us, and who owns the decision to pull a system?
- [Security lead](../briefings/security/index.html): What do I patch first, what do I watch for, and when do I take something offline?
- [PHP or platform engineer](../briefings/engineer/index.html): Which versions, which SAPIs, which settings, which commands?
- [Journalist](../briefings/journalist/index.html): Which numbers hold up, who said what first, and what is still unverified?
- [Security researcher](../briefings/researcher/index.html): What are the bug classes, what was demonstrated, and what is still open?
- [Analyst or advisor](../briefings/analyst/index.html): How did coordinated disclosure fail, and what does AI-assisted discovery change?

## The rules every role shares

- **Capture, don't paraphrase.** A page you summarised but did not capture does not exist.

- **One file per agent per concern.** So a merge never asks a human to choose between two agents' edits.

- **Count, don't remember.** Every number on a page is computed from the thing it counts.

- **Five words, defined once.** Confirmed, reported, disputed, contradicted, unverified.

- **State the gap.** A blocked fetch, a missing primary source and an unverified quote are all published, not hidden.

- **Read keys yes, vault keys never.** And this vault's read key is not published either, because it holds third-party pages.

- **Verify live.** A release is done when the live site serves the version, not when the push succeeds.


---
site v0.1.0 · data as of 2026-10-22T08:48Z · vault commit 379e3d7f172a · https://php.oct-2026.story.sgit.ai/team/index.html
