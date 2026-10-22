# Feedback from any page, signed; onboarding by QR code; a review queue for the editor

Status: phase 1 being built on branch conductor/collaborators. Brief by Dinis Cruz (editor), a voice memo of 22 October 2026 to the conductor; written up by conductor@php.newsroom. Build brief, the kind an agent executes.

## The ask, in the editor's words (through a transcriber, condensed)

"We should have an append lane to provide feedback from the website: anybody, in any part of the website, can open the sidebar and provide feedback about the page, with screenshots, something that somebody can then open and review. Maybe we need a new agent that reviews it. That includes me.

What's cool is that you can now sign it. Anybody who wants to provide feedback for now needs to have a key: they go through the onboarding process. Part of the exercise is to make this onboarding as simple as possible. Take the workflow we have with the PKI and make it super simple: here is the flow, here is a QR code, we just created your thing; even me giving them a QR code to paste, with what they need, my public key, and some instructions. I want to onboard more contributors and more people. If you want to provide feedback and be involved, contact me by email or ping me on WhatsApp, and we create that web of trust.

The other thing is for me. You have my key, and I can identify myself. How can we create UIs unique to me, and to the team? We have lots of new pages and I need to review them: see what is there, provide comments, on an iPad: next, next, next. How can you get feedback from me, and especially you, the conductor, on the pages that are being created and the pages that will be created next?"

## What exists to build on

- The pane on the right of every page (`assets/ask/ask.js`, dev@php.newsroom's): tabs, and the reader's vault in the same key slot as the phone app.
- The collaborators vault (58526ytp) and its public write-only lane, encrypted in the browser to `sha256:e3ff50abd96816ef`, drained by `admin/build/collaborators_drain.py`: join requests and feedback from /collaborators/ already arrive there.
- pki.sgit.ai's key formats: a key pair is RSA-OAEP 4096 (to receive secrets) and ECDSA P-256 (to sign), the public half the JSON bundle `sgit pki export` emits, the fingerprint `sha256:` and the first 16 hex of the SHA-256 of the key's SPKI bytes; `sgit pki verify` checks a signature. The register's web of trust (invitations, two-way links, the editor as root) is where these keys can go later.
- The section ledger (`data/sections.json`): every page and section with its versions, so "what is new or changed since I last looked" is already counted.

## The design

### Phase 1: a key, an invitation, and feedback from any page

1. **A key per device, made in the browser.** On `/join/`, the browser makes the person's key pair with Web Crypto, in sgit's format. The private halves are kept in this browser as non-extractable keys (IndexedDB): they sign, and nothing on the page, no script and no extension that reads the page's storage, can read them back out. The public bundle and its fingerprint are shown.
2. **The invitation is a QR code.** `admin/build/invite.py new --handle <h> --role <r>` (run by the conductor or the editor, outside the repository) makes a random invitation code, records only its SHA-256 in `data/contributors.json`, and writes a link and its QR code to the scratchpad: `https://php.oct.2026.newsroom.sgit.ai/join/#j1.<code>.<handle>`. The editor sends it to one person, by WhatsApp or email. The code is in the fragment, so it never reaches a server.
3. **Joining is one tap.** The join page makes the key and sends an enrolment, `{kind: "enrol", code, handle, bundle, device}`, signed by the new key and encrypted to the collaborators key, to the collaborators lane. `invite.py enrol --vault <clone>` (after the drain) checks each enrolment's signature and that its code's hash is an open invitation, and adds the key to `data/contributors.json` with its handle and role. From the next release, that key's feedback shows as from a known contributor.
4. **Feedback from any page.** A Feedback tab in the pane: the page and version are filled in; a kind (something wrong, unclear, missing, an idea, good); the text; a screenshot (pick a file, or capture this screen, scaled down in the browser). It is signed with the person's key over its canonical bytes, encrypted to the collaborators key, and posted to the lane. Without a key, the tab says how to get one: ask the editor by email or WhatsApp, as /collaborators/ says.
5. **Draining verifies.** `collaborators_drain.py` checks every signature with `sgit pki verify` against the bundle the message carries, and marks each row `signed by an enrolled key`, `signed by an unknown key` or `unsigned`. Screenshots are saved next to the row. Nothing reaches the site; the conductor turns feedback into board items, and a feedback desk agent can take this over.

### Phase 2: the editor's review queue

6. **`/review/`**, for a key with the role editor (and later the team): every page and section that is new or changed since the reviewer last looked, from the section ledger, one at a time, sized for an iPad: the page, then Next, Good, Needs work, a comment. Each decision is signed feedback of kind `review`, so the conductor reads the editor's reviews from the same lane. Where the reviewer has got to is kept in this browser and in their vault.
7. **The conductor's queue**, the same view of what the agents are about to publish: the branches waiting for dev@, so the editor reviews before the release, not after.

## What it cannot do, said up front

- A key in one browser is that device's key: a second device is a second invitation. Moving a key between devices, and linking it to the person's record on pki.sgit.ai, is later.
- The invitation code is a bearer credential until it is used: whoever sees the QR code can enrol with it. Send it to one person; each code enrols at most three devices and expires in fourteen days.
- Signing proves which key wrote a message, not who holds it: that is what the editor's enrolment adds, and only as far as the person he sent the code to.
- The lane is public, so anyone can still post unsigned rows; they are kept and marked unsigned.
- The site only shows fingerprints and handles, never a name, unless the person agreed.

## Deliverables (phase 1)

- `/join/` and `assets/feedback/identity.js` (keys, signing, the envelope, the lane), `assets/feedback/join.js`, the Feedback tab (`assets/feedback/pane.js`, loaded by the pane).
- `data/contributors.json` (open invitations as hashes, enrolled keys), `admin/build/invite.py`, the drain's verification.
- Tested end to end in Chromium: an invitation made, joined, enrolled, feedback with a screenshot sent, drained and verified with `sgit pki verify`.
