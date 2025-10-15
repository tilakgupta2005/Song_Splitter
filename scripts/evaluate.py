import librosa
import numpy as np
import os

def analyze_stems(folder_path):
    print(f"\n🔍 Evaluating stems in {folder_path}\n")
    for stem_file in os.listdir(folder_path):
        if stem_file.endswith(".wav"):
            y, sr = librosa.load(os.path.join(folder_path, stem_file))
            energy = np.mean(y ** 2)
            print(f"{stem_file:15s} | Energy: {energy:.4f}")

    print("\n✅ Basic comparison complete.")
    
if __name__ == "__main__":
    analyze_stems("outputs/test_clip")
