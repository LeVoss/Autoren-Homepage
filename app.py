import streamlit as st
import os

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen, 
die das Herz berühren und den Geist bewegen.
</p>
""", unsafe_allow_html=True)

st.divider()

# --- ROMAN 1: Ein Herz, das keinen Zorn mehr trägt ---
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
    """)
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch, inkl. Versand)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch, inkl. Versand)")

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
    **Berlin, späte Weimarer Republik:** Eine Stadt voller Kontraste - Jazz und Aufmärsche, Hoffnung und Gefahr. 
    Mitten darin begegnen sich Nathaniel, ein amerikanischer Reporter, und Clara, die nach einem neuen Anfang sucht.
    
    *Derzeit als E-Book über Amazon Kindle erhältlich.*
    """)

st.divider()

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("""Möchtest du das Buch "Ein Herz, das keinen Zorn mehr trägt" bestellen? Wenn ja, fülle einfach das Formular aus, ich melde mich dann per E-Mail bei Dir!""")

with st.form("bestellung"):
    name = st.text_input("Dein Name")
    email_kunde = st.text_input("Deine E-Mail-Adresse")
    buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                               ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
    widmung = st.text_area("Widmungswunsch (Optional)")
    
    submit = st.form_submit_button("Bestellanfrage senden")
    
    if submit:
        if name and email_kunde:
            # Professionelle Bestätigung für den Nutzer
            st.success(f"Vielen Dank, {name}! Deine Bestellanfrage wurde erfolgreich übermittelt. Ich melde mich in Kürze unter {email_kunde} bei dir.")
        else:
            st.warning("Bitte gib mindestens deinen Namen und deine E-Mail-Adresse an, damit ich dich erreichen kann.")

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser | [Besuch mich auf Facebook](https://facebook.com/stefan.roeser.autor)")
