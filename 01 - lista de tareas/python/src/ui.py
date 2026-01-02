from src.almacenamiento import cargar_json, guardar_json
from src.tareas import GestorTareas

RUTA_DB = "tareas.json"


def pedir_entero(mensaje: str) -> int:
    raw = input(mensaje).strip()
    if raw == "":
        raise ValueError("Debes ingresar un número.")
    if not raw.isdigit():
        raise ValueError("Debes ingresar un número válido (solo dígitos).")
    return int(raw)


def imprimir_tareas(gestor: GestorTareas, filtro: str) -> None:
    tareas = gestor.listar(filtro)
    if not tareas:
        print("\n(No hay tareas para mostrar)\n")
        return

    print("\nID  Estado     Título")
    print("--  ---------  ------------------------------")
    for t in tareas:
        estado = "APROBADO" if t.completada else "ESPERANDO"
        print(f"{t.id:<3} {estado:<9} {t.titulo}")
    print("")


def menu() -> None:
    print("=== LISTA DE TAREAS (Python CLI) ===")
    print("1) Agregar tarea")
    print("2) Listar (todas)")
    print("3) Listar (pendientes)")
    print("4) Listar (completadas)")
    print("5) Editar tarea")
    print("6) Marcar completada")
    print("7) Marcar pendiente")
    print("8) Eliminar tarea")
    print("0) Salir")


def ejecutar_app() -> None:
    data = cargar_json(RUTA_DB)
    gestor = GestorTareas.from_json_list(data)

    while True:
        menu()
        opcion = input("\nElige una opción: ").strip()

        try:
            if opcion == "1":
                titulo = input("Título de la tarea: ")
                t = gestor.crear(titulo)
                guardar_json(RUTA_DB, gestor.to_json_list())
                print(f"\n Tarea creada (ID {t.id}).\n")

            elif opcion == "2":
                imprimir_tareas(gestor, "todas")

            elif opcion == "3":
                imprimir_tareas(gestor, "pendientes")

            elif opcion == "4":
                imprimir_tareas(gestor, "completadas")

            elif opcion == "5":
                tarea_id = pedir_entero("ID de la tarea a editar: ")
                nuevo = input("Nuevo título: ")
                gestor.editar(tarea_id, nuevo)
                guardar_json(RUTA_DB, gestor.to_json_list())
                print("\n  Tarea actualizada.\n")

            elif opcion == "6":
                tarea_id = pedir_entero("ID de la tarea a completar: ")
                gestor.marcar_completada(tarea_id, True)
                guardar_json(RUTA_DB, gestor.to_json_list())
                print("\n Marcada como completada.\n")

            elif opcion == "7":
                tarea_id = pedir_entero("ID de la tarea a dejar pendiente: ")
                gestor.marcar_completada(tarea_id, False)
                guardar_json(RUTA_DB, gestor.to_json_list())
                print("\n Marcada como pendiente.\n")

            elif opcion == "8":
                tarea_id = pedir_entero("ID de la tarea a eliminar: ")
                gestor.eliminar(tarea_id)
                guardar_json(RUTA_DB, gestor.to_json_list())
                print("\n  Tarea eliminada.\n")

            elif opcion == "0":
                print("\n¡Listo! Cerrando...\n")
                break

            else:
                print("\nOpción inválida.\n")

        except ValueError as e:
            print(f"\n Alerta: {e}\n")
        except Exception as e:
            print(f"\n Error inesperado: {e}\n")
