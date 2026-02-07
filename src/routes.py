import os

DB_FILE = "tasks.json"

DIR_SRC = os.path.dirname(os.path.abspath(__file__)) # Ruta del directorio src

DIR_PROJECT = os.path.dirname(DIR_SRC) # Ruta del directorio raiz 

DIR_JSON = os.path.join(DIR_PROJECT, "data", DB_FILE) # Ruta del json

DIR_ICONS = os.path.join(DIR_PROJECT, "icons") # Ruta de directorio icons

ROBOTO_REGULAR = os.path.join(DIR_PROJECT, "fonts","roboto_regular.ttf") # ruta para roboto regular

ROBOTO_BOLD = os.path.join(DIR_PROJECT, "fonts","roboto_bold.ttf") # ruta para roboto bold