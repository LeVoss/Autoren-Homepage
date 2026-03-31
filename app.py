import streamlit as st
import os
from datetime import datetime

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- CSS ZUM VERSTECKEN DER STREAMLIT-MENÜS ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stAppDeployButton {display:none;}
            #stDecoration {display:none;}
            [data-testid="stStatusWidget"] {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- FUNKTIONEN: DATEN SPEICHERN & ZÄHLEN ---

def update_besucherzaehler():
    datei = "besucher.txt"
    if not os.path.exists(datei):
        with open(datei, "w", encoding="utf-8") as f:
            f.write("0")
    zahl = 0
    try:
        with open(datei, "r", encoding="utf-8") as f:
            inhalt = f.read().strip()
            if inhalt.isdigit():
                zahl = int(inhalt)
    except Exception:
        zahl = 0
    if 'besuch_gezaehlt' not in st.session_state:
        zahl += 1
        try:
            with open(datei, "w", encoding="utf-8") as f:
                f.write(str(zahl))
        except Exception:
            pass 
        st.session_state['besuch_gezaehlt'] = True
    return zahl

def speichere_bestellung(name, anschrift, email, auswahl, widmung):
    zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    adresse_clean = anschrift.replace('\n', ' ').replace('\r', '')
    eintrag = f"{zeitstempel} | Name: {name} | Adresse: {adresse_clean} | Mail: {email} | Buch: {auswahl} | Widmung: {widmung}\n"
    with open("bestellungen.txt", "a", encoding="utf-8") as f:
        f.write(eintrag)

# Besucherstand abrufen
besucher_stand = update_besucherzaehler()

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #2C5E9E;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen, 
die das Herz berühren und den Geist bewegen.
</p>
""", unsafe_allow_html=True)

st.divider()

# --- ROMAN 1: Aktuelles Werk ---
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

# --- HINWEIS MÄNGELEXEMPLARE ---
st.info("""
**Sonderangebot:** Ein paar wenige Mängelexemplare zu verkaufen zum Preis von **9,90 Euro** (inklusive Versand). 
Hierbei handelt es sich um ein anderes Format (6:9) und eine zu große Schrift!
""")

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Möchtest du das Buch bestellen? Fülle einfach das Formular aus, ich melde mich dann per E-Mail bei Dir!")

with st.form("kunden_form", clear_on_submit=True):
    name = st.text_input("Dein Name")
    anschrift = st.text_area("Deine vollständige Anschrift (Straße, PLZ, Ort)")
    email = st.text_input("Deine E-Mail-Adresse")
    
    # Auswahlmöglichkeiten inklusive Mängelexemplar
    buch_optionen = [
        "Ein Herz (mit Signatur)", 
        "Ein Herz (ohne Signatur)",
        "Ein Herz (ohne Signatur) - Mängelexemplar"
    ]
    auswahl = st.selectbox("Welches Buch möchtest du?", options=buch_optionen)
    
    widmung = st.text_area("Widmungswunsch (Optional)")
    submit = st.form_submit_button("Jetzt verbindlich bestellen")
    
    if submit:
        if name and anschrift and email:
            speichere_bestellung(name, anschrift, email, auswahl, widmung)
            st.success(f"Vielen Dank, {name}! Deine Bestellung wurde erfolgreich gespeichert. Ich melde mich bald bei dir.")
            st.balloons()
        else:
            st.warning("Bitte fülle Name, Anschrift und E-Mail aus.")

st.divider()

# --- VORHERIGES PROJEKT ---
st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])

with col3:
    if os.path.exists("cover1.png"):
        st.image("cover1.png", caption="Mein erstes Werk", use_container_width=True)
    else:
        st.info("📖 Bild 'cover1.png' folgt...")

with col4:
    st.write("""
    **Über das Werk:**
    Berlin, späte Weimarer Republik: Eine Stadt voller Kontraste - Jazz und Aufmärsche, Hoffnung und Gefahr. 
    Mitten darin begegnen sich Nathaniel, ein amerikanischer Reporter, und Clara, die nach einem neuen Anfang sucht. 
    """)

# --- ADMIN LOGIN ---
st.markdown("---")
with st.expander("🛠️ Interner Bereich"):
    st.write("Dieser Bereich ist passwortgeschützt.")
    passwort_eingabe = st.text_input("Passwort", type="password")
    
    if passwort_eingabe == "Kalender20#":
        st.subheader("Statistik & Bestellungen")
        st.metric("Besucher gesamt", besucher_stand)
        st.divider()
        
        if os.path.exists("bestellungen.txt"):
            with open("bestellungen.txt", "r", encoding="utf-8") as f:
                bestellungen = f.readlines()
            
            if bestellungen:
                for b in reversed(bestellungen):
                    st.info(b.strip())
                
                if st.button("Alle Bestellungen löschen"):
                    if os.path.exists("bestellungen.txt"):
                        os.remove("bestellungen.txt")
                        st.rerun()
            else:
                st.write("Momentan liegen keine neuen Bestellungen vor.")
        else:
            st.write("Noch keine Bestellungen in der Datenbank.")

# --- RECHTLICHER FOOTER ---
st.divider()
col_inf1, col_inf2 = st.columns(2)

with col_inf1:
    with st.expander("Impressum"):
        st.write("""
        **Verantwortlich für den Inhalt:** Stefan Röser  
        [DEINE STRASSE]  
        [DEIN ORT]  
        E-Mail: [DEINE MAILADRESSE]
        """)

with col_inf2:
    with st.expander("Datenschutz"):
        st.write("""
        **Datennutzung:** Ihre Daten (Name, Adresse, E-Mail) werden ausschließlich 
        zur Abwicklung der Buchbestellung lokal gespeichert.  
        Eine Weitergabe an Dritte erfolgt nicht.
        """)

st.write("© 2026 Stefan Röser")
