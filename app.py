import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Stefan Röser | Autor", page_icon="✍️", layout="centered")

# 2. CSS (Entfernt Menüs für einen sauberen Look)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 3. TITEL & WILLKOMMEN
st.write(f"<h1 style='text-align: center; color: #2E4053;'>Willkommen in der Welt von Stefan Röser 📚</h1>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Schön, dass du hier bist. Tauche ein in meine Geschichten über das Leben, die Liebe und den Weg zu sich selbst.
</p>
""", unsafe_allow_html=True)

st.divider()

# 4. Buch-Präsentation: Roman
st.header("Aktueller Roman")
col1, col2 = st.columns([1, 2])
with col1:
    # Hier das Cover deines Romans (z.B. cover_roman.png)
    if os.path.exists("cover_roman.png"):
        try:
            st.image("cover_roman.png", use_container_width=True)
        except Exception:
            st.error("Bilddatei konnte nicht geladen werden.")
    else:
        st.info("📖 Cover-Bild folgt...")

with col2:
    st.write("""
    **Ein Herz, das keinen Zorn mehr trägt**
    Ein bewegender Roman über Vergebung, zweite Chancen und die Suche nach dem inneren Frieden. Begleite die Protagonisten auf einer Reise, die zeigt, dass es nie zu spät ist, die Schatten der Vergangenheit hinter sich zu lassen.
    """)

st.divider()

# 5. BESTELL-ÜBERSICHT & FORMULAR
st.header("📦 Buch direkt bei mir bestellen")
st.write("Wähle hier deine gewünschte Ausgabe aus (Preise inkl. Versand innerhalb Deutschland):")

st.markdown("""
* **14,99 €** – Ein Herz, das keinen Zorn mehr trägt (Taschenbuch)
""")

# Hier bleibt die URL deines ursprünglichen Stefan-Röser-Bestellformulars
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

# 6. FOOTER
st.divider()
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)

footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    with st.expander("Impressum"):
        st.write("""
        **Angaben gemäß § 5 TMG:** Stefan Röser,  
        c/o Online Impressum.de #6281, Europaring 90, 
        53757 Sankt Augustin
        
        **Kontakt:** E-Mail: stefan@booksart.de  
        """)
with footer_col2:
    with st.expander("Datenschutz"):
        st.write("""
        **Datenschutzerklärung** Diese Seite nutzt ein eingebettetes Google Formular zur Bestellabwicklung. 
        Die Daten werden auf Google-Servern gespeichert, damit der Autor die Bestellung bearbeiten kann. 
        """)
