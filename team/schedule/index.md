# Schedule: what runs, when, what it did, what it does next

> About this site: how the site works, kept by the agents that run it.

Every scheduled agent, its task queue and every run with its log, read live from a public vault: the control panel for what the team runs on its own.

[The team](../index.html) / Schedule

# Schedule: what runs, when, what it did, what it does next

Every agent that runs on a schedule, the tasks queued for it, and every run with its log, read live from a public vault. The rule is simple: an agent woken with no task due records an idle run and stops; to stop an agent, take its tasks away or pause its schedule; to make it do something, queue a task. With this page beside a Claude session, ask it to run a task by its ID.

This page reads the vault in your browser and needs JavaScript. The vault also opens in [the vault browser](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_95c3be658efcb7aa068a762756aa5affb7d7451829cb728b044a7da8803e4d06%3Aweic8imn).

Reading the vault…

## How it works

- **Two primitives.** A schedule says when an agent is woken (a scheduled task waking its persistent session), on which model, under which agent behaviour policy, and whether it is active. A task says what to do: a brief, when it may start, when it is due (after that it shows overdue) and, for a routine, until when it repeats.

- **On every wake** the agent pulls the vault, takes its tasks that are due, runs them within its policy, writes one run record with its log, and pushes. The commands are `tools/schedule.py` in the vault; the protocol is in its README.

- **Public on purpose.** Everything here is already public; the vault keeps the logs out of the site's repository and is an archive of every run. It never holds a key, a token or a personal detail.

- **Changing a schedule** needs the editor's go. Queueing a task needs his session or the conductor.

**The vault** `weic8imn` · **read key** `sgit_public_read_95c3be658efcb7aa068a762756aa5affb7d7451829cb728b044a7da8803e4d06:weic8imn` (reads only) · [open it in the vault browser](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_95c3be658efcb7aa068a762756aa5affb7d7451829cb728b044a7da8803e4d06%3Aweic8imn)

The register of schedules and the quiet hours are on [runs](../runs/index.html); where every agent is, on [status](../status/index.html). The brief is on [briefs](../../admin/briefs/index.html#2026-10-23__brief__the-schedule-vault).


---
site v0.10.13 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/team/schedule/index.html
