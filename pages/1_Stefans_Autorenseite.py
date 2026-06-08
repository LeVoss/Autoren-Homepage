import streamlit as st

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Stefans Autorenwelt", 
    page_icon="👤", 
    layout="centered"
)

# 2. CSS (Sidebar verstecken)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stSidebarCollapseButton"] {display: none !important;}
    section[data-testid="stSidebar"] {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. Horizontales Menü (Mit internem Streamlit-Pfad)
menu_col1, menu_col2, _ = st.columns([1, 2, 5])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Stefans Autorenwelt", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Stefans_Autorenseite.py")

st.divider()

# 4. INHALT FÜR DIE AUTORENSEITE
st.write(f"<h1 style='text-align: center; color: #008080;'>Stefans Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)

st.header("👤 Über mich")
st.write("""
Hier ist Platz für deine persönliche Vorstellung als Autor! 
Erzähle deinen Lesern von deinem Werdegang, deinen Inspirationen oder woran du aktuell arbeitest.
""")

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Autorenseite von Stefan Röser</p>", unsafe_allow_html=True)
