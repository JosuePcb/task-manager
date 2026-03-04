# Task Manager with Python & CustomTkinter

I made that for fun kekw and to learn how to make GUI using CustomTkinter and data persistence using LocalStorage and Json with python. Never touching this code again (i think)

## 📁 Project structure

```text
src/
├── gui.py          # Frontend
├── modules.py      # Backend
├── routes.py       # Endpoints
├── data/           # Database
├── fonts/          # Fonts
└── icons/          # Icons (i didnt use it kekw)
```
🛠️ Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto localmente:

    Clona el repositorio:
    Bash

    git clone https://github.com/JosuePcb/task-manager.git
    cd task-manager

    Crea el entorno virtual e instala las dependencias con uv:
    Bash

    uv venv
    # Activa el entorno (Windows)
    .venv\Scripts\activate
    # Activa el entorno (macOS/Linux)
    source .venv/bin/activate

    uv sync

    Nota: uv sync leerá el archivo pyproject.toml o requirements.txt e instalará customtkinter y demás dependencias automáticamente.

💻 Uso

Para ejecutar la aplicación, utiliza el siguiente comando:
Bash

uv run src/gui.py
