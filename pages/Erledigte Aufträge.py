import streamlit as st
import pandas as pd
import altair as alt
import os

# Funktion zum Laden der Daten aus der CSV-Datei
def load_data():
    try:
        data = pd.read_csv("bearbeitsungsstatus.csv")
        return data
    except FileNotFoundError:
        return None

# Zeige die Daten als Tabelle
data = load_data()
if data is not None:
    st.write("Bearbeitungsstatus CSV-Datei")
    st.write(data)

# Füge einen Button hinzu, um die Daten zu löschen
if st.button("CSV-Daten löschen"):
    try:
        os.remove("bearbeitsungsstatus.csv")
        st.success("CSV-Daten wurden erfolgreich gelöscht.")
    except FileNotFoundError:
        st.warning("Die CSV-Datei existiert nicht.")

# Zeige einen Datei-Uploader, um die Datei erneut hochzuladen
uploaded_file = st.file_uploader("CSV-Datei erneut hochladen")
if uploaded_file is not None:
    with open("bearbeitsungsstatus.csv", "wb") as f:
        f.write(uploaded_file.read())
    st.success("CSV-Datei wurde erneut hochgeladen.")

# Lade die Daten erneut
data = load_data()

# Erstelle das anpassbare Balkendiagramm mit Altair
if data is not None:
    chart = alt.Chart(data, width=600, height=400).mark_bar().encode(
        x='Kunde:N',
        y='Zeitdifferenz:Q',
        color=alt.condition(
            alt.datum.Kundentakt <= alt.datum.Zeitdifferenz,
            alt.value('rot'), alt.value('green')
        )
    )
    st.altair_chart(chart, use_container_width=True)
