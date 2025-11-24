# Project Summary

## Overall Goal
Create a comprehensive Chinese language learning application that uses audio generation and shadowing techniques to help users practice Mandarin pronunciation with organized content, multiple practice modes, and dynamic file loading capabilities.

## Key Knowledge
- **Technology Stack**: Python for audio generation, React+Babel+Tailwind for web interface, edge-tts for audio synthesis, MD5 hashing for consistent audio filenames
- **File Structure**: YAML files in `yaml/` folder, audio files organized in category-based subfolders under `audio/`, HTML files for web interfaces
- **Audio Generation**: Uses MD5 hashing to create consistent filenames for audio files based on Chinese and English text; generates both Chinese and English audio files for each phrase
- **Two Web Applications**: `index.html` (Shadowing App) and `memory-activator.html` (Memory Activator mode with EN Audio -> Pause -> CH Audio -> Pause sequence)
- **Voice Configuration**: Chinese voice `zh-CN-XiaoxiaoNeural`, English voice `en-US-JennyNeural` with 0.85x speaking rate
- **Dynamic File Loading**: Both applications can load additional YAML files using the "+" button without refreshing the page
- **Keyboard Shortcuts**: Space bar (play/pause), arrows (navigation), W/S (speed), Q/E (pause duration) in Memory Activator

## Recent Actions
1. [DONE] Updated Python script to organize audio files in category-based subfolders in audio directory
2. [DONE] Created yaml folder to organize YAML files and made script process all YAML files in the folder
3. [DONE] Modified audio engine to construct correct paths using category subfolders
4. [DONE] Implemented Memory Activator mode with English audio first, pause for recall, then Chinese audio
5. [DONE] Added keyboard shortcuts for better control in Memory Activator
6. [DONE] Added "+" button to both web apps to load new YAML files without page refresh
7. [DONE] Fixed JSX syntax errors in both HTML files
8. [DONE] Updated README to document all new features and project structure
9. [DONE] Created .gitignore to exclude unnecessary files/folders (VSCode, Qwen, archives)

## Current Plan
- [DONE] Audio generation with organized folder structure working correctly
- [DONE] Dynamic YAML file loading without page refresh implemented
- [DONE] Memory Activator mode with proper audio sequence (EN->Pause->CH->Pause)
- [DONE] Keyboard shortcuts available in Memory Activator
- [DONE] Application ready for use with organized content structure
- [TODO] Generate audio for more categories if needed
- [TODO] Test all functionality thoroughly in browser environment
- [TODO] Document any additional customization options for users

---

## Summary Metadata
**Update time**: 2025-11-24T12:01:59.868Z 
