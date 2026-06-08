import streamlit as st
import os
from streamlit_navigation_bar import st_navbar

# 1. Konfiguration
st.set_page_config(page_title="Marions Autorenwelt", page_icon="👤", layout="centered", initial_sidebar_state="collapsed")

# 2. Das obere Navigationsmenü (Genauso wie auf der Startseite)
pages = ["Home", "Marions Autorenwelt"]
styles = {
    "nav": {
        "background-color": "#008080", # Eine edle Petrol-Farbe für Marions Bereich
        "justify-content": "center",
    },
    "span": {
        "color": "white",
        "padding": "14px 20px",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
        "font-weight": "bold",
    }
}

page = st_navbar(pages, styles=styles, selected="Marions Autorenwelt")

# Wenn der User auf "Home" klickt, springt er zurück zu deiner Hauptseite
if page == "Home":
    st.switch_page("app.py")

# 3. CSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

# 4. MARIONS INHALT
st.write(f"<h1 style='text-align: center; color: #008080;'>Marions Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Vorschau: Deine 4 Wunsch-Rubriken</h3>", unsafe_allow_html=True)

st.divider()

# Rubrik 1
st.header("👤 1. Über mich")
col_about1, col_about2 = st.columns([1, 2])
with col_about1:
    st.info("📸 [Autorenfoto]")
with col_about2:
    st.write("""
    **Herzlich Willkommen!** Hier ist Platz für deine persönliche Vorstellung, Marion. Ein packender Text darüber, wer du bist, was dich antreibt und warum du schreibst.
    """)

st.divider()

# Rubrik 2
st.header("📚 2. Mein Buch")
col_book1, col_book2 = st.columns([1, 2])
with col_book1:
    st.info("📖 [Buch-Cover]")
with col_book2:
    st.subheader("Dein Buchtitel")
    st.write("Hier kommt dein Klappentext hin.")
    st.markdown("### 🛒 Jetzt im Handel bestellen:")
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.link_button("🌐 Bei Amazon kaufen", "https://amazon.de", type="primary")
    with btn_col2:
        st.link_button("📖 Bei Thalia kaufen", "https://thalia.de")

st.divider()

# Rubrik 3
st.header("📅 3. Veranstaltungen & Lesungen")
termine = [
    {"Datum": "15. Oktober 2026", "Event": "Autorenlesung & Signierstunde", "Ort": "Stadtbibliothek, Berlin"},
    {"Datum": "12. Dezember 2026", "Event": "Große Premierenlesung", "Ort": "Buchhandlung Schmidt, Hamburg"}
]
for t in termine:
    with st.expander(f"📌 {t['Datum']} – {t['Event']}"):
        st.write(f"**Wo:** {t['Ort']}")

st.divider()

# Rubrik 4
st.header("🎙️ 4. Multimedia & Presse")
col_media1, col_media2 = st.columns(2)
with col_media1:
    st.subheader("🎧 Podcast-Gast")
    st.link_button("Jetzt reinhören", "https://spotify.com")
with col_media2:
    st.subheader("📰 Fachartikel")
    st.link_button("Artikel lesen", "https://google.com")

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Vorschau-Modus für Marion | Erstellt von Stefan Röser</p>", unsafe_allow_html=True)
