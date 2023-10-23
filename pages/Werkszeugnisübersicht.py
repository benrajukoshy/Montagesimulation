import streamlit as st
import json
import pandas as pd

# Setze Streamlit-Option für die Spaltenbreite
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# Dateiname der Datenbank
database_filename = "werkzeugnis_database.json"

def display_werkzeugnis_results():
    # Laden der Werkzeugnisdaten aus der JSON-Datei
    werkzeugnis_data = []
    with open(database_filename, "r") as db:
        for line in db:
            werkzeugnis_info = json.loads(line)
            werkzeugnis_data.append(werkzeugnis_info)

    # Wenn Daten vorhanden sind, diese in einer Tabelle anzeigen
    if werkzeugnis_data:
        # Erstellen eines leeren DataFrames mit den erforderlichen Spalten
        df = pd.DataFrame(columns=["Bestelldatum:", "Kunde:"], index=[1])  # Nur 2 Spalten
        idx = 1  # Startindex

        for entry in werkzeugnis_data:
            # Nur "Bestelldatum und Uhrzeit" aus dem JSON-Format extrahieren
            bestelldatum_uhrzeit = entry["Bestelldatum und Uhrzeit"]
            df.loc[idx] = [
                bestelldatum_uhrzeit,
                entry["Kunde"]
            ]
            idx += 1  # Inkrementiere den Index für jede Zeile

        st.dataframe(df.T, use_container_width=True)  # Transponieren des DataFrames und Anzeigen als Tabelle

    else:
        st.write("Keine Werkzeugnisdaten vorhanden.")

if __name__ == '__main__':
    display_werkzeugnis_results()
