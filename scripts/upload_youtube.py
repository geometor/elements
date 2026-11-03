#!/usr/bin/env python3
"""Automated YouTube Data API v3 uploader for GEOMETOR Euclid proposition videos.

Supports:
- One-time OAuth 2.0 authorization & automatic token refresh (--auth)
- Resumable MP4 upload for both 16:9 (1080p) and 9:16 (Shorts)
- Custom thumbnail upload (I_XX_thumb.png and I_XX_short_thumb.png)
- Frame-accurate .srt closed-caption track upload (I_XX.srt)
- In-place metadata/thumbnail updates for already-uploaded videos (--update-meta)
- Persistent tracking of uploaded video IDs and URLs inside each prop's youtube.json
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

CONFIG_DIR = Path.home() / ".config" / "geometor"
DEFAULT_CLIENT_SECRET = CONFIG_DIR / "youtube_client_secret.json"
DEFAULT_TOKEN_PATH = CONFIG_DIR / "youtube_token.json"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

VIDEOS_Root = Path(__file__).resolve().parents[1] / "resources" / "videos"


def _load_client_config(client_secret_path: Path) -> dict:
  if not client_secret_path.exists():
    raise FileNotFoundError(
        f"OAuth client secret not found at: {client_secret_path}\n"
        "Save your Google Cloud Desktop OAuth client JSON there or pass --client-secret."
    )
  raw = json.loads(client_secret_path.read_text(encoding="utf-8"))
  cfg = raw.get("installed") or raw.get("web")
  if not cfg:
    raise ValueError(
        f"Invalid client_secret JSON in {client_secret_path}: expected 'installed' or 'web' key."
    )
  return cfg


def run_oauth_flow(
    client_secret_path: Path,
    token_path: Path,
    port: int = 8085,
) -> dict:
  """Runs local loopback OAuth 2.0 flow and saves refreshable token."""
  cfg = _load_client_config(client_secret_path)
  client_id = cfg["client_id"]
  client_secret = cfg["client_secret"]
  auth_uri = cfg.get("auth_uri", "https://accounts.google.com/o/oauth2/v2/auth")
  token_uri = cfg.get("token_uri", "https://oauth2.googleapis.com/token")
  redirect_uri = f"http://127.0.0.1:{port}"

  captured: dict[str, str] = {}

  class _CallbackHandler(BaseHTTPRequestHandler):

    def do_GET(self):  # noqa: N802
      parsed = urllib.parse.urlparse(self.path)
      qs = urllib.parse.parse_qs(parsed.query)
      if "code" in qs:
        captured["code"] = qs["code"][0]
        body = (
            "<html><body style='background:#0b0e15;color:#e8b85a;"
            "font-family:monospace;padding:40px;'>"
            "<h2>GEOMETOR YouTube Authorization Complete</h2>"
            "<p style='color:#f4f1ea;'>You can close this tab and return to the terminal.</p>"
            "</body></html>"
        )
        self.send_response(200)
      else:
        captured["error"] = qs.get("error", ["unknown_error"])[0]
        body = f"<html><body>Authorization failed: {captured['error']}</body></html>"
        self.send_response(400)
      self.send_header("Content-Type", "text/html; charset=utf-8")
      self.end_headers()
      self.wfile.write(body.encode("utf-8"))

    def log_message(self, format, *args):  # noqa: A002
      return

  params = {
      "client_id": client_id,
      "redirect_uri": redirect_uri,
      "response_type": "code",
      "scope": " ".join(SCOPES),
      "access_type": "offline",
      "prompt": "consent",
  }
  consent_url = f"{auth_uri}?{urllib.parse.urlencode(params)}"
  print("\n======================================================================")
  print("GEOMETOR YOUTUBE OAUTH 2.0 AUTHORIZATION")
  print("======================================================================")
  print("1. Opening browser to authorize https://www.youtube.com/@geometor ...")
  print("   (When prompted, select your Google account and choose the @geometor channel)")
  print(f"\n   URL: {consent_url}\n")

  server = HTTPServer(("127.0.0.1", port), _CallbackHandler)
  try:
    webbrowser.open(consent_url)
  except Exception:
    pass

  print(f"Waiting for OAuth callback on {redirect_uri} ...")
  server.handle_request()
  server.server_close()

  if "error" in captured or "code" not in captured:
    raise RuntimeError(
        f"OAuth authorization failed: {captured.get('error', 'no code received')}"
    )

  form = urllib.parse.urlencode({
      "code": captured["code"],
      "client_id": client_id,
      "client_secret": client_secret,
      "redirect_uri": redirect_uri,
      "grant_type": "authorization_code",
  }).encode("utf-8")

  req = urllib.request.Request(
      token_uri,
      data=form,
      headers={"Content-Type": "application/x-www-form-urlencoded"},
      method="POST",
  )
  with urllib.request.urlopen(req) as resp:
    token_data = json.loads(resp.read().decode("utf-8"))

  token_data["client_id"] = client_id
  token_data["client_secret"] = client_secret
  token_data["token_uri"] = token_uri
  token_data["expires_at"] = int(time.time()) + int(token_data.get("expires_in", 3600)) - 60

  token_path.parent.mkdir(parents=True, exist_ok=True)
  token_path.write_text(json.dumps(token_data, indent=2), encoding="utf-8")
  os.chmod(token_path, 0o600)
  print(f"Saved OAuth token to: {token_path}")

  channel = get_authenticated_channel(token_data["access_token"])
  if channel:
    snippet = channel.get("snippet", {})
    print(
        f"Connected Channel   : {snippet.get('title')} "
        f"({snippet.get('customUrl', channel.get('id'))})"
    )
  return token_data


def get_valid_access_token(
    client_secret_path: Path = DEFAULT_CLIENT_SECRET,
    token_path: Path = DEFAULT_TOKEN_PATH,
) -> str:
  """Loads token_path and automatically refreshes access_token if expired."""
  if not token_path.exists():
    raise FileNotFoundError(
        f"YouTube OAuth token not found at {token_path}.\n"
        f"Run `python3 {Path(__file__).name} --auth` first."
    )
  token_data = json.loads(token_path.read_text(encoding="utf-8"))
  now = int(time.time())
  if token_data.get("access_token") and now < int(token_data.get("expires_at", 0)) - 540:
    return token_data["access_token"]

  refresh_token = token_data.get("refresh_token")
  if not refresh_token:
    raise RuntimeError(
        f"Token in {token_path} has no refresh_token. Re-run with `--auth`."
    )

  client_id = token_data.get("client_id")
  client_secret = token_data.get("client_secret")
  token_uri = token_data.get("token_uri", "https://oauth2.googleapis.com/token")
  if not (client_id and client_secret):
    cfg = _load_client_config(client_secret_path)
    client_id = cfg["client_id"]
    client_secret = cfg["client_secret"]

  form = urllib.parse.urlencode({
      "client_id": client_id,
      "client_secret": client_secret,
      "refresh_token": refresh_token,
      "grant_type": "refresh_token",
  }).encode("utf-8")

  req = urllib.request.Request(
      token_uri,
      data=form,
      headers={"Content-Type": "application/x-www-form-urlencoded"},
      method="POST",
  )
  with urllib.request.urlopen(req) as resp:
    refreshed = json.loads(resp.read().decode("utf-8"))

  token_data["access_token"] = refreshed["access_token"]
  token_data["expires_at"] = int(time.time()) + int(refreshed.get("expires_in", 3600)) - 600
  if "refresh_token" in refreshed:
    token_data["refresh_token"] = refreshed["refresh_token"]

  token_path.write_text(json.dumps(token_data, indent=2), encoding="utf-8")
  os.chmod(token_path, 0o600)
  return token_data["access_token"]


def get_authenticated_channel(access_token: str) -> dict | None:
  url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&mine=true"
  req = urllib.request.Request(
      url,
      headers={"Authorization": f"Bearer {access_token}"},
      method="GET",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      items = data.get("items", [])
      return items[0] if items else None
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"Warning: could not query channel info ({e.code}): {err_body}")
    return None


def upload_video_resumable(
    access_token: str,
    mp4_path: Path,
    title: str,
    description: str,
    tags: list[str],
    category_id: str = "27",
    privacy_status: str = "unlisted",
) -> str:
  """Uploads an MP4 via YouTube Data API v3 resumable upload protocol and returns video_id."""
  file_size = mp4_path.stat().st_size
  metadata = {
      "snippet": {
          "title": title,
          "description": description,
          "tags": tags,
          "categoryId": str(category_id),
          "defaultLanguage": "en",
          "defaultAudioLanguage": "en",
      },
      "status": {
          "privacyStatus": privacy_status,
          "selfDeclaredMadeForKids": False,
      },
  }
  body_bytes = json.dumps(metadata).encode("utf-8")

  init_url = (
      "https://www.googleapis.com/upload/youtube/v3/videos"
      "?uploadType=resumable&part=snippet,status"
  )
  init_req = urllib.request.Request(
      init_url,
      data=body_bytes,
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "application/json; charset=UTF-8",
          "X-Upload-Content-Length": str(file_size),
          "X-Upload-Content-Type": "video/mp4",
      },
      method="POST",
  )
  try:
    with urllib.request.urlopen(init_req) as resp:
      upload_url = resp.headers.get("Location")
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    raise RuntimeError(f"Failed to initiate video upload ({e.code}): {err_body}") from e

  if not upload_url:
    raise RuntimeError("YouTube resumable upload did not return a Location header.")

  video_bytes = mp4_path.read_bytes()
  put_req = urllib.request.Request(
      upload_url,
      data=video_bytes,
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Length": str(file_size),
          "Content-Type": "video/mp4",
      },
      method="PUT",
  )
  try:
    with urllib.request.urlopen(put_req) as resp:
      result = json.loads(resp.read().decode("utf-8"))
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    raise RuntimeError(f"Failed uploading MP4 bytes ({e.code}): {err_body}") from e

  return result["id"]


def update_video_metadata(
    access_token: str,
    video_id: str,
    title: str,
    description: str,
    tags: list[str],
    category_id: str = "27",
    privacy_status: str = "unlisted",
) -> None:
  """Updates title, description, tags, and privacy status of an existing YouTube video."""
  metadata = {
      "id": video_id,
      "snippet": {
          "title": title,
          "description": description,
          "tags": tags,
          "categoryId": str(category_id),
          "defaultLanguage": "en",
          "defaultAudioLanguage": "en",
      },
      "status": {
          "privacyStatus": privacy_status,
          "selfDeclaredMadeForKids": False,
      },
  }
  url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,status"
  req = urllib.request.Request(
      url,
      data=json.dumps(metadata).encode("utf-8"),
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "application/json; charset=UTF-8",
      },
      method="PUT",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      resp.read()
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    raise RuntimeError(
        f"Failed updating metadata for {video_id} ({e.code}): {err_body}"
    ) from e


def upload_thumbnail(
    access_token: str,
    video_id: str,
    png_path: Path,
) -> None:
  """Uploads a custom PNG thumbnail for video_id."""
  if not png_path or not png_path.exists():
    return
  img_bytes = png_path.read_bytes()
  url = (
      "https://www.googleapis.com/upload/youtube/v3/thumbnails/set"
      f"?videoId={urllib.parse.quote(video_id)}&uploadType=media"
  )
  req = urllib.request.Request(
      url,
      data=img_bytes,
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "image/png",
          "Content-Length": str(len(img_bytes)),
      },
      method="POST",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      resp.read()
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Thumbnail upload warning for {video_id} ({e.code}): {err_body}")


def upload_captions_srt(
    access_token: str,
    video_id: str,
    srt_path: Path,
    language: str = "en",
    name: str = "English",
) -> str | None:
  """Uploads an .srt closed-caption track for video_id via multipart/related."""
  if not srt_path or not srt_path.exists():
    return None

  boundary = f"===============geometor_{int(time.time() * 1000)}=="
  snippet_json = json.dumps({
      "snippet": {
          "videoId": video_id,
          "language": language,
          "name": name,
          "isDraft": False,
      }
  }).encode("utf-8")
  srt_bytes = srt_path.read_bytes()

  parts = [
      f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n".encode("utf-8"),
      snippet_json,
      f"\r\n--{boundary}\r\nContent-Type: application/x-subrip; charset=UTF-8\r\n\r\n".encode(
          "utf-8"
      ),
      srt_bytes,
      f"\r\n--{boundary}--\r\n".encode("utf-8"),
  ]
  body = b"".join(parts)

  url = (
      "https://www.googleapis.com/upload/youtube/v3/captions"
      "?uploadType=multipart&part=snippet"
  )
  req = urllib.request.Request(
      url,
      data=body,
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": f'multipart/related; boundary="{boundary}"',
          "Content-Length": str(len(body)),
      },
      method="POST",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      return data.get("id")
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Captions upload warning for {video_id} ({e.code}): {err_body}")
    return None


def list_channel_playlists(access_token: str) -> dict[str, str]:
  """Returns {title: playlist_id} for the authenticated channel."""
  url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&mine=true&maxResults=50"
  req = urllib.request.Request(
      url,
      headers={"Authorization": f"Bearer {access_token}"},
      method="GET",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      return {
          item["snippet"]["title"]: item["id"]
          for item in data.get("items", [])
          if "snippet" in item and "id" in item
      }
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Could not list playlists ({e.code}): {err_body}")
    return {}


def create_playlist(
    access_token: str,
    title: str,
    description: str,
    privacy_status: str = "unlisted",
) -> str | None:
  """Creates a new YouTube playlist and returns its playlist_id."""
  payload = {
      "snippet": {
          "title": title,
          "description": description,
          "defaultLanguage": "en",
      },
      "status": {
          "privacyStatus": privacy_status,
      },
  }
  url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"
  req = urllib.request.Request(
      url,
      data=json.dumps(payload).encode("utf-8"),
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "application/json; charset=UTF-8",
      },
      method="POST",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      return data.get("id")
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Playlist creation warning for '{title}' ({e.code}): {err_body}")
    return None


def ensure_book_playlists(
    access_token: str,
    book_rom: str = "I",
    privacy_status: str = "unlisted",
) -> tuple[str | None, str | None]:
  """Ensures separate 16:9 and 9:16 Shorts playlists exist for Book <book_rom>."""
  reg_path = VIDEOS_Root / "playlists.json"
  reg: dict = {}
  if reg_path.exists():
    try:
      reg = json.loads(reg_path.read_text(encoding="utf-8"))
    except Exception:
      reg = {}

  book_key = f"book_{book_rom.lower()}"
  book_entry = reg.setdefault(book_key, {})

  title_1080p = f"Euclid's Elements • Book {book_rom.upper()}"
  title_short = f"Euclid's Elements • Book {book_rom.upper()} • Shorts"

  desc_1080p = (
      f"Step-by-step geometric constructions and proofs from Book {book_rom.upper()} "
      "of Euclid's Elements (1908 Heath Edition + GEOMETOR G-Index)."
  )
  desc_short = (
      f"Vertical 9:16 Shorts walking step-by-step through every proposition of Book {book_rom.upper()} "
      "of Euclid's Elements (1908 Heath Edition + GEOMETOR G-Index)."
  )

  pl_1080p = book_entry.get("wide_1080p", {}).get("id")
  pl_short = book_entry.get("short", {}).get("id")

  if not pl_1080p or not pl_short:
    existing_map = list_channel_playlists(access_token)
    if not pl_1080p:
      pl_1080p = existing_map.get(title_1080p)
    if not pl_short:
      pl_short = existing_map.get(title_short)

  if not pl_1080p:
    print(f"Creating 16:9 Playlist : {title_1080p} ...")
    pl_1080p = create_playlist(access_token, title_1080p, desc_1080p, privacy_status)
    if pl_1080p:
      print(f"  → Created: https://www.youtube.com/playlist?list={pl_1080p}")

  if not pl_short:
    print(f"Creating 9:16 Playlist : {title_short} ...")
    pl_short = create_playlist(access_token, title_short, desc_short, privacy_status)
    if pl_short:
      print(f"  → Created: https://www.youtube.com/playlist?list={pl_short}")

  if pl_1080p:
    book_entry["wide_1080p"] = {
        "id": pl_1080p,
        "title": title_1080p,
        "url": f"https://www.youtube.com/playlist?list={pl_1080p}",
    }
  if pl_short:
    book_entry["short"] = {
        "id": pl_short,
        "title": title_short,
        "url": f"https://www.youtube.com/playlist?list={pl_short}",
    }

  reg_path.parent.mkdir(parents=True, exist_ok=True)
  reg_path.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")
  return pl_1080p, pl_short


def find_playlist_item(
    access_token: str,
    playlist_id: str,
    video_id: str,
) -> tuple[str | None, int | None]:
  """Finds (playlist_item_id, position) of video_id inside playlist_id."""
  url = (
      "https://www.googleapis.com/youtube/v3/playlistItems"
      f"?part=snippet&playlistId={urllib.parse.quote(playlist_id)}"
      f"&videoId={urllib.parse.quote(video_id)}&maxResults=5"
  )
  req = urllib.request.Request(
      url,
      headers={"Authorization": f"Bearer {access_token}"},
      method="GET",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      items = data.get("items", [])
      if items:
        item = items[0]
        return item.get("id"), item.get("snippet", {}).get("position")
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Playlist lookup warning for {video_id} ({e.code}): {err_body}")
  return None, None


def delete_playlist_item(
    access_token: str,
    playlist_item_id: str,
) -> bool:
  """Removes a playlistItem by its ID."""
  url = (
      "https://www.googleapis.com/youtube/v3/playlistItems"
      f"?id={urllib.parse.quote(playlist_item_id)}"
  )
  req = urllib.request.Request(
      url,
      headers={"Authorization": f"Bearer {access_token}"},
      method="DELETE",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      resp.read()
    return True
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(
        f"  [!] Playlist item delete warning for {playlist_item_id} ({e.code}): {err_body}"
    )
    return False


def add_video_to_playlist(
    access_token: str,
    playlist_id: str,
    video_id: str,
    position: int | None = None,
) -> str | None:
  """Inserts video_id into a YouTube playlist (optionally at position) and returns playlist_item_id."""
  snippet: dict = {
      "playlistId": playlist_id,
      "resourceId": {
          "kind": "youtube#video",
          "videoId": video_id,
      },
  }
  if position is not None:
    snippet["position"] = int(position)
  payload = {"snippet": snippet}
  url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet"
  req = urllib.request.Request(
      url,
      data=json.dumps(payload).encode("utf-8"),
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "application/json; charset=UTF-8",
      },
      method="POST",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      data = json.loads(resp.read().decode("utf-8"))
      return data.get("id")
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Playlist insert warning for {video_id} ({e.code}): {err_body}")
    return None


def process_proposition_dir(
    prop_dir: Path,
    access_token: str | None,
    target: str = "both",
    privacy_override: str | None = None,
    playlist_1080p: str | None = None,
    playlist_short: str | None = None,
    update_meta_only: bool = False,
    update_thumb: bool = False,
    replace_existing: bool = False,
    sync_missing: bool = False,
    skip_captions: bool = False,
    force: bool = False,
    dry_run: bool = False,
) -> None:
  yt_json_path = prop_dir / "youtube.json"
  if not yt_json_path.exists():
    print(f"[SKIP] No youtube.json found in {prop_dir}")
    return

  meta = json.loads(yt_json_path.read_text(encoding="utf-8"))
  short_code = meta.get("short_code", prop_dir.name)
  files = meta.get("files", {})
  privacy = privacy_override or meta.get("privacyStatus", "unlisted")
  category_id = str(meta.get("categoryId", "27"))
  tags = meta.get("tags", [])
  description = meta.get("description", "")
  srt_path = Path(files["captions_srt"]) if files.get("captions_srt") else None
  uploads = meta.setdefault("uploads", {})
  history = meta.setdefault("history", {})

  variants = []
  if target in ("both", "1080p"):
    variants.append({
        "key": "wide_1080p",
        "label": "16:9 1080p",
        "title": meta.get("title_1080p", f"{short_code} • Euclid's Elements"),
        "mp4": Path(files["wide_1080p_mp4"]),
        "thumb": (
            Path(files["thumbnail_16x9_png"])
            if files.get("thumbnail_16x9_png")
            else None
        ),
        "playlist": playlist_1080p,
        "url_fmt": "https://youtu.be/{vid}",
    })
  if target in ("both", "short"):
    variants.append({
        "key": "short",
        "label": "9:16 Short",
        "title": meta.get("title_short", f"{short_code} • Euclid's Elements"),
        "mp4": Path(files["short_mp4"]),
        "thumb": (
            Path(files["thumbnail_9x16_png"])
            if files.get("thumbnail_9x16_png")
            else None
        ),
        "playlist": playlist_short,
        "url_fmt": "https://youtube.com/shorts/{vid}",
    })

  print(f"\n======================================================================")
  print(f"PROPOSITION {short_code} ({meta.get('g_id', '')}) — {prop_dir}")
  print(f"======================================================================")

  for v in variants:
    key = v["key"]
    existing = uploads.get(key, {})
    existing_vid = existing.get("video_id")
    old_version = int(existing.get("version", 1))
    meta_version = int(meta.get("version", 2 if existing_vid else 1))
    new_version = (
        max(meta_version, old_version + 1)
        if (existing_vid and replace_existing)
        else meta_version
    )

    if dry_run:
      print(f"  [DRY-RUN] {v['label']} (v{new_version})")
      print(f"    Title     : {v['title']}")
      print(f"    MP4       : {v['mp4'].name} ({v['mp4'].stat().st_size / 1024:.1f} KB)")
      print(f"    Thumbnail : {v['thumb'].name if v['thumb'] else 'None'}")
      print(f"    Captions  : {srt_path.name if (srt_path and not skip_captions) else 'None'}")
      print(f"    Privacy   : {privacy}")
      if existing_vid:
        action = (
            f"REPLACE & UNLIST [v{old_version}]"
            if replace_existing
            else "EXISTING"
        )
        print(f"    {action:9s} : {existing_vid} ({existing.get('url')})")
      continue

    access_token = get_valid_access_token()
    assert access_token is not None

    if sync_missing:
      if not existing_vid:
        print(f"  [SKIP] {v['label']} has not been uploaded yet; cannot --sync-missing.")
        continue
      print(f"  [SYNC] Syncing missing thumbnail/captions/playlist for {v['label']} ({existing_vid}) ...")
      if v["thumb"] and v["thumb"].exists():
        print(f"  [THUMB] Setting custom thumbnail: {v['thumb'].name} ...")
        upload_thumbnail(access_token, existing_vid, v["thumb"])
      if not skip_captions and not existing.get("caption_id") and srt_path and srt_path.exists():
        print(f"  [CC] Uploading closed captions: {srt_path.name} ...")
        existing["caption_id"] = upload_captions_srt(access_token, existing_vid, srt_path)
      prev_list = history.get(key, [])
      prev_entry = prev_list[-1] if prev_list else None
      prev_vid = prev_entry.get("video_id") if prev_entry else None
      prev_ver = prev_entry.get("version", old_version - 1) if prev_entry else (old_version - 1)
      if v["playlist"]:
        old_pl_item_id = None
        old_pos = None
        if prev_vid:
          old_pl_item_id, old_pos = find_playlist_item(
              access_token, v["playlist"], prev_vid
          )
        if not existing.get("playlist_item_id"):
          pos_label = f" at position {old_pos}" if old_pos is not None else ""
          print(f"  [PLAYLIST] Adding {existing_vid} to playlist {v['playlist']}{pos_label} ...")
          existing["playlist_item_id"] = add_video_to_playlist(
              access_token, v["playlist"], existing_vid, position=old_pos
          )
        if old_pl_item_id:
          print(
              f"  [PLAYLIST] Removing superseded v{prev_ver} ({prev_vid}) from playlist ..."
          )
          delete_playlist_item(access_token, old_pl_item_id)
      if prev_vid:
        old_title = f"{v['title']} [v{prev_ver}]"
        if len(old_title) > 100:
          old_title = f"{v['title'][:93]} [v{prev_ver}]"
        old_desc = f"Superseded by v{old_version}.\n\n{description}"
        print(
            f"  [UNLIST] Unlisting superseded v{prev_ver} ({prev_vid}) as '{old_title}' ..."
        )
        try:
          update_video_metadata(
              access_token=access_token,
              video_id=prev_vid,
              title=old_title,
              description=old_desc,
              tags=tags,
              category_id=category_id,
              privacy_status="unlisted",
          )
        except Exception as e:
          print(f"  [!] Warning unlisting {prev_vid}: {e}")
      existing["updated_at"] = datetime.now(timezone.utc).isoformat()
      yt_json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
      print(f"  [OK] Synced {existing.get('url')}")
      continue

    if update_meta_only:
      if not existing_vid:
        print(f"  [SKIP] {v['label']} has not been uploaded yet; cannot --update-meta.")
        continue
      print(f"  [UPDATE] Updating metadata for {v['label']} ({existing_vid}) ...")
      update_video_metadata(
          access_token=access_token,
          video_id=existing_vid,
          title=v["title"],
          description=description,
          tags=tags,
          category_id=category_id,
          privacy_status=privacy,
      )
      if update_thumb and v["thumb"]:
        upload_thumbnail(access_token, existing_vid, v["thumb"])
      existing["privacyStatus"] = privacy
      existing["updated_at"] = datetime.now(timezone.utc).isoformat()
      yt_json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
      print(f"  [OK] Updated {existing.get('url')}")
      continue

    if existing_vid and not (force or replace_existing):
      print(
          f"  [SKIP] {v['label']} already uploaded: {existing.get('url')} "
          "(use --replace to upload new version & unlist previous, or --update-meta)"
      )
      continue

    print(f"  [UPLOAD] Uploading {v['label']} (v{new_version}): {v['mp4'].name} ...")
    try:
      vid = upload_video_resumable(
          access_token=access_token,
          mp4_path=v["mp4"],
          title=v["title"],
          description=description,
          tags=tags,
          category_id=category_id,
          privacy_status=privacy,
      )
    except RuntimeError as e:
      if "uploadLimitExceeded" in str(e):
        print(
            f"  [LIMIT] YouTube daily upload limit reached for @geometor while uploading {short_code} ({v['label']}).\n"
            f"          Re-run `python3 scripts/upload_youtube.py --props {short_code.split('.')[-1]} --target {target} --replace` "
            "once the 24h rolling window resets or Advanced Features verification completes."
        )
        return False
      if "quotaExceeded" in str(e):
        print(
            f"  [QUOTA] Google Cloud YouTube Data API v3 daily quota (10,000 units) reached while uploading {short_code} ({v['label']}).\n"
            "          Quota resets at midnight Pacific Time (00:00 America/Los_Angeles)."
        )
        return False
      raise
    url = v["url_fmt"].format(vid=vid)
    print(f"  [OK] Video ID  : {vid} → {url}")

    now_iso = datetime.now(timezone.utc).isoformat()

    # If replacing an existing take, archive the old record in history first
    if existing_vid and replace_existing:
      archived = dict(existing)
      archived["version"] = old_version
      archived["privacyStatus"] = "unlisted"
      archived["superseded_by"] = vid
      archived["superseded_at"] = now_iso
      history.setdefault(key, []).append(archived)

    meta["version"] = new_version
    uploads[key] = {
        "version": new_version,
        "video_id": vid,
        "url": url,
        "studio_url": f"https://studio.youtube.com/video/{vid}/edit",
        "caption_id": None,
        "playlist_id": v["playlist"],
        "playlist_item_id": None,
        "privacyStatus": privacy,
        "uploaded_at": now_iso,
    }
    yt_json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    access_token = get_valid_access_token()

    if v["thumb"] and v["thumb"].exists():
      print(f"  [THUMB] Setting custom thumbnail: {v['thumb'].name} ...")
      upload_thumbnail(access_token, vid, v["thumb"])

    caption_id = None
    if not skip_captions and srt_path and srt_path.exists():
      print(f"  [CC] Uploading closed captions: {srt_path.name} ...")
      caption_id = upload_captions_srt(access_token, vid, srt_path)

    pl_item_id = None
    if v["playlist"]:
      old_pl_item_id = None
      old_pos = None
      if existing_vid and replace_existing:
        old_pl_item_id, old_pos = find_playlist_item(
            access_token, v["playlist"], existing_vid
        )
      pos_label = f" at position {old_pos}" if old_pos is not None else ""
      print(f"  [PLAYLIST] Adding {vid} to playlist {v['playlist']}{pos_label} ...")
      pl_item_id = add_video_to_playlist(
          access_token, v["playlist"], vid, position=old_pos
      )
      if old_pl_item_id:
        print(
            f"  [PLAYLIST] Removing superseded v{old_version} ({existing_vid}) from playlist ..."
        )
        delete_playlist_item(access_token, old_pl_item_id)

    if existing_vid and replace_existing:
      old_title = f"{v['title']} [v{old_version}]"
      if len(old_title) > 100:
        old_title = f"{v['title'][:93]} [v{old_version}]"
      old_desc = f"Superseded by v{new_version}.\n\n{description}"
      print(
          f"  [UNLIST] Unlisting superseded v{old_version} ({existing_vid}) as '{old_title}' ..."
      )
      try:
        update_video_metadata(
            access_token=access_token,
            video_id=existing_vid,
            title=old_title,
            description=old_desc,
            tags=tags,
            category_id=category_id,
            privacy_status="unlisted",
        )
      except Exception as e:
        print(f"  [!] Warning unlisting {existing_vid}: {e}")

    uploads[key]["caption_id"] = caption_id
    uploads[key]["playlist_item_id"] = pl_item_id
    yt_json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def get_videos_status(
    access_token: str,
    video_ids: list[str],
) -> dict[str, dict]:
  """Queries status and processingDetails for up to 50 video IDs in a single 1-unit API call."""
  if not video_ids:
    return {}
  out: dict[str, dict] = {}
  for i in range(0, len(video_ids), 50):
    batch = [vid for vid in video_ids[i : i + 50] if vid]
    if not batch:
      continue
    ids_param = urllib.parse.quote(",".join(batch))
    url = (
        "https://www.googleapis.com/youtube/v3/videos"
        f"?part=status,processingDetails,snippet&id={ids_param}"
    )
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {access_token}"},
        method="GET",
    )
    try:
      with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        for item in data.get("items", []):
          vid = item.get("id")
          st = item.get("status", {})
          pr = item.get("processingDetails", {})
          up_status = st.get("uploadStatus", "unknown")
          proc_status = pr.get("processingStatus")
          priv_status = st.get("privacyStatus", "unknown")
          is_ready = up_status == "processed" and proc_status in (
              "succeeded",
              None,
          )
          out[vid] = {
              "upload_status": up_status,
              "processing_status": proc_status or "succeeded"
              if up_status == "processed"
              else (proc_status or "processing"),
              "privacy_status": priv_status,
              "rejection_reason": st.get("rejectionReason"),
              "failure_reason": pr.get("processingFailureReason"),
              "is_ready": is_ready,
              "snippet": item.get("snippet", {}),
          }
    except urllib.error.HTTPError as e:
      err_body = e.read().decode("utf-8", errors="replace")
      if "quotaExceeded" in err_body:
        raise RuntimeError(f"quotaExceeded: {err_body}") from e
      print(f"  [!] Video status query warning ({e.code}): {err_body}")
  return out


def update_playlist_privacy(
    access_token: str,
    playlist_id: str,
    title: str,
    description: str,
    privacy_status: str = "public",
) -> bool:
  """Updates a YouTube playlist's privacyStatus (e.g. from unlisted to public)."""
  payload = {
      "id": playlist_id,
      "snippet": {
          "title": title,
          "description": description,
      },
      "status": {
          "privacyStatus": privacy_status,
      },
  }
  url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"
  req = urllib.request.Request(
      url,
      data=json.dumps(payload).encode("utf-8"),
      headers={
          "Authorization": f"Bearer {access_token}",
          "Content-Type": "application/json; charset=UTF-8",
      },
      method="PUT",
  )
  try:
    with urllib.request.urlopen(req) as resp:
      resp.read()
    return True
  except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="replace")
    print(f"  [!] Playlist privacy update warning for {playlist_id} ({e.code}): {err_body}")
    return False


def check_and_publish_propositions(
    prop_dirs: list[Path],
    client_secret_path: Path,
    token_path: Path,
    target: str = "both",
    book_rom: str = "I",
    publish: bool = False,
    wait: bool = False,
    poll_interval: int = 60,
    skip_captions: bool = False,
) -> None:
  """Checks processing/check status of uploaded videos and optionally marks them public when ready."""
  reg_path = VIDEOS_Root / "playlists.json"
  reg = json.loads(reg_path.read_text(encoding="utf-8")) if reg_path.exists() else {}
  book_entry = reg.get(f"book_{book_rom.lower()}", {})
  pl_1080p = book_entry.get("wide_1080p", {}).get("id")
  pl_short = book_entry.get("short", {}).get("id")

  while True:
    access_token = get_valid_access_token(client_secret_path, token_path)
    entries: list[dict] = []
    video_ids: list[str] = []

    for pdir in prop_dirs:
      yt_json_path = pdir / "youtube.json"
      if not yt_json_path.exists():
        continue
      meta = json.loads(yt_json_path.read_text(encoding="utf-8"))
      short_code = meta.get("short_code", pdir.name)
      uploads = meta.get("uploads", {})
      for key, label, pl_id in (
          ("wide_1080p", "16:9", pl_1080p),
          ("short", "9:16", pl_short),
      ):
        if target == "1080p" and key != "wide_1080p":
          continue
        if target == "short" and key != "short":
          continue
        u = uploads.get(key, {})
        vid = u.get("video_id")
        if vid:
          video_ids.append(vid)
          entries.append({
              "prop_dir": pdir,
              "yt_json_path": yt_json_path,
              "short_code": short_code,
              "key": key,
              "label": label,
              "playlist_id": pl_id or u.get("playlist_id"),
              "video_id": vid,
              "version": u.get("version", 1),
              "url": u.get("url", ""),
              "has_cc": bool(u.get("caption_id")),
              "has_pl": bool(u.get("playlist_item_id")),
              "local_privacy": u.get("privacyStatus", "unlisted"),
          })

    try:
      status_map = get_videos_status(access_token, video_ids)
    except RuntimeError as e:
      if "quotaExceeded" in str(e):
        if not wait:
          print(
              "\n[QUOTA] Google Cloud YouTube Data API v3 daily quota (10,000 units) is currently exhausted.\n"
              "        Quota resets at midnight Pacific Time (00:00 America/Los_Angeles).\n"
              "        Run with `--publish --wait` to automatically wait for reset and publish."
          )
          return
        now_str = datetime.now().strftime("%H:%M:%S")
        print(
            f"[{now_str}] API daily quota exhausted; sleeping 15m until quota reset ..."
        )
        time.sleep(900)
        continue
      raise

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n==========================================================================================")
    print(f"YOUTUBE CHECK & PUBLISH STATUS ({now_str})")
    print(f"==========================================================================================")
    print(f"{'Prop':6s} {'Fmt':5s} {'Ver':4s} {'Video ID':12s} {'Upload':10s} {'Checks/HD':11s} {'Privacy':9s} {'CC':4s} {'PL':4s} {'URL'}")
    print(f"{'-'*6} {'-'*5} {'-'*4} {'-'*12} {'-'*10} {'-'*11} {'-'*9} {'-'*4} {'-'*4} {'-'*32}")

    pending_count = 0
    quota_hit = False

    for item in entries:
      vid = item["video_id"]
      st = status_map.get(vid, {})
      up_st = st.get("upload_status", "?")
      pr_st = st.get("processing_status", "?")
      pv_st = st.get("privacy_status", item["local_privacy"])
      is_ready = st.get("is_ready", False)
      cc_flag = "yes" if item["has_cc"] else "no"
      pl_flag = "yes" if item["has_pl"] else "no"
      print(
          f"{item['short_code']:6s} {item['label']:5s} v{item['version']:<3d} "
          f"{vid:12s} {up_st:10s} {pr_st:11s} {pv_st:9s} {cc_flag:4s} {pl_flag:4s} {item['url']}"
      )

      needs_work = (
          not is_ready
          or pv_st != "public"
          or not item["has_pl"]
          or (not skip_captions and not item["has_cc"])
      )
      if not publish:
        if not is_ready:
          pending_count += 1
        continue

      if not is_ready:
        pending_count += 1
        continue

      if needs_work and not quota_hit:
        yt_json_path = item["yt_json_path"]
        meta = json.loads(yt_json_path.read_text(encoding="utf-8"))
        files = meta.get("files", {})
        uploads = meta.setdefault("uploads", {})
        history = meta.setdefault("history", {})
        key = item["key"]
        u = uploads.get(key, {})
        title = (
            meta.get("title_1080p")
            if key == "wide_1080p"
            else meta.get("title_short")
        ) or f"{item['short_code']} • Euclid's Elements"
        description = meta.get("description", "")
        tags = meta.get("tags", [])
        category_id = str(meta.get("categoryId", "27"))
        thumb_key = "thumbnail_16x9_png" if key == "wide_1080p" else "thumbnail_9x16_png"
        thumb_path = Path(files[thumb_key]) if files.get(thumb_key) else None
        srt_path = Path(files["captions_srt"]) if files.get("captions_srt") else None

        # 1. Ensure thumbnail is set if missingplaylist/cc
        if not item["has_pl"] and thumb_path and thumb_path.exists():
          print(f"  [THUMB] Uploading thumbnail for {item['short_code']} {item['label']} ({vid}) ...")
          upload_thumbnail(access_token, vid, thumb_path)

        # 2. Ensure .srt captions are uploaded unless --no-captions
        if not skip_captions and not u.get("caption_id") and srt_path and srt_path.exists():
          print(f"  [CC] Uploading captions for {item['short_code']} {item['label']} ({vid}) ...")
          cap_id = upload_captions_srt(access_token, vid, srt_path)
          if cap_id:
            u["caption_id"] = cap_id
          else:
            quota_hit = True

        # 3. Ensure playlist swap is complete
        pl_id = item["playlist_id"]
        prev_list = history.get(key, [])
        prev_entry = prev_list[-1] if prev_list else None
        prev_vid = prev_entry.get("video_id") if prev_entry else None
        prev_ver = prev_entry.get("version", item["version"] - 1) if prev_entry else (item["version"] - 1)

        if pl_id and not u.get("playlist_item_id") and not quota_hit:
          old_pl_item_id = None
          old_pos = None
          if prev_vid:
            old_pl_item_id, old_pos = find_playlist_item(access_token, pl_id, prev_vid)
          pos_label = f" at position {old_pos}" if old_pos is not None else ""
          print(f"  [PLAYLIST] Adding {vid} to playlist {pl_id}{pos_label} ...")
          pl_item_id = add_video_to_playlist(access_token, pl_id, vid, position=old_pos)
          if pl_item_id:
            u["playlist_item_id"] = pl_item_id
            if old_pl_item_id:
              print(f"  [PLAYLIST] Removing superseded v{prev_ver} ({prev_vid}) from playlist ...")
              delete_playlist_item(access_token, old_pl_item_id)
          else:
            quota_hit = True

        # 4. Ensure superseded video is unlisted with [vN] title
        if prev_vid and not quota_hit and not prev_entry.get("unlisted_confirmed"):
          old_title = f"{title} [v{prev_ver}]"
          if len(old_title) > 100:
            old_title = f"{title[:93]} [v{prev_ver}]"
          old_desc = f"Superseded by v{item['version']}.\n\n{description}"
          try:
            update_video_metadata(
                access_token=access_token,
                video_id=prev_vid,
                title=old_title,
                description=old_desc,
                tags=tags,
                category_id=category_id,
                privacy_status="unlisted",
            )
            prev_entry["unlisted_confirmed"] = True
          except Exception as e:
            if "quotaExceeded" in str(e):
              quota_hit = True

        # 5. Flip current video to PUBLIC!
        if pv_st != "public" and not quota_hit:
          print(f"  [PUBLISH] Marking {item['short_code']} {item['label']} ({vid}) → PUBLIC ...")
          try:
            update_video_metadata(
                access_token=access_token,
                video_id=vid,
                title=title,
                description=description,
                tags=tags,
                category_id=category_id,
                privacy_status="public",
            )
            u["privacyStatus"] = "public"
            u["published_at"] = datetime.now(timezone.utc).isoformat()
            print(f"  [OK] Published: {item['url']}")
          except Exception as e:
            print(f"  [!] Failed publishing {vid}: {e}")
            if "quotaExceeded" in str(e):
              quota_hit = True
            pending_count += 1
        elif pv_st == "public":
          u["privacyStatus"] = "public"

        if quota_hit:
          pending_count += 1

        yt_json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    if publish and not quota_hit and pending_count == 0:
      # Also ensure the Book playlists themselves are public
      for sub_key, default_title, default_desc in (
          (
              "wide_1080p",
              f"Euclid's Elements • Book {book_rom.upper()}",
              f"Step-by-step geometric constructions and proofs from Book {book_rom.upper()} of Euclid's Elements (1908 Heath Edition + GEOMETOR G-Index).",
          ),
          (
              "short",
              f"Euclid's Elements • Book {book_rom.upper()} • Shorts",
              f"Vertical 9:16 Shorts walking step-by-step through every proposition of Book {book_rom.upper()} of Euclid's Elements (1908 Heath Edition + GEOMETOR G-Index).",
          ),
      ):
        pl_info = book_entry.get(sub_key, {})
        if pl_info.get("id") and pl_info.get("privacyStatus") != "public":
          print(f"  [PLAYLIST] Marking playlist '{pl_info.get('title', default_title)}' → PUBLIC ...")
          if update_playlist_privacy(
              access_token,
              pl_info["id"],
              pl_info.get("title", default_title),
              default_desc,
              "public",
          ):
            pl_info["privacyStatus"] = "public"
            reg_path.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")

    if not wait or pending_count == 0:
      if publish and pending_count == 0:
        print("\n[DONE] All target videos have completed checks and are now PUBLIC!")
      break

    sleep_sec = 900 if quota_hit else poll_interval
    reason = "API quota reset" if quota_hit else f"{pending_count} video(s) still processing/pending"
    print(f"\n[WAIT] {reason}; polling again in {sleep_sec}s ...")
    time.sleep(sleep_sec)


def _parse_prop_range(spec: str) -> list[int]:
  nums: list[int] = []
  for part in spec.split(","):
    part = part.strip()
    if not part:
      continue
    if "-" in part:
      a, b = part.split("-", 1)
      nums.extend(range(int(a), int(b) + 1))
    else:
      nums.append(int(part))
  return nums


def main() -> None:
  parser = argparse.ArgumentParser(
      description="Upload GEOMETOR Euclid 16:9 1080p videos and 9:16 Shorts to YouTube."
  )
  parser.add_argument(
      "dirs",
      nargs="*",
      help="Proposition folder paths (e.g. resources/videos/book_i/01).",
  )
  parser.add_argument(
      "--book",
      default="i",
      help="Book numeral slug when using --props (default: i).",
  )
  parser.add_argument(
      "--props",
      help="Proposition numbers or ranges (e.g., '1' or '1-5' or '1,3,5').",
  )
  parser.add_argument(
      "--auth",
      action="store_true",
      help="Run OAuth 2.0 browser flow to authorize @geometor and save token.",
  )
  parser.add_argument(
      "--whoami",
      action="store_true",
      help="Verify current OAuth token and print the connected YouTube channel.",
  )
  parser.add_argument(
      "--client-secret",
      type=Path,
      default=DEFAULT_CLIENT_SECRET,
      help=f"Path to OAuth 2.0 client_secret.json (default: {DEFAULT_CLIENT_SECRET}).",
  )
  parser.add_argument(
      "--token",
      type=Path,
      default=DEFAULT_TOKEN_PATH,
      help=f"Path to saved OAuth token JSON (default: {DEFAULT_TOKEN_PATH}).",
  )
  parser.add_argument(
      "--target",
      choices=["both", "1080p", "short"],
      default="both",
      help="Which video format(s) to upload (default: both).",
  )
  parser.add_argument(
      "--privacy",
      choices=["unlisted", "private", "public"],
      help="Override privacyStatus from youtube.json.",
  )
  parser.add_argument(
      "--playlist-1080p",
      help="Optional YouTube Playlist ID for 16:9 1080p videos.",
  )
  parser.add_argument(
      "--playlist-short",
      help="Optional YouTube Playlist ID for 9:16 Shorts.",
  )
  parser.add_argument(
      "--no-playlists",
      action="store_true",
      help="Skip automatic playlist creation and assignment.",
  )
  parser.add_argument(
      "--no-captions",
      action="store_true",
      help="Skip .srt caption upload (saves 400 API quota units per video).",
  )
  parser.add_argument(
      "--update-meta",
      action="store_true",
      help="Update title, description, tags, and thumbnail on already-uploaded videos.",
  )
  parser.add_argument(
      "--update-thumb",
      action="store_true",
      help="Also re-upload custom thumbnail when using --update-meta.",
  )
  parser.add_argument(
      "--replace",
      action="store_true",
      help="Upload a new version (vN+1), swap it into the playlist at the same position, unlist the previous take with [vN] suffix, and archive in history.",
  )
  parser.add_argument(
      "--sync-missing",
      action="store_true",
      help="Sync missing thumbnails, captions, playlist items, and superseded unlistings for already-uploaded videos without re-uploading MP4s.",
  )
  parser.add_argument(
      "--status",
      action="store_true",
      help="Query live YouTube processing/check status and privacy for the selected propositions.",
  )
  parser.add_argument(
      "--publish",
      action="store_true",
      help="Verify videos have finished YouTube processing & checks, sync any missing items, and mark videos & playlists PUBLIC.",
  )
  parser.add_argument(
      "--wait",
      action="store_true",
      help="Poll continuously until all target videos finish processing & checks (and are published if --publish is set).",
  )
  parser.add_argument(
      "--poll-interval",
      type=int,
      default=60,
      help="Polling interval in seconds when using --wait (default: 60).",
  )
  parser.add_argument(
      "--force",
      action="store_true",
      help="Upload even if youtube.json already records a video_id.",
  )
  parser.add_argument(
      "--dry-run",
      action="store_true",
      help="Inspect youtube.json and print upload plan without calling the YouTube API.",
  )
  args = parser.parse_args()

  if args.auth:
    run_oauth_flow(args.client_secret, args.token)
    if not args.dirs and not args.props:
      return

  if args.whoami:
    token = get_valid_access_token(args.client_secret, args.token)
    ch = get_authenticated_channel(token)
    if ch:
      s = ch.get("snippet", {})
      st = ch.get("statistics", {})
      print(
          f"Authenticated Channel: {s.get('title')} ({s.get('customUrl', ch.get('id'))}) "
          f"• {st.get('videoCount', '0')} videos"
      )
    return

  prop_dirs: list[Path] = [Path(d).resolve() for d in args.dirs]
  if args.props:
    book_dir = VIDEOS_Root / f"book_{args.book.lower()}"
    for n in _parse_prop_range(args.props):
      prop_dirs.append(book_dir / f"{n:02d}")

  if not prop_dirs:
    parser.print_help()
    sys.exit(1)

  if args.status or (args.publish and not (args.replace or args.force)):
    check_and_publish_propositions(
        prop_dirs=prop_dirs,
        client_secret_path=args.client_secret,
        token_path=args.token,
        target=args.target,
        book_rom=args.book.upper(),
        publish=args.publish,
        wait=args.wait,
        poll_interval=args.poll_interval,
        skip_captions=args.no_captions,
    )
    return

  access_token = (
      None
      if args.dry_run
      else get_valid_access_token(args.client_secret, args.token)
  )

  pl_1080p = args.playlist_1080p
  pl_short = args.playlist_short
  if (
      not args.dry_run
      and not args.no_playlists
      and not args.update_meta
      and access_token
      and (not pl_1080p or not pl_short)
  ):
    auto_1080p, auto_short = ensure_book_playlists(
        access_token=access_token,
        book_rom=args.book.upper(),
        privacy_status=args.privacy or "unlisted",
    )
    pl_1080p = pl_1080p or auto_1080p
    pl_short = pl_short or auto_short

  for pdir in prop_dirs:
    ok = process_proposition_dir(
        prop_dir=pdir,
        access_token=access_token,
        target=args.target,
        privacy_override=args.privacy,
        playlist_1080p=pl_1080p,
        playlist_short=pl_short,
        update_meta_only=args.update_meta,
        update_thumb=args.update_thumb,
        replace_existing=args.replace,
        sync_missing=args.sync_missing,
        skip_captions=args.no_captions,
        force=args.force,
        dry_run=args.dry_run,
    )
    if ok is False:
      break

  if args.publish and not args.dry_run:
    check_and_publish_propositions(
        prop_dirs=prop_dirs,
        client_secret_path=args.client_secret,
        token_path=args.token,
        target=args.target,
        book_rom=args.book.upper(),
        publish=True,
        wait=args.wait,
        poll_interval=args.poll_interval,
        skip_captions=args.no_captions,
    )


if __name__ == "__main__":
  main()
