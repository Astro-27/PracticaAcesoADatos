from Datos.conexion import inicializar_tablas
from Objetos.activo import Activo
from Consultas.activo_sql import insertar_activo, listar_inventario

def probar_sistema():
    # 1. Creamos la base de datos y las tablas si no existen
    print("--- Pasando fase de inicialización ---")
    inicializar_tablas()

    # 2. Creamos un objeto Activo de prueba (cumpliendo campos obligatorios)
    # [cite: 19, 20, 21, 22, 23, 24, 25, 26, 29]
    nuevo_item = Activo(
        codigo="ACT-0001",
        tipo="Portátil",
        marca="Dell",
        modelo="Latitude 5420",
        numero_serie="SN-987654321",
        ubicacion="Aula 102",
        fecha_alta="2024-05-20",
        estado="Operativo"
    )

    # 3. Intentamos guardarlo en el inventario (SQLite)
    print("\n--- Insertando activo de prueba ---")
    insertar_activo(nuevo_item)

    # 4. Listamos el inventario para confirmar
    print("\n--- Consultando el inventario actual ---")
    inventario = listar_inventario()
    for item in inventario:
        print(item)

from Consultas.incidencia_sql import crear_incidencia, listar_incidencias
for inc in listar_incidencias():
    print(inc)

# ... después de insertar el activo de la prueba anterior ...

# Creamos una incidencia para el activo con ID 1
nueva_averia = Incidencia(
    activo_id=1,
    fecha_apertura="2024-05-21",
    prioridad="Alta",
    categoria="Hardware",
    descripcion="La pantalla no enciende",
    estado="Abierta",
    tecnico_asignado="Ramón García"
)

crear_incidencia(nueva_averia)

print("\n--- Listado de Incidencias ---")
for inc in listar_incidencias_detalladas():
    print(inc)




if __name__ == "__main__":
    probar_sistema()