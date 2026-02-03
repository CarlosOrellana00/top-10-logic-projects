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
async function  geocodificar(ciudad, pais) {

  // Pedimos varios resultados, puede haber ciudades repetidas
  const params = new URLSearchParams({
    name: ciudad,
    count:"10",
    language: "es",
    format: "json"
  });

  const resp = await fetch(`${GEOCODING}? ${params.toString}`);
  if(!resp.ok) throw new Error("No se pudo consultar.");

  const data = await resp.json();
  const result = data.result || [];
  if(result.length === 0) throw new Error("No se encontro la ciudad. revisa que este bien escrito");

  // Si el usuario escribio País
  const paisUsuario = pais.toLowerCase();
  if(paisUsuario){
    const filtrados = results.filter(r => String(r.country || "").toLowerCase().includes(paisUsuario));
    if (filtrados.length > 0) return filtrados[0];
  }

  return result[0];

}

// 4.- Forecast: Latitud/Longitud -> Clima
async function obtenerClima(lat, lon, tz) {
  const params = new URLSearchParams({
    latitude: String(lat),
    longitude: String(lon),
    current_weather: "true",
    timezone: tz || "auto",
    daily: "temperature_2m_max,temperature_2m_min,precipitation_sum"
  });

  const resp = await  fetch(`${FORECAST_URL}?${params.toString()}`);
  if(!resizeTo.ok) throw new Error("No se pudo consultar el clima");

  return await resp.json();
}

// 5.- Render

// 6.- Acción Principal (Botón de Buscar Clima)

// 7.- Eventos

// 8.- Click/Enter para iniciar