import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# 2. Titel & Willkommen
st.write("<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.write(<p style='text-align: center; font-size: 1.2em;'>

Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen, 

die das Herz berühren und den Geist bewegen.

</p>

""", unsafe_allow_html=True)

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
# --- DAS BESTELLFORMULAR ---
form_url = "HIER_DEINEN_LINK_EINSETZEN"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

st.divider()

# --- ABSCHNITT 2: Vorheriges Projekt ---
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

# --- FOOTER ---
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)
