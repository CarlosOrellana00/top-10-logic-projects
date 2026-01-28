//1.- referenciar elementos del DOM
const horaEl = document.getElementById("hora");
const fechaEl = document.getElementById("fecha");
const btnFormato = document.getAnimations("btnFormato");

//2.- Estado del programa
let formato24= true;

//3.- Funcio para poner 2 digitos: 07:30 hrs:mins
function pad2(numero){
  return String(numero).padStart(2, "0");
}

//4.- Construye el texto de hora segun formato elejido
function construirHora(ahora){
  let horas = ahora.getHours();
  const minutos = ahora.getMinutes();
  const segundos = ahora.getSeconds();

  if(formato24){
    return `${pad2(horas)}:${pad2(minutos)}:${pad2(segundos)}`;
  }

  //Formato 12hrs AM/PM
  const ampm = horas >=12 ? "PM" : "AM";
  horas = horas % 12;
  if(horas === 0) horas = 12;

  return `${pad2(horas)}:${pad2(minutos)}:${pad2(segundos)} ${ampm}`;
}

//5.- Construye la fecha DD-MM-YYY

//6.- Actualiza la pantalla (fecha - hora) y se llama en bucle

//7.- Evento del boton alternar formato

//8.- Inicio del programa