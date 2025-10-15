import streamlit as st
import os
import subprocess

st.title("🎵 AI Song Splitter")
st.write("Upload a song and get separate stems (vocals, drums, bass, other).")

uploaded_file = st.file_uploader("Upload MP3/WAV file", type=["mp3", "wav"])

if uploaded_file:
    input_path = f"input/{uploaded_file.name}"
    os.makedirs("input", exist_ok=True)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.audio(input_path)
    
    if st.button("🔍 Separate Stems"):
        st.info("Processing... please wait")
        subprocess.run(["python", "scripts/splitter.py", input_path, "--output", "outputs"])
        song_name = os.path.splitext(uploaded_file.name)[0]
        folder = f"outputs/{song_name}"

        st.success("✅ Separation complete!")
        for file in os.listdir(folder):
            st.subheader(file)
            st.audio(os.path.join(folder, file))
