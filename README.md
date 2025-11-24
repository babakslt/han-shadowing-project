# Mandarin Shadowing App

## **Made using QWEN CLI and QWEN Coder**

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
- **Organized Audio Files**: Audio files organized in category-based subfolders
- **YAML File Management**: Support for multiple YAML files in a dedicated folder
- **Dynamic YAML Loading**: Add new YAML files without refreshing the page
- **Memory Activator Mode**: Alternative practice mode (EN Audio -> Pause -> CH Audio -> Pause)

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
   pip install edge-tts pyyaml argparse glob3
   ```

## Usage

### Generate Audio Files

Run the Python script to generate audio files for phrases:

**For a specific YAML file:**
```bash
python main.py path/to/your/yaml/file.yaml
```

**For all YAML files in the yaml/ folder:**
```bash
python main.py
```

This will:
- Create a `yaml/` folder if it doesn't exist
- Load phrases from specified YAML file or all YAML files in the `yaml/` folder
- Generate audio files using Edge TTS for both Chinese and English text
- Save MP3 files to category-named subfolders under the `audio/` folder with MD5-based filenames
- Skip files that already exist

### Use the Web Applications

1. **Shadowing App**: Open `index.html` in your web browser
2. **Memory Activator**: Open `memory-activator.html` in your web browser
3. Both applications will automatically use the pre-generated audio files from the `audio/` folder's category subfolders
4. Use the dropdown menu to select categories
5. Use the "+" button to add new YAML files without refreshing
6. Use the playback controls to practice shadowing

### Memory Activator Mode

The Memory Activator provides an alternative learning sequence:
- Plays English audio first
- Pauses to allow mental recall of the Chinese translation
- Plays Chinese audio for verification
- Includes keyboard shortcuts for better control

### Keyboard Shortcuts (Memory Activator)

- **Space bar**: Play/pause audio
- **Left arrow** or **A**: Previous phrase
- **Right arrow** or **D**: Next phrase
- **Up arrow** or **W**: Increase speed
- **Down arrow** or **S**: Decrease speed
- **Q**: Decrease pause duration
- **E**: Increase pause duration

### Configuration

The `main.py` file contains configurable options:

- `OUTPUT_FOLDER`: Directory to save audio files (default: "audio")
- `YAML_FOLDER`: Directory to look for YAML files (default: "yaml")
- `CHINESE_VOICE`: Chinese TTS voice (default: "zh-CN-XiaoxiaoNeural")
- `ENGLISH_VOICE`: English TTS voice (default: "en-US-JennyNeural")
- `SPEAKING_RATE`: Speed of speech (default: 0.85 for 85% of normal speed)

## Project Structure

```
.
├── main.py                  # Python script for audio generation
├── index.html               # Web-based shadowing player
├── memory-activator.html    # Alternative practice mode
├── yaml/                    # YAML files organized by categories
│   ├── data.yaml            # Original phrase collection
│   └── sample_phrases.yaml  # Example file structure
├── audio/                   # Generated audio files organized by category
│   ├── Greetings/           # Audio files for Greetings category
│   ├── Basic_Phrases/       # Audio files for Basic Phrases category
│   └── ...                  # Other category folders
└── README.md                # This file
```

## How It Works

1. The YAML files contain Chinese phrases organized by categories (levels and lessons)
2. Each phrase includes:
   - Chinese characters
   - Pinyin pronunciation
   - English translation
3. Running `main.py` generates audio files for each phrase in both Chinese and English
4. Audio files are organized in category-named subfolders under the audio directory
5. The web players use these audio files for the shadowing practice
6. If audio files are missing, the web app falls back to browser-based TTS
7. New YAML files can be added dynamically using the "+" button

## Customization

### Adding New Phrases

1. **To the yaml folder**: Add new YAML files with the following format:

```yaml
- category: "New Category"
  phrases:
    - chinese: "你好。"
      pinyin: "Nǐ hǎo."
      meaning: "Hello."
```

2. **To the application**: Use the "+" button in either web application to add new YAML files without refreshing

### Changing Voice Settings

Modify the constants in `main.py`:
- `CHINESE_VOICE`: Choose from available Microsoft Edge TTS Chinese voices
- `ENGLISH_VOICE`: Choose from available Microsoft Edge TTS English voices
- `SPEAKING_RATE`: Adjust between 0.5 (slower) and 1.5 (faster)

## License

This project is open source and available under the MIT License.