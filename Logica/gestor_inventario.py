from Consultas.activo_sql import insertar_activo
from Herramientas.validador import validar_codigo_activo, validar_campos_obligatorios


def alta_activo_segura(activo_objeto):
    """
    Intenta dar de alta un activo aplicando todas las validaciones previas. [cite: 31, 115]
    """
    # 1. Validar formato de código [cite: 20]
    if not validar_codigo_activo(activo_objeto.codigo):
        print("Error: El código debe ser ACT-XXXX (ej. ACT-0001)")
        return False

    # 2. Validar campos obligatorios [cite: 19]
    datos = {
        "codigo": activo_objeto.codigo,
        "tipo": activo_objeto.tipo,
        "marca": activo_objeto.marca,
        "estado": activo_objeto.estado
    }

    es_valido, campo_error = validar_campos_obligatorios(datos)
    if not es_valido:
        print(f"Error: El campo {campo_error} no puede estar vacío.")
        return False

    # 3. Si todo está ok, guardar en SQL
    insertar_activo(activo_objeto)
    return True