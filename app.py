import streamlit as st
import os
import requests

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- DEINE KONFIGURATION ---
KONTAKT_EMAIL = "DEINE_EMAIL@BEISPIEL.DE" 

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)

st.divider()

# --- ROMAN 1 ---
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
    else:
        st.info("📖 Cover lädt...")
with col2:
    st.write("Ein tief bewegender Roman über die Kraft des Vergebens.")

st.divider()

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")

with st.form("bestellung"):
    name = st.text_input("Dein Name")
    email_kunde = st.text_input("Deine E-Mail-Adresse")
    buch_auswahl = st.selectbox("Welches Buch?", ["Ein Herz, das keinen Zorn mehr trägt", "Anfrage"])
    widmung = st.text_area("Widmungswunsch")
    
    submit = st.form_submit_button("Bestellanfrage senden")
    
    if submit:
        if name and email_kunde:
            # Wir senden die Daten an FormSubmit
            url = f"https://formsubmit.co/ajax/{KONTAKT_EMAIL}"
            payload = {
                "name": name,
                "email": email_kunde,
                "message": f"Bestellung: {buch_auswahl}\nWidmung: {widmung}"
            }
            
            try:
                # Hier passiert der eigentliche Versand
                response = requests.post(url, json=payload)
                
                if response.status_code == 200:
                    st.success(f"Erfolg! Bitte prüfe jetzt dein Postfach ({KONTAKT_EMAIL}) – auch den SPAM-Ordner!")
                    st.balloons() # Ein kleiner Effekt für das Video
                else:
                    st.error(f"Fehler vom Mail-Dienst: Status {response.status_code}")
                    st.info("Falls hier 'Status 404' steht, prüfe bitte die E-Mail-Adresse im Code.")
            except Exception as e:
                st.error(f"Technisches Problem: {e}")
        else:
            st.warning("Bitte Name und E-Mail ausfüllen.")

st.divider()

# --- ROMAN 2 (UNTER DEM FORMULAR) ---
st.header("Vorheriges Projekt")
st.write("Berlin, späte Weimarer Republik...")

# --- FOOTER ---
st.write("© 2026 Stefan Röser | [Facebook](https://facebook.com/stefan.roeser.autor)")
