import streamlit as st
import os

# Definieren der Dateinamen
file_names = ['bearbeitsungsstatus.csv', 'bestellungen_database.json', 'werkzeugnis_database.json']

# Streamlit-Anwendung
st.title('Dateien löschen')

# Funktion zum Löschen der Datei
def delete_file(file_name):
    try:
        os.remove(file_name)
        st.success(f'Datei {file_name} wurde erfolgreich gelöscht.')
    except Exception as e:
        st.error(f'Fehler beim Löschen der Datei {file_name}: {str(e)}')

# Dropdown-Menü zur Auswahl der Datei
selected_file = st.selectbox('Wählen Sie die zu löschende Datei aus:', file_names)

# Löschen-Button
if st.button('Datei löschen'):
    delete_file(selected_file)
