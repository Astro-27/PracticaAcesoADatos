from Datos.conexion import obtener_conexion
from Herramientas.gestor_log import registrar_info, registrar_error

def crear_incidencia(incidencia):
    """Registra una nueva incidencia asociada a un activo."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        sql = '''INSERT INTO incidencias (activo_id, fecha_apertura, prioridad, categoria, descripcion, estado, tecnico_asignado)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        valores = (incidencia.activo_id, incidencia.fecha_apertura, incidencia.prioridad,
                   incidencia.categoria, incidencia.descripcion, incidencia.estado, incidencia.tecnico_asignado)
        cursor.execute(sql, valores)
        conn.commit()
        registrar_info(f"INSERT: Incidencia creada para el activo ID {incidencia.activo_id}.")
    except Exception as e:
        registrar_error(f"ERROR al crear incidencia: {str(e)}")
    finally:
        conn.close()

def listar_incidencias_detalladas():
    """Lista las incidencias mostrando el código del activo relacionado."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    # Usamos INNER JOIN para juntar las dos tablas
    sql = '''
        SELECT i.id, a.codigo, i.fecha_apertura, i.prioridad, i.estado, i.tecnico_asignado
        FROM incidencias i
        INNER JOIN activos a ON i.activo_id = a.id
    '''
    cursor.execute(sql)
    filas = cursor.fetchall()
    conn.close()
    return filas