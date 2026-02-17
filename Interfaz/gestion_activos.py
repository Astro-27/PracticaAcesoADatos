import tkinter as tk  # <--- ESTA LÍNEA ES LA QUE TE FALTA
from tkinter import ttk, messagebox
from Consultas.activo_sql import listar_inventario


class PantallaActivos(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        tk.Label(self, text="Inventario de Activos", font=("Arial", 14, "bold")).pack(pady=10)

        # Configuración de la tabla
        columnas = ("ID", "Código", "Tipo", "Marca", "Modelo", "Estado", "Ubicación")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Botonera
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Actualizar", command=self.cargar_datos).pack(side="left", padx=5)

        self.cargar_datos()

    def cargar_datos(self):
        """Limpia y carga los datos desde la capa de Consultas."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Accedemos a los datos por índice (0=id, 1=codigo, 2=tipo, 3=marca, 4=modelo, 6=ubicacion, 8=estado)
        for a in listar_inventario():
            self.tabla.insert("", tk.END, values=(a[0], a[1], a[2], a[3], a[4], a[8], a[6]))