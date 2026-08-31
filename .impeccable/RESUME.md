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

To recapture: log in to the local app on :8000 (`app.scripts.reset_local_dev_logins`
restores the documented dev passwords), then screenshot
`/teacher/grades/15/study-path?student_id=93` clipped to `.oak-layout` with the
`.oak-note` hidden. Viewport 2000px wide for the landscape file, 1000px for the
portrait one, at deviceScaleFactor 2.

## Two known false positives in the design hook

Both measured, both safe to ignore — do not "fix" them:

- `cramped-padding` on `section.tint`: the detector reads `padding: 86px 0` on
  the section and stops. The horizontal inset comes from the child `.wrap`;
  measured, text sits **224px** from both edges.
- `flat-type-hierarchy` reporting 12.8/14.4/16px: it cannot resolve `clamp()`,
  so it misses the h1 and h2. The rendered scale is 49.6 / 36.8 / 19.2 / 17 /
  16 / 14.4 / 12.8px.

## Loose ends

- **The hero's right half is empty.** The finish review wanted a produced spot
  illustration there and declined a CSS-shape substitute. Needs image
  generation; no session so far has had it. It must not become a proof band or
  a metric row — there is no evidence for either (PRODUCT.md § Evidence).
- "Logi sisse" points at `edup.fly.dev/login`, behind the Basic Auth wall.
- This repo is **public** and Pages serves its root. `_config.yml` excludes the
  working documents from the build. Anything added at root is world-readable.
- Local preview: `python3 -m http.server 8899` from the repo root.
