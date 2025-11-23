import os
import hashlib
import asyncio
import edge_tts
import yaml

# --- CONFIGURATION ---
OUTPUT_FOLDER = "audio"
VOICE = "zh-CN-XiaoxiaoNeural"  # Options: zh-CN-XiaoxiaoNeural, zh-CN-YunxiNeural
SPEAKING_RATE = 0.85  # Speaking rate: 1.0 is normal speed, 0.85 is 85% of normal speed, 0.8 is 80% of normal speed

def load_phrases_from_yaml(yaml_file):
    """Loads phrases from YAML file and extracts Chinese text."""
    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    phrases = []
    for category in data:
        for phrase in category['phrases']:
            phrases.append(phrase['chinese'])

    return phrases

def add_ssml_speed(text, rate):
    """Wraps text in SSML tags to control speaking rate."""
    # Convert rate to percentage format (e.g., 0.85 becomes "85%")
    percentage_rate = f"{int(rate * 100)}%"
    return f'{text}', percentage_rate

# Load phrases from data.yaml
PHRASES = load_phrases_from_yaml('data.yaml')

def get_filename(text):
    """Generates the same MD5 filename hash as the JavaScript app."""
    hash_object = hashlib.md5(text.encode('utf-8'))
    return f"audio_{hash_object.hexdigest()}.mp3"

async def generate_all():
    # Create audio directory if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created folder: {OUTPUT_FOLDER}")

    print(f"Generating audio for {len(PHRASES)} phrases...")

    for text in PHRASES:
        filename = get_filename(text)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        
        if os.path.exists(output_path):
            print(f"Skipping (already exists): {text[:10]}...")
            continue

        print(f"Generating: {text[:10]}... -> {filename}")
        try:
            # Use SSML to control speaking rate
            ssml_text,rate = add_ssml_speed(text, SPEAKING_RATE)
            communicate = edge_tts.Communicate(ssml_text, rate ="-15%")
            await communicate.save(output_path)
        except Exception as e:
            print(f"Error generating '{text}': {e}")

    print("\nDone! You can now open index.html")

if __name__ == "__main__":
    asyncio.run(generate_all())