import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# 2. Titel & Willkommen
st.write("<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 1.2em;'>Ich bin <strong>Stefan Röser</strong>.</p>", unsafe_allow_html=True)

st.divider()

# 3. Aktuelles Buch (Kurzfassung für maximale Übersicht)
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
with col2:
    st.subheader("Ein Herz, das keinen Zorn mehr trägt")
    st.write("Ein tief bewegender Roman über die Kraft des Vergebens.")
    st.markdown("**16,99 €** (Signiert) | **14,49 €** (Standard)")

st.info("Sonderangebot: Mängelexemplare (Format 6:9, große Schrift) für **9,90 Euro** inkl. Versand verfügbar!")

st.divider()

# 4. DAS BESTELLFORMULAR (Das Herzstück)
st.header("📦 Buch direkt bei mir bestellen")
st.write("Bitte fülle das Formular aus. Die Daten werden sicher in Google gespeichert.")

# HIER DEINEN LINK ZWISCHEN DIE ANFÜHRUNGSZEICHEN SETZEN:
# Beispiel: https://docs.google.com/forms/d/e/1FAIpQLS.../viewform?embedded=true
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?usp=dialog"

if form_url == "DEIN_GOOGLE_FORMULAR_LINK_HIER":
    st.warning("⚠️ Bitte füge noch deinen Google-Forms-Link im Code ein!")
else:
    st.markdown(f"""
        <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
            Wird geladen…
        </iframe>
    """, unsafe_allow_html=True)

st.divider()

# 5. Vorheriges Projekt
st.subheader("Vorheriges Projekt: Berlin Roman")
if os.path.exists("cover1.png"):
    st.image("cover1.png", width=200)
st.write("Mein Erstlingswerk aus dem Sommer 2025.")

st.write("© 2026 Stefan Röser")
