import os
from pydub import AudioSegment

SUPPORTED_FORMATS = ('.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.mp3e')

INPUT_DIR = "audio_files"
OUTPUT_DIR = "converted_mp3"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_to_mp3(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")
        print(f"✅ Converted: {input_file} → {output_file}")
    except Exception as e:
        print(f"❌ Error converting {input_file}: {e}")

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(SUPPORTED_FORMATS):
            input_path = os.path.join(INPUT_DIR, filename)
            if filename.endswith(".mp3e"):
                temp_path = os.path.join(INPUT_DIR, filename[:-1])
                os.rename(input_path, temp_path)
                input_path = temp_path
                print(f"🔁 Renamed .mp3e to .mp3: {temp_path}")
            output_name = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(OUTPUT_DIR, output_name)
            convert_to_mp3(input_path, output_path)

if __name__ == "__main__":
    main()
