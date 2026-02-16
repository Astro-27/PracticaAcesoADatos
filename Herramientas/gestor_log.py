import logging
import os

# Configuramos el log
def configurar_log():
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def registrar_info(mensaje):
    configurar_log()
    logging.info(mensaje)

def registrar_error(mensaje):
    configurar_log()
    logging.error(mensaje)