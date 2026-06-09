import streamlit as st

st.set_page_config(page_title="Veranstaltungen - Stefan Röser", page_icon="📅", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;} .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none !important;} section[data-testid="stSidebar"] {display: none !important;}
    div.stButton > button {
        background-color: #ffffff !important; color: #31333F !important; border: 2px solid #E6E8F1 !important;
        padding: 14px 10px !important; font-size: 1.1em !important; font-weight: bold !important;
        height: 60px !important; border-radius: 8px !important; transition: all 0.3s ease !important;
    }
    div.stButton > button[data-testid="baseButton-primary"] { border: 2px solid #FF4B4B !important; }
    div.stButton > button:hover { border-color: #FF4B4B !important; background-color: #FAFAFA !important; }
    </style>
    """, unsafe_allow_html=True)

menu_col1, menu_col2, menu_col3, menu_col4 = st.columns([2, 2, 2, 2])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Über mich", use_container_width=True): st.switch_page("pages/1_Über_mich.py")
with menu_col3:
    if st.button("📅 Termine", use_container_width=True, type="primary"): st.switch_page("pages/2_Veranstaltungen.py")
with menu_col4:
    if st.button("🎬 Media", use_container_width=True): st.switch_page("pages/3_Multimedia.py")

st.divider()
st.write("<br>", unsafe_allow_html=True)

st.header("📅 Zukünftige Termine & Lesungen")
st.write("<div style='font-size: 1.2em;'>Hier findest du bald alle aktuellen Termine zu Lesungen, Buchmessen und Signierstunden.</div>", unsafe_allow_html=True)

# Platzhalter für Marion
st.info("💡 *Muster-Eintrag für Marion:* Herbst 2026 – Lesung zu 'Ein Herz, das keinen Zorn mehr trägt' in Koblenz (Details folgen).")

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
