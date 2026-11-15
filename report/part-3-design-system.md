# PART 3 — MASTER DESIGN SYSTEM

Every one of the 35 formats in Part 4 inherits this system. Formats may override individual rules (stated in their cards), but no format may violate the palette rule or the licensing rule.

## 3.1 STRICT RULES (never violated)

1. **NO green — including light green — in any design.** No green backgrounds, text, bars, icons, buttons, photos with green overlay, or "success" styling in green. Where a normal design system would use green (confirmation, "live", positive scores), use **navy or gold** instead.
2. **Never use an unlicensed wire photo** (Reuters, AP, Getty, NYT, broadcast screenshots of footage). Layouts are copyable; photos are not. Sources: Pexels, Unsplash, Wikimedia Commons (check licence per photo), Canva stock, or no photo at all.
3. **Never crop the source out of a screenshot.** The originating outlet's name/handle stays visible.
4. **Never place text over a face.** Darken the photo instead.
5. **BREAKING only when it is genuinely breaking** (Fox/NewsWhip label rule). Otherwise use the correct label (§3.5).
6. **Every post carries a source line.** No exceptions.

## 3.2 Colour palette

| Role | Hex | Where it is used |
|---|---|---|
| **Navy — primary** | `#0B1F3A` | Card backgrounds, header bands, headline panels, gradient scrims |
| **Breaking red — accent** | `#C8102E` | BREAKING/RESULT/DEVELOPING labels, numbers, dividers, quote marks, urgent bars |
| **White — canvas** | `#FFFFFF` | Body cards, text on navy, slide backgrounds |
| **Black — text** | `#111111` | Body copy on white/light panels |
| **Light grey — support** | `#F2F2F2` | Secondary panels, captions, dividers, metadata strips |
| **Gold — rule only** | `#C9A227` | Thin 4–6 px rules and small accents only — **never as a background or body text** |

Forbidden: every green hue (incl. light green, mint, olive, teal-leaning greens), and any decorative gradient that lands in green.

## 3.3 Typography

| Level | Font | Spec (on a 1080 px canvas) |
|---|---|---|
| Headline | Montserrat ExtraBold / Oswald Bold / Arial Black | ALL CAPS, 72–110 pt, tight leading (1.05–1.15), max 3 lines |
| Sub-headline / labels | Montserrat Bold | ALL CAPS, 28–40 pt |
| Body / facts | Inter Regular / Arial Regular | 36–44 pt, sentence case, leading 1.3 |
| Caption text (in-image) | Inter Regular | 28–32 pt minimum |
| Source line | Inter Regular | 20–24 pt, 70% opacity white on dark / 60% grey on light |
| Video subtitles | Inter Bold | 32–40 pt, high contrast, never in the bottom 15% of frame |

Legibility rule: **if it can't be read on a 5-inch phone at arm's length, it is too small.**

## 3.4 Canvas & export specs

| Use | Canvas | Ratio | Notes |
|---|---|---|---|
| Feed card (FB + IG) | 1080 × 1080 | 1:1 | Default for F01–F24, F29–F33 |
| Feed card (IG max height) | 1080 × 1350 | 4:5 | Use when text needs more room; tallest uncropped in feed |
| Reels / Stories | 1080 × 1920 | 9:16 | F06, F14, F16, F27; keep text out of top 15% and bottom 25% (UI zones) |
| Link preview | 1200 × 630 | 1.91:1 | F12 — pulled automatically from the linked article |

Export: **PNG** for any graphic containing text or logos; **JPG** for pure photos; sRGB; 2× export when the tool allows. Keep headline text out of the **lower third** of Facebook feed images (UI overlap).

## 3.5 Label system

| Label | Colour | Placement | Use only when |
|---|---|---|---|
| **BREAKING** | Red rectangle, white bold caps | Top-left, never over a face | The event is genuinely urgent and happening now |
| **DEVELOPING** | Red rectangle, white bold caps | Top-left | Facts are still emerging (F22) — pair with "we are verifying" copy |
| **UPDATE / CORRECTION** | Navy rectangle, white caps | Top-left | You are amending or correcting an earlier post (F23) |
| **EXPLAINED** | Navy rectangle, white caps | Top-left | The post is context/analysis, not live news (F20) |
| **RESULT / FULL TIME** | Red bar | Top-centre | Sports results (F07) |
| **TIMELINE** | Navy bar + red times | Cover slide | Hour-by-hour reconstructions (F18) |
| **TODAY** | Red tag | Cover slide only | Round-ups (F08) |
| **FACT CHECK** | Navy rectangle + red check icon | Top-left | Debunks (F24) |

Optional time stamp beside the label: `09:00 PKT` in white. The label occupies at most 8% of the canvas height.

## 3.6 Photo treatment

- Full-bleed photo behind text → apply a **navy gradient scrim** over the text zone (bottom 40% minimum, `#0B1F3A` at 85% → 20% opacity upward).
- Never text over faces, logos, or busy areas; move the text block, not the face.
- Square-crop photos to the subject; never stretch.
- One photo per card unless the format is a photo essay (F10) or carousel.
- **Every photo gets a credit:** `Photo: [Photographer/Source]` or `Source: [Outlet]` in the source line.

## 3.7 Caption framework (all formats)

```
LINE 1 — THE HEADLINE IN PLAIN TEXT (identical to the on-image headline)
LINE 2–3 — 1–2 sentences of verified fact (total caption body under 40 words where possible)
LINE 4 — Source: [outlet name]  ·  Photo: [credit] (if applicable)
LINE 5 — ONE call to action (and only one)
LINE 6 — Hashtags
```

- **Facebook hashtags: 1–2** (e.g. `#BreakingNews`) — the biggest Pages use almost none. **Instagram hashtags: 3–5** (e.g. `#BreakingNews #PakistanNews #WorldNews #Speakenza`).
- Pakistan video descriptions may add the regional hashtag block `#breakingnews #latestnews #headlines` (Geo/ARY/Dunya convention) — in the video description, not as caption spam.
- No exclamation marks in hard-news captions (Dawn style rule). Curiosity-gap clickbait is forbidden (BBC plain-headline standard).
- CTA bank (pick exactly one): "Follow for updates" · "Save this post" · "Share this update" · "Read the full story at the link" · "Comment your answer" · "Which matters more — comment P or W".

## 3.8 Accessibility & ethics

- Burned-in subtitles on every video (sound-off viewing is the default).
- Contrast ratio ≥ 4.5:1 for body text; white on navy and black on white pass; gold only for rules.
- Honest labelling: if the post is analysis, it says EXPLAINED; if unverified, it says DEVELOPING (never BREAKING).
- Every post is traceable: source line, photo credit, and — where the story changed — a correction (F23).

## 3.9 Do-not list (design)

No green (incl. light green) · no text over faces · no unlicensed wire photos · no cropped-out sources · no BREAKING for routine news · no more than one CTA · no text under 20 pt · no more than 3 type sizes per card · no exclamation marks in hard news · no decorative stock-photo collages · no vertical video in 16:9 letterbox · no watermarks other than your own logo (small, bottom-right, max 6% width).
