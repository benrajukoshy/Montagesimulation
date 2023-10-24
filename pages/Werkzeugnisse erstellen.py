import streamlit as st
import datetime
import json
import pandas as pd

st.markdown("# Werkzeugnis erstellen ✏️")
st.sidebar.markdown("# Werkzeugniserstellen ✏️")

# ...

# Schaltfläche, um das Werkzeugnis zu generieren
if st.button("Werkzeugnis wurde generiert und Bestellung zum Kunden verschickt"):
    # Berechne die Differenz zwischen dem aktuellen Datum/Uhrzeit und dem ausgewählten Bestelldatum
    bestelldatum = datetime.datetime.strptime(current_datetime, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    time_difference = (now - bestelldatum).total_seconds()

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

    st.write(f"Der Kundenauftrag wurde {int(time_difference)} Sekunden bearbeitet")

    # Erstellen eines DataFrames aus den Werkzeugnisdaten
    df = pd.DataFrame(existing_data)

    # Setzen des Index auf "Kunde"
    df.set_index("Kunde", inplace=True)

    # Anzeigen des DataFrames
    st.write("Alle Werkzeugnisse:")
    st.dataframe(df)

    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
