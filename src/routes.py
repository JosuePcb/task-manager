import os

data = "tasks.json"

dir_src = os.path.dirname(os.path.abspath(__file__)) # Ruta del directorio src

dir_proyecto = os.path.dirname(dir_src) # Ruta del directorio raiz 

dir_json = os.path.join(dir_proyecto, "data", data) # Ruta del json

dir_icons = os.path.join(dir_proyecto, "icons") # Ruta de directorio icons

roboto_regular = os.path.join(dir_proyecto, "fonts","roboto_regular.ttf") # ruta para roboto regular

roboto_bold = os.path.join(dir_proyecto, "fonts","roboto_bold.ttf") # ruta para roboto bold