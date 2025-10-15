import librosa
import librosa.display
import matplotlib.pyplot as plt
import os

def plot_waveforms(folder_path):
    plt.figure(figsize=(12, 8))
    stems = [f for f in os.listdir(folder_path) if f.endswith(".wav")]

    for i, stem in enumerate(stems, 1):
        y, sr = librosa.load(os.path.join(folder_path, stem))
        plt.subplot(len(stems), 1, i)
        librosa.display.waveshow(y, sr=sr)
        plt.title(stem)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_waveforms("outputs/test_clip")


#pip install spleeter==2.3.2
