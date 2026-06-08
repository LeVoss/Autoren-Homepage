import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Autor Stefan Röser", page_icon="✍️", layout="centered")

# 2. CSS (Entfernt Menüs für einen sauberen Look und stylt die Tabs)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    
    /* Macht die Tabs optisch etwas präsentierbarer */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF4B4B !important;
        color: white !important;
    }
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
# NEU: DIE REITER-NAVIGATION (TABS) FÜR MARION
# ==========================================
st.markdown("<h3 style='text-align: center; color: #333333;'>Demo: Deine Rubriken als Reiter</h3>", unsafe_allow_html=True)

# Hier definieren wir die 4 Reiter oben drüber
tab1, tab2, tab3, tab4 = st.tabs(["👤 Über mich", "📚 Mein Buch", "📅 Veranstaltungen", "🎙️ Multimedia"])

# REITER 1: Über mich
with tab1:
    st.write("## ") # Kleiner Abstandhalter
    col_about1, col_about2 = st.columns([1, 2])
    with col_about1:
        if os.path.exists("stefan.png"):
            st.image("stefan.png", use_container_width=True)
        else:
            st.info("📸 [Autorenfoto]")
    with col_about2:
        st.write("""
        **Herzlich Willkommen!**  
        Hier ist Platz für deine persönliche Vorstellung, Marion. Ein packender Text darüber, wer du bist, was dich antreibt und warum du schreibst. Deine Leser lieben es, das Gesicht hinter den Geschichten kennenzulernen.
        """)

# REITER 2: Mein Buch
with tab2:
    st.write("## ")
    col_book1, col_book2 = st.columns([1, 2])
    with col_book1:
        if os.path.exists("cover2.png"):
            st.image("cover2.png", use_container_width=True)
        else:
            st.info("📖 [Buch-Cover]")
    with col_book2:
        st.subheader("Ihr Buchtitel / The Novel Factory")
        st.write("""
        **Klappentext / Kurzbeschreibung:**  
        Hier setzen wir die packende Beschreibung deines Buches perfekt in Szene. Daneben platzieren wir direkte, schnelle Verlinkungen zu den Shops.
        """)
        st.markdown("### 🛒 Jetzt im Handel bestellen:")
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.link_button("🌐 Bei Amazon kaufen", "https://amazon.de", type="primary")
        with btn_col2:
            st.link_button("📖 Bei Thalia kaufen", "https://thalia.de")

# REITER 3: Veranstaltungen
with tab3:
    st.write("## ")
    st.write("### Aktuelle Termine & Lesungen")
    termine = [
        {"Datum": "15. Oktober 2026", "Event": "Autorenlesung & Signierstunde", "Ort": "Stadtbibliothek, Berlin"},
        {"Datum": "04. November 2026", "Event": "Online-Werkstattgespräch (Zoom)", "Ort": "Überall (Digital)"},
        {"Datum": "12. Dezember 2026", "Event": "Große Premierenlesung", "Ort": "Buchhandlung Schmidt, Hamburg"}
    ]
    for t in termine:
        with st.expander(f"📌 {t['Datum']} – {t['Event']}"):
            st.write(f"**Wo:** {t['Ort']}")
            st.write("Einlass ab 19:00 Uhr. Ich freue mich auf den Austausch mit euch! Eintritt frei.")

# REITER 4: Multimedia
with tab4:
    st.write("## ")
    st.write("### Interviews & Medienberichte")
    col_media1, col_media2 = st.columns(2)
    with col_media1:
        st.subheader("🎧 Podcast-Gast")
        st.info("»Im Gespräch über die Kunst des Schreibens«")
        st.link_button("Jetzt reinhören", "https://spotify.com")
    with col_media2:
        st.subheader("📰 Fachartikel")
        st.info("»Die Zukunft des Self-Publishing«")
        st.link_button("Artikel lesen", "https://google.com")

# ==========================================
# ENDE DER DEMO - HIER FOLGEN DEINE ORIGINALELEMENTE
# ==========================================

st.divider()

# DEIN BESTELLFORMULAR
st.header("📦 Buch direkt bei mir bestellen")
st.write("Möchtest du das Buch bestellen? Fülle einfach das Formular unten aus. Deine Bestellung wird direkt in meiner Datenbank gespeichert!")

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

st.divider()

# Vorheriges Projekt
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
