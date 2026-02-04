import os
import hashlib
import asyncio
import edge_tts
import yaml
import sys
import glob
import argparse

# --- CONFIGURATION ---
OUTPUT_FOLDER = "audio"
YAML_FOLDER = "yaml"
CHINESE_VOICE = "zh-CN-XiaoxiaoNeural"  # Options: zh-CN-XiaoxiaoNeural, zh-CN-YunxiNeural
ENGLISH_VOICE = "en-US-JennyNeural"  # Options: en-US-JennyNeural, en-US-GuyNeural
SPEAKING_RATE = 0.85  # Speaking rate: 1.0 is normal speed, 0.85 is 85% of normal speed, 0.8 is 80% of normal speed
REQUEST_TIMEOUT = 60  # seconds per request
RETRY_COUNT = 3  # retries per phrase
RETRY_BACKOFF = 2.0  # seconds base backoff

def load_phrases_from_yaml(yaml_file):
    """Loads phrases from YAML file and extracts both Chinese and English text."""
    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    phrases = []
    for category in data:
        for phrase in category['phrases']:
            # Add both Chinese and English phrase objects
            phrases.append({'text': phrase['chinese'], 'lang': 'zh-CN', 'category': category['category']})
            phrases.append({'text': phrase['meaning'], 'lang': 'en-US', 'category': category['category']})
    
    return phrases

def get_edge_rate(rate):
    """Convert a float rate (e.g., 0.85) to Edge TTS rate string (e.g., '-15%')."""
    percent_delta = int(round((rate - 1.0) * 100))
    sign = "+" if percent_delta >= 0 else ""
    return f"{sign}{percent_delta}%"

def get_filename(text, category):
    """Generates the same MD5 filename hash as the JavaScript app, in category subfolder."""
    hash_object = hashlib.md5(text.encode('utf-8'))
    # Normalize category name to be filesystem-friendly
    safe_category = "".join(c for c in category if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_category = safe_category.replace(' ', '_')
    return os.path.join(OUTPUT_FOLDER, safe_category, f"audio_{hash_object.hexdigest()}.mp3")

async def generate_audio_for_text(text, lang, output_path):
    """Generate audio for a single text."""
    voice = CHINESE_VOICE if lang == 'zh-CN' else ENGLISH_VOICE
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    temp_path = output_path + ".tmp"

    for attempt in range(1, RETRY_COUNT + 1):
        try:
            # Use Edge TTS rate to control speaking speed
            rate = get_edge_rate(SPEAKING_RATE)
            communicate = edge_tts.Communicate(text, voice, rate=rate)
            await asyncio.wait_for(communicate.save(temp_path), timeout=REQUEST_TIMEOUT)

            # Validate non-empty file
            if not os.path.exists(temp_path) or os.path.getsize(temp_path) == 0:
                raise RuntimeError("Generated file is empty")

            # Atomically replace target
            os.replace(temp_path, output_path)
            return True
        except Exception as e:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass
            print(f"Error generating '{text}': {e}")
            if attempt < RETRY_COUNT:
                backoff = RETRY_BACKOFF * attempt
                print(f"Retrying ({attempt}/{RETRY_COUNT}) after {backoff:.1f}s...")
                await asyncio.sleep(backoff)
            else:
                return False

async def generate_all_for_yaml(yaml_file):
    """Generate audio files for a specific YAML file."""
    print(f"Processing YAML file: {yaml_file}")
    
    phrases = load_phrases_from_yaml(yaml_file)
    print(f"Generating audio for {len(phrases)} phrases (Chinese and English)...")

    for phrase in phrases:
        text = phrase['text']
        lang = phrase['lang']
        category = phrase['category']
        
        output_path = get_filename(text, category)

        if os.path.exists(output_path):
            print(f"Skipping (already exists): {text[:10]}...")
            continue

        print(f"Generating: {text[:20]}... -> {output_path} (lang: {lang}, cat: {category})")
        success = await generate_audio_for_text(text, lang, output_path)
        if not success:
            print(f"Failed to generate audio for: {text}")

async def process_all_yaml_files():
    """Process all YAML files in the yaml folder."""
    # Ensure yaml folder exists
    os.makedirs(YAML_FOLDER, exist_ok=True)
    
    # Find all YAML files in the yaml folder
    yaml_files = glob.glob(os.path.join(YAML_FOLDER, "*.yaml")) + glob.glob(os.path.join(YAML_FOLDER, "*.yml"))
    
    if not yaml_files:
        print(f"No YAML files found in {YAML_FOLDER} folder.")
        return
    
    print(f"Found {len(yaml_files)} YAML files to process: {yaml_files}")
    
    for yaml_file in yaml_files:
        await generate_all_for_yaml(yaml_file)

def main():
    parser = argparse.ArgumentParser(description='Generate audio files from YAML data')
    parser.add_argument('yaml_file', nargs='?', help='Path to a specific YAML file to process')
    args = parser.parse_args()

    if args.yaml_file:
        # Process specific YAML file
        if not os.path.exists(args.yaml_file):
            print(f"Error: YAML file {args.yaml_file} does not exist.")
            sys.exit(1)
        asyncio.run(generate_all_for_yaml(args.yaml_file))
    else:
        # Process all YAML files in yaml folder
        asyncio.run(process_all_yaml_files())

if __name__ == "__main__":
    main()
