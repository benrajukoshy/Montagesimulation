import streamlit as st
import json
import pandas as pd

# Dateiname der Datenbank
database_filename = "bestellungen_database.json"

def display_results():
    st.title("Bestellungen")

    # Laden der Werkzeugnisdaten aus der JSON-Datei
    bestellungen_data = []
    with open(database_filename, "r") as db:
        for line in db:
            bestellungen_info = json.loads(line)
            bestellungen_data.append(bestellungen_info)

    # Wenn Daten vorhanden sind, diese in einer Tabelle anzeigen
    if bestellungen_data:
        st.write("Bestellungen:")
        df = pd.DataFrame(bestellungen_data)
        st.dataframe(df)
    else:
        st.write("Keine Bestellungen vorhanden.")

    if __name__ == '__main__':
        display_results()
