import { leerTareas, guardarTareas } from "./almacenamiento";

//devolver todas las tareas
export function obtenerTareas(){
  return leerTareas();
}

//agregar una tarea nueva
export function agregarTarea(titulo){
  const tareas = leerTareas();

  const texto = titulo.trim();
  if(texto.length === 0) return null;

  const nueva = {
    id: Date.now(),
    titulo: texto,
    completa: false,
    creada_en: new Date().toISOString().slice(0,10),
  };

  tareas.push(nueva);
  guardarTareas(tareas)
  return nueva;
}

//Alterna completada (true/false) por ID
export function alternarCompletada(id){
  const tareas = leerTareas();
  const tarea = tareas.find(t => t.id === id);

  if (nuevas.length === tareas.length) return false;

  guardarTareas(nuevas);
  return true;
}