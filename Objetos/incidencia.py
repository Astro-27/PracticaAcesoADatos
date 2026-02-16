class Incidencia:
    def __init__(self, activo_id, fecha_apertura, prioridad, categoria, descripcion, estado, tecnico_asignado, id=None):
        self.id = id
        self.activo_id = activo_id  # ID del activo relacionado (FK)
        self.fecha_apertura = fecha_apertura
        self.prioridad = prioridad   # Alta, Media, Baja
        self.categoria = categoria   # Hardware, Software, Red, etc.
        self.descripcion = descripcion
        self.estado = estado         # Abierta, En Proceso, Resuelta
        self.tecnico_asignado = tecnico_asignado