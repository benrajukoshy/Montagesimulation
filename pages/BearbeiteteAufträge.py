import streamlit as st
import pandas as pd
import altair

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

# Erstelle das Balkendiagramm
st.bar_chart(data[["Kunde", "Zeitdifferenz"]].set_index("Kunde"))
