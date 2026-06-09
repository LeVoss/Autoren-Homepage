import streamlit as st
import os

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Stefans Autorenwelt", 
    page_icon="👤", 
    layout="centered"
)

# 2. CSS (Sidebar verstecken)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none !important;}
    section[data-testid="stSidebar"] {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. Horizontales Menü
menu_col1, menu_col2, _ = st.columns([1, 2, 5])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Stefans Autorenwelt", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Stefans_Autorenseite.py")

st.divider()

# 4. INHALT FÜR DIE AUTORENSEITE (Mit Passfoto und neuem Text)
st.write(f"<h1 style='text-align: center; color: #008080;'>Stefans Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Spalten für Foto und Text
foto_col, text_col = st.columns([1, 2])

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
    Schön, dass Du den Weg auf meine persönliche Autorenseite gefunden hast.
    
    Mein Name ist Stefan Röser, ich wurde 1977 in Koblenz geboren und lebe mit meiner Frau und unseren beiden Kindern in der Nähe von Koblenz.
    
    Meine Leidenschaft gilt den historischen Romanen, die ich seit vielen Jahren begeistert lese. Mit *Ein leises wir* legte ich im Jahr 2025 mein erstes eigenes Werk in diesem Genre vor. Mit *Ein Herz, das keinen Zorn mehr trägt* veröffentlichte ich Anfang 2026 meinen zweiten Roman.
    """)

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
