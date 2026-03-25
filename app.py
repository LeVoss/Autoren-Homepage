import streamlit as st
import os
import urllib.parse

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- DEINE KONFIGURATION ---
# Gib hier deine Handynummer im internationalen Format an (z.B. 491701234567)
MEINE_WHATSAPP = "49123456789"  # <--- BITTE ANPASSEN (ohne + oder 00 am Anfang)

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
    st.markdown("**Preis: 16,99 €** (Signiertes Taschenbuch, inkl. Versand)")
    st.markdown("**Preis: 14,49 €** (Standard Taschenbuch, inkl. Versand)")

st.divider()

# --- BESTELLUNG VIA WHATSAPP ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Fülle die Felder aus und sende mir deine Bestellung direkt per WhatsApp.")

name = st.text_input("Dein Name")
buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                           ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
widmung = st.text_area("Widmungswunsch (Optional)")

if st.button("Bestellung per WhatsApp senden 🟢"):
    if name:
        # Nachricht zusammenbauen
        text = f"Hallo Stefan, ich möchte gerne bestellen:\n\n*Buch:* {buch_auswahl}\n*Name:* {name}\n*Widmung:* {widmung}"
        
        # Link für WhatsApp generieren
        # wa.me öffnet direkt den Chat mit dir
        wa_link = f"https://wa.me/{MEINE_WHATSAPP}?text={urllib.parse.quote(text)}"
        
        # Schöner Button zur Weiterleitung
        st.markdown(f"""
            <a href="{wa_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 12px; text-align: center; border-radius: 8px; font-weight: bold;">
                    JETZT WHATSAPP ÖFFNEN & ABSENDEN
                </div>
            </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("Bitte gib zumindest deinen Namen an.")

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
