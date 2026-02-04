# Project Memory

This repository is a Mandarin shadowing web app with a Python audio generator. It includes two web players and a lesson creator.

## Purpose
- Help users practice Mandarin by shadowing audio (Chinese + English).
- Generate MP3 audio from YAML lesson files using `main.py` (Edge TTS).
- Provide a browser-based player (`index.html`) and memory-activator mode (`memory-activator.html`).
- Provide a lesson creator (`lesson-creator.html`) to build YAML from pasted sentence lists.

## Key Files
- `index.html`: Main React-in-browser shadowing app.
- `memory-activator.html`: Memory activator mode (EN audio -> pause -> CH audio -> pause).
- `lesson-creator.html`: New lesson builder with CSV/TSV paste, YAML export, auto-pinyin.
- `main.py`: Generates MP3 audio for YAML lessons.
- `yaml/`: Lesson data.
- `audio/`: Generated MP3 files.

## Recent Work (Feb 2026 session)
- Added editable keyboard shortcuts to the player:
  - New toggles for display: Chinese (`CTRL+ALT+C`), Pinyin (`CTRL+ALT+Z`), English (`CTRL+ALT+X`).
  - Shortcut editor in Help modal (edit + reset), persisted in localStorage.
- Mirrored editable shortcuts in `memory-activator.html` with default multi-bind (e.g. `A,LEFT`).
- Added theme system with dropdown + floating settings button:
  - Themes: Paper & Lantern, Calm Ink Wash, Modern Studio, Glacier Bright (cool/bright + warm accents).
  - Settings button is a circular gear bottom-right; click outside closes panel.
  - Theme persists via `localStorage` key `appTheme`.
  - Warm accents used for pinyin and control labels via `theme-warm`.
- Built `lesson-creator.html`:
  - Paste CSV/TSV lines (2 columns: Chinese/English; 3 columns: Chinese/Pinyin/English).
  - Generates YAML preview + download + copy.
  - Auto-pinyin option using `pinyin-pro` (tone marks default; also numbers/none).
  - Navigation links to `index.html` and `memory-activator.html`.
- Added link to Lesson Creator from player headers.

## Git Notes
- Git push previously failed due to network (github.com not reachable).

