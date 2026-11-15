# PART 6 — ACTIONABLE IMPLEMENTATION FRAMEWORK

For a digital publisher of any size, with a one-person track (Speakenza / @lifespark955379) called out explicitly. The evidence baseline: WaPo grew 600K→6M with 8–9 people and ~10 posts/day; BBC doubled Instagram engagement by posting less; the newsroom-scale accounts (Aaj Tak 110M IG actions in Aug 2025; Daily Mail 1B video views/month; BBC 6–8 posts/day) are **not** the target model — **2–3 timed posts/day at fixed slots is the repeatable unit.**

## 6.1 The cadence model (PKT)

| Slot | Time | Primary formats | Purpose |
|---|---|---|---|
| **Morning** | 09:00 | F04 bulletin or F08/F26 | Start the habit; scan of overnight news |
| **Midday** | 14:00 | F01/F03/F05/F19 (story of the day) | Main story of the day, maximum clarity |
| **Evening** | 19:00 | F02/F11/F20 (explainer) or F07/F35 (results) | Saves and depth while the feed is slow |
| **Reactive window** | any | F01/F22/F25 within 15 min of a real event | True breaking only — otherwise it waits for the next slot |
| **Stories** | 2–3×/day | F14 + reshares of feed posts | Cheap daily presence; poll stickers for replies |

Rules: slots never move; a missed slot is skipped, never rushed; the reactive window is for genuine news only (label discipline in §3.5).

## 6.2 Weekly format matrix (one-person track)

| | 09:00 | 14:00 | 19:00 | Stories |
|---|---|---|---|---|
| **Mon** | F04 | F01/F03 | F02 (explainer) | F14 ×2 |
| **Tue** | F04 | F19 (Pak+World) | F11 ("3 things") | poll sticker |
| **Wed** | F04 | F01/F03 | F08 (round-up cover) | F14 ×2 |
| **Thu** | F04 | F05 (what we know) | F20 (EXPLAINED) | poll sticker |
| **Fri** | F04 | F01/F03 | F30 (numbers) | F14 ×2 |
| **Sat** | F08 (week wrap) | F07/F35 (sport) | F15/F29 (question/poll) | reshares |
| **Sun** | F32 (key points) | F10 (in pictures) | F18 (timeline) | reshares |

Rotate formats weekly; keep the slots fixed. Breaking news overrides the matrix — the matrix is the floor, not the ceiling.

## 6.3 Production pipeline (Canva-first)

1. **Build the template library first (day 1):** one locked master per family — breaking card (F01/F21), carousel set (F02), bulletin (F04), quote (F17), score board (F07/F35), Reel cover (F06). Naming: `SPEAK_F01_BREAKING_1x1`, `SPEAK_F02_CAROUSEL_5SLIDE`…
2. **Per-post workflow (target ≤15 min):** verify facts (2 independent sources) → pick format from the matrix → fill the template (headline from Part 5) → caption per §3.7 → export PNG/JPG per §3.4 → schedule at the slot.
3. **Photo pipeline:** free stock only (Pexels/Unsplash/Wikimedia with per-photo licence check/Canva stock) → credit captured at download → credit line on the post. **No wire photos, ever** (copyright strikes end small accounts).
4. **Video pipeline (F06/F16/F27/F28):** script = the caption; stills + voiceover + burned-in subtitles; export 1080×1920 H.264 + AAC; hard cap 30 seconds for routine news.
5. **Naming & archive:** `2026-11-15_0900_F04_headlines.png` → keep every exported asset in the project's Google Drive folder (dated subfolders).

## 6.4 Verification & ethics protocol (non-negotiable)

| Step | Rule |
|---|---|
| **Sourcing** | 2 independent sources before publishing a claim; 1 official source for alerts/numbers (F25/F30/F35) |
| **Labels** | BREAKING only if urgent + now; if unconfirmed details remain → DEVELOPING (F22) |
| **Screenshots** | Source name/handle visible (F13); verify the account is real first |
| **Numbers** | Every figure carries source + date; never mix tracker dates silently |
| **Photos/video** | Licence checked per asset; credit per use; never crop credits out |
| **Corrections** | Publish F23 openly and promptly; never silently delete (the wire practice) |
| **Tone** | No exclamation marks in hard news; no mockery in debunks; quote verbatim |
| **Conflict** | Court cases and tragedies: no polls (F25/F29 restriction), no BREAKING on verdicts (use `[RESULT]`) |

## 6.5 Measurement framework

Track in a simple sheet (one row per post): `date · slot · format ID · platform · reach · likes · comments · shares · saves · link clicks · watch time (video) · notes`.

| KPI | Meaning | Review |
|---|---|---|
| **Reach per post** | Distribution health | Weekly median vs previous week |
| **Saves (IG)** | Recommendation fuel — the carousel KPI | Per format family |
| **Shares (FB)** | The photo/alert/score KPI | Per format family |
| **Watch-through (video)** | Hook quality (first 3 seconds) | Per video |
| **Comments** | Trigger quality (F15/F29) | Weekly |
| **Follows per post** | Profile conversion (F34 grid + bio) | Weekly |

**Keep/kill rule (4-week cycle):** any format used ≥4 times whose median reach sits below the account's overall median for 2 consecutive weeks is paused for 2 weeks and replaced by a stronger family member. Never judge a format on one post.

## 6.6 30-day rollout plan

| Week | Focus | Deliverables |
|---|---|---|
| **1** | Template library + slots | 6 locked Canva templates (§6.3); first 7 daily bulletins (F04) at 09:00; profile/bio rewrite; grid plan (F34) |
| **2** | Card consistency | F01/F03/F21 daily at 14:00; first 3 carousels (F02/F11); source-line and caption framework on 100% of posts |
| **3** | Discovery formats | First 2 Reels (F06) + 1 Stories sequence (F14); first F19 split card; poll (F29) once |
| **4** | Depth & review | F20 EXPLAINED + F18 timeline; F30 stat card; first metrics review (§6.5); keep/kill decisions; month-2 matrix adjustment |

**Growth ladder (expectations, grounded in the corpus):**
0→100 followers: consistency of slots and layout — the algorithm tests reliability. 100→1K: carousels and saves (F02/F11/F20) plus Reels (F06) become the growth engine. 1K→10K: add collaborations/reshares with credible pages, Stories polls, and one live segment per month if feasible. Expect the BBC lesson to hold: **relevance beats volume at every stage.**

## 6.7 Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Publishing a wrong fact | Medium | Severe (trust) | §6.4 two-source rule; F22 holding card; F23 corrections |
| Copyright strike (photo/video) | Medium | Severe (page penalty) | Free-stock-only pipeline; credit lines; no match footage |
| BREAKING-label fatigue | High | Medium (reach decay) | Label rules §3.5; audits weekly ("was that really breaking?") |
| Algorithm demotion of unoriginal reposts | High | Medium | Original design over reposts; screenshot-with-credit (F13) instead of re-uploads |
| Burnout at volume | High | Severe (consistency) | 2–3 posts/day cap; template library; batch production |
| Misattribution / fake screenshots | Medium | Severe | Verify source account; date the screenshot; debunk via F24 |
| Palette/design drift (incl. accidental green) | Medium | Low | Locked templates; §3.2 forbidden-colour list; pre-publish glance |
