import streamlit as st
import os

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Stefans Autorenwelt", 
    page_icon="✍️", 
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

# 4. INHALT FÜR DIE AUTORENSEITE (Mit größerem Foto und größerer Schrift)
st.write(f"<h1 style='text-align: center; color: #008080;'>Stefans Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Spaltenverhältnis von [1, 2] auf [1.2, 2] geändert, um das Foto zu vergrößern
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
    
    # Der Text wird hier über ein HTML-Format mit einer größeren Schriftstärke (1.2em) ausgegeben
    st.write("""
    <div style='font-size: 1.2em; line-height: 1.6;'>
    <p>Schön, dass Du den Weg auf meine persönliche Autorenseite gefunden hast.</p>
    <p>Mein Name ist Stefan Röser, ich wurde 1977 in Koblenz geboren und lebe mit meiner Frau und unseren beiden Kindern in der Nähe von Koblenz.</p>
    <p>Meine Leidenschaft gilt den historischen Romanen, die ich seit vielen Jahren begeistert lese. Mit <em>Ein leises wir</em> legte ich im Jahr 2025 mein erstes eigenes Werk in diesem Genre vor. Mit <em>Ein Herz, das keinen Zorn mehr trägt</em> veröffentlichte ich Anfang 2026 meinen zweiten Roman.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
