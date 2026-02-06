import json
import os
from datetime import datetime
import routes
import pyglet

# Fuentes utilizadas
pyglet.font.add_file(routes.roboto_regular)
pyglet.font.add_file(routes.roboto_bold)

# Funcion simple para validar el formato de fecha introducido
def fecha_verificada():
    while True:
        try:
            fecha = str(input("ingrese fecha en este formato dd/mm/YYYY"))
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("mal formato")
        

# Funcion simple para validar que los datos ingresados no sean solo numericos
def validar_string(mensaje=str) -> str:
    while True:
        cadena = input(mensaje)
        if cadena.isdigit():
            print("No puede ingresar solo numeros")
            continue
        else:
            return cadena

# Funcion para el create del crud

def guardar_tarea():
    lista_tareas=[]
    dir_json = os.path.join(routes.dir_proyecto, "data", routes.data)
    try:
        with open(dir_json, 'r') as info:
            lista_tareas = json.load(info)
    except FileNotFoundError:
        with open(dir_json, 'w') as f:
            f.write("[]")
    
    
    titulo = validar_string("Titulo: ")
    descripcion = validar_string("Descripcion: ")
    while True:
        prioridad = str(input("Elija una prioridad, Alta, Media, Baja")).lower()
        if prioridad == "alta" or prioridad == "media" or prioridad == "baja":
            break
        else:
            continue
    fecha = fecha_verificada()
    
    lista_tareas.append({"titulo":titulo, "descripcion":descripcion, "prioridad":prioridad, "fecha":fecha})
    with open(dir_json, 'w') as tarea:
        json.dump(lista_tareas, tarea, indent=4)
    
    
    
if __name__ == "__main__": 
    guardar_tarea()