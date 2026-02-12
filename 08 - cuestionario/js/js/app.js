// 1.- Capturar elementos del DOM
const pantallaInicio = document.getElementById("pantallaInicio");
const pantallaJuego = document.getElementById("pantallaJuego");
const pantallaResultado = document.getElementById("pantallaResultado");

const nombreInput = document.getElementById("nombre");
const btnIniciar = document.getElementById("btnIniciar");
const errorInicio = document.getElementById("errorInicio");

const nombreJugadorEl = document.getElementById("nombreJugador");
const progresoEl = document.getElementById("progreso");
const puntajeEl = document.getElementById("puntaje");
const enunciadoEl = document.getElementById("enunciado");
const opcionesEl = document.getElementById("opciones");
const feedbackEl = document.getElementById("feedback");
const btnSiguiente = document.getElementById("btnSiguiente");

const resumenFinalEl = document.getElementById("resumenFinal");
const mensajeFinalEl = document.getElementById("mensajeFinal");
const btnReiniciar = document.getElementById("btnReiniciar");

// 2.- Estado del juego
let jugador = "";
let preguntasJuego = []; // 10 preguntas elegidas
let indice = 0;
let correctas = 0;
let puntaje = 0;

// 3.- Utilidades
function mezclarArray(array) {
  // Fisher-Yates shuffle (mezcla)
  const copia = [...array];
  for (let i = copia.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copia[i], copia[j]] = [copia[j], copia[i]];
  }
  return copia;
}

function seleccionarPreguntas(banco, cantidad = 10) {
  // Tomamos una copia, mezclamos y elegimos las primeras 10 (sin repetición)
  const mezcladas = mezclarArray(banco);
  return mezcladas.slice(0, cantidad);
}

function aplicarEscalaNota(porcentaje) {
  // Igual a tu Python
  if (porcentaje >= 60) {
    return 4.0 + (porcentaje - 60) * (3.0 / 40.0);
  }
  return 1.0 + porcentaje * (2.9 / 60.0);
}

function mensajeLogro(porcentaje) {
  if (porcentaje === 100) return "¡Perfecto! Dominio total.";
  if (porcentaje >= 80) return "¡Excelente! Muy buen nivel.";
  if (porcentaje >= 60) return "¡Bien! Has aprobado.";
  if (porcentaje >= 40) return "Vas mejorando, casi lo logras.";
  return "Necesitas repasar más. ¡Ánimo!";
}
// 4.- Render de la Pregunta
function mostrarPregunta() {
  // Reset visual
  feedbackEl.textContent = "";
  btnSiguiente.classList.add("hidden");

  const p = preguntasJuego[indice];

  progresoEl.textContent = `${indice + 1}/10`;
  puntajeEl.textContent = String(puntaje);
  enunciadoEl.textContent = p.enunciado;

  // Limpiar opciones anteriores
  opcionesEl.innerHTML = "";

  // Crear botones A/B/C/D
  Object.entries(p.opciones).forEach(([letra, texto]) => {
    const btn = document.createElement("button");
    btn.className = "opcion-btn";
    btn.textContent = `${letra}) ${texto}`;
    btn.type = "button";

    btn.addEventListener("click", () => responder(letra));

    opcionesEl.appendChild(btn);
  });
}

// 5.- Responder Pregunta
function responder(letraElegida) {
  const p = preguntasJuego[indice];

  // Deshabilitar botones para que no respondan 2 veces
  const botones = opcionesEl.querySelectorAll("button");
  botones.forEach(b => (b.disabled = true));

  if (letraElegida === p.correcta) {
    correctas++;
    puntaje += 10;
    feedbackEl.textContent = "Correcto!";
  } else {
    feedbackEl.textContent = `Incorrecto. La correcta era ${p.correcta}) ${p.opciones[p.correcta]}`;
  }

  puntajeEl.textContent = String(puntaje);

  // Mostrar botón siguiente
  btnSiguiente.classList.remove("hidden");
}

// 6.- Pasar a la siguiente pregunta o terminar
function siguiente() {
  indice++;

  if (indice >= preguntasJuego.length) {
    terminar();
  } else {
    mostrarPregunta();
  }
}

// 7.- Terminar a la siguiente pregunta o terminar
function terminar() {
  const porcentaje = (correctas / 10) * 100;
  const nota = aplicarEscalaNota(porcentaje);

  const resumen =
    `Jugador: ${jugador}\n` +
    `Aciertos: ${correctas}/10\n` +
    `Puntaje: ${puntaje}/100\n` +
    `Porcentaje: ${porcentaje.toFixed(1)}%\n` +
    `Nota: ${nota.toFixed(1)}`;

  resumenFinalEl.textContent = resumen;
  mensajeFinalEl.textContent = mensajeLogro(porcentaje);

  // Cambiar pantalla
  pantallaJuego.classList.add("hidden");
  pantallaResultado.classList.remove("hidden");
}

// 8.- Iniciar Juego
function iniciar() {
  const nombre = nombreInput.value.trim();
  if (!nombre) {
    errorInicio.textContent = "Debes ingresar tu nombre para comenzar.";
    return;
  }
  errorInicio.textContent = "";
  jugador = nombre;

  // Estado inicial
  preguntasJuego = seleccionarPreguntas(PREGUNTAS, 10);
  indice = 0;
  correctas = 0;
  puntaje = 0;

  // Pintar jugador y mostrar primera pregunta
  nombreJugadorEl.textContent = jugador;

  // Cambiar pantalla
  pantallaInicio.classList.add("hidden");
  pantallaResultado.classList.add("hidden");
  pantallaJuego.classList.remove("hidden");

  mostrarPregunta();
}

// 9.- Reiniciar
function reiniciar() {
  nombreInput.value = "";
  pantallaResultado.classList.add("hidden");
  pantallaJuego.classList.add("hidden");
  pantallaInicio.classList.remove("hidden");
}

// 10.- Eventos
btnIniciar.addEventListener("click", iniciar);
btnSiguiente.addEventListener("click", siguiente);
btnReiniciar.addEventListener("click", reiniciar);

// Enter inicia desde el input nombre
nombreInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") iniciar();
});