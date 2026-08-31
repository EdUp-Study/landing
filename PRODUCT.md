# Product

<!-- impeccable:product-schema 1 -->

This repo is EdUp's **public site** — four static pages served from GitHub Pages
at www.educationaluplift.com. The application itself lives in a separate repo
(`EdUp`), whose own `PRODUCT.md` is the fuller record of the product; this file
carries the product truth that governs what the public pages may say.

## Platform

web

## Stack

Hand-authored static HTML/CSS. No framework, no build step, no bundler.

- **Deploy:** GitHub Pages from `EdUp-Study/landing`, branch `main`. `CNAME`
  points the apex at educationaluplift.com. A push is the deploy.
- **`index.html` is currently a Claude Design canvas export** — a 1.6 MB
  self-unpacking bundle whose markup lives as a JSON string inside
  `<script type="__bundler/template">`, with an ~880 KB canvas runtime, the
  logo, a screenshot and six Inter woff2 faces as base64 blobs in a sibling
  manifest. It renders nothing without JavaScript, ships
  `<title>Bundled Page</title>`, and carries no `lang`, description or OG tags.
  Decided 2026-08-30: it is to be replaced by a hand-authored page in the same
  idiom as the legal pages below. Until then it is the incumbent design
  authority, not a model for how new pages are built.
- **The three legal pages are generated, never hand-edited here.**
  `kasutustingimused.html`, `kupsised.html` and `privaatsuspoliitika.html` are
  rendered by `backend/app/scripts/build_legal_pages.py` in the EdUp repo from
  `docs/compliance_docs/*.md`, and copied in by `publish_legal.sh`. Each carries
  a `sha256:` digest of the whole rendered page — template, stylesheet and logo
  as well as the text — which that script checks against the live site. Editing
  one here silently desynchronises it from its source and defeats the check.
  They are also the reference for what a hand-built page in this repo looks
  like: `<html lang="et">`, a real title and description, inline CSS, no JS.

## Users

The public site addresses **three audiences as peers**. This differs from the
application, where the teacher is primary and the others follow; on this surface
the three are co-equal, which is what the current page's audience tags and its
two-panel "Kuidas toimib" section already do.

- **Õpilane** — roughly 7–16 years old, grades 1–9. In the product they receive a
  task at their own level, answer it typed or by photographing handwritten work,
  and read the feedback once a teacher publishes it.
- **Õpetaja** — a subject teacher or klassijuhataja in an Estonian
  üldhariduskool. Prepares and differentiates exercises against the riiklik
  õppekava, reviews every AI-drafted grade before a pupil sees it, and tracks
  where a class stands per õpitulemus.
- **Koolijuht** — evaluates EdUp for a school. Schools, not individuals, hold the
  licence (`kasutustingimused` §1).

**No visitor can act on this site alone.** There is no self-registration
anywhere in the product: a school administrator creates every account, teachers
and staff receive an emailed link to set a password, and pupils are handed a
temporary password by their teacher. Any page that implies a visitor can sign
themselves up is describing a product that does not exist.

## Product Purpose

EdUp is an õppetöö tugisüsteem for Estonian general-education schools, grades
1–9. It carries a teacher's exercise from authoring, through AI-assisted
differentiation into difficulty variations, to per-pupil assignment; collects the
pupil's answer (typed, or photographed and transcribed); drafts a 0–100 score and
short age-appropriate Estonian feedback with an LLM; and holds all of it until a
teacher confirms and publishes.

Success is a teacher who can serve a mixed-ability class at each pupil's own
level without writing five versions of every task by hand, and who can see what
each pupil has and has not acquired against the actual national curriculum
rather than against an average.

## Positioning

**The headline claim: no AI output reaches a pupil unreviewed.** Every score and
every feedback text is a draft until a teacher publishes the review; only then
does it become the pupil's score and begin counting toward statistics. The
learning-outcome assessment is a second, separate AI call, specifically so that a
failure there can never wipe out a score or feedback.

The differentiation engine is how that promise is delivered, not the pitch:

- **The national curriculum is the data model, not a tag vocabulary.**
  Aine → Teemavaldkond ∥ Tüviteema → Teema → Õpitulemus, seeded from the
  ministry workbook.
- **Each pupil carries a standing per õpitulemus** on a five-rung ladder
  (Harjutamisel → Laiendamas), proposed by grading and confirmed by the teacher.
- **Rollups take the weakest link plus coverage, never a mean.** An unassessed
  õpitulemus counts as not-yet-acquired instead of vanishing.
- **That standing picks which difficulty variation of an exercise a pupil is
  served.**
- **Scoring is a transparent weighted set of assessment domains** per subject ×
  exercise type, with the per-domain breakdown shown to the teacher — not one
  opaque number.

## Operating Context

**Language.** Estonian throughout, on the site as in the app. There is no i18n
layer and no locale switch; Estonian is the product's language, not one of
several. The company name (Educational Uplift OÜ) and the domain are the only
English on the site.

**Why this repo exists separately.** Production sits behind an HTTP Basic Auth
wall. A notice you need a shared password to read is not a notice, so the
operative legal texts are published here, on the open web, instead of from the
app.

**The site is four pages.** `index.html` plus the three generated legal notices,
which the homepage footer links. There are no other routes, no blog, no docs.

**The app entrance.** The header's "Logi sisse" points at
`https://edup.fly.dev/login`. That host is behind the same Basic Auth wall, so a
visitor who clicks it currently meets a browser password prompt rather than a
login screen — noted here as a fact about the surface, not as a resolved
decision.

**Contact.** `info@educationaluplift.com`; Tallinn, Eesti. There is no phone
number, no contact form and no address beyond the city.

## Capabilities and Constraints

- **Active pilot, and not recruiting further schools.** Confirmed 2026-08-30.
  The site's job is credibility: showing that EdUp is real, serious and safe to
  be associated with. It must carry no "join the pilot" ask, no waitlist, no
  trial offer, and nothing that implies general availability or that a school can
  buy today.
- **Real pupils and real teachers are in an in-flight term.** Public claims must
  match what the pilot actually does now, not what is planned.
- **Maths is the first subject, not the product.** Only Matemaatika is seeded.
  The site may say maths is where EdUp starts; it may not describe the platform
  as a maths tool, nor promise dated subject expansion.
- **GDPR roles are fixed:** the school is the vastutav töötleja for all education
  data; EdUp is the volitatud töötleja acting on documented instruction, with a
  narrow controller carve-out for security logs, staff analytics, support and the
  contract relationship. A per-school Art. 28 DPA is a prerequisite and, as of
  2026-08-26, does not yet exist — so the site must not describe schools as
  contracted.
- **LLM inference stays in the EU.** Vertex AI pinned to `europe-west4`;
  production refuses to boot on a non-EU-resident model. This is safe to state.
- **Analytics never touches pupils.** It does not run for pupils at all, does not
  start before login, stops during view-as, and staff can opt out persistently.
- **Terminology is Estonian and load-bearing:** õpitulemus, tüviteema, teema,
  õpirada, õpimootor, diferentseerimine, hindamiskriteeriumid, hindamise kaalud,
  kooliaste. Kooliaste is derived from grade, never stored. There is no
  tase I/II/III.
- **Undecided / not established:** pricing and licensing (in neither repo); the
  parent role (deliberately absent in the pilot); whether the app entrance should
  keep pointing at the fly.dev host.
- **The shipped screenshot is demo data — clearance for the current capture is
  outstanding.** `opirada.webp` was replaced on 2026-08-31 with a native 2×
  capture of the running app's tree view plus its Kokkuvõte panel. It ships as
  two art-directed files — `opirada.webp` (wide, ≥761px) and
  `opirada-kitsas.webp` (the app's own portrait layout, ≤760px) — selected by a
  `<picture>` element. Both are cropped to `.oak-layout` with the "klõpsa
  lehel…" note hidden, so **no account, school name, pupil name or other app
  chrome appears in either image** — the heading, view toggle, pupil picker and
  grade filter are all outside the frame. The earlier `Kivi, Ülle` capture,
  cleared by the user on 2026-08-31, showed `admin / Test Kool` and the pupil
  name; this one shows neither.

  The underlying rows are the local demo pupil `Põld, Raul` in `Test Kool`
  (profile 93, group 4a). Both names come from the hardcoded demo-fixture pool
  in the EdUp repo at `backend/app/routers/admin.py:325`, which assembles demo
  pupils from fixed first- and last-name lists, so they are synthetic on the
  same evidence as the previous capture. The caption still names them as
  fictional even though they are not rendered, which is a disclosure of
  provenance rather than of anything visible.

  **The marks are authored, not observed.** The pupil's 29 grade-4 rungs were
  deliberately set in the local development database so that every rung of the
  ladder appears on the tree and in the Kokkuvõte counts (Alustamata 4,
  Alustatud 3, Harjutamisel 4, Arenemas 6, Kinnistumas 6, Omandatud 4,
  Laiendamas 2). They illustrate the scale; they are not a real pupil's
  standing, and the caption says so.

  **The user has not yet re-confirmed this capture**, and the rule above stands:
  a replacement capture is re-checked before it ships.

## Brand Commitments

- **Name:** EdUp. Operated by **Educational Uplift OÜ**, registry code
  **17430785**, `info@educationaluplift.com`. Public site:
  www.educationaluplift.com.
- **Wordmark:** `brand/` in the EdUp repo holds the standalone files for use
  outside the app — 800 × 580 PNG, four surface variants. `frontend/src/assets/`
  holds a separate, smaller in-app set. **The two must not be swapped**; this
  site takes the `brand/` set.
- **Brand blue `#32448A`** on the "Up" and the arrow — identical in every
  variant. The `-light` / `-dark` suffix names *the surface the logo sits on*,
  not the ink.
- **The arrow rises well above the lettering, so size the wordmark by height and
  let width follow.** It is not 4:1 and must never be squashed to fit a slot.
- **Visual direction is the category standard, chosen deliberately.** Offered a
  round of distinctive visual worlds for the public site on 2026-08-31, the user
  took the standing exit: the familiar education-product page, executed at full
  craft. The quality bar they named is **Duolingo and Khan Academy** — rounded
  forms, friendly sans, generous space, saturated colour, illustration-led.
  This is a commitment, not a fallback: execute the convention without irony and
  without smuggling in a quirk. An earlier angular direction (a ruled class
  register in Bodoni) was built and rejected as "too faceted"; round forms,
  round lettering and a softened palette are the standing preference.
- **Voice:** Estonian, plain, and pitched at the reader's age — a grade-1 pupil
  and a koolijuht are not addressed the same way. On a page all three read, that
  means plain language that patronises nobody.

## Evidence on Hand

**Real, and usable as-is:**

- The national maths curriculum, converted from the ministry workbook: 11
  tüviteemat, 92 teemat, 263 specific and 147 general õpitulemust, seeded from
  `backend/seed/curriculum/*.csv` in the EdUp repo.
- The global five-band assessment scale, and grading-weight profiles seeded from
  a teacher's own rubric.
- Versioned operative legal texts — kasutustingimused v2, privaatsuspoliitika
  v2, küpsised — already published here.
- Logo assets in `brand/`.
- The application screenshot presently in the hero (see the open item above).

**Absent — and this surface is exactly where they get invented.** There are no
testimonials, no named pilot schools, no pupil-outcome or efficacy data, no
benchmarks, no pricing, no case studies and no press anywhere in either repo. A
credibility-mode marketing page is under constant pressure to supply social
proof; there is none to supply. Do not write a quote, a school name, a
percentage, a pupil count or a logo wall. Credibility here has to come from
being specific and honest about the mechanism, which the product genuinely has.

## Product Principles

1. **The teacher publishes; the machine drafts.** No AI-generated score or
   feedback reaches a pupil without a teacher's confirmation. This is the
   product's strongest and truest claim, and the site should lead on it.
2. **The curriculum is the unit of truth.** Progress is reported against
   õpitulemused, aggregated by weakest link plus coverage — never a mean that
   lets one unacquired outcome average itself away.
3. **Differentiation follows evidence, not effort.** What a pupil is served is
   computed from their recorded standing; the teacher can always override.
4. **Estonian, at the reader's age.** Teacher-facing language uses the õppekava's
   own vocabulary rather than a translation of it.
5. **Say only what the evidence list supports.** Specificity substitutes for
   social proof; invention does not.

## Ethical Constraints

The product's users are children, and the public page is read by children too.
Most of the standard dark-pattern taxonomy has no surface here — no cart, no
checkout, no consumer subscription, no advertising, no social graph, no
self-registration — so do not import checklists written for e-commerce. What
binds:

- **No overstated or unevidenced claims.** See Evidence on Hand. This is the
  binding constraint on a credibility surface.
- **No visual misdirection**, and no burying a notice in a wall of text. The
  legal notices stay reachable from the homepage footer.
- **Decline and secondary choices stay neutral** — "Ei luba", "Hiljem",
  "Tühista", never phrasing that frames the safe choice as a loss. Consent gets
  button parity; `AnalyticsConsent.tsx` in the app is the reference
  implementation, two buttons of equal weight differing only in fill.
- **No addictive mechanics**, and no framing of children's progress as
  competition or streaks.

## Accessibility & Inclusion

- **Target: WCAG 2.1 AA**, self-set — the bar design work and audits are held to.
- **Binding status is open and must not be overstated.** No school contract or
  procurement document has been verified as naming a standard. The likely route
  to a hard requirement is Directive (EU) 2016/2102 (public-sector bodies) passed
  down through school procurement — *not* the European Accessibility Act, which
  targets services sold to consumers, whereas EdUp is sold only to schools.
  Confirm against pilot procurement terms before claiming compliance anywhere,
  on this site included.
- **Product-specific need:** pupil-facing text must be readable by a
  seven-year-old in grade 1.
- **Motion:** `prefers-reduced-motion` is honoured across the application; any
  motion added here must keep that.
