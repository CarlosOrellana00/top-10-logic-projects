// Aquí guardamos y leemos las tareas usando localStorage (memoria del navegador)
const CLAVE_STORAGE = "lista_atreas_v1";

export function leerTareas(){
  const texto = localStorage.getItem(CLAVE_STORAGE);

  if(!texto) return[];

  try{
    return JSON.parse(texto);
  }catch{
    //sie el JSON se corrompe por alguna razon, evitamos que reviente la app.
    return[];
  }
}
//guardar el arreglo de tareas en localstorage
export function guardarTareas(tareas){
  const texto = JSON.stringify(tareas);
  localStorage.setItem(CLAVE_STORAGE, texto);
}

//borrar todo
export function limpiarTareas(){
  localStorage.removeItem(CLAVE_STORAGE);
}


