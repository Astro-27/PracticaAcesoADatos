from Datos.conexion import inicializar_tablas
from Objetos.activo import Activo
from Objetos.incidencia import Incidencia  # Corregido: Importación faltante
from Consultas.activo_sql import insertar_activo, listar_inventario
from Consultas.incidencia_sql import crear_incidencia, listar_incidencias # Corregido: Nombre de función unificado

def probar_sistema():
    # 1. Fase de inicialización de la base de datos
    print("--- Pasando fase de inicialización ---")
    inicializar_tablas()

    # 2. Creación de un activo de prueba
    print("\n--- Insertando activo de prueba ---")
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
    insertar_activo(nuevo_item)

    # 3. Consulta del inventario de activos
    print("\n--- Consultando el inventario actual ---")
    inventario = listar_inventario()
    for item in inventario:
        print(item)

    # 4. Creación de una incidencia asociada al activo ID 1
    print("\n--- Creando incidencia de prueba ---")
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

    # 5. Listado detallado de incidencias
    # Se utiliza listar_incidencias() que es el nombre definido en Consultas/incidencia_sql.py
    print("\n--- Listado de Incidencias ---")
    incidencias = listar_incidencias()
    for inc in incidencias:
        print(inc)

if __name__ == "__main__":
    probar_sistema()



if __name__ == "__main__":
    probar_sistema()