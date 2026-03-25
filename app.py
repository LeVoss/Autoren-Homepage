import streamlit as st
import os
from datetime import datetime

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- FUNKTION: BESTELLUNG SPEICHERN ---
def speichere_bestellung(name, email, auswahl, widmung):
    zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    eintrag = f"{zeitstempel} | Name: {name} | Mail: {email} | Buch: {auswahl} | Widmung: {widmung}\n"
    with open("bestellungen.txt", "a", encoding="utf-8") as f:
        f.write(eintrag)

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
    st.markdown("**16,99 €** (mit Signatur) | **14,49 €** (ohne Signatur)")

st.divider()

# --- BESTELLFORMULAR (FÜR KUNDEN) ---
st.header("📦 Buch direkt bei mir bestellen")
with st.form("kunden_form", clear_on_submit=True):
    name = st.text_input("Dein Name")
    email = st.text_input("Deine E-Mail-Adresse")
    auswahl = st.selectbox("Welches Buch möchtest du?", 
                          ["Ein Herz, das keinen Zorn mehr trägt - mit Signatur", 
                           "Ein Herz, das keinen Zorn mehr trägt - ohne Signatur"])
    widmung = st.text_area("Widmungswunsch (Optional)")
    
    submit = st.form_submit_button("Jetzt verbindlich bestellen")
    
    if submit:
        if name and email:
            speichere_bestellung(name, email, auswahl, widmung)
            st.success(f"Vielen Dank, {name}! Deine Bestellung wurde gespeichert. Ich melde mich bald bei dir.")
        else:
            st.warning("Bitte Name und E-Mail ausfüllen.")

st.divider()

# --- VORHERIGES PROJEKT ---
st.header("Vorheriges Projekt")
st.write("Berlin, späte Weimarer Republik...")

# --- ADMIN LOGIN (NUR FÜR DICH) ---
st.markdown("---")
with st.expander("🔐 Admin-Bereich (Nur für Stefan)"):
    passwort = st.text_input("Passwort eingeben", type="password")
    if passwort == "stefan2026": # <--- DEIN PASSWORT
        st.subheader("Eingegangene Bestellungen:")
        if os.path.exists("bestellungen.txt"):
            with open("bestellungen.txt", "r", encoding="utf-8") as f:
                bestellungen = f.readlines()
            
            if bestellungen:
                for b in reversed(bestellungen): # Neueste zuerst
                    st.text(b.strip())
                if st.button("Liste löschen"):
                    os.remove("bestellungen.txt")
                    st.rerun()
            else:
                st.info("Noch keine Bestellungen vorhanden.")
        else:
            st.info("Die Datei wurde noch nicht erstellt (keine Bestellungen).")

st.write("© 2026 Stefan Röser")
