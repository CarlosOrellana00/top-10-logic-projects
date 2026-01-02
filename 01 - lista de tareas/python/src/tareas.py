from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional


# -------------------------
# Utilidades
# -------------------------
def ahora_iso() -> str:
    """Devuelve la fecha/hora actual en formato texto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validar_titulo(titulo: str) -> str:
    """
    Limpia y valida el título de una tarea.
    - No puede quedar vacío.
    - Máximo 80 caracteres.
    """
    titulo = titulo.strip()
    if titulo == "":
        raise ValueError("El título no puede estar vacío.")
    if len(titulo) > 80:
        raise ValueError("El título no puede exceder 80 caracteres.")
    return titulo


# -------------------------
# Modelo
# -------------------------
@dataclass
class Tarea:
    id: int
    titulo: str
    completada: bool = False
    creada_en: str = ""
    actualizada_en: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convierte la tarea a diccionario (para guardar en JSON)."""
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Tarea":
        """Crea una Tarea desde un diccionario (al cargar JSON)."""
        return Tarea(
            id=int(d.get("id", 0)),
            titulo=str(d.get("titulo", "")),
            completada=bool(d.get("completada", False)),
            creada_en=str(d.get("creada_en", "")),
            actualizada_en=str(d.get("actualizada_en", "")),
        )


# -------------------------
# Lógica / CRUD
# -------------------------
class GestorTareas:
    def __init__(self, lista: Optional[List[Tarea]] = None):
        self._tareas: List[Tarea] = lista or []
        self._normalizar_ids()

    def _normalizar_ids(self) -> None:
        """
        Limpia IDs duplicados o inválidos (por si el JSON venía raro).
        Deja la lista ordenada por ID.
        """
        vistos = set()
        nuevas: List[Tarea] = []
        for t in self._tareas:
            if t.id <= 0 or t.id in vistos:
                continue
            vistos.add(t.id)
            nuevas.append(t)
        self._tareas = sorted(nuevas, key=lambda x: x.id)

    def _siguiente_id(self) -> int:
        """Calcula el siguiente ID disponible."""
        return max((t.id for t in self._tareas), default=0) + 1

    # ----------- Consultas -----------
    def listar(self, filtro: str = "todas") -> List[Tarea]:
        """
        Retorna tareas según filtro:
        - "todas"
        - "pendientes"
        - "completadas"
        """
        filtro = filtro.lower().strip()
        if filtro == "pendientes":
            return [t for t in self._tareas if not t.completada]
        if filtro == "completadas":
            return [t for t in self._tareas if t.completada]
        return list(self._tareas)

    def buscar_por_id(self, tarea_id: int) -> Optional[Tarea]:
        """Busca una tarea por ID. Devuelve la tarea o None."""
        for t in self._tareas:
            if t.id == tarea_id:
                return t
        return None

    # ----------- CRUD -----------
    def crear(self, titulo: str) -> Tarea:
        titulo = validar_titulo(titulo)
        nueva = Tarea(
            id=self._siguiente_id(),
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
            raise ValueError("No existe una tarea con ese ID.")
        t.titulo = validar_titulo(nuevo_titulo)
        t.actualizada_en = ahora_iso()
        return t

    def marcar_completada(self, tarea_id: int, estado: bool = True) -> Tarea:
        t = self.buscar_por_id(tarea_id)
        if not t:
            raise ValueError("No existe una tarea con ese ID.")
        t.completada = bool(estado)
        t.actualizada_en = ahora_iso()
        return t

    def eliminar(self, tarea_id: int) -> None:
        t = self.buscar_por_id(tarea_id)
        if not t:
            raise ValueError("No existe una tarea con ese ID.")
        self._tareas = [x for x in self._tareas if x.id != tarea_id]

    # ----------- JSON -----------
    def to_json_list(self) -> List[Dict[str, Any]]:
        """Convierte todas las tareas a lista de diccionarios (para guardar)."""
        return [t.to_dict() for t in self._tareas]

    @staticmethod
    def from_json_list(data: List[Dict[str, Any]]) -> "GestorTareas":
        """Crea un GestorTareas desde una lista de diccionarios (cargada del JSON)."""
        tareas: List[Tarea] = []
        for item in data:
            if isinstance(item, dict):
                tareas.append(Tarea.from_dict(item))
        return GestorTareas(tareas)
