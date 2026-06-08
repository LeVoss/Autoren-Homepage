import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(
    page_title="Autor Stefan Röser", 
    page_icon="✍️", 
    layout="centered"
)

# 2. CSS (Entfernt störende Elemente)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 3. Offizielle Streamlit-Navigation (Korrigierte Pfade!)
# WICHTIG: Bei Dateien im pages-Ordner wird NUR der Dateiname ohne "pages/" übergeben!
home_page = st.Page("app.py", title="Home", icon="🏠", default=True)
marion_page = st.Page("1_Stefans_Autorenseite.py", title="Marions Autorenwelt", icon="👤")

# Das lädt die Seiten im Hintergrund, position="hidden" blendet die linke Sidebar aus
pg = st.navigation([home_page, marion_page], position="hidden")

# Horizontale Buttons ganz oben als Menü
menu_col1, menu_col2, _ = st.columns([1, 2, 5])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True, type="primary"):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Marions Autorenwelt", use_container_width=True):
        st.switch_page("pages/1_Marions_Autorenseite.py")

st.divider()

# Hier startet die eigentliche Navigation
pg.run()

# 4. DEIN ORIGINALER INHALT (Startseite)
st.write("<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 1.2em;'>Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen.</p>", unsafe_allow_html=True)

# Aktuelles Buch
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        try:
            st.image("cover2.png", use_container_width=True)
        except Exception:
            st.info("📖 Buchcover 'cover2' wird geladen...")
    else:
        st.info("📖 Bild 'cover2.png' folgt...")
with col2:
    st.write("""
    **Klappentext:**
    Ein Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen. 
    """)

st.divider()

# DAS BESTELLFORMULAR
st.header("📦 Buch direkt bei mir bestellen")
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"
st.markdown(f'<iframe src="{form_url}" width="100%" height="900" frameborder="0">Wird geladen...</iframe>', unsafe_allow_html=True)

st.divider()

# FOOTER
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)
