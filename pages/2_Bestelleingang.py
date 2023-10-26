import streamlit as st
import json
import time
import pandas as pd

# Setze Streamlit-Option für die Spaltenbreite
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

st.markdown("# Aufträge 🚀")
st.sidebar.markdown("# Aufträge 🚀")

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
        
        df = pd.DataFrame(columns=["Bestelldatum und Uhrzeit:", "Kunde:", "Auftragsnummer", "Sonderwunsch:", "Führerhaus:", "Sidepipes:", "Container 1:", "Container 2:", "Container 3:", "Container 4:", "Kundentakt"])
        
        
        for idx, entry in enumerate(bestellungen_data, start=1):
            df.loc[idx] = [
                entry["Bestelldatum und Uhrzeit"],
                entry["Kunde"],
                entry["Auftragsnummer"],
                entry["Sonderwunsch"],
                generate_colored_text(entry["Variante nach Bestellung"].get('Führerhaus', 'N/A')),
                generate_colored_text(entry["Variante nach Bestellung"].get('Sidepipes', 'N/A')),
                generate_colored_text(entry["Variante nach Bestellung"].get('Container 1', 'N/A')),
                generate_colored_text(entry["Variante nach Bestellung"].get('Container 2', 'N/A')),
                generate_colored_text(entry["Variante nach Bestellung"].get('Container 3', 'N/A')),
                generate_colored_text(entry["Variante nach Bestellung"].get('Container 4', 'N/A')),
                entry["Kundentakt"]
            ]
        
        st.dataframe(df.T, use_container_width= True)  # Transponieren des DataFrames und Anzeigen als Tabelle
        

        #bestellungen_database_filename = "bestellungen_database.json"
        #bestellungen_data = display_results(bestellungen_database_filename)
        df["Kundentakt"] = df["Kundentakt"].apply(int)
        
        st.write("Wenn für bestimmte Bestandteile keine Farbangaben gemacht wurden, dann können diese frei gewählt werden")
        # Countdown-Timer für Kundentakt
        timer_placeholder = st.empty()
        for i in range(df["Kundentakt"].values[0], -1, -1):
            timer_text = f"<strong><span style='font-size: 2em;'>Zeit bis zum Ausliefern (Kundentakt): {i} Sekunden</span></strong>"
            timer_placeholder.markdown(timer_text, unsafe_allow_html=True)
            time.sleep(1)

        # Timer abgeschlossen
        timer_placeholder.empty()
        
    else:
        st.write("Keine Bestellungen vorhanden.")
        
def generate_colored_text(text):
    # Ersetzen Sie 'Blau', 'Rot', 'Grün', usw. durch entsprechende Farbcodes
    color_map = {
        'Blau': 'blue',
        'Rot': 'red',
        'Grün': 'green',
        # Fügen Sie weitere Farben hinzu, falls erforderlich
    }
    for color, color_code in color_map.items():
        text = text.replace(color, f"<span style='color: {color_code}'>{color}</span>")
    return text
        

if __name__ == '__main__':
    display_results()
st.experimental_rerun()  # Seite neu laden
