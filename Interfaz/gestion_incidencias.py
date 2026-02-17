import tkinter as tk
from tkinter import ttk, messagebox
# Importamos la consulta que ya creamos en Consultas
from Datos.conexion import obtener_conexion
from Consultas.incidencia_sql import listar_incidencias, cambiar_estado_incidencia


class PantallaIncidencias(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador

        tk.Label(self, text="Gestión de Incidencias Técnicas", font=("Arial", 14, "bold")).pack(pady=10)

        # --- Zona de Filtros ---
        frame_filtros = tk.LabelFrame(self, text="Filtros de búsqueda")
        frame_filtros.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_filtros, text="Estado:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_estado = ttk.Combobox(frame_filtros, values=["Todos", "Abierta", "En Proceso", "Resuelta"])
        self.combo_estado.current(0)
        self.combo_estado.grid(row=0, column=1, padx=5)

        tk.Button(frame_filtros, text="Filtrar", command=self.cargar_datos).grid(row=0, column=2, padx=10)

        # --- Tabla de Incidencias ---
        columnas = ("ID", "Activo", "Fecha", "Prioridad", "Categoría", "Estado", "Técnico")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=12)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Botonera de Acciones ---
        botonera = tk.Frame(self)
        botonera.pack(pady=10)

        tk.Button(botonera, text="Cambiar a 'En Proceso'", bg="#FF9800", fg="white",
                  command=lambda: self.actualizar_estado("En Proceso")).pack(side="left", padx=5)

        tk.Button(botonera, text="Marcar como Resuelta", bg="#4CAF50", fg="white",
                  command=lambda: self.actualizar_estado("Resuelta")).pack(side="left", padx=5)

        self.cargar_datos()

    def cargar_datos(self):
        """Carga y filtra las incidencias de la BD."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        filtro_estado = self.combo_estado.get()
        datos = listar_incidencias()  # Trae (id, activo_id, fecha, prioridad, categoria, desc, estado, tecnico, codigo_activo)

        for d in datos:
            # Aplicar filtro visual
            if filtro_estado == "Todos" or d[6] == filtro_estado:
                # Mostramos d[8] que es el CÓDIGO del activo (ACT-XXXX) en lugar del ID numérico
                self.tabla.insert("", tk.END, values=(d[0], d[8], d[2], d[3], d[4], d[6], d[7]))

    def actualizar_estado(self, nuevo_estado):
        """Cambia el estado de la incidencia seleccionada."""
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una incidencia de la tabla.")
            return

        item = self.tabla.item(seleccion)
        id_incidencia = item['values'][0]

        if cambiar_estado_incidencia(id_incidencia, nuevo_estado):
            messagebox.showinfo("Éxito", f"Incidencia {id_incidencia} actualizada a {nuevo_estado}.")
            self.cargar_datos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el estado.")

