import streamlit as st
import os
import urllib.parse

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- DEINE KONFIGURATION ---
MEINE_EMAIL = "STEFAN@BOOKSART.DE" 

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)

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
    st.write("""
    **Klappentext:**
    Ein Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens.
    """)
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch)")

st.divider()

# --- BESTELLFORMULAR (PLAN B) ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Fülle die Felder aus und klicke auf 'Bestellung vorbereiten'.")

name = st.text_input("Dein Name")
email_kunde = st.text_input("Deine E-Mail-Adresse")
buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                           ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
widmung = st.text_area("Widmungswunsch (Optional)")

if st.button("Bestellung vorbereiten ✉️"):
    if name and email_kunde:
        # Erstellt den Text für die E-Mail
        betreff = f"Buchbestellung von {name}"
        nachricht = f"Hallo Stefan,\n\nich möchte gerne bestellen:\n\nBuch: {buch_auswahl}\nName: {name}\nE-Mail: {email_kunde}\nWidmung: {widmung}"
        
        # Codiert den Text für einen Web-Link (verhindert Fehler bei Sonderzeichen)
        mailto_link = f"mailto:{MEINE_EMAIL}?subject={urllib.parse.quote(betreff)}&body={urllib.parse.quote(nachricht)}"
        
        # Erzeugt einen Button/Link, der das Mail-Programm öffnet
        st.markdown(f"""
            <a href="{mailto_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #FF4B4B; color: white; padding: 10px; text-align: center; border-radius: 5px;">
                    KLICKE HIER, UM DIE MAIL JETZT ABSENDEN
                </div>
            </a>
        """, unsafe_allow_html=True)
        st.info("Hinweis: Nach dem Klick öffnet sich dein Mail-Programm. Du musst dort nur noch auf 'Senden' klicken.")
    else:
        st.warning("Bitte gib Namen und E-Mail an.")

st.divider()

# --- ABSCHNITT 2: Vorheriges Projekt ---
st.header("Vorheriges Projekt")
st.write("""
**Berlin, späte Weimarer Republik:** Eine Stadt voller Kontraste. 
Mitten darin begegnen sich Nathaniel und Clara...
""")

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser")
