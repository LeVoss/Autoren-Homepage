import streamlit as st
import os

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- TITEL & WILLKOMMEN ---
st.title("Willkommen auf der offiziellen Seite von Stefan Röser")
st.markdown("### Geschichten, die das Herz berühren.")

st.divider()

# --- ROMAN 1: Ein Herz, das keinen Zorn mehr trägt ---
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])

with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", caption="Aktueller Roman", use_container_width=True)
    else:
        st.info("📖 Cover wird geladen...")
        st.write("Vorhandene Dateien:", os.listdir("."))

with col2:
    st.write("""
    **Klappentext:**
    Ein Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen. 
    Begleiten Sie die Protagonisten auf einer emotionalen Reise, die zeigt, dass Heilung dort beginnt, wo Bitterkeit endet. 
    Ein Buch für alle, die an die heilende Kraft der Menschlichkeit glauben.
    """)
    st.markdown("**Preis: 14,90 €** (Signiertes Exemplar)")

st.divider()

# --- ABSCHNITT 2: Platzhalter oder weiteres Werk ---
st.header("Vorschau & Projekte")
col3, col4 = st.columns([1, 2])

with col3:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", caption="In Arbeit", use_container_width=True)
    else:
        st.info("📖 Bild folgt...")

with col4:
    st.write("""
    **Vorheriges Projekt:**
    Mein erstes Buch habe ich im Sommer 2025 veröffentlicht.
    """) # <--- Das hier hat gefehlt!

st.divider()

# --- BESTELLFORMULAR ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Möchtest du ein signiertes Buch? Fülle einfach das Formular aus, ich melde mich dann per E-Mail bei dir!")

with st.form("bestellung"):
    name = st.text_input("Dein Name")
    email = st.text_input("Deine E-Mail-Adresse")
    buch_auswahl = st.selectbox("Welches Buch möchtest du?", 
                               ["Ein Herz, das keinen Zorn mehr trägt", "Andere Anfrage"])
    widmung = st.text_area("Widmungswunsch (Optional)")
    
    submit = st.form_submit_button("Bestellanfrage senden")
    
    if submit:
        if name and email:
            st.success(f"Danke {name}! Ich habe deine Anfrage erhalten und sende dir bald eine E-Mail.")
        else:
            st.warning("Bitte gib zumindest deinen Namen und deine E-Mail an.")

# --- FOOTER ---
st.markdown("---")
st.write("© 2026 Stefan Röser | [Besuch mich auf Facebook](https://facebook.com)")
