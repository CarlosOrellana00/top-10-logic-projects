// 1.- Conectar el HTML con el JS DOM
const pantalla = document.getElementById("pantalla");
const inputPaso = document.getElementById("paso");

const btnMenos = document.getElementById("btnMenos");
const btnReset = document.getElementById("btnReset");
const btnMas = document.getElementById("btnMas");

// 2.- Estado del programa
let valor = 0;

// 3.- Funcion para escribir el valor en pantalla
function render(){
  pantalla.textContent = String(valor);
}

// 4.- Leer el paso de forma segura
function obtenerPasoSeguro(){
  const paso = Number(inputPaso.value);

  // Si no es número o es <= 0, corregimos a 1
  if(!Number.isFinite(paso) || paso <= 0){
    inputPaso.value = "1";
    return 1;
  }

  // Entero (por seguridad, evitamos decimales)
  return Math.floor(paso);
}

// 5.- Acciones
function incrementar(){
  const paso = obtenerPasoSeguro();
  valor += paso;
  render();
}

function decrementar(){
  const paso = obtenerPasoSeguro();
  valor -= paso;
  render();
}

function resetear(){
  valor = 0;
  render();
}

// 6.- Eventos de Botones

// 7.- Atajos de teclado

// 8.- Inicio del Programa