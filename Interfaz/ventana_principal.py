import tkinter as tk
from tkinter import messagebox, ttk, filedialog

# Importaciones de tu capa de Lógica (Servicios)
from Logica.exportar_datos import exportar_activos_csv, exportar_incidencias_json
from Logica.importar_datos import importar_activos_desde_csv

# Importaciones de tu capa de Interfaz (Vistas)
from Interfaz.gestion_activos import PantallaActivos


class AplicacionGestion(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sistema de Gestión de Activos e Incidencias - IES")
        self.geometry("1000x700")

        # 1. Contenedor principal para cambiar entre pantallas (Activos/Incidencias)
        self.contenedor_vistas = tk.Frame(self)
        self.contenedor_vistas.pack(fill="both", expand=True)

        # 2. Configurar el menú superior
        self.configurar_menu()

        # 3. Pantalla de inicio por defecto (Listado de Activos)
        self.mostrar_pantalla_activos()

    def configurar_menu(self):
        """Crea la barra de navegación superior."""
        barra_menu = tk.Menu(self)

        # --- Menú Archivo: Intercambio de datos ---
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Exportar Activos (CSV)", command=self.accion_exportar_csv)
        menu_archivo.add_command(label="Exportar Incidencias (JSON)", command=self.accion_exportar_json)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Importar Activos (CSV)", command=self.accion_importar_csv)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.quit)

        # --- Menú Gestión: Navegación por el sistema ---
        menu_gestion = tk.Menu(barra_menu, tearoff=0)
        menu_gestion.add_command(label="Gestionar Activos", command=self.mostrar_pantalla_activos)
        menu_gestion.add_command(label="Gestionar Incidencias", command=self.mostrar_pantalla_incidencias)

        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        barra_menu.add_cascade(label="Gestión", menu=menu_gestion)

        self.config(menu=barra_menu)

    # --- Métodos de Navegación ---

    def limpiar_contenedor(self):
        """Borra la pantalla actual para cargar una nueva."""
        for widget in self.contenedor_vistas.winfo_children():
            widget.destroy()

    def mostrar_pantalla_activos(self):
        """Carga la vista de gestión de activos en el contenedor."""
        self.limpiar_contenedor()
        # Llamamos a la clase que creamos en Interfaz/gestion_activos.py
        vista = PantallaActivos(self.contenedor_vistas, self)
        vista.pack(fill="both", expand=True)

    def mostrar_pantalla_incidencias(self):
        """Carga la vista de gestión de incidencias."""
        self.limpiar_contenedor()
        vista = PantallaIncidencias(self.contenedor_vistas, self)
        vista.pack(fill="both", expand=True)
    # --- Métodos de Acción (Llamadas a la Capa de Lógica) ---

    def accion_exportar_csv(self):
        if exportar_activos_csv():
            messagebox.showinfo("Éxito", "CSV generado correctamente en la carpeta 'Exportaciones'.")
        else:
            messagebox.showerror("Error", "No se pudo exportar el CSV. Revisa app.log.")

    def accion_exportar_json(self):
        if exportar_incidencias_json():
            messagebox.showinfo("Éxito", "JSON generado correctamente en la carpeta 'Exportaciones'.")
        else:
            messagebox.showerror("Error", "No se pudo exportar el JSON. Revisa app.log.")

    def accion_importar_csv(self):
        ruta = filedialog.askopenfilename(title="Seleccionar CSV de Activos", filetypes=[("Archivos CSV", "*.csv")])
        if ruta:
            if importar_activos_desde_csv(ruta):
                messagebox.showinfo("Éxito", "Datos importados y guardados en la base de datos.")
                self.mostrar_pantalla_activos()  # Refrescar la tabla
            else:
                messagebox.showerror("Error", "La importación falló. Verifica el formato del CSV.")


if __name__ == "__main__":
    app = AplicacionGestion()
    app.mainloop()