# Detection and defence: what blocks php2shell and what shows it

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

What Cloudflare, Akamai, Fastly, Imperva, AWS and Fortinet deployed and what each says it cannot do; the community Suricata, Sigma, Falco and ModSecurity rules; the host signals; and how hard the exploit is according to the vendors who tried.

# Detection and defence: can it be blocked, can it be seen

In plain English Can these attacks be blocked or spotted? Yes at the edge and on the server, mostly; no from ordinary web logs alone.

The editor's premise is that a zero-day is not an invisibility cloak: an exploit that runs code on a web server leaves a request in the log, a crash in the kernel, a child process in the tree. The captured sources agree, and they also say where the logs go blind. This page is what six edge vendors, three community rule sets and one detection guide say about blocking the request, and what the host shows once the request got through.

## At the edge: what the WAF vendors deployed

| Vendor | What | When | Their own caveat | Sources |
|---|---|---|---|---|
| **Cloudflare** | Seven WAF rules per ruleset plus a response-side rule, live for every plan including Free | 2026-10-21T03:02Z, about nine hours before disclosure | 'This is a STOPGAP only' (CTO Dane Knecht); attackers mutated payloads; rules only cover traffic routed through Cloudflare; patch anyway | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [Safeguard](../sources/safeguard-waf-rules-limits/index.html) [Insurance Business](../sources/insurancebusiness-uk-councils-met/index.html) |
| **Akamai** | Adaptive Security Engine rule 3000991 v1, 'PHP Remote Code Execution Attack Detected', both CVEs; existing command-injection rules also catching weaponised payloads | 2026-10-21 | 'The most effective defense continues to be the prompt application of vendor patches' | [Akamai Security Research](../sources/akamai-blog-php-core-rce/index.html) [Safeguard](../sources/safeguard-waf-rules-limits/index.html) |
| **Fastly** | A CVE-specific templated rule in the Next-Gen WAF that customers must enable; looks for 'bodies and parameters shaped in ways that differ from legitimate traffic' | 2026-10-21 | 'assume active mitigation will only serve as partial protection and may require blocking a substantial portion of legitimate traffic' | [Fastly](../sources/fastly-blog-php2shell/index.html) |
| **Imperva** | Cloud WAF protected 'out of the box'; Elastic WAF and WAF Gateway after updates; inspects anomalous multipart payloads, repeated session fields, abnormal response headers, upload-progress activity | 2026-10-21 | Had the details under embargo; saw no matching traffic before disclosure | [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| **AWS** | No managed rule found; guidance to consider blocking multipart file uploads on PHP deployments that cannot be patched, after checking the application impact | 2026-10-21 | AWS's own PHP builds for managed distributions reportedly lagged the release (a reader's comment under the post, unverified) | [Amazon](../sources/aws-security-blog-madpot/index.html) [Safeguard](../sources/safeguard-waf-rules-limits/index.html) |
| **Fortinet FortiWeb** | Three FortiGuard signatures (090502648, 090502651, 09052654) in database 0.00438, plus four custom-rule templates | 2026-10-22T07:55 (article time) | Signatures ship in alert-only mode by default; must be switched to block | [Fortinet Community](../sources/fortinet-fortiweb-php2shell/index.html) |

Every one of them says the same two things: it is a stopgap, and patch anyway. The flaw fires during request set-up, so any URL that reaches PHP is a candidate and a rule can only match shape; a rule that blocks every multipart body also blocks every upload. And a WAF sees only the traffic routed through it: the detection guide's first step is a direct curl to the origin IP to prove there is no way round.

## Signatures
- **Community Suricata and Snort rules** (darkfibr/php2shell-detect, rjmendez/phpup-2026, Lexsah/php2shell-detection). Three independent repositories, all keying on request shape rather than payload bytes: the PHP_SESSION_UPLOAD_PROGRESS field plus many array-form parts; duplicate or excessive multipart headers; a PHP worker spawning a shell. rjmendez retired its own earlier rules after finding the leaked proof-of-concept's mechanism did not match the fix. No rule from the Emerging Threats or Snort projects themselves was found. [darkfibr, GitHub](../sources/github-darkfibr-php2shell-detect/index.html) [rjmendez, GitHub](../sources/github-rjmendez-phpup-2026/index.html) [Lexsah, GitHub](../sources/github-lexsah-php2shell-detection/index.html)
- **ModSecurity, Sigma, Falco, YARA, auditd** (Blevene's detection guide; Lexsah). A ModSecurity rule on the upload-progress field name (verified on 2.9.14, 'zero false positives by construction' once the feature is off), Sigma rules for the arm-phase fatal error ('in Unknown on line 0' means the bailout happened outside any script, in the multipart parse) and for FPM segfaults, Falco rules for a PHP worker exec or memfd, auditd for execve by the pool user. The guide notes ModSecurity's REQUEST_BODY is empty for multipart requests, so an earlier tripwire that matched it never fired. [Blevene](../sources/gist-blevene-detection-guide/index.html) [Lexsah, GitHub](../sources/github-lexsah-php2shell-detection/index.html)
- **The Hacker News, on what protects before the patch** (The Hacker News). Captured for the record; the newsroom's reading of it is on the exploitation page. [THN](../sources/thehackernews-what-protects-you/index.html)

## On the host: what exploitation looks like

| Where | Signal | Sources |
|---|---|---|
| **Access log** | Multipart POSTs to endpoints that do not take uploads; bodies larger than memory_limit ending in 500 or 502; a burst of 500s from one IP followed by a slow 200 | [Blevene](../sources/gist-blevene-detection-guide/index.html) [Fastly](../sources/fastly-blog-php2shell/index.html) |
| **PHP error log** | 'Allowed memory size exhausted ... in Unknown on line 0' (an OOM outside any script, during request parsing); 'Failed to decode session object' | [Blevene](../sources/gist-blevene-detection-guide/index.html) |
| **Web server and kernel** | Clusters of Apache 'exit signal Segmentation fault (11)' or php-fpm segfaults in dmesg within minutes; nginx 'upstream prematurely closed connection' correlated with a prior fatal from the same IP | [Fastly](../sources/fastly-blog-php2shell/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) |
| **Process tree** | A mod_php or php-fpm worker spawning /bin/sh, curl, wget, or executing from memfd; with the known exploits no application code runs, so a shell from a worker is the exploit | [CISA](../sources/cisa-alert-php-20261021/index.html) [Fastly](../sources/fastly-blog-php2shell/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) |
| **Network** | New outbound connections from php-fpm or httpd workers to non-database endpoints | [Blevene](../sources/gist-blevene-detection-guide/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| **What the log cannot show** | nginx's default log format records neither Content-Type nor bodies, so shape-based attempts are invisible there; no standard log carries the worker id the cross-request bug needs; a clean log proves little | [darkfibr, GitHub](../sources/github-darkfibr-php2shell-detect/index.html) [rjmendez, GitHub](../sources/github-rjmendez-phpup-2026/index.html) [JPCERT/CC](../sources/jpcert-at260033/index.html) |

## How hard it is to exploit

The sources that temper the headline, and the one that says expect more.
- **The CVE vector.** Attack complexity high (AC:H) and attack requirements present (AT:P): the attacker must defeat a built-in protection and needs conditions beyond the request. [CVE record](../sources/cve-cve-2026-109618/index.html)
- **Fastly.** 'the existing PoCs require knowledge of the specific, running PHP binary and address space layout on the server for an attack to yield code execution on x86_64, so most deployments may be safe from RCE. Do not assume this holds true for you. If you operate a 32-bit PHP application, you should likely assume compromise.' [Fastly](../sources/fastly-blog-php2shell/index.html)
- **Imperva.** 'Triggering the bug is much easier than turning it into code execution.' A later request must reach the same worker and place carefully shaped data. Five demonstrated techniques, three via upload progress; a memory disclosure of about 67 KB. [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html)
- **rjmendez (detection author).** A lab reproduction of the leaked proof-of-concept's precondition produced a clean 200; 'VulnCheck independently reports that none of the public PoCs they reviewed have the correct mechanism'. [rjmendez, GitHub](../sources/github-rjmendez-phpup-2026/index.html)
- **Huntress.** Had not built or reproduced a proof of concept and was not aware of public exploit code as of 20:30 UTC on 21 October. [Huntress](../sources/huntress-php2shell-rapid-response/index.html)
- **Fastly, on the fix.** 'The PHP source tree calls the zend_bailout mechanism many places'; patching the demonstrated paths 'does not make the mechanism safe'. Expect more paths. [Fastly](../sources/fastly-blog-php2shell/index.html)

## So: can it be detected?

Yes, at two layers, and no at a third. **At the edge**, the known request shapes are distinctive and the vendors say their rules match them; the limit is variants and traffic that bypasses the edge. **On the host**, the strongest signal is the one that needs no signature: a PHP worker spawning a shell or a downloader when no application code ran. That is a process-tree rule, cheap to deploy, and the one the detection authors and CISA converge on. **In the default web log**, no: nginx's standard format records neither the content type nor the body, and the cross-request bug leaves no worker id anywhere a log would carry it. An organisation whose only telemetry is the access log cannot answer "were we hit" from it, which is the fact behind the agencies' advice to assess for backdoors rather than to look for a log line.


---
site v0.4.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/defence/index.html
