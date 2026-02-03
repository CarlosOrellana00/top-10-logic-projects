// Endpoints "Open-Meteo"(mismos que los suando en Python)
const GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL  = "https://api.open-meteo.com/v1/forecast";

// 1.- DOM
const ciudadEl = document.getElementById("ciudad");
const pasiEl = document.getElementById("pais");
const btnBuscar = document.getElementById("btnBuscar");
const resumenEl = document.getElementById("resumen");
const pronosticoEl = document.getElementById("pronostico");

// 2.- Helpers
function limpiarTexto(t){
  return String(t || "").trim();
}

// 3.- Geocoding: ciudad/pais ->(Latitud/Longitud)
async function geocodificar(ciudad, pais) {
  const params = new URLSearchParams({
    name: ciudad,
    count: "10",
    language: "es",
    format: "json"
  });

  const resp = await fetch(`${GEOCODING_URL}?${params.toString()}`);
  if (!resp.ok) throw new Error("No se pudo consultar.");

  const data = await resp.json();
  const results = data.results || [];
  if (results.length === 0) throw new Error("No se encontró la ciudad. Revisa que esté bien escrito.");

  const paisUsuario = (pais || "").toLowerCase().trim();
  if (paisUsuario) {
    const filtrados = results.filter(r =>
      String(r.country || "").toLowerCase().includes(paisUsuario)
    );
    if (filtrados.length > 0) return filtrados[0];
  }

  return results[0];
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

  const resp = await fetch(`${FORECAST_URL}?${params.toString()}`);
  if (!resp.ok) throw new Error("No se pudo consultar el clima");

  return await resp.json();
}

// 5.- Render
function renderResumen({ ubicacion, time, temp, wind }) {
  resumenEl.textContent =
`Ubicación: ${ubicacion}
Hora Dato: ${time}
Temperatura Actual: ${temp}°C
Viento: ${wind} km/h`;
}

function renderPronostico(daily) {
  const dates = daily.time || [];
  const tmax = daily.temperature_2m_max || [];
  const tmin = daily.temperature_2m_min || [];
  const rain = daily.precipitation_sum || [];

  const lineas = [];
  lineas.push("Pronóstico (7 días):");
  lineas.push("");

  for (let i = 0; i < Math.min(dates.length, 7); i++) {
    lineas.push(`${dates[i]} | Max: ${tmax[i]}°C | Min: ${tmin[i]}°C | Lluvia: ${rain[i]} mm`);
  }

  pronosticoEl.textContent = lineas.join("\n");
}

// 6.- Acción Principal (Botón de Buscar Clima)
async function buscarClima() {
  const ciudad = limpiarTexto(ciudadEl.value);
  const pais = limpiarTexto(pasiEl.value);

  if (!ciudad || !pais) {
    alert("Debes escribir Ciudad y País.");
    return;
  }

  btnBuscar.disabled = true;
  resumenEl.textContent = `Buscando: ${ciudad}, ${pais} ...`;
  pronosticoEl.textContent = "";

  try {
    // A geocoding
    const geo = await geocodificar(ciudad, pais);
    const nombre = geo.name || ciudad;
    const admin1 = geo.admin1 || "";
    const country = geo.country || pais;
    const lat = geo.latitude;
    const lon = geo.longitude;
    const tz = geo.timezone || "auto";

    let ubicacion = nombre;
    if (admin1) ubicacion += `, ${admin1}`;
    ubicacion += `, ${country}`;

    // B forecast
    const clima = await obtenerClima(lat, lon, tz);
    const current = clima.current_weather || {};

    renderResumen({
      ubicacion,
      time: current.time ?? "N/A",
      temp: current.temperature ?? "N/A",
      wind: current.windspeed ?? "N/A"
    });

    renderPronostico(clima.daily || {});
  } catch (err) {
    resumenEl.textContent = "Error: " + (err?.message || "desconocido");
    pronosticoEl.textContent = "";
  } finally {
    btnBuscar.disabled = false;
  }
}

// 7.- Eventos
btnBuscar.addEventListener("click", buscarClima);

// 8.- Click/Enter para iniciar
document.addEventListener("keydown", (e) => {
  if (e.key === "Enter") buscarClima();
});