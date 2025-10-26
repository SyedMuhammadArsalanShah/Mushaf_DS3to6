import streamlit as st
import requests


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
    st.write(ayah["text"])
    st.audio(ayah["audio"])
