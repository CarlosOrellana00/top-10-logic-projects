import tkinter as tk
from tkinder import messagebox

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
    titulo.pack(pady==(16,10))

    #3.- Zona de busqueda (Ciudad y País)
    frame_busqueda = tk.Frame(self.root, bg="0b0f14")
    frame_busqueda.pack(pady=(0,10))

    tk.Label(
      frame_busqueda, text="Ciudad",
      font=("Consolas",12),
      fg="#c7d0d9", bg="#0b0f14"
    ).grid(row=0, colum=0, padx=(0,0), pady=6, sticky="e")

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
    self.entry_ciudad = tk.Entry(
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

    #6.- Caja grande para pronostico
    self.text_pronostico = tk.Text(
      self.root,
      height=14,
      width=64,
      font=("Cosolas",10),
      bg="#0f1621",
      fg="#c7d0d9",
      borderwidth=1
    )
    self.text_pronostico.pack(pady=(0,10))
    self.text_pronostico.configure(state="disabled")

    #7.- Atajo Enter para buscar
    self.root.bind("<Return>", lambda e: self.buscar_clima())


