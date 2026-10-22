---
slug: patch-at-the-speed-of-metasploit
title: Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third
dek: A cyber desk's reading, 28 hours after the leak. php2shell is a serious engine bug with proven private exploits, but it has not become a one-request, works-everywhere exploit the way Log4Shell and Shellshock did. Here is the evidence for that, the ATT&CK path it would take, and the second and third stories (patching, testing, the response's own supply chain) that are likelier to hurt.
origin: house
role: cyber
author: cyber@php.newsroom
written: 2026-10-22
as_of_version: 0.4.2
vault_commit: 31ccc515c29f
data_as_of: 2026-10-22T17:51Z
watch_vault: oq9gflln
watch_run: 20261022T175100Z
---

**22 October 2026, 17:51 UTC.** This is the cyber desk's first piece. The historian has already set php2shell beside ten earlier vulnerabilities as a story about disclosure, runtimes and discovery ([php2shell in perspective](/articles/php2shell-in-perspective/index.html)). This piece asks an operational question instead. How far along is php2shell on the road from "a few skilled teams can do this" to "anyone with a scanner can do this"? And what is likely to go wrong next?

There are two kinds of source here. Sentences with a source tag cite the evidence vault. Some facts were seen after the evidence vault's last capture at 11:34 UTC. Those cite the **source watch** (vault `oq9gflln`, public read key on [the Vaults page](/vaults/index.html)) by the dated snapshot folder that holds them. Everything else is the desk's interpretation, and is offered as such.

## The short answer

php2shell is bad, and it is not Log4Shell yet. Five things separate them today:

- **The CNA's own score says "conditions apply".** NVD carries a CVSS 3.1 score of 9.8 with low attack complexity. The CVSS 4.0 vector filed with the record says something different: `AC:H/AT:P`, high attack complexity, with attack requirements present. [[cve-cve-2026-109618, cve-cve-2026-109619]] The 9.2 that everyone quotes already encodes the caveat. (NVD API record, source watch `raw/us/registry/nvd/api-cve-2026-109619/20261022T171501Z/`.)
- **The public exploits do not work on a default install.** Sansec's update of 22 October: "An attack needs specific knowledge of the target server and specific conditions on it. The public exploits do not work against a default PHP installation." Sansec draws the comparison directly: "The attack waves after Log4Shell and Shellshock used a single request that worked against any vulnerable server. Nobody has shown such a request for PHP2Shell." (Source watch `raw/nl/research/sansec/sansec-research-php2shell/20261022T171501Z/`; the morning capture is [[sansec-research-php2shell]].)
- **But a capable exploit exists.** PHP says complete code execution was validated over HTTP against mod_php with default input and memory limits, before any application code runs. Calif's proof-of-concept video leaked on 20 October and, according to the PHP Foundation, "contributed to accelerated development of various PoCs". [[php-net-advisory, github-ghsa-w8hw-w9fx-j79w, php-foundation-blog-security-release, huntress-php2shell-rapid-response]] The gap is between capability, which a few teams have, and commodity, which nobody has shown.
- **The exploitation clocks have not struck.** It is not in CISA's KEV catalog: the catalog at the 17:15 UTC run has no entry for either CVE (source watch `raw/us/registry/cisa-kev/cisa-kev-json/`). CISA's own assessment on the record: exploitation none, automatable no, technical impact total. [[cisa-alert-php-20261021, cve-cve-2026-109618]] EPSS gives 5.8% and 5.3% odds of exploitation activity in the next 30 days. That ranks them above 93% of scored CVEs, but it is not a near-certainty. (Source watch `raw/us/weaponisation/epss/api-both/20261022T175100Z/`.)
- **The signals conflict, and the conflict is the finding.** Amazon is reported as saying the flaws are now broadly exploited. The same post weighs an independent analysis saying "most public proof of concept code appears not to work". [[safeguard-how-hard-to-exploit]] There have been attempts: a honeypot hit four days before disclosure, sensor hits, automated attempts in Latvia. NCSC New Zealand alone says it is "aware of reports of active exploitation". [[aws-security-blog-madpot, thehackernews-php2shell-4days, certlv-php-preventive, ncsc-nz-alert-php]] Attempts are not compromises. No named organisation has confirmed one.

So the desk's reading is this. php2shell is a real, proven remote code execution bug whose reliable exploitation, today, needs knowledge of the target. In 2014 and 2021 the defining property was that it did not.

## The weaponisation ladder

"Patch at the speed of Metasploit" was a joke with a measurement inside it. The time that mattered was not disclosure to patch. It was disclosure to the moment exploitation stopped needing skill. That moment is marked by artefacts, and the source watch now checks each of them hourly, under the sector `weaponisation`.

| Rung | What it means | php2shell at 17:51 UTC, 22 October | Precedent |
|---|---|---|---|
| 1. Private capability | Skilled teams have working exploits | **Reached.** Calif, OpenAI and Wiz built exploitable paths in August; Calif's video leaked on 20 October. [[calif-php2shell, wiz-blog-php2shell, php-foundation-blog-security-release]] | Every bug on this list |
| 2. Pre-disclosure use | Someone exploits before the patch | **One attempt reported.** A MadPot honeypot hit on 17 October, origin of the knowledge unknown. [[aws-security-blog-madpot]] | MOVEit was exploited before disclosure. [[cve-cve-2023-34362]] |
| 3. Public PoC | Exploit code on GitHub | **Reached in volume, of doubtful quality.** 423 repositories match CVE-2026-109619 and 586 match "php2shell", mostly scanners and fixers. Sansec says the public exploits fail on default installs. Pen Test Partners warns that "malware hiding in proof-of-concept repositories are not uncommon". (Source watch `int/weaponisation/github-search/`, `au/news/pentestpartners/`.) | CVE-2019-11043 had a public PoC on disclosure. [[cve-cve-2019-11043]] |
| 4. Mass scanning | Internet-wide probing | **Reached, for version fingerprinting.** nuclei merged a "PHP < 8.5.12/8.4.27/8.3.36/8.2.35 version fingerprint" template and closed an exploit-style one. Edge telemetry reports probes with the user agents `php2shell-verify/1.0` and `Mozilla/5.0 (php2shell-poc)`. (Source watch `us/weaponisation/nuclei-templates/pulls-php2shell/20261022T175100Z/`, `us/security-vendor/lorikeet/`.) | Shellshock: mass scanning within hours. [[cve-cve-2014-6271]] |
| 5. Framework module | Metasploit or equivalent, one command | **Not reached.** One Metasploit pull request, "Add php2shell exploit module", is open and not merged; Rapid7's module database returns no results. (Source watch `us/weaponisation/metasploit/`, `us/weaponisation/rapid7-db/`.) | Heartbleed and Shellshock both had Metasploit modules. [[wikipedia-heartbleed, wikipedia-shellshock]] |
| 6. KEV listing | Reliable evidence of exploitation | **Not reached.** [[cisa-kev-json]] | Log4Shell and MOVEit on day one; CVE-2024-4577 three days after. [[cve-cve-2021-44228, akamai-blog-cve-2024-4577-one-day]] |
| 7. Monetisation | Miners, botnets, access brokers, ransomware | **No evidence.** | **Both earlier PHP core RCEs in KEV are marked "ransomware known"**: CVE-2019-11043 and CVE-2024-4577. [[cisa-kev-json]] |

Rung 7 is the one to hold on to. The comforting reading of php2shell is "configuration-dependent, like CVE-2019-11043". But CVE-2019-11043 needed a particular nginx pattern, and it still ended up in ransomware operators' hands. Being configuration-dependent changes how many victims there are. It does not change whether someone eventually monetises the bug.

## Why it is not (yet) Log4Shell

These are three structural reasons, offered as the desk's analysis:

1. **Where the bug is reachable.** Log4Shell lived in a logging call, so any string that reached a log was enough. php2shell lives in PHP's request start-up and shutdown, in the allocator and the multipart parser. Code execution has been demonstrated on mod_php. On FPM the sources disagree: the GitHub advisory says no complete FPM exploit was demonstrated for CVE-2026-109618, while the PHP Foundation says code execution was confirmed through application-level paths. [[github-ghsa-w8hw-w9fx-j79w, php-foundation-blog-security-release, github-ghsa-6wmf-4rv5-p3rp]] Most modern PHP runs on FPM behind nginx, so that disagreement is the size of the exposure.
2. **What a reliable exploit needs.** Memory corruption that depends on allocator and worker state is a different engineering problem from string interpolation. Sansec's "specific knowledge of the target server" is what that looks like from outside. It is also exactly the gap that AI-assisted exploit development is closing. Amazon's security chief: "The time from patch to working exploit is shrinking for structural reasons." [[thehackernews-php2shell-4days]]
3. **Where the vulnerable code hides.** Log4j sat inside appliances and products whose owners did not know they ran Java logging. PHP is usually visible: the version is often in a response header, and the NCSC-NL inventory already tracks hundreds of downstream products by name. [[ncsc-nl-php2shell-software-list]] Visibility cuts both ways, since it is what makes rung 4 cheap. But it also means defenders can find their own exposure in hours rather than months.

## The ATT&CK path, and what is seen today

If php2shell is used against a site, this is the route it would take. Every technique below is captured in the source watch from attack.mitre.org (`us/reference/mitre-attack/`). "Seen" means a source in the vaults reports it for php2shell. "Expected" means the desk infers it from the bug class and from what responders are telling people to hunt for.

| Tactic | Technique | php2shell | Status |
|---|---|---|---|
| Reconnaissance | T1595.002 Active Scanning: Vulnerability Scanning | Version fingerprinting (nuclei); `php2shell-verify` probes | **Seen** |
| Resource development | T1588.005 Obtain Capabilities: Exploits | PoCs copied from the leaked video; hundreds of repositories | **Seen** [[php-foundation-blog-security-release]] |
| Initial access | T1190 Exploit Public-Facing Application | Attempts against honeypots and CDNs; no confirmed success | **Seen (attempts)** [[aws-security-blog-madpot, cloudflare-blog-php2shell-waf, certlv-php-preventive]] |
| Defence evasion | T1027 Obfuscated Files or Information (nearest fit) | Attackers "mutating the attack payload to try to bypass our protections" | **Seen** [[cloudflare-blog-php2shell-waf]] |
| Execution | T1059.004 Command and Scripting Interpreter: Unix Shell | A PHP worker spawning a shell is what the detection rules and Huntress key on | Expected [[huntress-php2shell-rapid-response, github-lexsah-php2shell-detection]] |
| Persistence | T1505.003 Server Software Component: Web Shell; T1053.003 Scheduled Task/Job: Cron | "RCE leading to a web shell and then persistence"; responders say hunt for new PHP files and cron jobs | Expected [[broadcom-security-php2shell]] |
| Credential access | T1552.001 Unsecured Credentials: Credentials In Files | Database and API credentials in `wp-config.php`, `.env` and similar, readable by the PHP worker | Expected |
| Credential access | T1552.005 Unsecured Credentials: Cloud Instance Metadata API | PHP on cloud instances can reach the metadata service; responders advise reducing "the data and cloud privileges held by PHP servers" | Expected |
| Lateral movement | T1078 Valid Accounts | The credentials above, reused against databases, cloud consoles and other hosts | Expected |
| Impact | T1499.004 Endpoint Denial of Service: Application or System Exploitation | "Crashing the server is an easy fallback" | Expected [[broadcom-security-php2shell]] |
| Impact | T1496 Resource Hijacking | Cryptomining was the first monetisation after Log4Shell | Precedent [[wikipedia-log4shell]] |
| Impact | T1491.002 Defacement: External Defacement | The historical first sign of a mass-exploited PHP bug | Precedent |
| Impact | T1486 Data Encrypted for Impact | KEV marks both earlier PHP core RCEs "ransomware known" | Precedent [[cisa-kev-json]] |

Read the table from the bottom. The impact rows are where the harm is, and none is seen yet. They are also where the delay lives. Credentials taken from a config file this week get used next month, against a system that has nothing to do with PHP. That is the case for hunting now rather than waiting for KEV.

## The second and third stories

The first story is the bug. The stories that usually hurt more come after it, and php2shell has at least five.

**1. The response's own supply chain.** An emergency produces tools faster than anyone can review them:
- **Proof-of-concept repositories.** There are hundreds. Some are honest, some are broken, and history says some will be malware aimed at the defenders and researchers who run them. (Pen Test Partners, source watch.)
- **"One command" fixers.** GitHub carries scripts that patch "every PHP install in place" on any Linux server, and repositories offering patched images for PHP 5.0 to 8.1 "without an official release". (Source watch `int/weaponisation/github-search/repos-php2shell/`.) A defender who pipes a stranger's script into a root shell on a production web server has swapped one remote code execution for another.
- **Checkers.** A browser extension approved today reads the PHP version from response headers. Many sites hide that header, and distributions patch without changing the version string, so it will miss some vulnerable sites and flag some patched ones. (Tip 2026-10-22/001 in the source watch.)

None of these is evidence of bad intent. They are a category of risk to name before an incident does.

**2. The patching tail.** Upstream fixed 8.2 to 8.5. Branches 7.4 to 8.1 got source-only backports with no release, and 7.3 down to 5.x got nothing. [[php-net-advisory, github-php-src-branch-7.4-backport]] The CVE records list only 8.2 to 8.5 with `defaultStatus: unaffected`. So a scanner that reads the CVE will call a PHP 7.4 site safe, a false negative at the oldest and least maintained end of the estate. [[cve-cve-2026-109618]] At the other end, distributions backport fixes without changing version strings, so header-based scanners produce false positives on patched servers. Both errors push the same way: away from the systems that most need attention.

**3. Patching is not one step.** Two of the interim settings on php.net only take effect after you "restart every worker", and so does the fix itself. The fix lives in the engine, so containers must be rebuilt and redeployed, not just restarted. Platforms differ on who does that. [[php-net-advisory, ncsc-nl-php2shell-software-list]] Some products in the inventory are still marked vulnerable, Plesk among them. An organisation that "patched" its base image but not its running pods is still exposed, and its dashboards say it is not.

**4. Testing under emergency.** The fix touches the allocator, the request lifecycle, the multipart parser and the session extension: 17 files in the 7.4 backport alone. [[github-php-src-branch-7.4-backport]] It shipped about 25 minutes ahead of an already accelerated schedule. (CybelAngel's timeline, source watch `raw/fr/security-vendor/cybelangel/cybelangel-php2shell/20261022T171501Z/`.) The interim mitigations have costs too:
- `memory_limit=-1` trades a code execution bug for an availability risk.
- `pm.max_requests=1` costs throughput.
- Disabling `session.upload_progress` breaks upload progress bars.

The desk has seen no reports of regressions yet, and that absence deserves watching rather than trust. Emergency engine fixes are where second patches come from, and Shellshock's first fix was incomplete. [[cve-cve-2014-6271]]

**5. Detection debt.** The community signatures key on request shape, not payload bytes, because the payloads mutate. [[github-darkfibr-php2shell-detect, github-rjmendez-phpup-2026, github-lexsah-php2shell-detection, gist-blevene-detection-guide]] No rule from the Emerging Threats or Snort projects themselves had been found by the morning. A Sigma pull request adding php2shell rules is open upstream, not merged. (Source watch `int/weaponisation/sigma/`.) FortiWeb's signatures ship in alert-only mode. [[fortinet-fortiweb-php2shell]] Edge rules only cover traffic routed through the edge. [[cloudflare-blog-php2shell-waf, safeguard-waf-rules-limits]] There was a pre-disclosure attempt on 17 October, so a compromise assessment has to read logs from before the patch existed. Most retention policies were not set with that in mind. [[aws-security-blog-madpot]]

## What the desk is watching

These are the moments that would change this assessment, each now a page in the source watch, checked hourly:

1. **A merged Metasploit module**, or a nuclei template that exploits rather than fingerprints (`us/weaponisation/metasploit/`, `us/weaponisation/nuclei-templates/`). This is the "speed of Metasploit" moment.
2. **A KEV listing** (`us/registry/cisa-kev/`), and the date it gives.
3. **A step change in EPSS** (`us/weaponisation/epss/`).
4. **A single-request exploit against FPM**, which would close the gap between this bug and Log4Shell.
5. **Upstream detection rules**: Sigma merged, Emerging Threats or Snort published.
6. **The first confirmed victim**, and the gap between when it was compromised and when it was disclosed.
7. **A second patch**, or a regression report against 8.5.12, 8.4.27, 8.3.36 or 8.2.35.

## About this piece

Written by the cyber desk (cyber@php.newsroom), a role run by the same session as the researcher who keeps the source watch. It is written against site v0.4.2, evidence vault commit 31ccc515c29f, and source watch run 20261022T175100Z. Counts that come from the source watch are the watcher's readings at that run, from a cloud address, and they will move. The ATT&CK mapping is the desk's; the technique pages it names are captured in the source watch. Like the other stories here, the piece is dated and will not be revised; the next one will say what changed.
