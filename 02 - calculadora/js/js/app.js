import { sumar, restar, multiplicar, dividir} from "./calculadora";

//1.- traer elementos de la vista HTML
const inputA = document.getElementById("numeroA");
const inputB = document.getElementById("numeroB");
const selectOperacion = document.getElementById("operacion");
const btnCalcular = document.getElementById("btnCalcular");
const btnLimpiar = document.getElementById("btnLimpiar");
const salida = document.getElementById("salida");

//2.- funcion leer numeros de inputs y validacion
