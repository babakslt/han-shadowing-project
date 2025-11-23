# Mandarin Shadowing App

A comprehensive Chinese language learning application that uses audio generation and shadowing techniques to help users practice Mandarin pronunciation.

## Overview

This project consists of two main components:
1. A Python script that generates audio files for Chinese phrases using Microsoft Edge TTS
2. A web-based player application that allows users to practice shadowing (repeating after audio)

The application includes phrases organized by difficulty levels (Level 1 to Level 10) and lessons, with each phrase containing Chinese characters, pinyin, and English translations.

## Features

- **Text-to-Speech Generation**: Uses Microsoft Edge TTS to generate high-quality Mandarin audio
- **Multiple Difficulty Levels**: Phrases organized from beginner (Level 1) to advanced (Level 10)
- **Audio Caching**: Generated audio files are saved locally for fast playback
- **Web-based Player**: React-powered interface for practicing shadowing
- **Customizable Playback**: Adjustable speed, repeat options, and pause times
- **Visual Controls**: Show/hide Chinese characters, pinyin, and English translations

## Prerequisites

- Python 3.7+
- Node.js (for development, though the web app runs in the browser)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd han-shadowing-project
   ```

2. Install Python dependencies:
   ```bash
   pip install edge-tts pyyaml
   ```

## Usage

### Generate Audio Files

Run the Python script to generate audio files for all phrases:

```bash
python main.py
```

This will:
- Load phrases from `data.yaml`
- Generate audio files using Edge TTS
- Save MP3 files to the `audio/` folder with MD5-based filenames
- Skip files that already exist

### Use the Web Application

1. Open `index.html` in your web browser
2. The application will automatically use the pre-generated audio files from the `audio/` folder
3. Select a category from the dropdown menu
4. Use the playback controls to practice shadowing

### Configuration

The `main.py` file contains configurable options:

- `OUTPUT_FOLDER`: Directory to save audio files (default: "audio")
- `VOICE`: TTS voice to use (default: "zh-CN-XiaoxiaoNeural")
- `SPEAKING_RATE`: Speed of speech (default: 0.85 for 85% of normal speed)

## Project Structure

```
.
├── main.py         # Python script for audio generation
├── data.yaml       # Chinese phrases organized by levels
├── index.html      # Web-based shadowing player
├── README.md       # This file
├── audio/          # Generated audio files
└── package-lock.json
```

## How It Works

1. The `data.yaml` file contains Chinese phrases organized by categories (levels and lessons)
2. Each phrase includes:
   - Chinese characters
   - Pinyin pronunciation
   - English translation
3. Running `main.py` generates audio files for each phrase
4. The web player uses these audio files for the shadowing practice
5. If audio files are missing, the web app falls back to browser-based TTS

## Customization

### Adding New Phrases

Edit `data.yaml` to add new phrases in the following format:

```yaml
- category: "New Category"
  phrases:
    - chinese: "你好。"
      pinyin: "Nǐ hǎo."
      meaning: "Hello."
```

### Changing Voice Settings

Modify the constants in `main.py`:
- `VOICE`: Choose from available Microsoft Edge TTS voices
- `SPEAKING_RATE`: Adjust between 0.5 (slower) and 1.5 (faster)

## License

This project is open source and available under the MIT License.