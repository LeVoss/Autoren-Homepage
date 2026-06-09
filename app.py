import streamlit as st
import os

st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# CSS für einheitliche weiße Buttons
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;} .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none !important;} section[data-testid="stSidebar"] {display: none !important;}
    div.stButton > button {
        background-color: #ffffff !important; color: #31333F !important; border: 2px solid #E6E8F1 !important;
        padding: 14px 10px !important; font-size: 1.1em !important; font-weight: bold !important;
        height: 60px !important; border-radius: 8px !important; transition: all 0.3s ease !important;
    }
    div.stButton > button[data-testid="baseButton-primary"] { border: 2px solid #FF4B4B !important; }
    div.stButton > button:hover { border-color: #FF4B4B !important; background-color: #FAFAFA !important; }
    </style>
    """, unsafe_allow_html=True)

# 4er-Menü
menu_col1, menu_col2, menu_col3, menu_col4 = st.columns([2, 2, 2, 2])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True, type="primary"): st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Über mich", use_container_width=True): st.switch_page("pages/1_Über_mich.py")
with menu_col3:
    if st.button("📅 Termine", use_container_width=True): st.switch_page("pages/2_Veranstaltungen.py")
with menu_col4:
    if st.button("🎬 Media", use_container_width=True): st.switch_page("pages/3_Multimedia.py")

st.divider()

# Startseiten-Inhalt (unverändert)
st.write("<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)

st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"): st.image("cover2.png", use_container_width=True)
    else: st.info("📖 Bild 'cover2.png' folgt...")
with col2:
    st.write("**Klappentext:**\nEin Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens...")
    st.markdown("**16,99 €** (Signiertes Taschenbuch) | **14,49 €** (Standard Taschenbuch)")

st.info("Sonderangebot: Mängelexemplare für **9,99 Euro** verfügbar!")
st.divider()
st.header("📦 Buch direkt bei mir bestellen")
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"
st.markdown(f'<iframe src="{form_url}" width="100%" height="900" frameborder="0">Wird geladen...</iframe>', unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)
amazon_url_buch2 = "https://www.amazon.de/Herz-keinen-Zorn-mehr-tr%C3%A4gt/dp/B0GK6QBS3P/..."
st.header(f"🛒 Oder über [Amazon bestellen]({amazon_url_buch2})")
st.divider()

st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])
with col3:
    if os.path.exists("cover1.png"): st.image("cover1.png", use_container_width=True)
    else: st.info("📖 Bild 'cover1.png' folgt...")
with col4:
    st.write("Mein erstes Buch habe ich im Sommer 2025 veröffentlicht...")
    amazon_url_buch1 = "https://www.amazon.de/Ein-leises-wir-Berlin-1930-ebook/dp/B0FQ2LSK8M/..."
    st.markdown(f"📖 **[Auf Amazon ansehen]({amazon_url_buch1})**")

st.divider()
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)
