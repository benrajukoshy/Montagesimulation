import streamlit as st
import datetime
import json
import pandas as pd
import csv

st.markdown("# Auftrag abschließen ✏️")
st.sidebar.markdown("# Auftrag abschließen ✏️")
st.write("Qualitätskontrolle und Versandt")

# Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
def load_existing_data(filename):
    try:
        with open(filename, "r") as file:
            data = [json.loads(line) for line in file]
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Funktion zum Laden und Anzeigen der Daten aus der CSV-Datei
def load_and_display_data(filename):
    try:
        df = pd.read_csv(filename)
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Die CSV-Datei existiert noch nicht.")

# ...

werkzeugnis_database_filename = "werkzeugnis_database.json"
existing_data = load_existing_data(werkzeugnis_database_filename)

# ...

# Schaltfläche, um das Werkzeugnis zu generieren
if st.button("Auftrag abgeschlossen und Bestellung zum Kunden verschickt"):
    werkzeugnis_info = {
        "Bestelldatum": current_datetime,
        "Kunde": current_Kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": current_Varianten,
        "Qualitätsprüfung": selected_quality,
        "Kundentakt": current_Kundentakt
    }

    existing_data.append(werkzeugnis_info)

    with open(werkzeugnis_database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    time_diff = timedifference(current_datetime)
    st.write(f"Der Kundenauftrag wurde in {time_diff} Sekunden bearbeitet")
    time.sleep(1)

    # Erstellen eines DataFrames aus den Werkzeugnisdaten
    df = pd.DataFrame(existing_data)

    # Setzen des Index auf "Kunde"
    df.set_index("Kunde", inplace=True)

    # Anzeigen des DataFrames
    st.write("Alle Werkzeugnisse:")
    st.dataframe(df)

    # Speichern der Daten in der CSV-Datei
    if len(existing_data) > 0:
        last_entry = existing_data[-1]  # Die letzte hinzugefügte Zeile
        save_to_csv([last_entry])  # Speichern Sie nur die letzte Zeile in der CSV-Datei

    st.experimental_rerun()
