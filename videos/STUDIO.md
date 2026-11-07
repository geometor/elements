# GEOMETOR Elements — Video Studio Context (`STUDIO.md`)

This document defines the project-specific conventions, script syntax, visual directives, and acoustic vocabulary for producing dual-format (`16:9` 1440p QHD + `9:16` 1080x1920 Shorts) proposition videos in **`geometor/elements`**.

---

## 1. Directory & Package Layout

Every proposition video package lives in `videos/book_<b>/<nn>/` (e.g., `videos/book_i/01/`):

### Tier 1 — Git-Tracked Source & Manifests
* `script.txt` — Canonical source script with `=== <section> ===` boundaries, `[screen: ...]` directives, `say:` narration lines, and `[sfx:...]` cues.
* `scenes.json` — Compiled sub-slide timing, highlights, ticks, and spoken transcript.
* `youtube.json` — Canonical YouTube broadcast state (`long_id`, `short_id`, `playlist_id`, `published_at`).

### Tier 2 — Vault-Linked Master Media (`/home/phi/MEDIA/geometor/elements/videos/book_<b>/<nn>/`)
* `<prop>.mp4` — `16:9` widescreen master (`2560x1440` QHD, H.264 + AAC).
* `<prop>_short.mp4` — `9:16` vertical Short master (`1080x1920`, H.264 + AAC).
* `<prop>_thumb.png` / `<prop>_short_thumb.png` — Custom thumbnails.
* `narration.wav` — Full concatenated master narration audio (`24000 Hz` PCM WAV).
* `sections/<section_id>.wav` — Per-section cached audio stems for incremental re-synthesis.

---

## 2. Three-Act Proposition Structure

Every proposition `script.txt` is divided into three modular `=== <section> ===` blocks so individual sections can be updated and re-synthesized without regenerating the entire proposition:

1. **`=== enunciation ===`**
   * Opens with the series signature bell (`[bell:E4,B4,G#5@2.0]`) and proposition identifier (`Book 1. Proposition 1.`).
   * States Heath's general enunciation clearly while progressively revealing the given elements on the canvas.
2. **`=== construction ===`**
   * Walks step-by-step through the compass-and-straightedge construction (`GIVEN`, `CONSTRUCT`, `INTERSECT`).
   * **Rule of One Construction Step per Sub-Slide**: Never combine a circle/line construction and its resulting intersection point into the same `[screen: ...]` block. Let the eye see the locus appear (`[sfx:circle]` or `[sfx:segment]`), then snap to the intersection (`[sfx:intersect]`).
   * **Inline Citations**: When a step invokes a Postulate or prior Proposition (`Post. 1`, `Post. 3`, `I.1`), display `badge: <citation>` and speak the justification concisely.
3. **`=== demonstration ===`**
   * Walks through the deductive proof chain (`PROVE`, `QED`).
   * **Rule of One Equality per Sub-Slide**: Each radius equality or deductive link gets its own `[screen: ...]` block with `ticks:` and `[sfx:equal]`, building up to the final synthesis (`[sfx:qed]`) and closing harmonic triad.

---

## 3. Symbolic Screen Notation (`[screen: ...]`)

Inside `[screen: ...]` blocks, geometric elements are referenced using GEOMETOR symbolic notation (resolved automatically against `elements.db` and `euclid` SVG IDs):

| Element Type | Symbolic Notation | Example | Resolved SVG ID |
| :--- | :--- | :--- | :--- |
| **Point** | `A`, `B`, `C` | `A, B` | `pt_A`, `pt_B` |
| **Segment** | `/ A B /` | `/ A B /, / A C /` | `seg_AB`, `seg_AC` |
| **Line** | `[ A B ]` | `[ A B ]` | `line_AB` |
| **Circle** | `( A B C )` *(center `B` through `A`, `C`)* | `( C A D )` | `circ_A_CD` |
| **Polygon / Triangle** | `< A B C >` | `< A B C >` | `poly_ABC` |
| **Angle** | `^ A B C ^` | `^ A B C ^` | `ang_ABC` |

### Screen Block Directives

```text
[screen: construction_step_2]
  show: A, B, / A B /
  highlight: ( C A D )
  ticks: / A B / = 1, / A C / = 1
  clause: "With center A and radius A B, describe the circle B C D."
  badge: Post. 3
say: [sfx:circle] From center A, with radius A B, draw circle B C D. By Postulate 3. [pause:0.4]
```

* `show:` — Elements visible on the canvas in their base color (`given` or `construct`).
* `highlight:` — Elements actively emphasized with a luminous gold halo on this sub-slide.
* `ticks:` — Green equality tick marks (`= 1`, `= 2`, `= 3`) drawn perpendicular to equal segments.
* `clause:` — Exact proof clause displayed in the typography card.
* `badge:` — Prerequisite pill (`Def. 15`, `Post. 1`, `Post. 3`, `C.N. 1`, `I.1`, etc.).

---

## 4. Elements Acoustic Vocabulary (`[sfx:...]`)

Every visual transition in `elements` is paired with a synthesized harmonic cue so the viewer hears the type of geometric operation occurring on screen:

| Cue | Geometric Event | Acoustic Character |
| :--- | :--- | :--- |
| `[bell:E4,B4,G#5@2.0]` | Proposition Entry Signature | Warm E-major harmonic bell triad |
| `[sfx:point]` | Plotting or naming a point (`A`, `B`) | Crisp high harmonic pluck |
| `[sfx:segment]` | Drawing a straight line or segment (`/ A B /`) | Clean tensored string draw |
| `[sfx:circle]` | Sweeping a circle (`( C A D )`) | Warm resonant arc sweep |
| `[sfx:intersect]` | Snapping an intersection point (`C`) | Crystalline two-tone lock |
| `[sfx:equal]` | Asserting equality with tick marks (`ticks:`) | Consonance fifth chime (`3:2`) |
| `[sfx:qed]` | Final figure completion (`< A B C >`) | Resolved golden chord |
| `[pause:0.4]` | Intentional breathing space between steps | Exact silence (`0.4s`) |

---

## 5. Build & Broadcast Commands

* **Build Dual-Format Proposition Video**:
  ```bash
  uv run --no-sync python scripts/build_prop_video.py --book i --prop 1
  ```
* **Verify Package Integrity**:
  ```bash
  studio verify --project elements
  ```
* **Link Master Binaries to `/home/phi/MEDIA` Vault**:
  ```bash
  studio archive link --project elements --execute
  ```
* **Upload / Sync to YouTube (`@geometor`)**:
  ```bash
  studio broadcast upload --project elements --prop I.1
  ```
