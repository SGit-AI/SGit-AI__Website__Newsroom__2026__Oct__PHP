# How everyone else is presenting the PHP flaws, and what this site should learn

Review for the editor, 22 October 2026, about 17:00 to 17:45 UTC. Written by the agent that builds php.oct.2026.newsroom.sgit.ai.

## What was looked at, and how

24 pages that cover the story, chosen to span the kinds of outlet a reader meets: general news (BBC live, CNN, Newsweek, The Next Web), security trade press (The Hacker News, SecurityWeek, Dark Reading, The Register, Help Net Security), the official sources (php.net, the PHP Foundation, CISA, NCSC UK, NCSC-NL), the researchers and their microsite (Wiz, Calif, php2shell.com), vendors (Cloudflare, Tenable, JFrog, SOCRadar, watchTowr), a community outage tracker found today (PHPocalypse Tracker), and the newsroom's own section.

Each was opened in a real Chromium at desktop (1366 x 900) and phone (390 x 844) size, the first screen and the full page screenshotted, and the page text kept. The appendix lists every page with its HTTP status and the SHA-256 of the desktop screenshot.

These are review screenshots, not evidence captures. They are held in the agent's session, not in the evidence vault, and are not republished (they are other people's pages). Anything below that this site does not yet carry as a fact needs a proper vault capture before it can become one.

## The short version

1. **On most of these pages, the first screen is not the story.** It is a cookie wall, an advert, a newsletter pop-up or a stock photo of code. Only php.net, CISA, the PHP Foundation, NCSC-NL, PHPocalypse and this site put the substance on the first screen at phone size.
2. **The 70% figure is still the headline.** CNN's headline says "affecting 70% of the internet", Wiz's says "70% of the Internet", the php2shell.com microsite animates a counter up to 70, and the BBC says PHP "helps run around 70% of sites". Nobody on this list says what it measures.
3. **The best "what is happening now" formats are not articles.** They are the BBC's summary box, NCSC-NL's README with two dated "last change" lines, Tenable's visible change log, and PHPocalypse's table of sites still dark and back up. All four are state, not story.
4. **Coverage is ahead of this site on facts, in five places.** Most important: memory disclosure, which most specialist write-ups lead with and this site does not mention; and Amazon's own blog saying php2shell is "broadly exploited in the wild", which is in our vault and understated on our front page. Details below.
5. **This site is ahead on what nobody else does.** Nobody else shows how far a claim can be trusted, what each number measures, how the agencies differ, a briefing per reader, or what changed between versions.

## What each kind of outlet does well, and badly

### General news

**BBC live page.** The best general-audience presentation on the list.
- Does well:
  - It opens with a **Summary** box of six bullets, each with a linked phrase into the live entries.
  - Each entry uses bold lead-ins in plain words: "Invisible, but essential", "When would you use it?", "What's gone wrong?".
  - It pairs the abstract with one concrete human consequence: a garage in Chepstow processing MOTs on pen and paper.
  - It offers short explainer videos ("PHP: the 'invisible infrastructure' of the internet").
  - It asks the reader directly: "How are you affected? What questions do you have? Get in touch".
- Does badly:
  - It carries "around 70% of sites" with no qualifier.
  - It says "90% of systems at risk are yet to [fix]" attributed only to "researchers".
  - Its sources are mostly links to its own pages.
  - The hero image is decorative code.
  - The live coverage ended at 17:12 UTC, so the page stopped being "now".

**CNN.** On a phone, a consent modal covers the whole first screen; the headline is "Websites shut down globally after AI finds cybersecurity flaw affecting 70% of the internet". It is a strong headline and an inaccurate one: it combines three claims, and the third has no stated measurement.

**The Next Web.** The best-balanced headline on the list: "Millions of PHP2Shell attempts so far, but officials see no break-in". It puts a number and a negative finding in one line, and the standfirst adds the concrete news (Japan's banks and airlines took services offline) and the timing (Amazon saw probing four days before disclosure). This is the register the front page should aim for.

**Newsweek.** The page title ("List of Websites Powered by PHP as Hacker Threat Prompts Scramble") differs from the on-page headline ("Critical PHP Flaws Threaten Millions of Websites in New AI Security Test"). The first is written for search, the second for readers. A privacy dialog and a video player take the first screen.

### Security trade press

- **The Hacker News.** "What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't" is the best framing of service journalism on the list: one question every operator has, answered both ways. The page around it is adverts.
- **SecurityWeek.** A full-screen conference advert covers the first screen on desktop and phone.
- **Dark Reading.** It is clean, but the first screen is a stock "WARNING" image and a cookie banner.
- **The Register.** Strong on the angle (the PHP Foundation blaming Chainguard). Its "read more" rail is the quickest way to see the newer developments: "PHP2Shell puts dozens of UK government services out of service" and "Hackers pile on PHP2Shell as AWS reveals attacks began before disclosure".
- **Help Net Security.** The headline leads with the action: "patched, update now!".

### The official sources

- **php.net.** Decision order is right: who is at risk, the two flaws, how to update, then what to do if you cannot. It is an archive page with a long list of years beside it, and the language is for engineers only.
- **CISA.** One paragraph says what, who, what to do, and a timestamped negative: CISA "has not observed exploitation of these vulnerabilities as of the time of publication". The time-stamped negative is the thing to copy.
- **NCSC UK.** On a phone, a cookie consent dialog covers the whole first screen.
- **NCSC-NL (GitHub).** The most useful operational page on the list.
  - The README opens with two separate dates: "Operational information last significant change" and "Software list last status update". Then it marks TLP:CLEAR.
  - Then come "Current status" and "Recommended actions", then a table of the latest software status updates.
  - Separating *last significant change* from *last update* is exactly the distinction the editor asked for in section versioning, and they show it in one line at the top.
- **PHP Foundation.** It opens by saying what the post is *not* about ("This post isn't about how to update"), which is a good courtesy to the reader who came for the fix.

### The researchers and their microsite

- **php2shell.com.** A branded microsite for the joint research:
  - a mascot (a pink elephant with a lightning bolt)
  - two calls to action: "Review upgrade guidance" and "Help me respond"
  - an animated counter that runs up to 70%
  - a grid of affected software
  - demonstration videos of pre-authentication remote code execution against WordPress, Drupal and Joomla

  Below the hero, the content is hidden until scroll animations run, so the full-page screenshot is blank. A reader without JavaScript, a printout or an agent gets the hero and nothing else. It frames the flaws as "arguably in software history" among the most severe.
- **Calif.** Scrollytelling, "A tale of two PHP remote vulnerabilities", told as a journey through time:
  - 2004, Stefan Esser's original memory-limit bug
  - 2020, a seemingly harmless bug report
  - 2024, the audit
  - July and August 2026, discovery
  - 21 October, the release

  It has a Pages/Panels toggle and "Covered by The Wall Street Journal and The New York Times" under the title. It is the most engaging telling of *how we got here* on the list.
- **Wiz.** The headline carries the 70%; the body says "70% of all websites". A table of contents and two buttons ("What you need to know", "Technical Threat Briefing") separate the two audiences. It is the only one that explicitly offers two depths.

### Vendors

- **Tenable.** A visible change log at the top ("Update October 21: Added Amazon Threat Intelligence's report..."), then key takeaways, then an FAQ. The change log is what a returning reader needs, and it is one line.
- **Cloudflare.** It says the flaws affect "all web servers running PHP 5.4 or later". It lists "What we know", "New rules" and "How to keep the protection enabled" as anchors in a sticky side menu.
- **JFrog.** The best single diagram on the list: "Two bugs. One big problem." It shows both CVEs side by side as a flow from request to remote code execution, each labelled with its bug class. A cookie dialog covers it on first load.
- **SOCRadar.** A sales banner ("Is your PHP version at risk? Check Free Now") is above the article. Dated "[Update]" lines inside the body.
- **watchTowr.** The page returned access denied (HTTP 403 in the page body) to an automated browser, as it did for the vault.

### The community tracker

**PHPocalypse Tracker** (allixsenos.github.io/phpocalypse-tracker) does one thing and does it better than anyone, including this site: which sites went dark and when they came back.
- It has two tables, "Still dark (2)" and "Back up (48)", and 50 sites against our impact ledger's 10.
- Every row gives the reported-dark time, the back-up time and the source.
- Every row also says *how* it was verified ("Confirmed by this tracker at 17:39 UTC in a manual browser check", "Automated checks are blocked").
- The top says "Last updated: 22 Oct, 15:41 UTC (2 h 2 min ago)".

That is row-level provenance plus state over time plus honest liveness, on one page.

## Where the coverage is ahead of this site

These are facts in other coverage that this site does not carry, or understates.

1. **Memory disclosure.** Wiz, php2shell.com and JFrog all say the flaws allow "Heartbleed-style memory disclosure": reading passwords, tokens, API keys and certificates from PHP process memory without first getting code execution. php2shell.com adds that this "can make the activity harder to detect". This site has no claim on it. The explainer, the flaws page and the front page all talk only about remote code execution. This is the most important gap: it changes the blast-radius question and the detection question.
2. **"Broadly exploited in the wild."** Amazon's own blog post (in the vault as `aws-security-blog-madpot`, captured 11:17 UTC) says php2shell "is now being broadly exploited in the wild", and Tenable repeats it.
   - Our front page says "Attackers are trying to use the flaws, in large numbers", and our fact `amazon-honeypot` is sourced to The Hacker News, not to Amazon's post.
   - We need a fact that quotes Amazon exactly, sourced to Amazon.
   - It also needs to say plainly what "exploited" means there: attempts in the wild, which is still not a confirmed compromise of a named organisation.
3. **New impact since the last capture.**
   - The UK: "32 government services were unavailable and four partially unavailable", said by a minister in the House of Lords, via the BBC.
   - Japan: Mizuho, Shizuoka Bank, airlines and Seven-Eleven Japan took services offline (The Next Web).
   - "90% of systems at risk" not yet fixed, from the BBC, attributed only to researchers.
   - Microsoft's chief executive: "not seen anything like this in a long, long time" (BBC).
4. **Affected versions back to 5.4.** Cloudflare and Wiz say PHP 5.4 and later. Our version table starts at 7.4, because that is where the backports start. The two are compatible but read as a contradiction unless said.
5. **Outage breadth.** PHPocalypse lists 50 sites with dark and back-up times; our impact ledger has 10 operators and no recovery times.

None of these is on the site yet. Each needs its source captured into the vault first, then a fact with a status. The editor's point from the afternoon holds: the site is only as current as its last capture, and its last capture is 11:34 UTC.

## What this site already does that nobody else does

- **A status word on every claim**, defined once (confirmed, reported, disputed, contradicted, unverified). Nobody else distinguishes "one party says" from "two primary sources agree".
- **The numbers, explained.** Every outlet carries a number; nobody says what it measures.
- **The agencies side by side.** Everyone quotes one agency; nobody shows that they disagree on taking systems offline.
- **A briefing per reader.** Wiz offers two depths; this site offers fifteen readers.
- **What changed, and when.** Tenable and SOCRadar have update lines; NCSC-NL has two dates. Only this site versions every section and every fact, with diffs.
- **No modal, no advert and no stock image on the first screen**, at either size.

## What to do, in order

1. **Capture the new sources into the vault now:**
   - the BBC live page as it stands at its close (17:12 UTC)
   - The Next Web
   - the three Register follow-ups
   - PHPocalypse Tracker
   - JFrog
   - php2shell.com
   - the Tenable FAQ with its change log

   This needs a session with the vault key.
2. **Add the missing facts, with exact wording:**
   - memory disclosure (Wiz, sourced to the Wiz post already in the vault)
   - Amazon's "broadly exploited in the wild", sourced to Amazon's own post, beside "no confirmed compromise"
   - the UK's 32 services
   - "affected from 5.4", reconciled with the version table
3. **Show "last significant change" separately from "last checked"** at the top of the front page and every briefing, the NCSC-NL way. The section ledger already knows the first; the vault knows the second.
4. **Add one line of change log under each section's version badge**, the Tenable way: "v4: added the Amazon post; status of exploitation changed". This can be generated from the ledger diff.
5. **Turn the impact ledger into a state tracker**, the PHPocalypse way: dark, back, with times and how each was verified, and a relative "updated 2 h ago". Credit PHPocalypse as a source and capture it rather than compete with it on breadth.
6. **Add a "Does this protect me?" matrix** to the playbook, The Hacker News's framing. Rows: patch, restart, WAF/CDN, settings, offline. Columns: blocks the remote code execution path, blocks the memory disclosure path, verified by.
7. **Make "how we got here" a richer view**, the Calif way: eras from 2004 to 2026, built from the timeline data, readable without JavaScript (php2shell.com is the warning).
8. **Add a human-impact strip to the front page**, the BBC way: one sourced line per real-world consequence (the garage on pen and paper, DigiD down, Japanese banks).
9. **Make the 70% a shareable card**: "What 70% means", one image, one sentence, one link, for journalists to paste. Nobody else has done it, and the error is everywhere.
10. **Ask readers**, the BBC way: "Were you affected? What do you want to know?" Every question becomes a candidate for the librarian's questions page.

## Appendix: the pages, as opened at about 17:20 to 17:45 UTC

| Page | HTTP | Title as served | URL | Desktop screenshot SHA-256 (first 16) |
|---|---|---|---|---|
| bbc-live | 200 | Scale of cyber-security flaw 'unprecedented' but no sign of breaches, says expert | https://www.bbc.co.uk/news/live/ckgel5xp2xv9t | 27847808dd32ba97 |
| cnn | 200 | Websites shut down globally after AI finds cybersecurity flaw affecting 70% of the internet | https://www.cnn.com/2026/10/21/tech/php2shell-vulnerability-ai-intl | f8629a1cc7517b62 |
| theregister | 200 | PHP blames supply chain security biz Chainguard for putting huge chunks of the web at risk | https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611 | b2cb5c891c8d08f8 |
| darkreading | 200 | 'PHP2Shell' Bugs Signal Red Alert for Security Industry | https://www.darkreading.com/application-security/php2shell-bugs-red-alert-security-industry | 1da5ebe69919e5b8 |
| thehackernews | 200 | PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't | https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html | 547e50ea93191c76 |
| securityweek | 200 | PHP2Shell: Mass Exploitation Looms for Leaked Critical PHP Flaws | https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/ | 678b9865d6f6f566 |
| newsweek | 200 | PHP Vulnerability: List of Websites Powered by PHP as Hacker Threat Prompts Scramble | https://www.newsweek.com/php-vunerability-php2shell-issue-websites-hack-server-12601225 | cd6a538fc9b57b69 |
| php-net | 200 | PHP: News Archive - 2026 | https://www.php.net/archive/2026.php#2026-10-21-5 | d1557e4815afd105 |
| php-foundation | 200 | Today's PHP Security Release, and How We're Strengthening PHP Security | https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/ | e42ba6e1be43f9c6 |
| cisa | 200 | Critical Vulnerabilities in PHP Require Immediate Patching | https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching | 2f65a83f1948e0a5 |
| ncsc-uk | 200 | Critical security issue affecting PHP | https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php | 1b2d6273692618f3 |
| ncsc-nl | 200 | NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities | https://github.com/NCSC-NL/php2shell | 8669f386d69bf2d5 |
| wiz | 200 | PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet | https://www.wiz.io/blog/php2shell-php-rce | 2308f80db05a7861 |
| calif | 200 | php2shell by Calif Research | https://calif.io/php2shell/ | 826a90f9419f3fca |
| php2shell-com | 200 | PHP2Shell: AI uncovers critical vulnerabilities in the backbone of the web | https://www.php2shell.com/ | e0c156c4112418fe |
| cloudflare | 200 | Cloudflare deploys protections against php2shell vulnerability | https://blog.cloudflare.com/php-vulnerabilities-waf-protection/ | 129738269ab60546 |
| tenable-faq | 200 | php2shell (CVE-2026-109618, CVE-2026-109619): Critical PHP RCE FAQ | https://www.tenable.com/blog/php2shell-cve-2026-109618-cve-2026-109619-frequently-asked-questions-about-critical-php-remote | 1b14d9ae9f12cb80 |
| watchtowr | 200, body says 403 | access denied to an automated browser | https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/ | f435af20ab8bcf0b |
| newsroom-sgit | 200 | The PHP flaws: AI found them, a leak forced them out, and the web went offline | https://newsroom.sgit.ai/php-flaws/index.html | 77b698b02710e1e1 |
| phpocalypse | 200 | PHPocalypse Tracker: PHP2Shell outages (CVE-2026-109618, CVE-2026-109619) | https://allixsenos.github.io/phpocalypse-tracker/ | 78556c4a5ec5cc85 |
| thenextweb | 200 | Millions of PHP2Shell attempts so far, but officials see no break-in | https://thenextweb.com/news/php2shell-millions-exploit-attempts-no-confirmed-breaches | 4d62d5c6fbabd7ad |
| helpnetsecurity | 200 | PHP2Shell: Critical PHP vulnerabilities patched, update now! | https://www.helpnetsecurity.com/2026/10/21/php2shell-php-vulnerabilities-patched-cve-2026-109618-cve-2026-109619/ | a4729833d3c5825f |
| jfrog | 200 | PHP2Shell: All You Need to Know About CVE-2026-109618 and CVE-2026-109619 | https://research.jfrog.com/post/php2shell-all-you-need-to-know-about-cve-2026-109618-and-cve-2026-109619/ | 77c3c75ae0f75692 |
| socradar | 200 | PHP2Shell CVE-2026-109618 & 109619: Affected Versions & Fix | https://socradar.io/blog/php2shell-cve-2026-109618-cve-2026-109619/ | 6fe2c411dc59bb36 |
