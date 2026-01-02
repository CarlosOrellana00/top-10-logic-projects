from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional

def ahora_iso() -> str:
  return  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@dataclass
class Tarea:
  id: int
  titulo: str
  completada: bool = False
  creada_en: str = ""
  actualizada_en: str =""

  def to_dict(self) -> Dict[str,Any]:
    return asdict(self)

  @staticmethod
  def from_dict(d:Dict[str,Any])->"Tarea":
    return Tarea(
      id=int(d.get("id",0)),
      titulo=str(d.get("titulo","")),
      completada=bool(d.get("completada",False)),
      creada_en=str(d.get("creada_en","")),
      actualizada_en=str(d.get("actualizada_en",""),)
    )

  def validar_titulo(titulo: str) -> str:
    titulo = titulo.strip()
    if len(titulo) == 0:
      raise ValueError("El titulo no puede estar vacio.")
    if len(titulo) > 80:
      raise ValueError("El titulo no puede exceder 80 caracteres.")
    return titulo

class GestorTareas:
    def __init__(self, lista: Optional[List["Tarea"]] = None):
      self._tareas: List[Tarea] = lista or []
      self._normalizar_ids()

    def _normalizar_ids(self) -> None:
      """Asegura IDs unicos y oprdenados si el JSON vino raro."""
      vistos = set()
      nuevas = []
      for t in self._tareas:
        if t.id in vistos or t.id <= 0:
          continue
        vistos.add(t.id)
        nuevas.append(t)
      self._tareas= sorted(nuevas, key=lambda x: x.id)

    def _siguiente_id(self) -> int:
      return(max((t.id for t in self._tareas), default=0)+1)

    def listar(self, filtro: str = "todas") -> List["Tarea"]:
      filtro = filtro.lower().strip()
      if filtro == "pendientes":
        return [t for t in self._tareas if not t.completada]
      if filtro == "completadas":
        return [t for t in self._tareas if t.completada]
      return list(self._tareas)

    def buscar_por_id(self, tarea_id: int) -> Optional["Tarea"]:
      for t in self._tareas:
        if t.id == tarea_id:
          return t
      return None

    def crear(self, titulo: str) -> Tarea:
      titulo = valida_titulo(titulo)
      nueva  = Tarea(
        id= self._siguiente_id(),
        titulo=titulo,
        completada=False,
        creada_en=ahora_iso(),
        actualizada_en=ahora_iso(),
      )
      self._tareas.append(nueva)
      return nueva

    def editar(self, tarea_id: int, nuevo_titulo: str) -> Tarea:
      t = self.buscar_por_id(tarea_id)
      if not t:
        raise ValueError("No existe una tarra con ese ID.")
      t.titulo = validar_titulo(nuevo_titulo)
      t.actualizada_en = ahora_iso()
      return t

    def marcar_completada(self, tara_id: int, estado: bool = True) -> Tarea:
      t = self.buscar_por_id(tarea_id)
      if not t:
        raise ValueError("No existe una tarea con ese ID.")
      t.completada = bool(estado)
      t.actualizada_en = ahora_iso()
      return t

    def eliminar(self, tarea_id: int) -> None:
      t = self.buscar_por_id(tarea_id)
      if not t:
        raise ValueError("No existe una tara con ese ID.")
      self._tareas = [x for x in self._tareas if x.id != tarea_id]

    def to_json_list(self) -> List[Dict[str, Any]]:
      return [t.to_dict() for t in self._tareas]

    @staticmethod
    def from_json_list(data: List[Dict[str, Any]]) -> "GestorTareas":
      tareas = []
      for item in data:
        if isinstance(item, dict):
          tareas.append(Tarea.from_dict(item))
      return GestorTareas(tareas)



