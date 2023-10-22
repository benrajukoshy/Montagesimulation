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
    if bestellungen_data:
        for idx, entry in enumerate(bestellungen_data):
            st.write(f"**Bestellung {idx + 1}**")
            with st.empty():
                st.write("Bestelldatum und Uhrzeit:", entry["Bestelldatum und Uhrzeit"])
                st.write("Kunde:", entry["Kunde"])
                st.write("Sonderwunsch:", entry["Sonderwunsch"])
                st.write("Variante nach Bestellung:")
                for kategorie, farbe in entry["Variante nach Bestellung"].items():
                    st.write(f"{kategorie}: {farbe}")
            st.write("")  # Neue Zeile für die nächste Bestellung

        # Countdown-Timer
        timer_placeholder = st.empty()
        for i in range(10, -1, -1): #time zeit
            timer_text = f"<strong><span style='font-size: 2em;'>Kundentakt: {i} Sekunden</span></strong>"
            timer_placeholder.markdown(timer_text, unsafe_allow_html=True)
            time.sleep(0.8) # Sleep time to reduce for loop speed
        # Timer abgeschlossen
            timer_placeholder.empty()
        st.write("Countdown-Timer abgelaufen.")
        st.image("https://t3.ftcdn.net/jpg/05/15/14/12/360_F_515141235_MoCb2kgQ3hwrPEjTIWTKkK6TgjDeekI5.jpg", width=300)
        time.sleep(1)
        
    else:
        st.write("Keine Bestellungen vorhanden.")

if __name__ == '__main__':
    display_results()
st.experimental_rerun()  # Seite neu laden