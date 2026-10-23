# Fact: Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWik

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · technical · reported

# Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS

**Who says it:** Calif; Wiz for WordPress and Drupal · **Sources:** [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)

Two researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded.

## Fact-check

**A2** Reported●●○○○○ · State · verdict: **holds**

Calif's own post lists all eleven applications as confirmed pre-auth RCE; Wiz independently confirms WordPress, Drupal and Joomla. The full list rests on one named party (A2); WordPress/Drupal/Joomla alone would be A4. No third-party reproduction in the vault (Huntress says it did not reproduce), so 'reported' fits.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [calif-php2shell](../../sources/calif-php2shell/index.html) | carries | *We confirmed pre-auth RCE on the following PHP apps as well as arbitrary PHP scripts in some instances.* | 23afef81971778f9 |
| [wiz-blog-php2shell](../../sources/wiz-blog-php2shell/index.html) | partial | *demonstrated that it could execute code remotely without authentication on deployments of WordPress (wordpress:latest), Drupal (drupal:latest), and Joomla (joomla:latest)* | e3568b6f88c93f6b |
| [huntress-php2shell-rapid-response](../../sources/huntress-php2shell-rapid-response/index.html) | absent | *We have not built or reproduced a proof of concept for these vulnerabilities* | a83d744768109a61 |

Open tickets: [Finding-116](../../factcheck/index.html#Finding-116).

Graded in Run-1, resting on captures up to 2026-10-22 08:10 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Calif publishes [php2shell by Calif Research — A tale of two PHP remote vulnerabilities](../../sources/calif-php2shell/index.html)
- 2026-10-21Wiz publishes [PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](../../sources/wiz-blog-php2shell/index.html)
- 2026-10-22 08:10 UTCSaved into the evidence vault: Calif
- 2026-10-22 08:10 UTCSaved into the evidence vault: Wiz
- 2026-10-22Enters this site as reported in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#wordpress-drupal).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · reported
```
Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS
Who says it: Calif; Wiz for WordPress and Drupal
Status: reported
Topic: technical
Sources: calif-php2shell, wiz-blog-php2shell
```


---
site v0.10.5 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/facts/wordpress-drupal/index.html
