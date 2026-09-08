# Resume: EdUp landing page

Last updated 2026-08-31. Read `PRODUCT.md` for product truth and `DESIGN.md`
for the visual system — both are current. This file carries only what neither
of them records.

## What this is

`index.html` is ~28 KB of hand-authored static HTML with **no build step and no
JavaScript**. Git history before this round holds a 1.6 MB Claude Design canvas
bundle; do not restore it.

## Decisions that are settled — do not re-litigate

1. **Two visual worlds were built and thrown away.** An angular ruled
   class-register ("too faceted… should be rounder"), then a hand-invented blue
   palette. The direction round was re-rolled and the user took **the standing
   exit — canon**, naming Duolingo and Khan Academy as the craft bar. Convention
   is the commitment: execute it straight, no irony, no smuggled quirk.
2. **The palette is the application's, not a brand palette.** Copied from
   `frontend/src/App.css` in the EdUp repo under the same token names. See the
   Borrowed Palette Rule in DESIGN.md.
3. **The copy is the product owner's.** An earlier rewrite was rejected as "AI
   slop, because your Estonian is not good" and reverted verbatim. Propose copy
   changes; do not make them. Flag typos rather than fixing them silently.
4. **The proof is a screenshot, not a drawing.** A hand-drawn SVG õpirada was
   built and then removed in favour of a capture of the running app.

## The õpirada capture

Two art-directed files behind a `<picture>`: `opirada.webp` (wide) and
`opirada-kitsas.webp` (the app's own portrait layout, ≤760px). Both are cropped
to `.oak-layout`, so no account, school or pupil name appears in either.

**The marks are authored.** The local demo pupil's 29 grade-4 rungs were set
deliberately so every rung of the ladder appears (Alustamata 4, Alustatud 3,
Harjutamisel 4, Arenemas 6, Kinnistumas 6, Omandatud 4, Laiendamas 2). See
PRODUCT.md for the clearance status, which is **still outstanding**.

The image is the **tree canvas only**. The Kokkuvõte panel used to be baked
into it, which squeezed the tree to 0.59x and made its labels ~8px; the panel is
now static markup on the page (`.oakp`) and the tree renders at 0.96x.

To recapture: log in to the local app on :8000 (`app.scripts.reset_local_dev_logins`
restores the documented dev passwords), then screenshot
`/teacher/grades/15/study-path?student_id=93` clipped to **`.oak-scroll`**
(`SEL=.oak-scroll node capture-tree.mjs`). Viewport **1350** for the wide file
(1043x670, renders at 0.96x) and **1000** for the portrait one, deviceScaleFactor 2.
If the panel data changes, the markup numbers must be updated to match —
they are hand-entered and nothing checks them against the app.

Note `timeout` does not exist on macOS; wrapping the capture in it silently
fails. Chrome also takes >2 min to start when several instances contend, so run
captures one at a time.

## The social card (`og-card.png`)

The 1200×630 `og:image`, added 2026-09-08. It replaced the bare
`edup-wordmark.png`, which LinkedIn and Facebook were letterboxing into a small
square because they crop to roughly 1.91:1; `twitter:card` moved from `summary`
to `summary_large_image` at the same time.

**It is generated, not hand-drawn — regenerate with `tools/build-og-card.py`**
(system python3, no dependencies). The script writes an HTML card and
screenshots it with headless Chrome at exactly 1200×630, so the type is the
site's own self-hosted Nunito and every colour is a `:root` token copied from
`index.html`. A card drawn with a raster library would drift from the page it
represents; this one cannot.

**The copy is the product owner's, as everywhere else.** The headline is the
approved `<title>` string verbatim and the three chips are the hero pills. No
new Estonian was written for it. `1.–9.&nbsp;klassile` is welded with a
non-breaking space and the `h1` is capped at 720px so the headline always breaks
into the same three lines — without both, "1.–9." orphans onto the middle line.

Checked at build time: all four text/ground pairs pass WCAG (lowest is the pill
text at 4.64:1 on white), and the headline stays legible downscaled to a 360px
feed thumbnail, which is what the type-led design was chosen for.

`tools/` is excluded in `_config.yml` — versioned for reproducibility, not served.

## Six known false positives in the design hook

All measured, all safe to ignore — do not "fix" them:

- `cramped-padding` on `section.tint` (x2): the detector reads `padding: 86px 0`
  on the section and stops. The horizontal inset comes from the child `.wrap`;
  measured, text sits **224px** from both edges.
- `cramped-padding` on `div.art`: measured inset below the caption is **23px**,
  well over the 8px the rule asks for.
- `flat-type-hierarchy` reporting 11/12.8/14.4/16px: it cannot resolve
  `clamp()`, so it misses the h1 and h2. The rendered scale is 49.6 / 36.8 /
  19.2 / 17 / 16 / 14.4 / 12.8px.
- `repeating-stripes-gradient`: the green hatch on the Alustatud bar segment.
  It is semantic, not decorative — it is the application's own treatment for a
  state drawn on a leaf as an *absence*, and an invisible segment would read as
  a gap.
- The 404 page reports `flat-type-hierarchy` for the same `clamp()` reason.

## Loose ends

- **The hero's right half is empty.** The finish review wanted a produced spot
  illustration there and declined a CSS-shape substitute. Needs image
  generation; no session so far has had it. It must not become a proof band or
  a metric row — there is no evidence for either (PRODUCT.md § Evidence).
- "Logi sisse" points at `edup.fly.dev/login`, behind the Basic Auth wall.
- This repo is **public** and Pages serves its root. `_config.yml` excludes the
  working documents from the build. Anything added at root is world-readable.
- Local preview: `python3 -m http.server 8899` from the repo root.
