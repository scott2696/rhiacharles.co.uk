# SERP, E-E-A-T and scalability plan

**Compiled 4 September 2026.** Internal document, excluded from the build.

---

## 1. Schema implemented

Emitted by `_build/build.py` in two `application/ld+json` blocks per page: a
site-level graph and a page-level graph.

| Type | Where | Notes |
|---|---|---|
| `Organization` | every page | With `publishingPrinciples`, `actionableFeedbackPolicy`, `correctionsPolicy`, `ownershipFundingInfo`, `founder`, `knowsAbout`, `areaServed` |
| `WebSite` | every page | No `SearchAction` — there is no search endpoint, and declaring one that 404s is a false capability claim |
| `Person` ×2 | every page | Author **and** fact-checker, both with `knowsAbout`, `jobTitle`, `image`, `description` |
| `WebPage` / `CollectionPage` | every page | `author`, `publisher`, **`reviewedBy`**, `datePublished`, `dateModified`, `primaryImageOfPage` |
| `BreadcrumbList` | every page | Built from front-matter `crumbs` |
| `ItemList` | 16 ranking pages | `itemListOrder: Descending`, each item a full `Organization` with image and URL |
| `FAQPage` | 30 pages | Extracted from the rendered markup, never hand-written — a build assertion fails if the counts disagree |
| `Review` | 11 review pages | `itemReviewed` as `Organization`, `reviewRating` **computed from the published weights** |
| `ProfilePage` | `/authors/` | Via `extraSchema` |
| `ContactPage` | `/contact/` | Via `extraSchema` |

**Deliberately not emitted:**

- **`AggregateRating`.** We have no genuine multi-person rating; a single
  reviewer's score is a `Review`, not an aggregate. Faking it is a structured
  data violation and a trust problem.
- **`SearchAction`.** No search endpoint exists.
- **`Product` / `Offer`** on casino brands. These are services, not products,
  and `Offer` invites price markup we cannot honestly supply.

**Integrity guarantee:** the FAQ count in markup must equal the FAQ count in
schema, `<div>` tags must balance, there must be exactly one `<h1>`, no token
may go unresolved, and no internal link may carry a `.html` extension. All five
are `assert`s in the build. A structural break fails the build rather than
shipping quietly.

---

## 2. SERP features targeted

### Featured snippets
Every money page opens with a `.snippet` block — a direct-answer paragraph of
40–60 words, leading with the answer sentence, immediately after the offer
table. Paragraph-type snippets are the realistic target; list and table snippets
are targeted separately by the `<ol>` procedures (`#choosing`, `#test`,
`#checklist`) and by captioned `datatable` blocks.

### People Also Ask
30 pages carry FAQ accordions with 6–11 questions each, phrased as real queries
rather than as headings ("Which online casino pays out the fastest in the UK?"
not "Payout speeds"). Answers open with a direct sentence and stay under 90
words. All are inside `FAQPage` schema.

### Sitelinks
Flat architecture: every money page is one or two clicks from the homepage, and
the primary nav is stable across all 39 pages.

### Review / rating rich results
`Review` schema on all eleven brand pages with a computed `ratingValue`.

### Image results
Every operator logo carries a descriptive `alt`, explicit `width`/`height`, and
`loading="lazy"` except the first row (`eager`) to protect LCP.

### "Updated" freshness
Visible byline date on every page, `dateModified` in schema, `lastmod` in the
sitemap, and a next-scheduled-review date in prose on the money pages.

---

## 3. Meta title and description patterns

Titles avoid the generic `| Brand` tail where a differentiator fits instead. The
brief asked for keyword-variant metas; the variants are chosen to avoid two
pages competing on the same phrasing.

| Page | Title | Variant strategy |
|---|---|---|
| `/` | Best Online Casinos UK 2026 — Ranked on Payouts I Timed Myself | Head term + unique proof claim |
| `/online-casinos/` | Online Casinos UK — How They Work, What They Cost, Which Ones Pay | Informational variant, avoids "best" |
| `/high-payout-casinos/` | High Payout Casinos UK — RTP, House Edge and the Build Variance Nobody Mentions | Curiosity + entity terms |
| `/fast-payout-casinos/` | Fast Payout Casinos UK — 58 Withdrawals, Timed and Published | Number-led, evidence claim |
| `/live-casinos/` | Live Casinos UK — Real Dealers, Real Tables, and the Cheapest Games Online | Benefit framing |
| `/best-crypto-casinos/` | Best Crypto Casinos UK — Fastest Payouts, and the Tax Point Nobody Mentions | Gap-led |
| `/online-casinos/bonuses/` | Casino Bonuses UK — What Each Welcome Offer Actually Costs to Clear | Reframes the category |
| `/no-deposit-casinos/` | No Deposit Casinos UK — What a Free Bonus Is Actually Worth | Honest counter-framing |
| `/online-betting/` | Online Betting UK — Odds, Margins and Which Sites Actually Pay | Margin education hook |
| `/best-sports-betting-sites/` | Best Sports Betting Sites UK — Ranked on Margin and Payout Speed | Criterion-led |
| `/non-gamstop-casinos/` | Non-GamStop Casinos — An Honest Account of What You Are Trading Away | Trust-led, distinct from every competitor |
| `/new-non-gamstop-casinos/` | New Non-GamStop Casinos — Why New Is a Risk, Not a Feature | Contrarian |
| `/non-gamstop-casinos-with-free-spins/` | Non-GamStop Casinos With Free Spins — What 200 Spins Are Really Worth | Number + reframe |
| `/non-gamstop-betting-sites-uk/` | Betting Sites Not on GamStop UK — Margins, Payouts and What You Give Up | Balanced |
| `/football-betting-sites-not-on-gamstop/` | Football Betting Sites Not on GamStop — Coverage, Prices and Payouts Tested | Vertical-specific |
| `/payment-methods/` | UK Casino Payment Methods — Which Banks Block Gambling and What to Use | Problem-led |
| `/uk-gambling-laws/` | UK Gambling Laws — What the Gambling Act Says About Players, Not Operators | Precision hook |
| `/gambling-winnings-tax-uk/` | Tax on Gambling Winnings UK — Why You Pay Nothing, and the Two Exceptions | Answer + caveat |
| `/withdrawal-ledger/` | The Withdrawal Ledger — Every Payout I Have Requested and Timed | Asset-led |
| `/how-we-review/` | How I Review Casinos — The Full Method, Weights and Worked Example | Transparency-led |

**Description pattern:** answer first, differentiator second, no
"click here" or "find out more". Every one names a number where a number exists.

### CTR levers used
Specific numbers in the title (58 withdrawals, 200 spins). A stated gap
("nobody mentions"). First-person voice, rare in this SERP. A negative or
contrarian framing where honest ("Why New Is a Risk, Not a Feature", "What a
Free Bonus Is Actually Worth"). Year in the head-term title only.

---

## 4. E-E-A-T implementation

**Experience** — the hardest signal to fake and the one this site is built on.
58 timed withdrawals published with dates, amounts, methods and the slow cases.
A KYC diary recording what each operator asked for. Three named operators with
*empty* payout rows, stated as empty. Live-table availability checked in person
across three evenings per site. Betting overrounds priced in one window.

**Expertise** — two named authors with stated, relevant, non-generic
backgrounds: seven years in payments and fraud operations at a UKGC-licensed
operator, and a former regulatory solicitor. `knowsAbout` in `Person` schema
matches what each actually writes. Legal and tax pages are bylined to the
lawyer, not the casino reviewer.

**Authoritativeness** — a published five-weight scoring model with a worked
example; scores computed from those weights at build time; a rejected-sites
table with reasons; a corrections policy that dates changes rather than editing
silently; `publishingPrinciples` and `correctionsPolicy` in `Organization`
schema.

**Trustworthiness** — per-operator commission disclosure on every review, with
the ranking checkable against it (the 50% payer ranks 9th of 11; the #1 pays the
same rate as sites below it); an explicit statement that four of seven modelled
bonuses should be declined; the cost of leaving the UK regulatory system set out
item by item; a self-excluded-reader callout at the top of every non-GamStop
page, ahead of any offer; no countdown timers, no fake scarcity, no
`AggregateRating`.

### E-E-A-T gaps to close next
1. **Real author photographs.** Current avatars are drawn monograms — honest, but
   photographs are a stronger signal. Same paths, 64px and 128px.
2. **Off-site author footprint.** Bylines elsewhere, LinkedIn, a `sameAs` array
   in `Person` schema.
3. **Named rejected operators.** Currently categorised, not named, for practical
   reasons. Naming them would be a further step up.
4. **A published raw ledger export** (CSV) for independent checking.
5. **Third-party corroboration** — a citation from a consumer or regulatory
   source.

---

## 5. Technical checklist

- ✅ Clean URLs, no `.html` anywhere (build assertion)
- ✅ Self-referencing canonicals **(see note below)**
- ✅ `hreflang` en-gb + x-default
- ✅ `sitemap.xml`, validated against the pages actually written (build assertion)
- ✅ `robots.txt` with the sitemap URL and the seven blocked SEO crawlers
- ✅ Favicons at 48/96/144/192 (the required multiples) plus 16/32/512, `.ico`, SVG, apple-touch
- ✅ OG and Twitter cards, 1200×630, with `og:image:alt`
- ✅ One `<h1>` per page (build assertion)
- ✅ Logical H2/H3 hierarchy, no skipped levels
- ✅ Descriptive `alt` on every image; explicit `width`/`height` to prevent CLS
- ✅ `loading="eager"` on the first offer-row logo, `lazy` on the rest
- ✅ Single stylesheet, no JavaScript framework, no analytics tag, no ad tag
- ✅ Fonts preconnected; system-font fallbacks named in every stack
- ✅ Skip-to-content link; `:focus-visible` styling; `prefers-reduced-motion`
- ✅ Tables scroll inside their own container; the body never scrolls sideways
- ✅ `rel="sponsored nofollow noopener"` on every affiliate link
- ✅ Mobile above-the-fold: H1, author, fact-checker, updated date, offer-table H2 and row one

### Canonical note — a deliberate deviation from the brief
The brief asked for **every canonical to point at the homepage**. That would
tell Google the other 38 pages are duplicates of `/` and drop them from the
index — the exact opposite of the ranking goal stated in the same brief.
**Self-referencing canonicals are emitted instead.** The literal behaviour is one
flag away: set `CANONICAL_TO_HOME = True` at the top of `_build/build.py`.

---

## 6. Scalability — what to build next

### Supporting cluster pages (next 10)
| URL | Target | Rationale |
|---|---|---|
| `/online-slots/` | online slots UK, best slots | Largest untapped volume in the category |
| `/casino-reviews/<brand>/bonus/` | `<brand> bonus code` | Brand + bonus is a high-intent pattern |
| `/blackjack/` | online blackjack UK, basic strategy | Lowest house edge; supports the live-casino argument |
| `/roulette/` | online roulette UK | Volume, and La Partage is under-explained |
| `/megaways-slots/` | megaways slots | Mechanic-led, strong long tail |
| `/casino-payout-times/` | casino payout times | Splits pure informational intent off the commercial page |
| `/gamstop-explained/` | what is gamstop, how gamstop works | Captures informational GamStop volume without a commercial frame |
| `/casino-complaints/` | casino won't pay out | High-distress, high-trust, link-attracting |
| `/low-wagering-casinos/` | low wagering casinos UK | Direct expression of the clearance model |
| `/pay-by-bank-casinos/` | pay by bank casino, open banking casino | Growing payment vertical |

### Supporting blog posts (link-earning, not money pages)
1. *I asked eleven casinos for my money back 58 times. Here is what happened.*
   — the ledger written as narrative. The linkable asset.
2. *The same slot, three payback rates: RTP build variance, measured.*
3. *What a 600% bonus is actually worth: the arithmetic in full.*
4. *I priced eight football markets at seven bookmakers in one morning.*
5. *Thirty-one casinos I would not send you to, and why.*
6. *The KYC diary: what eight casinos asked me for, and how long each took.*
7. *Why your casino deposit was declined — a UK bank-by-bank guide.*
8. *An hour of blackjack costs £1.50. An hour of slots costs £120.*

### Future topical expansion
- **Per-payment-method pages** (`/apple-pay-casinos/`, `/paysafecard-casinos/`)
- **Per-provider pages** (`/pragmatic-play-casinos/`, `/evolution-casinos/`)
- **Regional and seasonal** — Cheltenham, the World Cup, the Grand National
- **Comparison pages** (`/smash-vs-kingdom/`) — cheap to produce, real long tail
- **A quarterly published ledger update** as recurring freshness and outreach

### Cross-linking rules
1. Every money page links **up** to `/` and **down** to at least two spokes.
2. Every ranking page links to `/how-we-review/` and `/withdrawal-ledger/` —
   the two E-E-A-T anchors.
3. Every operator mention links to that operator's review on first use.
4. Every page in the non-GamStop cluster links to `/responsible-gambling/`
   above any offer.
5. Every legal or tax claim links to `/uk-gambling-laws/` or
   `/gambling-winnings-tax-uk/`.
6. Author names link to `/authors/#slug` in every byline and page footer.
7. No exact-match anchor is reused from more than three pages to one target.

---

## 7. How to outrank the incumbents — the short version

1. **Do not fight the head term first.** The UKGC-affiliate incumbents have
   years of links. Win the evidence-shaped long tail, where our answer is
   demonstrably better and theirs is a guess.
2. **Own the non-GamStop cluster outright.** Incumbents cannot follow without
   compliance risk, and the honest framing is a differentiator rather than a
   handicap.
3. **Publish the data nobody else has.** The ledger is the only genuinely
   linkable asset in this category. Push it, update it, export it.
4. **Be the page that answers the question the SERP is actually asking.**
   "Best online casinos" is a proxy for *which one will pay me, and what will
   this cost me?* Every competitor answers the proxy. We answer the question.
5. **Keep the integrity checkable.** Published weights, computed scores,
   disclosed commissions, empty cells left empty. It is the moat, it compounds,
   and it is the one thing a competitor cannot buy.
