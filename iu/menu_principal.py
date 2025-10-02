from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    print(f"Nombre: {nombre_aplicacion} Versión: {numero_version}")
    print("="*51)
    print("[1] Gestión de Empleados")
    print("[2] Gestión de Proyectos")
    print("[3] Gestión de Horarios")
    print("[0] Salir del sistema")
