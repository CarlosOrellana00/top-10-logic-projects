import { leerTareas, guardarTareas } from "./almacenamiento";

//devolver todas las tareas
export function obtenerTareas(){
  return leerTareas();
}

