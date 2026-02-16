# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from Datos.conexion import inicializar_tablas
from Interfaz.ventana_principal import AplicacionGestion
from Herramientas.gestor_log import registrar_info


def main():
    # 1. Asegurar que la base de datos existe [cite: 68]
    inicializar_tablas()

    # 2. Registrar inicio de la aplicación [cite: 65]
    registrar_info("--- Aplicación Iniciada ---")

    # 3. Lanzar la interfaz [cite: 5]
    app = AplicacionGestion()
    app.mainloop()


if __name__ == "__main__":
    main()