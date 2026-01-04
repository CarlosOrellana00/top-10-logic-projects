// Aquí guardamos y leemos las tareas usando localStorage (memoria del navegador)
const CLAVE_STORAGE = "lista_atreas_v1";

export function leerTareas(){
  const texto = localStorage.getItem(CLAVE_STORAGE);

  if(!texto) return[];

  try{
    return JSON.parse(texto);
  }catch{
    return[];
  }
}