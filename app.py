import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import os

# --- DEIN TABELLEN-LINK HIER ---
SHEET_URL = "HIER_DEINEN_KOPIERTEN_LINK_EINFÜGEN"

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# Verbindung herstellen (Public Mode)
conn = st.connection("gsheets", type=GSheetsConnection)

# --- CSS ---
st.markdown("<style>#MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;} .stAppDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- FUNKTIONEN ---
def get_data(sheet_name):
    # Liest die Daten ohne Authentifizierung (da Link öffentlich zum Bearbeiten ist)
    return conn.read(spreadsheet=SHEET_URL, worksheet=sheet_name)

def save_besucher(zahl):
    df_neu = pd.DataFrame([[zahl]])
    conn.update(spreadsheet=SHEET_URL, worksheet="Besucher", data=df_neu)

def speichere_bestellung(name, anschrift, email, auswahl, widmung):
    existing_data = get_data("Bestellungen")
    neue_zeile = pd.DataFrame([{
        "Zeitstempel": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Name": name,
        "Adresse": anschrift.replace('\n', ' '),
        "E-Mail": email,
        "Auswahl": auswahl,
        "Widmung": widmung
    }])
    updated_df = pd.concat([existing_data, neue_zeile], ignore_index=True)
    conn.update(spreadsheet=SHEET_URL, worksheet="Bestellungen", data=updated_df)

# Besucher-Logik
try:
    df_besucher = get_data("Besucher")
    aktuell = int(df_besucher.iloc[0, 0])
except:
    aktuell = 0

if 'besuch_gezaehlt' not in st.session_state:
    aktuell += 1
    save_besucher(aktuell)
    st.session_state['besuch_gezaehlt'] = True

# --- LAYOUT & TEXTE ---
st.write(f"<h1 style='text-align: center; color: #2C5E9E;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Ich bin <strong>Stefan Röser</strong>.</p>", unsafe_allow_html=True)

st.divider()

# Buchvorstellung
st.header("Ein Herz, das keinen Zorn mehr trägt")
c1, c2 = st.columns([1, 2])
with c1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
with c2:
    st.write("Ein tief bewegender Roman über die Kraft des Vergebens.")
    st.markdown("**16,99 €** (Signiert) | **14,49 €** (Standard)")

st.info("**Sonderangebot:** Mängelexemplare für **9,90 Euro** (Format 6:9, große Schrift) verfügbar!")

# Formular
with st.form("bestellung"):
    name = st.text_input("Name")
    anschrift = st.text_area("Anschrift")
    email = st.text_input("E-Mail")
    auswahl = st.selectbox("Buchwahl", ["Ein Herz (mit Signatur)", "Ein Herz (ohne Signatur)", "Ein Herz (Mängelexemplar)"])
    widmung = st.text_area("Widmung")
    if st.form_submit_button("Bestellen"):
        if name and anschrift and email:
            speichere_bestellung(name, anschrift, email, auswahl, widmung)
            st.success("Bestellung gespeichert!")
            st.balloons()

# Admin
with st.expander("🛠️ Intern"):
    if st.text_input("Passwort", type="password") == "Kalender20#":
        st.metric("Besucher", aktuell)
        st.dataframe(get_data("Bestellungen"))

st.write("© 2026 Stefan Röser")
