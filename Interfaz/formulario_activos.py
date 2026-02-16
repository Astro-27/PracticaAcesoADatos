import tkinter as tk
from tkinter import messagebox
from Objetos.activo import Activo
from Logica.gestor_inventario import alta_activo_segura


class FormularioActivo(tk.Toplevel):
    def __init__(self, padre, callback_actualizar):
        super().__init__(padre)
        self.title("Añadir Nuevo Activo")
        self.geometry("400x500")
        self.callback_actualizar = callback_actualizar

        # Diccionario para guardar las cajas de texto (Entry)
        self.campos = {}

        # Lista de etiquetas para los campos
        etiquetas = [
            ("Código (ACT-XXXX)", "codigo"),
            ("Tipo (Ej: Portátil)", "tipo"),
            ("Marca", "marca"),
            ("Modelo", "modelo"),
            ("Nº Serie", "serie"),
            ("Ubicación", "ubicacion"),
            ("Fecha Alta (AAAA-MM-DD)", "fecha"),
            ("Estado (Ej: Operativo)", "estado")
        ]

        # Crear los campos visualmente
        for i, (texto, clave) in enumerate(etiquetas):
            tk.Label(self, text=texto).pack(pady=(10, 0))
            entry = tk.Entry(self)
            entry.pack(pady=5, padx=20, fill="x")
            self.campos[clave] = entry

        # Botón de guardar
        tk.Button(self, text="Guardar Activo", bg="#4CAF50", fg="white",
                  command=self.guardar).pack(pady=20)

    def guardar(self):
        # 1. Recoger datos de los campos
        nuevo_activo = Activo(
            codigo=self.campos["codigo"].get(),
            tipo=self.campos["tipo"].get(),
            marca=self.campos["marca"].get(),
            modelo=self.campos["modelo"].get(),
            numero_serie=self.campos["serie"].get(),
            ubicacion=self.campos["ubicacion"].get(),
            fecha_alta=self.campos["fecha"].get(),
            estado=self.campos["estado"].get()
        )

        # 2. Llamar a la lógica de negocio para validar
        if alta_activo_segura(nuevo_activo):
            messagebox.showinfo("Éxito", "Activo guardado correctamente.")
            self.callback_actualizar()  # Refresca la tabla automáticamente
            self.destroy()  # Cierra el formulario
        else:
            messagebox.showerror("Error", "Datos inválidos. El código debe ser ACT-XXXX.")