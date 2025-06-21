import streamlit as st
from datetime import date

# Konfigurasi
st.set_page_config(page_title="Surat untuk Kamu", page_icon="💌", layout="centered")

# Inisialisasi state
if "page" not in st.session_state:
    st.session_state.page = "pembuka"

# Halaman Pembuka
if st.session_state.page == "pembuka":
    st.title("💌 Selamat Datang!")

    nama = st.text_input("Siapa nama kamu?")
    tgl_lahir = st.date_input("Tanggal lahirmu?", min_value=date(1900, 1, 1), max_value=date.today())

    if nama and tgl_lahir:
        if st.button("Buka Surat"):
            st.session_state.nama = nama
            st.session_state.tgl_lahir = tgl_lahir
            st.session_state.page = "isi"

# Halaman Isi (Surat)
elif st.session_state.page == "isi":
    nama = st.session_state.nama
    tgl_lahir = st.session_state.tgl_lahir
    hari_ini = date.today()
    umur = hari_i_
