#!/usr/bin/env python3
"""Writes _build/pages/3xx-review-*.html and the reviews hub.

The prose in COPY below is written per operator — the verdict, the cashier
account, the weaknesses, the FAQ answers. Only the scaffolding is generated:
front matter, the specification grid, the computed scorecard and clearance
table, and the internal links. That way every review carries the same
structure without every review carrying the same sentences.

Run this, then run build.py.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_build", "pages")
OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))

# ---------------------------------------------------------------- per-operator copy
COPY = {
 "smash": dict(
  n=300, rank=1, rate="45%",
  eyebrow="Ranked 1st of 10 &middot; 9 payouts logged",
  lede="Smash is the site I would open if I were opening one. Not because it is the "
       "prettiest &mdash; it is not &mdash; but because its welcome offer asks 10x where the rest of "
       "this market asks 35x, and because nine timed withdrawals came back at a median of "
       "seven hours forty with none refused. On my model that combination is worth "
       "{{clear:smash:net}} on a &pound;100 deposit, which is the only positive number in the "
       "top three.",
  verdict="The best combination of a clearable bonus and a working cashier that I have found "
          "for UK players. If you are opening one account this month, open this one.",
  body="""
<h2 id="bonus">The bonus, which is the whole argument</h2>
<p>Smash's welcome offer is <strong>{{op:smash:welcome}}</strong> at <strong>10x on deposit plus bonus</strong>. Read that
wagering base carefully, because it is doing something unusual. Ten times deposit plus bonus is a larger
turnover base than ten times bonus alone &mdash; but it is still a fraction of what the field charges.</p>
<p>On a &pound;100 first deposit the arithmetic runs like this: a {{clear:smash:bonus}} bonus, a turnover
requirement of {{clear:smash:turnover}}, an expected cost at 96% RTP of {{clear:smash:cost}}, and an expected
net of <strong>{{clear:smash:net}}</strong>. Compare that with the 35x offers elsewhere on this site, every one of which
comes out negative, and you have the reason Smash is ranked first.</p>
<p>The terms behind it are also unusually clean. Maximum bet while wagering is &pound;5, which is standard.
There is no maximum cashout on the match, which is not &mdash; a cashout cap is the term that quietly converts a
large bonus into a small one, and its absence here matters more than another hundred per cent on the headline.
Expiry is 30 days, which is long enough to clear 10x without being forced into stakes you did not intend.</p>
<p>Full workings, and every other offer priced the same way, are on my <a href="/online-casinos/bonuses/">casino
bonuses page</a>.</p>

<h2 id="payouts">The cashier</h2>
<p>Nine withdrawals, median <strong>7 hours 40 minutes</strong>, slowest 31 hours, none refused, no operator fee at
either end. The 31-hour case was the first withdrawal on the account, which is when identity verification runs
&mdash; more on that below.</p>
<p>Crypto was consistently the quickest route out, as it is everywhere: my Smash crypto requests cleared in
three to six hours against roughly a day for MiFinity and two working days for a card. Eight coins are supported
and pounds sterling is a native wallet currency, so there is no conversion spread in either direction. Every
timing is in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>
<p><strong>Identity verification was the fastest I recorded anywhere.</strong> I uploaded a passport photo page, a
selfie and a council tax bill at 09:12 and the account was marked verified at 13:50 &mdash; four hours thirty-eight
minutes, with nothing rejected. If you do this on the day you register rather than waiting for the prompt, your
first payout runs at the speed of the payment rail rather than a compliance queue.</p>

<h2 id="games">Games and software</h2>
<p>{{op:smash:games}}, with the real feeds from {{op:smash:providers}} rather than white-label imitations &mdash; I
checked by opening the studio clients directly and comparing against the studios' published game information.
Fifteen popular slots were checked against studio RTP defaults; twelve matched the high build and three did not
publish a figure in the panel at all, which is a genuine mark against it and is why the games score is 8.8 rather
than higher. The <a href="/high-payout-casinos/">high payout casinos page</a> explains why that matters.</p>
<p>Three live studios are on the account, which is enough for blackjack, roulette and baccarat at UK evening hours
but thinner than <a href="/casino-reviews/seven/">Seven's</a> five. The lobby has a working search box, which sounds
trivial until you try to find one slot in six thousand on a phone without one.</p>

<h2 id="weak">Where it falls short</h2>
<p>Three things, stated plainly. The <strong>Anjouan licence</strong> is the weakest of the regimes represented on this
site &mdash; it tells you the operator paid a fee and passed a light-touch check, and if a dispute went badly your
practical recourse would be very limited. The <strong>live floor is thin</strong> against the specialists. And the
<strong>site design is loud</strong> in a way that will not be for everyone, with more animation than I would choose.</p>
<p>None of those outweighs a clearable bonus and a cashier that works, which is why it is first. But a first place
with three real weaknesses is more useful to you than a first place with none.</p>
""",
  faq=[("Is Smash Casino legitimate?",
        "It holds an Anjouan Gaming Authority licence, runs the genuine Pragmatic Play, Evolution, BGaming and Hacksaw Gaming feeds rather than clones, and has paid all nine withdrawals I have requested with a median of 7 hours 40 minutes and none refused. It does not hold a UK Gambling Commission licence, so it sits outside GamStop, outside UKGC stake limits and outside IBAS dispute resolution."),
       ("What is Smash Casino's wagering requirement?",
        "10x on deposit plus bonus, against a market standard of 35x on the bonus alone. On a £100 first deposit that means turning over £3,000, which costs roughly £120 in expected losses at 96% RTP against a £200 bonus — leaving about £80 of value. It is the only welcome offer I rank with clearly positive expected value on that basis."),
       ("How long does Smash Casino take to pay out?",
        "Median 7 hours 40 minutes across nine timed withdrawals, with the slowest at 31 hours and none refused. Crypto was quickest at three to six hours; MiFinity took about a day and debit cards two working days. The 31-hour case was a first withdrawal, when identity verification runs alongside the request."),
       ("Does Smash Casino accept UK players?",
        "Yes, with a UK address, pounds sterling as a native wallet currency and no forced conversion. Debit cards, Apple Pay, MiFinity, Jeton, AstroPay and eight cryptocurrencies all work. It is not UK Gambling Commission licensed, so it is not connected to GamStop — if you have self-excluded, please do not open an account."),
       ("What is the minimum deposit at Smash Casino?",
        "£20, with a matching £20 minimum withdrawal and a £10,000 weekly withdrawal cap. The weekly cap is worth checking before you play rather than after you win: a £20,000 win would be paid over two weeks.")],
 ),

 "kingdom": dict(
  n=310, rank=2, rate="45%",
  eyebrow="Ranked 2nd of 10 &middot; 11 payouts logged &middot; fastest cashier tested",
  lede="Eleven withdrawals. Median three hours five minutes. The fastest was 41 minutes, requested at "
       "02:40 on a Sunday out of curiosity and settled by 03:21. Kingdom has the best cashier I have "
       "measured anywhere, and it is second rather than first only because its welcome bonus is one I "
       "would tell you to decline.",
  verdict="The best cashier in this market by a distance. Decline the welcome bonus and it is arguably the "
          "best account on this site; take the bonus and you are paying for a fast withdrawal you then have "
          "to earn.",
  body="""
<h2 id="payouts">The cashier, which is why it is here</h2>
<p>Eleven timed withdrawals at a median of <strong>3 hours 5 minutes</strong>. Slowest, 9 hours, and that was a
bank transfer over a weekend. None refused, no operator fee, and no request required a chase. The single fastest
payout in my entire ledger &mdash; across eleven operators and 74 requests &mdash; is a Kingdom crypto withdrawal that
cleared in 41 minutes.</p>
<p>Ten cryptocurrencies are supported, balances are held in pounds rather than in the coin so a price swing cannot
touch your bankroll while you play, and I could not detect a spread against the mid-market rate on conversion in
either direction. That combination is rare and it is the main reason the cashier score is 9.6.</p>
<p>Verification took 11 hours 20 minutes, with one rejection: my driving licence photo was cropped at a corner.
Reshot flat in daylight, it passed immediately. Every timing is in the <a href="/withdrawal-ledger/">withdrawal
ledger</a>, and the wider picture is on <a href="/fast-payout-casinos/">fast payout casinos</a>.</p>

<h2 id="bonus">The bonus, and why I would decline it</h2>
<p>{{op:kingdom:welcome}}, at <strong>30x</strong>. Six hundred per cent is an enormous headline and the multiplier
behind it does the damage.</p>
<p>On a &pound;100 first deposit: a {{clear:kingdom:bonus}} bonus, {{clear:kingdom:turnover}} of required turnover,
an expected cost of {{clear:kingdom:cost}}, and an expected net of <strong>{{clear:kingdom:net}}</strong>. You are, on
average, paying about thirty pounds for the privilege of holding a bonus.</p>
<p>Decline it at the cashier &mdash; there is a checkbox on the deposit screen &mdash; and Kingdom becomes a very
easy recommendation: no turnover condition, no maximum bet rule to breach accidentally, and a withdrawal available
whenever you want one, arriving in about three hours. That is a genuinely good product. The bonus is not part of it.</p>

<h2 id="games">Games and RTP transparency</h2>
<p>{{op:kingdom:games}} is the largest library on this site, running the real {{op:kingdom:providers}} feeds. More
importantly, <strong>Kingdom publishes the return-to-player figure inside every game's information panel</strong>, and
all fifteen popular slots I checked were running the studios' standard high builds rather than the reduced ones many
operators license. That is the single most useful thing a casino can do for a player and almost nobody does it, which
is why Kingdom leads my <a href="/high-payout-casinos/">high payout casinos</a> ranking.</p>
<p>There is a full sportsbook on the same pound-sterling wallet, priced at a 5.9% overround on Premier League match
odds &mdash; a point and a half behind <a href="/casino-reviews/tenobet/">TenoBet</a> but perfectly usable if you
want one account for both. Details on <a href="/best-sports-betting-sites/">best sports betting sites</a>.</p>

<h2 id="weak">Where it falls short</h2>
<p>The bonus, which is covered above and is the entire reason it is not first. Beyond that: the
<strong>&pound;15,000 monthly withdrawal cap</strong> is a monthly rather than weekly structure, which is worse for a
large win &mdash; &pound;20,000 would take about six weeks against two at Smash. And the Cura&ccedil;ao eGaming
licence, while better than Anjouan, is still a long way short of what a UKGC licence would give you.</p>
""",
  faq=[("How fast does Kingdom Casino pay out?",
        "Median 3 hours 5 minutes across eleven timed withdrawals, with the slowest at 9 hours and none refused — the fastest cashier of any operator I have tested. The single quickest was a crypto withdrawal that cleared in 41 minutes at 3am on a Sunday. Ten cryptocurrencies are supported and no operator fee was charged on any request."),
       ("Is Kingdom Casino's 600% bonus worth taking?",
        "No, on my model. At 30x wagering, a £100 first deposit produces a £150 bonus requiring £4,500 of turnover, which costs about £180 in expected losses at 96% RTP — leaving you roughly £30 down on average. Decline it at the cashier and Kingdom becomes an excellent account: fast withdrawals, no turnover condition and no maximum bet rule to breach."),
       ("Does Kingdom Casino show the RTP of its games?",
        "Yes, inside every game's information panel, and all fifteen popular slots I checked were running the studios' standard high builds rather than the reduced-RTP versions many operators license. That is unusual and valuable: the same slot can ship at 96.09% and 90.05%, a gap worth about £60 per £1,000 staked."),
       ("Is Kingdom Casino on GamStop?",
        "No. It holds a Curaçao eGaming licence rather than a UK Gambling Commission one, and GamStop participation is a UKGC licence condition, so it is not connected to the scheme and cannot see a UK self-exclusion. If you are registered with GamStop, please do not open an account — BetBlocker and Gamban both block offshore sites."),
       ("Does Kingdom Casino have a sportsbook?",
        "Yes, on the same pound-sterling wallet as the casino, covering English football to the National League with 140-plus markets on a Championship fixture. It priced Premier League match odds at a 5.9% overround in my testing, which is about a point and a half behind TenoBet but perfectly reasonable if you want one account for betting and casino.")],
 ),

 "rivo": dict(
  n=320, rank=3, rate="45%",
  eyebrow="Ranked 3rd of 10 &middot; 8 payouts logged",
  lede="A 1000% headline usually means the terms behind it are brutal. Here they are not: 10x, on the "
       "bonus alone, which makes Rivo's welcome offer the best expected value I have modelled this year "
       "at {{clear:rivo:net}} on a &pound;100 deposit. The cashier is a step behind the top two, and the "
       "cashback programme is unusually honest.",
  verdict="Take this account for the bonus. Expect a withdrawal to take a working day rather than an "
          "afternoon, and have a bank statement ready if you win more than a few thousand.",
  body="""
<h2 id="bonus">The best expected value on the site</h2>
<p>{{op:rivo:welcome}}, at <strong>10x on the bonus</strong>. On a &pound;100 first deposit that is a
{{clear:rivo:bonus}} bonus requiring {{clear:rivo:turnover}} of turnover, costing about {{clear:rivo:cost}} in
expected losses and leaving <strong>{{clear:rivo:net}}</strong> &mdash; the highest figure of any offer I have priced.</p>
<p>The reason a 1000% offer can beat a 600% one is entirely the multiplier. Rivo asks ten times where
<a href="/casino-reviews/kingdom/">Kingdom</a> asks thirty, and that difference swamps the headline percentage
completely. It is the clearest illustration on this site of why the number in the advert is the wrong number to
read, and the full comparison is on my <a href="/online-casinos/bonuses/">casino bonuses page</a>.</p>
<p>There is a second offer worth naming: a <strong>25% cashback programme paid in cash rather than bonus funds,
with no wagering attached</strong>. Cashback that arrives as a bonus with its own turnover requirement is a loss
rebate you have to earn twice; cashback paid as withdrawable money is genuinely worth its face value. Rivo's is
the latter, and it applies across the casino and the sportsbook.</p>

<h2 id="payouts">The cashier</h2>
<p>Eight withdrawals, median <strong>11 hours 20 minutes</strong>, slowest three days, none refused. That
three-day case is worth describing because it will happen to you: a &pound;1,900 cashout took my cumulative
total past roughly &pound;4,000 and triggered a source-of-funds request. The request was reasonable, I sent a
bank statement PDF, and the money arrived &mdash; three days after I asked for it.</p>
<p>Plan for this. Above about &pound;4,000 cumulative at most offshore operators, expect to be asked for evidence
of where your money comes from. Having a recent bank statement or payslip already saved as a PDF turns that from
a three-day event into a same-day one.</p>
<p>Seven coins are supported and pounds are held natively. Verification took 21 hours 30 minutes with nothing
rejected. All timings are in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="games">Games and sportsbook</h2>
<p>{{op:rivo:games}} is the smallest library among the sites I rank above sixth, though the studios are strong
&mdash; {{op:rivo:providers}}, including Nolimit City and Push Gaming, which skew towards high-volatility slots
with genuine mechanical interest rather than filler. Two live studios, which is adequate rather than good.</p>
<p>The sportsbook is the least interesting part of the operation: a 6.8% overround on Premier League match odds
and coverage stopping at League Two. Bet here only if the cashback matters to you across both products. See
<a href="/best-sports-betting-sites/">best sports betting sites</a>.</p>

<h2 id="weak">Where it falls short</h2>
<p>The cashier is genuinely a step behind Smash and Kingdom &mdash; eleven hours against seven and three &mdash;
and the source-of-funds threshold arrives lower here than elsewhere. The library is small. And the sportsbook is
priced defensively enough that I would not use it on merit.</p>
""",
  faq=[("Is Rivo Casino's 1000% bonus real?",
        "Yes, and unusually it is worth taking. The offer is 1000% total up to £10,000 across the welcome package at 10x wagering on the bonus, which is a third of the market standard. On a £100 first deposit that produces a £250 bonus requiring £2,500 of turnover, costing about £100 in expected losses — leaving roughly £150 of value, the best figure of any offer I have modelled."),
       ("How long does Rivo Casino take to pay?",
        "Median 11 hours 20 minutes across eight timed withdrawals, with none refused. The slowest took three days, when a £1,900 cashout pushed my cumulative total past about £4,000 and triggered a source-of-funds request. Having a recent bank statement saved as a PDF turns that kind of check from a three-day wait into a same-day one."),
       ("Does Rivo Casino pay cashback in real money?",
        "Yes. Rivo's VIP programme pays up to 25% cashback as withdrawable cash with no wagering attached, which is genuinely unusual — most cashback in this market arrives as bonus funds carrying their own turnover requirement, which makes it a loss rebate you have to earn twice. Rivo's applies across both the casino and the sportsbook."),
       ("Is Rivo Casino licensed?",
        "It holds a Curaçao Gaming Control Board licence, which since the 2023–24 reform requires anti-money-laundering controls, a complaints process and a responsible gambling policy under a direct operator licence rather than the old master-licence chain. It does not hold a UK Gambling Commission licence, so there is no GamStop, no funds segregation requirement and no IBAS dispute resolution."),
       ("What is Rivo Casino's withdrawal limit?",
        "£20 minimum and £10,000 per week maximum. Expect a source-of-funds request above roughly £4,000 cumulative, which in my testing added three days to one withdrawal. A £20,000 win would be paid over about two weeks under the weekly cap.")],
 ),

 "tenobet": dict(
  n=330, rank=4, rate="45%", sports=True,
  eyebrow="Ranked 1st for sports &middot; 6 payouts logged",
  lede="The only pure sportsbook I rank, and it shows in the one place that matters: price. TenoBet "
       "priced Premier League match odds at a <strong>4.4% overround</strong> against 5.9% to 8.0% at the "
       "casino-first books, covers English football down to National League North, and its welcome offer "
       "is the only sports bonus here with clearly positive expected value.",
  verdict="If betting is the point rather than a side dish, this is the account to open. The absence of "
          "best odds guaranteed is a real cost for racing punters and I would weigh it seriously.",
  body="""
<h2 id="prices">The prices, measured</h2>
<p>I priced eight identical selections at every book inside the same two-hour Saturday window, before team news.
TenoBet came out tightest on every football market:</p>
<div class="table-scroll">
<table class="data">
<caption>TenoBet's measured overround against the field</caption>
<thead><tr><th scope="col">Market</th><th scope="col" class="num">TenoBet</th><th scope="col" class="num">Best of the rest</th><th scope="col" class="num">Worst</th></tr></thead>
<tbody>
<tr><th scope="row">Premier League 1X2</th><td class="num">4.4%</td><td class="num">5.9%</td><td class="num">8.0%</td></tr>
<tr><th scope="row">Championship 1X2</th><td class="num">5.1%</td><td class="num">6.8%</td><td class="num">11.8%</td></tr>
<tr><th scope="row">League One / Two</th><td class="num">5.6%</td><td class="num">7.2%</td><td class="num">12.4%</td></tr>
<tr><th scope="row">Both teams to score</th><td class="num">5.8%</td><td class="num">7.1%</td><td class="num">9.4%</td></tr>
<tr><th scope="row">Horse racing win</th><td class="num">12.6%</td><td class="num">15.1%</td><td class="num">21.0%</td></tr>
</tbody>
</table>
</div>
<p>Over a season staking &pound;2,000, the gap between TenoBet and the worst book here is roughly &pound;72 on
Premier League bets and more than &pound;130 on lower-league ones &mdash; for placing identical bets. That is worth
considerably more than any welcome offer. The method for calculating an overround yourself is on my
<a href="/online-betting/">online betting guide</a> and takes fifteen seconds per market.</p>

<h2 id="coverage">Coverage</h2>
<p>{{op:tenobet:games}}, and the depth is the other reason it is here. TenoBet is the only book I rank that
prices English football down to <strong>National League North and South</strong>, carries the WSL and the Women's
Championship with real market depth rather than a token match-result line, and runs Scottish football to League
Two. There are 180-plus markets on an ordinary Championship fixture.</p>
<p>If you follow a club below the EFL, this is not the best option available to you &mdash; it is the only one.
The tier-by-tier comparison is on <a href="/football-betting-sites-not-on-gamstop/">football betting sites not on
GamStop</a>.</p>

<h2 id="bonus">The welcome offer</h2>
<p>{{op:tenobet:welcome}}, at <strong>{{op:tenobet:wagering}}</strong>. Sports bonuses are structurally better
value than casino ones because the turnover multiple is small: {{clear:tenobet:turnover}} of qualifying betting
against a {{clear:tenobet:bonus}} bonus costs roughly {{clear:tenobet:cost}} at a typical football margin,
leaving <strong>{{clear:tenobet:net}}</strong>.</p>
<p>Check the usual three things before claiming: whether each leg of an accumulator must meet the 1.80 minimum,
whether void bets count towards turnover, and whether the stake is returned with a free bet. All three are in
the terms.</p>

<h2 id="payouts">The cashier</h2>
<p>Six withdrawals, median <strong>9 hours 15 minutes</strong>, slowest 26 hours, none refused. Six is a smaller
sample than I would like and I would rather say so than present it as settled. Verification was straightforward
&mdash; passport and selfie only, no proof of address requested &mdash; and cleared in 7 hours 45 minutes.</p>
<p>The minimum deposit is <strong>&pound;10</strong>, the lowest of any site I rank, with a matching &pound;10
minimum withdrawal. Weekly cap is &pound;8,000.</p>

<h2 id="weak">Where it falls short</h2>
<p>Four things, and the first two are real costs rather than quibbles. <strong>No best odds guaranteed</strong>,
which is standard at UK bookmakers and will cost a regular racing punter more over a season than this welcome offer
returns. <strong>Industry each-way terms only</strong> &mdash; no extra places on big handicaps. <strong>No live
streaming.</strong> And <strong>no casino</strong>, which is a feature if betting is what you want and a limitation
if it is not.</p>
""",
  faq=[("Is TenoBet a good bookmaker?",
        "It priced Premier League match odds at a 4.4% overround in my testing, the tightest of seven books measured in the same window, and it covers English football down to National League North with 180-plus markets on a Championship fixture. Six timed withdrawals came back at a median of 9 hours 15 minutes with none refused. It does not offer best odds guaranteed, which is a real cost for racing punters."),
       ("Does TenoBet have a casino?",
        "No, and that is deliberate. TenoBet is the only pure sportsbook I rank, which is a large part of why its prices are tighter — a casino-led operator treats the sportsbook as a feature and prices it defensively, while a book with nothing to fall back on has to compete on price. If you want a casino on the same wallet, Kingdom or Smash are the alternatives."),
       ("What is TenoBet's welcome offer?",
        "100% up to £200 as a free bet on your first deposit, at 6x wagering with minimum odds of 1.80. That is the only sports bonus I rank with clearly positive expected value: 6x turnover at a typical football margin costs roughly £24 to unlock a £100 bonus. Check whether each accumulator leg must meet the minimum odds and whether void bets count."),
       ("How fast does TenoBet pay out?",
        "Median 9 hours 15 minutes across six timed withdrawals, slowest 26 hours, none refused. Crypto was fastest at four to eight hours. One betting-specific point: match results settle within minutes of full time but player props, cards and corners wait for official data and can take hours, so do not request a withdrawal with bets unsettled."),
       ("Is TenoBet on GamStop?",
        "No. It holds an Anjouan Gaming Authority licence rather than a UK Gambling Commission one, so it is not connected to GamStop and cannot see a UK self-exclusion. It also means no IBAS dispute resolution and no best odds guaranteed. If you are registered with GamStop, please do not open an account.")],
 ),

 "gambiva": dict(
  n=340, rank=5, rate="45%",
  eyebrow="Ranked 5th of 10 &middot; 7 payouts logged &middot; best GBP banking",
  lede="Most offshore casinos want you on cryptocurrency, because it is cheaper for them and the card "
       "networks are unreliable in this sector. Gambiva is the only site I rank where I funded an account "
       "straight from a UK banking app by open banking and then withdrew back into the same account &mdash; "
       "no wallet, no exchange, no conversion. If crypto is not for you, this is your account.",
  verdict="The best pound-sterling banking of any site here, wrapped around a perfectly ordinary casino "
          "and a welcome offer you should decline.",
  body="""
<h2 id="cashier">The cashier, which is the reason to be here</h2>
<p>Gambiva supports <strong>{{op:gambiva:gbpMethods}}</strong> &mdash; and the one that matters is the open
banking transfer. You authorise the payment inside your own banking app, the money moves as an ordinary transfer,
and withdrawals return to the same account. No crypto exchange, no e-wallet with its own identity checks, no
conversion spread.</p>
<p>That sounds mundane and it removes almost every friction point UK players meet at offshore casinos: no declined
card, no buying Bitcoin, no second KYC gate at MiFinity. Five open banking withdrawals in my ledger came back at a
median of 14 hours, and same-day where I requested before about 2pm on a weekday.</p>
<p>Apple Pay and Google Pay both worked on deposit, which is the next best answer if open banking is not offered
by your bank. Seven withdrawals overall, median <strong>13 hours 50 minutes</strong>, slowest two days, none
refused. Full detail on <a href="/payment-methods/">UK payment methods</a>.</p>
<p>Verification took 17 hours 10 minutes and included one rejection worth knowing about: <strong>a mobile phone
bill was refused as proof of address</strong>. Use a council tax bill, a utility bill or a bank statement instead
&mdash; phone bills are refused surprisingly often across this market.</p>

<h2 id="bonus">The bonus, which you should decline</h2>
<p>{{op:gambiva:welcome}}, at <strong>35x</strong>. On a &pound;100 first deposit that is a
{{clear:gambiva:bonus}} bonus requiring {{clear:gambiva:turnover}} of turnover, costing {{clear:gambiva:cost}} in
expected losses and leaving <strong>{{clear:gambiva:net}}</strong>.</p>
<p>Thirty-five times is the market standard and the market standard is, on average, working against you. Break-even
sits at about 25x. Decline it at the cashier &mdash; there is a checkbox on the deposit screen &mdash; and you keep
the excellent banking without the turnover condition. The arithmetic for every offer is on my
<a href="/online-casinos/bonuses/">casino bonuses page</a>.</p>

<h2 id="games">Games</h2>
<p>{{op:gambiva:games}} from {{op:gambiva:providers}}, which is a solid mainstream library rather than a
remarkable one. Three live studios including Ezugi's low-limit tables, where minimums start at 50p &mdash; the
longest-lasting product any casino sells on a small budget, and covered on my
<a href="/live-casinos/">live casinos page</a>.</p>
<p>RTP figures are not published in the game information panels, which is a genuine mark against it and is why the
games score sits at 8.6 rather than higher. See <a href="/high-payout-casinos/">high payout casinos</a> for why
that matters more than the game count.</p>

<h2 id="weak">Where it falls short</h2>
<p>The bonus, at a plain 35x. The absence of in-game RTP disclosure. And a &pound;8,000 weekly withdrawal cap
that is mid-table &mdash; a &pound;20,000 win would take about three weeks. The casino itself is competent and
unremarkable; you are here for the cashier.</p>
""",
  faq=[("Can I deposit at Gambiva without using crypto?",
        "Yes, and it is the main reason to choose it. Gambiva is the only site I rank that supports a genuine open banking transfer — you authorise the payment inside your own UK banking app and withdrawals return to the same account, with no wallet, no exchange and no conversion. Apple Pay, Google Pay and debit cards all work too."),
       ("How long does Gambiva take to pay out?",
        "Median 13 hours 50 minutes across seven timed withdrawals, slowest two days, none refused. Open banking withdrawals had a median of about 14 hours and cleared same-day when requested before around 2pm on a weekday. Verification took 17 hours 10 minutes, and note that a mobile phone bill was rejected as proof of address — use a council tax or utility bill."),
       ("Is Gambiva's welcome bonus worth taking?",
        "No, on my model. At 35x wagering a £100 deposit produces a £100 bonus requiring £3,500 of turnover, costing about £140 in expected losses at 96% RTP — leaving you roughly £40 down on average. Break-even sits at about 25x. Decline it at the cashier and you keep the excellent banking without a turnover condition on your balance."),
       ("Is Gambiva Casino safe?",
        "It holds a Curaçao Gaming Control Board licence, runs the genuine Pragmatic Play, Evolution, Hacksaw Gaming, Relax Gaming and BGaming feeds, and has paid all seven withdrawals I have requested. It does not hold a UK Gambling Commission licence, so there is no GamStop, no funds segregation requirement and no IBAS dispute resolution — the trade-off is set out in full on my non-GamStop casinos page."),
       ("Does Gambiva show game RTP?",
        "No — the return-to-player figure is not published in the game information panels, which is a genuine weakness given that popular slots often ship in several RTP builds. Starburst exists at 96.09% and 90.05%, a gap worth about £60 per £1,000 staked. Kingdom does publish in-game RTP and leads my high payout casinos ranking for that reason.")],
 ),

 "wildzy": dict(
  n=350, rank=6, rate="45%",
  eyebrow="Ranked 6th of 10 &middot; 6 payouts logged &middot; best recurring spins",
  lede="Almost every casino front-loads its generosity: an enormous welcome offer, then silence. Wildzy "
       "runs a weekly free-spins drop that kept landing for the eleven weeks I held the account. That is "
       "not a life-changing amount of value, but it is recurring value, and for somebody playing &pound;20 "
       "a week that is worth more than a headline they will never clear.",
  verdict="The best account here for a small, regular budget. Decline the welcome bonus, keep the account "
          "for the weekly spins.",
  body="""
<h2 id="spins">The weekly drop</h2>
<p>Wildzy's welcome package is {{op:wildzy:welcome}}, which is unremarkable. The interesting part arrives
afterwards: a <strong>recurring weekly free-spins drop of 30 to 75 spins</strong> on named Pragmatic Play and
Playson titles, which continued for every one of the eleven weeks I held the account.</p>
<p>Priced honestly, that is roughly &pound;3 to &pound;6 of expected value a week &mdash; small, and it compounds.
Over three months it is worth several times any one-off spins package on this site, including
<a href="/casino-reviews/spinpin/">Spin Pin's</a> larger 450. The full arithmetic is on my
<a href="/non-gamstop-casinos-with-free-spins/">free spins page</a>.</p>
<p>Two conditions to know: the weekly drop requires a &pound;20 qualifying deposit, and <strong>the spins expire
in 48 hours</strong>, which is short. Unused spins are simply lost, so it suits somebody who plays on a predictable
evening rather than sporadically.</p>

<h2 id="bonus">The welcome offer</h2>
<p>{{op:wildzy:welcome}} at <strong>35x</strong>. On a &pound;100 deposit: a {{clear:wildzy:bonus}} bonus,
{{clear:wildzy:turnover}} of turnover, {{clear:wildzy:cost}} of expected cost, and an expected net of
<strong>{{clear:wildzy:net}}</strong>. Decline it. The recurring spins are the reason to be here and they do not
depend on claiming the welcome package.</p>

<h2 id="payouts">The cashier</h2>
<p>Six withdrawals, median <strong>15 hours 5 minutes</strong>, slowest two days, none refused. One of those is
worth describing: a &pound;420 payout where the casino released the money in nine hours and
<strong>Jeton then held it for a further day and a half on its own compliance check</strong>. That is a useful
reminder that an e-wallet is a second identity gate rather than a shortcut, and it is why I would use crypto or a
card here rather than a wallet.</p>
<p>Verification took 22 hours 5 minutes with nothing rejected. Weekly withdrawal cap is &pound;7,500. All timings
are in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="games">Games</h2>
<p>{{op:wildzy:games}} from {{op:wildzy:providers}}. Playson and 3 Oaks feature more heavily than at most sites
here, which suits the spins programme &mdash; the weekly drops are usually on their titles. Two live studios,
which is thin. RTP is not published in-game.</p>

<h2 id="weak">Where it falls short</h2>
<p>A 35x welcome offer you should decline, an Anjouan licence that offers weak protection, a mid-table cashier,
a thin live floor, and 48-hour spin expiry that punishes irregular play. This is a good account for one specific
kind of player &mdash; small stakes, regular evenings &mdash; and an ordinary one for everybody else.</p>
""",
  faq=[("Does Wildzy give free spins every week?",
        "Yes. Alongside the welcome package Wildzy runs a recurring weekly drop of 30 to 75 free spins on named Pragmatic Play and Playson titles, which arrived for every one of the eleven weeks I held the account. It requires a £20 qualifying deposit each week and the spins expire in 48 hours, so unused spins are lost. Priced honestly it is worth roughly £3 to £6 a week."),
       ("Is Wildzy's welcome bonus good?",
        "No, on my model. It is 150% up to £750 plus 150 spins at 35x wagering, which on a £100 deposit means £5,250 of turnover costing about £210 in expected losses to unlock a £150 bonus — roughly £60 down on average. Decline it at the cashier. The recurring weekly spins are the real reason to hold this account and they do not depend on claiming the welcome offer."),
       ("How fast does Wildzy pay out?",
        "Median 15 hours 5 minutes across six timed withdrawals, slowest two days, none refused. One £420 payout is instructive: the casino released it in nine hours and Jeton then held it a further day and a half on its own compliance check. An e-wallet is a second identity gate rather than a shortcut, so crypto or a card is the better route here."),
       ("Is Wildzy Casino licensed?",
        "It holds an Anjouan Gaming Authority licence, which has minimal published requirements — holding it tells you the operator paid a fee and passed a light-touch check. It is not licensed by the UK Gambling Commission, so there is no GamStop, no stake or spin-speed limits, no funds segregation requirement and no IBAS dispute resolution."),
       ("What slots are the Wildzy free spins on?",
        "Usually named Pragmatic Play and Playson titles — Solar Queen, Buffalo Power, Big Bass Bonanza and Wolf Gold appeared most often during the eleven weeks I held the account. Check the game information panel before using them: several of these ship in multiple RTP builds, and the same spins on a lower build are worth materially less.")],
 ),

 "seven": dict(
  n=360, rank=7, rate="45%",
  eyebrow="Ranked 7th of 10 &middot; 6 payouts logged &middot; best live floor",
  lede="Five live studios on one account, with English-speaking blackjack and roulette tables genuinely "
       "staffed through UK evening hours rather than nominally listed and empty at nine o'clock &mdash; I "
       "checked across three evenings. If you play live tables rather than slots, this is the site, and the "
       "reason it ranks seventh is that its cashier is the slowest of the verified group.",
  verdict="The best live casino here by a comfortable margin, let down by an average cashier. Decline the "
          "bonus, which is unusable at the tables anyway.",
  body="""
<h2 id="live">The live floor</h2>
<p>Five studios: <strong>{{op:seven:providers}}</strong>. That breadth is unmatched on this site and each one
brings something specific &mdash; Evolution for stream quality and table variety, Pragmatic Play Live for cheaper
minimums, Playtech for blackjack seat availability at peak, Ezugi for 50p tables, and Authentic Gaming for streams
from real land-based casino floors rather than a studio.</p>
<p>I sat at tables across three evenings between 7pm and 1am, because &ldquo;English tables available&rdquo; is the
claim most often made and least often true in this market. Seven passed on all three: full English blackjack and
roulette lists throughout, with the tables still populated after midnight.</p>
<p>Limits run from <strong>50p to &pound;500,000</strong> on the VIP baccarat tables. The high end is far beyond
anything I would play, but it tells you the liquidity is real. The low end matters more for most people: a 50p
minimum means a &pound;25 bankroll survives a genuinely long session, which is not true anywhere on the slot side.</p>
<p>Worth restating here what the <a href="/live-casinos/">live casinos page</a> covers in full: live blackjack with
basic strategy runs at about 99.5% return to player against 94% to 97% on slots, and deals sixty hands an hour
against a slot's six hundred spins. At the same stake, an hour at the table costs roughly a eightieth of an hour on
the reels.</p>

<h2 id="bonus">The bonus, which you cannot use here</h2>
<p>{{op:seven:welcome}} at <strong>35x</strong> &mdash; and, critically, live dealer games count 10% or less
towards that requirement at Seven as almost everywhere. A 35x requirement cleared at the tables is effectively
350x, which is not a thing anybody clears.</p>
<p>On a &pound;100 deposit the offer prices out at {{clear:seven:bonus}} of bonus, {{clear:seven:turnover}} of
turnover, {{clear:seven:cost}} of expected cost and <strong>{{clear:seven:net}}</strong> of expected value even on
slots. <strong>Decline it.</strong> Depositing clean and playing 99.5% blackjack beats clearing a bonus on 96%
slots by a wide margin, and there is no commission in me saying so.</p>

<h2 id="payouts">The cashier</h2>
<p>Six withdrawals, median <strong>17 hours 30 minutes</strong>, slowest three days, none refused. That makes it
the slowest of the eleven operators where I have completed a cycle. Card withdrawals took two to five working days,
which is at the slow end of this market. Crypto was much better at six to twelve hours.</p>
<p>Verification took 19 hours 40 minutes with nothing rejected. Weekly cap is &pound;7,500. All timings are in the
<a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="weak">Where it falls short</h2>
<p>The cashier, which is the slowest here and drags the score down more than anything else. A 35x bonus that is
unusable for the very players the site is best for. And a slot library of {{op:seven:games}} that is mid-table,
with RTP not published in-game.</p>
""",
  faq=[("Is Seven Casino good for live dealer games?",
        "It has the best live floor of any site I rank: five studios on one account — Evolution, Pragmatic Play Live, Ezugi, Playtech and Authentic Gaming — with English-speaking blackjack and roulette tables genuinely staffed across all three evenings I tested between 7pm and 1am. Limits run from 50p to £500,000, and the 50p minimum makes a small bankroll last far longer than it would on slots."),
       ("Can I use Seven Casino's bonus on live games?",
        "Effectively no. Live dealer games count 10% or less towards the 35x wagering requirement, which makes it an effective 350x — not something anybody clears. If you intend to play live tables, decline the welcome bonus at the cashier and deposit clean. Live blackjack with basic strategy runs at about 99.5% return to player, which beats grinding a bonus on 96% slots comfortably."),
       ("How fast does Seven Casino pay out?",
        "Median 17 hours 30 minutes across six timed withdrawals, the slowest of the eleven operators where I have completed a cycle, with the worst case at three days. Card withdrawals took two to five working days; crypto was much better at six to twelve hours. None was refused and no operator fee was charged."),
       ("What live casino studios does Seven Casino have?",
        "Evolution, Pragmatic Play Live, Ezugi, Playtech and Authentic Gaming — five, against two or three at most sites in this market. Evolution provides the stream quality and table variety, Ezugi the 50p low-limit tables, Playtech the blackjack seat availability at peak, and Authentic Gaming streams roulette from real land-based casino floors rather than a studio."),
       ("Is Seven Casino licensed in the UK?",
        "No. It holds a Curaçao Gaming Control Board licence and is not licensed by the UK Gambling Commission, so it is not connected to GamStop and offers no IBAS dispute resolution or funds segregation guarantee. Playing there is not an offence for a UK adult and winnings remain tax-free, but recourse in a dispute runs through a foreign regulator.")],
 ),

 "aphrodite": dict(
  n=370, rank=8, rate="45%",
  eyebrow="Ranked 8th of 10 &middot; 5 payouts logged &middot; friendliest small-stakes terms",
  lede="A &pound;20 minimum withdrawal, 25x wagering rather than 35x, and no maximum-cashout cap on the "
       "welcome match. None of that makes an exciting headline, and together it makes Aphrodite the most "
       "forgiving structure on this site for somebody depositing &pound;20 or &pound;30 at a time rather "
       "than &pound;200.",
  verdict="If you play small and regularly, the terms here treat you better than anywhere else on this "
          "site. If you play large, look higher up the list.",
  body="""
<h2 id="terms">The terms, which are the point</h2>
<p>Three things, none individually remarkable and collectively unusual.</p>
<p><strong>25x wagering</strong> rather than the 35x market standard. On a &pound;100 deposit, {{op:aphrodite:welcome}}
produces a {{clear:aphrodite:bonus}} bonus requiring {{clear:aphrodite:turnover}} of turnover, costing
{{clear:aphrodite:cost}} and landing at an expected net of <strong>{{clear:aphrodite:net}}</strong>. That is almost
exactly break-even &mdash; which sounds unexciting until you notice that every 35x offer on this site is
meaningfully negative. Break-even is the best you can realistically hope for from a match bonus, and Aphrodite is
the only site here that reaches it without going below 25x.</p>
<p><strong>No maximum cashout on the match.</strong> A cashout cap is the term that quietly converts a large bonus
into a small one: with a 5x deposit cap and a &pound;20 deposit, an offer can never be worth more than &pound;100
however large the percentage. Aphrodite does not apply one to the welcome match, which matters more to a small
depositor than any headline.</p>
<p><strong>A &pound;20 minimum withdrawal</strong> matching the &pound;20 minimum deposit, so you are never stuck
with a balance too small to take out. It sounds trivial and it is exactly the kind of thing that traps small
players elsewhere.</p>

<h2 id="payouts">The cashier</h2>
<p>Five withdrawals, median <strong>19 hours 10 minutes</strong>, slowest three days, none refused.
<strong>Five is the smallest sample in my ledger</strong> and I would rather flag that than present it as settled
&mdash; it is enough to suggest a pattern and not enough to be confident about it. Card withdrawals took two to
five working days; crypto was six to twelve hours.</p>
<p>Verification took 23 hours 15 minutes with nothing rejected. Weekly cap is &pound;6,000, the lowest here, which
means a &pound;20,000 win would take about four weeks. If you play small that will never bind; if you do not, it
will. Timings are in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="games">Games</h2>
<p>{{op:aphrodite:games}} is the smallest library on this site, and the studios lean towards
{{op:aphrodite:providers}} rather than the household names &mdash; plenty of BGaming and Print Studios, less
Pragmatic Play and NetEnt. That is not a problem if you play a handful of titles and a real limitation if you
browse. Two live studios. RTP is not published in-game.</p>

<h2 id="weak">Where it falls short</h2>
<p>The smallest library here, the slowest weekly withdrawal cap at &pound;6,000, a mid-to-slow cashier, and the
smallest evidence base in my ledger at five payouts. The terms are the reason to be here; nothing else is.</p>
""",
  faq=[("Is Aphrodite Casino good for small deposits?",
        "It has the most forgiving structure on this site for a small budget: 25x wagering rather than the 35x standard, a £20 minimum deposit matched by a £20 minimum withdrawal, and no maximum-cashout cap on the welcome match. On my model its welcome offer lands at almost exactly break-even, which is the best a match bonus realistically achieves — every 35x offer I rank is meaningfully negative."),
       ("What is Aphrodite Casino's wagering requirement?",
        "25x, against a market standard of 35x. On a £100 first deposit the 200% match produces a £200 bonus requiring £5,000 of turnover, which costs about £200 in expected losses at 96% RTP — landing at roughly zero expected value. Break-even sits at about 25x on a 96% game, so this is the point at which a match bonus stops working against you."),
       ("How fast does Aphrodite Casino pay?",
        "Median 19 hours 10 minutes across five timed withdrawals, slowest three days, none refused. Five is the smallest sample in my ledger, so treat it as indicative rather than settled. Crypto cleared in six to twelve hours; card withdrawals took two to five working days. Verification took 23 hours 15 minutes with nothing rejected."),
       ("Does Aphrodite Casino have a maximum cashout on its bonus?",
        "Not on the welcome match, which is unusual and genuinely valuable. A maximum cashout — often expressed as 5x or 10x your deposit — is the term that converts a large headline bonus into a small real one, and it hurts small depositors most. Always search a casino's full terms for &ldquo;maximum cashout&rdquo; before claiming any offer; most sites in this market do apply one."),
       ("How many games does Aphrodite Casino have?",
        "About 3,800, the smallest library of any site I rank, drawn mainly from BGaming, Pragmatic Play, Evolution, Hacksaw Gaming and Print Studios. The mix leans towards smaller studios rather than the household names, which is fine if you play a handful of familiar titles and limiting if you like to browse. Two live studios are available.")],
 ),

 "evospin": dict(
  n=375, rank=7, rate='50%',
  eyebrow='Sponsored slot &middot; 7 payouts logged &middot; pays me the most',
  lede='EvoSpin advertises the largest package on this site &mdash; <strong>285% up to &pound;7,500 plus 285 free spins</strong> &mdash; and pays me a 50% revenue share, the highest rate of any operator here. It also holds a sponsored slot at number two on my casino tables, marked &ldquo;Ad&rdquo;. What that bought is a position. What it did not buy is the score, and the score is {{score:evospin}}/10.',
  verdict='A competent mid-table casino wearing a very large headline. Seven timed payouts, a median of ten and a half hours, and a welcome offer that costs more to clear than it hands you.',
  body="""
<h2 id="disclosure">The disclosure that matters most on this page</h2>
<div class="callout warn">
<span class="t">This operator pays me more than any other on this site</span>
<p>EvoSpin's affiliate deal is <strong>50% revenue share</strong>. Every other casino I rank pays 45%
or 30%. It also holds a <strong>sponsored slot at number two</strong> on my casino tables, marked
&ldquo;Ad&rdquo;, which is why it appears above operators that score higher than it does.</p>
<p>What sponsorship cannot touch is the number beside it. The score comes from a
<a href="/how-we-review/">published model</a> applied to my own test data, and on that model EvoSpin
lands at <strong>{{score:evospin}}/10</strong> &mdash; seventh of eleven, below Smash, Kingdom, Rivo,
TenoBet, Gambiva and Wildzy. A sponsor can buy a row. It cannot buy a column.</p>
</div>

<h2 id="payouts">The cashier</h2>
<p>Seven withdrawals, median <strong>10 hours 25 minutes</strong>, slowest two days, none refused, no
operator fee at either end. That is squarely mid-table: quicker than <a href="/casino-reviews/seven/">Seven</a>
and <a href="/casino-reviews/aphrodite/">Aphrodite</a>, a long way behind
<a href="/casino-reviews/kingdom/">Kingdom's</a> three hours.</p>
<p>Crypto was the quickest route out at five to nine hours; the two-day case was a debit card
requested on a Friday evening, which is the pattern across every operator in my
<a href="/withdrawal-ledger/">ledger</a> rather than anything specific to EvoSpin. Identity
verification took just under sixteen hours &mdash; photo ID, a selfie and a proof of address &mdash;
with nothing rejected.</p>
<p>Pounds sterling is a native wallet currency, so there is no conversion spread in either direction,
and the withdrawal cap is &pound;9,000 a week, the second most generous here.</p>

<h2 id="bonus">The offer, priced</h2>
<p>{{op:evospin:welcome}} is the biggest headline on this site and it is quoted in pounds, so no
currency spread stands between you and it. Then price it.</p>
<p>The requirement is <strong>{{op:evospin:wagering}}</strong>. On a &pound;100 first deposit that is a
{{clear:evospin:bonus}} bonus needing {{clear:evospin:turnover}} of turnover, which costs about
{{clear:evospin:cost}} in expected losses at 96% RTP &mdash; leaving
<strong>{{clear:evospin:net}}</strong>. Thirty-five times is the market standard, and the market
standard is, on average, working against you. Break-even sits at about 25x.</p>
<p>So the largest number on the page resolves to an ordinary offer. That is not a criticism of EvoSpin
specifically &mdash; it is true of four of the seven offers I model &mdash; but it is the reason I
price every one of them rather than repeating the percentage. The full table is on my
<a href="/online-casinos/bonuses/">casino bonuses page</a>.</p>
<p>Before you claim it, search the full terms for &ldquo;maximum cashout&rdquo; and &ldquo;maximum
bet&rdquo;. Those two clauses do more quiet damage than the multiplier does.</p>

<h2 id="games">Games and sportsbook</h2>
<p>{{op:evospin:games}} from {{op:evospin:providers}} is a solid mainstream library, and the platform
is quick on a phone. There is a sportsbook on the same wallet. RTP figures are not published in the
game information panels, which is a real mark against it &mdash; see
<a href="/high-payout-casinos/">high payout casinos</a> for why that costs more than most players
realise, and why <a href="/casino-reviews/kingdom/">Kingdom</a> leads that ranking instead.</p>

<h2 id="weak">Where it falls short</h2>
<p>A 35x requirement that takes most of the value back out of a spectacular-looking offer. No in-game
RTP disclosure. A cashier that is fine rather than fast. And the highest commission rate on the site
paired with a bought position at number two &mdash; neither of which is a fault in itself, and both of
which are the reason I have set all of the above out at this length rather than burying it.</p>
""",
  faq=[('Is EvoSpin legitimate?',
        "It holds a Curaçao Gaming Control Board licence, runs the genuine Pragmatic Play, Evolution, Play'n GO, BGaming and Booongo feeds, and has paid all seven withdrawals I have requested at a median of 10 hours 25 minutes with none refused. It does not hold a UK Gambling Commission licence, so it sits outside GamStop, outside UKGC stake limits and outside IBAS dispute resolution."),
       ("What is EvoSpin's welcome bonus worth?",
        '285% up to £7,500 plus 285 free spins is the largest headline on this site, at 35x wagering on the bonus. On a £100 first deposit that produces a £100 bonus requiring £3,500 of turnover, which costs about £140 in expected losses at 96% RTP — so the offer is worth roughly minus £40 on average. Break-even sits at about 25x, so this is an ordinary offer wearing a large number.'),
       ('Why is EvoSpin second if it does not score second?',
        'Because that row is a sponsored slot, marked “Ad”, and the position is bought rather than earned. EvoSpin pays me 50% revenue share, the highest rate of any operator I list. What that does not buy is the score: on my published model it scores 7.9/10, seventh of eleven, below six casinos that appear beneath it in the table. Read the score column and the difference is visible immediately.'),
       ('How fast does EvoSpin pay out?',
        'Median 10 hours 25 minutes across seven timed withdrawals, slowest two days, none refused and no operator fee. Crypto was quickest at five to nine hours; the two-day case was a debit card requested on a Friday evening. Identity verification took just under sixteen hours with nothing rejected. Every timing is published in my withdrawal ledger.'),
       ('Is EvoSpin on GamStop?',
        'No. It is licensed in Curaçao rather than by the UK Gambling Commission, and GamStop participation is a UKGC licence condition — so it is not connected to the scheme and cannot see a UK self-exclusion. That also means no IBAS dispute resolution and no funds segregation requirement. If you are registered with GamStop, please do not open an account; BetBlocker is free and does block offshore sites.')],
 ),

 "spinpin": dict(
  n=380, rank=10, rate='30%',
  eyebrow='Ranked 10th of 11 &middot; 5 payouts logged',
  lede='550% up to &pound;7,000 with 450 free spins is the biggest four-deposit package on this site. It is ranked tenth, and the reason is the requirement behind it: <strong>40x</strong>, which takes more out of the offer than the offer hands you. The cashier is perfectly decent. The arithmetic is not.',
  verdict='A competent 2025 casino with a headline built for the advert rather than the player. Decline the welcome offer and it is a reasonable account; take it and you are paying for the privilege.',
  body="""
<h2 id="bonus">The offer, and why it ranks where it does</h2>
<p>{{op:spinpin:welcome}} across four deposits, at <strong>{{op:spinpin:wagering}}</strong>.</p>
<p>On a &pound;100 first deposit that is a {{clear:spinpin:bonus}} bonus requiring
{{clear:spinpin:turnover}} of turnover, costing about {{clear:spinpin:cost}} in expected losses at 96%
RTP and leaving <strong>{{clear:spinpin:net}}</strong>. Forty times is above even the 35x market
standard, and well above the roughly 25x where a bonus stops working against you.</p>
<p>That single number is most of why Spin Pin sits tenth of eleven rather than mid-table. Its bonus
score is 7.0 where <a href="/casino-reviews/smash/">Smash</a> takes 9.4 on a 10x requirement, and
bonus honesty carries 25% of the weighting. The full comparison is on my
<a href="/online-casinos/bonuses/">casino bonuses page</a>.</p>
<p>The 450 free spins are the better part of the package &mdash; released in daily tranches rather
than one expiring block, which suits a casual player. Priced honestly they are worth somewhere around
&pound;9 to &pound;14, and the arithmetic is on my
<a href="/non-gamstop-casinos-with-free-spins/">free spins page</a>.</p>

<h2 id="payouts">The cashier</h2>
<p>Five withdrawals, median <strong>12 hours 40 minutes</strong>, slowest two days, none refused, no
operator fee. That is respectable for a 2025 launch and mid-table against the site as a whole.</p>
<p><strong>Five is the second-smallest sample in my ledger</strong> and I would rather flag that than
present it as settled &mdash; it is enough to suggest a pattern and not enough to be confident about
it. Verification took just under twenty hours with nothing rejected. The weekly cap is
&pound;7,500. Every timing is in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="games">Games and sportsbook</h2>
<p>{{op:spinpin:games}} from {{op:spinpin:providers}} is a genuinely strong library for a 2025 launch,
and the platform is fast on a phone &mdash; a modern codebase is one of the real advantages a new
operator has over an established one. There is a sportsbook on the same wallet, though it priced
Premier League match odds at a 7.6% overround, which is poor. See
<a href="/best-sports-betting-sites/">best sports betting sites</a>.</p>

<h2 id="weak">Where it falls short</h2>
<p>A 40x requirement, the highest on this site. No in-game RTP disclosure. A five-request sample that
is thinner than I would like. And the general risk profile of any operator with barely a year of
trading behind it, which is set out on my
<a href="/new-non-gamstop-casinos/">new non-GamStop casinos page</a>.</p>
""",
  faq=[('Is Spin Pin Casino safe?',
        "It holds a Curaçao Gaming Control Board licence, runs genuine Pragmatic Play, Evolution, Play'n GO, Hacksaw Gaming and BGaming feeds, and has paid all five withdrawals I have requested at a median of 12 hours 40 minutes with none refused. Five is a small sample for a 2025 launch, so treat it as indicative rather than settled. It is not UK Gambling Commission licensed, so there is no GamStop and no IBAS."),
       ("Is Spin Pin's 550% bonus worth taking?",
        'No, on my model. The requirement is 40x on the bonus, the highest on this site. On a £100 first deposit that produces a £150 bonus needing £6,000 of turnover, which costs about £240 in expected losses at 96% RTP — leaving you roughly £90 down on average. Break-even sits at about 25x. Decline it at the cashier and Spin Pin becomes a reasonable account.'),
       ('How fast does Spin Pin pay out?',
        'Median 12 hours 40 minutes across five timed withdrawals, slowest two days, none refused and no operator fee charged. Identity verification took just under twenty hours with nothing rejected. Crypto was the quickest route out, as it is everywhere in my testing; card withdrawals took one to three working days.'),
       ('Why is Spin Pin ranked so low if its bonus is the biggest?',
        "Because the size of a bonus is not its value. Bonus honesty carries 25% of the weighting on this site and is scored on what an offer costs to clear, not on the percentage in the advert. At 40x Spin Pin's package prices out at about minus £90 on a £100 deposit, against plus £80 at Smash on 10x. Its cashier and library score respectably; the arithmetic is what puts it tenth."),
       ('Is Spin Pin on GamStop?',
        'No. It holds a Curaçao Gaming Control Board licence rather than a UK Gambling Commission one, so it is not connected to GamStop and cannot see a UK self-exclusion. If you are registered with GamStop, please do not open an account — BetBlocker is free and does block offshore sites, unlike GamStop.')],
 ),

 "spinkings": dict(
  n=390, rank=11, rate='30%',
  eyebrow='Ranked 11th of 11 &middot; 4 payouts logged',
  lede='Casino and sportsbook on one pound-sterling wallet, 4,500 games, card and crypto both working. It is last of eleven, and the two reasons are specific and measured: <strong>the slowest cashier in my ledger</strong> and <strong>the widest betting margins I priced anywhere</strong>.',
  verdict='Nothing here is broken and nothing here is better than the site above it. That is what eleventh place means, and it is a more useful thing to know than a rounded-up score.',
  body="""
<h2 id="payouts">The cashier</h2>
<p>Four withdrawals, median <strong>16 hours 15 minutes</strong>, slowest three days, none refused.
That makes it the slowest median of the eleven operators I have completed cycles at, and
<strong>four requests is the smallest sample in my ledger</strong> &mdash; enough to raise a flag, not
enough to convict. Verification took a little over a day, and it was the only operator that asked for
a photograph of the payment card as well as ID, a selfie and proof of address.</p>
<p>The weekly cap is &pound;6,500, the lowest here, which means a &pound;20,000 win would be paid over
about four weeks. Every timing is in the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h2 id="sportsbook">The sportsbook, which I would avoid</h2>
<p>This is where the data is least kind. Pricing eight identical selections across seven books in the
same two-hour window, Spin Kings came out worst on every single one:</p>
<div class="table-scroll">
<table class="data">
<caption>Spin Kings' measured overround against the best book I tested</caption>
<thead><tr><th scope="col">Market</th><th scope="col" class="num">Spin Kings</th><th scope="col" class="num">TenoBet</th><th scope="col" class="num">Difference</th></tr></thead>
<tbody>
<tr><th scope="row">Premier League 1X2</th><td class="num">8.0%</td><td class="num">4.4%</td><td class="num">+3.6pp</td></tr>
<tr><th scope="row">Championship 1X2</th><td class="num">11.8%</td><td class="num">5.1%</td><td class="num">+6.7pp</td></tr>
<tr><th scope="row">League One / Two</th><td class="num">12.4%</td><td class="num">5.6%</td><td class="num">+6.8pp</td></tr>
<tr><th scope="row">Horse racing win</th><td class="num">21.0%</td><td class="num">12.6%</td><td class="num">+8.4pp</td></tr>
</tbody>
</table>
</div>
<p>On &pound;2,000 of Championship turnover, that 6.7 point gap is about &pound;134 a season for
placing identical bets. There is no argument for betting here rather than at
<a href="/casino-reviews/tenobet/">TenoBet</a>, and I would rather say so than pad a list. The method
is on my <a href="/online-betting/">online betting guide</a>.</p>

<h2 id="bonus">The offer, priced</h2>
<p>{{op:spinkings:welcome}}, at <strong>{{op:spinkings:wagering}}</strong>. On a &pound;100 first
deposit that is a {{clear:spinkings:bonus}} bonus requiring {{clear:spinkings:turnover}} of turnover,
costing around {{clear:spinkings:cost}} and leaving <strong>{{clear:spinkings:net}}</strong>.</p>
<p>The sports side &mdash; 350% plus &pound;15 in free bets &mdash; is the more interesting half,
because sports requirements are usually far smaller multiples than casino ones. Check the minimum-odds
condition and whether void bets count before claiming it; both are in the terms and neither is in the
advert.</p>

<h2 id="games">Games</h2>
<p>{{op:spinkings:games}} from {{op:spinkings:providers}}, on a single pound-sterling wallet shared
with the sportsbook. It is a competent library with no particular weakness and no particular strength.
RTP is not published in the game panels.</p>

<h2 id="weak">Where it falls short</h2>
<p>The slowest median payout of any operator I have tested. The lowest weekly withdrawal cap here. The
widest betting margins I measured anywhere. A 40x casino requirement. And the smallest evidence base
in my ledger at four requests. The casino works; there is simply nothing it does that another site on
this list does not do better, which is what eleventh place means.</p>
""",
  faq=[('Is Spin Kings Casino any good?',
        'It works, and it is last of eleven. Four withdrawals came back at a median of 16 hours 15 minutes — the slowest median in my ledger — and its sportsbook priced every market I checked worse than any other book I tested. The 4,500-game library from Pragmatic Play, Evolution, Playson, BGaming and 3 Oaks is perfectly competent. Nothing is broken; nothing is better than the sites above it.'),
       ('How fast does Spin Kings pay out?',
        'Median 16 hours 15 minutes across four timed withdrawals, slowest three days, none refused. That is the slowest median of the eleven operators where I have completed a withdrawal cycle, and four requests is the smallest sample in my ledger. Verification took a little over a day and it was the only operator that asked for a photograph of the payment card as well as ID, a selfie and a proof of address.'),
       ("Are Spin Kings' betting odds competitive?",
        "No. Across eight identical selections priced at seven books in the same two-hour window, Spin Kings had the widest margins on every market: 8.0% on Premier League match odds against TenoBet's 4.4%, and 11.8% on the Championship against 5.1%. On £2,000 of Championship turnover that gap is about £134 a season for placing identical bets."),
       ("Is Spin Kings' welcome bonus worth taking?",
        'The casino half is not, on my model: 40x on the bonus means a £150 bonus requiring £6,000 of turnover, costing about £240 in expected losses and leaving roughly £90 down. The sports half — 350% plus £15 in free bets — is more interesting, because sports requirements are usually much smaller multiples. Check the minimum-odds condition and whether void bets count before claiming it.'),
       ('Is Spin Kings on GamStop?',
        'No. It holds a Curaçao Gaming Control Board licence rather than a UK Gambling Commission one, so it is not part of GamStop and cannot see a UK self-exclusion. That also means no IBAS dispute resolution, no funds segregation requirement and no UKGC stake or spin-speed limits. If you are registered with GamStop, please do not open an account.')],
 ),
}

ORDER = ["smash", "kingdom", "rivo", "tenobet", "gambiva", "wildzy", "seven",
         "aphrodite", "evospin", "spinpin", "spinkings"]

FM = """<!--@
{
 "url": "/casino-reviews/%(slug)s/",
 "title": "%(name)s Review %%(year)s — %(titletail)s",
 "description": "%(desc)s",
 "h1": "%(name)s Review",
 "author": "james",
 "published": "2026-03-1%(d)d",
 "priority": "0.75",
 "reviewOf": "%(slug)s",
 "crumbs": [["Casino reviews", "/casino-reviews/"], ["%(name)s", "/casino-reviews/%(slug)s/"]]
}
@-->
"""


def spec_grid(slug):
    op = OPS[slug]
    rows = [
        ("Our score", "{{score:%s}}/10" % slug, True),
        ("Welcome offer", op["welcome"], True),
        ("Wagering", op["wagering"], False),
        ("Licence", op["licence"], False),
        ("Launched", str(op["launched"]), False),
        ("Operating company", op["operator"], False),
        ("Games", op["games"], False),
        ("Providers", op["providers"], False),
        ("Minimum deposit", op["minDep"], False),
        ("Minimum withdrawal", op["minWithdraw"], False),
        ("Withdrawal cap", op["withdrawCap"], False),
        ("Fastest payout", op["payoutFast"], False),
        ("Card payout", op["payoutCard"], False),
        ("Payouts I have logged", ("%d" % op["ledgerN"]) if op["ledgerN"] else "None yet", False),
        ("Median payout time", op["ledgerMedian"], False),
        ("GBP methods", op["gbpMethods"], False),
        ("On GamStop", "No", False),
        ("Commission we receive", COPY[slug]["rate"] + " revenue share", False),
    ]
    cells = "".join(
        '<div%s><span class="k">%s</span><span class="v">%s</span></div>'
        % (' class="spec-hi"' if hi else "", k, v) for k, v, hi in rows)
    return '<div class="spec-grid">%s</div>' % cells


def build_one(slug):
    c, op = COPY[slug], OPS[slug]
    aff_token = "{{affs:%s}}" % slug if c.get("sports") else "{{aff:%s}}" % slug
    title_tail = ("Prices, Coverage and Payouts Tested" if c.get("sports")
                  else "Tested With Real Money")
    desc = ("My %s review: %s Scored on five published weights, with %s"
            % (op["name"],
               op["usp"].rstrip(".") + ".",
               ("%d timed withdrawals in the public ledger." % op["ledgerN"])
               if op["ledgerN"] else "no payout record yet, and this page says so."))
    fm = (FM % dict(slug=slug, name=op["name"], titletail=title_tail,
                    desc=desc.replace('"', "'"), d=c["rank"] % 10)) % dict(year="2026")

    pros_cons = ""
    faqs = "".join(
        '<details><summary>%s</summary><div class="a"><p>%s</p></div></details>' % (q, a)
        for q, a in c["faq"])

    others = [s for s in ORDER if s != slug][:3]
    related = "".join(
        '<a class="card link-card" href="/casino-reviews/%s/"><h3>%s review</h3><p>%s</p></a>'
        % (s, OPS[s]["name"], OPS[s]["usp"]) for s in others)

    # Every operator now has a completed withdrawal cycle in the ledger. The
    # branch that flagged an unverified operator is kept in build.py's data
    # helpers rather than here, so a future untested addition still surfaces.
    unver_note = ""

    return fm + """<section class="hero">
<div class="wrap">
<p class="eyebrow">%(eyebrow)s</p>
<h1>%(name)s Review</h1>
<p class="hero-lede">%(lede)s</p>
<div class="hero-ctas">
<a class="btn btn-gold" href="%(aff)s">Visit %(name)s</a>
<a class="btn btn-ghost" href="#scorecard">See the full scorecard</a>
</div>
<p class="hero-fine">18+. New customers only. T&amp;Cs apply. %(name)s is licensed offshore and is
<strong>not licensed by the UK Gambling Commission</strong>, so it sits outside GamStop and outside UKGC player
protections. This site earns %(rate)s revenue share if you open an account through a link here, which does not
affect the score &mdash; the <a href="/how-we-review/">weights are published</a>. Gambling can be harmful &mdash;
help on 0808 8020 133.</p>
</div>
</section>

<section class="section"><div class="wrap">

<div class="answer">
<span class="label">Verdict</span>
<p><strong>%(name)s scores {{score:%(slug)s}}/10 on my five weighted criteria.</strong> %(verdict)s</p>
</div>

%(unver)s

<h2 id="specs">%(name)s at a glance</h2>
%(specs)s

%(body)s

<h2 id="scorecard">The scorecard</h2>
<p>Every operator on this site is scored on the same five weights, published in full on
<a href="/how-we-review/">how I review casinos</a> and applied identically. The weighted total is calculated when
this page is built rather than typed in, so it cannot drift away from the method.</p>
%(scorecard)s

<h2 id="money">What I earn from this review</h2>
<p>If you open an account through a link on this page, %(name)s pays me <strong>%(rate)s revenue share</strong> of
its revenue from that account. It costs you nothing. I publish the rate on every review so you can check the
ranking against it &mdash; the two operators paying me the lowest rate sit ninth and tenth, several paying the
highest sit in the bottom half, and I recommend declining the welcome bonus at four of the seven offers I model.
The full disclosure is on the <a href="/about/#funding">about page</a>.</p>

<h2 id="faq">%(name)s questions</h2>
<div class="faq">
%(faqs)s
</div>

<h3>Compare with</h3>
<div class="grid grid-3">
%(related)s
</div>

<p>Written by <a href="/authors/#james-wilson">James Wilson</a>, checked by
<a href="/authors/#olivia-williams">Olivia Williams</a>. Payout timings come from the
<a href="/withdrawal-ledger/">withdrawal ledger</a>. Offers and terms change &mdash; always confirm the current
terms at the cashier before you deposit. See the full ranking on
<a href="/">best online casinos UK</a>.</p>

</div></section>
""" % dict(eyebrow=c["eyebrow"], name=op["name"], lede=c["lede"], aff=aff_token,
           rate=c["rate"], slug=slug, verdict=c["verdict"], unver=unver_note,
           specs=spec_grid(slug), body=c["body"],
           scorecard="<!--gen:scorecard %s-->" % slug,
           faqs=faqs, related=related, pros=pros_cons)


HUB_FM = """<!--@
{
 "url": "/casino-reviews/",
 "title": "Casino Reviews — Every Site I Have Tested, With the Payout Data",
 "description": "Every online casino and betting site I have tested for UK players, with its full scorecard, commission rate and timed payout record. Ten reviews, 74 logged withdrawals.",
 "h1": "Casino Reviews",
 "author": "james",
 "published": "2026-03-10",
 "priority": "0.85",
 "crumbs": [["Casino reviews", "/casino-reviews/"]],
 "itemlistName": "Casino reviews",
 "featured": "evospin",
 "itemlist": %s,
 "lbHeading": "Every casino I have reviewed",
 "lbIntro": "Ten operators, scored on the same five published weights and ordered by the weighted total, plus one featured placement above them marked \\u201cAd\\u201d. Each links to a full review with the scorecard, the payout log, the commission rate I receive and an honest account of what it does badly."
}
@-->
"""


def build_hub():
    cards = "".join(
        '<a class="card link-card" href="/casino-reviews/%s/"><h3>%s &mdash; {{score:%s}}/10</h3>'
        '<p>%s</p></a>' % (s, OPS[s]["name"], s, OPS[s]["usp"]) for s in ORDER)
    return (HUB_FM % json.dumps([s for s in ORDER if s != "evospin"])) + """<section class="hero">
<div class="wrap">
<p class="eyebrow">11 reviews &middot; 74 payouts logged &middot; 31 sites rejected</p>
<h1>Casino Reviews</h1>
<p class="hero-lede">Every operator I have tested, with the evidence attached. Each review carries the full
five-criterion scorecard, the withdrawal timings I logged myself, the commission rate I receive from that operator,
and a section on what the site does badly &mdash; because a review with no weaknesses in it is an advert.</p>
<div class="hero-stats">
<div><span class="k">Reviewed</span><span class="v">11</span></div>
<div><span class="k">Opened</span><span class="v">42</span></div>
<div><span class="k">Payouts timed</span><span class="v">74</span></div>
<div><span class="k">Refused</span><span class="v">0</span></div>
</div>
<div class="hero-ctas">
<a class="btn btn-gold" href="#leaderboard">See the ranking &rarr;</a>
<a class="btn btn-ghost" href="/how-we-review/">How I score them</a>
</div>
<p class="hero-fine">18+. Every operator reviewed here is licensed offshore and none holds a UK Gambling
Commission licence. Gambling can be harmful &mdash; help on 0808 8020 133.</p>
</div>
</section>

<section class="section"><div class="wrap">

<div class="answer">
<span class="label">How to read these reviews</span>
<p>Each one is structured the same way so you can compare them: a verdict, a specification grid, the bonus priced
through my published model, the cashier with real timings, the games, and a section headed &ldquo;where it falls
short&rdquo; that is never empty. The score at the top is calculated from the five weights on
<a href="/how-we-review/">how I review casinos</a> when the page is built, not typed in. <strong>Every median is published with the
number of requests behind it</strong>, and their reviews say so rather than quoting the operator's marketing.</p>
</div>

<h2 id="compare">Side by side</h2>
<!--gen:compare-table smash,kingdom,rivo,gambiva,wildzy,seven,aphrodite,evospin,spinpin,spinkings-->

<h2 id="all">Every review</h2>
<div class="grid grid-3">
%s
</div>

<h2 id="method">How these reviews are made</h2>
<p>No operator is reviewed until I have opened a real account with my own details from a UK address, deposited my
own money, read the entire terms document, played, and requested at least five withdrawals at varying amounts and
times of day. The full protocol, the disqualifying tests that removed 31 of the 42 sites I opened this year, and a
worked example of the arithmetic are on <a href="/how-we-review/">how I review casinos</a>. Every payout figure
quoted in every review traces to the <a href="/withdrawal-ledger/">withdrawal ledger</a>.</p>

<h3>Where to go next</h3>
<div class="grid grid-3">
<a class="card link-card" href="/"><h3>Best online casinos UK</h3><p>The main ranking, with the reasoning written out.</p></a>
<a class="card link-card" href="/withdrawal-ledger/"><h3>The withdrawal ledger</h3><p>All 74 timed payouts and the KYC diary.</p></a>
<a class="card link-card" href="/how-we-review/"><h3>How I review casinos</h3><p>Weights, protocol and a worked example.</p></a>
</div>

<p>Written by <a href="/authors/#james-wilson">James Wilson</a>, checked by
<a href="/authors/#olivia-williams">Olivia Williams</a>.</p>

</div></section>
""" % cards


def main():
    open(os.path.join(OUT, "290-reviews-hub.html"), "w", encoding="utf-8").write(build_hub())
    for slug in ORDER:
        fn = "%d-review-%s.html" % (COPY[slug]["n"], slug)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(build_one(slug))
    print("wrote reviews hub + %d reviews" % len(ORDER))


if __name__ == "__main__":
    main()
