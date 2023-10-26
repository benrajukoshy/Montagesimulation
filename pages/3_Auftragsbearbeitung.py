import streamlit as st
import datetime
import time
import json
import pandas as pd
import os

st.markdown("# Auftrag abschließen ✏️")
st.sidebar.markdown("# Auftrag abschließen ✏️")
st.write("Qualitätskontrolle und Versandt")

werkzeugnis_database_filename = "werkzeugnis_database.json"

# Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
def load_existing_data(filename):
    try:
        with open(filename, "r") as file:
            data = [json.loads(line) for line in file]
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ...

existing_data = load_existing_data(werkzeugnis_database_filename)

# ...

def timedifference(current_datetime):
    bestelldatum = datetime.datetime.strptime(current_datetime, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    time_difference = (now - bestelldatum).total_seconds()
    return int(time_difference)

# Neue Funktion zum Speichern der Zeitdifferenz und der aktuellen Uhrzeit im JSON-Datei
def save_to_json(data):
    filename = "zeitdifferenz.json"
    zeitdifferenz_data = load_existing_data(filename)
    
    # Berechne die Zeitdifferenz
    bestelldatum = datetime.datetime.strptime(data["Bestelldatum"], "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    time_difference = (now - bestelldatum).total_seconds()
    data["Aktuelle Dauer und Uhrzeit"] = now.strftime("%Y-%m-%d %H:%M:%S")
    data["Zeitdifferenz"] = int(time_difference)
    
    zeitdifferenz_data.append(data)
    
    with open(filename, "w") as json_file:
        json.dump(zeitdifferenz_data, json_file)

# Schaltfläche, um das Werkzeugnis zu generieren
if st.button("Auftrag abgeschlossen und Bestellung zum Kunden verschickt"):
    # Speichern der Werkzeugnisinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    werkzeugnis_info = {
        "Bestelldatum": current_datetime,
        "Kunde": current_Kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": current_Varianten,
        "Qualitätsprüfung": selected_quality,
        "Kundentakt": current_Kundentakt
    }
    existing_data.append(werkzeugnis_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(werkzeugnis_database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    # Neue Funktion aufrufen, um Zeitdifferenz und aktuelle Uhrzeit zu speichern
    save_to_json(werkzeugnis_info)

    time_diff = timedifference(current_datetime)  # Berechnen der Zeitdifferenz
    st.write(f"Der Kundenauftrag wurde in {time_diff} Sekunden bearbeitet")
    time.sleep(1)
    # Erstellen eines DataFrames aus den Werkzeugnisdaten
    df = pd.DataFrame(existing_data)

    # Setzen des Index auf "Kunde"
    df.set_index("Kunde", inplace=True)

    # Anzeigen des DataFrames
    st.write("Alle Werkzeugnisse:")
    st.dataframe(df)
    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
