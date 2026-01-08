import{
  obtenerTareas,
  agregarTarea,
  alternarCompletada,
  eliminarTarea,
} from "./gestor_tareas.js";

import { limpiarTareas } from "./almacenamiento.js";

// 1.- Referencias a elementos HTML (DOM)
const formAgregar = document.getElementById("form-agregar");
const inputTarea = document.getElementById("input-tarea");
const listarTareas = document.getElementById("lista-tareas");
const mensajeVacio = document.getElementById("mensaje-vacio");
const botonesFiltro = document.querySelector(".btn-filtro");
const btnLimpiar = document.getElementById("btn-limpiar");

//2.- Estado simple (que el filtro esta vacio)
let filtroActual = "todas";

//3.- Fucncion que dibuja la lista en pantalla

//4.- Evento de agregar tarea

//5.- Evento de filtros

//6.- Evento de limpair todo
btnLimpiar.addEventListener("click", () =>{
  const ok = confirm("¿Seguro que quieres borrar TODAS las tareas?");
  if (!ok) return;

  limpiarTareas();
  renderizar();
});
//7.- Primea carga, marca a "todas" como activo y renderizar.
document.querySelector('[data-filtro="todas').classList.add("activo");
renderizar();