import streamlit as st
import os
import requests

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- DEINE KONFIGURATION ---
# Ersetze dies durch deine echte E-Mail-Adresse
KONTAKT_EMAIL = "DEINE_EMAIL@BEISPIEL.DE" 

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

# --- ROMAN 1 ---
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", caption="Aktueller Roman", use_container_width=True)
    else:
        st.info("📖 Cover wird geladen...")

with col2:
    st.write("**Klappentext:** Ein tief bewegender Roman über die Kraft des Vergebens.")
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch)")

st.divider()

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("""Fülle einfach das Formular aus, ich melde mich dann per E-Mail bei Dir!""")

with st.form("bestellung"):
    name = st.text_input("Dein Name")
    email_kunde = st.text_input("Deine E-Mail-Adresse")
    buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                               ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
    widmung = st.text_area("Widmungswunsch (Optional)")
    
    submit = st.form_submit_button("Bestellanfrage senden")
    
    if submit:
        if name and email_kunde:
            # Daten für den Versand vorbereiten
            form_data = {
                "Name": name,
                "Email": email_kunde,
                "Bestellung": buch_auswahl,
                "Widmung": widmung,
                "_subject": f"Neue Buchbestellung von {name}" # Betreffzeile der E-Mail
            }
            
            # Versand via FormSubmit (API Call)
            try:
                response = requests.post(f"https://formsubmit.co/ajax/{KONTAKT_EMAIL}", data=form_data)
                if response.status_code == 200:
                    st.success(f"Vielen Dank, {name}! Deine Anfrage wurde versendet. Ich melde mich in Kürze bei dir.")
                else:
                    st.error("Es gab ein Problem beim Versand. Bitte versuche es später noch einmal.")
            except:
                st.error("Verbindung zum Mail-Server fehlgeschlagen.")
        else:
            st.warning("Bitte gib Namen und E-Mail-Adresse an.")

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser | [Besuch mich auf Facebook](https://facebook.com/stefan.roeser.autor)")
