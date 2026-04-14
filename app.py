import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# 2. CSS (Entfernt Menüs für einen sauberen Look)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 3. TITEL & WILLKOMMEN
st.write(f"<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen, 
die das Herz berühren und den Geist bewegen.
</p>
""", unsafe_allow_html=True)

st.divider()

# 4. Aktuelles Buch & Preisliste
st.header("Meine aktuellen Titel")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
with col2:
    st.write("""
    **Ein Herz, das keinen Zorn mehr trägt**
    Ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen. 
    Ein Buch für alle, die an die heilende Kraft der Menschlichkeit glauben.
    """)
    st.write("---")
    st.markdown("**16,99 €** (Signiertes Taschenbuch, inkl. Versand innerhalb Deutschland)")
    st.markdown("**14,49 €** (Standard Taschenbuch, inkl. Versand innerhalb Deutschland)")
    st.markdown("**9,99 €** (Mängelexemplar, inkl. Versand innerhalb Deutschland)")
    st.markdown("**14,99 €** (Die Roman-Fabrik, inkl. Versand innerhalb Deutschland)")

st.info("Sonderangebot: Mängelexemplare von 'Ein Herz, das keinen Zorn mehr trägt' (Format 6:9, große Schrift) für **9,99 Euro** inkl. Versand verfügbar!")

st.divider()

# 5. DAS BESTELLFORMULAR
st.header("📦 Buch direkt bei mir bestellen")
st.write("Möchtest du eines meiner Bücher bestellen? Fülle einfach das Formular unten aus. Bitte wähle im Formular deine gewünschte Option aus:")

# Deine 4 Optionen für das Google Formular:
# 1. Ein Herz, das keinen Zorn mehr trägt (signiert): 16,99 Euro
# 2. Ein Herz, das keinen Zorn mehr trägt (nicht signiert): 14,49 Euro
# 3. Ein Herz, das keinen Zorn mehr trägt (Mängelexemplar): 9,99 Euro
# 4. Die Roman-Fabrik (nicht signiert): 14,99 Euro

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

st.divider()

# 6. Vorheriges Projekt
st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])

with col3:
    if os.path.exists("cover1.png"):
        st.image("cover1.png", caption="Mein erstes Werk", use_container_width=True)
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

# 7. FOOTER (Copyright & Rechtliches)
st.divider()
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)

footer_col1, footer_col2 = st.columns(2)

with footer_col1:
    with st.expander("Impressum"):
        st.write("""
        **Angaben gemäß § 5 TMG:** Stefan Röser,  
        c/o Online Impressum.de #628
