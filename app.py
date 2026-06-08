import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

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
st.write(f"<h1 style='text-align: center; color: #FF4B4B;'>Willkommen in meiner Welt der Geschichten! ✍️✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Schön, dass du da bist.</h3>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Ich bin <strong>Stefan Röser</strong> und ich lade dich ein, in Erzählungen einzutauchen, 
die das Herz berühren und den Geist bewegen.
</p>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# LIVE-DEMO FÜR MARION (4 RUBRIKEN FLIESSEND)
# ==========================================

# RUBRIK 1: Foto von mir (inkl. Text)
st.header("👤 Über mich")
col_about1, col_about2 = st.columns([1, 2])
with col_about1:
    # Nutzt dein bestehendes Cover oder einen eleganten Platzhalter für Marions Foto
    if os.path.exists("stefan.png"):
        st.image("stefan.png", use_container_width=True)
    else:
        st.info("📸 [Hier steht später dein Autorenfoto]")
with col_about2:
    st.write("""
    **Herzlich Willkommen!**  
    Hier ist Platz für deine persönliche Vorstellung, Marion. Ein packender Text darüber, wer du bist, was dich antreibt und warum du schreibst. Deine Leser lieben es, das Gesicht hinter den Geschichten kennenzulernen. Dieser Bereich lässt sich flexibel so lang gestalten, wie du es benötigst.
    """)

st.divider()

# RUBRIK 2: Abbildung des Buchs + Kurzbeschreibung daneben (Jetzt im Handel bestellen: Logo Amazon etc.)
st.header("📚 Mein aktuelles Werk")
col_book1, col_book2 = st.columns([1, 2])
with col_book1:
    # Hier simulieren wir das Buch-Cover (z.B. mit The Novel Factory oder deinem aktuellen Buch)
    if os.path.exists("cover2.png"):
        st.image("cover2.png", use_container_width=True)
    else:
        st.info("📖 [Buch-Cover Placeholder]")
with col_book2:
    st.subheader("The Novel Factory / Ihr Buchtitel")
    st.write("""
    **Klappentext / Kurzbeschreibung:**  
    Hier setzen wir die packende Beschreibung deines Buches perfekt in Szene. Daneben platzieren wir direkte, auffällige Verlinkungen zu den Shops.
    """)
    
    # Simulation der Shop-Buttons (inkl. Amazon)
    st.markdown("### 🛒 Jetzt im Handel bestellen:")
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.link_button("🌐 Bei Amazon kaufen", "https://amazon.de", type="primary")
    with btn_col2:
        st.link_button("📖 Bei Thalia kaufen", "https://thalia.de")

st.divider()

# RUBRIK 3: Veranstaltungen (z.B. Lesungen)
st.header("📅 Veranstaltungen & Lesungen")
st.write("Verpasse keinen Termin! Hier findest du alle aktuellen Daten, an denen wir uns persönlich treffen können:")

# Eine schicke Tabelle oder strukturierte Liste für ihre Termine
termine = [
    {"Datum": "15. Oktober 2026", "Event": "Autorenlesung & Signierstunde", "Ort": "Stadtbibliothek, Berlin"},
    {"Datum": "04. November 2026", "Event": "Online-Werkstattgespräch (Zoom)", "Ort": "Überall (Digital)"},
    {"Datum": "12. Dezember 2026", "Event": "Große Premierenlesung", "Ort": "Buchhandlung Schmidt, Hamburg"}
]

for t in termine:
    with st.expander(f"📌 {t['Datum']} – {t['Event']}"):
        st.write(f"**Wo:** {t['Ort']}")
        st.write("Einlass ab 19:00 Uhr. Ich freue mich auf den Austausch mit euch! Eintritt frei.")

st.divider()

# RUBRIK 4: Multimedia (Fachartikel, Podcasts)
st.header("🎙️ Multimedia & Presse")
st.write("Interviews, Gastbeiträge und Gespräche hinter den Kulissen:")

col_media1, col_media2 = st.columns(2)

with col_media1:
    st.subheader("🎧 Podcast-Gast")
    st.info("»Im Gespräch über die Kunst des Schreibens«")
    st.write("Höre hier rein, wie ich im 'Autoren-Talk-Podcast' über die Entstehung meines neuesten Manuskripts spreche.")
    st.link_button("Jetzt reinhören", "https://spotify.com")

with col_media2:
    st.subheader("📰 Fachartikel")
    st.info("»Die Zukunft des Self-Publishing«")
    st.write("Mein Gastbeitrag im großen Literaturmagazin über die versteckten Kosten bei der Buchproduktion.")
    st.link_button("Artikel lesen", "https://google.com")


# ==========================================
# ENDE DER DEMO - HIER FOLGEN DEINE ORIGINALELEMENTE
# ==========================================

st.divider()

# DEIN BESTELLFORMULAR (Ehemals Punkt 5)
st.header("📦 Buch direkt bei mir bestellen")
st.write("Möchtest du das Buch bestellen? Fülle einfach das Formular unten aus. Deine Bestellung wird direkt in meiner Datenbank gespeichert!")

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

st.divider()

# Vorheriges Projekt (Nathaniel & Clara)
st.header("Vorheriges Projekt")
col3, col4 = st.columns([1, 2])

with col3:
    if os.path.exists("cover1.png"):
        st.image("cover1.png", caption="Mein erstes Werk", use_container_width=True)
    else:
        st.info("📖 Bild 'cover1.png' folgt...")

with col4:
    st.write("""
    Mein erstes Buch habe ich im Sommer 2025 veröffentlicht. 
    Es ist derzeit nur als E-Book über Amazon Kindle oder Kindle-Unlimited erhältlich.

    **Klappentext:**
    Berlin, späte Weimarer Republik: Eine Stadt voller Kontraste - Jazz und Aufmärsche, Hoffnung und Gefahr. 
    Mitten darin begegnen sich Nathaniel, ein amerikanischer Reporter, und Clara, die nach einem neuen Anfang sucht. 
    """)

# FOOTER (Copyright & Rechtliches)
st.divider()
st.write("<p style='text-align: center;'>© 2026 Stefan Röser</p>", unsafe_allow_html=True)

# Rechtliche Links in zwei Spalten
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
        Die von Ihnen eingegebenen Daten werden auf Google-Servern gespeichert, 
        damit der Autor die Bestellung bearbeiten kann. 
        Weitere Informationen finden Sie in der Datenschutzerklärung von Google.
        """)
