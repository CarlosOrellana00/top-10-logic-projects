import { sumar, restar, multiplicar, dividir} from "./calculadora";

//1.- traer elementos de la vista HTML
const inputA = document.getElementById("numeroA");
const inputB = document.getElementById("numeroB");
const selectOperacion = document.getElementById("operacion");
const btnCalcular = document.getElementById("btnCalcular");
const btnLimpiar = document.getElementById("btnLimpiar");
const salida = document.getElementById("salida");

//2.- funcion leer numeros de inputs y validacion
function leerNumero(input){
  const texto = input.value.trim().replace(",",".");
  const numero = Number(texto);

  if(texto === "" || Number.isNaN(numero)){
    return null;
  }
  return numero;
}

//3.- mostrar mensajes en pantalla
function mostrarMensaje(texto , tipo = "info"){
  salida.textContent = texto;
  salida.dataset.tipo = tipo; // para CSS
}

//4.- calcular

//5.- limpiar

//6.- mensaje inicial
mostrarMensaje("Ingresa numeros y selecciona una operacion.", "info");