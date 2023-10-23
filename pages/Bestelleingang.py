import streamlit as st
import json
import time
import numpy as np
st.markdown("# Bestellungen 🚀")
st.sidebar.markdown("# Bestellungen 🚀")

# Dateiname der Datenbank
database_filename = "bestellungen_database.json"

def display_results():
    #st.title("Bestellungen")

    # Laden der Werkzeugnisdaten aus der JSON-Datei
    bestellungen_data = []
    with open(database_filename, "r") as db:
        for line in db:
            bestellungen_info = json.loads(line)
            bestellungen_data.append(bestellungen_info)

    # Wenn Daten vorhanden sind, diese in einer Tabelle anzeigen
    #if bestellungen_data:
    #    for idx, entry in enumerate(bestellungen_data):
    #        st.write(f"**Bestellung {idx + 1}**")
    #        with st.container():
    #            st.write("Bestelldatum und Uhrzeit:", entry["Bestelldatum und Uhrzeit"])
    #            st.write("Kunde:", entry["Kunde"])
    #            st.write("Sonderwunsch:", entry["Sonderwunsch"])
    #            st.write("Variante nach Bestellung:")
    #            for kategorie, farbe in entry["Variante nach Bestellung"].items():
    #                st.write(f"{kategorie}: {farbe}")
    #        st.write("")  # Neue Zeile für die nächste Bestellung
    # Erstellen eines leeren DataFrames mit den erforderlichen Spalten
    df = pd.DataFrame(columns=["Bestelldatum und Uhrzeit", "Kunde", "Sonderwunsch", "Führerhaus", "Sidepipes", "Container 1", "Container 2", "Container 3", "Container 4"])

        for idx, entry in enumerate(bestellungen_data):
            df.loc[idx] = [
                entry["Bestelldatum und Uhrzeit"],
                entry["Kunde"],
                entry["Sonderwunsch"],
                entry["Variante nach Bestellung"].get("Führerhaus", "N/A"),
                entry["Variante nach Bestellung"].get("Sidepipes", "N/A"),
                entry["Variante nach Bestellung"].get("Container 1", "N/A"),
                entry["Variante nach Bestellung"].get("Container 2", "N/A"),
                entry["Variante nach Bestellung"].get("Container 3", "N/A"),
                entry["Variante nach Bestellung"].get("Container 4", "N/A") ]

        st.dataframe(df.T)  # Transponieren des DataFrames und Anzeigen als Tabelle
        # Countdown-Timer
        timer_placeholder = st.empty()
        for i in range(10, -1, -1): #time zeit
            timer_text = f"<strong><span style='font-size: 2em;'>Zeit bis zum Ausliefern (Kundentakt): {i} Sekunden</span></strong>"
            timer_placeholder.markdown(timer_text, unsafe_allow_html=True)
            time.sleep(0.8) # Sleep time to reduce for loop speed
        # Timer abgeschlossen
            timer_placeholder.empty()
        #st.write("<strong><span style='font-size: 2em;'>Sie müssen jetzt ausliefern!</span></strong>")
        #time.sleep(1)
        
    else:
        st.write("Keine Bestellungen vorhanden.")

if __name__ == '__main__':
    display_results()
st.experimental_rerun()  # Seite neu laden