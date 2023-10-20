import streamlit as st
import datetime
import json

# Funktion zum Ermitteln der höchsten bisher verwendeten Werkzeugnisnummer
def get_highest_werkzeugnis_num(data):
    if not data:
        return 0
    return max(int(entry["Werkzeugnisnummer"]) for entry in data)

# Datenbank-Datei für Werkzeugnisinformationen im JSON-Format
database_filename = "werkzeugnis_database.json"

# Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
def load_existing_data(filename):
    try:
        with open(filename, "r") as file:
            data = [json.loads(line) for line in file]
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

existing_data = load_existing_data(database_filename)

# Seitentitel
st.title("Werkzeugnis")

# Werkszeugnisnummer
highest_werkzeugnis_num = get_highest_werkzeugnis_num(existing_data)
werkzeugnis_nr = highest_werkzeugnis_num + 1
st.write(f"Werkszeugnis Nr.: {werkzeugnis_nr}")

# Kunde
# Versuche, den letzten Kundenname aus der Datenbank zu laden
last_customer_name = existing_data[-1]["Kunde"] if existing_data else "Bitte Kundennamen eingeben"
kunde = st.text_input("Kunde", last_customer_name)

# Automatisches Einfügen des aktuellen Datums und der Uhrzeit
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.write(f"Bestellung vom: {current_datetime}")

# Varianten nach Bestellung
st.write("Variante nach Bestellung:")
varianten = ["Führerhaus", "Sidepipes", "Container 1", "Container 2", "Container 3", "Container 4"]
selected_variants = {}

for variante in varianten:
    st.write(variante)
    farben = ["Rot", "Grün", "Gelb", "Blau"]
    selected_color = st.radio(f"Auswahl {variante}", farben)
    if selected_color:
        selected_variants[variante] = selected_color

# Sonderwunsch
sonderwunsch = st.text_input("Sonderwunsch", "")

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

# Schaltfläche, um das Werkzeugnis zu generieren
if st.button("Werkzeugnis generieren"):
    
    # Speichern der Werkzeugnisinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    werkzeugnis_info = {
        "Werkzeugnisnummer": werkzeugnis_nr,
        "Ihre Bestellung": current_datetime,
        "Kunde": kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": selected_variants,
        "Qualitätsprüfung": selected_quality,
    }
    existing_data.append(werkzeugnis_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    st.write("Das Werkzeugnis wurde generiert")
    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
