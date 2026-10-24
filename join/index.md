# Join: a key for this device, in one tap

> About this site: how the site works, kept by the agents that run it.

Open the invitation the editor sent you and this page makes a key on your device, so the feedback you send from any page is signed as yours; the enrolled keys, as handles and fingerprints.

[Power users](../collaborators/index.html) / Join

# Join: a key for this device, in one tap

To give feedback on this site you sign it with a key of your own, so the team knows who it came from. Getting one is one tap: open the invitation the editor sent you (a link or a QR code), and this page makes a key on this device and sends it to him.

This page needs JavaScript: the key is made in your browser.

Loading…

## How it works

- **An invitation.** Ask Dinis, by email or on WhatsApp, or with [the join form](../collaborators/index.html#join). He makes it on his phone ([Invite](invite/index.html)) and sends you a link or a QR code meant for you alone.

- **One tap.** The link opens this page, which makes a key pair in your browser: one half signs, the other half is public. The signing half stays in this browser and cannot be copied out of it, by this site or anyone else.

- **Enrolled.** Your public key goes to the team, encrypted, with the invitation. When the invitation's signature checks out, your key is added to the list below; from then on what you sign shows as yours.

- **Feedback from any page.** Press **Feedback**, next to Ask at the top of every page: say what is wrong, unclear, missing or good, with a screenshot if you like, and send. It is signed with your key and encrypted to the team.

## Enrolled keys

Handles and fingerprints only, never a name. editor: The editor: his feedback and reviews come first, and the review queue is his; team: A member of the team that runs the site; power-user: A power user: reads what is new when asked, and says what works.

| Handle | Role | Signing key | Device | Enrolled |
|---|---|---|---|---|
| editor | editor | `sha256:89984d97af4d2deb` | desktop | 2026-10-23 |
| power-user-1 | power-user | `sha256:fe0518960fcebb22` | desktop | 2026-10-24 |

## What it does not do

- A key belongs to one browser on one device. Another device needs its own invitation; clearing this site's data deletes the key.

- An invitation is a credential until it is used: whoever opens it first can join with it. Each one enrols at most three devices and expires in two weeks.

- A signature proves which key wrote a message, not who holds the key: that is what the editor's enrolment adds.

Keys are in pki.sgit.ai's and sgit's format, so `sgit pki verify` checks every signature. The brief is on [briefs](../admin/briefs/index.html#2026-10-22__brief__feedback-keys-and-review).


---
site v0.14.9 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/join/index.html
