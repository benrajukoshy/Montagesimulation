# Contents of ~/my_app/main_page.py
import streamlit as st
from PIL import Image

image = Image.open('/bilder/layout.png')
st.sidebar.image("https://www.fau.de/files/2021/10/neues-fau-logo-nur-fuer-webmeldung-1024x198.jpg", use_column_width=True)

st.markdown("# Hauptmenü 🏚️")
st.sidebar.markdown("# Hauptmenü 🏚️")

st.title("Montagesimulation")
st.write("Im Rahmen eines Praktikums wird die Analyse und Optimierung nach Methoden der schlanken Produktion vermittelt.")
st.write("Diese Streamlit App dient der digitalen Abbildung von Bestellungen, deren Bearbeitung und Qualitätskontrolle")

st.image(image, caption='Layout mit den Arbeitsstationen')
