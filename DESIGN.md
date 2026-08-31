---
name: EdUp Public Site
description: The category-standard education page executed straight — the application's own palette, Nunito, and one radius logic where the corner tracks the box.
colors:
  accent: "#4978A7"
  accent-strong: "#2D5B88"
  accent-soft: "#DDEDFF"
  accent-alt: "#A06A20"
  accent-alt-soft: "#F6ECD9"
  bg-primary: "#F4F9FF"
  surface-card: "#FFFFFF"
  surface-sub: "#F0F4F9"
  border-color: "rgba(0,0,0,.09)"
  border-subtle: "rgba(0,0,0,.06)"
  text-primary: "#1B2025"
  text-body: "#33393E"
  text-dim: "#4E5359"
  text-secondary: "#65696F"
  text-muted: "#7C8186"
  text-on-color: "#FFFFFF"
  brand-blue: "#32448A"
  scroll-thumb: "#B9CBDD"
  skill-beginning: "#FDBA74"
  skill-easy: "#A9C785"
  skill-medium: "#639922"
  skill-advanced: "#4C7419"
  skill-extra: "#3A5A11"
typography:
  display:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "clamp(2rem, 4.4vw, 3.1rem)"
    fontWeight: 800
    lineHeight: 1.14
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "clamp(1.6rem, 3vw, 2.3rem)"
    fontWeight: 800
    lineHeight: 1.16
    letterSpacing: "-0.02em"
  subhead:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "1.125rem"
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "clamp(1.05rem, 1.6vw, 1.2rem)"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: "normal"
  body:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "17px"
    fontWeight: 500
    lineHeight: 1.65
    letterSpacing: "normal"
  body-mobile:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.65
    letterSpacing: "normal"
  label:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "0.9rem"
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: "normal"
  chip:
    fontFamily: "Nunito, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "0.8rem"
    fontWeight: 800
    lineHeight: 1.4
    letterSpacing: "normal"
rounded:
  xs: "8px"
  sm: "12px"
  card: "20px"
spacing:
  gutter: "clamp(20px, 5vw, 64px)"
  section: "clamp(44px, 6.5vw, 86px)"
  grid-gap: "clamp(18px, 2.4vw, 26px)"
  card-pad: "clamp(20px, 3vw, 32px)"
components:
  button-primary:
    backgroundColor: "{colors.accent-strong}"
    textColor: "{colors.text-on-color}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text-on-color}"
  button-ghost:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-strong}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  button-ghost-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-strong}"
  chip:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-strong}"
    typography: "{typography.chip}"
    rounded: "{rounded.xs}"
    padding: "7px 16px"
  step-number:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-strong}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    size: "30px"
  icon-slot:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-strong}"
    rounded: "{rounded.sm}"
    size: "46px"
  icon-slot-alt:
    backgroundColor: "{colors.accent-alt-soft}"
    textColor: "{colors.accent-alt}"
    rounded: "{rounded.sm}"
    size: "46px"
  card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-body}"
    rounded: "{rounded.card}"
    padding: "clamp(20px, 3vw, 32px)"
  accordion-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "16px 20px"
---

## Overview

**Creative North Star: "The product, shown plainly."**

This page took the standing exit in its direction round: the education-SaaS
page done at the category standard, executed at full fidelity rather than
subverted. Two earlier worlds were built and discarded — an angular ruled
class-register, then a hand-invented blue — and the lesson of both is written
into the rule below: **nothing on this surface is invented.**

The palette is not a brand palette designed for marketing. It is the
application's own light theme, copied token-for-token out of
`frontend/src/App.css` in the EdUp repo and kept under the same names, so the
two surfaces can be diffed line by line. A visitor who clicks *Logi sisse*
should not experience a change of world. The proof image is not an
illustration of the product; it is a screenshot of it. The copy is the
product owner's own Estonian.

The one composed decision is the shape language, and it is stated once: the
corner radius tracks the size of the box, at roughly a quarter of its side.
That ratio was already latent in the icon slots (12px on a 46px square) and is
now the whole page's rule, which is why nothing here is a pill or a circle.

**Key Characteristics:**

- Left-aligned throughout; the content edge holds across every section but one — the õpipuu figure, which is deliberately wider.
- Alternating `bg-primary` / `surface-sub` bands give section rhythm without rules or dividers.
- Every icon is Lucide, inlined, inheriting `currentColor` — never given a colour of its own.
- Two hues only: a blue that carries every interactive surface, and an amber that appears exactly once.
- One borrowed constant beside them: the wordmark's own blue, on the wordmark's own letters and nowhere else.
- No JavaScript. The page is static HTML and renders complete with scripting off.

## Colors

`accent` (#4978A7) carries links and hover fills; `accent-strong` (#2D5B88) is
the resting state of every filled button, which inverts the usual
darker-on-hover convention so the button lightens toward the link colour on
approach. Both clear 4.5:1 on white — the lightness is pinned by contrast
measurement, not by eye.

`accent-alt` (#A06A20) is the second hue and appears in exactly one place: the
second feature card's icon slot. It exists to prove the palette has a second
voice, not to introduce a decorative one.

The text ramp runs `text-primary` → `text-body` → `text-dim` →
`text-secondary` → `text-muted`, five steps, and headings always take
`text-primary` while supporting prose takes `text-secondary`.

**The Borrowed Palette Rule.** Every colour on this page is the application's
own token under the application's own name. If a value needs to change, change
it in `frontend/src/App.css` first and bring it across. Never tune a colour
here to suit the marketing page — that is how the two surfaces drift into
looking like two products.

**The Wordmark Blue Is Not A Palette Colour.** `brand-blue` (#32448A) is the
logo's own blue, recorded in PRODUCT.md § Brand Commitments — not an App.css
token, and the one value on this page that does not come from the application.
It exists so the "Up" in the h1 matches the wordmark sitting directly above it,
and it is used on those two letters and nowhere else. It is deliberately *not*
`accent-strong` (#2D5B88): with the real logo in the masthead a few hundred
pixels up, a near-miss would read as a mistake rather than as a second blue.
Do not reach for it for anything that is not the word EdUp. 8.52:1 on the page
ground.

**The Ladder Is Not Decoration.** The five `skill-*` greens (plus the orange
at the bottom) are the application's achievement ramp, copied from `App.css`
`--skill-*` along with the `--color-green` family it rides. They appear only in
the õpipuu panel, where each one *means* a rung — Harjutamisel through
Laiendamas — and they carry that meaning identically in the screenshot above
the panel. The stylesheet keeps App.css's `color-mix()` expressions rather than
resolved hexes so the two surfaces cannot drift; the values listed in the
frontmatter are what those expressions currently compute to. There is
deliberately **no** `skill-none`: "not started" is an absence, drawn as an
outline, and Alustatud is the same empty leaf with a dashed green edge. Never
use a ladder colour for anything that is not a rung.

**The Two Neutrals Rule.** Borders are `rgba()` black at 9% and 6%, not a
grey. They sit on both `surface-card` and `surface-sub` without a seam, which
a fixed grey cannot do across two backgrounds.

## Typography

Nunito at weight 400–1000, self-hosted as two woff2 subsets (latin and
latin-ext). It is **never** loaded from Google Fonts: this page is read by
Estonian schools on behalf of children, and PRODUCT.md treats EU data
residency as a hard constraint, so the page makes no third-party request that
would log a visitor's IP.

Body is 17px at 1.65 and weight 500 — a half-step heavier and larger than
default, because Nunito's rounded terminals go soft at 400. Below 760px it
drops to 16px, the only typographic breakpoint on the page.

Headings run 800 with `-0.02em` tracking and `text-wrap: balance`. Both
display sizes are `clamp()`, so the type scale is fluid rather than stepped
and there are no intermediate heading sizes to choose from.

**The Measure Rule.** Prose is capped: 66ch for body paragraphs, 58ch for
leads, 48ch inside step bodies, 46ch inside feature cards. The page is wide;
the reading line is not.

## Layout

`.wrap` caps at 1180px with `--gutter` padding and is the container for every
section but one. Every section is `padding: var(--section) 0` and alternates
background between `bg-primary` and `surface-sub`.

**The One Wide Section Rule.** `#opirada` uses `.wrap--wide` (1520px) because
the õpipuu is the page's proof and cannot be both legible and narrow: the tree
is a raster with a fixed aspect, so at the 1180px column a readable rendering
was 647px tall and pushed the summary panel below it, making the figure taller
than a laptop screen. The extra width buys the panel a column *beside* the
tree instead. This is the only section allowed to opt out, its left edge does
move relative to the rest of the page, and that cost was accepted knowingly —
do not extend the exception to a second section without the same argument.

Both multi-column blocks are `repeat(auto-fit, minmax(…, 1fr))` grids — the
feature pair at 320px, the step columns at 300px — so they collapse to one
column on their own without a media query. The page has exactly two media
queries: `prefers-reduced-motion` and a single 760px rule that drops body type
and unsticks the nav.

**The Art Direction Rule.** The õpirada figure is not one image scaled. Below
760px a `<picture>` swaps to a separate capture of the application's own
portrait layout, because a wide screenshot shrunk to phone width is
unreadable, not responsive.

## Elevation & Depth

Three shadows, all tinted with the ink colour rather than pure black, assigned
by how much the element should lift:

- `sh-1` — feature cards, contact cards, accordion items. Barely there.
- `sh-2` — the step columns, which are the page's main content blocks.
- `sh-3` — the õpirada figure alone. It is the page's proof and the only
  element allowed to float.

There is no border-plus-shadow escalation beyond this; depth is the only
hierarchy signal, and surfaces never gain a heavier border to compete.

## Shapes

**The Quarter-Side Rule.** The corner radius is about a quarter of the box's
shorter side, so it grows with the element instead of collapsing to a pill:

| Box | Radius |
|---|---|
| chips, step numbers (~30px) | `xs` 8px |
| buttons, social buttons, icon slots, images, accordion (36–46px) | `sm` 12px |
| cards, figures, sections | `card` 20px |

Nothing on the page is `border-radius: 999px` or `50%`. Labels and numbering
are softened rectangles in the same family as the icons they sit beside — an
earlier version mixed full pills against 20px cards, and the two shape
languages read as two designs.

## Components

**Buttons** are the only filled surfaces. `button-primary` rests on
`accent-strong` and lightens to `accent` on hover; there is no shadow, no lip
and no transform. `button-ghost` is a 2px-bordered white variant used where a
second action would otherwise compete.

**Chips** (`.pills`, `.who`) are `accent-soft` on `accent-strong` at 800
weight, 0.8rem. They label; they never act.

**Icon slots** are 46px squares at `sm` radius holding a 22px Lucide glyph.
The `accent-soft` variant is the default; `accent-alt-soft` marks the single
amber moment.

**Accordion** (`.kkk`) hides the native marker and rotates a Lucide chevron
180° on open. The summary row is the click target and takes `surface-sub` on
hover.

**Focus** is a 3px `accent` outline at 3px offset with `sm` radius, applied
via `:where()` so it costs no specificity and every interactive element
inherits it.

**The õpipuu panel** sits in a ~330px column to the right of the tree and
wraps beneath it under about 920px of content width. It is the one place the
page reproduces application UI in markup rather than as a screenshot. Its legend uses the app's own oak-leaf
glyph, copied from `oakTreeLayout.OAK_BLADE` — a **deliberate exception to the
Lucide rule**, because the legend has to carry the same mark the canopy in the
image above it does, and a generic swatch would break that link. Its bars are
flex rows of `flex-grow`-weighted segments, so they need no JavaScript. The
segments are colour-only, so every bar carries an `aria-label` naming its mix,
and the two non-rung states get visible stand-ins — a grey wash for Alustamata,
a green hatch for Alustatud — because an invisible segment reads as a gap.

## Do's and Don'ts

- **Do** take colours from `frontend/src/App.css` and keep the token name.
- **Do** use Lucide for every glyph, inlined, with no `color` or `stroke` attribute so it inherits `currentColor`.
- **Do** pick a radius by the size of the box, not by the kind of component.
- **Do** cap every run of prose with a `ch` measure.
- **Don't** introduce a pill or a circle. The shape language has three steps and none of them is round.
- **Don't** add a third hue. Amber appears once, deliberately, and `brand-blue` is reserved for the letters of the wordmark.
- **Don't** use a `skill-*` green for anything that is not a rung of the achievement ladder.
- **Don't** load a font, script, or asset from a third-party origin — EU data residency is a product constraint, not a preference.
- **Don't** add JavaScript for presentation. The page currently ships none.
- **Don't** claim anything the evidence list in PRODUCT.md doesn't support: there are no testimonials, no named pilot schools, no efficacy data, and a marketing surface is exactly where those get invented.
- **Don't** ship a screenshot without checking it for real pupil data, and disclose authored demo marks as such.
