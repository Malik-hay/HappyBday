import streamlit as st
from datetime import datetime, date

# Konfigurasi halaman
st.set_page_config(page_title="Surat untuk Kamu", page_icon="💌", layout="centered")

# State untuk simpan data antar halaman
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "tgl_lahir" not in st.session_state:
    st.session_state.tgl_lahir = None
if "lanjut" not in st.session_state:
    st.session_state.lanjut = False

st.title("💌 Selamat Datang!")

if not st.session_state.lanjut:
    st.write("Halo! Web ini punya pesan spesial buat kamu 🫶")

    st.session_state.nama = st.text_input("Siapa nama kamu?", "")
    st.session_state.tgl_lahir = st.date_input("Kapan tanggal lahirmu?", min_value=date(1900, 1, 1), max_value=date.today())

    if st.session_state.nama and st.session_state.tgl_lahir:
        if st.button("Buka Surat"):
            st.session_state.lanjut = True
            st.experimental_rerun()

else:
    # Hitung umur
    today = date.today()
    lahir = st.session_state.tgl_lahir
    umur = today.year - lahir.year - ((today.month, today.day) < (lahir.month, lahir.day))

    st.success("📬 Ini suratnya:")
    st.markdown(f"""
    ### Hai {st.session_state.nama}! 👋

    Selamat datang di halaman ini.

    Hari ini, kamu berusia **{umur} tahun** 🎉

    Semoga hari-harimu selalu penuh semangat, harapan, dan kebahagiaan.  
    Jangan lupa jaga diri baik-baik dan terus melangkah maju 💪

    > _Dari seseorang yang peduli._
    """)

    if st.button("Balik ke Halaman Utama"):
        st.session_state.lanjut = False
        st.experimental_rerun()
