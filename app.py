import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(
    page_title="Autor Stefan Röser", 
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
    
    /* Roter Rahmen für den jeweils aktiven Button (Home auf dieser Seite) */
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

# 3. Horizontales Menü (Symmetrisches Spaltenverhältnis)
menu_col1, menu_col2, _ = st.columns([2.5, 2.5, 3])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True, type="primary"):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Über mich", use_container_width=True):
        st.switch_page("pages/1_Stefans_Autorenseite.py")

st.divider()

# 4. DEIN INHALT (Startseite)
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
    Begleiten Sie die Protagonisten auf einer emotionalen Reise, die zeigt, dass Heilung dort beginnt, wo Bitterkeit endet. 
    Ein Buch für alle, die an die heilende Kraft der Menschlichkeit glauben.
    """)
    st.markdown("**16,99 €** (Signiertes Taschenbuch, inkl. Versand (innerhalb Deutschland))")
    st.markdown("**14,49 €** (Standard Taschenbuch, inkl. Versand (innerhalb Deutschland))")

st.info("Sonderangebot: Mängelexemplare (Format 6:9, große Schrift) für **9,99 Euro** inkl. Versand (innerhalb Deutschland) verfügbar!")

st.divider()

# DAS BESTELLFORMULAR
st.header("📦 Buch direkt bei mir bestellen")
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"
st.markdown(f'<iframe src="{form_url}" width="100%" height="900" frameborder="0">Wird geladen...</iframe>', unsafe_allow_html=True)

st.divider()

# Vorheriges Projekt
st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])
with col3:
    if os.path.exists("cover1.png"):
        try:
            st.image("cover1.png", caption="Mein erstes Werk", use_container_width=True)
        except Exception:
            st.info("📖 Buchcover 'cover1' wird geladen...")
    else:
        st.info("📖 Bild 'cover1.png' folgt...")
with col4:
    st.write("""
    Mein erstes Buch habe ich im Sommer 2025 veröffentlicht. 
    Es ist derzeit nur als E-Book über Amazon Kindle oder Kindle-Unlimited erhältlich.

    **Klappentext:**
    Berlin, späte Weimarer Republik: Eine Stadt voller Kontraste - Jazz und Aufmärsche, Hoffnung und Gefahr. 
    Mitten darin begegnen sich Nathaniel, ein amerikanischer Reporter, und Clara, die nach einem neuen Anfang sucht. 
    """)

# FOOTER
st.divider()
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)

footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    with st.expander("Impressum"):
        st.write("""
        **Angaben gemäß § 5 TMG:** Stefan Röser,  
        c/o Online Impressum.de #6281, Europaring 90, 
        53757 Sankt Augustin
         
        **Kontakt:** E-Mail: stefan@booksart.de  
        """)
with footer_col2:
    with st.expander("Datenschutz"):
        st.write("""
        **Datenschutzerklärung** Diese Seite nutzt ein eingebettetes Google Formular zur Bestellabwicklung. 
        Die von Ihnen eingegebenen Daten werden auf Google-Servern gespeichert.
        """)
