import streamlit as st
import os

# Seiteneinstellungen
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# --- CSS ZUM VERSTECKEN DER MENÜS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_width=True)

# --- TITEL & WILLKOMMEN ---
st.write(f"<h1 style='text-align: center; color: #2C5E9E;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 1.2em;'>Ich bin <strong>Stefan Röser</strong>.</p>", unsafe_allow_html=True)

st.divider()

# --- ROMAN SEKTION ---
st.header("Ein Herz, das keinen Zorn mehr trägt")
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
with col2:
    st.write("""
    **Klappentext:**
    Ein Herz, das keinen Zorn mehr trägt, ist ein tief bewegender Roman über die Kraft des Vergebens und den Mut, die eigene Vergangenheit hinter sich zu lassen. 
    Begleiten Sie die Protagonisten auf einer emotionalen Reise, die zeigt, dass Heilung dort beginnt, wo Bitterkeit endet. 
    """)
    st.markdown("**Preis: 16,99 €** (Signiert) | **14,49 €** (Standard)")

st.divider()

# --- HINWEIS MÄNGELEXEMPLARE ---
st.info("""
**Sonderangebot:** Ein paar wenige Mängelexemplare zu verkaufen zum Preis von **9,90 Euro** (inklusive Versand). 
Hierbei handelt es sich um ein anderes Format (6:9) und eine zu große Schrift!
""")

# --- DAS BESTELLFORMULAR (EINGEBETTET) ---
st.header("📦 Buch direkt bei mir bestellen")
st.write("Fülle bitte das folgende Formular aus. Deine Daten werden sicher übertragen und ich melde mich per E-Mail bei dir!")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# HIER UNTEN DEN LINK ZWISCHEN DEN ANFÜHRUNGSZEICHEN ERSETZEN:
form_url = "1Y8d9NlBUj1UE2iDBJOAfB0mqQlNjXs4tz70LcNZnv34"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen…
    </iframe>
""", unsafe_allow_html=True)

st.divider()

# --- VORHERIGES PROJEKT ---
st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])
with col3:
    if os.path.exists("cover1.png"):
        st.image("cover1.png", use_container_width=True)
with col4:
    st.write("Berlin, späte Weimarer Republik: Eine Stadt voller Kontraste...")

st.divider()
st.write("© 2026 Stefan Röser")
