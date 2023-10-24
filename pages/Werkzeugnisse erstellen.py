import streamlit as st
import datetime
import time
import json
import pandas as pd
import csv

st.markdown("# Werkzeugnis erstellen ✏️")
st.sidebar.markdown("# Werkzeugniserstellen ✏️")

# Funktion zum Ermitteln der höchsten bisher verwendeten Werkzeugnisnummer
def get_highest_werkzeugnis_num(data):
    if not data:
        return 0
    return max(int(entry["Werkzeugnisnummer"]) for entry in data)

# Datenbank-Datei für Werkzeugnisinformationen im JSON-Format
werkzeugnis_database_filename = "werkzeugnis_database.json"

# Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
def load_existing_data(filename):
    try:
        with open(filename, "r") as file:
            data = [json.loads(line) for line in file]
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []



# Funktion zum Speichern der Daten in einer CSV-Datei
def save_to_csv(data):
    filename = "bearbeitsungsstatus.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Schreibe die Kopfzeile
        csv_writer.writerow(["Kunde", "Auftragsnummer", "Bestelldatum Uhrzeit", "Aktuelle Dauer und Uhrzeit", "Zeitdifferenz", "current varianten", "selected quality"])
        for entry in data:
            kunde = entry["Kunde"]
            auftragsnummer = entry.get("Auftragsnummer", "N/A")
            bestelldatum_uhrzeit = entry["Bestelldatum"]
            aktuelle_dauer_uhrzeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            zeitdifferenz = timedifference(entry["Bestelldatum"])
            current_varianten = entry["Variante nach Bestellung"]
            selected_quality_montage = entry["Qualitätsprüfung"].get("Montage", "N/A")
            selected_quality_oberflaeche = entry["Qualitätsprüfung"].get("Oberfläche", "N/A")

            csv_writer.writerow([kunde, auftragsnummer, bestelldatum_uhrzeit, aktuelle_dauer_uhrzeit, zeitdifferenz, current_varianten, f"Montage: {selected_quality_montage}, Oberfläche: {selected_quality_oberflaeche}"])

# ...


existing_data = load_existing_data(werkzeugnis_database_filename)

# Seitentitel

# Automatisches Einfügen des ausgewählten Bestelldatums und der Uhrzeit
bestellungen_database_filename = "bestellungen_database.json"
bestellungen_data = load_existing_data(bestellungen_database_filename)
selected_datetime = st.selectbox("Bestellung:", bestellungen_data)
current_datetime = selected_datetime["Bestelldatum und Uhrzeit"] if bestellungen_data else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
current_Kunde = selected_datetime["Kunde"]
current_Sonderwunsch = selected_datetime["Sonderwunsch"]
current_Varianten = selected_datetime["Variante nach Bestellung"]
st.write(f"Bestellung vom: {current_datetime}")

# Kundenname
last_customer_name = existing_data[-1]["Kunde"] if existing_data else "Bitte Kundennamen eingeben"
kunde = st.text_input("Kunde", current_Kunde)

# Weitere Elemente
st.write("Varianten:")
st.write("Kundenvariante:", current_Varianten)
sonderwunsch = st.text_input("Sonderwunsch", current_Sonderwunsch)


# Qualitätsprüfung
st.write("Qualitätsprüfung:")
pruefungen = ["Montage", "Oberfläche"]
qualitaet = ["i.O", "ni.O"]
selected_quality = {}

for pruefung in pruefungen:
    st.write(pruefung)
    selected_q = st.radio(f"Auswahl {pruefung}", qualitaet)
    if selected_q:
        selected_quality[pruefung] = selected_q

# Hinzufügen der Funktion für die Zeitdifferenz
def timedifference(current_datetime):
    bestelldatum = datetime.datetime.strptime(current_datetime, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    time_difference = (now - bestelldatum).total_seconds()
    return int(time_difference)

# Schaltfläche, um das Werkzeugnis zu generieren
if st.button("Werkzeugnis wurde generiert und Bestellung zum Kunden verschickt"):
    # Speichern der Werkzeugnisinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    werkzeugnis_info = {
        "Bestelldatum": current_datetime,
        "Kunde": kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": current_Varianten,
        "Qualitätsprüfung": selected_quality,
    }
    existing_data.append(werkzeugnis_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(werkzeugnis_database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

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
    # Speichern der Daten in der CSV-Datei
    save_to_csv(existing_data
    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
