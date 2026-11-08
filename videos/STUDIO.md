# GEOMETOR Elements — Video Studio Context (`STUDIO.md`)

This document defines the project-specific conventions, `.scr` script syntax, visual directives, and acoustic vocabulary for producing dual-format (`16:9` 2560x1440 QHD + `9:16` 1080x1920 Shorts) proposition videos in **`geometor/elements`**.

---

## 1. Directory & Package Layout

Every proposition video package lives in `videos/book_<b>/<nn>/` (e.g., `videos/book_i/01/`):

### Tier 1 — Git-Tracked Source & Manifests
* `script.scr` — Single source of truth with top-level metadata (`prop:`, `title:`, `g_id:`, `folio:`, `enunciation:`, `svg:`, `hide:`), `=== <section> ===` boundaries, `[screen: ...]` directives, `say:` narration lines, and `[sfx:...]` cues. Compiled directly in memory (`scenes.json` is not needed on disk).
* `youtube.json` — Canonical YouTube broadcast state (`long_id`, `short_id`, `playlist_id`, `published_at`).
* `<prefix>.srt` / `<prefix>.vtt` — Closed caption tracks.

### Tier 2 — Local Git-Ignored Master Media (Archived via `studio archive push` / `pull`)
All rendered binary masters stay directly in `videos/book_<b>/<nn>/` as real local files (no symlinks):
* `<prefix>_1080p.mp4` — `16:9` widescreen master rendered at native **`2560x1440` QHD** (`30 fps` CFR, H.264 High@L5.1 + AAC, triggers YouTube VP9).
* `<prefix>_short.mp4` — `9:16` vertical Short master rendered at native **`1080x1920`** (`30 fps` CFR, H.264 High@L4.1 + AAC).
* `<prefix>_thumb.png` / `<prefix>_short_thumb.png` (and `< 2 MB` `.jpg` versions) — Custom thumbnails.
* `<prefix>.wav` / `<prefix>.json` — Full master narration audio (`24000 Hz` PCM WAV) and subsegment timing manifest.
* `.tts_cache/` — Per-line cached PCM stems keyed by SHA-256 so editing a single `say:` line in `script.scr` only calls the TTS API for that changed line.

---

## 2. Rendering Mode: Slide Sequence (`slides`)

`elements` uses **Studio Mode 1 (`slides` — Native Vector Slide Sequencing)**:
* **Capture**: `1920x1080` CSS layout rasterized natively at **`2560x1440`** via Chromium `--force-device-scale-factor=1.3333333333` (`4/3`), and `1080x1920` for `9:16` Shorts.
* **Encode**: FFmpeg `-f concat` demuxer with exact per-slide audio durations from `<prefix>.json` and `-c:v libx264 -preset fast -tune stillimage -crf 18`.

---

## 3. Three-Act Proposition Structure (`script.scr`)

Every proposition `script.scr` is divided into three modular `=== <section> ===` blocks:

1. **`=== enunciation ===`**
   * Opens with `[bell:proposition]` and spoken proposition identifier.
   * States the general enunciation (`GIVEN` $\rightarrow$ `GOAL`).
2. **`=== construction ===`**
   * Opens with `[bell:construction]` and walks step-by-step through the compass-and-straightedge construction (`CONSTRUCT`, `INTERSECT`).
   * **Rule of One Construction Step per Sub-Slide**: Give each circle/segment locus (`[sfx:circle]` / `[sfx:segment]`) and each resulting intersection (`[sfx:intersect]`) its own `[screen: ...]` block and `say:` line.
3. **`=== demonstration ===`**
   * Opens with `[bell:insight]` and walks through the deductive proof chain (`ASSERT`, `∴`).
   * **Rule of One Equality per Sub-Slide**: Each radius equality or deductive step gets its own `[screen: ...]` block with `equal:` and `[sfx:equal]`, concluding with `[sfx:qed]`.

---

## 4. Symbolic Screen Notation & Automatic Defining-Point Rule

Inside `[screen: ...]` blocks, geometric elements are referenced using GEOMETOR symbolic notation (resolved in memory from the SVG's `data-ref` and `data-aliases` attributes):

| Element Type | Symbolic Notation | Automatic Defining-Point Rule |
| :--- | :--- | :--- |
| **Point** | `A`, `B`, `C` | Highlights point dot (`el-pt-A`) and label (`lbl-A`). |
| **Segment** | `/ A B /` | Automatically includes defining points `A, B` and strikes segment `/ A B /`. |
| **Line** | `[ A B ]` | Automatically includes defining points `A, B` and strikes line `[ A B ]`. |
| **Circle** | `( A B )` *(center `A`, radius pt `B`)* | Automatically includes defining points `A, B` and strikes circle `( A B )`. |
| **Polygon / Triangle** | `< A B C >` | Automatically includes vertices `A, B, C` and fills/strokes `< A B C >`. |

* **`show:`** — Elements visible on the canvas (`*` for all non-hidden elements).
* **`active:`** — Elements highlighted in gold (`geom-highlight-active`).
* **`equal:`** — Equal segments highlighted in green (`geom-assert-active`) with perpendicular equality tick marks (`geom-tick-1`) automatically applied.

---

## 5. Elements Acoustic Vocabulary (`[sfx:...]`)

| Cue | Geometric Event | Acoustic Character |
| :--- | :--- | :--- |
| `[bell:proposition]` | Act I (`enunciation`) Entry | Warm harmonic bell triad |
| `[bell:construction]` | Act II (`construction`) Entry | Construction bell chime |
| `[bell:insight]` | Act III (`demonstration`) Entry | Insight bell chime |
| `[sfx:point]` | Plotting or naming a point (`A`, `B`) | Crisp high harmonic pluck |
| `[sfx:segment]` | Drawing a straight line or segment (`/ A B /`) | Clean tensored string draw |
| `[sfx:circle]` | Sweeping a circle (`( A B )`) | Warm resonant arc sweep |
| `[sfx:intersect]` | Snapping an intersection point (`C`) | Crystalline two-tone lock |
| `[sfx:equal]` | Asserting equality with tick marks (`equal:`) | Consonance fifth chime (`3:2`) |
| `[sfx:qed]` | Final figure completion (`< A B C >`) | Resolved golden chord |

---

## 6. Build, Archive & Broadcast Commands

* **Build Dual-Format Proposition Video from `script.scr`**:
  ```bash
  uv run --no-sync python scripts/build_prop_video.py videos/book_i/01 --tts
  ```
* **Verify Package Integrity**:
  ```bash
  studio verify videos/book_i/01
  ```
* **Push / Pull Git-Ignored Master Media with Google Drive (`gdrive:PHOTON-MEDIA`)**:
  ```bash
  studio archive sync videos/ geometor/elements/videos --direction push
  studio archive sync videos/ geometor/elements/videos --direction pull
  ```
* **Upload / Sync to YouTube (`@geometor`)**:
  ```bash
  studio broadcast upload --book i --props 1
  ```
