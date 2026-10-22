# Source: Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Huntress: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

**Huntress** · [https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities) · published 2026-10-21 · added by `claude-story-site` · slug `huntress-php2shell-rapid-response`

As of 16:30 ET (20:30 UTC) 21 Oct: no exploitation observed on partner systems; no PoC built or reproduced; not aware of public exploit code.

## What it says, as the collector read it

#### Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

Captured by claude-story-site. Status: captured. As of 16:30 ET (20:30 UTC) 21 Oct: no exploitation observed on partner systems; no PoC built or reproduced; not aware of public exploit code.

- Primary negative finding from a managed-detection vendor.

## Claims that cite it

| Claim | Who says it | Status | Primary | Sources |
|---|---|---|---|---|
| No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code known to Huntress [fact timeline →](../../facts/huntress-none/index.html) | Huntress | reported | 1/1 | [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |
| No named organisation has confirmed a compromise through php2shellA negative finding as of the latest capture. Amazon says 'broadly exploited' against sensors; Weird Gloop expects old forums to have been hit; CISA has not listed either CVE. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source | confirmed | 5/5 | [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
| None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200The Hacker News says the same of the public code. Fastly: working RCE needs knowledge of the running binary's layout on x86_64. [fact timeline →](../../facts/pocs-wrong/index.html) | rjmendez (detection author) citing VulnCheck; Huntress | reported | 1/2 | [rjmendez, GitHub](../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |
| 2026-10-21 20:30 UTC | Huntress: no exploitation observed on partner systems (16:30 ET). | stated |

### Exploitation signals from this source
- [2026-10-21 20:30 UTC](../../exploitation/index.html): No exploitation observed on partner systems; no public exploit code known.

## The bytes
capture 20261022T112853Z · HTTP 200 · https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities- `headers.json` 39dd8f8ed13d1e993a95f88bddf69702d0cd23e3aef38da50d65068f495d1cff 7,379 bytes
- `page.html` 39d79180c85ccbc63f3acbf3bb0f076d56933f94e5fa8a5be8dafc3ca3160c7a 913,455 bytes
- `provenance.json` 23031a4937921ef79d80fb4b2546b9d7054028e640b9babec2c44d9f66dee0a2 1,102 bytes
- `rendered.html` 41e5af59038a7155953c6809d743ca579e2eeb7cdc503f13f6e3550ea920d970 1,115,188 bytes
- `screenshot.png` a4d89c5787921c4fe23ea13f25dc2d0104756a669450c44aad83ad220d9bc3a7 1,862,920 bytes
- `text.txt` a83d744768109a61f623c0d4de5df589cde5c1e0da114b25d62a7321f159455c 17,843 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.5.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/sources/huntress-php2shell-rapid-response/index.html
