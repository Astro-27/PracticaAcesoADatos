import logging
import os

# Configuramos el log
import logging
from Herramientas.configuracion import cargar_config

def configurar_log():
    config = cargar_config()
    # Mapeo simple para convertir texto a nivel de logging
    niveles = {"INFO": logging.INFO, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}
    nivel = niveles.get(config.get("nivel_log", "INFO"), logging.INFO)

    logging.basicConfig(
        filename='app.log',
        level=nivel,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def registrar_info(mensaje):
    configurar_log()
    logging.info(mensaje)

def registrar_error(mensaje):
    configurar_log()
    logging.error(mensaje)