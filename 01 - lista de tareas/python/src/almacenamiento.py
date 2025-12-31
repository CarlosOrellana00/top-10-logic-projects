import json
import os
from typing import Any, Dict, List

def cargar_json(ruta: str) ->List[Dict[str, Any]]:
  """Carga la lista de tareas desde un archivo JSON. si no existe, devuelve lista vacia."""
  if not os.path.exists(ruta):
    return[]

  try:
    with open(ruta, "r", encoding="utf-8") as f:
      data = json.load(f)
      return data if isinstance(data, list) else []
  except (json.JSONDecodeError, OSError):
    return[]

def guardar_json(ruta: str, data: List[Dict[str, Any]])->None:
  """Gurdar la lista de tareas en un archivo JSON (pretty)."""
  with open(ruta, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False,indent=2)