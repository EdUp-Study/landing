---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Avaleht — index.html

**Scope:** the whole public homepage at educationaluplift.com. The three legal
pages are generated elsewhere and are out of scope.

**Visitor mode: Persuade** — persuading toward *credibility*, not conversion.
EdUp is mid-pilot and is not taking on new schools, so there is no signup, no
waitlist and no "join the pilot" ask. Success is a first-time visitor knowing
what EdUp is, that a teacher publishes every grade the machine drafts, and that
it is real — within seconds.

**Audience and job:** õpilane, õpetaja and koolijuht as peers. No visitor can
act alone; there is no self-registration anywhere in the product. The only
actions offered are contact and a login door for people who already have an
account.

**Direction: the category standard, taken deliberately.** Offered a hand of
distinctive worlds on 2026-08-31, the user took the standing exit and named
**Duolingo and Khan Academy** as the craft bar. This is a commitment, not a
fallback: round forms, pill buttons with the lip that idiom uses, 20px cards,
soft shadows, one saturated brand blue, generous air, Nunito throughout.
Execute the convention without irony and without smuggling in a quirk.

**What this replaced, and why it must not come back.** A previous build shipped
a "Klassipäevik" world — a ruled class register, Bodoni Moda, `border-radius: 0`
everywhere, hairline and double rules, deep navy on hard black. The user
rejected it as **"too faceted… should be rounder"** and named the forms, the
typeface and the colour — explicitly *not* the temperature. Angular execution is
a standing risk on this surface; do not answer "rounder" with "friendlier".

**Proof and content:** the product is the only proof available — no
testimonials, no named schools, no efficacy data. The page leads with the real
**õpirada screenshot from the app** (`opirada.webp`, demo data, labelled) and
follows with the real grade-4 maths curriculum — 6 tüviteemat, 14 teemat, 29
õpitulemust from the same CSVs the app seeds from — as an interactive table.
The user chose the screenshot over a hand-drawn SVG tree: canon leads with
product shots, and the drawn tree was twice judged poor.

**Memorable moment:** the operator toggle. One control recomputes the Seis
column between *nõrgima lüli järgi* and *keskmisena* over identical data, and
Naturaalarvud moves from Harjutamisel to Kinnistumas. The product's sharpest
claim, demonstrated rather than asserted.

**Constraints:** Estonian only. Hand-authored static HTML, no build step. Fonts
self-hosted rather than Google-hosted — EU residency, children's data. The
wordmark's "Up" is #32448A in every variant, so the wordmark never sits on a
#32448A field; on the blue footer it rides a white rounded patch.

**Unresolved:**
- `opirada.webp` is 1200×679 and soft on retina. A sharper capture needs a
  login to the local app, which no longer offers the old pick-a-user flow.
- "Logi sisse" points at edup.fly.dev/login, behind the Basic Auth wall.
