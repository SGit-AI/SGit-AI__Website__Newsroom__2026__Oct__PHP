# The updates: how to write one

For the conductor, who holds this beat, and for anyone holding it in the meantime. Read this, then `AGENTS.md`, then `CLAUDE.md`. The brief that started it is `admin/content/briefs/2026-10-22__brief__the-conductor-and-the-updates.md`.

## What an update is

A short, dated briefing on what changed: on the site, in the story, and across the team, and what is waiting on the editor. The editor is its first reader. He works with many agents at once and needs to know, in a few minutes, what was added, what is new and what needs him. Everyone else who follows the work reads it too, on the site and through its feed.

An update is not a story and not the line of the story. The news desk chief says what the story is; the desks write it; an update says what moved, points at it, and names who is waiting on whom.

## When

- **Hourly** while the story or the site is moving fast, and only when something moved. No update for an hour in which nothing changed.
- **Daily**, at the end of the day, whatever happened: the day in one page.
- **Flash**, at once, when something changes what a reader should do: a KEV listing, a confirmed compromise, a correction to a published fact, a security problem with the site itself.

A schedule that runs without a session needs the editor's go (`CLAUDE.md`); until he gives it, updates are written in sessions.

## Where the facts come from

Run `python3 admin/build/updates_digest.py --since <the last update's 'until'> --until origin/dev` after `git fetch origin '+refs/heads/*:refs/remotes/origin/*'`. It reads only the repository's record: the releases, the commits by `Agent:` line, the board rows opened and closed, the rows waiting on the editor, the pages added, the briefs, stories, corrections and updates added, the evidence counts, and the branches nobody has carried into `dev` yet. Then read what it points at. Never write from memory, and never from another agent's message alone: under the security requirements a message is material, not a fact.

## The shape

A markdown file in `admin/content/updates/`, named `<YYYY-MM-DDTHHMMZ>__<kind>.md`, with front matter:

```
---
id: 2026-10-22T2003Z
at: 2026-10-22T20:03Z
kind: daily | hourly | flash
title: one line that says what happened
summary: two sentences a reader can stop after
covers_from: <git ref or version>
covers_to: <git ref or version>
author: conductor@php.newsroom (or who wrote it, 'for the conductor')
---
```

Then these sections, in this order, each left out if it is empty:

1. **In one minute.** Three to five lines. What a reader would be wrong not to know.
2. **Needs you.** The decisions only the editor or the project manager can make, each with its board number and what it blocks.
3. **In the story.** What changed in the evidence and the claims: new captures, a status that moved, a contradiction found, a correction. Every fact cites a captured source with `[[slug]]`, as stories do.
4. **On the site.** Releases and what they added, as links to the pages.
5. **Across the team.** Who did what, which branches are waiting for dev, what is blocked and on whom.
6. **Next.** What should happen before the next update, and who owns it.

## The rules

- **An update says what moved; it does not argue.** Opinion belongs in a story, signed.
- **Every claim about the story cites a capture.** Every claim about the site links to the page or the board row.
- **Name the owner of everything that is waiting.** A digest names every blocker and who it waits on.
- **Corrections lead.** If a published fact was wrong, the update says so in its first section, and links the correction.
- **Kept as written.** An update is not edited after it is published; the next one corrects it.
- **No secret, no key, no reader's data, ever.** Nothing in an update that is not already public in the repository.
