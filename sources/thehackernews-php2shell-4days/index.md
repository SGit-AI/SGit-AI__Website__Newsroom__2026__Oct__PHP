# Source: Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The Hacker News (Ravie Lakshmanan): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed

**The Hacker News (Ravie Lakshmanan)** · [https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html](https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html) · published 2026-10-22 · added by `collector-researchers` · slug `thehackernews-php2shell-4days`

Dated Oct 22, 2026. Quotes Amazon CISO CJ Moses ('post shared with The Hacker News'): MadPot honeypot exploit attempt Oct 17 2026 from anonymization network IP geolocated to Australia; PoC attempts from ~02:00 UTC Oct 21. Says 'details about the CVE identifiers and a proof-of-concept (PoC) exploit leaked ahead of time' — contrast PHP Foundation 'No technical details leaked'. VulnCheck: PHP on 2,608,039 internet-facing hosts.

## What it says, as the collector read it

#### The Hacker News: Amazon saw a PHP2Shell exploit attempt 4 days before disclosure

- Ravie Lakshmanan, Oct 22, 2026. Captured 08:13:20Z.

- CJ Moses (CISO, Amazon Integrated Security), "in a post shared with The Hacker News": "The exploit attempt originated from an IP address associated with a commercial anonymization network ... While the vulnerability was under embargo, the targeting of a honeypot from an anonymized IP address suggests the activity was conducted by a threat actor, though it remains unclear how the actor acquired exploit information prior to disclosure." Date Oct 17, 2026, MadPot; IP geolocated to Australia (IOC omitted here).

- Amazon: PoC attempts from ~02:00 UTC Oct 21, then six hours of attempts from anonymised infrastructure; "multiple threat actors".

- ELLIO: first sensor hit Oct 21 08:36 UTC.

- Leak wording differs: THN says "details about the CVE identifiers and a proof-of-concept (PoC) exploit leaked ahead of time"; PHP Foundation said "No technical details leaked" (with the CVE IDs), the video came later.

- Size: VulnCheck counts PHP on 2,608,039 internet-facing hosts — a far smaller, host-based number than "70% of websites" or "30 million websites".

- Primary AWS post not yet found (THN does not link one). The AWS Security Blog post is still to be located.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, of the 2.58 million hosts it saw, could read a version on 1.58 million, and 1.57 million of those were unpatched on 21 OctoberCensys: 2.58 million hosts seen, 1.58 million reporting a version, 1.57 million not patched; nearly 3 million by 22 October. VirusTotal: 5.1 million IPs running PHP, 1.1 million announcing a version. Unit 42: 22.6 million systems that 'could be vulnerable' (via Insurance Business). Censys's own post was not found. [fact timeline →](../../facts/scale-2.6m-hosts/index.html) | VulnCheck and Censys, via The Hacker News and SecurityWeek | reported | **A2** Reported●●○○○○ | 0/2 | [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) |
| Frontier AI found the flaw ahead of attackers, giving defenders time to prepareAmazon reports an exploit attempt against a honeypot on 17 October, four days before disclosure, from an actor whose source of exploit information is unknown. [fact timeline →](../../facts/ahead-of-attackers/index.html) | OpenAI | disputed | **A2** Reported●●○○○○ opinion disputed | 1/2 | [OpenAI on X](../../sources/x-openai-php2shell/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims. [fact timeline →](../../facts/amazon-honeypot/index.html) | Amazon (CJ Moses, AWS Security Blog) | reported | **A2** Reported●●○○○○ superseded | 1/2 | [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-17 | An exploit attempt from an anonymisation-network IP hits an Amazon MadPot honeypot. | stated |
| 2026-10-21 02:00 UTC | Amazon sees proof-of-concept attempts, then six hours of attempts from anonymised infrastructure. | stated |
| 2026-10-21 08:36 UTC | ELLIO records its first sensor hit. | stated |
| 2026-10-22 | The Hacker News publishes Amazon's account of the 17 October honeypot attempt and VulnCheck's count of 2,608,039 hosts. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 2,608,039 | internet-facing hosts running PHP | reported |
| 4 days | before disclosure, an exploit attempt hit an Amazon honeypot | reported |

### Exploitation signals from this source
- [2026-10-17](../../exploitation/index.html): One exploit attempt against a MadPot honeypot from an IP on a commercial anonymisation network, geolocated to Australia, four days before disclosure. 'It remain
- [2026-10-21 02:00 UTC](../../exploitation/index.html): Proof-of-concept attempts begin, then six hours of attempts from anonymised infrastructure; 'multiple threat actors'.
- [2026-10-21 08:36 UTC](../../exploitation/index.html): First sensor hit, about 55 minutes after Chainguard's images.
- [2026-10-22](../../exploitation/index.html): Amazon and Cloudflare saw sites being probed for the flaw.

## The bytes
capture 20261022T081320Z · HTTP 200 · https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html- `headers.json` 54c094189f50f4afa3962d0e484ef93cf0f92bd1fefb71ae2fec7e63b71b3b14 783 bytes
- `page.html` b2b51b3736eab8ebf9fb584770654a563ec0cde9a258c8ccc9b2cac5e2759495 181,180 bytes
- `provenance.json` ef03914e372ab683b87cf258b84ec703ba5cc140e8b724fe1fa547d0f7a066fe 1,081 bytes
- `rendered.html` a7caeb00fddc406d6dcfeb68c7fdce453fdb39446eb83daa364cb3f2986a7834 176,478 bytes
- `screenshot.png` 71b28408de124895b1534822f79eff33a445be5296c09203d51f152ef67d089c 2,255,956 bytes
- `text.txt` c1cb63141287484c7b96b6f842f983bb978a108b3b82eebb95ebe78c4ed608f4 12,295 bytes
capture 20261023T160435Z · HTTP 200 · https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html- `headers.json` 421a40b8b01bedb96dc2f965ab732985b9acdfe566cb1046ac4522f6b5ce82a7 854 bytes
- `page.html` ef230d20b5059df376ebaca22a0031d7d1cb8b1bde9736da35073b93c319a3d7 186,319 bytes
- `provenance.json` 30680a19ac8a0b6c34a81631234187928f82c134b8a42f79dc7534efcd056463 1,839 bytes
- `rendered.html` 1426a64bb1181ef901405314bec3c221608a0d215a92c84dedf3b88febfc4896 183,052 bytes
- `screenshot.jpg` 139266d86df524fb02573a64129c85fa1e62866024c1aad8ffae1af2f86ae158 742,596 bytes
- `text.txt` 0c31fcebda310760b15f83418566d5bd2e63ebaffa0b93669443fb6f970efe31 12,859 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/thehackernews-php2shell-4days/index.html
