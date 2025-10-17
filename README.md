# 🎵 Song Splitter — End-to-End AI Audio Stem Separation

[https://song-splitter.streamlit.app/](https://song-splitter.streamlit.app/)
## 🧠 Overview
AI-powered music stem separator built using **Spleeter by Deezer**, capable of isolating vocals, drums, bass, and other instruments with minimal system resources.

## ⚙️ Tech Stack
- Python 3.10
- Spleeter (Audio Source Separation)
- Librosa, Matplotlib (Audio Analysis)
- Streamlit (Web Interface)

```## 🏗️ Structure
song-splitter/
├── input/
├── outputs/
├── scripts/
│ ├── splitter.py
│ ├── evaluate.py
│ └── visualize.py
├── app.py
├── README.md
├── requirements.txt
```


## ▶️ Run Steps
```bash
# Setup
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install spleeter==2.3.2
```


```bash
# Separate stems
python scripts/splitter.py input/test_clip.mp3
```
```bash
# Visualize or evaluate
python scripts/visualize.py
python scripts/evaluate.py
```
```bash
# (Optional) Launch Web UI
streamlit run app.py
```
