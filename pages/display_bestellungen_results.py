import streamlit as st
import json
import time

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
        for idx, entry in enumerate(bestellungen_data):
            st.write(f"**Bestellung {idx + 1}**")
            with st.beta_container():
                st.write("Bestelldatum und Uhrzeit:", entry["Bestelldatum und Uhrzeit"])
                st.write("Kunde:", entry["Kunde"])
                st.write("Sonderwunsch:", entry["Sonderwunsch"])
                st.write("Variante nach Bestellung:")
                for kategorie, farbe in entry["Variante nach Bestellung"].items():
                    st.write(f"{kategorie}: {farbe}")
            st.write("")  # Neue Zeile für die nächste Bestellung

        # Countdown-Timer
        timer_placeholder = st.empty()
        for i in range(10, -1, -1):
            timer_text = f"<strong><span style='font-size: 2em;'>Timer: {i} Sekunden</span></strong>"
            timer_placeholder.markdown(timer_text, unsafe_allow_html=True)
            time.sleep(1)

        # Timer abgeschlossen
        timer_placeholder.empty()
        st.write("Countdown-Timer abgelaufen.")
        st.experimental_rerun()  # Seite neu laden
    else:
        st.write("Keine Bestellungen vorhanden.")

if __name__ == '__main__':
    display_results()
