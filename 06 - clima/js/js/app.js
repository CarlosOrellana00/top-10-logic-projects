// Endpoints "Open-Meteo"(mismos que los suando en Python)
const GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL = "https://geocoding-api.open-meteo.com/v1/search";

// 1.- DOM
const ciudadEl = document.getElementById("ciudad");
const pasiEl = document.getElementById("pais");
const btnBuscar = document.getElementById("btnBuscar");
const ResumenEl = document.getElementById("resumen");
const pronosticoEl = document.getElementById("pronostico");

// 2.- Helpers
function limpiarTexto(t){
  return String(t || "").trim();
}

// 3.- Geocoding: ciudad/pais ->(Latitud/Longitud)

// 4.- Forecast: Latitud/Longitud -> Clima

// 5.- Render

// 6.- Acción Principal (Botón de Buscar Clima)

// 7.- Eventos

// 8.- Click/Enter para iniciar