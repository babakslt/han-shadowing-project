# Project Summary

## Overall Goal
Create a standalone Mandarin shadowing application that loads phrases from a YAML file and plays pre-generated audio at a slower, learning-friendly pace using a browser-based interface that works without a server.

## Key Knowledge
- **Technology Stack**: Python for audio generation, React+Babel+Tailwind for web interface, edge-tts for audio synthesis
- **File Structure**: data.yaml (phrase categories), audio/ folder (generated mp3 files), index.html (standalone interface)
- **Audio Generation**: Uses MD5 hashing to create consistent filenames for audio files based on Chinese text
- **Speed Control**: SSML prosody tags with percentage format (e.g., "85%") instead of decimals to control speaking rate
- **Voice**: zh-CN-XiaoxiaoNeural for Chinese speech synthesis
- **Standalone Operation**: Uses file upload interface to load YAML data instead of server fetch, allowing direct file:// access

## Recent Actions
1. [DONE] Modified main.py to load phrases from data.yaml instead of hardcoded list
2. [DONE] Added SSML support to control speaking rate (0.85x speed) for learning-friendly audio
3. [DONE] Updated index.html to use file upload instead of server fetch for YAML data
4. [DONE] Generated 10 audio files at slower speaking rate (85% of normal speed)
5. [DONE] Modified UI to show file upload screen when no data is loaded
6. [DONE] Preserved fallback to browser TTS if audio files are missing

## Current Plan
- [DONE] Audio generation at slower speed working correctly
- [DONE] Standalone HTML interface with file upload functionality
- [DONE] Application ready for offline use with pre-generated audio files
- [TODO] User can now open index.html directly in browser and upload data.yaml to use the application with slower-paced audio for learning

---

## Summary Metadata
**Update time**: 2025-11-23T14:24:55.650Z 
