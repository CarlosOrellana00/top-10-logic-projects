import { generarSecreto, evaluarIntento } from "./juego.js";

const inputMin = document.getElementById("minimo");
const inputMax = document.getElementById("maximo");
const inputIntento = document.getElementById("intento");

const btnIniciar = document.getElementById("btnIniciar");
const btnProbar = document.getElementById("btnProbar");
const btnReiniciar = document.getElementById("btnReiniciar");

const info = document.getElementById("info");
const estado = document.getElementById("estado");
const intentosUI = document.getElementById("intentos");

let secreto = null;
let intentos = 0;
let intentosMax = 7;
let juegoActivo = false;

function leerEntero(input) {
  const n = parseInt(input.value, 10);
  return Number.isNaN(n) ? null : n;
}

function setEstado(texto, tipo = "info") {
  estado.textContent = texto;
  estado.dataset.tipo = tipo;
}

function actualizarIntentos() {
  intentosUI.textContent = `Intentos: ${intentos} / ${intentosMax}`;
}

btnIniciar.addEventListener("click", () => {
  const min = leerEntero(inputMin);
  const max = leerEntero(inputMax);

  if (min === null || max === null) {
    setEstado(" Debes ingresar mínimo y máximo como enteros.", "error");
    return;
  }
  if (min >= max) {
    setEstado(" El mínimo debe ser menor que el máximo.", "error");
    return;
  }

  secreto = generarSecreto(min, max);
  intentos = 0;
  juegoActivo = true;

  info.textContent = `Estoy pensando un número entre ${min} y ${max}.`;
  setEstado(" Juego iniciado. Ingresa tu intento.", "ok");

  actualizarIntentos();
  inputIntento.value = "";
  inputIntento.focus();

  btnProbar.disabled = false;
  btnReiniciar.disabled = false;
});

btnProbar.addEventListener("click", () => {
  if (!juegoActivo) {
    setEstado(" Primero debes iniciar el juego.", "error");
    return;
  }

  const intento = leerEntero(inputIntento);
  if (intento === null) {
    setEstado(" Ingresa un número entero válido.", "error");
    return;
  }

  intentos++;
  actualizarIntentos();

  const resultado = evaluarIntento(secreto, intento);

  if (resultado === "correcto") {
    setEstado(` ¡Correcto! Adivinaste en ${intentos} intento(s).`, "ok");
    juegoActivo = false;
    btnProbar.disabled = true;
    return;
  }

  if (intentos >= intentosMax) {
    setEstado(` Se acabaron los intentos. El número era: ${secreto}`, "error");
    juegoActivo = false;
    btnProbar.disabled = true;
    return;
  }

  setEstado(
    resultado === "alto"
      ? " Muy alto. Intenta un número menor."
      : " Muy bajo. Intenta un número mayor.",
    "info"
  );

  inputIntento.select();
});

btnReiniciar.addEventListener("click", () => {
  secreto = null;
  intentos = 0;
  juegoActivo = false;

  info.textContent = "Define un rango y presiona Iniciar.";
  setEstado("Listo para comenzar.", "info");
  intentosUI.textContent = "Intentos: 0 / 7";

  inputIntento.value = "";
  btnProbar.disabled = true;
  btnReiniciar.disabled = true;
});
