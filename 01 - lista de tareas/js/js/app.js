import {
  obtenerTareas,
  agregarTarea,
  alternarCompletada,
  eliminarTarea,
} from "./gestor_tareas.js";

import { limpiarTareas } from "./almacenamiento.js";

// 1.- Referencias a elementos HTML (DOM)
const formAgregar = document.getElementById("form-agregar");
const inputTarea = document.getElementById("input-tarea");
const listaTareas = document.getElementById("lista-tareas");
const mensajeVacio = document.getElementById("mensaje-vacio");
const botonesFiltro = document.querySelectorAll(".btn-filtro");
const btnLimpiar = document.getElementById("btn-limpiar");

// 2.- Estado simple
let filtroActual = "todas";

// 3.- Función que dibuja la lista en pantalla
function renderizar() {
  const tareas = obtenerTareas();

  // aplicar filtro
  let filtradas = tareas;
  if (filtroActual === "pendientes") {
    filtradas = tareas.filter((t) => !t.completa);
  } else if (filtroActual === "completadas") {
    filtradas = tareas.filter((t) => t.completa);
  }

  // limpiar lista
  listaTareas.innerHTML = "";

  // mostrar/ocultar mensaje vacío
  if (filtradas.length === 0) {
    mensajeVacio.style.display = "block";
  } else {
    mensajeVacio.style.display = "none";
  }

  // dibujar tareas
  for (const tarea of filtradas) {
    const li = document.createElement("li");
    li.className = "tarea-item";
    li.dataset.id = tarea.id;

    li.innerHTML = `
      <label class="tarea-label">
        <input type="checkbox" class="chk-completa" ${tarea.completa ? "checked" : ""}>
        <span class="${tarea.completa ? "completa" : ""}">${tarea.titulo}</span>
      </label>
      <button class="btn-eliminar" title="Eliminar">✖</button>
    `;

    // evento checkbox
    li.querySelector(".chk-completa").addEventListener("change", () => {
      alternarCompletada(tarea.id);
      renderizar();
    });

    // evento eliminar
    li.querySelector(".btn-eliminar").addEventListener("click", () => {
      eliminarTarea(tarea.id);
      renderizar();
    });

    listaTareas.appendChild(li);
  }
}

// 4.- Evento de agregar tarea
formAgregar.addEventListener("submit", (e) => {
  e.preventDefault();

  const nueva = agregarTarea(inputTarea.value);
  if (!nueva) return;

  inputTarea.value = "";
  inputTarea.focus();
  renderizar();
});

// 5.- Evento de filtros
botonesFiltro.forEach((btn) => {
  btn.addEventListener("click", () => {
    filtroActual = btn.dataset.filtro;

    botonesFiltro.forEach((b) => b.classList.remove("activo"));
    btn.classList.add("activo");

    renderizar();
  });
});

// 6.- Evento de limpiar todo
btnLimpiar.addEventListener("click", () => {
  const ok = confirm("¿Seguro que quieres borrar TODAS las tareas?");
  if (!ok) return;

  limpiarTareas();
  renderizar();
});

// 7.- Primera carga
document.querySelector('[data-filtro="todas"]').classList.add("activo");
renderizar();
