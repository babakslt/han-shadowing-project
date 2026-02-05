# Project Memory

This repository is a Mandarin shadowing web app with a Python audio generator. It includes a unified player and a lesson creator.

## Purpose
- Help users practice Mandarin by shadowing audio (Chinese + English).
- Generate MP3 audio from YAML lesson files using `main.py` (Edge TTS).
- Provide a browser-based player (`index.html`) with Shadow/Memory modes.
- Provide a lesson creator (`lesson-creator.html`) to build YAML from pasted sentence lists.

## Key Files
- `index.html`: Main React-in-browser shadowing app.
- Memory Activator mode is inside `index.html` (toggle in header + `?mode=memory`).
- `lesson-creator.html`: New lesson builder with CSV/TSV paste, YAML export, auto-pinyin.
- `main.py`: Generates MP3 audio for YAML lessons.
- `yaml/`: Lesson data.
- `audio/`: Generated MP3 files.

## Recent Work (Feb 2026 session)
- Added editable keyboard shortcuts to the player:
  - New toggles for display: Chinese (`CTRL+ALT+C`), Pinyin (`CTRL+ALT+Z`), English (`CTRL+ALT+X`).
  - Shortcut editor in Help modal (edit + reset), persisted in localStorage.
- Removed standalone `memory-activator.html`; modes are unified in `index.html`.
- Added theme system with dropdown + floating settings button:
  - Themes: Paper & Lantern, Calm Ink Wash, Modern Studio, Glacier Bright, Neon Dusk, Crimson Sand, Ember Circuit, Blue Gold, Teal Terracotta.
  - Settings button is a circular gear bottom-right; click outside closes panel.
  - Theme persists via `localStorage` key `appTheme`.
  - Warm accents used for pinyin and control labels via `theme-warm`.
- Built `lesson-creator.html`:
  - Paste CSV/TSV lines (2 columns: Chinese/English; 3 columns: Chinese/Pinyin/English).
  - Generates YAML preview + download + copy.
  - Auto-pinyin option using `pinyin-pro` (tone marks default; also numbers/none).
  - Navigation links to `index.html`.
- Added link to Lesson Creator from player headers.
- Added starred review mode and fixes:
  - Star toggle works and is stored.
  - Playlist can toggle to Starred view; next/prev follow starred order.
- Added Memory mode repeat tracking:
  - Per-sentence repeat counts saved.
  - Progress pie in top-left of main card (click to set target; default 50).
- Dynamic pause timing:
  - Pause = duration of next audio + user margin; cached/estimated durations.
- Lesson dropdown moved to top of playlist; target input/progress bar removed.
- Added Profile analytics:
  - Totals for starred, memory repeats, repeat target.
  - Export stats to JSON or CSV.
- Lesson Creator upgraded:
  - Inline editable rows, add/remove row.
  - Fill pinyin and sort Chinese.

## Git Notes
- Git push previously failed due to network (github.com not reachable).
