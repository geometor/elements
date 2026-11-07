#!/usr/bin/env python3
"""Rebuild or synthesize + render a proposition video folder in videos/book_<b>/<nn>/.

Usage:
  # Render 9:16 Short + 16:9 1080p + .srt/.vtt + youtube.txt from existing <prefix>.wav/.json:
  python3 scripts/build_prop_video.py videos/book_i/01

  # Also re-synthesize <prefix>.wav from script.txt via Gemini TTS API:
  python3 scripts/build_prop_video.py videos/book_i/01 --tts
"""

import argparse
from pathlib import Path
import subprocess
import sys

SPEAK_PY = Path("/home/phi/.gemini/config/skills/studio/scripts/speak.py")
SHORTS_PY = Path("/home/phi/.gemini/config/skills/studio/scripts/shorts.py")


def infer_prefix(prop_dir: Path) -> str:
  book_part = prop_dir.parent.name  # e.g. book_i
  num_part = prop_dir.name          # e.g. 01
  rom = book_part.replace("book_", "").upper()
  return f"{rom}_{num_part}"


def main():
  parser = argparse.ArgumentParser(description="Build proposition 9:16 + 16:9 videos, CC, and YouTube metadata.")
  parser.add_argument("prop_dir", type=Path, help="Path to proposition video directory (e.g. videos/book_i/01)")
  parser.add_argument("--prefix", help="Optional filename prefix (defaults to <BOOK>_<NN>, e.g. I_01)")
  parser.add_argument("--tts", action="store_true", help="Synthesize <prefix>.wav and <prefix>.json from script.txt first")
  parser.add_argument("--keep-scratch", action="store_true", help="Keep Tier 3 scratch (*_stage.html, slides_*/)")
  args = parser.parse_args()

  prop_dir = args.prop_dir.resolve()
  prefix = args.prefix or infer_prefix(prop_dir)

  studio_src = Path("/home/phi/PROJECTS/photon-platform/studio/src")
  if studio_src.exists():
    sys.path.insert(0, str(studio_src))
    from photon_platform.studio.render import render_package

    res = render_package(
        prop_dir,
        prefix=prefix,
        tts=args.tts,
        purge_scratch=not args.keep_scratch,
    )
    if res.get("status") != "ok":
      raise SystemExit(f"Render/verification failed: {res}")
    return

  script_txt = prop_dir / "script.txt"
  scenes_json = prop_dir / "scenes.json"
  wav_path = prop_dir / f"{prefix}.wav"
  manifest_json = prop_dir / f"{prefix}.json"

  if args.tts or not wav_path.exists() or not manifest_json.exists():
    if not script_txt.exists():
      raise FileNotFoundError(f"Missing {script_txt}")
    subprocess.run(
        [sys.executable, str(SPEAK_PY), "-f", str(script_txt), "-o", str(wav_path)],
        check=True,
    )

  if not scenes_json.exists():
    raise FileNotFoundError(f"Missing {scenes_json}")

  subprocess.run(
      [
          sys.executable,
          str(SHORTS_PY),
          "-s",
          str(scenes_json),
          "-m",
          str(manifest_json),
          "-o",
          str(prop_dir),
          "-p",
          prefix,
      ],
      check=True,
  )


if __name__ == "__main__":
  main()

