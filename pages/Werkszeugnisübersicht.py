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

def display_ampel_color(werkzeugnis_data):
    # Überprüfe, ob die Untereinträge "Montage" und "Oberfläche" in Ordnung sind
    is_ok = all(
        item["Qualitätsprüfung"]["Montage"] == "i.O" and
        item["Qualitätsprüfung"]["Oberfläche"] == "i.O"
        for item in werkzeugnis_data
    )
    
    if is_ok:
        ampel_color = "Grün"
    else:
        ampel_color = "Rot"
    
    return ampel_color

def display_werkzeugnis_results():
    # Laden der Werkzeugnisdaten aus der JSON-Datei
    werkzeugnis_data = []
    with open(database_filename, "r") as db:
        for line in db:
            werkzeugnis_info = json.loads(line)
            werkzeugnis_data.append(werkzeugnis_info)

    # Wenn Daten vorhanden sind, diese in einer Tabelle anzeigen
    if werkzeugnis_data:
        df = pd.DataFrame(werkzeugnis_data)
        df.set_index("Kunde", inplace=True)  # Setzen des Index auf "Kunde"
        st.dataframe(df, use_container_width=True)
        
        ampel_color = display_ampel_color(werkzeugnis_data)
        #st.write(f"Ampel: {ampel_color}")
        
        if ampel_color == "Grün":
            st.image("gruene_ampel.jpg")  # Hier musst du den Pfad zur grünen Ampelgrafik angeben
        else:
            st.image("rote_ampel.jpg")  # Hier musst du den Pfad zur roten Ampelgrafik angeben
    else:
        st.write("Keine Werkzeugnisdaten vorhanden.")

if __name__ == '__main__':
    display_werkzeugnis_results()
