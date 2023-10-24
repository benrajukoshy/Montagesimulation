import streamlit as st
import datetime
import json

st.markdown("# Bestellen 🛒")
st.sidebar.markdown("# Bestellen 🛒")

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
#st.title("Bestellung aufgeben")

# Kunde
kunde = st.text_input("Kundenname")

# Automatisches Einfügen des aktuellen Datums und der Uhrzeit
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.write(f"Bestellung vom: {current_datetime}")
# Auswahl der Bestellvarianten
st.write("Bestellvarianten:")

varianten_farben = {
    "LKW Führerhaus": ["Blau", "Rot", "Gelb"],
    "Container": ["Grün", "Gelb", "Blau"],
    "Sidepipes": ["Rot", "Blau"]
}

selected_variants = {}

# Erstelle 6 Spalten
columns = st.columns(6)

for variante, farben in varianten_farben.items():
    with columns[0]:
        st.write(variante)
    with columns[1]:
        selected_color = st.radio(f"Auswahl {variante}", farben)
        if selected_color:
            selected_variants[variante] = selected_color

# Sonderwunsch
sonderwunsch = st.text_input("Sonderwunsch", "")

# Kundentakt
Kundentakt = st.text_input("Kundentakt", "")


# Schaltfläche, um Bestellung abzuschicken
if st.button("Bestellung abschicken"):
    
    # Speichern der Bestellinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    bestellungen_info = {
        "Bestelldatum und Uhrzeit": current_datetime,
        "Kunde": kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": selected_variants,
        "Kundentakt": Kundentakt,        
    }
    existing_data.append(bestellungen_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    st.write("Die Bestellung wurde abgeschickt")
    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
