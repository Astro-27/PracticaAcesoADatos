import csv
# Importamos la clase Activo de tu carpeta Objetos
from Objetos.activo import Activo
# Importamos la función de inserción de tu carpeta Consultas
from Consultas.activo_sql import insertar_activo
# Importamos el gestor de logs de tu carpeta Herramientas
from Herramientas.gestor_log import registrar_info, registrar_error


def importar_activos_desde_csv(ruta_archivo):
    """
    Lee un archivo CSV y registra cada fila como un nuevo activo en la BD.
    El CSV debe tener cabeceras: Codigo, Tipo, Marca, Modelo, Serie, Ubicacion, Fecha, Estado
    """
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # Usamos DictReader para leer por el nombre de la columna
            lector = csv.DictReader(archivo, delimiter=';')
            contador = 0

            for fila in lector:
                # Creamos el objeto con los datos de la fila del CSV
                nuevo_activo = Activo(
                    codigo=fila['Codigo'],
                    tipo=fila['Tipo'],
                    marca=fila['Marca'],
                    modelo=fila['Modelo'],
                    numero_serie=fila['Serie'],
                    ubicacion=fila['Ubicacion'],
                    fecha_alta=fila['Fecha'],
                    estado=fila['Estado']
                )

                # Lo mandamos a la capa de Consultas para guardarlo en Datos/inventario.db
                insertar_activo(nuevo_activo)
                contador += 1

        registrar_info(f"IMPORTACIÓN: Se han cargado {contador} activos desde {ruta_archivo}")
        print(f"Éxito: {contador} activos importados correctamente.")
        return True

    except FileNotFoundError:
        registrar_error(f"ERROR IMPORTACIÓN: No se encontró el archivo {ruta_archivo}")
        return False
    except KeyError as e:
        registrar_error(f"ERROR IMPORTACIÓN: Falta la columna {str(e)} en el CSV")
        return False
    except Exception as e:
        registrar_error(f"ERROR CRÍTICO IMPORTACIÓN: {str(e)}")
        return False