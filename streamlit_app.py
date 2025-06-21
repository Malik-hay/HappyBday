import streamlit as st
from datetime import date

st.set_page_config(page_title="Surat untuk Kamu", page_icon="💌", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "pembuka"

# CSS dasar
st.markdown("""
    <style>
        .stTextInput > div > div,
        .stDateInput > div {
            justify-content: center;
        }
        .stButton button {
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

if st.session_state.page == "pembuka":
    st.markdown("<h1 style='text-align:center;'>💌 Selamat Datang!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Masukkan nama dan tanggal lahirmu ya 👇</p>", unsafe_allow_html=True)

    nama = st.text_input("Nama kamu:")
    tgl_lahir = st.date_input("Tanggal lahir:", min_value=date(1900, 1, 1), max_value=date.today())

    if nama and tgl_lahir:
        if st.button("Buka Surat"):
            st.session_state.nama = nama
            st.session_state.tgl_lahir = tgl_lahir
            st.session_state.page = "isi"

elif st.session_state.page == "isi":
    nama = st.session_state.nama
    tgl_lahir = st.session_state.tgl_lahir
    hari_ini = date.today()
    umur = hari_ini.year - tgl_lahir.year - ((hari_ini.month, hari_ini.day) < (tgl_lahir.month, tgl_lahir.day))

    st.success("📬 Ini suratnya:")

    st.markdown(f"""
    <div style="
        background-image: url('https://i.imgur.com/O28hWzv.png');
        background-size: 100% auto;
        background-repeat: repeat-y;
        background-position: top center;
        padding: 60px 30px;
        border-radius: 12px;
        text-align: center;
        max-width: 800px;
        margin: auto;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    ">
        <h3>Hai {nama}! 👋</h3>
        <p>Hari ini kamu berusia <strong>{umur} tahun</strong> 🎉</p>
        <p>
        Semoga kamu selalu sehat, bahagia, dan dikelilingi hal-hal baik.  
        Terus semangat menjalani hari ya!  
        Kamu berharga dan nggak sendirian 🤍  
        </p>

        <p>
        (Isi surat panjang bisa ditaruh di sini, paragraf tambahan sebanyak yang kamu mau...)  
        Bisa sampai ratusan kata, dan background akan tetap ikut memanjang.
        </p>

        <p><em>— dari seseorang yang peduli.</em></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Kembali ke Halaman Awal"):
        st.session_state.page = "pembuka"
