import streamlit as st
import json
import pandas as pd

# Setze Streamlit-Option für die Spaltenbreite
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Werkzeugnisübersicht ⭐")
st.sidebar.markdown("# Werkzeugnisübersicht ⭐")

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
        
        df = pd.DataFrame(columns=["Bestelldatum:", "Kunde:", "Sonderwunsch:", "Führerhaus:", "Sidepipes:", "Container 1:", "Container 2:", "Container 3:", "Container 4:"])
        
        for idx, entry in enumerate(werkzeugnis_data, start=1):
            df.loc[idx] = [
                entry["Bestelldatum"],
                entry["Kunde"],                
                entry["Variante nach Bestellung"].get("Qualitätsprüfung", "N/A")]
        
        st.dataframe(df.T, use_container_width= True)  # Transponieren des DataFrames und Anzeigen als Tabelle
        
    else:
        st.write("Keine Werkzeugnisdaten vorhanden.")

if __name__ == '__main__':
    display_werkzeugnis_results()
