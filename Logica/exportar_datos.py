import csv
import json
import os
# Importamos desde tus carpetas reales
from Consultas.activo_sql import listar_inventario
from Consultas.incidencia_sql import listar_incidencias
from Herramientas.gestor_log import registrar_info, registrar_error


def exportar_activos_csv():
    """Genera un archivo CSV con todos los activos del inventario."""
    # Creamos una carpeta 'Exportaciones' si no existe para no llenar la raíz
    if not os.path.exists('Exportaciones'):
        os.makedirs('Exportaciones')

    ruta = "Exportaciones/activos_inventario.csv"

    try:
        # Obtenemos los datos de la capa de Consultas
        datos = listar_inventario()
        cabeceras = ["ID", "Código", "Tipo", "Marca", "Modelo", "Nº Serie", "Ubicación", "Fecha Alta", "Estado"]

        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo, delimiter=';')  # Usamos punto y coma para Excel
            escritor.writerow(cabeceras)
            escritor.writerows(datos)

        registrar_info(f"EXPORTACIÓN: Inventario exportado correctamente a {ruta}")
        print(f"Éxito: Archivo guardado en {ruta}")
        return True
    except Exception as e:
        registrar_error(f"ERROR EXPORTACIÓN CSV: {str(e)}")
        return False


def exportar_incidencias_json():
    """Genera un archivo JSON con el historial de incidencias."""
    if not os.path.exists('Exportaciones'):
        os.makedirs('Exportaciones')

    ruta = "Exportaciones/reporte_incidencias.json"

    try:
        datos = listar_incidencias()
        # Convertimos la lista de tuplas de SQL a diccionarios para que el JSON sea legible
        lista_final = []
        for d in datos:
            lista_final.append({
                "id_incidencia": d[0],
                "activo_id": d[1],
                "codigo_activo": d[8],  # El JOIN que hicimos antes
                "fecha": d[2],
                "prioridad": d[3],
                "categoria": d[4],
                "descripcion": d[5],
                "estado": d[6],
                "tecnico": d[7]
            })

        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(lista_final, archivo, indent=4, ensure_ascii=False)

        registrar_info(f"EXPORTACIÓN: Incidencias exportadas correctamente a {ruta}")
        print(f"Éxito: Archivo guardado en {ruta}")
        return True
    except Exception as e:
        registrar_error(f"ERROR EXPORTACIÓN JSON: {str(e)}")
        return False