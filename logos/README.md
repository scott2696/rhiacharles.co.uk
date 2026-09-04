# Brand logos

Master logo set for all sites under `MY_SITES/`. Copy this folder into a site as
`<site>/logos/` and reference images as `/logos/<file>`.

All artwork here is the **dark/coloured** variant, chosen to sit on the white
`.toplist-logo` tile (`background:#fff`). Note the vendors' folder naming is
inverted from what you'd expect — in the Brand Materials drive, "Light Logo"
means *for light backgrounds*, i.e. dark artwork. Variants were picked by
measuring mean luminance, not by folder name.

| Brand        | File                     | Notes                          |
|--------------|--------------------------|--------------------------------|
| Spinjo       | `spinjo.png`             |                                |
| Lucky Circus | `lucky-circus.jpg`       |                                |
| Lucky7even   | `lucky7even.jpg`         |                                |
| Lucky Vibe   | `lucky-vibe.jpg`         |                                |
| Roby Casino  | `roby-casino.jpg`        |                                |
| Spino        | `spino.jpg`              |                                |
| Ivibet       | `ivibet.png`             | casino logo                    |
| Ivibet       | `ivibet-sportsbook.jpg`  | use on sportsbook pages        |
| Hellspin     | `hellspin.jpg`           |                                |
| Slotgem      | `slotgem.jpg`            |                                |
| Bet&Play     | `betandplay.png`         |                                |
| Kingdom      | `kingdom.png`            | from Brand Materials drive     |
| MadCasino    | `madcasino.png`          | EN variant (RU also available) |
| Rivo         | `rivo.png`               | from Brand Materials drive     |
| Smash        | `smash.png`              | from Brand Materials drive     |
| Spin Pin     | `spinpin.png`            | wordmark recoloured to #111111 for the white tile |
| Spin Pin     | `spinpin-white.png`      | the vendor's original white wordmark, for dark backgrounds |
| Spin Kings   | `spinkings.png`          | dark artwork, use on the white tile |
| Spin Kings   | `spinkings-white.png`    | light artwork, for dark backgrounds only |
| Gambiva      | `gambiva.png`            | Brand Materials drive, Logo/PNG 420    |
| Wildzy       | `wildzy.png`             | Brand Materials drive, Logo/PNG 420    |
| Seven Casino | `seven.png`              | **Light** variant — the "dark" file omits the CASINO wordmark |
| Seven Casino | `seven-light.png`        | the vendor's "dark" file, for dark backgrounds |
| Aphrodite    | `aphrodite.png`          | **Light** variant — vendor naming is inverted |
| Aphrodite    | `aphrodite-light.png`    | the vendor's "dark" file, for dark backgrounds |
| TenoBet      | `tenobet.png`            | **Light** variant — vendor naming is inverted |
| TenoBet      | `tenobet-light.png`      | the vendor's "dark" file, for dark backgrounds |
| EvoSpin      | `evospin.png`            | supplied as a JPEG on a light-grey field; background removed, see below |

Vector originals for the four newest brands live in `svg/`. Prefer these where
the layout allows — they stay crisp at any size.

## Source

Master artwork lives in the shared **Brand Materials** Drive folder:
<https://drive.google.com/drive/folders/1cxtBhE3EP9XKcdP16dT8d4e-o1AgxUbz>

Structure is `Brand / Logo / PNG / [Dark|Light] / Brand_<width>.png`, plus a
matching `SVG` tree and a `Symbol` tree for the icon-only mark. Take the **420**
width — it is the largest supplied and downsamples cleanly to the 150x64 tile.

The folder is link-readable without signing in, so files can be pulled with
`curl -sL "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download"`,
and a folder can be listed as plain HTML via
`https://drive.google.com/embeddedfolderview?id=<FOLDER_ID>#list` — in that
listing, entries carrying a `/type/<mime>` icon are files and entries without
one are folders.

It also holds artwork for ~20 brands not currently on any site: Casineia,
Casinio, Chanze, Dracula, Gamblii, Gxmble, Hypersino, JinxCasino, Jokersino,
LuckiCasino, Luckzie, PalmCasino, PriveCasino, SlotHive, Slottio, SpinTime,
SpinToWin, Trixino, Tucan Casino, Wino, Winstler.

## Confirmed: the vendor's Dark/Light naming is inverted

Measured mean luminance of the opaque pixels in each 420px variant:

| Brand | vendor "dark" | vendor "light" | we use |
|---|---|---|---|
| Aphrodite | 201 (light artwork) | 142 (dark artwork) | **light** |
| TenoBet | 215 (light artwork) | 128 (dark artwork) | **light** |
| Seven | 126 | 95 | **light** — see below |

**Always eyeball the result as well as measuring.** Seven's two files both
measured dark-ish, but rendering them on the white tile showed the vendor's
"dark" file drops the CASINO wordmark entirely — it is set in white and simply
vanishes. Only the "light" file carries the full lockup.

## Spin Pin: wordmark recoloured

The vendor supplied only a dark-background lockup — coloured mark plus a white
`spinpin` wordmark that vanished on the white `.afl-chip`. Rather than keep a
one-off dark tile, the wordmark was recoloured to `#111111`.

The mark and the wordmark separate cleanly by column: coloured pixels end at
column 205, the wordmark starts at 208. Only near-white pixels (HSV saturation
< 0.30, value > 0.45) at x >= 207 were touched, so the orange spinner and its
specular highlights are untouched. Alpha was preserved per pixel, so the
antialiased edges survive. `spinpin-white.png` is the untouched original.

Re-run if the vendor ships new artwork — do not recolour by eye in an editor.

## Still missing

- **SpinsUp** — no asset yet. It is also held out of the site entirely until it
  gets its own affiliate link (its current one is Fortune Play's).

Rooster Bet and Fortune Play were supplied directly rather than via the drive.
Both arrived on white backgrounds with heavy padding, so near-white borders were
cropped before resizing — otherwise `object-fit:contain` letterboxes them and
they render visibly smaller than the rest of the set.

Wired into every `data-logo-slot` on `11woodward.co.nz` (see
`scratchpad/wire_logos.py` pattern: replaces the slot's fallback text with an
`<img>` keyed on the brand name).

## EvoSpin: grey field removed

Supplied as a JPEG on a near-uniform light-grey field (~219,219,219) with heavy
padding. JPEG has no alpha, so on the white `.afl-chip` tile it rendered as a
visible grey rectangle.

The alpha mask was built from **two** signals rather than one, because a plain
luminance threshold erases the pale blue of the planet's ring:

- **darkness** — `(bg_luminance - pixel_luminance)`, which catches the black wordmark
- **saturation** — `max(rgb) - min(rgb)`, which catches the blue planet and ring

`alpha = max(of the two)`, each with a small threshold to absorb JPEG noise in
the flat background. The result was then cropped to the artwork's bounding box
with an 8px margin and resized to the house 420px width.

Re-run that method if the vendor ships new artwork; do not knock the background
out by hand in an editor, and do not use a single luminance threshold.

## Slotgem corner artifacts

The original `slotgem.jpg` sits on a white rounded-rectangle card. JPEG has no
alpha channel, so the four areas outside that rounded rect encoded as solid
black — four dark 8x8 blobs, one per corner, clearly visible against the white
`.toplist-logo` tile.

Fixed by flood-filling inward from each corner and writing the result as PNG
with those regions transparent, so it now sits correctly on any background.
`slotgem.jpg` is kept as the untouched original; `slotgem.png` is the one to use.

Watch for this on any other logo supplied as JPEG with rounded corners.
