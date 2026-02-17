import json
import os

def cargar_config():
    ruta = "config.json" # Asegúrate de renombrar config.json a config.json
    if not os.path.exists(ruta):
        return {"base_datos": "Datos/inventario.db", "nivel_log": "INFO"}
    with open(ruta, 'r') as f:
        return json.load(f)