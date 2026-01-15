import { sumar, restar, multiplicar, dividir} from "./calculadora.js";

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
btnCalcular.addEventListener("click", () => {
  const a = leerNumero(inputA);
  const b = leerNumero(inputB);

  if(a === null || b === null){
    mostrarMensaje("Ingresa dos numeros validos.", "error");
    return;
  }

  try{
    let resultado;

    const op = selectOperacion.value;
    if(op === "sumar") resultado = sumar(a,b);
    else if (op === "restar") resultado = restar(a,b);
    else if (op === "multiplicar") resultado = multiplicar(a,b);
    else if (op === "dividir") resultado = dividir(a,b);

    mostrarMensaje(`resultado: ${resultado}`, "ok");
  }catch(error){
    mostrarMensaje(`Error: ${error.message}`,"error");
  }
});

//5.- limpiar
btnLimpiar.addEventListener("click", () => {
  inputA.value = "";
  inputB.value = "";
  selectOperacion.value = "sumar";
  mostrarMensaje("Ingresa numeros y selecciona una operacion.", "info");
  inputA.focus();
});
//6.- mensaje inicial
mostrarMensaje("Ingresa numeros y selecciona una operacion.", "info");