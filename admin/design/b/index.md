# Mockup B: the front page for a security lead, Standard view

A three-column working view for a security lead: their reading path and the site by task on the left, what changed since the last visit and the next three actions in the middle, and the state of the evidence as charts on the right.

> Mockup B for review, built from the data of release v0.14.2. Not the live site.

S 
 Sam 
Security lead 

Your reading path 

2 of 5 read · next: Exploitation signals 
 Today 9 new What to do The incident Detection and defence The agencies 16 Every claim 70 Ask 

Since your last visit · 23 October 2026, 16:04 UTC 

## 9 things are new, 3 changed. Two matter for your runbook.

Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when. 

### Your next three actions
 The whole playbook 

1 

#### Patch internet-facing first

mod_php, then FPM, then the rest. Restart every worker; rebuild every image. 

2 

#### Bound the known paths

session.upload_progress off, low post_max_size, fatal_error_backtraces off on 8.5. None of these is a fix. 

3 

#### Watch the process tree

Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing. 

### What changed

 All Facts Timeline Questions Stories 

 New question v0.12.1 
#### Is PHP really the software behind most websites?

✓ 

 New front v0.12.1 
#### Front page: what nobody knows yet

✓ 

 New front v0.12.1 
#### Front page: right now

✓ 

 New front v0.12.1 
#### Front page: at a glance

✓ 

 Changed front v0.12.1 
#### Front page: the core facts

✓ 

 Changed fact reported v0.12.1 
#### In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS

 Calif Wiz 
✓ 

 Changed fact reported v0.12.1 
#### PHP is used by almost 70% of websites whose server-side language is known

 Cloudflare OpenAI on X Wiz 
✓ 

 Changed fact unverified v0.12.1 
#### 70% of the Internet is affected

 Wiz Wiz on X BBC News 
✓ 

 Changed fact reported v0.12.1 
#### VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, of the 2.58 million hosts it saw, could read a version on 1.58 million, and 1.57 million of those wer

 THN SecurityWeek 
✓ 

Marked read, an item fades and then leaves this list; it comes back only if what it says changes. 

#### How sure are we?

- 19 confirmed 
- 36 reported 
- 8 disputed 
- 3 contradicted 
- 4 unverified 

#### Events per day, October

 12 17 18 19 20 21 22 
Red: from the leak on 20 October. 

#### Exploitation signals

- 2026-10-17 
Amazon: One exploit attempt against a MadPot honeypot from a commercial anonymisation network, fou 
- 2026-10-17 
Amazon: One exploit attempt against a MadPot honeypot from an IP on a commercial anonymisation net 
- 2026-10-20 to 21 
Cloudflare: 'We observed attack traffic targeting our customers' after the leak, and attackers 'mutati 
- 2026-10-21T02:00Z 
Amazon: Proof-of-concept attempts begin, then six hours of attempts from anonymised infrastructure 
 0 confirmed compromises 

#### Fixed in

 8.5.12 8.4.27 8.3.36 8.2.35 
8.1 and older: source backports only.

---
site v0.14.2 · https://php.oct.2026.newsroom.sgit.ai/admin/design/b/index.html
