import streamlit as st
import json
import time
import pandas as pd

# Setze Streamlit-Option für die Spaltenbreite
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

st.markdown("# Bestellungen 🚀")
st.sidebar.markdown("# Bestellungen 🚀")

# Dateiname der Datenbank
database_filename = "bestellungen_database.json"

def display_results():
    # Laden der Werkzeugnisdaten aus der JSON-Datei
    bestellungen_data = []
    with open(database_filename, "r") as db:
        for line in db:
            bestellungen_info = json.loads(line)
            bestellungen_data.append(bestellungen_info)

    # Wenn Daten vorhanden sind, diese in einer Tabelle anzeigen
    if bestellungen_data:
        # Erstellen eines leeren DataFrames mit den erforderlichen Spalten
        
        df = pd.DataFrame(columns=["Bestelldatum und Uhrzeit:", "Kunde:", "Sonderwunsch:", "Führerhaus:", "Sidepipes:", "Container 1:", "Container 2:", "Container 3:", "Container 4:", "Kundentakt"])
        
        for idx, entry in enumerate(bestellungen_data, start=1):
            df.loc[idx] = [
                entry["Bestelldatum und Uhrzeit"],
                entry["Kunde"],
                entry["Sonderwunsch"],
                entry["Variante nach Bestellung"].get("Führerhaus", "N/A"),
                entry["Variante nach Bestellung"].get("Sidepipes", "N/A"),
                entry["Variante nach Bestellung"].get("Container 1", "N/A"),
                entry["Variante nach Bestellung"].get("Container 2", "N/A"),
                entry["Variante nach Bestellung"].get("Container 3", "N/A"),
                entry["Variante nach Bestellung"].get("Container 4", "N/A"),
                entry["Kundentakt"]
            ]
        
        st.dataframe(df.T, use_container_width= True)  # Transponieren des DataFrames und Anzeigen als Tabelle
        st.write("Dies ist der Kundentakt:", df["Kundentakt"].values[0])

        #bestellungen_database_filename = "bestellungen_database.json"
        #bestellungen_data = display_results(bestellungen_database_filename)
        df["Kundentakt"] = df["Kundentakt"].apply(int)
        
        st.write("Wenn für bestimmte Bestandteile keine Farbangaben gemacht wurden, dann können diese frei gewählt werden")
        # Countdown-Timer für Kundentakt
        timer_placeholder = st.empty()
        for i in range(df["Kundentakt"], -1, -1):
            timer_text = f"<strong><span style='font-size: 2em;'>Zeit bis zum Ausliefern (Kundentakt): {i} Sekunden</span></strong>"
            timer_placeholder.markdown(timer_text, unsafe_allow_html=True)
            time.sleep(1)

        # Timer abgeschlossen
        timer_placeholder.empty()
        
    else:
        st.write("Keine Bestellungen vorhanden.")

if __name__ == '__main__':
    display_results()
st.experimental_rerun()  # Seite neu laden
