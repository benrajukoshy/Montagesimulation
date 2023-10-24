import streamlit as st
import datetime
import json
import pandas as pd

# ...

# Verwende st.camera_input, um Bilder von der Webcam aufzunehmen
webcam_image = st.camera_input("Webcam")
if webcam_image is not None:
    # Speichere das aufgenommene Bild als Datei mit einem eindeutigen Dateinamen
    image_filename = f"webcam_image_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    with open(image_filename, "wb") as image_file:
        image_file.write(webcam_image.read())

# ...

# Schaltfläche, um das Werkzeugnis zu generieren und Bilder aufzunehmen
if st.button("Werkzeugnis wurde generiert und Bestellung zum Kunden verschickt"):
    # Speichern der Werkzeugnisinformationen in der Datenbank als separates JSON-Objekt pro Zeile
    werkzeugnis_info = {
        "Bestelldatum": current_datetime,
        "Kunde": kunde,
        "Sonderwunsch": sonderwunsch,
        "Variante nach Bestellung": current_Varianten,
        "Qualitätsprüfung": selected_quality,
        "Webcam_Bild": image_filename  # Füge den Dateinamen des Webcam-Bilds hinzu
    }
    existing_data.append(werkzeugnis_info)  # Hinzufügen der neuen Daten zu den vorhandenen Daten

    with open(werkzeugnis_database_filename, "w") as db:
        for entry in existing_data:
            db.write(json.dumps(entry) + "\n")

    st.write("Das Werkzeugnis wurde generiert")

    # Erstellen eines DataFrames aus den Werkzeugnisdaten
    df = pd.DataFrame(existing_data)

    # Setzen des Index auf "Kunde"
    df.set_index("Kunde", inplace=True)

    # Anzeigen des DataFrames
    st.write("Alle Werkzeugnisse:")
    st.dataframe(df)

    # Laden der bestehenden Werkzeugnisdaten aus der JSON-Datei
    st.experimental_rerun()
