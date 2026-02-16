import sqlite3
import os


def obtener_conexion():
    """Establece conexión con la base de datos y activa claves foráneas."""
    # Creamos la carpeta si no existe para evitar errores
    if not os.path.exists('Datos'):
        os.makedirs('Datos')

    # Conexión al archivo SQLite
    conn = sqlite3.connect('Datos/inventario.db')

    # Requisito técnico: Activar claves foráneas
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn





def inicializar_tablas():
    """Crea las tablas necesarias si no existen al iniciar la app."""
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Tabla de Activos con campos obligatorios [cite: 19, 20, 21, 22, 23, 24, 25, 26, 29]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL, -- Formato ACT-XXXX
            tipo TEXT NOT NULL,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            numero_serie TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            fecha_alta TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')

    # Tabla de Incidencias relacionada con Activos [cite: 34, 35, 36, 37, 38, 39, 40, 41]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activo_id INTEGER NOT NULL,
            fecha_apertura TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT NOT NULL,
            tecnico_asignado TEXT NOT NULL,
            FOREIGN KEY (activo_id) REFERENCES activos(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()
    print("Base de datos e inicialización de tablas completada.")


if __name__ == "__main__":
    inicializar_tablas()