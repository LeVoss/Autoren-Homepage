import streamlit as st
import os

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Über mich - Stefan Röser", 
    page_icon="✍️", 
    layout="centered"
)

# 2. CSS (Sidebar verstecken & Buttons weiß, groß und einheitlich gestalten)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none !important;}
    section[data-testid="stSidebar"] {display: none !important;}
    
    /* Maßgeschneiderte Buttons: Absolut einheitliche Maße und große Schrift */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #31333F !important;
        border: 2px solid #E6E8F1 !important;
        padding: 14px 28px !important;
        font-size: 1.3em !important;
        font-weight: bold !important;
        height: 60px !important; /* Festgelegte Höhe für perfekte Symmetrie */
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    /* Roter Rahmen für den jeweils aktiven Button (Über mich auf dieser Seite) */
    div.stButton > button[data-testid="baseButton-primary"] {
        border: 2px solid #FF4B4B !important;
    }
    
    /* Kleiner Effekt beim Drüberfahren mit der Maus */
    div.stButton > button:hover {
        border-color: #FF4B4B !important;
        background-color: #FAFAFA !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Horizontales Menü (Exakt die identische Spaltenaufteilung wie auf der Startseite)
menu_col1, menu_col2, _ = st.columns([2.5, 2.5, 3])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Über mich", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Stefans_Autorenseite.py")

st.divider()

# 4. INHALT FÜR DIE AUTORENSEITE (Ohne die alte große Überschrift)
st.write("<br>", unsafe_allow_html=True)

# Spaltenverhältnis für Foto und Text
foto_col, text_col = st.columns([1.2, 2])

with foto_col:
    foto_name = "Bild_Autor.jpg" 
    if os.path.exists(foto_name):
        try:
            st.image(foto_name, use_container_width=True)
        except Exception:
            st.info("👤 Foto wird geladen...")
    else:
        st.info("📸 Foto folgt...")

with text_col:
    st.header("👤 Über mich")
    
    st.write("""
    <div style='font-size: 1.2em; line-height: 1.6;'>
    <p>Schön, dass Du den Weg auf meine persönliche Autorenseite gefunden hast.</p>
    <p>Mein Name ist Stefan Röser, ich wurde 1977 in Koblenz geboren und lebe mit meiner Frau und unseren beiden Kindern in der Nähe von Koblenz.</p>
    <p>Meine Leidenschaft gilt den historischen Romanen, die ich seit vielen Jahren begeistert lese. Mit <em>Ein leises wir</em> legte ich im Jahr 2025 mein erstes eigenes Werk in diesem Genre vor. Mit <em>Ein Herz, das keinen Zorn mehr trägt</em> veröffentlichte ich Anfang 2026 meinen zweiten Roman.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
