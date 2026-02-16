import re
from Herramientas.gestor_log import registrar_error

def validar_codigo_activo(codigo):
    """
    Valida que el código cumpla el formato ACT- seguido de 4 números. [cite: 20]
    Ejemplo: ACT-0001
    """
    patron = r'^ACT-\d{4}$'
    if re.match(patron, codigo):
        return True
    else:
        registrar_error(f"VALIDACIÓN FALLIDA: El código {codigo} no tiene formato ACT-XXXX") [cite: 65, 120]
        return False

def validar_campos_obligatorios(datos_dict):
    """
    Comprueba que no haya campos vacíos en el formulario. [cite: 19, 34, 116]
    """
    for campo, valor in datos_dict.items():
        if not valor or str(valor).strip() == "":
            registrar_error(f"VALIDACIÓN FALLIDA: El campo {campo} es obligatorio.") [cite: 65]
            return False, campo
    return True, None