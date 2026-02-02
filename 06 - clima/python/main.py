import tkinter as tk
from tkinder import messagebox

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


