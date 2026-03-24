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
    """)
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch)")

st.divider()

# --- BESTELLFORMULAR (MIT E-MAIL-FUNKTION) ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("""Fülle einfach das Formular aus, ich melde mich dann per E-Mail bei Dir!""")

# HIER DEINE E-MAIL EINTRAGEN
MEINE_EMAIL = "DEINE_EMAIL@BEISPIEL.stefan"

with st.form("bestellung"):
    name = st.text_input("stefan@booksart.de")
    email_kunde = st.text_input("Deine E-Mail-Adresse")
    buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                               ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
    widmung = st.text_area("Widmungswunsch (Optional)")
    
    submit = st.form_submit_button("Bestellanfrage senden")
    
    if submit:
        if name and email_kunde:
            # Hier simulieren wir den Versand oder nutzen eine Schnittstelle.
            # Für ein Video ist es am ehrlichsten zu sagen: 
            # "Hier werden die Daten verarbeitet."
            
            st.success(f"Danke {name}! Deine Anfrage wurde vorbereitet.")
            st.info("Hinweis für Stefan: Um E-Mails echt zu versenden, wird ein Dienst wie FormSubmit.co verknüpft.")
            
            # Profi-Tipp: In einem echten Deployment würde hier ein API-Call stehen.
        else:
            st.warning("Bitte gib zumindest deinen Namen und deine E-Mail an.")

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser | [Besuch mich auf Facebook](https://facebook.com/stefan.roeser.autor)")
