# Every source: 144 pages, 137 captures, 857 hashes

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The manifest of the php2shell evidence vault: every captured source with its publisher, kind, publication time, capture times, HTTP status and the SHA-256 of every captured file.

# Every source, every capture, every hash

In plain English Every web page this site relied on, with the time it was saved and a fingerprint proving it has not been altered since.

144 sources, 73 of them primary, 137 dated captures and 857 hashed files, from the evidence vault at commit `200d08971937`. 10 sources could not be read because the site blocked an automated browser; the block, with the challenge page's hash, is the record. The captures are third-party pages held privately and are not republished; this page links to the originals and lists the SHA-256 of every captured file, so that anyone the vault is later opened to can check that the bytes are the ones the agents saw, at the minute they saw them.

| Kind | Sources |
|---|---|
| news | 29 |
| advisory | 25 |
| vendor | 22 |
| cve | 14 |
| government | 13 |
| researcher | 11 |
| code | 9 |
| other | 9 |
| social | 9 |
| forum | 2 |
| news-live | 1 |

Each capture holds `page.html` (as served), `rendered.html` (after scripts ran), `text.txt`, `screenshot.png`, `headers.json` and `provenance.json`. A `raw/` folder holds anything fetched another way, with its own checksum file. The manifest this page is built from is [data/sources.json](../data/sources.json).

### [PHP2Shell: sanate vulnerabilità critiche in PHP (AL07/261021/CSIRT-ITA)](acn-it-php2shell/index.html) [original ↗](https://www.acn.gov.it/portale/w/php2shell-sanate-vulnerabilita-critiche-in-php)

**ACN / CSIRT Italia** · advisory · secondary · captured · published 2026-10-21 · added by `collector-gov` · `acn-it-php2shell`

Alert AL07/261021/CSIRT-ITA, published 21-10-2026. CVSS v4.0 9.2 each (Use After Free). Mitigation: only 'aggiornare i prodotti vulnerabili' (update); it gives no offline advice.

capture 20261022T081354Z · HTTP 200 · https://www.acn.gov.it/portale/w/php2shell-sanate-vulnerabilita-critiche-in-php- `headers.json` c44211ff9b8440ef6922919056abed0873179324fdf7db7ddf969c8d1dd6bd15 732 bytes
- `page.html` 6ab511ebb1dd7a3d6235d88dc71a02c8ecefec27283538cec68a134d33d67440 118,598 bytes
- `provenance.json` b832861c53d09b3d98083bc23e3c4578748f1f8173e2ea7c23bd8c9dfa6f1c8b 1,038 bytes
- `rendered.html` 91c9550654c551eeacb33e829fe2246a7307efbcf7cd00d4cf10f5a44413cf07 131,205 bytes
- `screenshot.png` 94246ab38f323d629edf5c1820908d804f7f45f61bc276e7c77e756aa549fc65 687,162 bytes
- `text.txt` 19fac2edc25161cd867bda0ea1c8bf8b6ce7625fbdd1e9a9a7cd41bdd8d1bef6 6,137 bytes

### [Critical vulnerabilities in PHP](acsc-alert-php/index.html) [original ↗](https://www.cyber.gov.au/alert/critical-vulnerabilities-in-php)

**ASD's ACSC (Australia)** · advisory · primary · captured · published 2026-10-21 (Published); Last reviewed 2026-10-22 · added by `collector-gov` · `acsc-alert-php`

Alert Status: Critical. Published 21 Oct 2026, last reviewed 22 Oct 2026. 'Recent update': identify PHP, review php.net, apply updates and mitigations, monitor. NO offline advice. 'not aware of successful active exploitation within Australia'. Says full details were announced 'Thursday 22 October 2026 at 0100 AEDT' (=21 Oct 14:00Z). The body text is stale (pre-patch).

capture 20261022T081658Z · HTTP 200 · https://www.cyber.gov.au/alert/critical-vulnerabilities-in-php- `headers.json` 3f7c0fe9c702d22193630225a56b0991c08fc52fb05ef53f26ea0f611b798b4e 1,985 bytes
- `page.html` 650742fe93abb6dec911f58d21b7cd6d8d82c2d4a7b89eb9745e9a9857bc0c72 1,541,271 bytes
- `provenance.json` 37ce725a8459c6db87ef8d7e3abd3cf92d350bab9e4228852c7d07dd08d65a6f 985 bytes
- `rendered.html` 731eef8ce851ccf1650bc66cf3bb8658569c3de13b3a8084c14761658743e931 1,557,700 bytes
- `screenshot.png` 39318847477c383a130dbafc83210dc27ed7ccae88107979ed124e372d67da9d 345,966 bytes
- `text.txt` 9370af142ded6de9a44fed4330585d677fde367d90d33ce355e9ebe6a75f7d56 6,299 bytes

### [cyber.gov.au home](acsc-home/index.html) [original ↗](https://www.cyber.gov.au/)

**ASD's ACSC** · government · secondary · captured · published not stated · added by `collector-gov` · `acsc-home`

Home at 08:16Z: the PHP alert teaser is dated 22 Oct 2026 with the stale pre-disclosure blurb.

capture 20261022T081604Z · HTTP 200 · https://www.cyber.gov.au/- `headers.json` 3d448cbb053930039edd6bcb6779264beb2fa8c4c073bc5084ca3a5b0c369a5f 1,937 bytes
- `page.html` bd81a8f884e1cbe1f2ae88c146b6198346568f2324677adce3198b5578db19c3 1,854,064 bytes
- `provenance.json` 992e9c6ce0b26d2edb42343e569ac2634e532a277a5e804ec657ed66acda47a9 879 bytes
- `rendered.html` e22b8af8cb588bdf894c62c53337db8940108a269e2f517f1d6ffa1886d8d904 1,889,870 bytes
- `screenshot.png` 3f7acad6a96208dca53692a35f83a89e3b21e8266fcd183892673c6e4b3b39b0 723,009 bytes
- `text.txt` b7198501ad800f9312359edf414e81c46b1b35f7d0fae787ff629a8f029ad0b9 13,389 bytes

### [PHP flaws: France's ANSSI orders sites offline](actuia-anssi-sites-offline/index.html) [original ↗](https://www.actuia.com/en/news/php-flaws-frances-anssi-orders-sites-offline-after-ai-assisted-discovery/)

**ActuIA** · news · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `actuia-anssi-sites-offline`

Secondary: 'France's ANSSI orders sites offline'; compare CERT-FR's own wording (isolate, then migrate).

capture 20261022T112454Z · HTTP 200 · https://www.actuia.com/en/news/php-flaws-frances-anssi-orders-sites-offline-after-ai-assisted-discovery/- `headers.json` ee48005ae8388bf72bebfeea8f3d95100abf6faae001e3c235a5506d2f6dc21e 473 bytes
- `page.html` ff30fd43654cd08a1f693e8d4d915c41820729be9a1991d5f4e462d1d0bb22f4 116,023 bytes
- `provenance.json` e9c5fc723d72d43ad18613c74102fa5d72fc2799e91e0f81c2cfbfd51a52d794 1,090 bytes
- `rendered.html` 74e68194027420a7a98f41f234f8da46f93ff0e5c77fec86c07d115f15365688 122,914 bytes
- `screenshot.png` f934a67b32d8386b43d01a1a9baece42d7406c36ed9bec407ef19f9a26d73475 1,673,964 bytes
- `text.txt` 8f399970329ffcead878dced88dbb206b9677895965091d0efb60334becc9f9a 10,744 bytes

### [CVE-2024-4577 Exploits in the Wild One Day After Disclosure](akamai-blog-cve-2024-4577-one-day/index.html) [original ↗](https://www.akamai.com/blog/security-research/2024-php-exploit-cve-one-day-after-disclosure)

**Akamai Security Research** · vendor · primary · captured · published 2024 · added by `claude-story-site` · `akamai-blog-cve-2024-4577-one-day`

Historical: exploits of the previous PHP core RCE, CVE-2024-4577, seen in the wild one day after disclosure.

capture 20261022T112501Z · HTTP 200 · https://www.akamai.com/blog/security-research/2024-php-exploit-cve-one-day-after-disclosure- `headers.json` b8600b926f54d0c326ae453a4aa45ee026728ff7329884997710f9d1e5f541cb 5,460 bytes
- `page.html` 10bed4c03e0d208afa3e6d6d67c8d2250149138bb4d63e87605d1e28079a5171 279,021 bytes
- `provenance.json` 67c5b82965151100b965313d300e89e4bd9ca9ce8520a47fa8ba174bd637833b 1,084 bytes
- `rendered.html` 3aea0cbcf996a4c4d7b0dfe721b61fee812595d5df395a7b8eb1317ca7c0fa8f 478,692 bytes
- `screenshot.png` 5fed6383355ce8c109b539a7e534592d29b584d533df10d4b2228cd9c2431475 2,944,679 bytes
- `text.txt` f7a58be0ecaaa8db0b45cf79431fcc8609cd27f52b20baefafb80d760164e567 23,021 bytes

### [Critical Remote Code Execution Vulnerabilities in PHP Core | Akamai](akamai-blog-php-core-rce/index.html) [original ↗](https://www.akamai.com/blog/security-research/critical-remote-code-execution-vulnerabilities-php-core)

**Akamai Security Research** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `akamai-blog-php-core-rce`

Adaptive Security Engine rule 3000991 v1 'PHP Remote Code Execution Attack Detected' for both CVEs; existing command-injection rules also blocking weaponised payloads; 'prompt application of vendor patches' is the most effective defence.

capture 20261022T112525Z · HTTP 200 · https://www.akamai.com/blog/security-research/critical-remote-code-execution-vulnerabilities-php-core- `headers.json` 3ed908175f73e8f392f99df0845982f172ad44c49cb12692c16c1fcf7849d28d 5,850 bytes
- `page.html` 8f9e02a272dd67f8a2770e849f8f8118fc34e45f1cd056fd56e4b5a7f9bae592 213,450 bytes
- `provenance.json` c335fab9c5745922bf97664aa64c00fa23b563ae875eeb2c95316f70f3ae758d 1,103 bytes
- `rendered.html` 0400fefe0ed144f5140e8077e5e6d9b401d41cad7ef0b66825c4dec6663f4b33 415,118 bytes
- `screenshot.png` 5757611708b507626fda25038e770bb96adb831e42b474d6c5229c30ba0a3a98 609,040 bytes
- `text.txt` 2a001600cd450bc582ed42e8355951626ef8ae60e5c4afe233629dbeeaacba5b 5,509 bytes

### [Finding, Prioritizing, and Patching PHP2Shell Exposure | Arctic Wolf](arcticwolf-php2shell-exposure/index.html) [original ↗](https://arcticwolf.com/resources/blog/arctic-wolf-labs-finding-prioritizing-and-patching-php2shell-exposure/)

**Arctic Wolf Labs** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `arcticwolf-php2shell-exposure`

Vendor guidance on finding and patching exposure.

capture 20261022T112342Z · HTTP 200 · https://arcticwolf.com/resources/blog/arctic-wolf-labs-finding-prioritizing-and-patching-php2shell-exposure/- `headers.json` cb2dc7b843210683b8616d4f651fe7942a43433cea11e494ec0adb084f793b82 1,052 bytes
- `page.html` 62b3d068fbefbb9b312c2418b4a38ef788132d55782e1e41244e77c0bad59726 351,404 bytes
- `provenance.json` 015cfc5316cc7077049a8aee5da1a198699d54f7244e62ab8f7bf89b9e5ac590 1,123 bytes
- `rendered.html` 1f059cea13ae6b9fa434e23a67c3e8ec05c47fa9af94ac9c5a476013862adb78 1,342,610 bytes
- `screenshot.png` 0f1c79ead2d73038424318bb8efbe497717653cc82a2b3763f24ce7a95386336 1,555,808 bytes
- `text.txt` ef2210c0fd1c35032d70283c91ab44c01c091342c21c9ac55571b12b45f8f75b 10,879 bytes

### [Just a moment...](armis-php2shell-find-patch/index.html) [original ↗](https://www.armis.com/blog/php2shell-how-to-find-prioritize-and-patch-affected-systems/)

**Armis** · vendor · secondary · blocked · published 2026-10-21 · added by `claude-story-site` · `armis-php2shell-find-patch`

Vendor guidance on finding and patching.

capture 20261022T112544Z · HTTP 403 · https://www.armis.com/blog/php2shell-how-to-find-prioritize-and-patch-affected-systems/- `headers.json` beaea17cfe605c6045c7491c7d444b6fc828d614e9fbacea1cc080a269cc4c31 1,990 bytes
- `page.html` f8ff0c9e277962b98d66e9cf2027f78e3bfbc4d17999419d62b105822a78c6ba 6,399 bytes
- `provenance.json` 0cdaf4cb11738a799892b7d79d673ed08c085634e8be431b89fd732adde39e19 1,026 bytes
- `rendered.html` 64996869be46fe0ae90238d579e23c2599e4293e9f0c15e82d322efe96fde39b 28,992 bytes
- `screenshot.png` 4da50c06b7082cecc3965a33e2fcf67ce4919b97b0730000f14723d2e5ec0321 38,997 bytes
- `text.txt` d15eed6dfa57239bfe3d8333949627f35d8011042027db230828460dbf2b4ff3 261 bytes

### [Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog](aws-security-blog-madpot/index.html) [original ↗](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/)

**Amazon (CJ Moses, AWS Security Blog)** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `aws-security-blog-madpot`

Primary account of the 17 October honeypot attempt and the 02:00 UTC proof-of-concept attempts; 'PHP2Shell is now being broadly exploited in the wild'.

capture 20261022T111755Z · HTTP 200 · https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/- `headers.json` cd2b6b91c536e98366aa450fc499555f4c46f1fc50e52b619d41fdd8156f7621 961 bytes
- `page.html` 94afa0f2233266fa0310186f90425778563bae6747ca3cf284d7d176d5339c8b 1,407,726 bytes
- `provenance.json` 0d0fa2b45ba63031f0e80fc3fdf09aaa336dc7d1bb31664221072c5be8924343 1,223 bytes
- `rendered.html` 5e11969294ad2dba28416a6f535b5e0674e071861c00efcd5c7b6dbecd42ee92 1,473,573 bytes
- `screenshot.png` 838da55574a9351f12a7a7ef936be739360c2221877d6e744c1ec445ad70a84a 688,402 bytes
- `text.txt` 94315ded6e1175f290a4a7cac71ba39dcf18ada7232367f66c34e1decfb08c7d 8,561 bytes

### [PHP: Global scramble to fix critical cyber-security flaws as many websites taken offline - follow live](bbc-live-ckgel5xp2xv9t/index.html) [original ↗](https://www.bbc.co.uk/news/live/ckgel5xp2xv9t)

**BBC News** · news-live · secondary · captured · published 2026-10-22T06:16:24Z · added by `claude-newsroom-lead` · `bbc-live-ckgel5xp2xv9t`

Live page; bbc.co.uk redirects to bbc.com. raw/ holds a curl copy at 07:55Z and its __INITIAL_DATA__. Captures 080453Z and 080526Z have no raw body (the tool's first fallback was blocked by egress); 080559Z is complete. Edited by Kieran Kelly and Imogen James.

capture 20261022T080453Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` 6f92f9cc2df7e178c6a5480cde0a0d07eaa057374c17573ed0539cd2ec5e4f76 5,640 bytes
- `page.html` dc9a4c45bac2ffecb6c3904ab17c14f29288f0928f0247acd449f62d0b715981 24 bytes
- `provenance.json` de7ccc50e0cd85c96d0c814a87e22d61df580452ccc7cc08bec00fe2acb36000 1,094 bytes
- `rendered.html` e9ae7f01673df9b32a99007f255c2106bc6f4179841891af83732ce54cac1bde 500,416 bytes
- `screenshot.png` a466ce380b452e0a851e07db1d769f1ccb1b41391a8bf001b5febe1a6b0a8352 2,737,568 bytes
- `text.txt` df1dbe6b553a8c004f6d950a1d606138f2795062d3225feaa37043d24343bc99 14,389 bytes
capture 20261022T080526Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` d63c60c458f9e0144dfc1ec7336b7e7eb13ac35383008623841bf01030b99175 5,690 bytes
- `page.html` dc9a4c45bac2ffecb6c3904ab17c14f29288f0928f0247acd449f62d0b715981 24 bytes
- `provenance.json` b0b6c73c98d7b9af8e3cea8a007eb2212d89e38f80d8fdcb1c99b32cac545a18 1,094 bytes
- `rendered.html` b42a90b0ed17266eac83cb8bc81fc6e2321285b3b3dd01c15aed55411ec51255 511,866 bytes
- `screenshot.png` 65eb8a2dd5d93f8ef2399b62dd91d4bae200c41997a77ccae9b9388d33c505bf 3,587,122 bytes
- `text.txt` 9ae96265aa96cff67f4da71f5ed410376023b17283d83b617eab7e98d2602738 14,501 bytes
capture 20261022T080559Z · HTTP 200 · https://www.bbc.com/news/live/ckgel5xp2xv9t- `headers.json` adef455045234df0fcb6936e0b86ce89d83c6b68719892c1e08bc498d0704517 5,647 bytes
- `page.html` 50bc0fc20681b834b1a40742cf921b27ceb5356d5ab38b417c7e53513016eefd 501,921 bytes
- `provenance.json` b62c78eb8ac92bd2d3d7bbd6749e8f0c24519b5d2edac76d107af558eaf78d2f 1,092 bytes
- `rendered.html` 8ae9c4bca9c7ff8b5037ffa58536c2b75c45efdee1f851d583a80ac5cd05ff5c 501,515 bytes
- `screenshot.png` f3cf0359a5f9aec2edf5dfa6cd060f55f94aa3c64b90f7e260edec02180a434c 2,685,632 bytes
- `text.txt` c88b8c5f4c6bc07d2ef85b78d0d66482f0322075621abb0631ef4352932aa97d 14,389 bytes
raw, 2 files with SHA256SUMS- `initial-data.json` ee7445a58187bcd67df827007a8100941993a24dc3e7eea7e8a45f723a9e3305
- `page.2026-10-22T0755Z.html` fe32274b64ee109a7e37fc4c26e37e793dc22481a6122888782c393e01102488

### [Bloomberg - Are you a robot?](bloomberg-governments-offline/index.html) [original ↗](https://www.bloomberg.com/news/articles/2026-10-21/governments-take-websites-offline-after-php-security-warnings)

**Bloomberg** · news · secondary · blocked · published 2026-10-21 · added by `claude-story-site` · `bloomberg-governments-offline`

European governments take websites offline; may be paywalled, see capture status.

capture 20261022T112602Z · HTTP 403 · https://www.bloomberg.com/news/articles/2026-10-21/governments-take-websites-offline-after-php-security-warnings- `headers.json` ebbf488d8ec3cb9e82e0b2850092794fa151b40e36e5527483c925bd8bc043c2 1,744 bytes
- `page.html` 42ba14394a9bbfcfd2d92ca9d569ec69f03944659af408f36f57faea50e788d2 13,856 bytes
- `provenance.json` 3c8c1301b67db2b3dbe016f7c0f83861dc5a27d0a02c693c16b232b3a0f0bc56 1,091 bytes
- `rendered.html` cf863d12c016944da5fa0f4a5d5a6b20441810b9d390e4cd795477677e22219c 15,882 bytes
- `screenshot.png` 381a9b176a6f0b8aa7805f9ddb22a7cd17826528afa7a41b24b0015b1c3a355e 78,255 bytes
- `text.txt` a66e04101bddd06c4cc5019d69b57bd2db4ff7d0a6ecdfe0fbd4d6fc5e05b303 665 bytes

### [PHP2Shell: Two Critical PHP Flaws Allow Unauthenticated Remote Code Execution | SECURITY.COM](broadcom-security-php2shell/index.html) [original ↗](https://www.security.com/blog-post/php2shell-critical-vulns-cve-2026-109618-109619)

**Broadcom (Symantec) Security** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `broadcom-security-php2shell`

Vendor explainer.

capture 20261022T112608Z · HTTP 200 · https://www.security.com/blog-post/php2shell-critical-vulns-cve-2026-109618-109619- `headers.json` 90e7e97292b84a9655eb632719cd295101372dea8bfbbea1c37cac21f29c6083 2,018 bytes
- `page.html` ee4999fb83f9cd38b29e33384e6cd904f855429326277bbcaaaa0b5796879cf8 329,468 bytes
- `provenance.json` c676441507e6939f7a352231caebe725dfa363ad55108ae190166cc7123411b0 1,093 bytes
- `rendered.html` 087b78f1dbe37ce2b31dc124b10b31a4009ac15969a40407f65afddb1dff30b7 431,453 bytes
- `screenshot.png` a4a4f3fec342e365df75bcdd5a2b61bac1edb4a1417b9a1200702734cd579cff 2,841,458 bytes
- `text.txt` ade5eb86aa233a2122f483429993bf21453456fc608ee191949dacc2f7e3a260 13,607 bytes

### [php2shell by Calif Research — A tale of two PHP remote vulnerabilities](calif-php2shell/index.html) [original ↗](https://calif.io/php2shell/)

**Calif (Calif Research)** · researcher · primary · captured · published 2026-10-21 · added by `collector-researchers` · `calif-php2shell`

Calif's own write-up by Ryan Austin (@lcfr_hax). Page has no machine timestamp; story panel dated 'Oct 21, 2026'. Embeds two YouTube exploit demo videos (pfWZrdzvooc 'php2shell exploit demonstration', cE4h79AWbT4 'Exploiting Nginx with PHP-FPM'); videos NOT downloaded. Its timeline omits the leaked/deleted video.

capture 20261022T081033Z · HTTP 200 · https://calif.io/php2shell/- `headers.json` 1fc0b2864079499b5911e31166e216c1c753a83da9a65d38086609e84372794e 759 bytes
- `page.html` 9f3df4d68b9d185563f9b5eec4b1e910f296389f54e02b4f6a25fef2573662a3 68,302 bytes
- `provenance.json` c800836bfdf2759a20495415eb65bff17d26b8d9127d0695f7be27870b1dc67b 906 bytes
- `rendered.html` 24e345e4514f5240f94df7537536a5ed14ba6e440cffffae74f8c38c7c8e5644 68,280 bytes
- `screenshot.png` 38990c6ce9af5828a86614d9dff808d621097986d5288e8136bda70412b3ac63 20,097,747 bytes
- `text.txt` 23afef81971778f954d3cefb62c4901814afddd6ae0948c941af3edead40ced4 23,876 bytes

### [AL26-026 - Critical vulnerabilities impacting PHP - CVE-2026-109618 and CVE-2026-109619](cccs-al26-026/index.html) [original ↗](https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619)

**Canadian Centre for Cyber Security (CCCS)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `cccs-al26-026`

Date: October 21, 2026; Date modified 2026-10-21. 'Where immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied.' PoC available; no active exploitation identified. Also AV26-1070 (PHP security advisory), same date.

capture 20261022T081700Z · HTTP 200 · https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619- `headers.json` 0db6dd151e1887553a32a56de4d1f6a133645e87d6dbee931f362e8a21a370f3 583 bytes
- `page.html` 171c897e4a6fde98e73f9d1e221188dae6d0c04b49e8b6a242fba591739a11c9 39,250 bytes
- `provenance.json` 9759aec757d5df865a795a86bf304ffdcc697988c45f47adcc0159a6771a4fa1 1,195 bytes
- `rendered.html` d6536d39602e9709a1afb05fb61fad1b88b57a5d1b839a7f5de58c7f3588300c 149,258 bytes
- `screenshot.png` 9df75da37b7ed8ceb13b241f71f041d29c9f33055750a65070c6c785bbe9cdd2 538,343 bytes
- `text.txt` 9e7f44cc73e21ad54d1caf36c5273a289839c76ff1e1ac35bf377e4645ad91a2 5,403 bytes

### [Alerts and advisories - Canadian Centre for Cyber Security](cccs-alerts/index.html) [original ↗](https://www.cyber.gc.ca/en/alerts-advisories)

**CCCS** · government · secondary · captured · published not stated · added by `collector-gov` · `cccs-alerts`

Listing page at 08:16Z: AL26-026 and AV26-1070 (PHP), both 2026-10-21.

capture 20261022T081604Z · HTTP 200 · https://www.cyber.gc.ca/en/alerts-advisories- `headers.json` 43f213e29f0be568c8c4a231d0404fc7c33db33ea4b6d75c538f505a2a139b88 586 bytes
- `page.html` b7e604271809b8579356f2e76d4be26c44d1aa9a92893b73efa23358036ba52e 21,909,500 bytes
- `provenance.json` bcff9a25cb070bd8554c2d407548464544b8792a9046b93a670f29e70dc5c6ad 1,026 bytes
- `rendered.html` b15a0c243be41ff42e41fd4f94617f75373bce255f915cc57cded297c97ef6a4 50,788,748 bytes
- `screenshot.png` 9029e12095ac74977c8777919e317ffd20cc42da26e60903f1964abddab3774d 494,360 bytes
- `text.txt` c226b8df2f21a14934c6c79d53fae9685707e4adcca0fcf2d7b6143e296b2000 3,812 bytes

### [CCN-CERT AL 11/26: Actualización inmediata de vulnerabilidad crítica en PHP](ccn-cert-al-11-26/index.html) [original ↗](https://www.ccn-cert.cni.es/es/seguridad-al-dia/alertas-ccn-cert/13200-ccn-cert-al-11-26-actualizacion-inmediata-de-vulnerabilidad-critica-en-php.html)

**CCN-CERT (Spain)** · advisory · primary · blocked · published not stated · added by `collector-gov` · `ccn-cert-al-11-26`

HTTP 403 bot challenge ('Voight-Kampff Browser Test') to both Playwright and curl; WebFetch also got 403. The URL and title come from ENISA CNW-2026-04. The challenge body is saved in raw/.

capture 20261022T081353Z · HTTP 403 · https://www.ccn-cert.cni.es/es/seguridad-al-dia/alertas-ccn-cert/13200-ccn-cert-al-11-26-actualizacion-inmediata-de-vulnerabilidad-critica-en-php.html error: page.title: Execution context was destroyed, most likely because of a navigation- `provenance.json` 3499d3985dcda97902ce1e89dd5edffba4a20b56ba01cab266db1e9fc7f50c36 780 bytes
raw, 2 files with SHA256SUMS- `curl-body.20261022T0814Z.html` a3de1982de0d6d2967b7ac55d2787011ba4fdd8707f4a8e9e25e1b50b345d9f7
- `curl-headers.20261022T0814Z.txt` a397cde2f98a7851bb54672621f25f4834926a0250ea5140f65c91110b53d3f8

### [Security Advisory 2026-018: Critical Vulnerabilities in PHP](certeu-sa-2026-018/index.html) [original ↗](https://cert.europa.eu/publications/security-advisories/2026-018/)

**CERT-EU** · advisory · primary · captured · published 2026-10-21 15:20:18 (as stated; timezone not given) · added by `collector-gov` · `certeu-sa-2026-018`

v1.0 and v1.1 both 21/10/2026. States the PHP fixes were released '21 October 2026 at 13:30 UTC'. CVSS 9.2 each. Advice: 'patch affected assets immediately. Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified.' Notes PoCs are circulating.

capture 20261022T081329Z · HTTP 200 · https://cert.europa.eu/publications/security-advisories/2026-018/- `headers.json` 035d980d7924b86c61cd912c5ae8e55b5adbdf20e9f99f9c780d7b37e830e596 1,370 bytes
- `page.html` 1cc49d8c9b94ac2e09eb5f4e2bcb732a0d1fd4f630eaedad06da28a295978e53 24,504 bytes
- `provenance.json` d5c1ea12a493fd9c195d90ee56eba85c93cd77d6131bce3ac08929d72f275820 999 bytes
- `rendered.html` abb92e1078d68ea54089f704855e78b2a71cee27a6244c2d3f26cd1b8c90b759 23,744 bytes
- `screenshot.png` 894baac8f7c1a2e25439f481a468e1c086cf4c783d11e7f020bb354120ef6c99 624,274 bytes
- `text.txt` c65c95cf165d9ed7ec5d362642e92dd918c77fdfca1d4f88b303db6a3ab24ae3 7,105 bytes

### [[Màj] Multiples vulnérabilités dans PHP (CERTFR-2026-ALE-014)](certfr-2026-ale-014/index.html) [original ↗](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/)

**CERT-FR (ANSSI)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `certfr-2026-ale-014`

First and last version 21 Oct 2026. 'Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue...'. Affected: all 5.x, 6.x, 7.x, 8.0, 8.1, and 8.2-8.5 below the fixed versions. Workarounds: session.upload_progress off; block multipart Content-Type at WAF.

capture 20261022T081353Z · HTTP 200 · https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/- `headers.json` 96a5cd42d4ca38099fc910e8c06f10cfd15f15e6ca7bebdb699b3b7245d08d58 1,075 bytes
- `page.html` 91f474e2f0f414b2d8575b91cecd59d880e62f0179033baae665177100fc094a 26,782 bytes
- `provenance.json` 53ea7bfd63a634427908cc6846e7e974b45c9cdc7028b88d7e87d148408ecd59 989 bytes
- `rendered.html` f71933fcd112f86a98d8838cc53fa38dabffe5f27a6c4dc7bfc62f9ef6e9aa7c 27,674 bytes
- `screenshot.png` e6ccac8825818ecc2cfd2223035c6c335a3de1c38fad734d7dd292215618cef7 502,064 bytes
- `text.txt` f9e9557ab49ddb9598b22d6774d5466de0429deba8720e6e3fba62d778b5d0f3 5,127 bytes

### [Saistībā ar globāli atklātām PHP ievainojamībām Latvijā ievieš preventīvus pasākumus](certlv-php-preventive/index.html) [original ↗](https://cert.lv/lv/2026/10/saistiba-ar-globali-atklatam-php-ievainojamibam-latvija-ievies-preventivus-pasakumus)

**CERT.LV (Latvia)** · government · primary · captured · published 2026-10-21T18:25 local (EEST, =15:25Z); updated 2026-10-21T23:00 local (=20:00Z) · added by `collector-gov` · `certlv-php-preventive`

Latvia restricted access from abroad to several state digital resources (geo-blocking, possibly until Mon 26 Oct). Update 23:00: the TVP unified website platform is patched and reachable from Latvia; latvija.gov.lv is restricted only from abroad; lsm.lv and 112.lv restored. About 6000 potentially affected resources in Latvia, a few hundred of them public sector. Automated exploitation attempts seen, none successful so far.

capture 20261022T081354Z · HTTP 200 · https://cert.lv/lv/2026/10/saistiba-ar-globali-atklatam-php-ievainojamibam-latvija-ievies-preventivus-pasakumus- `headers.json` b75279eb611beef16c83a6ab4d307db8ec59d18614d4d21ea1c78320a4346166 737 bytes
- `page.html` de622b5e59bf43071dcb45655edbd42b337e97f28b3e41e801ebaacc64a33581 35,634 bytes
- `provenance.json` e046187fdaa6dc172317abf6fa62152e1b5594b3c2d59c75c1de1baafa4667ba 1,158 bytes
- `rendered.html` 4f3a30ed3f755cd5965265ba1cc6f1cce9e514537463c1f9d2b87fdfceaaf514 35,482 bytes
- `screenshot.png` 504fd0c9b36378f8039c94b1157842426c17d95ab822429554c1bfc0cdbfb4d2 750,435 bytes
- `text.txt` e37a6582c4e6c685ad840001892ea94cd8e91ec107708ce4e7b7110899c2d05e 6,579 bytes

### [Critical vulnerabilities in PHP: Install security updates immediately](ch-bacs-warnung-php/index.html) [original ↗](https://www.bacs.admin.ch/en/warnung-php-en)

**Swiss Federal Office for Cyber Security (BACS / NCSC)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `ch-bacs-warnung-php`

Published on 21 October 2026 (the home page teaser shows 20 October 2026). 'If an immediate update is not possible': restrict access; 'Check, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary.' Says a WAF alone is not sufficient.

capture 20261022T081700Z · HTTP 200 · https://www.bacs.admin.ch/en/warnung-php-en- `headers.json` 603765d5dfe2bc360d0d8becb67c71a6a5810ad02fbe68f5d677488189ac7317 6,406 bytes
- `page.html` bdef753f8a5972cd0d5af92574637f8edd425df0511ef469bf2c11ee39207e0f 160,186 bytes
- `provenance.json` 1574e8470bf5e04e0a830d2ee1ffd4d728872599f3828cba3399f0b095066f39 984 bytes
- `rendered.html` 7400fa0917a78b8192f819815d7bddbc76a93e9ddb57e9ce574cb60b713b4e0b 174,883 bytes
- `screenshot.png` b14b81a2939d7eafc4abdd581e6591629c66d8728ce4402a2c68421d788a9f63 846,454 bytes
- `text.txt` 99886a19aead8abe4faab9f41918c8654a2e070c816f856c0dd3e14a194d6890 4,966 bytes

### [BACS home](ch-ncsc-home/index.html) [original ↗](https://www.ncsc.admin.ch/ncsc/en/home.html)

**Swiss BACS** · government · secondary · captured · published not stated · added by `collector-gov` · `ch-ncsc-home`

Redirects to bacs.admin.ch/en; the PHP teaser is dated 20 October 2026.

capture 20261022T081604Z · HTTP 200 · https://www.bacs.admin.ch/en- `headers.json` 80c563292cf0e8178e58809441cc65504b120a6299d27979fc429c606efaa3fd 6,406 bytes
- `page.html` db63fa0b832d6e1c47503189a9e2dd40e5a0dc6e8aab560cae02e8db1f3806f4 683,600 bytes
- `provenance.json` a459bb8ebb915fac015c2f06c8c45177516e9c968f132531f1d20fa7053e7c69 923 bytes
- `rendered.html` 772da1668f48bd3c5a4f64e05a57da3b25759fb0029663257cdb7ffef85aec1f 739,577 bytes
- `screenshot.png` 0aaffb075e051c6b2ad0f9f8261010a963e502b32700d1fc07b0cdee4d9a835e 1,095,138 bytes
- `text.txt` 29c1b2cfeb73db9702347d8cbb1b37690641e3abf5ddda16da0af6451f54e41b 11,068 bytes

### [Apache Releases Log4j Version 2.15.0 to Address Critical RCE Vulnerability Under Exploitation | CISA](cisa-alert-log4j-2021/index.html) [original ↗](https://www.cisa.gov/news-events/alerts/2021/12/10/apache-releases-log4j-version-2150-address-critical-rce-vulnerability-under-exploitation)

**CISA** · government · primary · captured · published 2021-12-10 · added by `claude-story-site` · `cisa-alert-log4j-2021`

Historical: CISA's alert on Log4j the day it was published.

capture 20261022T113354Z · HTTP 200 · https://www.cisa.gov/news-events/alerts/2021/12/10/apache-releases-log4j-version-2150-address-critical-rce-vulnerability-under-exploitation- `headers.json` 81c7dcf0ae8dbb9db7007301569c1098a3ef6556dd79a9630d630651daa84547 2,869 bytes
- `page.html` 96fb8cf20f99673da75e17b169ced8e990ef1852c39832a988ce04901089dd93 52,975 bytes
- `provenance.json` 3f51e4f7a62ee09109ff3dc36fcb8369a5ad5cc50b151b08368a863938e9bf91 1,209 bytes
- `rendered.html` 5badb6aa92a2948ebfdb3e6213117ffa468b50a21ae447dd975d608df7786007 76,046 bytes
- `screenshot.png` 181a9b4f1fb059019f1f42b3d6d7ec914a53307ae7276e8d10637cdd93807b1c 311,343 bytes
- `text.txt` 98840739d797dd49ca9582640f9a88007c32812ba8e49d2cc0492e54c138c9e5 2,015 bytes

### [Critical Vulnerabilities in PHP Require Immediate Patching](cisa-alert-php-20261021/index.html) [original ↗](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)

**US Cybersecurity and Infrastructure Security Agency (CISA)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `cisa-alert-php-20261021`

CISA Alert, Release Date October 21, 2026. Names CVE-2026-109618/109619 'php2shell'. 'Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated.' CISA 'has not observed exploitation ... as of the time of publication'. Not in KEV as of catalog 2026.10.21.

capture 20261022T081353Z · HTTP 200 · https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching- `headers.json` 30fb6764c792111ac226e0fb1ca4f574f5e2faadfc10d2150ae9dfa35ea0858d 2,825 bytes
- `page.html` be6b410fc0da16de2c1b96dc3132a195632d636467ab7c859c343494fa7accfa 53,868 bytes
- `provenance.json` ea18f4dbc502d3c87b5d9a6c83d49ff128544ad074140c502f37abff350d9f8a 1,110 bytes
- `rendered.html` 0e3e08492a52d48e8ccb18f836df984af4f15f251f6089697676b540458b3371 78,116 bytes
- `screenshot.png` 2724e9107ccae45a888b3531fdc43373b154be3eeadb78841791dcb6a60a34c1 384,239 bytes
- `text.txt` 7bf853872a073bde9c2d71a41fbf9bfd3cda8147c278ab15426ebc9c8e627a9f 3,223 bytes

### [Page Not Found | CISA](cisa-ed-22-02-log4j/index.html) [original ↗](https://www.cisa.gov/news-events/directives/ed-22-02-mitigate-apache-log4j-vulnerability)

**CISA** · government · primary · captured · published 2021-12-17 · added by `claude-story-site` · `cisa-ed-22-02-log4j`

Historical: Emergency Directive 22-02 on Log4j.

capture 20261022T113402Z · HTTP 404 · https://www.cisa.gov/news-events/directives/ed-22-02-mitigate-apache-log4j-vulnerability- `headers.json` 1b3806dec260fe8e3a777ba86f9ee746b6edd19e249375bf255f7a5d9697921a 2,712 bytes
- `page.html` 601f61af5acf4d62056f2376b007d492c9f77dbc84557f9ea9f9f4a7834691da 47,323 bytes
- `provenance.json` bdfcae4f97b12f4551a9070ae19917243e91048c4e13feb7fb06f939368c8d1c 1,026 bytes
- `rendered.html` 4e45e69f1aa1a5d929a2896dce31b78f23be1bbfd88195b6030c0e1a5b7761e5 66,546 bytes
- `screenshot.png` d0899ef76fbd637495baf797c91303c02eaf04c8f12bdfafa20265b9052fe302 186,488 bytes
- `text.txt` 74b20e7dc5b8d12bb09978a2b9ab15941b343248ce65584eb76548fd8b68b0d2 1,035 bytes

### [Home Page | CISA](cisa-home/index.html) [original ↗](https://www.cisa.gov/)

**CISA** · government · secondary · captured · published not stated · added by `collector-gov` · `cisa-home`

Home page at 08:13Z: the PHP alert (Oct 21, 2026) is top of the news list. No emergency directive is shown.

capture 20261022T081329Z · HTTP 200 · https://www.cisa.gov/- `headers.json` a76ca34b24fba67b623a4b3e4b5748241af7aac12f07bb31b73a1f88445398b2 2,712 bytes
- `page.html` 24ba8c3fe3e00e4445bd9fbbbabf113099d53e872bb4d594e92c8575084cfe31 71,972 bytes
- `provenance.json` 364cc06b578cd41d9fc3e1155cd62c9694ca854bdfe27923863a3a00eb71ee53 877 bytes
- `rendered.html` 06fa4013f8e36ab399d6cef932f7d506a073b84357e4e4c40627479b5a3a1fa5 92,635 bytes
- `screenshot.png` ed352cf8665d21d75d282faefdb680a9c65965edae9b6cbf4541c84f9dcbba23 1,291,590 bytes
- `text.txt` ab2aa07bb46ba14c14a2f76a312ff7b81e2c8c19ca3588de9313236b10007a34 4,261 bytes

### [Known Exploited Vulnerabilities Catalog (JSON feed)](cisa-kev-catalog/index.html) [original ↗](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)

**CISA** · government · primary · captured · published 2026-10-21T14:04:39Z · added by `collector-primary` · `cisa-kev-catalog`

raw/ only (JSON feed). catalogVersion 2026.10.21, dateReleased 2026-10-21T14:04:39Z. Neither CVE-2026-109618 nor CVE-2026-109619 is listed as of fetch ~08:12Z on 22 Oct.

raw, 1 files with SHA256SUMS- `known_exploited_vulnerabilities.json` ef8fffede5c472001da046c7751beb2a3242458896d0ce08da52b30968b8b56b

### [CISA Known Exploited Vulnerabilities catalog (JSON feed)](cisa-kev-json/index.html) [original ↗](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)

**CISA** · advisory · primary · captured · published 2026-10-21T14:04:39Z (catalogVersion 2026.10.21) · added by `collector-gov` · `cisa-kev-json`

At 08:15Z on 22 Oct: catalogVersion 2026.10.21, dateReleased 2026-10-21T14:04:39.8983Z, 1754 entries. CVE-2026-109618/109619 NOT in KEV. Raw JSON + headers + SHA256SUMS in raw/.

raw, 2 files with SHA256SUMS- `headers.20261022T0816Z.txt` e3a7dc7610f87ca2b7829303cd01ef65a3d0d08be833334024807456cc943db9
- `known_exploited_vulnerabilities.20261022T0816Z.json` ef8fffede5c472001da046c7751beb2a3242458896d0ce08da52b30968b8b56b

### [Cloudflare deploys protections against php2shell vulnerability](cloudflare-blog-php2shell-waf/index.html) [original ↗](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/)

**Cloudflare** · vendor · primary · captured · published 2026-10-21 · added by `collector-researchers` · `cloudflare-blog-php2shell-waf`

Dated OCTOBER 21, 2026. Says the vulnerability 'was leaked before the official release date and we observed attack traffic targeting our customers'. WAF protection live from Oct 21 03:02 UTC (~9h before disclosure). Lists disclosers as 'Calif.io, Wiz, OpenAI and Quarkslab'. 'PHP is used by almost 70% of websites.'

capture 20261022T081216Z · HTTP 200 · https://blog.cloudflare.com/php-vulnerabilities-waf-protection/- `headers.json` 904849b322ddad92fccc55d4ce8527d9c4138d07d61937ce1da5602ea2bef244 7,260 bytes
- `page.html` 421005107f81d30d16850fdbf830446d6fd544746dfa7d201be9b4bd3f656e72 301,730 bytes
- `provenance.json` 7f98162527014e2989dfaa73146a26c079c634ddf24eff95ae99fad7ea43beb0 1,045 bytes
- `rendered.html` a0d3c37cde7c1721a08b028748a412672817c45958d05cc7fedaede582b5537b 373,881 bytes
- `screenshot.png` 1784904e6fdda092941881d0e5c85d73801054f216295ca43b17f76e7f5cd34b 989,488 bytes
- `text.txt` 302408765abf45e3ae84473d9050c1c65b35c2858e5b53be4fee29dda4de2823 10,205 bytes

### [Alerta de Vulnerabilidade PHP (CNCS)](cncs-pt-alerta-136114/index.html) [original ↗](https://dyn.cncs.gov.pt/pt/alerta-detalhe/art/136114/alerta-de-vulnerabilidade-php)

**CNCS (Portugal)** · advisory · primary · blocked · published not stated · added by `collector-gov` · `cncs-pt-alerta-136114`

HTTP 513 'Verifying your browser | DiamWall' challenge to Playwright; curl got a 167-byte stub; WebFetch got a redirect loop. The URL comes from ENISA CNW-2026-04.

capture 20261022T081354Z · HTTP 513 · https://dyn.cncs.gov.pt/pt/alerta-detalhe/art/136114/alerta-de-vulnerabilidade-php- `headers.json` 5c140f9296dcaee3311e6857332cd02f3ecef21ddea2f8e064632238f0723a07 411 bytes
- `page.html` edb193e6b70aacbf1578ad062b6fa5085bfef2f34cbf0fd97aa924338c502db7 1,083 bytes
- `provenance.json` e1e0d3e656a7c6ebfab6919cf39d5574b3af7346b5b2a843039c2dbcb844b2e9 1,028 bytes
- `rendered.html` ee72ee19cc622226439df3668a6e44283b40bf5c8a256279d4ca08a5381fe4ad 1,094 bytes
- `screenshot.png` 5950f00ba8371e122d55c0b80325546131c084d32f70aed1fdf1bafdbf9f5d27 39,887 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes
raw, 2 files with SHA256SUMS- `curl-body.20261022T0814Z.html` 9171fe017af37f1f055d8e8bac037fc72bf67dd77e534de433be05297a582b0f
- `curl-headers.20261022T0814Z.txt` b246a0bf67a34295b2bb54fc5724574f6176d92a46b05886076810bacd9a7e6c

### [Websites shut down globally after AI finds a critical flaw affecting 70% of the internet | CNN Business](cnn-php2shell-websites-shut/index.html) [original ↗](https://www.cnn.com/2026/10/21/tech/php2shell-vulnerability-ai-intl)

**CNN** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `cnn-php2shell-websites-shut`

Wikimedia Foundation to CNN: systems 'taken down as a precautionary measure'; '70% of the internet' in the headline.

capture 20261022T112616Z · HTTP 200 · https://www.cnn.com/2026/10/21/tech/php2shell-vulnerability-ai-intl- `headers.json` ff524b7f55b3e2e8e2a9abaa229a6d5694a59dcdb7346d04d4e47af17c87dc26 2,363 bytes
- `page.html` e194020ee0611e31ea5feb275ff76e19b40e03b3a1680e8e7e6ae37b1cdef60e 5,623,694 bytes
- `provenance.json` d46dfcb30fd93dcb98e4468deabbc7c3b555698dc2bcba8c6cbc81fea8306682 1,074 bytes
- `rendered.html` 9928b7deeb656b8f9d34f7844cf0e79c2e5a9ea2b05721c03e84a0bc404646d8 5,844,671 bytes
- `screenshot.png` a531b130b77be1e05bf3c9896abfc3abc4a70cc920a819eee04f7665c1a438e9 161,563 bytes
- `text.txt` ee49fc4265ae1c7cfb7ed245597071af43f17d437ed08be951d8388502f5a533 8,896 bytes

### [CVE-2008-1447 (DNS cache poisoning, Kaminsky)](cve-cve-2008-1447/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2008-1447)

**CVE Program (cveawg API)** · cve · primary · captured · published 2008-07-08T23:00:00.000Z · added by `claude-story-site` · `cve-cve-2008-1447`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2008-07-08.

raw, 1 files with SHA256SUMS- `cveawg-api.json` 4025bae38315c16e5ac26105365646c67c4bce58937a187a627274f023ff1501

### [CVE-2012-1823 (php-cgi query string)](cve-cve-2012-1823/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2012-1823)

**CVE Program (cveawg API)** · cve · primary · captured · published 2012-05-11T10:00:00.000Z · added by `claude-story-site` · `cve-cve-2012-1823`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2012-05-11.

raw, 1 files with SHA256SUMS- `cveawg-api.json` fc02a593375ecc025b00f8c4ba49d3227cae19c5ed0c9b78f7771362355abdb0

### [CVE-2014-0160 (Heartbleed)](cve-cve-2014-0160/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2014-0160)

**CVE Program (cveawg API)** · cve · primary · captured · published 2014-04-07T00:00:00.000Z · added by `claude-story-site` · `cve-cve-2014-0160`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2014-04-07.

raw, 1 files with SHA256SUMS- `cveawg-api.json` b0b80e14890433984e302ac8c3e6fe5d1669bcd52dfd8bd52de6945a2d06dff9

### [CVE-2014-6271 (Shellshock)](cve-cve-2014-6271/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2014-6271)

**CVE Program (cveawg API)** · cve · primary · captured · published 2014-09-24T18:00:00.000Z · added by `claude-story-site` · `cve-cve-2014-6271`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2014-09-24.

raw, 1 files with SHA256SUMS- `cveawg-api.json` 5f9825de68cb0d172329bdc64da9bd93951aae29803454926d4be7d1ac6d609d

### [CVE-2017-5638 (Apache Struts)](cve-cve-2017-5638/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2017-5638)

**CVE Program (cveawg API)** · cve · primary · captured · published 2017-03-11T02:11:00.000Z · added by `claude-story-site` · `cve-cve-2017-5638`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2017-03-11.

raw, 1 files with SHA256SUMS- `cveawg-api.json` 525b90b7605a6c18ccd4812dbc70dfdcf7f330374648173e0ade5fcb1e1b8d38

### [CVE-2019-11043 (PHP-FPM underflow)](cve-cve-2019-11043/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2019-11043)

**CVE Program (cveawg API)** · cve · primary · captured · published 2019-10-28T14:19:04.252Z · added by `claude-story-site` · `cve-cve-2019-11043`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2019-10-28.

raw, 1 files with SHA256SUMS- `cveawg-api.json` e32115c5b48bca1c90fab5a125d64f9067e728bb3ac6e13939ee0886d267e526

### [CVE-2021-44228 (Log4Shell)](cve-cve-2021-44228/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2021-44228)

**CVE Program (cveawg API)** · cve · primary · captured · published 2021-12-10T00:00:00.000Z · added by `claude-story-site` · `cve-cve-2021-44228`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2021-12-10.

raw, 1 files with SHA256SUMS- `cveawg-api.json` cae2ad45ea2739a59680c360555a538019b8f46199c797aed96fba49c073aa89

### [CVE-2022-22965 (Spring4Shell)](cve-cve-2022-22965/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2022-22965)

**CVE Program (cveawg API)** · cve · primary · captured · published 2022-04-01T22:17:30.000Z · added by `claude-story-site` · `cve-cve-2022-22965`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2022-04-01.

raw, 1 files with SHA256SUMS- `cveawg-api.json` b38ff19768aa5757d264340669a3c06e4a78e5e2014c813bc509d052e2f267f3

### [CVE-2023-34362 (MOVEit Transfer)](cve-cve-2023-34362/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2023-34362)

**CVE Program (cveawg API)** · cve · primary · captured · published 2023-06-02T00:00:00.000Z · added by `claude-story-site` · `cve-cve-2023-34362`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2023-06-02.

raw, 1 files with SHA256SUMS- `cveawg-api.json` feae1a77086ce7533526a0f9d24afb4c67917deb3363569795ea4bbc57b2abbf

### [CVE-2024-4577 (PHP-CGI argument injection)](cve-cve-2024-4577/index.html) [original ↗](https://cveawg.mitre.org/api/cve/CVE-2024-4577)

**CVE Program (cveawg API)** · cve · primary · captured · published 2024-06-09T19:42:36.464Z · added by `claude-story-site` · `cve-cve-2024-4577`

Historical comparator for the context page: the CVE record JSON, fetched 22 Oct 2026 with curl; SHA256SUMS in raw/. Published 2024-06-09.

raw, 1 files with SHA256SUMS- `cveawg-api.json` e8cc1b1dcd1a3333776e9a0f08cd4543bc662e0ee60fc094bda0820f84b114eb

### [CVE-2026-109618: RCE via OOM corruption](cve-cve-2026-109618/index.html) [original ↗](https://www.cve.org/CVERecord?id=CVE-2026-109618)

**CVE Program (CNA: PHP Group)** · cve · primary · captured · published 2026-10-21T13:48:34.845Z · added by `collector-primary` · `cve-cve-2026-109618`

CVE record JSON in raw/ (cveawg API). dateReserved 2026-10-12T21:03:58Z, datePublished 2026-10-21T13:48:34Z, dateUpdated 2026-10-21T16:07:52Z at fetch. CISA ADP SSVC at 14:34Z: Exploitation none, Automatable no, Technical Impact total.

capture 20261022T081218Z · HTTP 200 · https://www.cve.org/CVERecord?id=CVE-2026-109618- `headers.json` 58be2c1dc484c3910605b35d9e612014fc4b6e0c9de9f605d6286d788fde6c7a 1,500 bytes
- `page.html` a112001fc560b257188b1628cf8f547b421b7bb934cbd574254375a26151ab50 880 bytes
- `provenance.json` adc09f106ba451478b387bb819c13df4cc15e0ac6f7ab6507a24175c8cc75458 952 bytes
- `rendered.html` 37b9582087865e1776a98adadf13b2fd1cda169569affa0d7e113500697e5edb 146,271 bytes
- `screenshot.png` bfb16ac90b930eabd692ee995fc41e848022b6b3ad486b96eaab255d08553229 341,195 bytes
- `text.txt` f8705d8e0aa2a2488fd26ae277c71e7f460465f1c2566805b29408d46c08db4b 3,115 bytes
raw, 1 files with SHA256SUMS- `cveawg-api.json` f856138e139c216e7b499d86b519d6371b92494c7d63fcccbcd79117102750a1

### [CVE-2026-109619: RCE via stale global state](cve-cve-2026-109619/index.html) [original ↗](https://www.cve.org/CVERecord?id=CVE-2026-109619)

**CVE Program (CNA: PHP Group)** · cve · primary · captured · published 2026-10-21T13:54:43.866Z · added by `collector-primary` · `cve-cve-2026-109619`

CVE record JSON in raw/. dateReserved 2026-10-12T21:04:00Z, datePublished 2026-10-21T13:54:43Z, dateUpdated 2026-10-22T08:09:24Z (updated minutes before our fetch; CVE Program container lists oss-security refs incl. 22/2). CISA ADP SSVC: Exploitation none.

capture 20261022T081219Z · HTTP 200 · https://www.cve.org/CVERecord?id=CVE-2026-109619- `headers.json` 03c46200ee6c4d6c0d0a06fdaae6fb0a376986fa48431cdc5543e5ae073ca8f7 1,500 bytes
- `page.html` a112001fc560b257188b1628cf8f547b421b7bb934cbd574254375a26151ab50 880 bytes
- `provenance.json` 7de30cfb3eb2de89b08dcd062e6eee6c14efb0710ba248992dd2c1e2d3636335 952 bytes
- `rendered.html` 83e446fe17d5717ad7f281973b506b4ba9e19b1b7cec8a4687132cd84419c71f 150,334 bytes
- `screenshot.png` ae02d0aca995d93891d5bc181141c569b6b465a32272d727709884750ecdb50b 367,927 bytes
- `text.txt` 3162135e82a9edd4b3ce352b41d2ecc34275ee0bb55a6444ed40c2146f1566c5 3,351 bytes
raw, 1 files with SHA256SUMS- `cveawg-api.json` d045248b93425b1a6f5a0fc29ae36b5cfcd3c8188d969664a0d8e5f82ff05f61

### [What We Know About php2shell [Critical update]](cybelangel-php2shell/index.html) [original ↗](https://cybelangel.com/blog/critical-php-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/)

**CybelAngel** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `cybelangel-php2shell`

Vendor explainer; Cloudflare CTO 07:43 UTC early attacks; Aikido reporting exploitation.

capture 20261022T112625Z · HTTP 200 · https://cybelangel.com/blog/critical-php-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/- `headers.json` 434967eca3ae83ed546f2b8d4839eeb91ca1b11c8740be1e1e1f3864d5e4f809 1,530 bytes
- `page.html` 842333792c959891233e6290ecc0857bfd361fbc9dfb4b377a8325657855a025 169,382 bytes
- `provenance.json` d2e13e8d5bd7b15ee078cbe727f55708366293caa3c4a68445ce1fbd5e206201 1,070 bytes
- `rendered.html` 538f2982edeb0859af905cbcf0dc02f6899dcd997e9a7245917ad53e04faa993 174,398 bytes
- `screenshot.png` 64c9ca6ef1602bd645b956fe272f9fcb7d3d50ec0f24b4af5b980edfc9e424d5 1,631,217 bytes
- `text.txt` 4ffc5347bfe22fb45007c6d0d169a6cdff75522822604e9d8e0e421fda4e2f27 12,396 bytes

### [PHP2Shell CVE-2026-109618 PHP Flaw Hits Gov Sites](cyberexpress-php2shell-gov-sites/index.html) [original ↗](https://thecyberexpress.com/php2shell-cve-2026-109618-php-flaw/)

**The Cyber Express** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `cyberexpress-php2shell-gov-sites`

Secondary: Wikimedia quote; government sites hit.

capture 20261022T112646Z · HTTP 200 · https://thecyberexpress.com/php2shell-cve-2026-109618-php-flaw/- `headers.json` 12ba694e03c07c68e519eee401b1f3c26bbbf5e314d5681dd8dee8202a9ddc2b 1,486 bytes
- `page.html` 58d2d840bcff4c80b422282f8358fded7d8d4a8a0ae0005b66dd7ce51049222d 567,233 bytes
- `provenance.json` b259cfb46f07df0edf091ae5b56f255c93846d9656a80d9adbe65e6aa496349f 1,017 bytes
- `rendered.html` ed8d3c7588accfa0810ec2d054a01b00bf1c8783e9100bc6f46557783e623fa5 598,469 bytes
- `screenshot.png` d80c357eed47fd016ffe1e5a7866573916c9044f011f6e0e3c7b2487c93d296a 18,579,851 bytes
- `text.txt` f45bc7599367343e65c9a0d202d909990a7a802e526f44362042e0de16cf20a6 14,589 bytes

### [PHP2Shell exploit attempts hit millions, Amazon and Cloudflare warn | Cybernews](cybernews-php2shell-millions/index.html) [original ↗](https://cybernews.com/security/php2shell-wordpress-amazon-cloudflare-ai-cyberattacks/)

**Cybernews** · news · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `cybernews-php2shell-millions`

Secondary: Cloudflare and Amazon warnings; millions of attempts.

capture 20261022T112703Z · HTTP 200 · https://cybernews.com/security/php2shell-wordpress-amazon-cloudflare-ai-cyberattacks/- `headers.json` 6be6626f1e9d0a6627adcf4b3cfe7e0e3fbc8107a1ef9772318e3b2f95ccfc6b 2,119 bytes
- `page.html` c66a7d30501a36b114a61e46813ab2e0d7ec2dfa4d5fb106f8c5a9ff50ef69b6 264,681 bytes
- `provenance.json` fd6fc60ea011e77252fb66fb924fa6ded42288362364dea1c51a872c9f0a80d3 1,087 bytes
- `rendered.html` 396bc3073c8b12fb2dc2ed624d0f38b6fc6dbf885f976267d2e1c0b5b47ef108 268,472 bytes
- `screenshot.png` 4593aadc41abb1ffd9875242e346506becf26679a960c352c74a1b52d2c5f956 2,513,246 bytes
- `text.txt` a5ebfc60c25fe8b2c4cf59d2c2b9019703ef75d77de84f502e27df28ea891ceb 7,502 bytes

### ['PHP2Shell' Bugs Signal Red Alert for Security Industry](darkreading-php2shell-red-alert/index.html) [original ↗](https://www.darkreading.com/application-security/php2shell-bugs-red-alert-security-industry)

**Dark Reading** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `darkreading-php2shell-red-alert`

Secondary coverage.

capture 20261022T112357Z · HTTP 200 · https://www.darkreading.com/application-security/php2shell-bugs-red-alert-security-industry- `headers.json` 285a1d8359a3246821411a25457fe0ebe5714a3f3b64d2b0d9594549c5e28ee8 1,005 bytes
- `page.html` 6a65a719cc37abf4198febfdb8afedb400656bbab8a87ecbf7979436acde2db7 451,026 bytes
- `provenance.json` 0f49ff38cf40ae508792e69a36322fd852a90a413670686eb09c7abc3bab0e2a 1,078 bytes
- `rendered.html` 94b8a23834d88b4202c8131505e4bb6abb7c27095cd873031af7f721a4d155f3 470,067 bytes
- `screenshot.png` 2672b1f34bea1f587b758b2d846512d528d66179b9c6267f491669fb7287326e 2,410,017 bytes
- `text.txt` 6db30e279f5f38773c58ae71e0d753d7a7f90fcf4148ea65658c2f967de7f32d 10,175 bytes

### [What the PHP2Shell rumors got wrong, from inside the PHP security team](daubois-blog-php2shell-rumors/index.html) [original ↗](https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/)

**Alexandre Daubois (PHP security team / PHP Foundation)** · researcher · secondary · captured · published 2026-10-21 · added by `collector-researchers` · `daubois-blog-php2shell-rumors`

Personal blog of a PHP Foundation contractor on the PHP security team, dated 21 OCT 2026. Describes anonymous HN post Oct 20, leaked 'PHP2Shell tool' screenshot credited to Calif.IO, the short exploitation video, and watchTowr confirming the CVEs publicly. Gives GHSA advisory opened 2026-08-27 credited to lcfr-hax, sagitzadik-wiz, amyb-oai and tomash-areion.

capture 20261022T081256Z · HTTP 200 · https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/- `headers.json` 7f4da02c6bd4388f7475aed4c30ba66fbfd5e93f9e9b69537b21005081745afa 1,049 bytes
- `page.html` 8f85e508b569e07d58f4ab54611fc7bb886c13f58b8c0448198f44899bf54d10 22,135 bytes
- `provenance.json` c86d302cfb9e3442fe758ce082c1015c8500db089f7e8350402efbd4b259241d 1,046 bytes
- `rendered.html` 8bc8f77f0b030a431c17cfb6048a516fae5d743bcf9af1d571e1a377dbe77fbd 21,926 bytes
- `screenshot.png` c86032b5d2ce179ae664684fe600ba45c0b3ff7003c835716b5cce042a13e514 817,325 bytes
- `text.txt` 5ef17f9886aa93f7f15ab1f6657ef6991a8ec008e5e309bdde5b5e51d961c4d8 8,821 bytes

### [Just a moment...](dutchitleaders-websites-offline/index.html) [original ↗](https://www.dutchitleaders.nl/news/763189/diverse-websites-offline-door-kritieke-kwetsbaarheden-in-php)

**Dutch IT Leaders** · news · secondary · blocked · published 2026-10-21 · added by `claude-story-site` · `dutchitleaders-websites-offline`

Dutch: various websites offline over the PHP flaws.

capture 20261022T112724Z · HTTP 403 · https://www.dutchitleaders.nl/news/763189/diverse-websites-offline-door-kritieke-kwetsbaarheden-in-php- `headers.json` 3d4ed9c4a01097923a5877669d569d5ef394a8cdbe10aac65675668a31143782 1,537 bytes
- `page.html` 15b89d416c1e20625b50003213b1a4360e6045761598fec254652a1b5f3873b8 6,469 bytes
- `provenance.json` 8cea400474f5ccc7e7b350c5c9cf809ccb654b95894cae6c78613d5ff0c04d1e 1,061 bytes
- `rendered.html` 2f12251c8ab3b803be5a1123525fe94ec19fd2e3ad6daa9bab26759a181be3fe 7,234 bytes
- `screenshot.png` 1e7419104eee208b5ba0cc5f6696749ef060e1608266268dffcbd5d925e8f5ad 20,501 bytes
- `text.txt` 28f6003be69e3a9719618a62764a55d30d9d28570363ffd8126d1ef0f32a5803 75 bytes

### [No breach of Budget security after critical flaw found in PHP, minister says | East Anglian Daily Times](eadt-minister-budget-no-breach/index.html) [original ↗](https://www.eadt.co.uk/news/national/26659279.no-breach-budget-security-critical-flaw-found-php-minister-says/)

**East Anglian Daily Times (PA)** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `eadt-minister-budget-no-breach`

A minister: no breach of Budget security after the OBR site was affected.

capture 20261022T112742Z · HTTP 200 · https://www.eadt.co.uk/news/national/26659279.no-breach-budget-security-critical-flaw-found-php-minister-says/- `headers.json` 4262ef46e445ece7b451c5d9768be9e2c72be47dd23270284566f23c6429c24b 925 bytes
- `page.html` 47c1d48da4a78b3172325945c56a5b1bbbdd826cc02ad5b208f097d735b8deb9 291,406 bytes
- `provenance.json` b59efe28603612dd036d6a98ba25b7b39db79e7b4739b163b239131955e26cc7 1,163 bytes
- `rendered.html` 790f7f3108d2c3fc28b38ccd146871560b9b62412b719911f578da424f7d70df 451,816 bytes
- `screenshot.png` 5079181e1c5eb09fb0b82305b4599b7b3767e0da3fdd0263cb2fc25a3cd8c349 1,490,164 bytes
- `text.txt` 4c8556b5aaedee9f059a9862338d94d85df76b55d648396c2a7f964507cda4dc 7,475 bytes

### [CSIRTs Network - php2shell (CNW-2026-04)](enisa-cnw-2026-04-php/index.html) [original ↗](https://github.com/enisaeu/CNW/blob/main/advisories/2026/CNW-2026-04_php.md)

**ENISA / EU CSIRTs Network (CNW)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `enisa-cnw-2026-04-php`

EU CSIRTs Network index of national advisories (date 21-October-2026). Lists ~30 national CSIRT alert links. The 'Mitigation' field still holds unfilled template text. The title has a typo: 'CVE-2026-10961'. curl got 403 from GitHub; Playwright got 200.

capture 20261022T081329Z · HTTP 200 · https://github.com/enisaeu/CNW/blob/main/advisories/2026/CNW-2026-04_php.md- `headers.json` 4fddd3b1827235c9608b8a4c92566f15c7fde3ea496d7a74061d64b18fdd4072 5,637 bytes
- `page.html` 212f41dffb19edf392212f2ec2997428225cc9da6dbbcf1361dffc30f3ac163f 252,581 bytes
- `provenance.json` ce33999aec2752cab53039232bb4a7da90a38f090b374d68f470a0f9c78f4c7a 1,052 bytes
- `rendered.html` 3d40c318822605660674e8a69d6a51d523c3df892b77cd2ccf520e51bb9ad552 295,999 bytes
- `screenshot.png` 0b9c0e94049921b40590086857c547bc0dea05461fad30201388de32c3f35c8e 451,547 bytes
- `text.txt` dfcaa1afe1c4194c00ff2dc38b4fab496a900ce9b4e770a722b4bae96b886093 3,930 bytes

### [CVE-2026-109618 and CVE-2026-109619: What we know about PHP2Shell and how to prepare | Equixly](equixly-php2shell-what-we-know/index.html) [original ↗](https://equixly.com/blog/2026/10/21/cve-2026-109618-and-cve-2026-109619-what-we-know-about-php2shell-and-how-to-prepare/)

**Equixly** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `equixly-php2shell-what-we-know`

Vendor explainer listing exploitation as disputed and KEV as not listing the CVEs.

capture 20261022T112832Z · HTTP 200 · https://equixly.com/blog/2026/10/21/cve-2026-109618-and-cve-2026-109619-what-we-know-about-php2shell-and-how-to-prepare/- `headers.json` f7cf1d20d42b031e13757abae43ca1755e99a6e9bb3c4924d4b4d4a220ecc177 916 bytes
- `page.html` 850a5ee9c4cc603f0e67b5b759b07fd4fa2a58589e3a5ca3c118bb52bb137f1e 69,255 bytes
- `provenance.json` 9e7737082f0e4348bffb9bbee063d4618149ca26ce04c93ad349a82de0747038 1,174 bytes
- `rendered.html` 5f9daf95daffe64c7e40e58452326ecada0b2a45839cc411b569ccd3d8aa0152 137,760 bytes
- `screenshot.png` 4ff3a6bf1cf643f1beaea2676b32f6a8763bd97a1c958c2647e3613fdd247fde 2,260,486 bytes
- `text.txt` 34bf72d02f14deb9d0a164cd5ae8b59901f640461fa00f170fb618d727ce337c 14,172 bytes

### [Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly](fastly-blog-php2shell/index.html) [original ↗](https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618)

**Fastly** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `fastly-blog-php2shell`

Candid on exploitability (PoCs need the binary's layout on x86_64; 32-bit assume compromise), on WAF limits, on signals (segfault bursts, workers spawning /bin/sh) and on more bailout paths to come.

capture 20261022T111906Z · HTTP 200 · https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618- `headers.json` 6756cb0315f3eede874eb6e0c7c5bf69e9530954bc546eed72665c7d035f47a4 1,049 bytes
- `page.html` 811a842d39ce55fe1b7b9ef1e35c767deadda63bbf07044ac6d848812045d8fa 164,855 bytes
- `provenance.json` ea10f0c918a09cb23072d0099d2a206b10c844041a8649ce45f3446a7229ccec 1,117 bytes
- `rendered.html` beb13bda9a79b867d0b11deda470a987cd8f76186e6af59cb63333eb6d426839 327,821 bytes
- `screenshot.png` 259708a035d74a2d833a8fe3a555097ecee5678d854a5e5357b94bf20566b7e4 2,470,515 bytes
- `text.txt` bacf27615fe1180a00a1b2085b55ead30ce7e828eca5a4aa47c46d0c5808913f 20,043 bytes

### [How to block PHP2Shell (CVE-2026-109618, CVE-2026-109619) on FortiWeb | Community](fortinet-fortiweb-php2shell/index.html) [original ↗](https://community.fortinet.com/fortiweb-40/how-to-block-php2shell-cve-2026-109618-cve-2026-109619-on-fortiweb-230750)

**Fortinet Community (FortiWeb knowledge base)** · vendor · primary · captured · published 2026-10-22T07:55 (article time, timezone not stated) · added by `claude-story-site` · `fortinet-fortiweb-php2shell`

FortiGuard signatures 090502648, 090502651, 09052654 in database 0.00438; alert-only by default; four custom-rule templates.

capture 20261022T112039Z · HTTP 200 · https://community.fortinet.com/fortiweb-40/how-to-block-php2shell-cve-2026-109618-cve-2026-109619-on-fortiweb-230750- `headers.json` a0454c866ef8c53658075dd181e88a1d6f0387b633b7e59fcf740b5254c0e7d0 823 bytes
- `page.html` d5bc4f5c0a9b665b7bdc4d37c6adebfca47aaab1f93795c3a0551393e25a2531 789,605 bytes
- `provenance.json` ddfff2dafe3e00768857136f2f89239b03664e07eaf4a3282e1552b2b1d65ec1 1,150 bytes
- `rendered.html` 2d8aabfc30d2116425651b788f2c8e4d58122738b69721391022332ab628815b 1,208,805 bytes
- `screenshot.png` 03a275af997e6093c4700503437ee405b77df000307b546eda109ddb0f40acff 826,331 bytes
- `text.txt` 66beb7cb9c50e017b68c7c28ce5f985fd12b156c4060ecd82205cea19185d2a4 6,244 bytes

### [PHP2Shell: Detection Opportunities · GitHub](gist-blevene-detection-guide/index.html) [original ↗](https://gist.github.com/Blevene/472692937d05145d29d17dc3c6edc2a0)

**Blevene (GitHub gist)** · code · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `gist-blevene-detection-guide`

The most detailed detection guide found: verified ModSecurity tripwire on the upload-progress field, Sigma rules for the arm-phase fatal ('in Unknown on line 0'), FPM segfault correlation, Falco worker-exec rules, and the arm/fire success receipt in the access log.

capture 20261022T112029Z · HTTP 200 · https://gist.github.com/Blevene/472692937d05145d29d17dc3c6edc2a0- `headers.json` e515879745065efa3f6d82ddfddf934b4dd0528d08c9cd4686517a7909ad53a9 5,398 bytes
- `page.html` 638f078193990b68d231d7f9d70c8090f0fa5ea1c6f17144ce040e86005b0e0e 172,916 bytes
- `provenance.json` b55dcda494ff7fa675bdade5d18cd9c720a7f4c91f3c8902067bb528fe41a621 1,010 bytes
- `rendered.html` e632d2722b6bc2f11dae20c788c7c087967ff8b1617f9e49874b67f34f3ccbc7 171,073 bytes
- `screenshot.png` 40cb4bc63512079ac9f9922051f970143f708fe8f10a7839fdf8f3a8cebe109d 2,916,589 bytes
- `text.txt` e87c134fef2ac6dadce17cc4b2ede04888da65e4c1939814c3e2acc5683ddb81 28,797 bytes

### [PHP2Shell Censys Query (CVE-2026-109618 / CVE-2026-109619 ) · GitHub](gist-silascutler-censys-query/index.html) [original ↗](https://gist.github.com/silascutler/c7f04537a79ace89569f979d964af0f9)

**Silas Cutler (GitHub gist)** · code · secondary · captured · published not stated · added by `claude-story-site` · `gist-silascutler-censys-query`

A Censys query for php2shell exposure.

capture 20261022T112841Z · HTTP 200 · https://gist.github.com/silascutler/c7f04537a79ace89569f979d964af0f9- `headers.json` 07517141f85eb8c967f82ff329f3ec582d07ba06c068b4f69137e6f1b1bbc2bd 5,405 bytes
- `page.html` 6efd8ea91d0aeff2abdb43f40fb4a5695eacdbc5720b7a18c6746858dc3e2b89 126,486 bytes
- `provenance.json` bfd64368239f0a7cf7a26eac489eda86effc8c0e4c6b09653d8eaa7a838bc2aa 1,044 bytes
- `rendered.html` d31d94a0e67d4acc2f75d4548fd7bc98b0259d143eb16ec35ff1181b6f3fc0c6 124,729 bytes
- `screenshot.png` fdcd80585ae0e06e894d974485b23ecf187fa65cc7195ccf17f13486b9c5782a 122,357 bytes
- `text.txt` 5cea858eacc35a20d7943cf8334baad5fa8b37ed7f19ecbf3416f489935edd49 1,361 bytes

### [GitHub - darkfibr/php2shell-detect: Defensive detection toolkit for php2shell (CVE-2026-109618/109619, PHP session.upload_progress UAF): UA-independent shape scanner, estate checker, Suricata/Snort rules · GitHub](github-darkfibr-php2shell-detect/index.html) [original ↗](https://github.com/darkfibr/php2shell-detect)

**darkfibr (Mike Haddock), GitHub** · code · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `github-darkfibr-php2shell-detect`

Community detection toolkit: Suricata/Snort rules keyed on request shape (upload-progress field + many array parts), YARA for the public PoC, estate checker.

capture 20261022T111956Z · HTTP 200 · https://github.com/darkfibr/php2shell-detect- `headers.json` 0032162778e9e13e6056d409874d38d891d76817b61b685b8cac6978d0946ff1 5,443 bytes
- `page.html` 47a54e3191d2665698e13d8dd3b157f63a32f0565ae7755ea8bfb9634774ac91 287,088 bytes
- `provenance.json` 1d8350230abbd90feb1f18d64a3d02b15f7b35d71914d26d2207c18cb626d091 1,143 bytes
- `rendered.html` e0597533f94146958614e519387471deb149af84b19ea359e01dbd50d4dddbcf 305,777 bytes
- `screenshot.png` eb849fd1179b14a53199521fd46cca0b26c498292d2553acc0d976e79b0e03a7 748,563 bytes
- `text.txt` 3592ec9f3bb73cd3a91f3fd0c698fb45375984c5c0326bbcb4f7f7c36b2b8f73 7,156 bytes

### [RCE via stale global state (CVE-2026-109619)](github-ghsa-6wmf-4rv5-p3rp/index.html) [original ↗](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)

**PHP (php/php-src GitHub security advisory, published by bukka)** · advisory · primary · captured · published 2026-10-21T13:34:13Z · added by `collector-primary` · `github-ghsa-6wmf-4rv5-p3rp`

CVSS v4 9.2, same vector as 109618. Use-after-free of worker global state across requests. Confirmed RCE mod_php (PHP 8.5 fatal_error_backtraces path) and session upload progress path on mod_php and FPM. GitHub API blocked; timestamp from page.

capture 20261022T080901Z · HTTP 200 · https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp- `headers.json` 9474439a8ed75c50ba02584a2c67a564bf208b0caa8b2aefe0d7d2704e46c263 5,440 bytes
- `page.html` 93ff984c03081442f47f1c338683875fabf1741564d711e2a3862d71cef29fdd 221,023 bytes
- `provenance.json` ab199ddc3636b44804bf4b7da3949fe9d22f000959f8fc04c7f00eb3e416a0bb 1,039 bytes
- `rendered.html` 89eb250785b0066130856745323cc48cd37a515b3264c10da91dfee64deb45cb 222,855 bytes
- `screenshot.png` bb279a6b633c6e9d1de5a4778673aa4b3ed7dc5e1a1d9f08a3ba27c30f99820a 1,024,722 bytes
- `text.txt` 99d85c973c41c0242c944f052d5f13beee1b0e381b83f8f89416c986099db4fc 13,502 bytes

### [RCE via OOM corruption (CVE-2026-109618)](github-ghsa-w8hw-w9fx-j79w/index.html) [original ↗](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)

**PHP (php/php-src GitHub security advisory, published by bukka)** · advisory · primary · captured · published 2026-10-21T13:34:25Z · added by `collector-primary` · `github-ghsa-w8hw-w9fx-j79w`

CVSS v4 9.2 CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N. Affected capture 20261022T080901Z · HTTP 200 · https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w- `headers.json` a5b68bac81984833a0df448856c563c0abaaf285f4eac25b6fc9a01c0b4d705f 5,447 bytes
- `page.html` f429f17d81fee9dced4234a3f88772e1a7fdb87170b5bf5e3c6a016758b2a14e 212,571 bytes
- `provenance.json` bb24fb081f4677b9fb91aac8bf728da3b708aec4d694572ccf432df9c0e5162b 1,035 bytes
- `rendered.html` 79647ef8c491692c787e535f84364db88577ccdd26a84a066643ac2d8f0a1110 214,403 bytes
- `screenshot.png` 4e10459ced9f68c1f9fb25ce9f8c603fad05b9e1981b2b9de3c10c16ade86d77 535,897 bytes
- `text.txt` 84ab95d3b1d538ba0ff48d9f7371e482501999c23847fbecb67de6840324bfc4 6,692 bytes

### [GitHub - Lexsah/php2shell-detection: Detection and mitigation rules for CVE-2026-109618 / CVE-2026-109619 (php2shell). Blue-team only. · GitHub](github-lexsah-php2shell-detection/index.html) [original ↗](https://github.com/Lexsah/php2shell-detection)

**Lexsah, GitHub** · code · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `github-lexsah-php2shell-detection`

Blue-team rules (YARA, Sigma, Suricata SIDs 910961801-803, ModSecurity, Falco, auditd) and the server-level session.upload_progress.enabled=Off mitigation.

capture 20261022T112009Z · HTTP 200 · https://github.com/Lexsah/php2shell-detection- `headers.json` 25e99ec6775270a84bcecf5a232634c2e640ef9246b469967311c1240df22dd7 5,436 bytes
- `page.html` 6151205973ed45a3e00af67742bf708f8d42f4caf1171c1b5671e024b730bdbb 288,052 bytes
- `provenance.json` 2560ba2b32e6f1ea7e5feb0e81a7b6db2855392524862a91661362e6410175ca 1,077 bytes
- `rendered.html` 14e642e4e762e427c9bd8be65bfd45e0d8e2a3289c65ab7c197e197cc9077a66 301,999 bytes
- `screenshot.png` c5300a3f00d8c04d057f920a6e8ceb48282544a99c967bd855027483a7a4ffc9 779,281 bytes
- `text.txt` 10b6edf13054c98d5da298e7bdc04a654d2e0a7fa7fa820047a7996a4887c25e 7,136 bytes

### [Branch PHP-7.4-CVE-2026-109618-109619](github-php-src-branch-7.4-backport/index.html) [original ↗](https://github.com/php/php-src/tree/PHP-7.4-CVE-2026-109618-109619)

**php/php-src on GitHub** · code · primary · captured · published 2026-10-18T18:10:24Z · added by `collector-primary` · `github-php-src-branch-7.4-backport`

Unofficial minimal source backport for EOL 7.4. '1 commit ahead of ... master'; latest commit 'Avoid state corruption via bailout', commit date 2026-10-18T18:10:24Z. The 8.0 and 8.1 branches are not captured (same naming pattern).

capture 20261022T081558Z · HTTP 200 · https://github.com/php/php-src/tree/PHP-7.4-CVE-2026-109618-109619- `headers.json` a849a6e452711b855043ae9fe1fd0982b11d14633681acc628fa56e60ceb8323 5,439 bytes
- `page.html` 04dcda73bc626ce33da19b196795fd7c00b63b030f9fd6a530acedcbbe4f2b77 363,416 bytes
- `provenance.json` b879f4cb8fe1d72fc30175af0e12496f9df0b4e09ce90b1de15b99d1e8ed29fc 1,040 bytes
- `rendered.html` f6eba14e4661be71a25a3f70b5e988478a727cc6ea78f657fe86284d54d727fd 412,706 bytes
- `screenshot.png` 6a7c4e4d30f1cb137b32490feb57c7053ca293f0f59d4aada14082309c525f0a 759,378 bytes
- `text.txt` bd71e98ee89b7c6ca97f0ec6029e0200f86d26f2528387a96c99ac93ea63dc1f 6,550 bytes

### [Commit 3584a98bd: Avoid state corruption via bailout (the php2shell fix) and the PHP-7.4 backport 712e60f9e](github-php-src-fix-commit-3584a98bd/index.html) [original ↗](https://github.com/php/php-src/commit/3584a98bda0f2c0d367255b046798b0d3a221a19)

**php/php-src (git), read from a clone** · code · primary · captured · published 2026-10-18T15:26:39Z (authored); 2026-10-21T14:06:22Z (committed) · added by `claude-story-site` · `github-php-src-fix-commit-3584a98bd`

git show output of the fix commit (stat, file list, engine/main/session hunks), the 7.4 backport commit and patch, and the merge path to PHP-8.5, from a shallow clone made 22 Oct 2026. SHA256SUMS in raw/. 389 files, +10689/-976; authors Arnaud Le Blanc with Ilija Tovilo, Jakub Zelenka, Nora Dossche, Nicolas Grekas.

raw, 7 files with SHA256SUMS- `commit-3584a98bd.NEWS.diff` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- `commit-3584a98bd.engine-main-session.patch` 26bed812bcc7c89ea684f52d0a2e2a09f7bf516296f31b7065387c3c85013d84
- `commit-3584a98bd.files.txt` d9b8465ccfbd22fa5bcd5f1a8c58c11b4af70befe488051f843fd4f45bf559b5
- `commit-3584a98bd.stat.txt` 0d696e59634f83a4040532d4c6e4ac9cb5319e1c6e81ac2c76f3b7e9257f2b4b
- `commit-712e60f9e-PHP-7.4-backport.patch` 307e49f52c4f3829e75ce82697b81c6ab771deb7ce0c8ce961159e40026866da
- `commit-712e60f9e-PHP-7.4-backport.stat.txt` 7f5e6289ca2d1a14b2be78ca230e2077f3d5f695bb9d52087773e3df2633e7f0
- `merge-path-3584a98bd-to-PHP-8.5.txt` 81c3025511c2f4744d1fcbe1d18fe7da97cfd68b005a6a883efc229a3c91193f

### [Release PHP 8.5.12](github-php-src-tag-php-8.5.12/index.html) [original ↗](https://github.com/php/php-src/releases/tag/php-8.5.12)

**php/php-src on GitHub (release by adoy)** · code · primary · captured · published 2026-10-21T14:06:46Z · added by `collector-primary` · `github-php-src-tag-php-8.5.12`

GitHub release published 2026-10-21T14:06:46Z by adoy; tag object 2026-10-21 13:35:38 UTC; tagged commit dated 2026-10-19T17:04:37Z.

capture 20261022T081558Z · HTTP 200 · https://github.com/php/php-src/releases/tag/php-8.5.12- `headers.json` 5c5686f2496a1b93d144afdd699626ee85dc4af2813a242dbf615446ddb664eb 5,448 bytes
- `page.html` 67ce23eedb690c74470175cf0a56c7a573cbd02ec5f27120c3ced5d05fa5eb3b 207,502 bytes
- `provenance.json` 8e480c6bdb33a1d5e82ddf99493ac5149329b2ab40d2fe95c088ba4b9672832a 990 bytes
- `rendered.html` 330630ed887249f612aa5637d43d010f74ecc0970060b8bed32da7957a2521aa 214,534 bytes
- `screenshot.png` ca5cc2bad8c65a0a5325554ef804f2b83d3fc7a4b7e9c2750dfd7047e564208c 123,213 bytes
- `text.txt` 3fa0b4ca147ee06698f340ee959bf381aee7c0fda597bd687ff1f128f4978799 1,184 bytes

### [Tags · php/php-src](github-php-src-tags/index.html) [original ↗](https://github.com/php/php-src/tags)

**php/php-src on GitHub** · code · primary · captured · published not stated · added by `collector-primary` · `github-php-src-tags`

Tags php-8.5.12, php-8.4.27, php-8.3.36, php-8.2.35 all show 'Verified' and tag dates of 2026-10-21 13:35:38 UTC; php-8.6.0RC4 at 14:57:44 UTC. php-8.5.12RC1 and php-8.4.27RC1 tags also exist.

capture 20261022T081558Z · HTTP 200 · https://github.com/php/php-src/tags- `headers.json` c1e8341353ae8ccbb1b8406734139fd6ade271a8ecb16de19cc396443719b543 5,449 bytes
- `page.html` 9dd05842513d6ae6569812a9aad0f4abef35733b14f8515c3b86b3d1fac53d49 279,656 bytes
- `provenance.json` fb3a77d83afa6bbbffbf5b0dba33cf24208559ef6dafc50b4fe37998fd225316 928 bytes
- `rendered.html` ca0a96e8466a34796c2120346612561d23d3d53e81a8b52e679148924f0abcd9 281,310 bytes
- `screenshot.png` 9208f3cecdd6dd08a577e0172d3a114ac84322533de8e95591e5b0694b085eda 125,085 bytes
- `text.txt` 850531b6512cfe4d37a2bb6b7fdcd37ec9cbb42ed6ceea172d081be054e28c61 924 bytes

### [GitHub - rjmendez/phpup-2026: IOCs and detection rules for CVE-2026-109618 / CVE-2026-109619 (PHP session.upload_progress UAF) · GitHub](github-rjmendez-phpup-2026/index.html) [original ↗](https://github.com/rjmendez/phpup-2026)

**rjmendez, GitHub** · code · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `github-rjmendez-phpup-2026`

Detection rules rewritten on 21 Oct after a lab reproduction showed the leaked PoC's mechanism did not match the fix; cites VulnCheck: none of the public PoCs has the correct mechanism.

capture 20261022T112003Z · HTTP 200 · https://github.com/rjmendez/phpup-2026- `headers.json` 582bbe71ccaa5a3323db8d3d2caec68f5af4561fd8b8b29bd932cbea2126e5cf 5,445 bytes
- `page.html` e7e78dc79587fcaf7eac2ce0b48d90575d55f6fdb4313b768f0637f7a5d8ff0c 275,240 bytes
- `provenance.json` 7500ba6175c9e2f09a379b74a283542b6e7e4e637714a2006f0e68a86c44b348 1,048 bytes
- `rendered.html` 7bb4a810ad56f4620b7e1f2b14591c31b935a76a017c72cae93435ef05b8d088 302,107 bytes
- `screenshot.png` a69607bd90cb0667ecdd5ab2e0191ae6c1534b599824084514dbcc1055712cde 940,580 bytes
- `text.txt` 84742b6e86fb259d4db36361e86d4b739c6cd09184337f365f5e2958271f5379 9,221 bytes

### [Government websites shut down in Finland over critical security flaws - Helsinki Times](helsinkitimes-finland-shutdown/index.html) [original ↗](https://www.helsinkitimes.fi/finland/finland-news/domestic/29412-government-websites-shut-down-in-finland-over-critical-security-flaws.html)

**Helsinki Times** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `helsinkitimes-finland-shutdown`

Valtori began restricting incoming public traffic at 12:45 local; patch scheduled 17:00 Finnish time; restore after checks.

capture 20261022T112845Z · HTTP 200 · https://www.helsinkitimes.fi/finland/finland-news/domestic/29412-government-websites-shut-down-in-finland-over-critical-security-flaws.html- `headers.json` 8cfe23a4571454de0ce2c8804eef8e57888689f139258fc400bc4074345e22c4 1,424 bytes
- `page.html` aae25312014733334061a2a0cedc5e7a800cfd4d711717e78fe9f492a1923fb1 74,712 bytes
- `provenance.json` 616d5f35071adec7fda82e308c994ebebbe96580f9f0d09c2ca595e95eca3565 1,204 bytes
- `rendered.html` 86c43a2ba4b2b595bc14316aefdf8f5d08736e778a980690075033168a6258ec 155,636 bytes
- `screenshot.png` 9c23d876698ad3081c6ac7846ed601a071d01e5b57de834755b1ef846cc2d26a 701,429 bytes
- `text.txt` 524315badf6e56339623c59b54db482dffa48d62583a026e7134dae4bb30d118 6,660 bytes

### [Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress](huntress-php2shell-rapid-response/index.html) [original ↗](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities)

**Huntress** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `huntress-php2shell-rapid-response`

As of 16:30 ET (20:30 UTC) 21 Oct: no exploitation observed on partner systems; no PoC built or reproduced; not aware of public exploit code.

capture 20261022T112853Z · HTTP 200 · https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities- `headers.json` 39dd8f8ed13d1e993a95f88bddf69702d0cd23e3aef38da50d65068f495d1cff 7,379 bytes
- `page.html` 39d79180c85ccbc63f3acbf3bb0f076d56933f94e5fa8a5be8dafc3ca3160c7a 913,455 bytes
- `provenance.json` 23031a4937921ef79d80fb4b2546b9d7054028e640b9babec2c44d9f66dee0a2 1,102 bytes
- `rendered.html` 41e5af59038a7155953c6809d743ca579e2eeb7cdc503f13f6e3550ea920d970 1,115,188 bytes
- `screenshot.png` a4d89c5787921c4fe23ea13f25dc2d0104756a669450c44aad83ad220d9bc3a7 1,862,920 bytes
- `text.txt` a83d744768109a61f623c0d4de5df589cde5c1e0da114b25d62a7321f159455c 17,843 bytes

### [PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva](imperva-blog-php2shell/index.html) [original ↗](https://www.imperva.com/blog/php2shell-vulnerability-updates/)

**Imperva Threat Research (Nadav Avital, Bar Menachem)** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `imperva-blog-php2shell`

Five demonstrated techniques, three via session upload progress; attack complexity high; ~67 KB memory disclosure; no matching traffic in pre-disclosure monitoring; '69% of websites whose server-side language is known'.

capture 20261022T111855Z · HTTP 200 · https://www.imperva.com/blog/php2shell-vulnerability-updates/- `headers.json` fa04ad94125d615ccc22bfe0f44544c8737419ff06a9d85acf2e5e4776931849 3,102 bytes
- `page.html` b659e89f8fb17c9833c2b8d60454655d038e41bd867043684aff25984c3bf6e2 243,832 bytes
- `provenance.json` a2f25ae502d617f41375750794a46ff83e8a433361944da98d0daab48bd962ec 1,022 bytes
- `rendered.html` cb3120b21b6f0c89f3af549534f6b8ce3e381a19e5c6eecce3ec513cb1d18d5a 301,023 bytes
- `screenshot.png` 1f96ba16ce949cfd1d6f4051df3dd2b7910754612bb6fae060c14d96950f9c9e 1,932,384 bytes
- `text.txt` 3da873bdb21219a616245663c1c5bfccb9d8d5db507092c70bb2c20519e031e4 15,842 bytes

### [UK councils and Met Police among sites pulled offline after NCSC alert | Insurance Business](insurancebusiness-uk-councils-met/index.html) [original ↗](https://www.insurancebusinessmag.com/uk/news/cyber/uk-councils-and-met-police-among-sites-pulled-offline-after-ncsc-alert-594424.aspx)

**Insurance Business (Matthew Sellers)** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `insurancebusiness-uk-councils-met`

Edinburgh and Oxford councils and the Met Police unavailable; Bristol, Lambeth and Barnet errors; Dutch NCSC offline; Valtori; Cloudflare CTO 'STOPGAP only'; Unit 42 22.6 million systems; W3Techs Aug 2026 ~70%.

capture 20261022T112225Z · HTTP 200 · https://www.insurancebusinessmag.com/uk/news/cyber/uk-councils-and-met-police-among-sites-pulled-offline-after-ncsc-alert-594424.aspx- `headers.json` 3d07c50bb43d9b0530e97433ee53da60ac0afc3cb28ee547618e5cce5e68d8d0 1,370 bytes
- `page.html` 3cf31852fd2bdd575e2b3cb127faa507e947fbd823c16befeaca3901daa676a4 223,253 bytes
- `provenance.json` 3d2dc87a1364e14f154fb92ea66b98c53bcf8b335f6ab4488be62bf869fe6071 1,200 bytes
- `rendered.html` 2db316644de0dc7e608587a786f6571e83708d928733ae4a8a227c5b31f3b1cd 400,028 bytes
- `screenshot.png` 143c99a16e7b571c7069d3cc0b3396802d75971d4ec8a883b902db2b02a15061 2,153,476 bytes
- `text.txt` 89357150e0bc8363b71ef8b709b7e047e0503f20791d7d062a758550609d0d20 7,188 bytes

### [PHP Foundation angered by ‘clumsy’ disclosure of vulnerabilities - ITdaily](itdaily-php-clumsy-announcement/index.html) [original ↗](https://itdaily.com/blogs/software/php-angry-clumsy-announcement/)

**ITdaily (Jens Jonkers)** · news · secondary · captured · published 2026-10-22T09:36 (local, Belgium) · added by `claude-story-site` · `itdaily-php-clumsy-announcement`

Secondary: the Foundation 'caught off guard'; 'aware for two years of at least one vulnerability'; Ecosystem Security Team since May 2026; a VUB professor on the disclosure window.

capture 20261022T112142Z · HTTP 200 · https://itdaily.com/blogs/software/php-angry-clumsy-announcement/- `headers.json` 9c96a4285eed59d7470a9a983facb2964a82b6539cf0dd85887c0cb4b2fb0740 606 bytes
- `page.html` c93c7d6384ee8c4a47a08e5ac9e9aa9dc1d96089fc05044a194b1220e7c9d4ed 130,955 bytes
- `provenance.json` ebec1bc848714c197d387275d82b755dbb12649df06083c9d18633217827d2a5 1,049 bytes
- `rendered.html` b634233f4e687df8538e68d9f0af3af145ab15dc5bbe966f7a1457f2350eaf4a 134,246 bytes
- `screenshot.png` 5a11124ea720acd8ae8b3af6b0df0a3925b72abfa059d3db627464c578ae2700 1,036,421 bytes
- `text.txt` 27772c396e4bd60e2e200b2ba8db0273291060cad355f3927bdcd0ee9c2aa7ad 6,719 bytes

### [PHPにおける複数の脆弱性（CVE-2026-109618、CVE-2026-109619）に関する注意喚起 (JPCERT-AT-2026-0033)](jpcert-at260033/index.html) [original ↗](https://www.jpcert.or.jp/at/2026/at260033.html)

**JPCERT/CC (Japan)** · advisory · primary · captured · published 2026-10-22 · added by `collector-gov` · `jpcert-at260033`

JPCERT-AT-2026-0033, published 2026-10-22, updated 2026-10-22 (wording fix in section V). Advice: apply fixed versions promptly 'after sufficient testing' and investigate for compromise. No offline advice. Says PHP is widely used in Japan. JVN entry also listed 2026-10-22 14:20 JST.

capture 20261022T081700Z · HTTP 200 · https://www.jpcert.or.jp/at/2026/at260033.html- `headers.json` cbc1e287bde3882e41d91bfa7315dcbaccf9a996c0a383acc62f9095fbe921eb 605 bytes
- `page.html` 85db7a09e865158643525fef5aa5cfc69513aaf896fcb2da4562189d43decf44 31,008 bytes
- `provenance.json` 4ba4d01fa5ebe5235184ed530cedbac6cd8985446a10845775da38efa45aa5b9 1,013 bytes
- `rendered.html` c4ba52d8393f4189aade005389d1b8c2923eeb29f0d917a7221b5330cff3bf91 30,690 bytes
- `screenshot.png` 99789e60674ab7b0d3f01afbc2012337348a1434417d4820d6c89133f2d6ff64 722,717 bytes
- `text.txt` 1fea87241b307f92c5ddc2b16356954d947ec3e0f5ad55158315dc08d98127f5 8,327 bytes

### [JPCERT home](jpcert-home/index.html) [original ↗](https://www.jpcert.or.jp/)

**JPCERT/CC** · government · secondary · captured · published not stated · added by `collector-gov` · `jpcert-home`

Home page at 08:16Z: the PHP alert (2026-10-22) and a JVN item at 2026-10-22 14:20.

capture 20261022T081606Z · HTTP 200 · https://www.jpcert.or.jp/- `headers.json` ffa0d53fc7fd1c2d4339dd045991caa54d31c4515face33fcad2b50bfbfdb00f 605 bytes
- `page.html` 07612f480101608a837f0a0dfff30db2d1f5091eabb55fe048bf6546979e25f7 31,630 bytes
- `provenance.json` deeeef14fce691e60314064b4efa728667689e9676e5263b880005c0cdcc5ca3 917 bytes
- `rendered.html` b41d0ff975f9a0815c4626b027f239c76e939b2070f0e7221fdeef67c9615d21 32,010 bytes
- `screenshot.png` 0870f642b705aeed4116685bb2897f814fff8eb758a665a969b80be60f36dc81 1,483,609 bytes
- `text.txt` 0e3188607f06a768281c4dd19a88acecbe0e7fe6b5c20a312e9095a2a498dfba 6,293 bytes

### [Websites taken offline as ‘critical’ security flaw hits Met Police, Traitors and government sites | LBC](lbc-uk-websites-offline/index.html) [original ↗](https://www.lbc.co.uk/article/uk-internet-outage-php-websites-tech-5HjdkDd_2/)

**LBC** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `lbc-uk-websites-offline`

Met Police, The Traitors, government sites offline; fixes 'around 3pm UK time'.

capture 20261022T112915Z · HTTP 200 · https://www.lbc.co.uk/article/uk-internet-outage-php-websites-tech-5HjdkDd_2/- `headers.json` 61fade0ae97f79d231f97a5777f63b2e81a66ef6baadd7a7099a825dd6c29ef2 971 bytes
- `page.html` d4ed63db00e26889d772c2570efda5fb8fa6cce84a1d5826b8876ade8bf939bb 95,257 bytes
- `provenance.json` e04ec30a201ba0f120a5f1c48aafef2c90f871816cde4084454cdc63c5244456 1,094 bytes
- `rendered.html` e14de8389551e0d0109667c7b79786b3489c9cfa31c36fac97a71f6cf5398cb7 107,817 bytes
- `screenshot.png` 72e82d8825a1870d48523fc0b7ecfd8f99a8f2f981f64bb572699545b7dfd811 1,602,728 bytes
- `text.txt` 125176f10b5494a60744d6f6d3c7918b76c38477c6c229b636fbeb00b3bed173 6,376 bytes

### [php2shell: Inside the Leaked Critical PHP Flaws Triggering Emergency RCE Patching (CVE-2026-109618 & CVE-2026-109619) | Lorikeet Security](lorikeet-php2shell/index.html) [original ↗](https://lorikeetsecurity.com/blog/php2shell-leaked-critical-php-vulnerabilities)

**Lorikeet Security** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `lorikeet-php2shell`

Vendor explainer with an example Suricata rule (sid 2026109618) of questionable direction; no testing evidence.

capture 20261022T112438Z · HTTP 200 · https://lorikeetsecurity.com/blog/php2shell-leaked-critical-php-vulnerabilities- `headers.json` b7888c7584d4891b481a804cc3243ec9dff82d301a8ac2c7070c6b7f25bd5fe2 1,727 bytes
- `page.html` b74c194ddfc61843d47bd6ffa9d691718fab73fa370cf3c82d1cd24ea3f3f998 343,430 bytes
- `provenance.json` 38298cededb4b803f1214bfa4a6a30e1cdf06ddc417f0771577affd057d13e5a 1,123 bytes
- `rendered.html` 38608a412a2fb2a979d5821ccb1a9764037d3d2bbad075a509f0d25884973ae5 904,734 bytes
- `screenshot.png` 281038d16371213c89c2ce9df773de5a82e6eac69bdfe5c855e3975b02ac6387 8,419,643 bytes
- `text.txt` db7958824da2628a693fcca386ac3ea9994977209f017b245fab2d3e894cb349 37,837 bytes

### [Critical security issue affecting PHP](ncsc-news-php/index.html) [original ↗](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php)

**UK National Cyber Security Centre (NCSC)** · advisory · primary · captured · published 2026-10-21 · added by `collector-gov` · `ncsc-news-php`

NCSC Alert. Page: PUBLISHED 21 October 2026; JSON-LD dateModified 2026-10-22; HTTP last-modified Thu, 22 Oct 2026 07:30:02 GMT. Names CVE-2026-109618 and CVE-2026-109619. Advice: update; else PHP Foundation temporary mitigations; 'If you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated.' Wording differs from BBC's quote.

capture 20261022T080903Z · HTTP 200 · https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php- `headers.json` 642ad2462903a32f7050dae5e198654e710dadc0a6225333d96370031c7ede4c 852 bytes
- `page.html` 2d8e9e72ec5efa695b2d587a4af1bcb75662ead0add90b964cf767e8023ff4f8 225,168 bytes
- `provenance.json` fe3daad10ed2709f256ce5547b2a21d8b35120fe041248d698a63d75652a19fb 1,025 bytes
- `rendered.html` 0b839c8974dc2310cc6f85d334620ae5b5cd944842d6de180bf76938f5b6dcf5 761,056 bytes
- `screenshot.png` 260b9c91a3bf1a838fd1a81633415032eacd24ccaf249c11227903c6038b4544 542,775 bytes
- `text.txt` a18ceeb011a3fe6f0311d92399618b5231abb0f57f3b94ffd7371cab6eccc339 5,135 bytes

### [NCSC NL | Security Advisories (PHP banner: Ernstige kwetsbaarheden in PHP: bereid je voor op patchen)](ncsc-nl-advisories/index.html) [original ↗](https://advisories.ncsc.nl/advisories)

**NCSC-NL** · advisory · primary · captured · published not stated · added by `collector-gov` · `ncsc-nl-advisories`

Final URL advisories.ncsc.nl/. A banner is still the pre-patch text: 'bereid je voor op patchen', patch expected '21 oktober 16:00 Nederlandse tijd'; 'Er is een publieke Proof of Concept (PoC)- code beschikbaar, maar het NCSC heeft nog geen actief misbruik gesignaleerd.' Affects 'alle versies vanaf versie 5'.

capture 20261022T081605Z · HTTP 200 · https://advisories.ncsc.nl/- `headers.json` 3e389f62cb8a1de496ebc873bbcfb98ccf729f22e1ec56c94d0893bba1bef324 884 bytes
- `page.html` c0c4e5aa82e2eaec26497f7eb201c72888ecdcb1361964f73aab7b5dcc046c5f 240 bytes
- `provenance.json` cd3655ebd5a05e5e7a94cfc0438e17c9f78418f1c570bf5097613f30ba7612ca 980 bytes
- `rendered.html` f008b1f5da4c00459105f979db89eebc16702be90d3a6de1656acfab41951cc6 69,813 bytes
- `screenshot.png` 9bd5b7a047aff8b7f81e8c61b6f1ccc1475f7be1ad89a7d9d32a6f2aee84abbe 611,099 bytes
- `text.txt` b7e4ac6caf7d177d8b7e55fa8c587da75a1e78fafc951012d2d2595a6dfa5e8b 8,130 bytes

### [NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities](ncsc-nl-php2shell/index.html) [original ↗](https://github.com/NCSC-NL/php2shell)

**NCSC-NL (Netherlands National Cyber Security Centre)** · advisory · primary · captured · published 2026-10-21T15:25:00Z · added by `collector-gov` · `ncsc-nl-php2shell`

README: 'Readme last significant change: 21 October 2026 17:25 CEST TLP:CLEAR' (=15:25Z). Fixed releases: PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. Links to CERT-EU SA 2026-018 and ENISA CNW-2026-04. Holds the software inventory list (the NCSC UK cites it). Does NOT advise taking systems offline.

capture 20261022T080925Z · HTTP 200 · https://github.com/NCSC-NL/php2shell- `headers.json` dbef75c6f088a0a21eeac77ab2178aead9e625d6ed750dd4894fc7fb9537f297 5,443 bytes
- `page.html` 4e1f8dc6dd2c6d494b9d1229a0de601b0e1096e81337d8a4b5b06fa7c3c293ce 261,528 bytes
- `provenance.json` 939b683f13402c1f5d315ff79800619b30e3780d4eb31bfc2b17282148c8e03a 1,005 bytes
- `rendered.html` 323e0a19a3dd13c2b214ff7b1a8553eacac4c17bdfb8b8c1a9bf2032781934db 273,849 bytes
- `screenshot.png` a27d227bafcdfbc38ca5c431a5fb525aa95eeac6e7bfbe31c98ae8057c2e4d64 494,937 bytes
- `text.txt` 8944dd45c25fa7c1fc1c6f3e2a646d86fe0849a83248fe1f91cec791a58589e6 4,852 bytes
capture 20261022T084815Z · HTTP 200 · https://github.com/NCSC-NL/php2shell- `headers.json` dc374a245415e7981501c8d9adea6d18ac20101116a21380bafe62b351dba7c0 5,453 bytes
- `page.html` 556efff0dd62f6bdf88e3ed5566f6f2213e828b2bbfeba7eef0b3cd3ac622057 261,276 bytes
- `provenance.json` 7544f40915d6c5cb74cdc60621deee2e3d7773de3a0191201caf4089fbd5d094 1,005 bytes
- `rendered.html` 42194f5b28315e862789c25ed7c3a2bbbfa3244da3bb68e8e3ff284f321ccd38 275,802 bytes
- `screenshot.png` c6a14bc8234e3b2b5692240e1f2821e9e80e51e52bd5bec2e89dcf3a7a8a1764 497,834 bytes
- `text.txt` f3eec24a226910fb8440714b4f44c40db5c5f7826f3c23b65aece1cc5775712e 4,854 bytes
raw, 3 files with SHA256SUMS- `commits-cca173c64ec5.txt` 4d4f80bd9da0076e2bd74323e947a05f1e0f1a246a5a25b2874dd9370b4a2ea9
- `php2shell-cca173c64ec5.bundle` 4a72bcc9bbc58e886df6eee7cc875bd5deab547f1028f7525a7e7e808859411f
- `software-list-cca173c64ec5.json` f0a17e96a336a8782231290acf4ba4a4f4fa469270c59a7c87a95da2207dad01

### [List of software with PHP dependency potentially affected by php2shell CVEs](ncsc-nl-php2shell-software-list/index.html) [original ↗](https://github.com/NCSC-NL/php2shell/blob/main/software/software_list.md)

**NCSC-NL (Netherlands National Cyber Security Centre)** · government · primary · captured · published generated from the repo's SPDX inventory; commit cca173c64ec5 at 2026-10-22T08:40:58Z · added by `claude-newsroom-lead` · `ncsc-nl-php2shell-software-list`

Pointed out by the editor as the source for affected systems. 674 entries at commit cca173c64ec5. CVE-2026-109618: Fix 46, Investigation 418, Vulnerable 206, Not vuln 3. The parsed list, the repo bundle and the tree are in ../ncsc-nl-php2shell/raw/.

capture 20261022T084807Z · HTTP 200 · https://github.com/NCSC-NL/php2shell/blob/main/software/software_list.md- `headers.json` ced0e6933669176a62c459545b9b58df2ecd44f502200c04ac548e8bf513cf2d 5,624 bytes
- `page.html` b6810b0801213bba67b7fff83b519ffc971c4271b217cf2ab4083ecee77d2c81 223,836 bytes
- `provenance.json` d02a4a269f2919ede5233e84a57e72d3dc9adb56e4d98d2ca23fb319384925b9 1,059 bytes
- `rendered.html` ed0e84fc69079d5df2c192b657719a25a29e9ce62aae2034ece866b27ee6c079 288,875 bytes
- `screenshot.png` c610a27540c7c58e4e02cc90bc268c1a5f5b8bd8295fd543badb47cfcdad0e3c 137,355 bytes
- `text.txt` 83f3aa60070e20b847980ff396e3f2468de1e291562a6a16a69f6a20ffbe2004 1,255 bytes

### [UPDATED: CVE-2026-109618 and CVE-2026-109619 affecting PHP](ncsc-nz-alert-php/index.html) [original ↗](https://www.ncsc.govt.nz/alerts/cve-2026-109618-and-cve-2026-109619-affecting-php/)

**NCSC New Zealand** · advisory · primary · captured · published 2026-10-22T09:15+13:00 (=2026-10-21T20:15Z); updated 10:20am 22-10-26 NZDT (=21:20Z) · added by `collector-gov` · `ncsc-nz-alert-php`

TLP:CLEAR. 'The NCSC is aware of reports of active exploitation.' The only agency so far to say this. Advice: update to fixed versions 'as soon as possible'; investigate compromise. No offline advice.

capture 20261022T081700Z · HTTP 200 · https://www.ncsc.govt.nz/alerts/cve-2026-109618-and-cve-2026-109619-affecting-php/- `headers.json` 5e5b7ef0258116f0d6925dab7f8189e2223e414a58521729043ca4f399ceabcc 1,992 bytes
- `page.html` 9f3205c8338c598bedc1fa1f1b0726243fd7cce324d6d0a797a7c55fbd277915 49,604 bytes
- `provenance.json` 7536377248a3645980d9a70e1d2e6c3bb2f1c0e799ff9ccd12b4320bd1724b01 1,049 bytes
- `rendered.html` 32cdd5364dd2c631a73c0c834763cf3cb9b776145d2ebf5e4f3376e25e89758e 41,928 bytes
- `screenshot.png` 4dd2cb007efcf0696650ebca1087f184c6ed83297bc6f80dd678d9f6954146ac 528,343 bytes
- `text.txt` 992fc3b6639069a9eb6618d9f6a71e994633960f0d6d4c77bd74bc797caa5301 3,799 bytes

### [Alerts listing](ncsc-nz-alerts/index.html) [original ↗](https://www.ncsc.govt.nz/alerts/)

**NCSC New Zealand** · government · secondary · captured · published not stated · added by `collector-gov` · `ncsc-nz-alerts`

Listing at 08:16Z: the PHP alert, dated 22 October 2026.

capture 20261022T081605Z · HTTP 200 · https://www.ncsc.govt.nz/alerts/- `headers.json` 74c848feb39a21fb80f489bb294b8d8a697fe6fdae03a6c61098de514241564c 2,034 bytes
- `page.html` 328191a093edcb0fb9ff08b20687f3c271db0b69eb58c770700dbfdfa080da96 75,111 bytes
- `provenance.json` 1e8d90e0d23cf4b63e37636b005fac4be349ebd5ce37cd39f3e8e921d84644fb 894 bytes
- `rendered.html` ccc94fffbb92d25658fbb11c5935488c45109113a44b5ec6bf775ad2240cea3f 53,664 bytes
- `screenshot.png` f9033cc86d53addc1cf8ed9db6855d4e30e30eec050db17bec1d47beb99651ee 226,803 bytes
- `text.txt` d1c97bbc45ba4cc7861035a6f606f1bc1c7b782b44ce8bdc279c7143640f4a5f 1,276 bytes

### [PHP Vulnerability: List of Websites Powered by PHP as Hacker Threat Prompts Scramble - Newsweek](newsweek-php2shell-websites/index.html) [original ↗](https://www.newsweek.com/php-vunerability-php2shell-issue-websites-hack-server-12601225)

**Newsweek** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `newsweek-php2shell-websites`

Secondary: Wikimedia Foundation quote 'taken down a number of other systems as a precautionary measure'; no evidence of US federal sites compromised or offline.

capture 20261022T112237Z · HTTP 200 · https://www.newsweek.com/php-vunerability-php2shell-issue-websites-hack-server-12601225- `headers.json` b6ede4c5fe94adc6fedb71cb10b74af567162d6452ec0218be0bb8c7b17748dd 2,453 bytes
- `page.html` 02014f6004d880e2069129f15e86dde9bc0690358b12879271104aa686ed7af0 559,900 bytes
- `provenance.json` 3924e8c0bcf61c3ac2c4018ed3883377b700cd1ff8b1868e156d09adbb78ffc1 1,106 bytes
- `rendered.html` ba7e1618e4d6808ff4982067fda5725d0e4c5a6fcfd94dc91b4b6bd65068189d 815,834 bytes
- `screenshot.png` 3d81fb9fa70f4b8446dc70da529dd38f40b9e9caf64fd826a7c1fd282de0d3b0 2,773,005 bytes
- `text.txt` 323ccf78f4d6f2d0d0a657e9792a88bb3b05ac66492762caa614e9fe02343294 11,698 bytes

### [NSA Advisory: Critical Patches Recommended for PHP Vulnerabilities](nsa-press-php-4630238/index.html) [original ↗](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-critical-patches-recommended-for-php-vulnerabilities/)

**US National Security Agency (NSA)** · government · primary · captured · published 2026-10-21 · added by `collector-gov` · `nsa-press-php-4630238`

Press release dated Oct. 21, 2026 (no time given). Nicknames the bugs 'PHP2Shell'. Recommends patching, inventory, enhanced logging, replacing EOL PHP; 'If an immediate update is not feasible, it is recommended that organizations take the system offline until it can be fully mitigated.' Says the risks 'require immediate patching across United States Government departments and agencies'.

capture 20261022T080954Z · HTTP 200 · https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-critical-patches-recommended-for-php-vulnerabilities/- `headers.json` 97a8c93336e9eaf70c80dd55bf2a30afda4f796323bb1e628388046b2d71ff58 671 bytes
- `page.html` 18db3cea62d9017227ca3bc12cc73fe965e84f2a0d946dbc0278c4772dd415f3 98,539 bytes
- `provenance.json` 246b632f5be873be48cc8894fb4abdb03858ee784e155a5f703c690e0c937495 1,286 bytes
- `rendered.html` 0e42d4e7ce3e0af33f09f09b458d895320523102285301139861be8ba95f5889 122,356 bytes
- `screenshot.png` 1bc158a28beb2de8ef2533cca0ddffbec42a196ae7094ca2d019ff076cd27725 992,031 bytes
- `text.txt` 8a8553ea1ffcd794a5f6a39dea4162c7f84f0737d5061577a3e569cb39b79154 4,995 bytes

### [NSA Cyber on X: Effective Immediately ... two critical vulnerabilities](nsa-x-2112903220209098897/index.html) [original ↗](https://x.com/NSACyber/status/2112903220209098897)

**NSA Cybersecurity (@NSACyber)** · social · primary · captured · published 2026-10-21T13:45:58Z · added by `collector-gov` · `nsa-x-2112903220209098897`

First NSA post (pinned). Time from tweet snowflake ID = 2026-10-21T13:45:58Z; the page shows '13:45 · 21 Oct 2026' (UTC browser). 10.1M views at capture. 'If an immediate update is not feasible, it is recommend that organizations take the system offline until it can be fully mitigated.'

capture 20261022T080954Z · HTTP 200 · https://x.com/NSACyber/status/2112903220209098897- `headers.json` 2b72f04731267bb06c6ed80fb9fab697c55697ef2b83303924c315720ed63729 9,020 bytes
- `page.html` 49362e7db1112702cb4586ed77daa898c86293d85b5ebe33b7a7dca7db1396a2 139,058 bytes
- `provenance.json` 569e1386915c3d850f140375196be63051f6099dd3eaa803bee46f3d014e8984 1,240 bytes
- `rendered.html` a95403e3cb7230cb93a3aad7f6f4a09998596f2636f7516355cf3d52bb8fcf58 162,779 bytes
- `screenshot.png` f9e02ad5c04f114f4ab6cc0cd14b556924d445869fb512f4306683da40d50564 452,042 bytes
- `text.txt` 92ebce791a7b35429d2fee94427932a19b1629de3821a52201648a58298d52e7 1,811 bytes

### [NSA Cyber on X: UPDATE: Specific mitigation guidance ... now available](nsa-x-2113068811058622971/index.html) [original ↗](https://x.com/NSACyber/status/2113068811058622971)

**NSA Cybersecurity (@NSACyber)** · social · primary · captured · published 2026-10-22T00:43:58Z · added by `collector-gov` · `nsa-x-2113068811058622971`

Second NSA post, from the snowflake ID: 2026-10-22T00:43:58Z. It links (t.co/nuXgQ10Fzc) to the NSA press release 4630238. 206.4K views at capture.

capture 20261022T080954Z · HTTP 200 · https://x.com/NSACyber/status/2113068811058622971- `headers.json` 9292b5863f63684cb58479f72ed4579062a1ff66108183ddfd21a51a34f25f60 9,022 bytes
- `page.html` 8b2c9d9cbd6c8cfa6e5614e7900653b6bcddb21e5d8e4a0a880b9613ae9d1bfe 166,142 bytes
- `provenance.json` 0931b8c67b66649c978bd87fd385c5c0e597b091e5e840db5dc9d4d1e1b63c9d 1,154 bytes
- `rendered.html` 3a297e1972ba61e2d78a5ca5842af0507e79e8d8b04aa8c7dcfa311794d9242c 167,035 bytes
- `screenshot.png` 846daf6b3e0004aee5355c16bf1ad5d57544d6b38547e5cf26d513a0dc8d168a 224,980 bytes
- `text.txt` 899e5ba4af69c5311210a846d98721e674abded497de292dfdc4af17b2ff1bd3 2,052 bytes

### [NSA Cyber (@NSACyber) / X profile timeline](nsa-x-nsacyber/index.html) [original ↗](https://x.com/NSACyber)

**NSA Cybersecurity (@NSACyber)** · social · secondary · captured · published not stated · added by `collector-gov` · `nsa-x-nsacyber`

Profile timeline at 08:09Z: the pinned PHP post plus the UPDATE post; 201.8K followers.

capture 20261022T080925Z · HTTP 200 · https://x.com/NSACyber- `headers.json` 9fa8661bfa8f332a71ed3f88de6e09033b05073ba537b3d891f1b4209bf1c757 9,022 bytes
- `page.html` 35b05885b38c909cd06bc0f6617a32454843249a5c4d5c92274ca3a543b98310 160,043 bytes
- `provenance.json` 0680efdf34c9fb08e25e730dbadcc178f7f0a02d64d82260f9802d4fdaf70a00 893 bytes
- `rendered.html` ae4abd70be7db953acec8f33cae64b339eb2729b8661c3191dc88e62eb17ee1d 198,521 bytes
- `screenshot.png` 20541dc8b918cda68c8be3b4a94e4698a53f3edb149d38ba9d8344210189f384 1,255,100 bytes
- `text.txt` 5889a1c26173dac8ee58b5269e4f78aeb57dc93520afa220d496e634b5e5b7c0 2,388 bytes

### [nitter.net (shutdown notice, no tweets)](nsa-x-nsacyber-nitter/index.html) [original ↗](https://nitter.net/NSACyber)

**nitter.net** · social · secondary · failed · published not stated · added by `collector-gov` · `nsa-x-nsacyber-nitter`

Mirror is dead: it serves only the maintainer's 10 Oct 2026 notice about X Corp cease-and-desist letters. xcancel.com/NSACyber returned HTTP 451 via curl (not captured).

capture 20261022T080925Z · HTTP 200 · https://nitter.net/NSACyber- `headers.json` ab425e76be267227a6680e0572e20c30271e2d99585b0cb665f948349e7e5e22 700 bytes
- `page.html` 846a9048bdd79311b1c92ef549dc68d73a61edd0f9832264cea107686a3f53cc 12,341 bytes
- `provenance.json` 5866931f9bcffc1f87e58582a3b73e4fd0fe9414f675213c27278464589fa4c8 895 bytes
- `rendered.html` 21e41f57eb9abbe1a4b2db26e202689f711d079cff963c4af7c549714eccd108 12,292 bytes
- `screenshot.png` d179e4f97e7b7e0371b33c4fc9e9dd245980aa3bf0ef5add188775144552c848 162,950 bytes
- `text.txt` f4e954159062308642561f65d6f65c068c8ee1001bcafdf6e9388181a78d2d93 1,513 bytes

### [NVD - CVE-2026-109618](nvd-cve-2026-109618/index.html) [original ↗](https://nvd.nist.gov/vuln/detail/CVE-2026-109618)

**NIST National Vulnerability Database** · cve · primary · captured · published 2026-10-21T14:17:09.357Z · added by `collector-primary` · `nvd-cve-2026-109618`

NVD page did not render in two Playwright captures (empty text); the authoritative copy is raw/nvd-api-2.0.json. NVD published 14:17:09Z, lastModified 17:18:24Z, status Modified. Only CNA (security@php.net, Secondary) CVSS v4 9.2; no NIST primary score yet. NVD CWEs: 416, 755, 824, 1325 (no 1419). No CISA KEV fields.

capture 20261022T081218Z · HTTP 200 · https://nvd.nist.gov/vuln/detail/cve-2026-109618- `headers.json` f81072c6a6dc3dda5884e2b701c37879b7d8762357ffa7bd4ea88ab95f9e5d6a 1,414 bytes
- `page.html` 5218b57d88785ba853fce0de8804f8994d73d4cb3209339fa458c4a5cbb9881f 2,453 bytes
- `provenance.json` f9105904aa37fc65ae54d1cb66b08b59b354c3eb7b20bf7cc925bd7ff4cfce78 935 bytes
- `rendered.html` b4880a9e6a29cbee557232a66f9db3531b225dd95a517433c6e326be8bb41e87 2,827 bytes
- `screenshot.png` 442aa587ff9ee582c291e7c7a8bca102504856b7a4db838cb313226e016f993e 106,759 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes
capture 20261022T081302Z · HTTP 200 · https://nvd.nist.gov/vuln/detail/cve-2026-109618- `headers.json` 5d77eaec3eb1fe5d7fb3a76a35571380e31671576d24b40c26f0f87d75f2c610 1,414 bytes
- `page.html` f372c9f8983a6331efb78d85ea53abc653d4bbe75457c02c9a25d9cc1ec2086e 2,453 bytes
- `provenance.json` 578b5687fe8afa3ad4f74ab69b8ca2471a0b0ee0a650e832021623cf9e346931 935 bytes
- `rendered.html` 2aa4037a7f7c9c97111573860083b648f53df74a60cea8fc7f9205b76d01f36e 2,827 bytes
- `screenshot.png` 8d848319be976cd91ac761f8f5b19ff3d8547393428ff570f273a774b5094d39 106,512 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes
raw, 1 files with SHA256SUMS- `nvd-api-2.0.json` dd864fa6ed53d4b549d2429fad6a22878ddb5a6def44b80cac0628cf4fdab438

### [NVD - CVE-2026-109619](nvd-cve-2026-109619/index.html) [original ↗](https://nvd.nist.gov/vuln/detail/CVE-2026-109619)

**NIST National Vulnerability Database** · cve · primary · captured · published 2026-10-21T14:17:09.823Z · added by `collector-primary` · `nvd-cve-2026-109619`

Page rendered only as 'Loading CVE Information'; use raw/nvd-api-2.0.json. NVD published 14:17:09Z, lastModified 21:17:52Z. CNA CVSS v4 9.2 only; no NIST score. No KEV fields.

capture 20261022T081219Z · HTTP 200 · https://nvd.nist.gov/vuln/detail/cve-2026-109619- `headers.json` fc8d0ec5d6feaed052fd64b49abaebe2394f7ef3bc2ce70aee91e20e1306822e 1,413 bytes
- `page.html` fbdf9ac8177380bc8093bab92baaa18402cc52721b3aaa5b037cb507c15a3bf3 2,453 bytes
- `provenance.json` bad76168518f8666d20502a4cb32e9b3425e785e7abbf63160cbd9081db807b5 944 bytes
- `rendered.html` 3784d224686072278cb9ed34c55c7390353818b2d9b35535eb289099d5bb536f 31,323 bytes
- `screenshot.png` 56539f358f1226f93c35cc6828cee0c2edbcda7da8a3fce9e8deaad68f133fea 106,528 bytes
- `text.txt` fbcf781e4294ea8f1f693ce52cf0e7c6ff9e8dff930df337294d54fb9f849466 839 bytes
raw, 1 files with SHA256SUMS- `nvd-api-2.0.json` 627fdaed31c96626e2dcc8af24a6acab1b2da1658bb32b5cf627e30149a0b61c

### [Patch the Planet: global response coordination as agents uncover critical vulnerabilities](openai-blog-coordinated-disclosure/index.html) [original ↗](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)

**OpenAI** · researcher · primary · blocked · published 2026-10-21 · added by `collector-researchers` · `openai-blog-coordinated-disclosure`

openai.com served a Cloudflare 'Just a moment...' challenge (HTTP 403) to capture.mjs, curl and WebFetch at 2026-10-22T08:11Z. The 403 capture folder is kept as the record. Content known only via secondary quotes; another agent should retry. Retried by claude-story-site on 22 Oct: still blocked. Retried by claude-story-site on 22 Oct: still blocked. Retried by claude-story-site on 22 Oct: still blocked.

capture 20261022T081113Z · HTTP 403 · https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/- `headers.json` 7b02609d3cb8321fcd39f1fb944357b1becd2b3914b213682188380e551a576e 1,912 bytes
- `page.html` fdf2d9f575486a9ace314ca2636c5ddac6e6cbe0cb71fbd74c561248b86caef2 10,672 bytes
- `provenance.json` 044271cf8e68e02415a432222e0036e63e3bc6ba426046d653313c6cf329a96e 1,012 bytes
- `rendered.html` 582d07e3d24a3e25bdb6f9515a3ecee4de66710e90c88b8fe2bb35f6457f1387 11,479 bytes
- `screenshot.png` c3713ab2f5047798e977f0bad1562ea67d8aa85432c230ecbeb28d7c937cb5dc 13,108 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes
capture 20261022T112413Z · HTTP 403 · https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/- `headers.json` e4f85b63820ea6efd08d11267c2b64182f40b903e674511097639f35151ff850 1,914 bytes
- `page.html` db092a078bc5df2a4c7258208dd350e18d58597541c27492bb6085ddc605b519 10,672 bytes
- `provenance.json` adbd882dc23ca47f5c3ce16c95f07213ed270f28011521f7beade694144a3cb0 1,012 bytes
- `rendered.html` 727b7be84beefe987e85a9a6d99200779878441c04443791f3ee6aa992118351 11,479 bytes
- `screenshot.png` c3713ab2f5047798e977f0bad1562ea67d8aa85432c230ecbeb28d7c937cb5dc 13,108 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes

### [OpenAI models help researchers uncover critical PHP security flaws](openai-community-php-flaws/index.html) [original ↗](https://community.openai.com/t/openai-models-help-researchers-uncover-critical-php-security-flaws/1408490)

**OpenAI Developer Community (user 'sps', Leader)** · forum · secondary · captured · published 2026-10-21 · added by `collector-researchers` · `openai-community-php-flaws`

Forum repost of OpenAI's announcement text, Oct 21; links https://github.com/openai/php2shell-checker (Codex skill).

capture 20261022T081721Z · HTTP 200 · https://community.openai.com/t/openai-models-help-researchers-uncover-critical-php-security-flaws/1408490- `headers.json` 86f75f0dcbf3bc611bd0c24cc8c87f49138270eaac36ff55f379acd57638d537 1,273 bytes
- `page.html` 9b1e1cbea269bc3fe068f7344d39a81937b9ec473044047d9d0700cb653af679 296,980 bytes
- `provenance.json` 1394b5dabf1a6c5064c6bd0a2a0750815ffb787cf14f7155f7a1c680a5566c8d 1,153 bytes
- `rendered.html` f20e90bdf364618ef6f4900343a7e3abbdb5e6006e628ae4e80a8b92bd8bdf47 624,051 bytes
- `screenshot.png` e3138cd2f1d4e9539051514491c494acd19c7c4afffabe913081dd1ef8d3a691 370,209 bytes
- `text.txt` 43afe7a0a3b96a86e52cbeea1c6ae41560bab1566da848fc4f9067152f739cd5 3,504 bytes

### [Patch the Planet (launch announcement)](openai-patch-the-planet-launch/index.html) [original ↗](https://openai.com/index/patch-the-planet/)

**OpenAI** · researcher · primary · captured · published not stated · added by `collector-researchers` · `openai-patch-the-planet-launch`

Cloudflare challenge (403) at 2026-10-22T08:17Z. Launch date reported by secondary sources as June 2026 (unverified); Calif says invitation came by July 30 2026; BBC says PHP Foundation joined in July 2026. Retried by claude-story-site on 22 Oct: captured. Retried by claude-story-site on 22 Oct: captured. Retried by claude-story-site on 22 Oct: captured.

capture 20261022T081658Z · HTTP 403 · https://openai.com/index/patch-the-planet/- `headers.json` dabb6d316b2a9ca13a6a49cd3d11a59538e1df05d7bd684ec04dd3ff4a830c61 1,920 bytes
- `page.html` 1debac9983b263577c7488d66e2818ce992f602955f908219aa39abff4854500 10,484 bytes
- `provenance.json` eecdf8db164ee1e68d9f8e7f6c9705554227dbe3f65fa9ddf547d56f2aa0fb54 940 bytes
- `rendered.html` 80b0289e281954fb599df1170766a5d6f8a6bdecad2a5b444dd54e0a109542ab 11,291 bytes
- `screenshot.png` c3713ab2f5047798e977f0bad1562ea67d8aa85432c230ecbeb28d7c937cb5dc 13,108 bytes
- `text.txt` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 0 bytes
capture 20261022T112430Z · HTTP 200 · https://openai.com/index/patch-the-planet/- `headers.json` cb97f3646fc464783030ad6f26b7191a2153e7964501252ae1fd40d86db2fbb7 3,536 bytes
- `page.html` ad9f31cd0180d78e020821254328f835f4aa9b45f55d380ac5c4ba0e0fbd0a12 471,833 bytes
- `provenance.json` a4668895879d2911dd924db2f462ac177db64b7dd8c7343b68e6f57540c78da8 1,007 bytes
- `rendered.html` 66a7a5d479dc9553dcba734583b2b1a930f2ea9a4284417125fb1ec24ff54088 471,423 bytes
- `screenshot.png` d24aaf68ae28b9ffd320d4f4bec241764fe84587ae5932454b99c3780aafe6b2 1,532,182 bytes
- `text.txt` 1bc9a32356688dd3f82be20cb4c54b29c9d9d1fd3d04278dcdccb0fe504c2db4 13,908 bytes

### [Re: CVE-2026-109619 thread (21/16, 21/17, 21/23, 22/2)](openwall-oss-security-109619-thread/index.html) [original ↗](https://www.openwall.com/lists/oss-security/2026/10/21/16)

**oss-security list (replies: Aaron Rainbolt, Yves-Alexis Perez/Debian, Christian Fischer/Greenbone)** · forum · secondary · captured · published 2026-10-21T15:24:37Z · added by `collector-primary` · `openwall-oss-security-109619-thread`

raw/ curl copies of four replies. Fediverse report (fedi.katze.sh/@elise) that the 8.5.12 fix may be incomplete or a different new bug; Canonical reportedly told by PHP 'unrelated and not a real issue' (second-hand, via Matrix). Greenbone notes 7.4-8.1 are implicitly affected.

raw, 4 files with SHA256SUMS- `oss-security-2026-10-21-16.html` 6a76141ae5a06584e8c6f6e61f4c455ce078152d6c56ce05206ee1c9ef7acccf
- `oss-security-2026-10-21-17.html` 059317aa4a1f458e19196e6add44a6b3106632b82c82f104a5b83d0df6fbe09f
- `oss-security-2026-10-21-23.html` 39555f34a419becc6a47480eabb369e05f4bac6ce06e9e3843e4dfcb5c99801b
- `oss-security-2026-10-22-2.html` bbc0f0fc06953b13308925334e39e7808796e46ea9505630917762502996bea2

### [Upcoming Critical PHP Security Release](openwall-oss-security-2026-10-20-34/index.html) [original ↗](https://www.openwall.com/lists/oss-security/2026/10/20/34)

**oss-security list (Alan Coopersmith, Oracle)** · advisory · primary · captured · published 2026-10-20T20:22:51Z · added by `collector-primary` · `openwall-oss-security-2026-10-20-34`

Date header Tue, 20 Oct 2026 13:22:51 -0700 (= 20:22:51Z). Quotes the php.net pre-announcement verbatim: scheduled 21 Oct 14:00 UTC, two vulns CVSS v4.0 9.2.

capture 20261022T081408Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/20/34- `headers.json` 716db9e977d3bc55b5045e260d9914e03196ed370f73c86c22880782e6a6a114 239 bytes
- `page.html` 46a94f610255e2ee75ab240c658666ef2589e34e4dd4fcb93b5c5e45fc9917d4 5,800 bytes
- `provenance.json` 04ff8e63e2b72caeb3d48ed4a44ecc28434a0414db9f8d59022e7b75af8ccb40 1,012 bytes
- `rendered.html` 5c80dc74b7328496b9f3ee62eef06aa707db7327bd0bcdd7ab9aa4f0c5a5a5d8 6,056 bytes
- `screenshot.png` c03f4fc0fefe0485485685cdf28d3e439a4b167b3022a946ee928be55cd4ee0d 120,872 bytes
- `text.txt` 57b273733e7d5fe658deca4275db17ad5fd01aeb06d84d973d55551983dfa392 1,415 bytes

### [CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption](openwall-oss-security-2026-10-21-6/index.html) [original ↗](https://www.openwall.com/lists/oss-security/2026/10/21/6)

**oss-security list (Jakub Zelenka, PHP security team)** · advisory · primary · captured · published 2026-10-21T14:41:54Z · added by `collector-primary` · `openwall-oss-security-2026-10-21-6`

Date header Wed, 21 Oct 2026 16:41:54 +0200. Official PHP security team announcement.

capture 20261022T081408Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/21/6- `headers.json` 716db9e977d3bc55b5045e260d9914e03196ed370f73c86c22880782e6a6a114 239 bytes
- `page.html` d43a7569e9b4ff185814a61ed2a17e0b058d4554558a9fee8e3a7a29810169c5 6,170 bytes
- `provenance.json` 9ab3756501428b0a77ed30c1d7ef15298f6a8edb131b1dc1436043a045609b4b 1,024 bytes
- `rendered.html` 0686ceff1b17dfaad334b167b4f0fbb9dc9cbcdc897203d210b9a1d7a9630269 6,426 bytes
- `screenshot.png` 6604c447fd5c7db94e64b0c9eeb75cd7301d461bd4f903890db31f9971d20236 146,765 bytes
- `text.txt` 2f2d3ff13f3a32b7b624d0c1f0e16f1d9172beabd52d42d7c20e504cb4cf8e4f 1,805 bytes

### [CVE-2026-109619: PHP 8.2–8.5 RCE via stale global state](openwall-oss-security-2026-10-21-7/index.html) [original ↗](https://www.openwall.com/lists/oss-security/2026/10/21/7)

**oss-security list (Jakub Zelenka, PHP security team)** · advisory · primary · captured · published 2026-10-21T14:44:06Z · added by `collector-primary` · `openwall-oss-security-2026-10-21-7`

Date header Wed, 21 Oct 2026 16:44:06 +0200. Replies at 21/16, 21/17, 21/23, 22/2 are in openwall-oss-security-109619-thread.

capture 20261022T081407Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/21/7- `headers.json` ffb76440772a63ed2186c00ea575b6e673ca3c7222ae89205c2bbb9de07e38ae 239 bytes
- `page.html` 81caae4759a5e9cd8e501221e12f31928874e9d16d7f7e8523e8cb1d36aa69fd 6,323 bytes
- `provenance.json` deeabe8cb21005c2d60c6ffcca6537969877e4411a8d1bbc88503109265756ce 1,028 bytes
- `rendered.html` b797761c288a2b59dad8b9bf3c0f4810af1b669a685b93013a7d6edc0e688638 6,579 bytes
- `screenshot.png` d6c5ab360073ebc5769973dc76493c74acf62cdc6e099f668ebffae91de551fa 154,322 bytes
- `text.txt` ceef70b4943f78182c26af1c04cdac8a7986a9c2c5f5cbb5385a73efdd112384 1,934 bytes

### [Oxfordshire council websites offline amid critical global security issue | Oxford Chronicle](oxfordchronicle-councils-offline/index.html) [original ↗](https://www.oxfordchronicle.co.uk/2026/10/21/oxfordshire-council-websites-offline-amid-critical-global-security-issue/)

**Oxford Chronicle** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `oxfordchronicle-councils-offline`

Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident'; Oxfordshire County Council also down.

capture 20261022T112935Z · HTTP 200 · https://www.oxfordchronicle.co.uk/2026/10/21/oxfordshire-council-websites-offline-amid-critical-global-security-issue/- `headers.json` ffb2fca308d4c4c89c5593350a364a6121becb966829713a17b3a99c2669d99b 1,048 bytes
- `page.html` 7603fb4868cc7b8a8fa437b7e2a8500726acf1332fd3f2252489e8f71471e5a2 472,071 bytes
- `provenance.json` 94eda260baf0d2faf05d45a4bb93b717ed498b664f3b724444bb046dba9ec628 1,169 bytes
- `rendered.html` e1614eeb5b71eb2bebf826c3131167eed9cefd83826c53632ff386d1a1a90afa 477,225 bytes
- `screenshot.png` 6e1d23c7119672f3ed76f38b59112885b43f6961b77abd0009ea77015e7ec42d 1,579,440 bytes
- `text.txt` 35c847290193f872826f6d65f370bcb6863fafe692817cc449f97431f350ae73 6,281 bytes

### [Patch the Planet — OpenAI](patchtheplanet-org/index.html) [original ↗](https://patchtheplanet.org/)

**OpenAI (Patch the Planet / Daybreak)** · researcher · primary · captured · published not stated · added by `collector-researchers` · `patchtheplanet-org`

OpenAI microsite. 'An OpenAI Daybreak initiative'; 'In collaboration with Trail of Bits, Calif, HackerOne'. Latest disclosure php2shell links to https://php2shell.com/. No date on page.

capture 20261022T081652Z · HTTP 200 · https://patchtheplanet.org/- `headers.json` 2efe5a08cc256108fdb7a72a5bdeb92c7596564181f1d63e2e31fd2b71e2a321 563 bytes
- `page.html` 280b5c18a8bb8c6254841014830e299d803e1d21ffd98141296156a2b5423bda 2,325 bytes
- `provenance.json` e6def2821be82e7593e0ea8682f9c24fdf763a48424e1814e65b815a1db3a78f 909 bytes
- `rendered.html` d347cfa4c1e9dc2c990b725259875a732e38470560bfc51b6bb21da3419d2662 7,680 bytes
- `screenshot.png` 0872d96463aabdeccdeb873b9cb455601fe9cdea8cb6b15f45c65a9e85f1bb75 285,779 bytes
- `text.txt` 3e32706fb7c0ed83bb988da8372dbca5e70dbdfebc6135060f3f777805f852ae 1,053 bytes

### [Today's PHP Security Release, and How We're Strengthening PHP Security](php-foundation-blog-security-release/index.html) [original ↗](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

**The PHP Foundation** · advisory · primary · captured · published 2026-10-21 · added by `collector-primary` · `php-foundation-blog-security-release`

Foundation's account of discovery, 2024 audit origin, leak timeline (20 Oct 15:00Z), Calif video, Chainguard embargo break (21 Oct 07:41Z). Page embeds an r/PHP comment thread (third-party, not Foundation).

capture 20261022T080901Z · HTTP 200 · https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/- `headers.json` c18914982a4c07d0a15b76e052d18c5f77f345016e356ea5cb65e766f0096b0f 857 bytes
- `page.html` 6b8915a800a5311c06544c4c47fe0e6b69586e9d75aeab49d2922a6a71446223 40,324 bytes
- `provenance.json` 2acdcc9ae9ee9e14a8960ed26727dee21b5561915fc6632378e78c9ae27a3f1b 1,218 bytes
- `rendered.html` 874a78d766936a3c9d375512a1882ac83f25921f0a1050ed8169c5f37ea72cf2 126,413 bytes
- `screenshot.png` f6eb5d0b42048f1570880df5c5e38adea3d5ee8635a98b8fef51f6234e5d2089 2,631,098 bytes
- `text.txt` a1be057adc1c5bfabad6a59007bd08960168346230f03967fba68f2402ab3f04 31,882 bytes

### [Security advisory: Critical remote code execution vulnerabilities, update now](php-net-advisory/index.html) [original ↗](https://www.php.net/archive/2026.php#2026-10-21-5)

**PHP Group (php.net)** · advisory · primary · captured · published 2026-10-21 · added by `collector-primary` · `php-net-advisory`

Official php.net advisory (archive anchor 2026-10-21-5) plus the 8.2.35/8.3.36/8.4.27/8.5.12 release posts and the 20 Oct pre-announcement on the same page. Feed  timestamps (00:05-00:35Z on 21 Oct; 20:32Z on 20 Oct) do not match the Foundation's stated times (release 14:00Z, pre-announcement 19:30Z). raw/ holds feed.atom and a curl copy.

capture 20261022T080901Z · HTTP 200 · https://www.php.net/archive/2026.php#2026-10-21-5- `headers.json` 42812c4d4f151d93b62d63d08b84b83e50a94a9e2ab79427924d5b5df582cc72 899 bytes
- `page.html` 3b02b9e9f8ebedb87cbe39a2852c8cc3205067f59572000c730844fbc4a03555 99,388 bytes
- `provenance.json` b1c9672106ace3646ee3912d7e4e87d94dc91cc5b60b9acc1066295675ce5014 948 bytes
- `rendered.html` a8cbeb0c17b3646681217db64cce0e0beb6dc71765bd1bad550f8e20170ef7d0 238,404 bytes
- `screenshot.png` 4727eaed5a4a5a90eb95aed5c3c0093702f427e1aae4bc63ed9ccfea2ca92da4 3,983,360 bytes
- `text.txt` df0b1bba3deae2823b3f7c6200d5a4fafa1625c51cde86e50f650e0b0726b31e 35,947 bytes
raw, 2 files with SHA256SUMS- `archive-2026.curl.html` 3b02b9e9f8ebedb87cbe39a2852c8cc3205067f59572000c730844fbc4a03555
- `feed.atom` 79c12996a433f66b2e2422e32d1dd5d4251c7c24531f75c3a0611f58dc1894a8

### [PHP 8 ChangeLog](php-net-changelog-8/index.html) [original ↗](https://www.php.net/ChangeLog-8.php)

**PHP Group (php.net)** · advisory · primary · captured · published not stated · added by `collector-primary` · `php-net-changelog-8`

8.5.12, 8.4.27, 8.3.36, 8.2.35 entries dated '22 Oct 2026' (the original target date), although they were released 21 Oct. Core entry: 'Fixed GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp (Avoid state corruption via bailout).' 8.5.12 and 8.4.27 also carry unrelated bug fixes.

capture 20261022T081558Z · HTTP 200 · https://www.php.net/ChangeLog-8.php- `headers.json` 7e0f775cb09c408472e389bec122b0fc703a450df430b26aca98e4539caf6f4f 892 bytes
- `page.html` 8d771e4a97a9457c8ff4dfff88d79661cf8b5d520666b8799a944f033e620e68 752,126 bytes
- `provenance.json` 08d9493b6d1480061ad20e23c5ea875c121bb9741f79ccf69dd923284133f1c9 919 bytes
- `rendered.html` 03ecb3465829e89ba578ae7bc7f36881fbbd37d9bc77ae5bb3c74bdd15e2d36a 751,162 bytes
- `screenshot.png` 0954e33d2a52ac1470b5c204eaaeea8d8fe811854486542ece88541cf7dbc526 15,023,593 bytes
- `text.txt` e39f8d2cb60ee8a58c5400536714b0688b198b31bc07685fd7cdada8f2f0dd70 417,190 bytes
raw, 1 files with SHA256SUMS- `ChangeLog-8.curl.html` 8d771e4a97a9457c8ff4dfff88d79661cf8b5d520666b8799a944f033e620e68

### [PHP2Shell — AI uncovers critical vulnerabilities in the backbone of the web](php2shell-com/index.html) [original ↗](https://www.php2shell.com/)

**OpenAI / Wiz / Calif joint microsite (php2shell.com)** · researcher · primary · captured · published not stated · added by `claude-story-site` · `php2shell-com`

The researchers' joint site: credits, '70% of websites', demonstrated RCE on WordPress, Drupal, Joomla; FPM RCE via application-level paths; memory disclosure.

capture 20261022T111831Z · HTTP 200 · https://www.php2shell.com/- `headers.json` 95d2d3cfe2f388045327d30e2dd08bb49dd3e8dd426ae09aa80e1261f01cd7ed 1,509 bytes
- `page.html` 8c12d8880e5b0e798d3e4457997397a1c0de6b36ab774a8fe46518f3270532a0 284,683 bytes
- `provenance.json` 020c3cad8f308d11c8454cbf625b7310e0958428a69ade312c2cd43d349c2897 952 bytes
- `rendered.html` e5958b710931a3753baaa7475dea5c3be9f08677412269976d9e50100e3f9022 506,683 bytes
- `screenshot.png` 77a8c0a27f91ee02eab5575847f4611e6605f030f286c20c51eb4de3cf0f496a 2,152,724 bytes
- `text.txt` b1e83b4f0feb87d5abb59bfb76015b154a7b678a51c0e965e06929f1e6b17f48 9,251 bytes

### [PHP Security in 2025: Lessons from the Core Security Audit | PHP Architect](phparch-php-security-2025-audit/index.html) [original ↗](https://www.phparch.com/2025/09/php-security-in-2025-lessons-from-the-core-security-audit/)

**php[architect]** · news · secondary · captured · published 2025-09 · added by `claude-story-site` · `phparch-php-security-2025-audit`

Background on the 2024 core security audit.

capture 20261022T112947Z · HTTP 200 · https://www.phparch.com/2025/09/php-security-in-2025-lessons-from-the-core-security-audit/- `headers.json` f94a2cb9fd6c974ab16b7f672856596b84da0ee50036c93a902f055a2efebb3f 1,063 bytes
- `page.html` 85b9dacfb542ca35651d775dfe24c41186dfdca2ae5abc86bafcdd1e19b79195 94,581 bytes
- `provenance.json` 4783394753855b623aa99c5c3077af3a72dc1b6dbd18ba5e2e181737ffcbc90b 1,095 bytes
- `rendered.html` 8f4192ecc48d4d4fb38e2492bac830525bfcab04ff70a72849ad8ccc35e38358 94,279 bytes
- `screenshot.png` 51293897aa9bc0b5b07dbb244193f6b3da545420a92eb912de4664a8e0ebe245 2,293,707 bytes
- `text.txt` 95189f8e2e198e19e39271f1750db73ca525f593abbe9ec363969f3eae4499ec 28,517 bytes

### [Today's PHP Security Release, and How We're Strengthening PHP Security](phpfoundation-blog-security-release-leak/index.html) [original ↗](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

**The PHP Foundation** · advisory · primary · captured · published 2026-10-21 · added by `collector-researchers` · `phpfoundation-blog-security-release-leak`

Dated Oct 21, 2026. Primary account of the leak: CVE IDs circulating Oct 20 ~15:00 UTC; Calif 'mistakenly published a video' ~20:00 UTC; mitigation advice may have leaked; Chainguard broke embargo Oct 21 07:41 UTC. Captured text also contains reader comments below the post (lines ~90 onward) — those are third-party, unverified.

capture 20261022T081244Z · HTTP 200 · https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/- `headers.json` 3b9ca485b393afa38381b67bb251208dca58e32f815fd1aed95ba69e1d88dda3 856 bytes
- `page.html` 6b8915a800a5311c06544c4c47fe0e6b69586e9d75aeab49d2922a6a71446223 40,324 bytes
- `provenance.json` 777ac74e8e4915a67c651d019c1cdcf9a099773e9963221b097b676fa5054bde 1,222 bytes
- `rendered.html` 074da5662f04df8f88a2efc163726c553f5bb43c8095278a089daa0faf364955 126,414 bytes
- `screenshot.png` 09956999247e6e42a5635bb2b1234a2f8a11f0c66c26b88fafc020c31f3b6cd6 2,630,327 bytes
- `text.txt` b9f29cfdc1c0cd65dd505738d06d5f7d590d5d3da95801309990871870d2e0dd 31,883 bytes

### [php2shell: Detecting and Investigating CVE-2026-109618 and CVE-2026-109619 | Prophet Security](prophetsecurity-php2shell-detect/index.html) [original ↗](https://www.prophetsecurity.ai/blog/php2shell)

**Prophet Security** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `prophetsecurity-php2shell-detect`

Vendor detection guidance.

capture 20261022T112954Z · HTTP 200 · https://www.prophetsecurity.ai/blog/php2shell- `headers.json` 3d69271680bbf150bc6fae70fc1287cd80311e2b43424bbf4f428714ecd955b7 1,637 bytes
- `page.html` b00c997496adf4b1764b46125a9a74849e83e0baf12ba075d39cc6b0c4493bb0 178,998 bytes
- `provenance.json` c58cd7be80e63d3760a0f31b5507e5a3f5678bcc269f1ef1e986c903224553af 1,025 bytes
- `rendered.html` 3ac8595af5225424d4be82b0b063abfb5254d537481410f86cb935ebdb46b2a5 797,451 bytes
- `screenshot.png` 8a43fab6765b4d462f55e613f1f5fec6d081c690d44afd1fc4af635f917078f4 1,773,221 bytes
- `text.txt` 2e8efe1d3d72efc2c7357b939ba6e0a4ee639b3fb3cde21efaa44f5f60a00e51 15,452 bytes

### [403 Forbidden](qualys-blog-php-preannounce/index.html) [original ↗](https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities)

**Qualys** · vendor · secondary · blocked · published 2026-10-20 · added by `claude-story-site` · `qualys-blog-php-preannounce`

Published on 20 October on the pre-announcement.

capture 20261022T113004Z · HTTP 403 · https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities- `headers.json` 9ae7ad7eb7ecad9ff1195f99f730cc79be3ed1abdbb907f73ad003c7d28c5651 628 bytes
- `page.html` dd1c2f122d665c4b3fb0be7b2e8e1eb717607b195475efd409f666dfbd979b60 1,486 bytes
- `provenance.json` f3a38995a937d0edc65d7304bf5014e3d946eb475aa675593c5aa03aea58e148 1,110 bytes
- `rendered.html` eddbe1ecca686ffa5ca8cfa12c3054e26ecd8eb8c21461faaa9951759d65f41d 1,203 bytes
- `screenshot.png` 88143431c2f2ccebbb073449167e29d4114759e3e211d651114b2d152afd2e9e 10,431 bytes
- `text.txt` c6c1266b1b8854e014702a20b4d2b956f885b89fc66f21fad180d33a4c37467d 19 bytes

### [Security audit of PHP-SRC - Quarkslab's blog](quarkslab-blog-php-src-audit/index.html) [original ↗](https://blog.quarkslab.com/security-audit-of-php-src.html)

**Quarkslab** · researcher · primary · captured · published 2025-04-10 · added by `claude-story-site` · `quarkslab-blog-php-src-audit`

Quarkslab's own account of the 2024 php-src audit (OSTIF, Sovereign Tech Agency): findings, two redacted high-severity issues with fixes in progress.

capture 20261022T113008Z · HTTP 200 · https://blog.quarkslab.com/security-audit-of-php-src.html- `headers.json` 9a1974a3d0e74f6c61049df444eec6f88c921c1df160c4d36547d455f5f69d3a 721 bytes
- `page.html` cfffdbab1e24dbeaafa236432ed6653fa2442387aeae475f996cddddb722bb89 28,339 bytes
- `provenance.json` c1a3e69c282c4e578340fa0788f636f5604d1f0d0a6076bac4cd7bd024ee55ca 996 bytes
- `rendered.html` 032ff57da663f85dcf219749a2b1849c606efef96c9044684130409249a05e18 27,638 bytes
- `screenshot.png` 84a81db5a451d763ffe7a40817ea3c94e0e0a7d7da3bd0b7c74b2b8b0c912974 932,374 bytes
- `text.txt` cd5ccdaf99da0be1676b319643939d20c0a5d17df18eb8f0636eaad6ef7c9321 7,821 bytes

### [PHP2Shell Exploitation: Two Critical PHP Flaws Explained](recordedfuture-php2shell/index.html) [original ↗](https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation)

**Recorded Future** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `recordedfuture-php2shell`

Vendor explainer.

capture 20261022T113014Z · HTTP 200 · https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation- `headers.json` 3f16adaf8c9cba92536851d7836d4e787039ea13bccb4da34e56759d45f7fbef 1,234 bytes
- `page.html` cd54cc52e04832d03115211f9aca789fb9d4861a8460a25a4e6ccc45f2d11f9b 27,860 bytes
- `provenance.json` d044ae83506d9d12bb11b3e2357405fd0be2350bf9782b8f21e5d0bc7134c316 1,034 bytes
- `rendered.html` ca1457d1d590d21807ebf2cd64d30304ff3607b8171472c2d205a8fd4365a37c 178,844 bytes
- `screenshot.png` cd745753c1ec28fcaf45c4b291d01045bdf86c88cbd0184e664e196bdd0f8ddc 2,871,582 bytes
- `text.txt` f9cb130d64545fe46a477766dce91126405f12d99e8051aff2c05e084a904fe9 18,444 bytes

### [Global Websites Offline Amid PHP Security Flaws: Finance Sector Impact](reuters-factbox-websites-offline/index.html) [original ↗](https://www.globalbankingandfinance.com/factbox-websites-taken-offline-over-php-risks/)

**Reuters factbox, via Global Banking and Finance** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `reuters-factbox-websites-offline`

Reuters list of websites taken offline: Netherlands, France, Germany, Belgium, Finland and others.

capture 20261022T113026Z · HTTP 200 · https://www.globalbankingandfinance.com/factbox-websites-taken-offline-over-php-risks/- `headers.json` 8756be9a476cea45bf6f0ba5d6afec78293d9a1c08b04c463ba887aa51643743 1,259 bytes
- `page.html` 8c4668f8881f07f4e9fcdaf5498ac560214aa9243a2e163122532b0a80b2d141 214,076 bytes
- `provenance.json` 93bc4bfda9e1316396b718afd5bf442ed65dbddf92c7700d9308c0d04c3c7806 1,084 bytes
- `rendered.html` 5732718cdad049baa24fe5d9d7c0e91fd962f71df61672c4e0b3d101b9a262c3 227,694 bytes
- `screenshot.png` 28b7c31e70d01ad1a8ca150a6127d7188c38f431b913c022f6aa6a997c47cc5c 3,456,506 bytes
- `text.txt` d562e28995b00a19ceb36a346ffec05542ec675499998931b8936af7ba41d5d3 10,148 bytes

### [NCSC: Ernstige kwetsbaarheden in PHP | Rijksoverheid.nl](rijksoverheid-ncsc-php-news/index.html) [original ↗](https://www.rijksoverheid.nl/actueel/nieuws/2026/10/21/ncsc-ernstige-kwetsbaarheden-in-php)

**Rijksoverheid (Dutch government) / NCSC-NL** · government · primary · captured · published 2026-10-21 · added by `claude-story-site` · `rijksoverheid-ncsc-php-news`

Primary: NCSC.NL taken offline 'uit voorzorg'; advises a risk assessment per internet-facing PHP system and considering switching systems off until fixed.

capture 20261022T113033Z · HTTP 200 · https://www.rijksoverheid.nl/actueel/nieuws/2026/10/21/ncsc-ernstige-kwetsbaarheden-in-php- `headers.json` 02c777fcd4897b76fb5febbe44f6827eac84175c43def883b4074889c879f1e6 2,789 bytes
- `page.html` cd5e199ae854bb38177fa187f36f80b267ee93f5b23262122697c7038276e21e 240,904 bytes
- `provenance.json` 41eeb42a42ffe905a45ac1fe625d4acb5b9ba172ca4fd9253d01dc7295a7aa8b 1,072 bytes
- `rendered.html` e364ac0a4f3336a54bc2581a182d37db39961f47802adca7c95247e9c0fd4613 244,344 bytes
- `screenshot.png` 0b023dc6a8fca71e18932ef0a168051841129928264b33c1937fff623cab4457 435,918 bytes
- `text.txt` 7e10bcf7cb44e5f753e057d6a6d5f07747f231c066728373806fa14d80bff5b3 3,720 bytes

### [PHP2Shell: How Hard Is It to Exploit, and What PHP Is Changing | Safeguard Blog](safeguard-how-hard-to-exploit/index.html) [original ↗](https://safeguard.sh/resources/blog/php2shell-how-hard-to-exploit-php-foundation-changes)

**Safeguard (vendor blog)** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `safeguard-how-hard-to-exploit`

Secondary analysis of exploit difficulty: a public PoC that failed under test; the upload-progress primitive is real; quotes a PHP core developer on Mastodon that patching is the only mitigation.

capture 20261022T113039Z · HTTP 200 · https://safeguard.sh/resources/blog/php2shell-how-hard-to-exploit-php-foundation-changes- `headers.json` f024dda4aca45ee7784179ce10f5502c7cdc1848b68820c5e3ac4d5ae9977fe4 1,910 bytes
- `page.html` ca8f171043e3a56f99149b1ffa731bfdd00faa1aca0dde315bab896ba544148f 419,051 bytes
- `provenance.json` dc78d80894e1f67eb84e8f3dbcb4fce3d4687ae21172b11e13dab9e452491777 1,094 bytes
- `rendered.html` d50d0675b422cf74595a98594b026b8936b4a597bfdd8e14bf6417f1fb65c089 425,970 bytes
- `screenshot.png` 81bc77d288b0f16b3a5aff9755c8f70d850d79e54d2f786960ea233e942d2e24 3,150,477 bytes
- `text.txt` 271a233b1b8e628f66e764b3e3f089b09951d09ecdbb5fb9ef39d619eae623e9 37,594 bytes

### [PHP2Shell WAF rules: what they block and where they fall short | Safeguard Blog](safeguard-waf-rules-limits/index.html) [original ↗](https://safeguard.sh/resources/blog/php2shell-waf-rules-stopgap-limits)

**Safeguard (vendor blog)** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `safeguard-waf-rules-limits`

Secondary comparison of what each WAF vendor said about its own rules; the direct-to-origin check; quotes Cloudflare's CTO 'STOPGAP only' via Reuters/KSL.

capture 20261022T111928Z · HTTP 200 · https://safeguard.sh/resources/blog/php2shell-waf-rules-stopgap-limits- `headers.json` 0c47d1b3b4483fe3dfbc1d2c92601e2da277c00bd9b13a0b4e1400d532b810f8 1,911 bytes
- `page.html` 7ee15349d487eb9f5fb2f578f4e465e1bdd8b44a4f7ecbfc4b2d6da5277b7dda 428,039 bytes
- `provenance.json` a152958c004bbd289d33c79fc1eaf5b3b1aa6442001c31226607d2a25f3b67d4 1,055 bytes
- `rendered.html` 9cf1b889fa9c9bfb3bc5a219a58059a1fbb4ad867e796b6d89a2ca8960724e69 436,335 bytes
- `screenshot.png` ec0109ce98dbf571daf5c08aeff60ae7e9957e2fc907b50f17bd9e196ef0c621 3,153,430 bytes
- `text.txt` 664a398aae1f5c1df20e43deb46b962fd818b4403c864de8cab55f23c79c193c 36,136 bytes

### [PHP2Shell: Critical PHP RCE (CVE-2026-109618, CVE-2026-109619) | Sansec](sansec-research-php2shell/index.html) [original ↗](https://sansec.io/research/php2shell)

**Sansec** · researcher · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `sansec-research-php2shell`

Vendor advisory predicting mass exploitation within 15 minutes of release; no IOCs; later accused in a reader comment of leaking a vector in page metadata (unverified).

capture 20261022T113104Z · HTTP 200 · https://sansec.io/research/php2shell- `headers.json` 2dfd5ab190184ed3ba6295db2882e7dce9719d6048f860a68a011034c1e1e26e 1,167 bytes
- `page.html` 60368be8e17445397b0865e1a7c8a7142cd888ffd81aac0b11d7d0644dbaab1d 36,814 bytes
- `provenance.json` 7443427160ac153a29c5b8c8c5278458e0b6c1eb5bc1bb1597d25757d01836bb 978 bytes
- `rendered.html` 31f57c6c03a271c045e195256e2d406614c505ca3c3d07ce40c299983be0cc0a 37,783 bytes
- `screenshot.png` 21518bc8c146169d1d397668488e88840c646c1286340aa20808740f0538eed8 1,506,901 bytes
- `text.txt` 281e3c508909a7002ae17602fd885f6acbd78e3766d8de3153f1139c7be8d134 9,554 bytes

### [Edinburgh council website offline amid global cyber security alert](scotsman-edinburgh-council-offline/index.html) [original ↗](https://www.scotsman.com/news/edinburgh-council-website-offline-amid-global-cyber-security-alert-9302652)

**The Scotsman (Jack Davies)** · news · secondary · captured · published 2026-10-21T18:09+01:00 · added by `claude-story-site` · `scotsman-edinburgh-council-offline`

Edinburgh council site offline late Wednesday afternoon; spokesperson: 'essential maintenance', 'waiting on an update from our provider'; link not confirmed.

capture 20261022T112150Z · HTTP 200 · https://www.scotsman.com/news/edinburgh-council-website-offline-amid-global-cyber-security-alert-9302652- `headers.json` 1c3f67fd980359a0bfbaa40d100d35aea3cac3074d6b29d0a1753b16584a605a 1,536 bytes
- `page.html` 90aaacae5232524ded421df348d5573c267ac8e950c4e48628bd8ed586c6aedd 262,633 bytes
- `provenance.json` 25e30a911da3a7887aafc5080201b7d8bc5dc8508f1d3a7a2545b1c4d5963ee7 1,118 bytes
- `rendered.html` e02581dcf2ba49c3963ed48490b34c813b9558ff27991256fc0f50231be75ac2 712,640 bytes
- `screenshot.png` bb1c80d6965bbdc9c3143e0ff88f84de54ca8c9af02419c854993868a6452a05 2,399,966 bytes
- `text.txt` fcdbc39d82bfd477159635a160dc431f569345ad40cd7b1f23b050917f41ddd6 8,754 bytes

### [PHP2Shell Exploitation Started Days Before Patches - SecurityWeek](securityweek-exploitation-days-before/index.html) [original ↗](https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/)

**SecurityWeek** · news · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `securityweek-exploitation-days-before`

Secondary: Censys 2.58M hosts / 1.58M versioned / 1.57M unpatched on 21 Oct; nearly 3M by 22 Oct; VirusTotal 5.1M IPs, 1.1M announcing a version; Amazon's 17 Oct attempt; Cloudflare CTO early attacks.

capture 20261022T112314Z · HTTP 200 · https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/- `headers.json` 20346ce7a28ae2cea09c5ce445b478a4fe9837f2cc4cf97d5ae15a6bcd846d48 1,083 bytes
- `page.html` d00e2e5608d37d978b2fa983ffa1087430976a445caa72df9a49b7618dbe9566 168,865 bytes
- `provenance.json` 99114af56492dfd4921ca1b095bf85f256188ccd6d6e17fdaadd7657d629d83b 1,072 bytes
- `rendered.html` e493b8fc733dacfc40164c4bb153884e96b82e984e2e3c738c13c536a5edce73 259,915 bytes
- `screenshot.png` e5454077149da3ca0ea83a39c68e30ce9f6f984788c53349e104a0d45dea3fb9 2,097,665 bytes
- `text.txt` ac663f2d9dbd0197d3721e1756bdc12e2491cb512eaa32197592ff9792f2632c 13,376 bytes

### [PHP2Shell Patches Land as First Exploitation Attempts Hit Sensors - SecurityWeek](securityweek-first-attempts-sensors/index.html) [original ↗](https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/)

**SecurityWeek** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `securityweek-first-attempts-sensors`

Secondary: patches land; first exploitation attempts hit sensors.

capture 20261022T112324Z · HTTP 200 · https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/- `headers.json` dd993a8f1006a3a64fb1decac73db56de8468b6aa2d213379f7b8925a27f83af 1,083 bytes
- `page.html` 6d603d0aa60802788b1f163a27b575df0c62e1bb903bca9e6a3c98133e5d095c 169,487 bytes
- `provenance.json` 2dca30a4387489ca9868c223790494256dc26503ee6b709a46643fa881c589e8 1,115 bytes
- `rendered.html` f5cdb5755f0b1ab2a897933da2b213a674ccfa76931ab1a19ef6627b79408b15 261,102 bytes
- `screenshot.png` f5f51f0db7037127107f38fdaa5cbdc77c6df0328ef92619061ceb4a76bfb575 2,236,355 bytes
- `text.txt` b63772dddccf9cee302313f5dece42bf30d91abdb6f30ca61fb2a38081c85a41 13,245 bytes

### [PHP2Shell: Mass Exploitation Looms for Leaked Critical PHP Flaws - SecurityWeek](securityweek-mass-exploitation-looms/index.html) [original ↗](https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/)

**SecurityWeek** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `securityweek-mass-exploitation-looms`

Pre-release: 'mass exploitation looms'; watchTowr and Huntress had not seen exploitation.

capture 20261022T113111Z · HTTP 200 · https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/- `headers.json` bb347753d4feee250192fd7b5bdc50a5bd970acacdb2bbc50ff7ec8f02e421f5 1,083 bytes
- `page.html` cee26b75f5542752d57c034b8a0eccf6b6227242d7619e33a91a35e8d3af8ebb 162,723 bytes
- `provenance.json` f31a296260b932686cb33c7c964e56367479a31e090172999a0b6a20bfac343c 1,111 bytes
- `rendered.html` a85f0c144d03bd751e0f5f14784fdfcb65809370f94510720b7abc2d66c06403 254,022 bytes
- `screenshot.png` 65e2d5f0404ae070f6a43772ca24731d6e2b0a1125aac8132107060f194bc2d7 1,822,934 bytes
- `text.txt` 693aa4300139d2afc431484c18fe038f9b0b2fb411a89b5defbdad622958e851 9,475 bytes

### [Stopping PHP2SHELL: How SentinelOne Protects Customers From This Attack Technique](sentinelone-php2shell/index.html) [original ↗](https://www.sentinelone.com/blog/stopping-php2shell-how-sentinelone-protects-customers-from-this-attack-technique/)

**SentinelOne** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `sentinelone-php2shell`

Vendor explainer; a table of triggers (OOM during request start-up such as multipart parsing).

capture 20261022T113120Z · HTTP 200 · https://www.sentinelone.com/blog/stopping-php2shell-how-sentinelone-protects-customers-from-this-attack-technique/#cq=i1- `headers.json` 652bccd3c7747978e637a6cf3ca0dd3adcb9d8d6dff7f6ea1e7529206dfc78b6 6,215 bytes
- `page.html` aaf6dfa7fac00ac3a9150b9baee326803df94377bbae974995178f465292bf84 343,729 bytes
- `provenance.json` 2a83e001a66dd0c777afe90a659023a49d81f93cd3c8310b6024faf644b74974 1,146 bytes
- `rendered.html` d09c9b7551468ab7f7a69721a397eab5bb3d72b48ef9b756d0427a34c54bc0af 553,092 bytes
- `screenshot.png` aeaf87bfa3d2dea7b44c00746ea38837ee3dbaf866640044a48d46125967360c 3,003,286 bytes
- `text.txt` 0e75697fb5149ca627012455a8e06b03535c31e0c70e6ef87501d1beb7d39d69 24,686 bytes

### [Just a moment...](socket-blog-embargo-dispute/index.html) [original ↗](https://socket.dev/blog/php-embargo-dispute)

**Socket** · news · secondary · blocked · published not stated · added by `claude-story-site` · `socket-blog-embargo-dispute`

BLOCKED: Cloudflare bot challenge.

capture 20261022T112047Z · HTTP 403 · https://socket.dev/blog/php-embargo-dispute- `headers.json` a80f2b5ad8ae81c3b83a000871a7819d186da9f1d450b3717ea39deb9bcacc71 1,990 bytes
- `page.html` b8ac97a2a385dc96494c44b3886248703441a11d350a683a472b690ffe293803 6,187 bytes
- `provenance.json` 8255345be61952af9d34d90c1a80520fcab5675c9c8ed3951c2aa93bdc5d64db 939 bytes
- `rendered.html` 45f09ae7a4bb5f729e0b016d77de302dd1646fe819943e3054160f7bc5552cb1 28,771 bytes
- `screenshot.png` 38b458f2d97ad16e0fe1fa55afc35614ff1c9d6704c168964e2d9c3c625be655 38,311 bytes
- `text.txt` 2edb7b291225f9a58dd5ed7546e5c5ead9d84e0c92a9d78e93e06e030687646e 258 bytes

### [The Patch Is the Exploit - by David Lopez-Kurtz](substack-lopezkurtz-patch-is-the-exploit/index.html) [original ↗](https://davidlopezkurtz.substack.com/p/the-patch-is-the-exploit)

**David Lopez-Kurtz (Substack)** · other · secondary · captured · published 2026-10 · added by `claude-story-site` · `substack-lopezkurtz-patch-is-the-exploit`

Analysis: the audit's public summary lists 27 findings, two redacted, and does not describe an OOM finding.

capture 20261022T113134Z · HTTP 200 · https://davidlopezkurtz.substack.com/p/the-patch-is-the-exploit- `headers.json` 93831a587e5a9a37a455a49bb5bc1a735ffddbaa9462baecf8483bd621dc0d80 3,448 bytes
- `page.html` 77bae2f3d20efe5af0c1bf780b1c2618202d3da7941792444a8fbfed1d4a87f5 224,610 bytes
- `provenance.json` b49aa2b0f632867066da181f78cf57cd3495f0c1c9c7c7634875a04c5f86b5ff 1,023 bytes
- `rendered.html` 5a9958401f0de8caa87154eb38d082ae37fe969fe4928862d4e557f4bac4ba1e 263,845 bytes
- `screenshot.png` 4f94dc2329c6fd545b1a600cccfc7b2ce2db41deb2b8288403a9eec27e63dd56 3,979,940 bytes
- `text.txt` cb3714dc12f96c969959784164a40f12aa923b46cf56df83aa950a9ea2573330 33,564 bytes

### [PHP accuses Chainguard in PHP2shell](techzine-php-chainguard/index.html) [original ↗](https://www.techzine.eu/news/security/145182/php-accuses-chainguard-in-php2shell/)

**Techzine Global** · news · secondary · blocked · published not stated · added by `collector-researchers` · `techzine-php-chainguard`

Cloudflare challenge (HTTP 403) at 2026-10-22T08:13Z; 403 capture folder kept. Per search snippet: Chainguard CEO Dan Lorenc does not dispute timeline but denies leaking. Unverified until captured. Retried by claude-story-site on 22 Oct: still blocked. Retried by claude-story-site on 22 Oct: still blocked. Retried by claude-story-site on 22 Oct: still blocked.

capture 20261022T081301Z · HTTP 403 · https://www.techzine.eu/news/security/145182/php-accuses-chainguard-in-php2shell/?ki-cf-botcl=1- `headers.json` e4c1c978fae1d476008a0220bd56d79c287115d6dca754076ac5c220c8403209 1,084 bytes
- `page.html` f261423d1da97890ff6bfccd31ff4ee0b74f69351cf75095fbe791cb16cbf5bd 103 bytes
- `provenance.json` 0b93d24048c39675ef0bec6c63cbadc201cd4c761b3fd85f96538ec7afa93ea9 1,084 bytes
- `rendered.html` 8631afb05e141985b74d3ac4fc67eca679d940e50dcd377593b0a5faf473e4a8 29,118 bytes
- `screenshot.png` 83e27bf325b865db2d303c7c20ec30a0a5c0b452145b2b48175a74d4b292d20f 38,816 bytes
- `text.txt` a709538005b7efca9f1059e2eeaa4a13cd196d9f8215befc91b286d42f56d334 263 bytes
capture 20261022T112124Z · HTTP 403 · https://www.techzine.eu/news/security/145182/php-accuses-chainguard-in-php2shell/?ki-cf-botcl=1- `headers.json` 5345616d7653c07e708bb2b1f5f0b9fe2afefd06cca4a63dc7bb7fee0684222a 1,080 bytes
- `page.html` f261423d1da97890ff6bfccd31ff4ee0b74f69351cf75095fbe791cb16cbf5bd 103 bytes
- `provenance.json` 8870e433407b07164f7f83ef420dd5307c6c1c525544cc382a43dd9da569c4ac 1,084 bytes
- `rendered.html` f9d1600dea692ee1e52186d55f0ac9eee1a19f909c76aec8fa9b5ef26f1278bb 29,118 bytes
- `screenshot.png` 6127fef1895a985b7bcd7168fff19347a8ca8f67cfc409d39a802caebc1fce9c 38,923 bytes
- `text.txt` 93f61d068317f6ef84245b70a7d8b8ea0f4b1d351af10fc89a31cbe4ae7eb1da 263 bytes

### [php2shell (CVE-2026-109618, CVE-2026-109619): Critical PHP RCE FAQ | Tenable®](tenable-php2shell-faq/index.html) [original ↗](https://www.tenable.com/blog/php2shell-cve-2026-109618-cve-2026-109619-frequently-asked-questions-about-critical-php-remote)

**Tenable** · vendor · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `tenable-php2shell-faq`

Vendor FAQ; notes Cloudflare's rules cover only traffic routed through Cloudflare.

capture 20261022T112331Z · HTTP 200 · https://www.tenable.com/blog/php2shell-cve-2026-109618-cve-2026-109619-frequently-asked-questions-about-critical-php-remote- `headers.json` 5ddfb8ebd67d5b056190eb932bd7230be55b6dcec36b71da7591e9ff3ef787e9 1,390 bytes
- `page.html` 0f90e53e8a45f385d5e14f7493f1aa99aff8d34b7405ed43d70a3534381dd264 274,325 bytes
- `provenance.json` f1f23ada9af900931c49744b7cb544a8b730ec5038bd6637c3a3b521f095c4d6 1,155 bytes
- `rendered.html` bbc941dd99bd25fbb24457889bb89c0cd2213187cc104c491b15a86ad1167425 469,247 bytes
- `screenshot.png` fb42572ffc60b269206740e6d85216b9fa06d7226bfb49682d148b44740c897c 2,222,099 bytes
- `text.txt` 10d98694b9c0243efaf17de612d27de215138873b711598eae3f68ceb9b11b54 16,528 bytes

### [Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed](thehackernews-php2shell-4days/index.html) [original ↗](https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html)

**The Hacker News (Ravie Lakshmanan)** · news · secondary · captured · published 2026-10-22 · added by `collector-researchers` · `thehackernews-php2shell-4days`

Dated Oct 22, 2026. Quotes Amazon CISO CJ Moses ('post shared with The Hacker News'): MadPot honeypot exploit attempt Oct 17 2026 from anonymization network IP geolocated to Australia; PoC attempts from ~02:00 UTC Oct 21. Says 'details about the CVE identifiers and a proof-of-concept (PoC) exploit leaked ahead of time' — contrast PHP Foundation 'No technical details leaked'. VulnCheck: PHP on 2,608,039 internet-facing hosts.

capture 20261022T081320Z · HTTP 200 · https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html- `headers.json` 54c094189f50f4afa3962d0e484ef93cf0f92bd1fefb71ae2fec7e63b71b3b14 783 bytes
- `page.html` b2b51b3736eab8ebf9fb584770654a563ec0cde9a258c8ccc9b2cac5e2759495 181,180 bytes
- `provenance.json` ef03914e372ab683b87cf258b84ec703ba5cc140e8b724fe1fa547d0f7a066fe 1,081 bytes
- `rendered.html` a7caeb00fddc406d6dcfeb68c7fdce453fdb39446eb83daa364cb3f2986a7834 176,478 bytes
- `screenshot.png` 71b28408de124895b1534822f79eff33a445be5296c09203d51f152ef67d089c 2,255,956 bytes
- `text.txt` c1cb63141287484c7b96b6f842f983bb978a108b3b82eebb95ebe78c4ed608f4 12,295 bytes

### [PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert](thehackernews-php2shell-unpatched-alert/index.html) [original ↗](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html)

**The Hacker News** · news · secondary · captured · published 2026-10-20 · added by `claude-story-site` · `thehackernews-php2shell-unpatched-alert`

Pre-release coverage of the two unpatched flaws.

capture 20261022T113144Z · HTTP 200 · https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html- `headers.json` 504e60a31ad0c0649db5fe4d0560bcb64bcea39e2c5d8b374dd60c86235937fb 783 bytes
- `page.html` b8297488c796fba8c0c46fbb558121433294b8f8991c457777efa33409b6634e 175,875 bytes
- `provenance.json` 3eccd35b7d04ded29ea8937c2d7870a8be4adac2340d632f92f01cfe630c3147 1,090 bytes
- `rendered.html` e34515d9ce5113ec57194450be97a765341affcc8cae816dd5a475c8d200873c 171,094 bytes
- `screenshot.png` 1686d34457b358c5f9a1950a0da921ac4d765a0491953e9383a70b1498568c29 2,281,720 bytes
- `text.txt` 33ba8292e26406d7275daee8f4f0b07cf240d878bdcff089c5a9e1d4c21eff6b 10,078 bytes

### [PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't](thehackernews-what-protects-you/index.html) [original ↗](https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html)

**The Hacker News** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `thehackernews-what-protects-you`

What protects before the 14:00 UTC patch; no compromise confirmed; public exploit code not shown to work; not in KEV.

capture 20261022T113151Z · HTTP 200 · https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html- `headers.json` 1d0e37d8f272c2035915a1e3bae5d055fd9d8a9dac4b60116725e2af378e7d7a 783 bytes
- `page.html` c3d4ade9c8b6af04990a2ee26114a8665f943ed5142ae7348e38ef3b23d34ab9 180,675 bytes
- `provenance.json` b3b2d8123bee4172bcdb4453abeb515d86f34dd658088159147c1b0b944661d2 1,081 bytes
- `rendered.html` 64ef5d20df0ea8dfc700220c350757cc455bcfc017751142819841c35e11ff9c 179,165 bytes
- `screenshot.png` e0e1a25547dc8d319ff4071cceff2950d36aa030ec7f2ab1625d04018d2e39cc 3,022,943 bytes
- `text.txt` 2301d254784fd6612f36f844e16a706e2e7ca5f8d8f942f7f36544c59d78d82c 13,774 bytes

### [PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024 | The Record from Recorded Future News](therecord-php-foundation-statement/index.html) [original ↗](https://therecord.media/php-foundation-statement-critical-vulnerabilities)

**The Record (Recorded Future News)** · news · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `therecord-php-foundation-statement`

Secondary: the Foundation's account that AI review first sparked alarm in August but signs surfaced in 2024.

capture 20261022T113158Z · HTTP 200 · https://therecord.media/php-foundation-statement-critical-vulnerabilities- `headers.json` 2257c81e7400eff589569be8295f608e775b7e305c9af66d1e8d4a8f580c7229 914 bytes
- `page.html` 8849918ee23ea9f6e709c68d21726ff22f31b4e88bf3fc8d6c2d67f55d338d81 92,120 bytes
- `provenance.json` e26d3d9bab095c3530be9242fd010f71c6efd72f0f561f48cc26892f32df92cb 1,122 bytes
- `rendered.html` 387866a008c5068d55372962daa2904c6bee30821494b4c30a467aaa1c775383 96,511 bytes
- `screenshot.png` 31f0aeaac3e78e1ab3c579a6217361b9148b439f02245b029c43c19d4f7f759a 1,498,927 bytes
- `text.txt` 28c72344e03a5a79b2ee018193bbd930283c78444f9cffcea3dc7a422c49051e 7,717 bytes

### [PHP blames supply chain security biz Chainguard for putting huge chunks of the web at risk](theregister-php-blames-chainguard/index.html) [original ↗](https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611)

**The Register** · news · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `theregister-php-blames-chainguard`

Carries Dan Lorenc's reply: 'I made the call to get these out early when exploits hit in the wild'; several unnamed vendors; honeypots trapped IPs from China and Russia; a researcher warned on the Friday; found independently with an AI harness; apology for the stress.

capture 20261022T113204Z · HTTP 200 · https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611- `headers.json` f037ca6b2e792623b19de3cc87220576a70faf147d1140a31fe0f0a22fa34d1e 610 bytes
- `page.html` f7f24a70afadc30edf03beb3e697086d5126ad7f5ddf2875c2e5c54bc07208a5 183,584 bytes
- `provenance.json` 28bb52465a44cfdc683cafd60ae043da8145a2e31fa1e280fa7ed7b81e417e32 1,225 bytes
- `rendered.html` 3729f08f3b948bc4af5a39a2b7351e38db6eeafbbcb982556755e5929dabb56d 197,763 bytes
- `screenshot.png` d7c98b6141ded745143bbb5bc018fb02e07f795ab320a20434e063f150a3b875 1,745,666 bytes
- `text.txt` b355691c9b584c533c626787860d8f2f329c17e1618422ab1088cfcdb71530ca 13,215 bytes

### [PHP-lek legt DigiD, MijnOverheid en Tweede Kamer plat | TPO.NL](tpo-nl-digid-offline/index.html) [original ↗](https://tpo.nl/2026/10/21/php2shell-websites-offline-digid-ncsc/)

**TPO.nl** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `tpo-nl-digid-offline`

Dutch: DigiD, MijnOverheid and the Tweede Kamer offline.

capture 20261022T113213Z · HTTP 200 · https://tpo.nl/2026/10/21/php2shell-websites-offline-digid-ncsc/- `headers.json` 3b4fb879e9421d7c88e3feb33a0521286d51f96fea6fe5ce5a04f9a54f055b3b 826 bytes
- `page.html` 1ad044bff8e96636aba6f7cd64ffc320eea5c69055aa087a1b96187ccb5cacad 233,569 bytes
- `provenance.json` e8a125363be8a52f4be95819b63112af3af8ea3317977ed509fbe2a52b0e31df 1,020 bytes
- `rendered.html` d32cd4732dc20dda8b4464a52f471b942ec7756397f0ff01d40dd7344843c936 407,728 bytes
- `screenshot.png` 50d028e45666fd51dea41fe9359edc265ec4671d4ca742a6acc17eb2ef119a4d 1,351,320 bytes
- `text.txt` 2ddfd8817abf25b62a1d65842ea2e1eda4c28468ef7c075bdcb2b736ab509dcb 3,796 bytes

### [watchtowr.com](watchtowr-php2shell/index.html) [original ↗](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/)

**watchTowr** · researcher · primary · captured · published not stated · added by `claude-story-site` · `watchtowr-php2shell`

BLOCKED: HTTP 403 to the capture tool. Search summaries say watchTowr reports active exploitation attempts and lists the flaws as exploited in the wild.

capture 20261022T111839Z · HTTP 200 · chrome-error://chromewebdata/- `headers.json` ff01331edab1c463627b7d97ebbf6c6089f2893fb06dcf8f589c2d11416bf603 2,911 bytes
- `page.html` cfe1d709b20d9c9c8d6383853add5bab85c168f532041e5f4733b5cce5fed8f3 456,212 bytes
- `provenance.json` 97a66648fa1ef3d782a7e0d1be25a472e3d4248521e20afc78bba0856d9006cb 1,001 bytes
- `rendered.html` afa2a67a0dee2a2d057885312d74f1277ab47cc85f919220d2421a6d6044265d 183,693 bytes
- `screenshot.png` cf4d945cb2330cd935081e252fc10d1572223e7a321e3d7f8c1e4e333a7737ee 21,632 bytes
- `text.txt` 1837b6e2c766cabd6d7c651bca1ee976260ea128783d9173159ed738d75ff2ab 106 bytes

### [watchtowr.com](watchtowr-php2shell-faq/index.html) [original ↗](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/)

**watchTowr** · researcher · primary · captured · published not stated · added by `claude-story-site` · `watchtowr-php2shell-faq`

BLOCKED: HTTP 403.

capture 20261022T111847Z · HTTP 200 · chrome-error://chromewebdata/- `headers.json` 0c655abac86df9e59b49a895ed0bc35a702af92b957d5db757df55be64fd9ff8 2,908 bytes
- `page.html` 9ad5ad45ab50498bff4fec7104988da089ca1e17cc8145805e57fe493e22893c 457,843 bytes
- `provenance.json` 779e5cb94040a7b1083dedc2aa737205276d134f02007caceae9ff3ab737420c 993 bytes
- `rendered.html` ed77bdfb70c799526cb11ef4c80486ab375a2bebf338de76275278dd5be92f25 183,669 bytes
- `screenshot.png` cf4d945cb2330cd935081e252fc10d1572223e7a321e3d7f8c1e4e333a7737ee 21,632 bytes
- `text.txt` 1837b6e2c766cabd6d7c651bca1ee976260ea128783d9173159ed738d75ff2ab 106 bytes

### [Recent wiki downtime (PHP2Shell mitigation) | Weird Gloop](weirdgloop-blog-php2shell/index.html) [original ↗](https://weirdgloop.org/blog/php2shell)

**Weird Gloop (cookmeplox)** · vendor · primary · captured · published 2026-10-21 · added by `claude-story-site` · `weirdgloop-blog-php2shell`

Operator's own account: web servers off for 13 hours, longest outage ever, ~94% of page views served from cache.

capture 20261022T111827Z · HTTP 200 · https://weirdgloop.org/blog/php2shell- `headers.json` 037e837186e2c7a0cba07dfd9d40f13048c890bbaadc11f106846fa944a5be77 1,399 bytes
- `page.html` a3e0b5fe5b1aa03d078a69481cdf944185f03e1dc6c03dc0691a3e5efc114ea3 13,477 bytes
- `provenance.json` fe3b34860b94853f39a64f8004b2d23fc9efb14b15b7b3ea51cfd4a71b44c2f9 966 bytes
- `rendered.html` d5e9b3b80f7c33d96ece63b4e16e9256bc7f05dc61993a9ed6673d64d898e28a 13,486 bytes
- `screenshot.png` 8014b0889ab8777b9c1ef8b2562da1fe3f4c2d0d858c2727dfe7d79acae1ceaa 369,760 bytes
- `text.txt` 6bd492a6220e8eea4b3f89a098f09f546ccd4df2f38848c651a016aa215ae962 4,262 bytes

### [Dan Kaminsky - Wikipedia](wikipedia-dan-kaminsky/index.html) [original ↗](https://en.wikipedia.org/wiki/Dan_Kaminsky)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-dan-kaminsky`

Tertiary: Dan Kaminsky, for the 2008 DNS flaw.

capture 20261022T113323Z · HTTP 200 · https://en.wikipedia.org/wiki/Dan_Kaminsky- `headers.json` 230fef32ef2b8e3a03fd564dddff422d11bc2aaa9c55bf790e489e49cd1728d0 6,516 bytes
- `page.html` 6c89a48790d2570768a3e30b6e6773d391a8726a2ea374490158e9788351b499 239,532 bytes
- `provenance.json` 912e913138aa6da2c78cb8a72b6f0f49ff311ecb7d55a3f3ebe018788dc415c7 940 bytes
- `rendered.html` 6965408cf93703569203e0b1fa6278195218e7179ca2f79c981126987636c876 431,088 bytes
- `screenshot.png` 615f1446bfe1602439edb7b7273d7e7b74aeb78f40c45e5ef95312ecab6b44d8 2,208,990 bytes
- `text.txt` 565033cfb92639ca1311f148e4c1fddbec463cd655a7b253b698b0d3bbee7d5b 19,564 bytes

### [2017 Equifax data breach - Wikipedia](wikipedia-equifax-breach/index.html) [original ↗](https://en.wikipedia.org/wiki/2017_Equifax_data_breach)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-equifax-breach`

Tertiary: the 2017 Equifax breach (Struts CVE-2017-5638).

capture 20261022T113329Z · HTTP 200 · https://en.wikipedia.org/wiki/2017_Equifax_data_breach- `headers.json` c3bc169ae4d898eb6475902410fddd73fa4ed34ce0daddd19f5f6a5f46ce5742 6,561 bytes
- `page.html` 063ebe77541faf5b4a538fb6536569545115ba07e4ece30ec4b609b3f10e0715 357,275 bytes
- `provenance.json` f1e5a749836d6e8fa78cb7d8298991d435408424506415523c68e32f854be7ea 978 bytes
- `rendered.html` fd59a52a810139932c34d91ab988792d0f289833507ce5edaa59b5f0c50a1403 561,514 bytes
- `screenshot.png` 87c5de1374b3c50ce76b221a56993bae2c23023f9774f9bce5dea3822cde37c9 3,123,746 bytes
- `text.txt` e38b857233007afea66a356c3b1b109917746f474776fef1897536936986af07 34,565 bytes

### [Heartbleed - Wikipedia](wikipedia-heartbleed/index.html) [original ↗](https://en.wikipedia.org/wiki/Heartbleed)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-heartbleed`

Tertiary: the Heartbleed article, for the context page.

capture 20261022T113241Z · HTTP 200 · https://en.wikipedia.org/wiki/Heartbleed- `headers.json` ebf98b097de4ce11194b4121b9de21f82d8c75e7117279bd2b10d469c923f907 6,561 bytes
- `page.html` 548f1ff2c768078511e876df9f95289590100729e454fe278693a08fc838717e 833,943 bytes
- `provenance.json` 6ce9e63913d1a8ac51b9519d592d2eb038f9cf41bd235baf4008e90594ca666b 932 bytes
- `rendered.html` 7fa05158620c1d78de2df881c24a28d80da7f4244ada06ba16854d311e830cf5 1,113,858 bytes
- `screenshot.png` 7affc5c7f2af7e59d01dddfa5ae745b2a322d785e9d0e23b518defaf08b9b12c 6,147,603 bytes
- `text.txt` 335a02e5907d498b4ff7cd3bb3e63c86596c9590ec307cd2b82a13a8d0b9911d 66,888 bytes

### [Log4Shell - Wikipedia](wikipedia-log4shell/index.html) [original ↗](https://en.wikipedia.org/wiki/Log4Shell)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-log4shell`

Tertiary: the Log4Shell article.

capture 20261022T113317Z · HTTP 200 · https://en.wikipedia.org/wiki/Log4Shell- `headers.json` 87abc43f478d756f7d6b4f160635cf45fb9be84375d34b71cc12d70e91c81117 6,559 bytes
- `page.html` f21f5113f869aeb05d3c2467525fa6a946a0622c8295ec8ca5e52e2cdee958ad 350,814 bytes
- `provenance.json` d08c417c0b7261fd57ff15f73a65ba91d48121268d596490e7f069b30b449a53 928 bytes
- `rendered.html` 6b9cee027909f277350e142b3d325f5a0575732f0b5e2c76f8c35c9361c214e3 553,202 bytes
- `screenshot.png` a64453cfa8cdf7caa73bdc64dbb02943ed99ea9130ce83fd5c6cdd1cebdb74d5 2,405,972 bytes
- `text.txt` cd08f6a7082ea6e3cc172d7738243c4eda26331c8af2aded091e27dca5066058 25,890 bytes

### [2023 MOVEit data breach - Wikipedia](wikipedia-moveit-breach/index.html) [original ↗](https://en.wikipedia.org/wiki/2023_MOVEit_data_breach)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-moveit-breach`

Tertiary: the 2023 MOVEit breach.

capture 20261022T113336Z · HTTP 200 · https://en.wikipedia.org/wiki/2023_MOVEit_data_breach- `headers.json` 5c9771f190e153438296ebd93a2e83ed2e272b0edabfdc8e90270b0e8cc36a0a 6,516 bytes
- `page.html` 586dcd3eba4df977cd0483dd2543c14bb75c8097933ea13131fa4b0913ac6847 163,389 bytes
- `provenance.json` 9ac856ea4fd003d7c9d3e5784e6ab684a8bc8ccd3c807e4cf1174b414aee3936 974 bytes
- `rendered.html` bcc9ee65deff5809f27130574759019489d461e3374937d785fd991252a55488 339,581 bytes
- `screenshot.png` 3348e9116d0ce06e40962d5c5f4bb2592f0ff8d1b01baab3d3911f1710f8f8f5 1,089,154 bytes
- `text.txt` ad5c2515a778a3582e85c270cfbb1178c90a7477c3f38eaf804fa10528942be1 11,123 bytes

### [PHP2Shell - Wikipedia](wikipedia-php2shell/index.html) [original ↗](https://en.wikipedia.org/wiki/PHP2Shell)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-php2shell`

Tertiary: the encyclopaedia article, captured as a record of the public account on 22 Oct; says publicly announced 20 Oct and patched the next day.

capture 20261022T112309Z · HTTP 200 · https://en.wikipedia.org/wiki/PHP2Shell- `headers.json` df684951111f873760fab5d20078208e1e989557f1150d9aeaa7966ee6c8ca75 6,560 bytes
- `page.html` f306b23e38d55d74fa6405a49e04b8dd420d7f5795c1b999f7d2303feed2a904 223,796 bytes
- `provenance.json` 16395d927a990f7bb2679d0861242bf3705586641c4f2e7bc9b839580b0eaf64 928 bytes
- `rendered.html` f51281e6ee013358343fd07568c8ef63acc38f4340841c824d6c3941004b14e3 408,195 bytes
- `screenshot.png` ae58953f05c3bd41c5e57931462c15c8213fb7843a0c45d0b9b045b00f4ce8c5 1,586,902 bytes
- `text.txt` bbb51bbd069506b09282b45086984565ae875b5d974d121584c8e2b3c912222f 16,230 bytes

### [Shellshock (software bug) - Wikipedia](wikipedia-shellshock/index.html) [original ↗](https://en.wikipedia.org/wiki/Shellshock_(software_bug))

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-shellshock`

Tertiary: the Shellshock article.

capture 20261022T113310Z · HTTP 200 · https://en.wikipedia.org/wiki/Shellshock_(software_bug)- `headers.json` f2a4b3ae6fb24202324c3478fe96ec7d871fbf062829bf047dea987ca29a646d 6,559 bytes
- `page.html` 800b60bd11e65365ea12c0db8526f932f55188ca76f3f6eaec4ff4833ba26fec 326,860 bytes
- `provenance.json` 0468fb94f26b99cb42b1033597a200e955bd047d1d544cf0aa1e63108588a950 977 bytes
- `rendered.html` 2823f220d4e3aa6ce700cdff250ab35732495a32d273c0b6ab24dd2445aa2dc1 522,813 bytes
- `screenshot.png` 5f62672b0225c6d055a4a1d802c68a3acf695790ff6f20fee8baaf67f7b5f21a 2,735,619 bytes
- `text.txt` 300be73066bba3f66a53bc1116a1a3c7bbe5e61695f1ce8a801c112237b61041 27,686 bytes

### [Spring Framework - Wikipedia](wikipedia-spring-framework/index.html) [original ↗](https://en.wikipedia.org/wiki/Spring_Framework)

**Wikipedia (English)** · other · secondary · captured · published not stated · added by `claude-story-site` · `wikipedia-spring-framework`

Tertiary: Spring Framework (Spring4Shell section).

capture 20261022T113341Z · HTTP 200 · https://en.wikipedia.org/wiki/Spring_Framework- `headers.json` 93660dd4eb58188f8cdd099a1a9f09f42a33c872d13690748edc637974e623d7 6,517 bytes
- `page.html` 242f49c0d152a3caa2f0bf0cbfef5baa6f4dfcc62b890886a6f53576021af63d 622,623 bytes
- `provenance.json` 2a065f50a364fdd1cae0a5b064fe9e7fe715a6aabe14d7e11ca72727b5b61330 956 bytes
- `rendered.html` 96223727d419aba6ee0c683f3d172a10324e28762e3f7dcb32d41519da2596a8 896,578 bytes
- `screenshot.png` 0601fe81d23975fda4d4036553b0ff37eb4fe8ea9928d9b697df2d4791acf6da 4,931,001 bytes
- `text.txt` 710060585680e022348a35516ce4f13f4d99c2df75fe72a6ec01fe1a223081d1 49,455 bytes

### [PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](wiz-blog-php2shell/index.html) [original ↗](https://www.wiz.io/blog/php2shell-php-rce)

**Wiz (Wiz Research)** · researcher · primary · captured · published 2026-10-21 · added by `collector-researchers` · `wiz-blog-php2shell`

Wiz Research post dated October 21, 2026. Source of '70% of the Internet' headline; body basis is 'powers 70% of all websites'. Disclosure timeline: discovered Aug 19, reported Aug 24, PHP ack Sep 21. Credits Gemini 4 Argon, GPT-5.6 Sol, Wiz Atlas.

capture 20261022T081047Z · HTTP 200 · https://www.wiz.io/blog/php2shell-php-rce- `headers.json` f3a7f515bda9ae91541c7792cad2fbb4d5864a7962be4f5db93bccbe8caa2d03 5,075 bytes
- `page.html` 32408c9f60071e7bdcf0e702160f6c398d6967cb89fbc81b5f0e0029e34af07b 438,665 bytes
- `provenance.json` 4e362d46ccd571e124b20fb3518c8d00076dc508a0146ee5338a7dce931d1fa1 1,002 bytes
- `rendered.html` 6db43e32910bdf4bc2b82a93afa5097900aa4a205b5cdde32d1a2510beff4c68 580,534 bytes
- `screenshot.png` 4ba83874c540e1f7faf4c817b6b8c3ae1ef61eacda5851a112d6601e47d6d91f 2,753,995 bytes
- `text.txt` e3568b6f88c93f6bb08eebe3c8811f9fd283212f7331b287d5170b91d6bad1ea 19,147 bytes

### [Matthew Prince 🌥 on X: "Some stats on #php2shell. In the 10 hours before it was publicly announced, across the @Cloudflare network we saw thousands of attempts to exploit it. That jumped to tens of thousands in the 45 minutes post announcement, hundreds of thousands within 2 hours, and millions no… / X](x-eastdakota-php2shell-stats/index.html) [original ↗](https://x.com/eastdakota/status/2113079352682570051)

**Matthew Prince (@eastdakota), Cloudflare CEO** · social · primary · captured · published 2026-10-22T01:25Z · added by `claude-story-site` · `x-eastdakota-php2shell-stats`

Attempt counts: thousands before announcement, tens of thousands in 45 minutes, hundreds of thousands in 2 hours, millions by 01:25 UTC 22 Oct. 1.4M views at capture.

capture 20261022T111808Z · HTTP 200 · https://x.com/eastdakota/status/2113079352682570051- `headers.json` d77dc66c0c59c96e2e54ddfecf08d3b1bd24635a9d74435e5e11a42df31beefb 9,023 bytes
- `page.html` 957516e4670ab0fa18a3dbfcc6a2a4fb7bf154370fd7b09506a876e6d327f357 143,568 bytes
- `provenance.json` 6ef963e6f636da1603f65de2817e02480ed92a2c4d5b330a151bc2d515c21277 1,249 bytes
- `rendered.html` 25a31a5f7554396a5640c88efcf0624e0eab811ea96a53cebc603eb9c55925ad 165,274 bytes
- `screenshot.png` 7a098d734f074f04d4c95973bd0f4463f3c18bd7aaf274912a6eea795095879c 216,866 bytes
- `text.txt` 4069805bcb164ff1a04dbf2f3900e36c0c61120ca2122452ba6372c46f1737b3 1,884 bytes

### [Feross on X: "Chainguard received PHP’s fix for two critical RCEs under embargo, like every other distributor. On October 21 at 07:41 UTC, more than six hours before the coordinated release, it published built images containing that fix. The PHP Foundation’s postmortem says Chainguard unilaterally… / X](x-feross-chainguard/index.html) [original ↗](https://x.com/feross/status/2113043398664015878)

**Feross Aboukhadijeh (@feross) on X** · social · secondary · captured · published 2026-10-22 · added by `claude-story-site` · `x-feross-chainguard`

A security founder's summary of the Chainguard embargo break; 'PHP runs 69% of websites whose server-side language is known'.

capture 20261022T112105Z · HTTP 200 · https://x.com/feross/status/2113043398664015878- `headers.json` c7243f6c403eb56e9b3d6e563eb8a8b216ea9dd8211fb1b22d4707fb94277f57 9,023 bytes
- `page.html` a96f60627079ac4894ec940931bd0fd5f7aafe3bf8894230fb3292b941681412 192,869 bytes
- `provenance.json` a7be68aef95eb2bd14be51e50215f101dd44d0e36eb5539a9393115df9ab4ce2 1,233 bytes
- `rendered.html` 61fc4e7f751c5a119c9a9a1081b8c47669ac9fe2d7dfd07833772658c39e8fdf 173,209 bytes
- `screenshot.png` 75299998b6abad9947b1d3f6d8ce0f477a1e8980c7f9484bdde10796bfc16bb1 560,505 bytes
- `text.txt` de7648491d66413734279a020d89f709bff521b202058171a6b74288788f7fc6 5,709 bytes

### [LCFR on X: hash commitment d935be02…](x-lcfr-hax-hash-tweet/index.html) [original ↗](https://x.com/lcfr_hax/status/2085031675382071483)

**Ryan Austin (@lcfr_hax), Calif** · social · primary · captured · published 2026-08-05T15:54Z · added by `collector-researchers` · `x-lcfr-hax-hash-tweet`

Hash-only tweet shown as '15:54 · 5 Aug 2026' (capture browser in UTC). Cited by Calif's timeline and by X Community Note on OpenAI's post as proof of prior discovery. Pre-image not published here.

capture 20261022T081603Z · HTTP 200 · https://x.com/lcfr_hax/status/2085031675382071483- `headers.json` ea81d1bf086428a65e67d0551ac1c3aebc53a1cd4c39b43d3ed837bbd8acee28 9,022 bytes
- `page.html` 11a7ec8817e3966590490fb928089c210339261afe54cc2f72353dca15f41391 132,347 bytes
- `provenance.json` 508544ce2c74aa23119fa27daa5a30b5ae63e47e7cd3e690fb9cf9a54ef7cded 1,012 bytes
- `rendered.html` 9a1b5b36d22e9689e136b35c76adc712c6977f4ec6f1bd41655bdb1caff65fac 160,702 bytes
- `screenshot.png` 9dfa4845de672eb2ec27885a9cff17fe9af803635a290c1cfc17f6ee5902d54e 262,114 bytes
- `text.txt` 2c10f3991caf3a74b21df9d9e0362fd1bab8aefc5113877a412dac999ca36372 1,018 bytes

### [OpenAI on X: OpenAI models helped researchers ... discover critical security flaws in PHP](x-openai-php2shell/index.html) [original ↗](https://x.com/OpenAI/status/2112907856018309586)

**OpenAI (@OpenAI)** · social · primary · captured · published 2026-10-21T14:04Z · added by `collector-researchers` · `x-openai-php2shell`

Shown '14:04 · 21 Oct 2026', 5.2m views. Full text captured (stands in for the blocked openai.com post). Carries an X Community Note disputing OpenAI's discovery role and linking lcfr_hax.

capture 20261022T081645Z · HTTP 200 · https://x.com/OpenAI/status/2112907856018309586- `headers.json` 427b75f5bb12cb7b0acee221f2065095d92c82279e0db87f9b80909525886df3 9,023 bytes
- `page.html` 8e6a0183b6982e8530d7b48277e4b0f6f010b22d3348b30328cc4460cc371d90 160,064 bytes
- `provenance.json` 3e52aad242520de5ca4db4103baf86c58e7d477a8f7c04c19b841034f1ca49e3 1,232 bytes
- `rendered.html` 2e31eee6ab72f0703675cd74158267dbe5cfb55bf03b80153deaa1b899be4c10 147,195 bytes
- `screenshot.png` aaf750d50e69e80b34fbdf908a9fdc330ac315b765eacb2e3e8361cb40f2cbb2 570,247 bytes
- `text.txt` 785b7cae55e3748b3d11e002f9b254408a57849c1ef08eb9fcc16a2cd196f189 3,316 bytes

### [Wiz on X: BREAKING ... #PHP2SHELL ... impacting 70% of the Internet](x-wiz-io-php2shell/index.html) [original ↗](https://x.com/wiz_io/status/2112899813264277528)

**Wiz (@wiz_io)** · social · primary · captured · published 2026-10-21T13:32Z · added by `collector-researchers` · `x-wiz-io-php2shell`

Shown '13:32 · 21 Oct 2026' (UTC in capture browser) — 28 min before the 14:00 UTC release. Thread says 'Apply the Oct 22 security release immediately' — stale date from the original schedule.

capture 20261022T081624Z · HTTP 200 · https://x.com/wiz_io/status/2112899813264277528- `headers.json` f9a8ec8c80b7e7b13a6e772a718ece30ec0796dffd3481acc57a310616eca249 9,022 bytes
- `page.html` 6adc23abb012a9e89f22453d2d8d4f0eff574edc67373bc94eef59cfc12ebe85 183,867 bytes
- `provenance.json` 5df6949985ad1cf4a150d5b9a7e52f1355bac3b127484b31c70c8052986b1556 1,086 bytes
- `rendered.html` 9c5f87ac8afbe6aad1205a23ecbe79d83dc801c77f4d0ffb750ffb5b53625888 193,354 bytes
- `screenshot.png` d2187dc09d49ec23ea5593aa7ffef5df60cd2385f290922ec6d77b6861fc7abb 578,314 bytes
- `text.txt` 6c17977662815b0cb25a32e0987d1b1f95942156825b0cc616dc43a3f7f46809 2,222 bytes

### [Finland temporarily shuts down government websites as a precaution for critical vulnerabilities | Yle News | Yle](yle-finland-government-sites-shut/index.html) [original ↗](https://yle.fi/a/74-20252600)

**Yle (Finnish public broadcaster)** · news · secondary · captured · published 2026-10-21 · added by `claude-story-site` · `yle-finland-government-sites-shut`

Finland temporarily shuts government websites as a precaution; Valtori; NCSC-FI rated 9.2, no sign of exploitation.

capture 20261022T113225Z · HTTP 200 · https://yle.fi/a/74-20252600- `headers.json` 629207adb678c676219268f5339e1768a1aa4af6f503c8ab3dc33a9690a1dc94 4,002 bytes
- `page.html` 2845424a60768d77b6561e42e259b0675624771b8b77baa4741fbaf4cd0103c8 325,894 bytes
- `provenance.json` e77236132533b194633ab7767e55f09e2854beb49c9ce44fc2725e3606534e78 1,011 bytes
- `rendered.html` 156e30b543681b560d3356d18ca5ff9531fa172e3e81f59ceae7ec8662120dd9 269,020 bytes
- `screenshot.png` f6f90718b94a07351d302934a8a237c2e0360d1ac9ae51e79faf8a29afdaf46e 2,031,875 bytes
- `text.txt` 720785d651f827be6d44f009bb84e15924a410299bf53fbe4f193194c1c30a57 6,283 bytes


---
site v0.9.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/sources/index.html
