import logging
from logging.handlers import RotatingFileHandler
from Herramientas.configuracion import cargar_config


def configurar_log():
    config = cargar_config()
    nivel_str = config.get("nivel_log", "INFO").upper()
    nivel = getattr(logging, nivel_str, logging.INFO)

    logger = logging.getLogger("app")
    logger.setLevel(nivel)

    # Si ya tiene manejadores, no añadimos más (evita duplicados)
    if not logger.handlers:
        # Crea archivos de max 500KB y guarda 2 copias de seguridad
        handler = RotatingFileHandler("app.log", maxBytes=500000, backupCount=2, encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    return logger


def registrar_info(mensaje):
    configurar_log().info(mensaje)


def registrar_error(mensaje):
    configurar_log().error(mensaje)