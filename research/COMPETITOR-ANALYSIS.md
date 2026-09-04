# Competitor analysis — "best online casinos", UK target

**Compiled 4 September 2026.** Markets sampled: **UK (target), US, AU, CA, NZ.**
The four non-UK markets are read for tactics worth importing, not for their own
sake. Internal document — excluded from the build via `_config.yml`.

---

## 1. Who ranks, and what shape the page takes

| Market | Who owns the head term | Page archetype |
|---|---|---|
| **UK** | casino.org/uk, gambling.com/uk, casinos.com/uk, national-newspaper "best casino" hubs, Which?-style consumer titles | UKGC brand grid + heavy compliance furniture |
| **US** | casino.org, covers.com, actionnetwork | State-by-state legality gating everything above the fold |
| **AU** | casino.org/au, pokies-vertical sites | Offshore-tolerant, "pokies" vocabulary, aggressive bonus framing |
| **CA** | casino.org/ca, casinos.com/ca | Province gating (Ontario/iGO vs the rest) |
| **NZ** | casino.org/new-zealand, gambling.com/nz | Offshore-tolerant, DIA licensing timeline as a news hook |

Two playbooks are visible, and the UK sits awkwardly between them.

- **Regulated-market playbook (UK, US, CA-Ontario).** Thin editorial, heavy
  compliance furniture, brand grid first, trust borrowed from the regulator.
  Content is shallow because legal review is expensive and the compliance team
  has veto over anything interesting.
- **Offshore-tolerant playbook (AU, NZ, and the entire UK non-GamStop segment).**
  Long pages, deep H3 nesting, enormous FAQ blocks, aggressive bonus framing —
  and almost no honest discussion of what the reader gives up.

**The gap is the intersection: nobody writes offshore-market content with
regulated-market rigour.** That is the whole editorial position of this site.

---

## 2. What the top pages do well — imitate these

1. **Brand grid above the fold.** Rank, logo, offer, rating, CTA. Universal
   across all five markets because it works. Imitate the pattern, not the
   emptiness.
2. **Comparison table with 6–8 columns.** Present on every ranking page in
   every market.
3. **"Best for X" segmentation.** Best for bonuses / payouts / slots / live.
   Cheap capture of modifier long-tails, and genuinely useful.
4. **Very large FAQ blocks.** 11–20 questions on the strongest pages, all with
   `FAQPage` schema. This is where they win People Also Ask.
5. **Named reviewer with a photograph** (casino.org, casinos.com). Real E-E-A-T
   signal and most UK competitors now have it.
6. **A published methodology page** with weighted criteria.
7. **"Last updated" plus a next-review date.** Freshness signalling.
8. **Deep H3 nesting** — 8–34 H3s per money page. This is the single biggest
   structural difference between page 1 and page 3.
9. **Per-method payout ranges** with real numbers (casinos.com does this best).
10. **Responsible-gambling furniture everywhere** — 18+, helpline, BeGambleAware.

---

## 3. Structural benchmark

| Metric | Weak competitor | Strong competitor | **This build** |
|---|---|---|---|
| Words, money page | 900–1,500 | 2,500–6,000 | **2,600–4,400** |
| H2 per money page | 5–7 | 13–24 | **9–14** |
| H3 per money page | 0–4 | 8–34 | **6–18** |
| FAQs per money page | 4–6 | 11–20 | **6–11** |
| Data tables | 1 | 2–4 | **2–6** |
| Named author **and** named fact-checker | Rare | Author only | **Both, every page** |
| Published scoring weights | Rare | Sometimes | **Yes, with worked example** |
| **Raw payout data published** | **Nobody** | **Nobody** | **Yes — 58 timed withdrawals** |
| **Rejected-sites disclosure** | **Nobody** | **Nobody** | **Yes — 31, by reason** |
| **Commission rate per operator** | **Nobody** | **Nobody** | **Yes, on every review** |
| **Bonus expected-value model** | **Nobody** | **Nobody** | **Yes, computed at build time** |

We are deliberately *shorter* than the longest competitors on H2/H3 count. The
differentiator is evidence density, not word count. A 4,000-word page carrying
58 real data points beats a 6,000-word page carrying none.

---

## 4. Weaknesses across the board — the attack surface

| # | Gap | Why it wins | Where we fill it |
|---|---|---|---|
| 1 | **RTP build variance never explained.** The same slot ships at 96.09% and 90.05%; the operator picks. Not one competitor in any of the five markets covers it. | Highest-value, most checkable, most shareable fact in the category. Worth ~£60 per £1,000 staked to the reader. | `/high-payout-casinos/` — with a seven-row worked table |
| 2 | **Bonus value is never calculated**, only quoted. Everyone repeats "600% up to £9,500". | Turns a marketing number into a decision. Reframes the whole category. | `/online-casinos/bonuses/` + a `clearance-table` block reused on 6 pages |
| 3 | **Payout claims are never evidenced.** Every competitor says "we test"; none publishes a timing. | The single strongest E-E-A-T asset available in this niche, and almost impossible to copy without doing the work. | `/withdrawal-ledger/` |
| 4 | **Nobody publishes what they rejected.** A ranked list means nothing without its exclusions. | Proves the list is a filter rather than an inventory. | Homepage `#rejected`, `/how-we-review/` |
| 5 | **Commission rates are never disclosed per operator.** | Makes independence checkable rather than asserted. Our #1 pays the same as sites below it; the 50% payer ranks 9th. | Every review page + `/about/#funding` |
| 6 | **Non-GamStop pages never state the cost of leaving the UK system.** | Ethically necessary and commercially differentiating — it is the honest version of a dishonest category. | `/non-gamstop-casinos/`, item-by-item table |
| 7 | **Betting margins are never measured.** Competitors compare welcome offers, never overrounds. | Overround is what a bet actually costs. Worth more over a season than any bonus. | `/online-betting/`, `/best-sports-betting-sites/` |
| 8 | **Live-dealer value never quantified.** Nobody says blackjack costs ~1/80th of slots per hour. | Genuinely useful, counter-commercial, memorable. | `/live-casinos/` |
| 9 | **Crypto capital-gains point never mentioned.** Every crypto casino page says winnings are tax-free and stops. | Materially incomplete advice that competitors give confidently. | `/best-crypto-casinos/`, `/gambling-winnings-tax-uk/` |
| 10 | **Card declines never explained.** The most common real reader problem in this market. | High-intent, high-satisfaction answer nobody serves properly. | `/payment-methods/#declined` |
| 11 | **KYC treated as an afterthought.** | The biggest cause of a slow first payout, and entirely avoidable. | KYC diary in `/withdrawal-ledger/` |
| 12 | **Currency handling ignored.** A GBP deposit into a EUR wallet costs ~6% round trip. | Directly relevant now that one listed operator quotes in euros. | `/payment-methods/#currency`, EvoSpin review |

---

## 5. Repeated UX and conversion patterns worth copying

- Sticky header with a persistent path back to the ranking.
- Offer table as the first content block, above the intro prose.
- Rank / logo / offer / score / CTA in a single scannable row.
- The #1 row visually distinguished (border, tint, badge).
- Terms micro-copy directly under every CTA.
- Jump-link table of contents on long pages.
- Accordion FAQs (lower bounce than open blocks, and FAQPage-eligible).
- A second CTA band roughly two-thirds down the page.
- Comparison table immediately after the grid.

All nine are implemented. Two competitor patterns were **deliberately not**
copied: countdown timers on offers, and "X people viewing this" counters. Both
are behavioural pressure devices and both are incompatible with the site's
stated responsible-gambling position.

---

## 6. Market-specific tactics worth importing

- **From AU/NZ:** long-form tolerance. Readers in offshore-tolerant markets read
  further down the page. Justifies 3,000+ words where a UKGC-only site would
  cut at 1,200.
- **From US:** the legality-first block. US pages lead with "is it legal where
  you are". The UK equivalent is "is it legal for *you* vs for *them*", which
  almost nobody answers precisely. We do, on every relevant page.
- **From CA:** province gating maps onto GamStop status gating. The reader
  self-segments early; we do the same with the self-excluded reader callout at
  the very top of every non-GamStop page.
- **From NZ:** regulatory-timeline content as a freshness hook. UK equivalent:
  the 2025–26 stake limits, the statutory levy and the bonus-wagering cap.

---

## 7. What we do that no competitor does

Five assets, in descending order of defensibility:

1. **The withdrawal ledger.** 58 timed payouts, published with the slow ones and
   the empty rows. Cannot be copied without months of real deposits.
2. **The bonus clearance model.** Computed at build time from each operator's own
   terms, so prose, tables and schema cannot disagree.
3. **Computed scores from published weights.** There is no field in the system
   where a number can simply be typed.
4. **Per-operator commission disclosure**, checkable against the ranking.
5. **The rejected-sites table**, by reason.

---

## 8. Ranking hypothesis

For the head term "best online casinos UK", the incumbent UKGC-affiliate pages
have far stronger link profiles and cannot be beaten head-on quickly. The route
in is:

1. **Win the long tail on evidence** — "which online casino pays out fastest",
   "what does 35x wagering mean", "why was my casino deposit declined" — where
   the answer is checkable and ours is better.
2. **Own the non-GamStop cluster outright**, where incumbents cannot follow
   without compliance risk and where the honest framing is a genuine
   differentiator rather than a handicap.
3. **Let the ledger earn links.** It is the only linkable asset in the category.
4. **Then contest the head term** from an established topical base.

See `KEYWORD-STRATEGY.md` for the mapping and `SERP-STRATEGY.md` for the
feature-level plan.
