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

# 4. INHALT FÜR DIE AUTORENSEITE (Mit Passfoto)
st.write(f"<h1 style='text-align: center; color: #008080;'>Stefans Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Spalten für Foto und Text
foto_col, text_col = st.columns([1, 2])

with foto_col:
    # Der exakte Name deines hochgeladenen Fotos
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
    Schön, dass du den Weg auf meine persönliche Autorenseite gefunden hast! 
    
    Mein Name ist Stefan Röser. Das Schreiben ist für mich mehr als nur ein Handwerk – es ist die Leidenschaft, emotionale und tiefgründige Geschichten zu weben, die den Leser berühren und zum Nachdenken anregen.
    
    Hier werde ich dich in Zukunft über meine aktuellen Schreibprojekte auf dem Laufenden halten und dir exklusive Einblicke in meine Arbeit als Autor geben.
    """)

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
