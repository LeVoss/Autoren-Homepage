import streamlit as st
import os
import urllib.parse

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- DEINE KONFIGURATION ---
# Gib hier deine Handynummer im internationalen Format an (z.B. 491701234567)
# WICHTIG: Keine Leerzeichen, kein Plus, keine führenden Nullen!
MEINE_WHATSAPP = "491632012232" 

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

# --- BESTELLUNG VIA WHATSAPP ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Fülle die Felder aus und sende mir deine Bestellung bequem per WhatsApp.")

# Eingabefelder
name = st.text_input("Dein Name")
email_kunde = st.text_input("Deine E-Mail-Adresse (für die Rechnung/Kontakt)")
buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                           [
                               "Ein Herz, das keinen Zorn mehr trägt - mit Signatur", 
                               "Ein Herz, das keinen Zorn mehr trägt - ohne Signatur",
                               "Andere Anfrage"
                           ])
widmung = st.text_area("Widmungswunsch (Optional)")

if st.button("Bestellung per WhatsApp vorbereiten 🟢"):
    if name and email_kunde:
        # Nachricht für WhatsApp zusammenbauen
        text = (
            f"Hallo Stefan, ich möchte gerne bestellen:\n\n"
            f"*Buch:* {buch_auswahl}\n"
            f"*Name:* {name}\n"
            f"*E-Mail:* {email_kunde}\n"
            f"*Widmung:* {widmung if widmung else 'Keine'}"
        )
        
        # Link generieren
        wa_link = f"https://wa.me/{MEINE_WHATSAPP}?text={urllib.parse.quote(text)}"
        
        # Bestätigung und Weiterleitungs-Button
        st.info("Deine Bestelldaten wurden vorbereitet. Klicke jetzt auf den Button unten, um sie abzuschicken.")
        st.markdown(f"""
            <a href="{wa_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 1.1em;">
                    JETZT WHATSAPP ABSENDEN ✅
                </div>
            </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("Bitte gib deinen Namen und deine E-Mail-Adresse an.")

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
    """)

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser")
