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

# ... (mantén tus otros imports y funciones)

def listar_incidencias(): # Cambiado de listar_incidencias_detalladas a listar_incidencias
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = '''
        SELECT i.id, i.activo_id, i.fecha_apertura, i.prioridad, i.categoria, 
               i.descripcion, i.estado, i.tecnico_asignado, a.codigo
        FROM incidencias i
        INNER JOIN activos a ON i.activo_id = a.id
    '''
    cursor.execute(sql)
    filas = cursor.fetchall()
    conn.close()
    return filas

def cambiar_estado_incidencia(id_incidencia, nuevo_estado):
    """Cambia el estado de una incidencia (Abierta/En Proceso/Resuelta).""" [cite: 44]
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE incidencias SET estado = ? WHERE id = ?", (nuevo_estado, id_incidencia))
        conn.commit()
        registrar_info(f"UPDATE: Incidencia {id_incidencia} cambió a {nuevo_estado}.") [cite: 65]
    except Exception as e:
        registrar_error(f"ERROR al cambiar estado: {str(e)}") [cite: 65]
    finally:
        conn.close()