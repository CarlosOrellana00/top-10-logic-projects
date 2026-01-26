import { generarSecreto, evaluarIntento } from "./juego.js";

// 1.- Referencias al HTML
const inputMin = document.getElementById("minimo");
const inputMax = document.getElementById("minimo");
const inputIntento = document.getElementById("intento");

const btnIniciar = document.getElementById("btnIniciar");
const btnProbar = document.getElementById("btnProbar");
const btnReiniciar = document.getElementById("btnReiniciar");

const info = document.getElementById("info");
const estado = document.getElementById("estado");
const intentosUI = document.getElementById("intentos");

//2.- estado del juego
let secreto = null;
let intentos = 0;
let intentosMax = 7;
let juegoActivo = false;

//3.. Helpers
function leerEntero(input){
  const texto = input.value.trim();
  const n = Number(texto);
  if(texto === "" || !Number.isInteger(n)) return null;
  return n;
}

function setEstado(texto, tipo = "info"){
  estado.textContent = texto;
  estado.dataset.tipo = tipo;
}

function actualizarIntentos(){
  intentosUI.textContent = `Intentos: ${intentos} / ${intentosMax}`;
}

//4.- iniciar juego
btnIniciar.addEventListener("click", () => {
  const min = leerEntero(inputMin);
  const max = leerEntero(inputMax);

  if(min == null || max === null){
    setEstado("Debes de ingresar minimo y maximo como enteros.","error");
    return;
  }

  if(min >= max){
    setEstado("El minimo debe de ser menor que el numero maximo.","error");
    return;
  }

  secreto = generarSecreto(min, max);
  intentos = 0;
  juegoActivo = true;

  info,textContent = `Estoy pensando un numero entre ${min} y ${max}`;
  setEstado("Juego Iniciado, ingresa tu numero.", "ok");

  actualizarIntentos();
  inputIntento.value ="";
  inputIntento.focus();

  btnProbar.disabled = false;
  btnReiniciar.disabled = false;
});

//5.- probar intento
btnProbar.addEventListener("click", () => {
  if(!juegoActivo){
    setEstado("Primero debes de inicia el juego","error");
    return;
  }

  const intento = leerEntero(inputIntento);
  if(intento === null){
    setEstado("Ingresa un numero entero valido.","error");
    return;
  }

  intentos++;
  actualizarIntentos();

  const resultado = evaluarIntento(secreto,intento);



});


