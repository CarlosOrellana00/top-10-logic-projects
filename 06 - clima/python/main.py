import tkinter as tk
from tkinter import messagebox
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# Test de Ventana
# root = tk.Tk()
# root.title("Prueba Tkinder - Clima")
# root.geometry("320x120")
# root.mainloop()

class ClimaApp:
  def __init__(self, root: tk.Tk) ->None:
    # 1.- Ventana Principal
    self.root = root
    self.root.title("App de Clima")
    self.root.resizable(False, False)
    self.root.geometry("540x420")
    self.root.configure(bg="#0b0f14")

    # 2.- Titulo
    titulo = tk.Label(
      self.root,
      text="Consulta de Clima",
      font=("Consolas", 18, "bold"),
      fg="#c7d0d9",
      bg="#0b0f14"
    )
    titulo.pack(pady=(16,10))

    #3.- Zona de busqueda (Ciudad y País)
    frame_busqueda = tk.Frame(self.root, bg="#0b0f14")
    frame_busqueda.pack(pady=(0,10))

    tk.Label(
      frame_busqueda, text="Ciudad",
      font=("Consolas",12),
      fg="#c7d0d9", bg="#0b0f14"
    ).grid(row=0, column=0, padx=(0,0), pady=6, sticky="e")

    self.ciudad_var = tk.StringVar(value="Santiago")
    self.entry_ciudad = tk.Entry(
      frame_busqueda,
      textvariable=self.ciudad_var,
      width=22,
      font=("Consolas",12)
    )
    self.entry_ciudad.grid(row=0, column=1, pady=6)

    tk.Label(
      frame_busqueda, text="Pais: ",
      font=("Consolas",12),
      fg="#c7d0d9", bg="#0b0f14"
    ).grid(row=0,column=2, padx=(18,8), pady=6, sticky="e")

    self.pais_var = tk.StringVar(value="Chile")
    self.entry_pais = tk.Entry(
      frame_busqueda,
      textvariable=self.pais_var,
      width=18,
      font=("Consolas",12)
    )
    self.entry_pais.grid(row=0, column=3, pady=6)

    #4.- Boton Buscar
    self.btn_buscar = tk.Button(
      frame_busqueda,
      text="Buscar clima",
      font=("Consolas",12,"bold"),
      command=self.buscar_clima
    )
    self.btn_buscar.grid(row=1,column=0, columnspan=4, pady=(10,0))

    #5.- Zona de resultado
    self.lbl_resumen = tk.Label(
      self.root,
      text="Escribe una ciudad y país, y presiona 'Buscar Clima'.",
      font=("Consolas",11),
      fg="#7f8c99",
      bg="#0b0f14",
      justify="left",
      wraplength=520
    )
    self.lbl_resumen.pack(pady=(12, 10))

    #6.- Caja grande para pronostico
    self.text_pronostico = tk.Text(
      self.root,
      height=14,
      width=64,
      font=("Consolas",10),
      bg="#0f1621",
      fg="#c7d0d9",
      borderwidth=1
    )
    self.text_pronostico.pack(pady=(0,10))
    self.text_pronostico.configure(state="disabled")

    #7.- Atajo Enter para buscar
    self.root.bind("<Return>", lambda e: self.buscar_clima())

  def buscar_clima(self) -> None:

    ciudad = self.ciudad_var.get().strip()
    pais = self.pais_var.get().strip()

    if not ciudad or not pais:
      messagebox.showwarning("Campos vacios","Debes escribir Ciudad y País.")
      return

    # si todo va bien, lo mostramos como previisualizacion
    self.lbl_resumen.config(
      text=f"Listo para buscar: {ciudad}, {pais}",
      fg="#c7d0d9"
    )

    try:
      self.btn_buscar.config(state="disabled")

      geo = self.geocodificar(ciudad, pais)
      nombre = geo.get("name", ciudad)
      admin1 = geo.get("admin1", "")
      country = geo.get("country", pais)
      lat = geo["latitude"]
      lon = geo["longitude"]
      tz = geo.get("timezone", "auto")

      clima = self.obtener_clima(lat, lon, tz)

      current = clima.get("current_weather", {})
      temp = current.get("temperature", "N/A")
      wind = current.get("windspeed", "N/A")
      time = current.get("time", "N/A")

      ubicacion = f"{nombre}"
      if admin1:
        ubicacion += f", {admin1}"
      ubicacion += f", {country}"

      self.lbl_resumen.config(
        text=(
          f"Ubicación: {ubicacion}\n"
          f"Hora dato: {time}\n"
          f"Temperatura actual: {temp}°C\n"
          f"Viento: {wind} km/h"
        ),
        fg="#c7d0d9"
      )

      daily = clima.get("daily", {})
      dates = daily.get("time", [])
      tmax = daily.get("temperature_2m_max", [])
      tmin = daily.get("temperature_2m_min", [])
      rain = daily.get("precipitation_sum", [])

      lines = ["Pronóstico (7 días):\n"]
      for i in range(min(len(dates), 7)):
        lines.append(f"- {dates[i]} | Máx: {tmax[i]}°C | Mín: {tmin[i]}°C | Lluvia: {rain[i]} mm")

      self.text_pronostico.configure(state="normal")
      self.text_pronostico.delete("1.0", "end")
      self.text_pronostico.insert("end", "\n".join(lines))
      self.text_pronostico.configure(state="disabled")

    except requests.exceptions.RequestException:
      messagebox.showerror("Error de conexión", "No se pudo conectar al servicio de clima.")
    except ValueError as e:
      messagebox.showwarning("No encontrado", str(e))
    finally:
      self.btn_buscar.config(state="normal")

  def geocodificar(self, ciudad: str, pais: str) -> dict:

    params = {
        "name": ciudad.strip(),
        "count": 10,
        "language": "es",
        "format": "json"
    }

    r = requests.get(GEOCODING_URL, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    results = data.get("results", [])
    if not results:
        raise ValueError("No se encontró la ciudad. Revisa la escritura.")

    pais_usuario = pais.strip().casefold()
    if pais_usuario:
        filtrados = []
        for item in results:
            country_name = str(item.get("country", "")).casefold()
            if pais_usuario in country_name:
                filtrados.append(item)

        if filtrados:
            return filtrados[0]

    return results[0]

  def obtener_clima(self, lat: float, lon: float, tz: str) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": tz,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"
    }
    r = requests.get(FORECAST_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def main() -> None:
  root = tk.Tk()
  app = ClimaApp(root)
  root.mainloop()

if __name__ == "__main__":
  main()


