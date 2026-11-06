# GEOMETOR Video Formatting, Encoding & YouTube Publishing Specification

This document codifies the battle-tested dual-format (`9:16` Vertical Shorts + `16:9` 1440p QHD Widescreen) video rendering, `ffmpeg` encoding, and YouTube Data API v3 publishing pipeline developed in `geometor/elements` for portability across all **GEOMETOR**, **PHOTON Platform**, and **Harmonic Resonance** repositories.

---

## 1. Architecture Overview (Dual-Track 5-Bell Pipeline)

From a single spoken script (`script.txt`) and scene specification (`scenes.json`), the pipeline produces two synchronized videos from one voice synthesis pass:

| Track | Aspect Ratio | Master Resolution | Content Scope | Target YouTube Surface |
| :--- | :--- | :--- | :--- | :--- |
| **Vertical Short** (`<prefix>_short.mp4`) | `9:16` | `1080 × 1920` (FHD Vertical) | **Bells 1–3**: Core presentation / step-by-step proof (`"widescreen_only": false`) | YouTube Shorts Feed (`youtube.com/shorts/<id>`) |
| **Widescreen QHD** (`<prefix>_1080p.mp4`) | `16:9` | `2560 × 1440` (1440p QHD) | **Bells 1–5**: Core presentation (`Bells 1–3`) + Historical/Technical Commentary, Dependency Genealogy & Code, and Call-to-Action (`Bells 4–5`, `"widescreen_only": true`) | Main YouTube Watch Page (`youtu.be/<id>`) & Embedded Sphinx Codex |

### Why `16:9` Widescreen is Mastered at `2560 × 1440` (1440p QHD)
When `1920 × 1080` slide-based videos with low inter-frame motion are uploaded to YouTube, YouTube routes them to its legacy `avc1` transcode ladder and frequently defaults viewer playback to blurry `240p` or `360p`.

By upscaling the `1920 × 1080` Chromium master frames to **`2560 × 1440` (`scale=2560:1440:flags=lanczos`)** during `ffmpeg` assembly:
1. YouTube automatically routes the video into its **7-rung hardware `vp09` (VP9) + H.264 ladder (`144p`, `240p`, `360p`, `480p`, `720p`, `1080p`, `1440p`)**.
2. Vector diagrams, hairline geometric strokes, and monospace code blocks remain razor-sharp with zero macroblocking.
3. Initial playback defaults immediately to **HD / QHD** instead of `240p`.

---

## 2. Stage 1 — Audio Synthesis & Subsegment Timing (`speak.py`)

- **Tool**: `/home/phi/.gemini/config/skills/dialogue/scripts/speak.py`
- **Voice**: `voice_xdhacg1pn1cq` (**Argon III-C**, Gemini 3.8 TTS)
- **Output**:
  - `<prefix>.wav`: `24 kHz` mono PCM master (re-encoded to `48 kHz` stereo AAC `192 kbps` during MP4 muxing).
  - `<prefix>.json`: Timing manifest containing exact `start_sec`, `end_sec`, and `duration_sec` for every `[bell:...]` segment and paragraph `subsegment`.

### Command
```bash
python3 /home/phi/.gemini/config/skills/dialogue/scripts/speak.py \
  -f <dir>/script.txt \
  -o <dir>/<prefix>.wav
```

### Multi-Paragraph Subslide Synchronization
- Each `[bell:<name>]` cue in `script.txt` maps `1:1` to a top-level entry in `scenes.json`.
- Blank-line-separated paragraphs inside a bell segment map `1:1` to `subsegments` in `<prefix>.json` and `subslides` in `scenes.json`, giving exact per-step slide transitions without manual timestamp guessing.

---

## 3. Stage 2 — Isolated Headless Chromium Frame Rendering (`shorts.py`)

To run multiple render workers in parallel without Chromium profile locks, `/dev/shm` exhaustion, or GPU cache corruption, each slide is rendered in an isolated ephemeral profile and cropped to exact pixel dimensions:

```python
cmd = [
    chrome_binary,
    "--headless=new",
    f"--user-data-dir={tmp_root / 'profile'}",
    "--disk-cache-size=1",
    "--media-cache-size=1",
    "--aggressive-cache-discard",
    "--disable-application-cache",
    "--allow-file-access-from-files",
    "--no-sandbox",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    f"--window-size={width},{height + 100}",
    f"--virtual-time-budget={wait_ms}",
    f"--screenshot={raw_png}",
    f"file://{html_path.resolve()}",
]
```
Followed by an exact viewport crop via ImageMagick:
```bash
/usr/bin/convert _raw_slide.png -crop "${width}x${height}+0+0" +repage slide.png
```

- **`9:16` Short Slides**: `1080 × 1920` (`slides_9x16/slide_XX.png`)
- **`16:9` Widescreen Slides**: `1920 × 1080` (`slides_16x9/slide_XX.png`)
- **Thumbnails**: Rendered automatically from the punchline scene (`"is_punchline": true`) at both `1920 × 1080` (`<prefix>_thumb.png`) and `1080 × 1920` (`<prefix>_short_thumb.png`).

---

## 4. Stage 3 — Production `ffmpeg` Encoding Specification

Earlier experiments with raw `-f concat` slide decks failed YouTube processing or stuttered on mobile because sparse slide inputs produce variable-framerate (VFR) streams with huge keyframe gaps.

Our production `assemble_mp4()` function in `/home/phi/.gemini/config/skills/shorts/scripts/shorts.py` enforces **Constant Frame Rate (`30 fps`)**, **Closed 3-Second GOPs (`-g 90`)**, **BT.709 Color Signaling**, and **Faststart MOOV Atoms**:

### A. Concat Demuxer Input (`_<stem>_concat.txt`)
Every slide duration is clamped to `>= 0.400s`, and the final PNG is repeated on a trailing `file '...'` line (required by `ffmpeg`'s `concat` demuxer so the last slide's duration is honored):
```text
file '/abs/path/slides_16x9/slide_00.png'
duration 13.711
file '/abs/path/slides_16x9/slide_01.png'
duration 9.048
...
file '/abs/path/slides_16x9/slide_11.png'
```

### B. Exact `ffmpeg` Command — `9:16` Vertical Short (`1080 × 1920`)
Truncates cleanly at `total_dur` (the sum of non-`widescreen_only` slides) so the Short ends right after the conclusion punchline:
```bash
/usr/bin/ffmpeg -y \
  -f concat -safe 0 -i _short_concat.txt \
  -i <prefix>.wav \
  -c:a aac -ar 48000 -ac 2 -b:a 192k -shortest \
  -t <short_total_dur> \
  -vf "fps=30,setsar=1:1,format=yuv420p" \
  -vsync cfr -r 30 \
  -c:v libx264 -preset fast -profile:v high -level:v 4.1 \
  -crf 18 -maxrate 10M -bufsize 20M \
  -g 90 -keyint_min 90 -sc_threshold 0 -bf 2 -flags +cgop \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart \
  <prefix>_short.mp4
```

### C. Exact `ffmpeg` Command — `16:9` Widescreen QHD (`2560 × 1440`)
Upscales with `lanczos` to `2560 × 1440` at H.264 Level `5.1` (`-maxrate 16M -bufsize 32M`) and includes the full audio track across all 5 bells:
```bash
/usr/bin/ffmpeg -y \
  -f concat -safe 0 -i _1080p_concat.txt \
  -i <prefix>.wav \
  -c:a aac -ar 48000 -ac 2 -b:a 192k -shortest \
  -t <wide_total_dur> \
  -vf "fps=30,scale=2560:1440:flags=lanczos,setsar=1:1,format=yuv420p" \
  -vsync cfr -r 30 \
  -c:v libx264 -preset fast -profile:v high -level:v 5.1 \
  -crf 18 -maxrate 16M -bufsize 32M \
  -g 90 -keyint_min 90 -sc_threshold 0 -bf 2 -flags +cgop \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart \
  <prefix>_1080p.mp4
```

### Key Parameter Rationale
| Flag | Value | Why It Matters for YouTube |
| :--- | :--- | :--- |
| `-vf scale=2560:1440:flags=lanczos` | `2560×1440` (Wide) | Triggers YouTube's `vp09` (VP9) transcode ladder and HD default playback. |
| `-vsync cfr -r 30` + `fps=30` | `30.00 fps` constant | Eliminates VFR timestamp drift between static slides and AAC audio. |
| `-g 90 -keyint_min 90 -sc_threshold 0` | Fixed 3.0s GOP | Guarantees a seekable I-frame every 90 frames (`3.0s`) even on static slides. |
| `-flags +cgop -bf 2` | Closed GOP, 2 B-frames | Matches YouTube's recommended broadcast ingest spec (`High@L4.1` / `High@L5.1`). |
| `-crf 18 -maxrate 16M -bufsize 32M` | Visually lossless | Keeps text/SVG edges pristine while bounding peak bitrate for streaming. |
| `-colorspace bt709 ... -color_range tv` | Rec.709 Limited | Prevents dark-mode background gamma shifts (`#0b0d13`) across browsers. |
| `-c:a aac -ar 48000 -ac 2 -b:a 192k` | `48 kHz` Stereo AAC | Prevents mono phase issues and resampler artifacts on YouTube mobile players. |
| `-movflags +faststart` | Front-loaded `moov` | Enables instant streaming and rapid YouTube ingest check completion. |

---

## 5. Stage 4 — Resilient YouTube Upload, Scheduling & Quota Optimization (`upload_youtube.py`)

- **Tool**: `/home/phi/PROJECTS/geometor/elements/scripts/upload_youtube.py`

### A. IPv4 Resumable Chunked Upload (`4 MB` Chunks)
Standard Python HTTP libraries frequently hang on broken IPv6 routes when uploading media to `www.googleapis.com`. `upload_youtube.py` uses `curl -4 --resolve www.googleapis.com:443:172.217.117.4` with **4 MB resumable `PUT` chunks** and automatic `HTTP 308 Resume Incomplete` range recovery, plus JPEG thumbnail compression (`ffmpeg -y -i thumb.png -q:v 4 thumb.jpg`) so thumbnails upload in `< 2 seconds`.

### B. Google Cloud API Quota Management (`100 Uploads/Day` vs `10,000 Queries/Day`)
Google Cloud Console enforces two separate daily counters (resetting at **`00:00 PST` midnight Pacific Time**):
1. **`Video Uploads per day` (`100` uploads/day)**: Governs `videos.insert` media uploads.
2. **`Queries per day` (`10,000` units/day)**: Governs metadata, thumbnails (`50` units), playlists (`50` units), and `.srt` captions (`400` units).

**Critical Optimization**:
- Uploading `.srt` captions via the API costs **`400` units per video** (`800` units per dual-format proposition), which exhausts the `10,000` query quota after just ~10 videos and blocks `50`-unit thumbnail and playlist calls.
- Because YouTube automatically generates accurate English captions for our Argon III-C narration at zero quota cost, `upload_youtube.py` defaults to **`--no-captions`** (with `--with-captions` available as an opt-in).
- With `--no-captions` enabled by default, each proposition (`16:9` + `9:16`) uses only **`100` units for thumbnails + `100` units for playlists**.

### C. Common CLI Workflows

1. **Upload & Schedule a Batch at Regular 4-Hour Intervals**:
   Automatically sets `privacyStatus="private"` and increments `publishAt` by `4` hours per proposition for both `16:9` and `9:16`:
   ```bash
   python3 scripts/upload_youtube.py \
     --book i --props 21-48 \
     --schedule-start 2026-11-05T16:00:00Z \
     --schedule-step-hours 4
   ```

2. **Sync Missing Thumbnails & Playlists (Zero Video Re-Upload)**:
   Reads `youtube.json` (`"thumbnail_set"` and `"playlist_item_id"`) and backfills only missing thumbnails and playlist entries:
   ```bash
   python3 scripts/upload_youtube.py \
     --book i --props 25-48 \
     --sync-missing
   ```

3. **Check Processing Status & Publish Immediately**:
   ```bash
   python3 scripts/upload_youtube.py \
     --book i --props 1-20 \
     --status --publish
   ```

4. **Replace an Existing Video with a New Take (`vN+1`)**:
   Uploads the new MP4, swaps it into the same playlist position, unlists the old take with a `[vN]` title suffix, and archives the old ID in `youtube.json["history"]`:
   ```bash
   python3 scripts/upload_youtube.py \
     --book i --props 1 \
     --replace
   ```
