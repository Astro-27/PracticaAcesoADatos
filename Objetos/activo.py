class Activo:
    def __init__(self, codigo, tipo, marca, modelo, numero_serie, ubicacion, fecha_alta, estado, id=None):
        self.id = id  # El ID lo pone la base de datos automáticamente
        self.codigo = codigo  # Ejemplo: "ACT-0001"
        self.tipo = tipo      # Ejemplo: "Portátil", "Proyector"
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.ubicacion = ubicacion
        self.fecha_alta = fecha_alta
        self.estado = estado  # Ejemplo: "Operativo", "En reparación", "Baja"

    def __str__(self):
        return f"[{self.codigo}] {self.marca} {self.modelo} - Ubicación: {self.ubicacion}"