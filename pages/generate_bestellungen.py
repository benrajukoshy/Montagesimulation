import streamlit as st
import datetime
import json

# Datenbank-Datei für Werkzeugnisinformationen im JSON-Format
database_filename = "bestellungen_database.json"

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
st.title("Bestellung aufgeben")

# Kunde


# Automatisches Einfügen des aktuellen Datums und der Uhrzeit
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.write(f"Bestellung vom: {current_datetime}")

# Auswahl der Bestellvariante
st.write("Bestellvariante:")
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




# Schaltfläche, um Bestellung abzuschicken
if st.button("Bestellung abschicken"):
    
    # Speichern der Bestellinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    werkzeugnis_info = {
        "Bestelldatum und Uhrzeit": current_datetime,
        "Kunde": kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": selected_variants,        
    }
    existing_data.append(werkzeugnis_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    st.write("Die Bestellung wurde abgeschickt")
    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
