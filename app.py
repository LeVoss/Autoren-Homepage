import streamlit as st
import os

# 1. SEITENEINSTELLUNGEN
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# 2. CSS (ENTFERNT STREAMLIT-MENÜS FÜR PROFIS-LOOK)
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

# 4. ROMAN 1: Aktuelles Werk
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])

with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", caption="Aktueller Roman", use_container_width=True)
    else:
        st.info("📖 Cover wird geladen...")

with col2:
    st.write("""
    **Klappentext:**
    Ein Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen. 
    Begleiten Sie die Protagonisten auf einer emotionalen Reise, die zeigt, dass Heilung dort beginnt, wo Bitterkeit endet. 
    Ein Buch für alle, die an die heilende Kraft der Menschlichkeit glauben.
    """)
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch, inkl. Versand)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch, inkl. Versand)")

st.divider()

# 5. HINWEIS MÄNGELEXEMPLARE
st.info("""
**Sonderangebot:** Ein paar wenige Mängelexemplare zu verkaufen zum Preis von **9,90 Euro** (inklusive Versand). 
Hierbei handelt es sich um ein anderes Format (6:9) und eine zu große Schrift!
""")

# 6. DAS BESTELLFORMULAR (EINGEBETTETES GOOGLE FORMULAR)
st.header("📦 Buch direkt bei mir bestellen")
st.write("""Möchtest du das Buch bestellen? Fülle einfach das Formular unten aus. Deine Bestellung wird direkt in meiner Datenbank gespeichert, so dass nichts verloren geht!""")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WICHTIG: Ersetze den Link unten durch deinen eigenen Google-Forms-Link!
# Den Link findest du unter 'Senden' -> '< >' -> nur die URL bei src="..." kopieren.
form_url = "HIER_DEINEN_LINK_VON_GOOGLE_FORMULAR_EINSETZEN"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen…
    </iframe>
""", unsafe_allow_html=True)

st.divider()

# 7. ABSCHNITT 2: Vorheriges Projekt
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
    Zwischen vorsichtigen Briefen und heimlichen Treffen wächst eine Verbindung, die stärker ist als Angst und Konvention. 
    Ein bewegender Roman über Liebe, Mut und die Kraft, in unsicheren Zeiten das Herz sprechen zu lassen.
    """)

# 8. FOOTER
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)
