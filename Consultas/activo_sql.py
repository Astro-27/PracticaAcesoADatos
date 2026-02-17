from Datos.conexion import obtener_conexion
from Herramientas.gestor_log import registrar_info, registrar_error

def insertar_activo(activo):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        sql = '''INSERT INTO activos (codigo, tipo, marca, modelo, numero_serie, ubicacion, fecha_alta, estado)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        valores = (activo.codigo, activo.tipo, activo.marca, activo.modelo,
                   activo.numero_serie, activo.ubicacion, activo.fecha_alta, activo.estado)
        cursor.execute(sql, valores)
        conn.commit()
        # Registramos la acción en el log [cite: 65, 74]
        registrar_info(f"INSERT: Activo {activo.codigo} creado correctamente.")
    except Exception as e:
        # Registramos el error si algo falla [cite: 16, 88]
        registrar_error(f"ERROR al insertar activo {activo.codigo}: {str(e)}")
    finally:
        conn.close()


def listar_inventario(filtro="", limite=10, desplazamiento=0):
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Filtro combinado (Busca en código, marca, modelo o ubicación)
    sql = """SELECT * FROM activos 
             WHERE codigo LIKE ? OR marca LIKE ? OR modelo LIKE ? OR ubicacion LIKE ?
             ORDER BY id DESC LIMIT ? OFFSET ?"""

    termino = f"%{filtro}%"
    cursor.execute(sql, (termino, termino, termino, termino, limite, desplazamiento))
    filas = cursor.fetchall()
    conn.close()
    return filas