import os
import subprocess
import argparse

def split_song(input_path, output_dir="outputs", stems=4):
    os.makedirs(output_dir, exist_ok=True)
    print(f"🎵 Splitting {input_path} into {stems} stems...")
    
    cmd = [
        "spleeter", "separate",
        f"-p", f"spleeter:{stems}stems",
        "-o", output_dir,
        input_path
    ]
    subprocess.run(cmd)
    song_name = os.path.splitext(os.path.basename(input_path))[0]
    print(f"✅ Done! Stems saved at {output_dir}/{song_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Song Splitter using Spleeter")
    parser.add_argument("input", help="Input song path (.mp3/.wav)")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--stems", type=int, default=4, choices=[2,4])
    args = parser.parse_args()

    split_song(args.input, args.output, args.stems)
