# The PHP security flaws, explained from the start

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

No technical background assumed: what PHP is, what went wrong, why it is called php2shell, what the CVE numbers mean, why websites went offline, whether anyone was hacked, and what to do now.

Start here · ******Plain English

# The PHP security flaws, explained from the start

No technical background assumed. Seven short answers, in the order people usually ask them, each linking to the page with the evidence. Words in the dotted underline are explained when you hover or tap them.

What is PHP?What went wrong?Why php2shell?What are the numbers?Why did sites go offline?Was anyone hacked?What happens now?How to read this site

## 1. What is PHP, and is it on my computer?

PHP is a programming language for websites. When you open a page on a site built with it, a program on the website's server, written in PHP, puts the page together (your name, the latest posts, the basket) and sends the result to your browser. WordPress, which runs a very large number of blogs, shops and company sites, is written in PHP; so are Drupal, Joomla, Moodle, Magento and the software behind Wikipedia.

**PHP runs on servers, not on your phone or laptop.** This story is about the organisations that run websites. Visitors are affected only indirectly: if a site they use is broken into, or is taken offline as a precaution.

A normal visitYour browserasks for a page→The website's server, running PHPbuilds the page→Database and filesthe site's content and settings

## 2. What went wrong?

Two bugs were found deep inside PHP itself, not in any one website. Both are in how PHP cleans up after something goes wrong while it is handling a request.

An analogy. Think of PHP as the kitchen behind every page a website serves. When an order is impossible (it needs more than the kitchen is allowed to use), the cook abandons it. The flaws are in how the kitchen abandons and tidies up: in some cases it leaves the counter half cleared, and the next step, or the next order, uses what was left as if it were fresh. A customer who knows this can send an order designed to leave exactly the right things on the counter, so that the kitchen ends up following the customer's instructions instead of the menu.

The attackAnyone on the internetno account, no password→A crafted requestpushes PHP into its error path→The clean-up goes wrongleftover memory is trusted→The attacker's commands runon the server, as the website
What that can reach- the website's own code and settings
- passwords stored in those settings, such as the database's
- files the website can read or write
- other systems that trust this server
What it does not automatically reach- systems the server is not allowed to talk to
- passwords that were never on that server
- your own phone or computer

In the jargon, this is *unauthenticated remote code execution*: no login needed, from anywhere, and the attacker's code runs. It is the most serious kind of flaw there is, which is why the response was so loud. The researchers proved it end to end against the most traditional way of running PHP, inside the Apache web server, before any of the website's own code had run. That last point matters: **it does not matter how well a website is written**; if PHP underneath it is unpatched, it is in scope. [php.net](../sources/php-net-advisory/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

The technical version is on [the two flaws](../flaws/index.html), and the code itself on [the code](../code/index.html).

## 3. Why is it called php2shell?

Serious flaws get nicknames so people can talk about them: Heartbleed, Shellshock, Log4Shell. **php2shell** reads as *PHP to shell*. A shell is the command line an administrator types into; getting a shell on a server means being able to run commands on it. So the name is the whole attack in one word: start with a PHP website, end with a command line on its server. The US NSA wrote it PHP2Shell. [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) [Calif](../sources/calif-php2shell/index.html)

## 4. What are CVE-2026-109618 and CVE-2026-109619?

They are the official names. A CVE number is a serial number for a security flaw, so that vendors, governments and journalists know they mean the same bug: CVE, the year the number was reserved, and a sequence number. Each has a public record saying what is affected and how bad it is.

### CVE-2026-109618

PHP running out of memory mid-request can leave memory half set up, and the clean-up that follows can be steered by an attacker. Severity 9.2 out of 10.

### CVE-2026-109619

Leftover settings from one visitor's request can point at memory that has been released, and the next request on the same worker uses it. Severity 9.2 out of 10.

Both are fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October 2026. Older versions (8.1 and before) are past their support date and got no ready-made fix. [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) [php.net](../sources/php-net-advisory/index.html)

## 5. Why did governments tell people to take websites offline?

Because an unpatched website with this flaw can be taken over by anyone, and updating every server takes time. The US NSA and CISA said: if you cannot update, take the system offline until you can. The UK's NCSC put that fourth on its list, after updating and temporary fixes; several European agencies said isolate it; others did not mention it at all. Dutch government services, including the DigiD login many Dutch citizens use, were taken offline as a precaution. [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) [CISA](../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../sources/ncsc-news-php/index.html) [Rijksoverheid / NCSC-NL](../sources/rijksoverheid-ncsc-php-news/index.html)

Taking a site offline is a decision an organisation makes, not evidence it was attacked. The [agencies page](../agencies/index.html) sets the sixteen sets of advice side by side.

## 6. Was anyone actually hacked?

Not that anyone has confirmed, as of the latest evidence this site holds. Attackers have certainly been trying: Cloudflare says it saw millions of attempts across its network, and Amazon says a decoy server was hit four days before the fix was public. But an attempt is not a success, no named organisation has said it was broken into, and the US list of flaws known to be exploited did not include either of these when last checked. That can change quickly, and this site will say so when the evidence does. [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) [THN](../sources/thehackernews-php2shell-4days/index.html) [CISA](../sources/cisa-kev-json/index.html)

The details: [who went offline and who was compromised](../impact/index.html), and [every sign of exploitation, in order](../exploitation/index.html).

## 7. What happens now?

- **If you only use websites:** nothing to do. Ignore messages that tell you to install anything because of this; that is a scam pattern.

- **If you own a website:** ask whoever hosts it whether PHP has been updated and restarted. [The website owner's briefing](../briefings/site-owner/index.html) has the exact question to send.

- **If you run systems:** update, restart, verify, and look for signs of compromise. [The step-by-step list](../playbook/index.html) has every agency's advice in order.

- **If you decide or communicate:** [pick your briefing](../start/index.html).

## How to read this site

Every statement on this site carries one of five words, so you can tell a fact from a rumour at a glance:

- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

Every one of those statements links to the pages it comes from, and every one of those pages was saved, dated and fingerprinted when it was read, so that it can be checked later even if the original changes. [How that works](../method/index.html).


---
site v0.15.13 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/explained/index.html
