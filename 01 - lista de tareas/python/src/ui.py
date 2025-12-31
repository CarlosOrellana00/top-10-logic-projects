from typing import Optional
from src.almacenamiento import cargar_json, guardar_json
from src.tareas import GestorTareas

RUTA_DB ="tareas.json"

def pedir_entero(mensaje: str) -> int:
  raw = input(mensaje),strip()
  if raw == "":
    raise ValueError("Debes de ingresar un numero.")
  if not raw.isdigit():
    raise ValueError("Debes de ingresar un numero valida (solo digitos).")
  return int(raw)

def imprimir_tareas(gestor: GestorTareas, filtro: str) -> None:
  tareas = gestor.listar(filtro)
  if not tareas:
    print("\n(No hay tareas para mostrar)\n")
    return

  print("\nID Estado itulo")
  print("--  ------  ------------------------------")
  for t in tareas:
    estado = "APROBADO" if t.completada else "ESPERANDO"
    print(f"{t.id:<3} {estado:<6} {t.titulo}")
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


