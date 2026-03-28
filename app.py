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

# Stand abrufen
besucher_stand = update_besucherzaehler()

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #2C5E9E;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 1.2em;'>Ich bin <strong>Stefan Röser</strong>.</p>", unsafe_allow_html=True)

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
    st.write("Ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen.")
    st.markdown("**16,99 €** (Signiertes Taschenbuch, inkl. Versand)")
    st.markdown("**14,49 €** (Standard Taschenbuch, inkl. Versand)")

st.divider()

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")
with st.form("kunden_form", clear_on_submit=True):
    name = st.text_input("Dein Name")
    anschrift = st.text_area("Deine vollständige Anschrift (Straße, PLZ, Ort)")
    email = st.text_input("Deine E-Mail-Adresse")
    
    auswahl = st.selectbox("Welches Buch
