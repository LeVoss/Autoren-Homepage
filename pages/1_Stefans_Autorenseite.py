import streamlit as st

st.set_page_config(page_title="Marions Autorenwelt", page_icon="👤", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# Das identische Menü für die Unterseite
menu_col1, menu_col2, _ = st.columns([1, 2, 5])
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with menu_col2:
    if st.button("👤 Marions Autorenwelt", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Marions_Autorenseite.py")
st.divider()

# MARIONS INHALT
st.write(f"<h1 style='text-align: center; color: #008080;'>Marions Autorenwelt ✍️✨</h1>", unsafe_allow_html=True)

st.header("👤 1. Über mich")
st.write("Hier ist Platz für deine persönliche Vorstellung, Marion.")

st.divider()
st.write("<p style='text-align: center; font-size: 0.8em; color: gray;'>Vorschau-Modus für Marion | Erstellt von Stefan Röser</p>", unsafe_allow_html=True)
