# Source: GitHub - rjmendez/phpup-2026: IOCs and detection rules for CVE-2026-109618 / CVE-2026-109619 (PHP session.upload_progress UAF) · GitHub

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

rjmendez, GitHub: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · secondary · captured

# GitHub - rjmendez/phpup-2026: IOCs and detection rules for CVE-2026-109618 / CVE-2026-109619 (PHP session.upload_progress UAF) · GitHub

**rjmendez, GitHub** · [https://github.com/rjmendez/phpup-2026](https://github.com/rjmendez/phpup-2026) · published 2026-10-21 · added by `claude-story-site` · slug `github-rjmendez-phpup-2026`

Detection rules rewritten on 21 Oct after a lab reproduction showed the leaked PoC's mechanism did not match the fix; cites VulnCheck: none of the public PoCs has the correct mechanism.

## What it says, as the collector read it

#### GitHub - rjmendez/phpup-2026: IOCs and detection rules for CVE-2026-109618 / CVE-2026-109619 (PHP session.upload_progress UAF) · GitHub

Captured by claude-story-site. Status: captured. Detection rules rewritten on 21 Oct after a lab reproduction showed the leaked PoC's mechanism did not match the fix; cites VulnCheck: none of the public PoCs has the correct mechanism.

- '2026-10-21 rewrite. This repo previously described a single-request, multipart-stall heap-spray mechanism ... derived from the leaked PoC artifact's own claims ... That mechanism is deleted, not caveated - it doesn't match the real fix, a real lab reproduction of its precondition produced a clean 200 OK, and VulnCheck independently reports that none of the public PoCs they reviewed have the correct mechanism.'

- Names the fix commit as 82f8f31b16a (a different hash from the 3584a98bd this site found on PHP-8.5; likely the PHP-8.2 commit or a cherry-pick; not reconciled).

- Suricata SIDs 9109627, 9109633, 9109637 active; others retired. 'the cross-request same worker requirement is not visible from any standard web/WAF/MDE log source'.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200The Hacker News says the same of the public code. Fastly: working RCE needs knowledge of the running binary's layout on x86_64. [fact timeline →](../../facts/pocs-wrong/index.html) | rjmendez (detection author) citing VulnCheck; Huntress | reported | **A1** Weak signal●○○○○○ status overstated | 1/2 | [rjmendez, GitHub](../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T112003Z · HTTP 200 · https://github.com/rjmendez/phpup-2026- `headers.json` 582bbe71ccaa5a3323db8d3d2caec68f5af4561fd8b8b29bd932cbea2126e5cf 5,445 bytes
- `page.html` e7e78dc79587fcaf7eac2ce0b48d90575d55f6fdb4313b768f0637f7a5d8ff0c 275,240 bytes
- `provenance.json` 7500ba6175c9e2f09a379b74a283542b6e7e4e637714a2006f0e68a86c44b348 1,048 bytes
- `rendered.html` 7bb4a810ad56f4620b7e1f2b14591c31b935a76a017c72cae93435ef05b8d088 302,107 bytes
- `screenshot.png` a69607bd90cb0667ecdd5ab2e0191ae6c1534b599824084514dbcc1055712cde 940,580 bytes
- `text.txt` 84742b6e86fb259d4db36361e86d4b739c6cd09184337f365f5e2958271f5379 9,221 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-rjmendez-phpup-2026/index.html
