# Source: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Amazon (CJ Moses, AWS Security Blog): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

**Amazon (CJ Moses, AWS Security Blog)** · [https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) · published 2026-10-21 · added by `claude-story-site` · slug `aws-security-blog-madpot`

Primary account of the 17 October honeypot attempt and the 02:00 UTC proof-of-concept attempts; 'PHP2Shell is now being broadly exploited in the wild'.

## What it says, as the collector read it

#### Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

Captured by claude-story-site. Status: captured. Primary account of the 17 October honeypot attempt and the 02:00 UTC proof-of-concept attempts; 'PHP2Shell is now being broadly exploited in the wild'.

- By CJ Moses, 21 Oct 2026. Verbatim: 'identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure'; 'originated from an IP address associated with a commercial anonymization network'; 'it remains unclear how the actor acquired exploit information prior to disclosure'.

- 'multiple proof of concept exploits for the vulnerability, with the earliest around 2026-10-21 0200 UTC'; attempts 02:00 to 08:00 UTC from additional anonymised infrastructure, 'multiple actors'; 'it's unclear if any of these attempts would have succeeded in real-world systems'.

- After release: 'PHP2Shell is now being broadly exploited in the wild.' No counts.

- Advice: investigate from 17 October; detections that do not rely on a CVE signature; consider blocking multipart uploads where you cannot patch.

- A reader comment complains AWS managed distributions lacked packages for 10 hours (unverified).

## Claims that cite it

| Claim | Who says it | Status | Primary | Sources |
|---|---|---|---|---|
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims. [fact timeline →](../../facts/amazon-honeypot/index.html) | Amazon (CJ Moses, AWS Security Blog) | reported | 1/2 | [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| No named organisation has confirmed a compromise through php2shellA negative finding as of the latest capture. Amazon says 'broadly exploited' against sensors; Weird Gloop expects old forums to have been hit; CISA has not listed either CVE. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source | confirmed | 5/5 | [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |

### Exploitation signals from this source
- [2026-10-17](../../exploitation/index.html): One exploit attempt against a MadPot honeypot from a commercial anonymisation network, four days before disclosure; 'it remains unclear how the actor acquired e

## The bytes
capture 20261022T111755Z · HTTP 200 · https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/- `headers.json` cd2b6b91c536e98366aa450fc499555f4c46f1fc50e52b619d41fdd8156f7621 961 bytes
- `page.html` 94afa0f2233266fa0310186f90425778563bae6747ca3cf284d7d176d5339c8b 1,407,726 bytes
- `provenance.json` 0d0fa2b45ba63031f0e80fc3fdf09aaa336dc7d1bb31664221072c5be8924343 1,223 bytes
- `rendered.html` 5e11969294ad2dba28416a6f535b5e0674e071861c00efcd5c7b6dbecd42ee92 1,473,573 bytes
- `screenshot.png` 838da55574a9351f12a7a7ef936be739360c2221877d6e744c1ec445ad70a84a 688,402 bytes
- `text.txt` 94315ded6e1175f290a4a7cac71ba39dcf18ada7232367f66c34e1decfb08c7d 8,561 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.4.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/sources/aws-security-blog-madpot/index.html
