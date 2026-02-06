import customtkinter as ctk # Libreria principal para creacion de GUI 
import modules as mod # Backend de la aplicacion
from PIL import Image # Libreria para detectar imagenes


# Ventana principal 
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("800x600")
app.title("TaskManager")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

#fuentes
font_texto = ctk.CTkFont(family="Roboto Condensed",size=16)
font_titulo = ctk.CTkFont(family="Roboto SemiCondensed",size=24)
#----------------------------------

# Menu de inicio, sin tareas guardadas

label_logo = ctk.CTkLabel(app,text="Task Manager",font=font_titulo)
label_logo.grid(row=0,column=0)

agregar_tarea = ctk.CTkButton(app, text="Agregar Tarea",font=font_texto,height=50,width=350)
agregar_tarea.grid(row=1, column=0,sticky="n")

if __name__ == "__main__": 
    app.mainloop()