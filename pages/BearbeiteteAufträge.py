import streamlit as st
import pandas as pd
import altair as alt

# Lade die CSV-Datei
@st.cache
def load_data():
    data = pd.read_csv("bearbeitsungsstatus.csv")
    return data

data = load_data()

# Zeige die Daten als Tabelle
st.write("Bearbeitungsstatus CSV-Datei")
st.write(data)

# Füge einen Download-Button hinzu
st.download_button(
    label="CSV-Datei herunterladen",
    data=data.to_csv(index=False).encode('utf-8'),
    file_name="bearbeitsungsstatus.csv",
    key="download-button"
)

# Erstelle das anpassbare Balkendiagramm mit Altair
base = alt.Chart(data, width=600, height=400).encode(x='Kunde:N', y='Zeitdifferenz:Q')
color_condition = alt.condition(
    alt.datum['Kundentakt'] <= alt.datum['Zeitdifferenz'],
    alt.value('green'), alt.value('red')
)
bars = base.mark_bar().encode(
    color=color_condition
)
st.altair_chart(bars, use_container_width=True)
