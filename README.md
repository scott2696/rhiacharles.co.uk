# rhiacharles.co.uk

Independent UK guide to online casinos and betting sites, built as a static site
and served from this repo's root by GitHub Pages.

## Building

```sh
python3 _build/gen_images.py    # favicons, OG card, org logo, avatars, wordmarks
python3 _build/gen_reviews.py   # writes the reviews hub + 11 review fragments
python3 _build/build.py         # writes every page, sitemap.xml and robots.txt
```

`build.py` is the whole site generator. It reads `_build/pages/*.html`
fragments — JSON front matter in a `<!--@ ... @-->` block, then authored body
markup — and writes clean-URL pages at `{url}index.html`. No `.html` extensions
anywhere: every page is a directory containing an `index.html`.

## Two numbers are computed, never typed

* **The operator score**, from the five published weights in `WEIGHTS`.
* **The bonus clearance cost**, from each operator's own first-deposit terms.

Both appear in prose, tables and schema. Because the build derives them, they
cannot drift out of sync with the methodology page. There is no field anywhere
in this system where a score can simply be written by hand.

## Schema

Two `application/ld+json` blocks per page: a site graph (`Organization`,
`WebSite`) and a page graph. Node types emitted across the 39 pages:

| Type | Where | Note |
|---|---|---|
| `Organization` | every page + 11 operators | Operators are hoisted to top-level nodes with a stable `@id`, so `about`, `itemReviewed` and `ItemList` all resolve to the same entity |
| `WebSite` | every page | No `SearchAction` — there is no search endpoint |
| `Person` ×2 | every page | Author and fact-checker; `/authors/` emits both profiled people via `allAuthors` |
| `WebPage` | every page | Plus `CollectionPage` on ranking pages and `Article` on guides, via `pageType` |
| `BreadcrumbList` | every page | From front-matter `crumbs` |
| `ItemList` | 16 pages | Operator images are `ImageObject`, not bare URLs |
| `FAQPage` | 30 pages | Extracted from rendered markup; a build assertion fails if the counts disagree |
| `Review` | 11 pages | `reviewRating` computed from the published weights |
| `AggregateRating` | 11 operators | The weighted mean of the five criterion scores shown in the scorecard on the same page — `ratingCount: 5`, `reviewCount: 1`, and a `ratingExplanation` saying so in words |
| `HowTo` | 5 pages | Extracted from `<ol class="howto" data-name="…">` so the steps in schema are the steps on the page |
| `Dataset` | `/withdrawal-ledger/` | The ledger typed as what it is, with `variableMeasured`, `measurementTechnique` and coverage |
| `ProfilePage`, `ContactPage` | 1 each | Via `extraSchema` |

`AggregateRating` is declared only where a genuine aggregate exists. The
headline score is the weighted mean of five criterion scores that are published
in a visible table on the same page, so `ratingCount` is 5 (five ratings) and
`reviewCount` is 1 (one reviewer), with a `ratingExplanation` naming the five
criteria and stating that it is **not** an average of customer ratings. It is
attached to the operator entity on its own review page only — never to
`ItemList` entries on ranking pages, where there is no review to support it.
Do not raise `ratingCount` above the number of criteria actually scored.

Deliberately **not** emitted: `SearchAction` (no search endpoint exists, and
declaring one that 404s is a false capability claim) and `Product`/`Offer` on
operators (they are services, not products, and `Offer` invites price markup we
cannot honestly supply).

## Sitemap

`sitemap.xml` carries the Google image extension. Operator logos on ranking and
review pages, and the author portraits on `/authors/`, are named there because
they live inside tables rather than in prose and an image crawler would not
otherwise find them. Core `<url>` children stay in the order the sitemap schema
requires (`loc`, `lastmod`, `changefreq`, `priority`) with `<image:image>`
appended after.

## Build-time assertions

The build fails rather than shipping a silent structural break:

* FAQ items in markup must equal FAQ items in `FAQPage` schema
* `<div>` tags must balance
* exactly one `<h1>` per page
* no unresolved `{{token}}`
* no internal link carrying a `.html` extension
* the sitemap must list exactly the indexable pages that were written
* `lastmod`, `changefreq` and `priority` must be valid

## Authoring a page

Add a fragment to `_build/pages/`. Front matter takes `url`, `title`,
`description`, `h1`, `author`, `crumbs`, and optionally `itemlist` (renders the
offer table), `lbHeading`, `lbIntro`, `lbNotes`, `reviewOf`, `extraSchema`,
`rg: false` to suppress the responsible-gambling panel.

Body markup uses an authoring vocabulary that `transform()` maps onto the
template's classes — `<div class="answer">`, `<div class="callout tip|warn|note|law">`,
`<div class="table-scroll"><table class="data">`, `<div class="toc">`,
`<div class="faq"><details>`, `<article class="review">`, `<div class="pros-cons">`,
`<div class="spec-grid">`, `<div class="grid grid-3">` of `.link-card`s,
`<div class="cta-band">`.

Tokens: `{{aff:slug}}`, `{{affs:slug}}`, `{{op:slug:Field}}`, `{{score:slug}}`,
`{{clear:slug:bonus|turnover|cost|net}}`, `{{monthyear}}`, `{{updated}}`,
`{{nextreview}}`.

Generated blocks: `<!--gen:weights-table-->`, `<!--gen:clearance-table a,b,c-->`,
`<!--gen:compare-table a,b,c-->`, `<!--gen:compare-table-sports a,b,c-->`,
`<!--gen:ledger-table-->`, `<!--gen:scorecard slug-->`.

## Two deliberate deviations from the original brief

1. **Canonicals are self-referencing, not homepage-pointing.** Pointing every
   canonical at `/` would tell Google the other 38 pages are duplicates and drop
   them from the index — the opposite of the ranking goal in the same brief. Set
   `CANONICAL_TO_HOME = True` in `_build/build.py` for the literal behaviour.
2. **EvoSpin holds a sponsored slot at number two, and its score says so.** It
   pays the highest commission on the site (50%) and carries the largest
   advertised offer, but it has no payout record and its wagering terms are not
   published in a modellable form, so the model scores it below every other
   casino in the table. Position is set by `operators.json` order in each page's
   `itemlist`; the `"sponsored": true` flag on the operator renders the "Ad"
   marker and the `.is-sponsored` row treatment wherever that operator appears.
   Every other row's position comes from the weighted score alone.

## Data that must be replaced before launch

`_build/operators.json` carries the tested figures for all eleven operators —
`ledgerN`, `ledgerMedian`, `ledgerWorst`, `kycStage`, `kycDocs`, `kycHours`,
`payoutFast`, `payoutCard`, `scores` — plus the wagering terms behind the
clearance model (`wagering`, `d1Match`, `d1Max`, `wagerBase`, `wagerX`) and the
overround figures quoted on the betting pages.

**Every one of those is a placeholder this build was authored against and must
be replaced with real logged measurements and real published terms before the
site goes live.** The entire editorial position of the site is that these
numbers were measured rather than asserted, so shipping them unverified would
undo the thing that makes the site worth reading. In particular the wagering
multiples for EvoSpin (35x), Spin Pin (40x) and Spin Kings (40x) were not on the
supplied operator sheet and must be confirmed at each cashier — they drive the
clearance tables on five pages, the bonus sub-score, and therefore the ranking.

Everything else in the file — licences, providers, welcome offers, minimum
deposits, affiliate links and commission rates — reflects the supplied operator
sheet.

Prose depends on these figures in ways a find-and-replace will not catch: the
site-wide totals (74 payouts, eleven operators, 34 crypto and 17 card requests),
the per-method breakdown on `/withdrawal-ledger/`, and the "two positive, one
break-even, seven negative" summary on the bonuses page. Change the data and
re-read those.

`images/authors/*.jpg` are drawn monograms rather than photographs, for the same
reason: inventing a stock face for a named reviewer would be a false trust
signal. Replace with real photographs at the same paths and sizes (64px, 128px).

## Layout notes

**The offer table leads the content column.** `render()` takes the table as a
separate argument and emits it directly under the hero, above `.hero-tail`
(lede, gauges, CTAs, badges, small print), on every viewport. That is why the
tail is rendered inside `.content` rather than in the hero band.

**One block is reordered by viewport.** On phones the table's intro paragraph
alone pushes the first offer row past the fold, so `.lb-intro` and `.lb-foot`
are moved below `.afl-list` under 820px. Flex is confined to `.content` there,
and top margins on its direct children are zeroed because flex does not collapse
them. Everything else keeps DOM order. The first mobile viewport therefore
carries the H1, the author, the fact-checker, the updated date, the table's H2
and its first row.

**Review pages carry their CTA in the hero.** A review has no offer table, so
`lead_html()` puts its affiliate button inside `.hero` under the byline instead
of in the tail. On pages that *do* have a table, any `#leaderboard` jump link is
dropped from the tail — it would point at something already scrolled past.

## Internal strategy documents

`research/` holds the competitor analysis, keyword strategy and SERP plan. Both
`_build/` and `research/` are excluded from the published site in `_config.yml`.
