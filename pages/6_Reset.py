import streamlit as st
import os

# Definieren der Dateinamen
file_names = ['bearbeitsungsstatus.csv', 'bestellungen_database.json', 'werkzeugnis_database.json']

# Streamlit-Anwendung
st.title('Inhalt von Dateien löschen')

# Funktion zum Löschen des Inhalts der Datei
def delete_file_content(file_name):
    try:
        with open(file_name, 'w') as file:
            file.truncate(0)  # Löscht den Inhalt der Datei
        st.success(f'Inhalt von {file_name} wurde erfolgreich gelöscht.')
    except Exception as e:
        st.error(f'Fehler beim Löschen des Inhalts von {file_name}: {str(e)}')

# Dropdown-Menü zur Auswahl der Datei
selected_file = st.selectbox('Wählen Sie die Datei aus, deren Inhalt gelöscht werden soll:', file_names)

# Löschen-Button
if st.button('Inhalt der Datei löschen'):
    delete_file_content(selected_file)
