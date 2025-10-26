import streamlit as st
import requests


# --- Custom CSS to load Amiri Quran font ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri+Quran&display=swap');

    html, body, [class*="css"] {
        font-family: 'Amiri Quran', serif;
    }

    .quran-text {
        font-family: 'Amiri Quran', serif;
        font-size: 28px;
        direction: rtl;
        text-align: right;
        line-height: 2.2;
        color: #222;
    }

    .title {
        text-align: center;
        font-family: 'Amiri Quran', serif;
        font-size: 36px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Mushaf Quranic App")


response_surah_index = requests.get("https://api.alquran.cloud/v1/surah").json()["data"]


arabic_surah_names = [
    f"{s["number"]} . {s["englishName"]} {s["name"]} " for s in response_surah_index
]


selected_surah_name = st.selectbox("choose surah", arabic_surah_names)

surah_num = int(selected_surah_name.split(" . ")[0])


response_surah = requests.get(
    f"https://api.alquran.cloud/v1/surah/{surah_num}/ar.alafasy"
).json()["data"]["ayahs"]


for ayah in response_surah:
    st.markdown(f'<div class="quran-text">{ayah["text"]}</div>', unsafe_allow_html=True)
    st.audio(ayah["audio"])

















