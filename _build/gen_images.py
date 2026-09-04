#!/usr/bin/env python3
"""Generates every image the template references.

  * the favicon set at root paths — 48/96/144/192 as the brief requires, plus
    16/32/512, an .ico and an apple-touch-icon;
  * the SVG favicon, which is also the header and footer brand mark;
  * the 400x120 organisation logo referenced by Organization schema;
  * the 1200x630 Open Graph card;
  * author avatars.

Author avatars are real photographs committed to images/authors/ and are NOT
generated here — the avatar loop is deliberately empty so a run of this script
cannot overwrite them. Sizes: <slug>.jpg at 64px, <slug>@2x.jpg at 128px.

The mark is a casino chip. Palette is the stylesheet's --night / --amber so
nothing drifts.
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
os.makedirs(os.path.join(IMG, "authors"), exist_ok=True)

PLUM = (26, 11, 46, 255)      # --night
PLUM3 = (91, 42, 140, 255)    # --night-4
CITRINE = (245, 184, 65, 255) # --amber
WHITE = (255, 255, 255, 255)
MUT = (183, 166, 198, 255)


def font(sz, bold=True):
    for p in ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold
              else "/System/Library/Fonts/Supplemental/Georgia.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
              else "/System/Library/Fonts/Supplemental/Arial.ttf",
              "/System/Library/Fonts/Helvetica.ttc"):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, sz)
            except Exception:
                pass
    return ImageFont.load_default()


def centre(d, box, text, f, fill):
    x0, y0, x1, y1 = box
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text((x0 + (x1 - x0 - (r - l)) / 2 - l, y0 + (y1 - y0 - (b - t)) / 2 - t),
           text, font=f, fill=fill)


# ------------------------------------------------------------------ the mark
# A casino chip: an amber disc with six edge notches cut back to the ground, a
# plum gap ring and an amber centre. Chosen over anything card- or dice-shaped
# because a chip is a single circular silhouette — it still reads as a chip at
# 16px, where a spade turns to mush and a pair of dice turns to noise. The six
# notches are what make it a chip rather than a target, so they are cut wide
# enough to survive downsampling.
CHIP_ANGLES = (0, 60, 120, 180, 240, 300)


def draw_chip(d, cx, cy, r, ground):
    """A casino chip centred on (cx, cy) with outer radius r.

    The six edge spots are *inlaid* into the rim rather than cut through it, so
    the outer silhouette stays a clean circle. That is the whole difference
    between reading as a chip and reading as a cog — cut the spots through the
    edge and you get gear teeth. There is deliberately no inner ring or hub:
    the spots alone carry the chip, and less detail survives 16px better.
    """
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=CITRINE)
    for a in CHIP_ANGLES:
        t = math.radians(a)
        d.line([(cx + r * 0.64 * math.cos(t), cy + r * 0.64 * math.sin(t)),
                (cx + r * 0.93 * math.cos(t), cy + r * 0.93 * math.sin(t))],
               fill=ground, width=max(1, int(round(r * 0.30))))


# ------------------------------------------------------------------ favicon
S = 768
fav = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(fav)
d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * .23), fill=PLUM)
draw_chip(d, S / 2, S / 2, S * 0.325, PLUM)
for sz in (16, 32, 48, 96, 144, 192, 512):
    fav.resize((sz, sz), Image.LANCZOS).save(os.path.join(ROOT, "favicon-%dx%d.png" % (sz, sz)))
fav.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, "apple-touch-icon.png"))
fav.resize((64, 64), Image.LANCZOS).save(os.path.join(ROOT, "favicon.ico"),
                                         sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

# The SVG is the same geometry, and is what the header and footer brand render.
# Spots are stroked radial segments so they stay crisp at any size.
def _svg_spots(cx, cy, r, colour):
    out = []
    for a in CHIP_ANGLES:
        t = math.radians(a)
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                   'stroke-width="%.1f"/>'
                   % (cx + r * 0.64 * math.cos(t), cy + r * 0.64 * math.sin(t),
                      cx + r * 0.93 * math.cos(t), cy + r * 0.93 * math.sin(t),
                      colour, r * 0.30))
    return "".join(out)


open(os.path.join(ROOT, "favicon.svg"), "w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192" role="img" '
 'aria-label="Rhia Charles">'
 '<rect width="192" height="192" rx="44" fill="#1A0B2E"/>'
 '<circle cx="96" cy="96" r="62.4" fill="#F5B841"/>'
 + _svg_spots(96, 96, 62.4, "#1A0B2E") +
 '</svg>')

# ------------------------------------------------------------------ org logo
logo = Image.new("RGBA", (400, 120), PLUM)
d = ImageDraw.Draw(logo)
draw_chip(d, 56, 60, 34, PLUM)
d.text((104, 30), "Rhia Charles", font=font(31), fill=WHITE)
d.text((106, 72), "PROVEN PAYOUTS  \u00b7  NOT PROMISES", font=font(13, False), fill=CITRINE)
logo.save(os.path.join(IMG, "logo.png"))

# ------------------------------------------------------------------ OG card
og = Image.new("RGBA", (1200, 630), PLUM)
d = ImageDraw.Draw(og)
d.rectangle((0, 0, 1200, 9), fill=CITRINE)
draw_chip(d, 116, 112, 46, PLUM)
d.text((186, 82), "Rhia Charles", font=font(52), fill=WHITE)
d.text((70, 232), "Best Online Casinos UK", font=font(76), fill=WHITE)
d.text((70, 330), "Know which casinos actually pay", font=font(44), fill=CITRINE)
d.text((70, 412), "Every payout logged  \u00b7  Every bonus costed  \u00b7  Nothing bought",
       font=font(30, False), fill=MUT)
d.text((70, 546), "rhiacharles.co.uk   \u00b7   18+   \u00b7   Gamble responsibly   \u00b7   BeGambleAware.org",
       font=font(25, False), fill=MUT)
og.convert("RGB").save(os.path.join(IMG, "og-rhiacharles.jpg"), quality=88)

# ------------------------------------------------------------------ avatars
# Author photographs are real images supplied by the editorial desk and
# committed to images/authors/. Nothing is generated here — regenerating
# monograms would overwrite them. Sizes: <slug>.jpg at 64px, <slug>@2x.jpg at
# 128px, square.
AUTH = []

# ------------------------------------------------------------ operator wordmarks
# Only for brands with no supplied artwork in /logos. 300x128 so the 150x64 tile
# in the offer table renders at 2x. Every other operator has real vendor artwork.
os.makedirs(os.path.join(IMG, "casino-logos"), exist_ok=True)
# Every operator now has real vendor artwork in /logos, so no wordmark
# placeholders are generated. Add a brand here only if artwork is missing.
WORD = {}
for slug, (word, accent) in WORD.items():
    W, H = 300, 128
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dd = ImageDraw.Draw(c)
    dd.rounded_rectangle((0, 0, W - 1, H - 1), radius=18, fill=PLUM)
    dd.rectangle((0, 0, W, 6), fill=accent)
    centre(dd, (0, 6, W, H - 30), word, font(44), WHITE)
    centre(dd, (0, H - 42, W, H - 12), "CASINO", font(16, False), accent)
    c.save(os.path.join(IMG, "casino-logos", "%s.png" % slug))

print("images: favicons 16/32/48/96/144/192/512 + ico + apple-touch + svg, "
      "org logo, OG card, %d author avatars, %d wordmarks" % (len(AUTH), len(WORD)))
