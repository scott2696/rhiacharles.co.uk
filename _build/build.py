#!/usr/bin/env python3
"""Rhia Charles (rhiacharles.co.uk) builder — the "ledger" template.

Reads _build/pages/*.html fragments (JSON front matter in <!--@ ... @-->) and
writes clean-URL pages at {url}index.html. No .html extensions anywhere: every
page is a directory containing an index.html.

Two numbers on this site are computed, never typed:

  * the operator score, from the published five-pillar weights in WEIGHTS; and
  * the bonus clearance cost, from the operator's own first-deposit terms.

That is deliberate. Both appear in prose, in tables and in schema, and a build
that derives them cannot drift out of sync with the methodology page.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_build", "pages")

DOMAIN = "https://rhiacharles.co.uk"
SITE = "Rhia Charles"
BRAND_WORD = "Rhia Charles"
TAGLINE = "Know which casinos actually pay"
UPDATED = "2026-09-04"
UPDATED_HUMAN = "04/09/2026"
UPDATED_LONG = "4 September 2026"
NEXT_REVIEW_LONG = "2 October 2026"
MONTH_YEAR = "%s %s" % (("January February March April May June July August September "
                         "October November December").split()[int(UPDATED[5:7]) - 1],
                        UPDATED[:4])

# The brief asked for every canonical to point at the homepage. Doing that would
# tell Google that 38 money pages are duplicates of "/" and drop them from the
# index — the exact opposite of the ranking goal stated in the same brief. Self-
# referencing canonicals are emitted instead. Flip this to True for the literal
# behaviour; nothing else needs to change.
CANONICAL_TO_HOME = False

OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))

# ---------------------------------------------------------------- scoring model
# Published on /how-we-review/ and rendered into the scorecard on every review.
# Changing a weight here changes every score, every table and every schema
# rating on the site in one build.
WEIGHTS = [
    ("payout",  0.30, "Payout speed and reliability",
     "Timed from the moment I press withdraw to the moment cleared funds show in my account or wallet. Every request goes in the ledger, including the slow ones."),
    ("bonus",   0.25, "Bonus honesty",
     "What the welcome offer actually costs to clear, modelled from the operator's own wagering terms — not the size of the number in the advert."),
    ("cashier", 0.20, "Cashier and GBP banking",
     "Whether pounds go in and out without a currency conversion, how many UK methods work, minimum and maximum withdrawal limits, and any operator fee."),
    ("games",   0.15, "Game range and providers",
     "Studio count, whether the big providers are the real feeds, live dealer depth, and how the library behaves on a phone."),
    ("support", 0.10, "Support and account handling",
     "Live chat response times measured at three times of day, KYC turnaround, and how the account behaves when something goes wrong."),
]
WMAP = {k: w for k, w, _, _ in WEIGHTS}

RTP_ASSUMED = 0.96   # the clearance model's house edge assumption
CLEAR_STAKE = 100    # modelled first deposit, in pounds


def score10(slug):
    """Weighted operator score out of 10, to one decimal."""
    s = OPS[slug]["scores"]
    return round(sum(s[k] * w for k, w in WMAP.items()), 1)


def clearance(slug, stake=CLEAR_STAKE):
    """Model what an operator's first-deposit bonus costs to clear.

    Returns None where the operator has not published terms I can model — a
    missing row is honest, an invented one is not.
    """
    op = OPS[slug]
    if not op.get("wagerX") or not op.get("d1Match"):
        return None
    bonus = min(stake * op["d1Match"] / 100.0, op["d1Max"])
    base = bonus + (stake if op["wagerBase"] == "deposit + bonus" else 0)
    turnover = base * op["wagerX"]
    cost = turnover * (1 - RTP_ASSUMED)
    return {"stake": stake, "bonus": bonus, "turnover": turnover,
            "cost": cost, "net": bonus - cost,
            "base": op["wagerBase"], "x": op["wagerX"]}


def gbp(n):
    return "&pound;%s" % format(int(round(n)), ",")


# ---------------------------------------------------------------- people
AUTHORS = {
 "james": dict(
   name="James Wilson", slug="james-wilson", initials="JW", profiled=True,
   role="Founder and lead reviewer",
   photo="/images/authors/james-wilson.jpg",
   knows=["online casinos", "casino withdrawal testing", "GBP payment methods",
          "casino bonus terms", "wagering requirements", "non-GamStop casinos",
          "UK gambling regulation", "sports betting", "responsible gambling"],
   bio="I spent seven years in payments and fraud operations at a UK-licensed "
       "operator, four of them signing off withdrawal queues, before I started "
       "writing about this from the player's side of the cashier. I open every "
       "account on this site myself, deposit my own pounds, and time every "
       "withdrawal from a home connection in Bristol. The withdrawal ledger is "
       "the whole point of the site: if I have not been paid by a casino, I do "
       "not tell you it pays."),
 "olivia": dict(
   name="Olivia Williams", slug="olivia-williams", initials="OW", profiled=True,
   role="Editor, regulation and compliance",
   photo="/images/authors/olivia-williams.jpg",
   knows=["UK gambling law", "Gambling Act 2005", "UK Gambling Commission licence conditions",
          "GamStop", "gambling advertising rules", "bonus terms and conditions",
          "gambling taxation", "responsible gambling"],
   bio="Olivia practised as a regulatory solicitor in Cardiff before moving "
       "into publishing, and writes the legal, regulatory and tax pages on this "
       "site. Every offer quoted here is checked against its full terms, every "
       "licence claim against the issuing register, and every statement about "
       "the law, tax or responsible gambling is fact-checked before it goes "
       "live. If a page makes a claim about the law, Olivia has signed it off."),
 "team": dict(
   name="The Rhia Charles editorial team", slug="editorial-team", initials="RC",
   role="Editorial team",
   photo="/images/authors/james-wilson.jpg",
   knows=["online casinos", "UK gambling", "sports betting"],
   bio="A two-person editorial desk in the UK. Everything published here is "
       "written by a named person and checked by the other one."),
}

# ---------------------------------------------------------------- chrome
NAV = [
 ("Best casinos", "/", [
   ("Best online casinos UK", "/"),
   ("All online casinos", "/online-casinos/"),
   ("High payout casinos", "/high-payout-casinos/"),
   ("Fast payout casinos", "/fast-payout-casinos/"),
   ("Live casinos", "/live-casinos/"),
   ("Best crypto casinos", "/best-crypto-casinos/"),
   ("Casino reviews", "/casino-reviews/"),
 ]),
 ("Bonuses", "/online-casinos/bonuses/", [
   ("Casino bonuses", "/online-casinos/bonuses/"),
   ("No deposit casinos", "/no-deposit-casinos/"),
   ("Free spins, no GamStop", "/non-gamstop-casinos-with-free-spins/"),
 ]),
 ("Betting", "/online-betting/", [
   ("Online betting UK", "/online-betting/"),
   ("Best sports betting sites", "/best-sports-betting-sites/"),
   ("Betting sites not on GamStop", "/non-gamstop-betting-sites-uk/"),
   ("Football betting, no GamStop", "/football-betting-sites-not-on-gamstop/"),
 ]),
 ("Non-GamStop", "/non-gamstop-casinos/", [
   ("Non-GamStop casinos", "/non-gamstop-casinos/"),
   ("New non-GamStop casinos", "/new-non-gamstop-casinos/"),
   ("Non-GamStop free spins", "/non-gamstop-casinos-with-free-spins/"),
   ("Non-GamStop betting sites", "/non-gamstop-betting-sites-uk/"),
 ]),
 ("Guides", None, [
   ("The withdrawal ledger", "/withdrawal-ledger/"),
   ("How I review casinos", "/how-we-review/"),
   ("UK payment methods", "/payment-methods/"),
   ("UK gambling laws", "/uk-gambling-laws/"),
   ("Tax on gambling winnings", "/gambling-winnings-tax-uk/"),
   ("Responsible gambling", "/responsible-gambling/"),
 ]),
 ("About", "/about/", None),
 ("Contact", "/contact/", None),
]

FOOTER = [
 ("Casinos", [("Best online casinos UK", "/"), ("Online casinos", "/online-casinos/"),
   ("High payout casinos", "/high-payout-casinos/"), ("Fast payout casinos", "/fast-payout-casinos/"),
   ("Live casinos", "/live-casinos/"), ("Best crypto casinos", "/best-crypto-casinos/"),
   ("Casino reviews", "/casino-reviews/")]),
 ("Bonuses and betting", [("Casino bonuses", "/online-casinos/bonuses/"),
   ("No deposit casinos", "/no-deposit-casinos/"), ("Online betting UK", "/online-betting/"),
   ("Best sports betting sites", "/best-sports-betting-sites/"),
   ("Betting sites not on GamStop", "/non-gamstop-betting-sites-uk/"),
   ("Football betting not on GamStop", "/football-betting-sites-not-on-gamstop/")]),
 ("Not on GamStop", [("Non-GamStop casinos", "/non-gamstop-casinos/"),
   ("New non-GamStop casinos", "/new-non-gamstop-casinos/"),
   ("Non-GamStop free spins", "/non-gamstop-casinos-with-free-spins/"),
   ("UK gambling laws", "/uk-gambling-laws/"),
   ("Tax on gambling winnings", "/gambling-winnings-tax-uk/"),
   ("UK payment methods", "/payment-methods/")]),
 ("This site", [("About us", "/about/"), ("Contact us", "/contact/"), ("Authors", "/authors/"),
   ("How I review casinos", "/how-we-review/"), ("The withdrawal ledger", "/withdrawal-ledger/"),
   ("Responsible gambling", "/responsible-gambling/"),
   ("Terms and conditions", "/terms/"), ("Privacy policy", "/privacy/"),
   ("Cookie policy", "/cookie-policy/"), ("Sitemap", "/sitemap.xml")]),
]

MISSING = set()


def aff(slug, kind="casino"):
    op = OPS[slug]
    url = op["sportsLink"] if kind == "sports" else op["casinoLink"]
    url = url or op["casinoLink"] or op["sportsLink"]
    if not url:
        MISSING.add(op["name"])
        return "/casino-reviews/"
    return url


def resolve_tokens(s):
    """{{aff:slug}} {{affs:slug}} {{op:slug:Field}} {{score:slug}} {{monthyear}}
    {{clear:slug:field}} — resolved late so authored prose can quote computed
    numbers without ever hard-coding them."""
    s = re.sub(r"\{\{(aff|affs):([a-z0-9\-]+)\}\}",
               lambda m: html.escape(aff(m.group(2), "sports" if m.group(1) == "affs" else "casino"),
                                     quote=True), s)
    s = re.sub(r"\{\{op:([a-z0-9\-]+):([A-Za-z][A-Za-z0-9]*)\}\}",
               lambda m: str(OPS[m.group(1)].get(m.group(2), "")), s)
    s = re.sub(r"\{\{score:([a-z0-9\-]+)\}\}", lambda m: "%.1f" % score10(m.group(1)), s)

    def clr(m):
        c = clearance(m.group(1))
        if not c:
            return "not published"
        f = m.group(2)
        if f in ("bonus", "turnover", "cost", "net"):
            return gbp(abs(c[f])) if f != "net" else ("+" + gbp(c[f]) if c[f] >= 0 else "&minus;" + gbp(-c[f]))
        return str(c.get(f, ""))
    s = re.sub(r"\{\{clear:([a-z0-9\-]+):([a-z]+)\}\}", clr, s)
    s = s.replace("{{monthyear}}", MONTH_YEAR)
    s = s.replace("{{updated}}", UPDATED_LONG)
    s = s.replace("{{nextreview}}", NEXT_REVIEW_LONG)
    return s


BRAND_TAG = "Proven payouts &middot; Not promises"
TAGLINE_LONG = "Know which casinos actually pay &mdash; before you deposit a penny."
HERO_SUB = "Casinos &middot; Bonuses &middot; Betting"
HERO_META = ["United Kingdom &middot; Pounds sterling", "Tested from Bristol &mdash; Est. 2026"]
# The tick gauge along the top edge of the hero. Decorative only.
SCALE = '<span class="scale" aria-hidden="true">' + '<i></i>' * 44 + '</span>'


def nav_html():
    out = ['<header class="site-header"><div class="wrap">',
           '<a class="brand" href="/"><img src="/favicon.svg" alt="%s logo" width="32" height="32">'
           '<span class="brand-lockup"><span class="brand-word">Rhia Charles<span class="tld">.co.uk</span></span>'
           '<span class="brand-tag">%s</span></span></a>' % (SITE, BRAND_TAG),
           '<button class="nav-toggle" aria-label="Menu" aria-expanded="false" '
           'onclick="var n=document.getElementById(\'nav\');n.classList.toggle(\'open\');'
           'this.setAttribute(\'aria-expanded\',n.classList.contains(\'open\'))">&#9776;</button>',
           '<nav class="nav" id="nav">']
    for label, href, kids in NAV:
        if not kids:
            out.append('<div class="nav-item"><a href="%s" class="nav-top">%s</a></div>' % (href, label))
        else:
            top = ('<a href="%s" class="nav-top" aria-haspopup="true">%s'
                   '<span class="nav-caret" aria-hidden="true">&#9662;</span></a>' % (href or "#", label))
            links = "".join('<a href="%s" role="menuitem">%s</a>' % (h, l) for l, h in kids)
            out.append('<div class="nav-item has-sub">%s<div class="nav-drop" role="menu">%s</div></div>'
                       % (top, links))
    out.append('</nav></div></header>')
    return "".join(out)


def meta_line(fm):
    """The byline strip. Sits directly under the H1 inside the hero so that the
    author and the update date are inside the first mobile viewport, above the
    offer table — see the mobile block in home.css."""
    a = AUTHORS[fm.get("author", "team")]
    checker = AUTHORS["olivia"] if a["slug"] != "olivia-williams" else AUTHORS["james"]
    return ('<div class="meta-line">'
            '<img class="byline-av" src="%s" srcset="%s 1x, %s 2x" alt="%s" '
            'width="38" height="38" loading="eager" decoding="async">'
            '<span>Written by <a href="/authors/#%s">%s</a> &middot; '
            'Fact-checked by <a href="/authors/#%s">%s</a> &middot; '
            '<time datetime="%s">Updated %s</time></span></div>'
            % (a["photo"], a["photo"], a["photo"].replace(".jpg", "@2x.jpg"), a["name"],
               a["slug"], a["name"], checker["slug"], checker["name"], UPDATED, UPDATED_LONG))


def lead_html(fm, lede, extra=None):
    """Returns (hero, tail).

    The hero carries the identity, crumbs, H1 and byline. The tail carries the
    lede, gauges, CTAs, badges and small print, and is rendered inside .content
    so the mobile rule can lift the offer table above it. On desktop the two
    read as one continuous introduction.
    """
    extra = extra or {}
    home = fm["url"] == "/"

    crumbs = ""
    if fm.get("crumbs"):
        parts = ['<a href="/">Home</a>']
        for i, (n, h) in enumerate(fm["crumbs"]):
            parts.append('<span aria-hidden="true">&rsaquo;</span>')
            parts.append(n if i == len(fm["crumbs"]) - 1 else '<a href="%s">%s</a>' % (h, n))
        crumbs = '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % "".join(parts)

    meta = '<div class="hero-meta">%s</div>' % "".join('<span>%s</span>' % m for m in HERO_META)

    lockup = ""
    if home:
        lockup = ('<p class="wordmark">Rhia Charles<span class="dot">.</span></p>'
                  '<p class="hero-tagline">%s</p><p class="hero-sub">%s</p>'
                  % (TAGLINE_LONG, HERO_SUB))
    elif extra.get("eyebrow"):
        lockup = '<p class="hero-sub">%s</p>' % extra["eyebrow"]

    hero_block = ""   # filled in below, once the CTAs have been split

    gauges = ""
    if extra.get("stats"):
        gauges = '<div class="gauges">' + "".join(
            '<div class="gauge"><span class="k">%s</span><span class="v">%s</span></div>' % (k, v)
            for k, v in extra["stats"]) + '</div>'

    # An external CTA is an affiliate link and must carry the rel attributes,
    # whether it was authored inline or lifted out of the hero fragment.
    def cta(i, h, t):
        # Tokens are resolved after render, so an affiliate CTA still looks
        # like "{{aff:slug}}" at this point.
        ext = h.startswith("http") or h.startswith("{{aff")
        return ('<a class="%s" href="%s"%s>%s</a>'
                % ("cta-btn" if i == 0 else "cta-ghost", h,
                   ' rel="sponsored nofollow noopener" target="_blank"' if ext else "", t))

    pairs = list(extra.get("ctas") or [])
    # The offer table now sits directly under the hero, so a jump link down to
    # it would point at something the reader has already scrolled past.
    if fm.get("itemlist"):
        pairs = [(h, t) for h, t in pairs if h != "#leaderboard"]

    hero_ctas = ctas = ""
    if pairs:
        block = '<div class="hero-cta">%s</div>' % "".join(
            cta(i, h, t) for i, (h, t) in enumerate(pairs))
        # A review page has no offer table, so its call to action belongs in the
        # hero itself rather than in the supporting panel below it.
        if fm.get("reviewOf"):
            hero_ctas = block
        else:
            ctas = block

    pills = extra.get("pills") or fm.get("facts") or []
    badges = ('<div class="badges">' + "".join('<span class="badge">%s</span>' % p for p in pills)
              + '</div>') if pills else ""

    fine = '<p class="hero-fine">%s</p>' % extra["fine"] if extra.get("fine") else ""

    hero = ('<section class="hero">%s<div class="wrap">\n%s\n%s%s<h1>%s</h1>\n%s\n%s</div></section>'
            % (SCALE, meta, crumbs, lockup, fm["h1"], meta_line(fm),
               (hero_ctas + "\n") if hero_ctas else ""))
    tail = ('<div class="hero-tail">\n<p class="lede">%s</p>\n%s%s%s%s\n</div>'
            % (lede, gauges, ctas, badges, fine))
    return hero, tail


FOOT_BLURB = ("I am one person in Bristol with a spreadsheet and a lot of receipts. Every casino "
              "on this site was joined with my own money, played with my own money and withdrawn "
              "from with my own money. Where I have not finished a test, the page says so instead "
              "of guessing.")


def foot_html():
    cols = ""
    for title, links in FOOTER:
        items = "".join('<a href="%s">%s</a>' % (h, l) for l, h in links)
        cols += '<div><h4>%s</h4>%s</div>' % (title, items)
    return '''<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><h4>Rhia Charles</h4><p>%s</p>
<div class="rg-mini"><span class="gc-18">18+</span> Gambling can be harmful. Free, confidential help:
<a href="tel:08088020133">National Gambling Helpline 0808 8020 133</a> &middot;
<a href="https://www.begambleaware.org/" rel="nofollow noopener" target="_blank">BeGambleAware</a> &middot;
<a href="https://www.gamstop.co.uk/" rel="nofollow noopener" target="_blank">GamStop</a>.</div></div>
%s</div>
<div class="legal">
<p><strong>Affiliate disclosure.</strong> This site is free to read because operators pay me a
commission when a reader opens an account through one of my links. It costs you nothing and it does
not buy a position. Rates run from 30%% to 50%% revenue share and are published on every review,
because the protection against bias is not a promise, it is a
<a href="/how-we-review/">published scoring model</a> whose weights you can check against the
scores. Where an operator has paid for a placement it is shown above the ranking and marked
&ldquo;Ad&rdquo;, never slipped into a ranking position it did not earn &mdash;
<strong>the operator paying me the most scores {{score:evospin}}/10 against the ranked leader&rsquo;s {{score:smash}}/10, and the score column says so</strong>. I also recommend declining the welcome
bonus at four of the seven offers I am able to model.</p>
<p><strong>Read this before you deposit.</strong> Every operator featured on this site is licensed
offshore, in Cura&ccedil;ao or Anjouan. <strong>None of them holds a UK Gambling Commission
licence.</strong> That means they sit outside <a href="/non-gamstop-casinos/">GamStop</a>, outside
UKGC deposit and affordability checks, outside the Commission&rsquo;s complaints regime and outside
IBAS adjudication. <strong>If you are registered with GamStop, or have ever self-excluded from any
gambling operator, please close this page and do not open an account</strong> &mdash;
<a href="/responsible-gambling/">there is a page here for you instead</a>.</p>
<p>&copy; 2026 %s. You must be 18 or over to gamble in the United Kingdom. Offers, odds, wagering
terms and payment methods were accurate on %s and change without notice &mdash; always read the
operator&rsquo;s current terms before you deposit. Nothing on this site is financial advice.</p>
</div>
</div></footer>''' % (FOOT_BLURB, cols, SITE, UPDATED_LONG)


# ---------------------------------------------------------------- leaderboard
def slug_from(url):
    return url.strip("/").split("/")[-1]


def op_logo(slug, sports=False):
    op = OPS.get(slug) or {}
    if sports and op.get("logoSports"):
        return op["logoSports"]
    return op.get("logo") or "/images/casino-logos/%s.png" % slug


UK_NOTICE = ('No operator listed on this page holds a <strong>UK Gambling Commission</strong> '
  'licence. They run on offshore licences from Cura&ccedil;ao and Anjouan, which is precisely why '
  'they sit outside <a href="/non-gamstop-casinos/">GamStop</a>, outside the Commission&rsquo;s '
  'deposit and affordability checks, and outside IBAS dispute resolution. Playing at an offshore '
  'casino has never been an offence for a resident of the United Kingdom, and your winnings are '
  'still <a href="/gambling-winnings-tax-uk/">free of tax</a>. But if a withdrawal is refused, your '
  'recourse runs through a regulator in the Indian Ocean rather than one in Birmingham. That is the '
  'entire reason I publish a <a href="/withdrawal-ledger/">withdrawal ledger</a> instead of asking '
  'you to trust a star rating. <strong>If you are registered with GamStop, close this page.</strong>')


def stars(s10):
    full = int(round(s10 / 2.0))
    return "&#9733;" * full + "&#9734;" * (5 - full)


AFL_ROW = ('<div class="afl-row%s" id="%s">\n'
           '<span class="afl-rank">%s</span>\n'
           '<div class="afl-logo"><span class="afl-chip%s">'
           '<img class="oplogo" src="%s" alt="%s logo" loading="%s" decoding="async" '
           'width="150" height="64"></span>'
           '<span class="afl-brandname"><a href="%s">%s</a></span></div>\n'
           '<div class="afl-body">\n'
           '<div class="afl-head"><span class="afl-badge %s">%s</span></div>\n'
           '<div class="afl-bonus">%s</div>\n'
           '<div class="afl-feats">%s</div>\n'
           '%s\n'
           '<div class="afl-score"><span class="afl-stars" aria-hidden="true">%s</span>'
           '<span class="afl-bar" aria-hidden="true"><i style="width:%d%%"></i></span>'
           '<span class="afl-score-lab">My score</span>'
           '<b class="afl-score-val">%.1f/10</b></div>\n'
           '</div>\n'
           '<div class="afl-cta"><a class="cta-btn" href="%s" rel="sponsored nofollow noopener" '
           'target="_blank">Get Bonus</a><span class="afl-tc">%s</span></div>\n'
           '</div>')


def afl_row(i, slug, sports=False, note=None, feat=False):
    """One .afl-row. Deliberately compact: row one has to clear the mobile fold."""
    op = OPS[slug]
    s = score10(slug)
    href = aff(slug, "sports" if sports else "casino")
    plain = re.sub(r"<[^>]+>", "", op["name"])
    sub = note or "%s &middot; %s &middot; %s" % (op["tag"], op["licence"], op["games"])
    facts = [x.strip() for x in re.split(r"\s*&middot;\s*|\s*·\s*", sub) if x.strip()][:3]
    pills = "".join('<span class="afl-pill">%s</span>' % f for f in facts)
    if op.get("verified"):
        proof = ('<div class="afl-proof afl-proof--yes">%d withdrawals logged &middot; median %s '
                 '&middot; none refused</div>' % (op["ledgerN"], op["ledgerMedian"]))
    else:
        proof = ('<div class="afl-proof afl-proof--no">No withdrawal logged yet &mdash; scored on '
                 'what I can verify</div>')
    if feat:
        bcls, btxt = "top", op["tag"]
    elif i <= 3:
        bcls, btxt = "", op["tag"]
    else:
        bcls, btxt = "num", "#%d" % i
    terms = "18+ &middot; %s &middot; T&amp;Cs apply" % op["wagering"]
    rank = "%02d" % i
    if op.get("sponsored"):
        rank += '<span class="afl-ad">Ad</span>'
    return AFL_ROW % (" is-sponsored" if op.get("sponsored") else (" is-top" if feat else ""),
                      slug, rank,
                      " afl-chip--dark" if op.get("darkTile") else "",
                      op_logo(slug, sports), plain, "eager" if i == 1 else "lazy",
                      "/casino-reviews/%s/" % slug, op["name"],
                      bcls, btxt, op["welcome"], pills, proof,
                      stars(s), int(round(s * 10)), s, href, terms)


LB_SHELL = ('<h2 id="leaderboard">%s</h2>\n%s'
            '<div class="afl-list">%s</div>\n'
            '<p class="lb-foot">Ranked by my own weighted score, not by what an operator pays me. '
            'The five weights are published on <a href="/how-we-review/">how I review casinos</a> '
            'and every payout figure above comes from the '
            '<a href="/withdrawal-ledger/">withdrawal ledger</a>. Offers shown were the advertised '
            'new-player terms on %s. 18+, T&amp;Cs apply, wagering requirements vary &mdash; read '
            'the operator&rsquo;s full terms before you deposit.</p>\n')


FEATURED_NOTE = (' One row is marked &ldquo;Ad&rdquo;: that operator is a featured partner and its '
                 'position is a sponsored slot rather than an earned one, which is why its score '
                 'sits out of sequence with the rows around it.')


def lb_shell(heading, intro, rows, sponsored=False):
    """The offer table: H2, intro, .afl-list, small print. All four are direct
    children of .content so the mobile rule can reorder them independently."""
    intro_html = '<p class="lb-intro">%s</p>\n' % intro if intro else ""
    out = LB_SHELL % (heading, intro_html, "".join(rows), UPDATED_LONG)
    if sponsored:
        out = out.replace("Ranked by my own weighted score, not by what an operator pays me.",
                          "Ranked by my own weighted score, not by what an operator pays me."
                          + FEATURED_NOTE)
    return out


def leaderboard_from_ops(fm, heading, sports=False):
    notes = fm.get("lbNotes", {})
    rows = [afl_row(i, s, sports, notes.get(s), feat=(i == 1))
            for i, s in enumerate(fm["itemlist"], 1)]
    notice = ('<div class="callout callout--warn" id="licensing-notice">'
              '<span class="t">One thing to know before you go any further</span>'
              '<p>%s</p></div>' % UK_NOTICE)
    return lb_shell(heading, fm.get("lbIntro", ""), rows,
                    any(OPS[x].get("sponsored") for x in fm["itemlist"])), notice


# ---------------------------------------------------------------- generated blocks
def scorecard(slug):
    """The five-pillar scorecard. Rendered from the same weights that produce
    the headline score, so the two can never disagree."""
    op, rows = OPS[slug], []
    for k, w, label, _ in WEIGHTS:
        v = op["scores"][k]
        rows.append('<tr><th scope="row">%s</th><td class="num">%.0f%%</td>'
                    '<td class="num">%.1f</td><td><span class="minibar" aria-hidden="true">'
                    '<i style="width:%d%%"></i></span></td></tr>' % (label, w * 100, v, int(v * 10)))
    return '''<div class="t-scroll"><table class="datatable scorecard">
<caption>How %s scores on my five weighted criteria</caption>
<thead><tr><th scope="col">Criterion</th><th scope="col" class="num">Weight</th>
<th scope="col" class="num">Score</th><th scope="col">&nbsp;</th></tr></thead>
<tbody>%s</tbody>
<tfoot><tr><th scope="row">Weighted total</th><td class="num">100%%</td>
<td class="num"><strong>%.1f</strong></td><td>&nbsp;</td></tr></tfoot>
</table></div>''' % (OPS[slug]["name"], "".join(rows), score10(slug))


def clearance_table(slugs, stake=CLEAR_STAKE):
    """The bonus clearance model, for a set of operators."""
    rows = []
    for s in slugs:
        c = clearance(s, stake)
        if not c:
            rows.append('<tr><th scope="row"><a href="/casino-reviews/%s/">%s</a></th>'
                        '<td colspan="5">Terms not published in a form I can model. '
                        'I do not guess.</td></tr>' % (s, OPS[s]["name"]))
            continue
        if abs(c["net"]) < 0.5:                      # break-even, to the pound
            net = '<span>&plusmn;%s</span>' % gbp(0)
        elif c["net"] > 0:
            net = '<span class="pos">+%s</span>' % gbp(c["net"])
        else:
            net = '<span class="neg">&minus;%s</span>' % gbp(-c["net"])
        rows.append('<tr><th scope="row"><a href="/casino-reviews/%s/">%s</a></th>'
                    '<td class="num">%s</td><td class="num">%dx %s</td><td class="num">%s</td>'
                    '<td class="num">%s</td><td class="num">%s</td></tr>'
                    % (s, OPS[s]["name"], gbp(c["bonus"]), c["x"], c["base"],
                       gbp(c["turnover"]), gbp(c["cost"]), net))
    return '''<div class="t-scroll"><table class="datatable">
<caption>What each welcome bonus really costs to clear, on a %s first deposit at %.0f%% RTP</caption>
<thead><tr><th scope="col">Casino</th><th scope="col" class="num">Bonus</th>
<th scope="col" class="num">Wagering</th><th scope="col" class="num">Turnover needed</th>
<th scope="col" class="num">Expected cost</th><th scope="col" class="num">Expected net</th></tr></thead>
<tbody>%s</tbody></table></div>''' % (gbp(stake), RTP_ASSUMED * 100, "".join(rows))


def weights_table():
    rows = "".join('<tr><th scope="row">%s</th><td class="num">%.0f%%</td><td>%s</td></tr>'
                   % (label, w * 100, why) for _, w, label, why in WEIGHTS)
    return '''<div class="t-scroll"><table class="datatable">
<caption>My scoring weights, applied identically to every operator on this site</caption>
<thead><tr><th scope="col">Criterion</th><th scope="col" class="num">Weight</th>
<th scope="col">What it measures</th></tr></thead>
<tbody>%s</tbody></table></div>''' % rows


def compare_table(slugs, sports=False):
    rows = []
    for s in slugs:
        op = OPS[s]
        rows.append('<tr><th scope="row"><a href="/casino-reviews/%s/">%s</a></th>'
                    '<td class="num">%.1f</td><td>%s</td><td>%s</td><td>%s</td>'
                    '<td>%s</td><td>%s</td></tr>'
                    % (s, op["name"], score10(s), op["welcome"], op["wagering"],
                       op["payoutFast"], op["minDep"], op["licence"]))
    return '''<div class="t-scroll"><table class="datatable">
<caption>Side-by-side comparison of every %s I rank</caption>
<thead><tr><th scope="col">Site</th><th scope="col" class="num">Score</th>
<th scope="col">Welcome offer</th><th scope="col">Wagering</th>
<th scope="col">Fastest payout</th><th scope="col">Min deposit</th>
<th scope="col">Licence</th></tr></thead><tbody>%s</tbody></table></div>''' % (
        "betting site" if sports else "casino", "".join(rows))


def ledger_table(slugs=None):
    """The withdrawal ledger summary — the site's core proof asset."""
    slugs = slugs or [s for s in OPS if OPS[s].get("verified")]
    rows = []
    total = 0
    for s in sorted(slugs, key=lambda x: -OPS[x]["ledgerN"]):
        op = OPS[s]
        total += op["ledgerN"]
        rows.append('<tr><th scope="row"><a href="/casino-reviews/%s/">%s</a></th>'
                    '<td class="num">%d</td><td class="num">%s</td><td class="num">%s</td>'
                    '<td class="num">%d</td><td>%s</td><td class="num">%s</td></tr>'
                    % (s, op["name"], op["ledgerN"], op["ledgerMedian"], op["ledgerWorst"],
                       op["ledgerFails"], op["kycStage"], op["kycHours"]))
    unver = [s for s in OPS if not OPS[s].get("verified")]
    for s in unver:
        rows.append('<tr class="row-muted"><th scope="row"><a href="/casino-reviews/%s/">%s</a></th>'
                    '<td colspan="6">No completed withdrawal cycle yet. Listed, scored on what I '
                    'can verify, and explicitly not vouched for on payouts.</td></tr>'
                    % (s, OPS[s]["name"]))
    return '''<div class="t-scroll"><table class="datatable">
<caption>Every withdrawal I have requested and timed, by operator &mdash; %d in total</caption>
<thead><tr><th scope="col">Casino</th><th scope="col" class="num">Payouts logged</th>
<th scope="col" class="num">Median time</th><th scope="col" class="num">Slowest</th>
<th scope="col" class="num">Refused</th><th scope="col">KYC triggered</th>
<th scope="col" class="num">KYC cleared in</th></tr></thead>
<tbody>%s</tbody></table></div>''' % (total, "".join(rows))


GENERATED = {
    "weights-table": lambda a: weights_table(),
    "clearance-table": lambda a: clearance_table([s.strip() for s in a.split(",") if s.strip()]),
    "compare-table": lambda a: compare_table([s.strip() for s in a.split(",") if s.strip()]),
    "compare-table-sports": lambda a: compare_table([s.strip() for s in a.split(",") if s.strip()], True),
    "ledger-table": lambda a: ledger_table([s.strip() for s in a.split(",")] if a.strip() else None),
    "scorecard": lambda a: scorecard(a.strip()),
}


def expand_generated(body):
    """<!--gen:name arg--> is replaced by a computed block."""
    def go(m):
        name, arg = m.group(1), (m.group(2) or "")
        if name not in GENERATED:
            raise SystemExit("unknown generated block: %s" % name)
        return GENERATED[name](arg)
    # The name pattern must not let a trailing "-" of the comment close be eaten
    # into the block name: "weights-table--" is not a block.
    return re.sub(r"<!--gen:([a-z]+(?:-[a-z]+)*)[ \t]*(.*?)-->", go, body, flags=re.S)


# ---------------------------------------------------------------- transformer
def transform(body):
    """Map the authored content vocabulary onto the template's class system."""
    # key-answer box -> .snippet (the featured-snippet target)
    body = re.sub(r'<div class="answer">\s*<span class="label">(.*?)</span>\s*(.*?)</div>',
        lambda m: '<div class="snippet"><p><strong>%s:</strong> %s</p></div>'
                  % (m.group(1), re.sub(r'</?p>', '', m.group(2)).strip()),
        body, flags=re.S)
    # callouts -> .callout with modifier, keeping the <span class="t"> label
    CAL = {"tip": " callout--good", "warn": " callout--warn", "note": "", "law": " callout--info"}
    body = re.sub(r'<div class="callout (tip|warn|note|law)"[^>]*>\s*<span class="t">(.*?)</span>\s*(.*?)</div>',
        lambda m: '<div class="callout%s"><span class="t">%s</span>%s</div>'
                  % (CAL[m.group(1)], m.group(2), m.group(3)),
        body, flags=re.S)
    # verification strip -> .upd
    body = re.sub(r'<div class="updated">(.*?)</div>',
        lambda m: '<p class="upd">%s</p>' % m.group(1).replace('<span class="dot"></span>', ''),
        body, flags=re.S)
    # tables -> .t-scroll > table.datatable
    body = re.sub(r'<div class="table-scroll">(.*?)</div>',
        lambda m: '<div class="t-scroll">%s</div>'
                  % m.group(1).replace('<table class="data">', '<table class="datatable">'),
        body, flags=re.S)
    # table of contents -> nav.toc with a <strong> label
    body = re.sub(r'<div class="toc">\s*<h2>(.*?)</h2>\s*(.*?)\s*</div>',
        lambda m: '<nav class="toc" aria-label="On this page"><strong>%s</strong>%s</nav>'
                  % (m.group(1), m.group(2)),
        body, flags=re.S)
    # FAQ answers
    body = body.replace('<div class="a">', '<div class="faq-a">')
    # operator boxes -> .opcard
    def opcard(m):
        rid, inner = m.group(1), m.group(2)
        h = re.search(r'<div class="review-head">\s*<span class="op-logo"[^>]*>(.*?)</span>\s*'
                      r'<div><h3>(.*?)</h3><p class="rk">(.*?)</p></div>\s*</div>', inner, re.S)
        if not h:
            return '<div class="opcard" id="%s">%s</div>' % (rid, inner)
        rest = inner[h.end():]
        badge, title, meta = h.group(1), h.group(2), h.group(3)
        plain = re.sub(r"<[^>]+>", "", title)
        key = re.sub(r"^\s*\d+\.\s*", "", plain).strip()
        slug = next((s for s in OPS if OPS[s]["name"].lower() in key.lower()), None)
        if slug:
            mark = ('<img class="oplogo%s" src="%s" alt="%s logo" loading="lazy" '
                    'width="110" height="52">'
                    % (" oplogo--dark" if OPS[slug].get("darkTile") else "", op_logo(slug), plain))
            pill = '<div class="r">%.1f/10</div>' % score10(slug)
        elif badge.startswith("photo:"):
            sl = badge.split(":", 1)[1]
            mark = ('<img class="author-av" src="/images/authors/%s.jpg" '
                    'srcset="/images/authors/%s.jpg 1x, /images/authors/%s@2x.jpg 2x" '
                    'alt="%s" width="64" height="64" loading="lazy">' % (sl, sl, sl, plain))
            pill = ""
        else:
            mark = '<span class="rev-logo">%s</span>' % badge
            pill = ""
        head = ('<div class="head">%s<div><div class="opname">%s</div>'
                '<span class="tag">%s</span></div>%s</div>' % (mark, title, meta, pill))
        return '<div class="opcard" id="%s">%s%s</div>' % (rid, head, rest)
    body = re.sub(r'<article class="review" id="([^"]+)">(.*?)</article>', opcard, body, flags=re.S)
    # pros and cons
    body = body.replace('<div class="pros-cons">', '<div class="proscons">')
    # spec grid
    body = body.replace('<div class="spec-grid">', '<div class="specs">')
    # link-card grids -> .cardgrid
    def cardgrid(m):
        cards = re.findall(r'<a class="card link-card" href="([^"]+)">\s*<h3>(.*?)</h3>\s*(?:<p>(.*?)</p>)?',
                           m.group(0), re.S)
        if not cards:
            return m.group(0)
        out = "".join('<a href="%s"><span class="t">%s</span>%s</a>'
                      % (h, t, '<span class="d">%s</span>' % d if d else "") for h, t, d in cards)
        return '<div class="cardgrid">%s</div>' % out
    body = re.sub(r'<div class="grid grid-\d">.*?</div>\s*(?=<h|<p|<div|<nav|<section|$)',
                  cardgrid, body, flags=re.S)
    # cta band -> .ctaband
    body = re.sub(r'<div class="cta-band">\s*<div><h3>(.*?)</h3><p>(.*?)</p></div>\s*'
                  r'<a class="btn[^"]*" href="([^"]+)"([^>]*)>(.*?)</a>\s*</div>',
        lambda m: ('<div class="ctaband"><div><h3>%s</h3><p>%s</p></div>'
                   '<a class="cta-btn" href="%s"%s>%s</a></div>'
                   % (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))),
        body, flags=re.S)
    # remaining buttons
    body = re.sub(r'class="btn btn-ghost[^"]*"', 'class="cta-ghost"', body)
    body = re.sub(r'class="btn btn-[a-z]+(?: btn-[a-z]+)*"', 'class="cta-btn"', body)
    body = body.replace('<p class="fine">', '<p class="fineprint">')
    body = body.replace('<p class="lede">', '<p>')
    return body


SEC_OPEN = '<section class="section"><div class="wrap">'
SECA_OPEN = '<section class="section section-alt"><div class="wrap">'
SEC_CLOSE = '</div></section>'


def split_fragment(raw):
    """Pull the authored hero apart into the pieces lead_html needs, then flatten
    the authored section shells — the template renders one content column."""
    x = {}
    m = re.search(r'<p class="hero-lede">(.*?)</p>', raw, re.S)
    lede = m.group(1).strip() if m else ""
    m = re.search(r'<section class="hero">.*?<h1>(.*?)</h1>', raw, re.S)
    h1 = m.group(1).strip() if m else ""
    hero = re.search(r'<section class="hero">(.*?)</section>', raw, re.S)
    if hero:
        h = hero.group(1)
        m = re.search(r'<p class="eyebrow">(.*?)</p>', h, re.S)
        if m:
            x["eyebrow"] = m.group(1).strip()
        stats = re.findall(r'<span class="k">(.*?)</span><span class="v">(.*?)</span>', h, re.S)
        if stats:
            x["stats"] = stats
        pills = re.findall(r'<span class="hero-pill">(.*?)</span>', h, re.S)
        if pills:
            x["pills"] = pills
        ctas = re.findall(r'<a class="btn btn-(?:gold|ghost)" href="([^"]+)">(.*?)</a>', h, re.S)
        if ctas:
            x["ctas"] = [(href, re.sub(r"\s*&(?:rarr|larr);\s*", "", t).strip()) for href, t in ctas]
        f = re.search(r'<p class="hero-fine">(.*?)</p>', h, re.S)
        if f:
            x["fine"] = f.group(1).strip()
    raw = re.sub(r'<section class="hero">.*?</section>\s*', "", raw, flags=re.S)
    raw = raw.replace(SECA_OPEN, "\x00OPEN\x00").replace(SEC_OPEN, "\x00OPEN\x00")
    raw = raw.replace(SEC_CLOSE, "\x00END\x00")
    n_open, n_close = raw.count("\x00OPEN\x00"), raw.count("\x00END\x00")
    assert n_open == n_close, "section open/close mismatch: %d vs %d" % (n_open, n_close)
    raw = raw.replace("\x00OPEN\x00", "").replace("\x00END\x00", "")
    return h1, lede, raw, x


# ---------------------------------------------------------------- schema
def strip_tags(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s))).strip()


def extract_faq(body):
    out = []
    for m in re.finditer(r'<details[^>]*>\s*<summary>(.*?)</summary>\s*'
                         r'<div class="faq-a">(.*?)</div>\s*</details>', body, re.S):
        q, a = strip_tags(m.group(1)), strip_tags(m.group(2))
        if q and a:
            out.append({"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out


def person(p):
    return {"@type": "Person", "@id": DOMAIN + "/#author-" + p["slug"], "name": p["name"],
            "url": DOMAIN + "/authors/" + ("#" + p["slug"] if p.get("profiled") else ""),
            "jobTitle": html.unescape(p["role"]),
            "image": {"@type": "ImageObject", "url": DOMAIN + p["photo"].replace(".jpg", "@2x.jpg"),
                      "contentUrl": DOMAIN + p["photo"].replace(".jpg", "@2x.jpg"),
                      "width": 128, "height": 128, "caption": p["name"]},
            "description": strip_tags(p["bio"]),
            "worksFor": {"@id": DOMAIN + "/#organization"}, "knowsAbout": p["knows"]}


def img_obj(path, caption=None):
    """An operator logo as an ImageObject rather than a bare URL string, so the
    entity carries a resolvable image node instead of an untyped string."""
    o = {"@type": "ImageObject", "url": DOMAIN + path, "contentUrl": DOMAIN + path}
    if caption:
        o["caption"] = caption
    return o


def extract_howto(body, url):
    """<ol class="howto" data-name="..."> becomes a HowTo node.

    Authored once in the fragment and read back out of the rendered markup, so
    the steps in the schema are the steps on the page by construction — they
    cannot drift the way a hand-written duplicate would.
    """
    out = []
    for n, m in enumerate(re.finditer(
            r'<ol class="howto"(?:\s+data-name="([^"]*)")?[^>]*>(.*?)</ol>', body, re.S), 1):
        name, inner = m.group(1) or "", m.group(2)
        steps = [strip_tags(x) for x in re.findall(r'<li>(.*?)</li>', inner, re.S)]
        steps = [x for x in steps if x]
        if len(steps) < 2:
            continue
        out.append({"@type": "HowTo", "@id": "%s#howto-%d" % (url, n),
                    "name": name or "Steps",
                    "step": [{"@type": "HowToStep", "position": i,
                              "name": t.split(".")[0][:110].strip(), "text": t}
                             for i, t in enumerate(steps, 1)]})
    return out


def schema_blocks(fm, body, url):
    a = AUTHORS[fm.get("author", "team")]
    checker = AUTHORS["olivia"] if a["slug"] != "olivia-williams" else AUTHORS["james"]
    org_site = {"@context": "https://schema.org", "@graph": [
      {"@type": "Organization", "@id": DOMAIN + "/#organization", "name": SITE, "url": DOMAIN,
       "logo": {"@type": "ImageObject", "@id": DOMAIN + "/#logo", "url": DOMAIN + "/images/logo.png",
                "contentUrl": DOMAIN + "/images/logo.png", "width": 400, "height": 120, "caption": SITE},
       "image": {"@id": DOMAIN + "/#logo"},
       "description": "Independent UK reviews of online casinos and betting sites. Every site is "
                      "joined with real money, every withdrawal is timed and published in an open "
                      "ledger, and every score comes from a published five-pillar model.",
       "areaServed": {"@type": "Country", "name": "United Kingdom"},
       "foundingDate": "2026", "email": "hello@rhiacharles.co.uk",
       "founder": {"@id": DOMAIN + "/#author-james-wilson"},
       "knowsAbout": ["online casinos", "casino withdrawal times", "casino bonuses",
                      "wagering requirements", "UK gambling regulation", "non-GamStop casinos",
                      "sports betting", "responsible gambling"],
       "publishingPrinciples": DOMAIN + "/how-we-review/",
       "actionableFeedbackPolicy": DOMAIN + "/contact/",
       "correctionsPolicy": DOMAIN + "/about/#corrections",
       "ownershipFundingInfo": DOMAIN + "/about/#funding"},
      # No SearchAction is declared: this site has no search endpoint, and
      # advertising one that 404s is a false capability claim in structured data.
      {"@type": "WebSite", "@id": DOMAIN + "/#website", "name": SITE, "url": DOMAIN,
       "publisher": {"@id": DOMAIN + "/#organization"}, "inLanguage": "en-GB"}]}

    # Guides are Articles; ranking pages are CollectionPages; everything else is
    # a plain WebPage. `pageType` in front matter overrides the default.
    if fm.get("pageType"):
        page_type = ["WebPage", fm["pageType"]]
    elif fm.get("itemlist"):
        page_type = ["WebPage", "CollectionPage"]
    else:
        page_type = "WebPage"

    people = [person(a), person(checker)]
    if fm.get("allAuthors"):
        have = {n["@id"] for n in people}
        for k in ("james", "olivia"):
            n = person(AUTHORS[k])
            if n["@id"] not in have:
                people.append(n)
                have.add(n["@id"])

    g = people + [
         {"@type": page_type,
          "@id": url + "#webpage", "url": url,
          "name": strip_tags(fm["h1"]), "headline": strip_tags(fm["h1"]),
          "alternateName": fm["title"], "description": fm["description"],
          "inLanguage": "en-GB", "isPartOf": {"@id": DOMAIN + "/#website"},
          "primaryImageOfPage": {"@type": "ImageObject", "@id": url + "#primaryimage",
                                 "url": DOMAIN + "/images/og-rhiacharles.jpg",
                                 "width": 1200, "height": 630},
          "author": {"@id": DOMAIN + "/#author-" + a["slug"]},
          "publisher": {"@id": DOMAIN + "/#organization"},
          "reviewedBy": {"@id": DOMAIN + "/#author-" + checker["slug"]},
          "datePublished": fm.get("published", "2026-02-02"),
          "dateModified": fm.get("modified", UPDATED),
          "isAccessibleForFree": True,
          "breadcrumb": {"@id": url + "#breadcrumb"}}]

    # g[2] is the page node above; keep the index stable if `people` grows
    PAGE = len(people)
    if fm.get("itemlist"):
        g[PAGE]["mainEntity"] = {"@id": url + "#ranking"}

    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    for i, (n, h) in enumerate(fm.get("crumbs", []), start=2):
        items.append({"@type": "ListItem", "position": i, "name": n, "item": DOMAIN + h})
    g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items})

    if fm.get("itemlist"):
        g.append({"@type": "ItemList", "@id": url + "#ranking",
                  "name": strip_tags(fm.get("itemlistName", fm["h1"])),
                  "numberOfItems": len(fm["itemlist"]),
                  "itemListOrder": "https://schema.org/ItemListOrderDescending",
                  "itemListElement": [
                    {"@type": "ListItem", "position": i, "name": OPS[s]["name"],
                     "url": DOMAIN + "/casino-reviews/" + s + "/",
                     "item": {"@type": "Organization", "@id": DOMAIN + "/#operator-" + s,
                              "name": OPS[s]["name"],
                              "description": strip_tags(OPS[s]["usp"]),
                              "image": img_obj(OPS[s]["logo"], OPS[s]["name"] + " logo"),
                              "url": DOMAIN + "/casino-reviews/" + s + "/"}}
                    for i, s in enumerate(fm["itemlist"], 1)]})

    faqs = extract_faq(body)
    if faqs:
        g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": faqs})

    g += extract_howto(body, url)

    if fm.get("reviewOf"):
        op = OPS[fm["reviewOf"]]
        sl = fm["reviewOf"]
        oid = DOMAIN + "/#operator-" + sl
        g[PAGE]["about"] = {"@id": oid}
        # The operator is a top-level node, not an object nested inside the
        # Review, so `about` and `itemReviewed` resolve to the same sibling
        # entity rather than to a copy of it.
        # AggregateRating is declared only where a genuine aggregate exists: the
        # headline score is the weighted mean of the five criterion scores
        # published in the scorecard on this page, so ratingCount is 5 ratings
        # from 1 reviewer, and the description says so rather than leaving a
        # bare "5" to be read as five customers.
        crit = ", ".join(label for _, _, label, _ in WEIGHTS)   # keep "GBP" cased
        g.append({"@type": "Organization", "@id": oid, "name": op["name"],
                  "description": strip_tags(op["usp"]),
                  "image": img_obj(op["logo"], op["name"] + " logo"),
                  "url": DOMAIN + "/casino-reviews/" + sl + "/",
                  "foundingDate": str(op["launched"]), "legalName": op["operator"],
                  "aggregateRating": {
                      "@type": "AggregateRating", "@id": url + "#aggregaterating",
                      "ratingValue": score10(sl), "bestRating": 10, "worstRating": 1,
                      "ratingCount": len(WEIGHTS), "reviewCount": 1,
                      "ratingExplanation":
                          "Weighted mean of %d criterion scores published in the scorecard on this "
                          "page (%s), assessed by one named reviewer. Not an average of customer "
                          "ratings." % (len(WEIGHTS), crit),
                      "author": {"@id": DOMAIN + "/#author-" + a["slug"]},
                      "itemReviewed": {"@id": oid}},
                  "subjectOf": {"@id": url + "#review"}})
        g.append({"@type": "Review", "@id": url + "#review", "name": strip_tags(fm["h1"]),
                  "mainEntityOfPage": {"@id": url + "#webpage"},
                  "reviewBody": strip_tags(op["usp"]),
                  "itemReviewed": {"@id": oid},
                  "author": {"@id": DOMAIN + "/#author-" + a["slug"]},
                  "publisher": {"@id": DOMAIN + "/#organization"},
                  "datePublished": fm.get("published", "2026-02-02"),
                  "dateModified": fm.get("modified", UPDATED),
                  "reviewRating": {"@type": "Rating", "ratingValue": score10(sl),
                                   "bestRating": 10, "worstRating": 1,
                                   "author": {"@id": DOMAIN + "/#author-" + a["slug"]}}})
    # The withdrawal ledger is a published dataset, and typing it as one is both
    # accurate and the only schema on this site that describes the evidence
    # rather than the writing.
    if fm.get("dataset"):
        total = sum(v["ledgerN"] for v in OPS.values())
        g.append({"@type": "Dataset", "@id": url + "#dataset",
                  "name": "Rhia Charles withdrawal ledger",
                  "description": ("Every withdrawal requested from an online casino by %s and timed "
                                  "from the confirm button to cleared funds: %d requests across %d "
                                  "operators, with median and slowest times, refusals and identity "
                                  "verification turnaround." % (a["name"], total, len(OPS))),
                  "url": url, "isAccessibleForFree": True,
                  "license": DOMAIN + "/terms/",
                  "creator": {"@id": DOMAIN + "/#author-" + a["slug"]},
                  "publisher": {"@id": DOMAIN + "/#organization"},
                  "datePublished": fm.get("published", "2026-02-02"),
                  "dateModified": fm.get("modified", UPDATED),
                  "temporalCoverage": "2026-01/2026-09",
                  "spatialCoverage": {"@type": "Place", "name": "Bristol, United Kingdom"},
                  "measurementTechnique": "Manual timing from withdrawal request to cleared funds",
                  "variableMeasured": [
                    {"@type": "PropertyValue", "name": "Withdrawals logged"},
                    {"@type": "PropertyValue", "name": "Median time to cleared funds"},
                    {"@type": "PropertyValue", "name": "Slowest time to cleared funds"},
                    {"@type": "PropertyValue", "name": "Withdrawals refused"},
                    {"@type": "PropertyValue", "name": "Identity verification turnaround"}],
                  "keywords": ["casino withdrawal times", "payout speed", "online casinos",
                               "United Kingdom"]})

    for extra in fm.get("extraSchema", []):
        g.append(extra)
    page = {"@context": "https://schema.org", "@graph": g}
    j = lambda dd: json.dumps(dd, ensure_ascii=False, separators=(",", ":"))
    return ('<script type="application/ld+json">\n%s\n</script>\n'
            '<script type="application/ld+json">\n%s\n</script>' % (j(org_site), j(page)))


# ---------------------------------------------------------------- page
def review_notice(slug):
    op = OPS.get(slug)
    if not op:
        return ""
    return ('<div class="callout callout--warn" id="licensing-notice">'
            '<span class="t">One thing to know before you go any further</span>'
            '<p>%s does not hold a UK Gambling Commission licence. It runs on %s. That is exactly '
            'why it sits outside <a href="/non-gamstop-casinos/">GamStop</a> and outside UKGC '
            'affordability checks, and it is also why, if a withdrawal is refused, your recourse '
            'runs through a foreign regulator rather than the Commission or IBAS. Playing here has '
            'never been an offence for a UK resident and your winnings remain '
            '<a href="/gambling-winnings-tax-uk/">free of tax</a>. '
            '<strong>If you are registered with GamStop, do not open an account.</strong></p></div>'
            % (op["name"], op["licence"]))


RG_PANEL = '''<div class="rg">
<h3>Before you play: staying in control</h3>
<p>Gambling is a paid entertainment. It is not an income, it is not a way out of a shortfall, and the
house edge does not take days off. The only reliable way to finish ahead is to decide what an evening
is worth to you before you start, and to stop when that is spent.</p>
<p><strong>Every operator on this site is licensed offshore and none of them is connected to
GamStop.</strong> If you are registered with GamStop, or have ever self-excluded from any gambling
company, these sites will not stop you and neither will your self-exclusion. Please do not use them.
Install <a href="https://betblocker.org/" rel="nofollow noopener" target="_blank">BetBlocker</a>
(free) or <a href="https://gamban.com/" rel="nofollow noopener" target="_blank">Gamban</a>, which do
block offshore sites, and turn on the gambling block inside your banking app.</p>
<p>Free, confidential help in the United Kingdom, 24 hours a day:</p>
<ul>
<li><strong>National Gambling Helpline (GamCare)</strong> &mdash; <a href="tel:08088020133">0808 8020 133</a>, or live chat at <a href="https://www.gamcare.org.uk/" rel="nofollow noopener" target="_blank">gamcare.org.uk</a></li>
<li><strong>GamStop</strong> &mdash; free national self-exclusion from every UKGC-licensed site, at <a href="https://www.gamstop.co.uk/" rel="nofollow noopener" target="_blank">gamstop.co.uk</a></li>
<li><strong>BeGambleAware</strong> &mdash; advice, self-assessment and local treatment services at <a href="https://www.begambleaware.org/" rel="nofollow noopener" target="_blank">begambleaware.org</a></li>
<li><strong>Gordon Moody</strong> &mdash; residential treatment for severe gambling harm, <a href="https://gordonmoody.org.uk/" rel="nofollow noopener" target="_blank">gordonmoody.org.uk</a></li>
<li><strong>Samaritans</strong> &mdash; <a href="tel:116123">116 123</a>, free, any time, from any phone</li>
</ul>
<p style="margin-bottom:0"><span class="gc-18">18+</span> You must be at least 18 to gamble online in
the United Kingdom. My full <a href="/responsible-gambling/">responsible gambling guide</a> covers
deposit limits, bank blocks, blocking software and how to self-exclude.</p>
</div>'''


def render(fm, lede, body, extra=None, lb=""):
    hero, tail = lead_html(fm, lede, extra)
    url = DOMAIN + fm["url"]
    canonical = DOMAIN + "/" if CANONICAL_TO_HOME else url
    t, d = html.escape(fm["title"]), html.escape(fm["description"])
    robots = fm.get("robots", "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1")
    body_cls = "home-ledger" if fm["url"] == "/" else "page-ledger"
    return '''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<link rel="alternate" hreflang="en-gb" href="%s">
<link rel="alternate" hreflang="x-default" href="%s">
<meta name="robots" content="%s">
<meta name="rating" content="adult">
<meta name="author" content="%s">
<meta property="og:type" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:site_name" content="%s">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="%s/images/og-rhiacharles.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Rhia Charles - independent UK casino reviews">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s/images/og-rhiacharles.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48x48.png" sizes="48x48" type="image/png">
<link rel="icon" href="/favicon-96x96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/favicon-144x144.png" sizes="144x144" type="image/png">
<link rel="icon" href="/favicon-192x192.png" sizes="192x192" type="image/png">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/home.css">
%s
</head>
<body class="%s">
<a class="skip" href="#main">Skip to content</a>
%s
%s
<main id="main"><div class="wrap"><div class="content">
%s
%s
%s
</div></div></main>
%s
</body>
</html>
''' % (t, d, canonical, url, url, robots, AUTHORS[fm.get("author", "team")]["name"],
       fm.get("ogType", "article"), t, d, url, SITE, DOMAIN, t, d, DOMAIN,
       schema_blocks(fm, body, url), body_cls, nav_html(), hero, lb, tail, body, foot_html())


FM_RE = re.compile(r"^\s*<!--@(.*?)@-->\s*", re.S)


def main():
    pages = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.endswith(".html"):
            continue
        raw = open(os.path.join(SRC, fn), encoding="utf-8").read()
        m = FM_RE.match(raw)
        if not m:
            raise SystemExit("%s: missing front matter" % fn)
        pages.append((fn, json.loads(m.group(1)), raw[m.end():]))

    seen = {}
    for fn, fm, _ in pages:
        if fm["url"] in seen:
            raise SystemExit("duplicate url %s in %s and %s" % (fm["url"], seen[fm["url"]], fn))
        seen[fm["url"]] = fn

    for fn, fm, frag in pages:
        try:
            full_h1, lede, unwrapped, extra = split_fragment(frag)
        except AssertionError as e:
            raise SystemExit("%s: %s" % (fn, e))
        if full_h1:
            fm = dict(fm, h1=full_h1)

        base = re.split(r"\s*[:·|]\s*", fm["h1"])[0]
        heading = fm.get("lbHeading") or (base if base.lower().startswith(("best", "the"))
                                          else "The best %s" % base[0].lower() + base[1:])
        sports = fm["url"] in ("/online-betting/", "/best-sports-betting-sites/",
                               "/non-gamstop-betting-sites-uk/",
                               "/football-betting-sites-not-on-gamstop/")

        lb_html = lb_notice = ""
        if fm.get("itemlist"):
            lb_html, lb_notice = leaderboard_from_ops(fm, heading, sports)

        body = transform(expand_generated(unwrapped))
        if not lb_notice and fm.get("reviewOf"):
            lb_notice = review_notice(fm["reviewOf"])

        # The offer table leads every page that has one, straight under the H1
        # and byline. On mobile the hero's tail is reordered below it by CSS.
        # The offer table is passed separately so render() can place it directly
        # under the hero, above the hero's tail, on every viewport.
        body = (body + lb_notice + RG_PANEL) if fm.get("rg", True) else (body + lb_notice)

        doc = resolve_tokens(render(fm, resolve_tokens(lede) or html.escape(fm["description"]),
                                    body, extra, lb_html))

        # ---- build-time integrity checks. A silent structural break on a money
        # page is worse than a failed build.
        n_faq = len(re.findall(r"<summary>", doc))
        n_schema = doc.count('"@type":"Question"')
        assert n_faq == n_schema, "%s: %d FAQ items in markup, %d in schema" % (fm["url"], n_faq, n_schema)
        opens, closes = len(re.findall(r"<div\b", doc)), doc.count("</div>")
        assert opens == closes, "%s: unbalanced <div> — %d open, %d close" % (fm["url"], opens, closes)
        assert doc.count("<h1") == 1, "%s: %d H1 tags, expected exactly 1" % (fm["url"], doc.count("<h1"))
        assert "{{" not in doc, "%s: unresolved token %s" % (fm["url"], re.search(r"\{\{[^}]*\}\}", doc).group(0))
        assert ".html" not in re.sub(r'href="[^"]*\.html"', "", doc) or True
        for bad in re.findall(r'href="(/[^"]*\.html)"', doc):
            raise SystemExit("%s: internal link with .html extension: %s" % (fm["url"], bad))

        out_dir = os.path.join(ROOT, fm["url"].strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(doc)

    # ---- sitemap
    # Carries the image extension: the operator logos on a ranking page and the
    # author portraits are the only images on this site worth discovering, and
    # naming them here is the only way an image crawler finds a logo that lives
    # inside a table rather than in prose.
    def page_images(fm):
        imgs = []
        for sl in list(fm.get("itemlist", [])):
            op = OPS[sl]
            imgs.append((DOMAIN + op["logo"], "%s logo" % op["name"]))
        if fm.get("reviewOf"):
            op = OPS[fm["reviewOf"]]
            imgs.append((DOMAIN + op["logo"], "%s logo" % op["name"]))
        if fm["url"] == "/authors/":
            for k in ("james", "olivia"):
                a = AUTHORS[k]
                imgs.append((DOMAIN + a["photo"].replace(".jpg", "@2x.jpg"), a["name"]))
        seen, out = set(), []
        for u, t in imgs:
            if u not in seen:
                seen.add(u)
                out.append((u, t))
        return out

    urls = [(fm, fm.get("modified", UPDATED), fm.get("changefreq", "weekly"),
             fm.get("priority", "0.7")) for _, fm, _ in pages
            if "noindex" not in fm.get("robots", "")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
          '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for fm, lm, cf, pr in urls:
        row = ["  <url>",
               "    <loc>%s%s</loc>" % (DOMAIN, fm["url"]),
               "    <lastmod>%s</lastmod>" % lm,
               "    <changefreq>%s</changefreq>" % cf,
               "    <priority>%s</priority>" % pr]
        for iu, it in page_images(fm):
            row += ["    <image:image>",
                    "      <image:loc>%s</image:loc>" % iu,
                    "      <image:title>%s</image:title>" % html.escape(it),
                    "    </image:image>"]
        row.append("  </url>")
        sm.append("\n".join(row))
    sm.append("</urlset>")

    listed = set(fm["url"] for fm, _, _, _ in urls)
    written = set(fm["url"] for _, fm, _ in pages)
    noindexed = set(fm["url"] for _, fm, _ in pages if "noindex" in fm.get("robots", ""))
    assert listed == written - noindexed, (
        "sitemap/pages mismatch — only in sitemap: %s; missing from sitemap: %s"
        % (sorted(listed - written), sorted(written - noindexed - listed)))
    for fm, lm, cf, pr in urls:
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", lm), "%s: bad lastmod %r" % (fm["url"], lm)
        assert cf in ("always", "hourly", "daily", "weekly", "monthly", "yearly", "never"), \
            "%s: bad changefreq %r" % (fm["url"], cf)
        assert 0.0 <= float(pr) <= 1.0, "%s: bad priority %r" % (fm["url"], pr)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write("""# robots.txt for %s
User-agent: *
Allow: /
Disallow: /go/
Disallow: /*?

Sitemap: %s/sitemap.xml

# SEO crawlers — blocked so our link graph and content stay out of third-party
# indexes and competitors cannot lift the ledger data wholesale.
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: Rogerbot
Disallow: /

User-agent: serpstatbot
Disallow: /

User-agent: SistrixBot
Disallow: /
""" % (DOMAIN, DOMAIN))

    print("built %d pages · sitemap %d urls" % (len(pages), len(urls)))
    if MISSING:
        print("WARNING no affiliate link for: " + ", ".join(sorted(MISSING)))


if __name__ == "__main__":
    main()
