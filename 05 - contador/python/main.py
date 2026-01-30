import tkinter as tk
from tkinter import messagebox

class ContadorApp:
  def __init__(self, root: tk.Tk) -> None:
    # Confirguracion de la ventana
    self.root = root
    self.root.title("Contador")
    self.root.resizable(False,True)
    self.root.geometry("420x260")
    self.root.configure(bg="#0b0f14")

    # Estado del Programa
    # valor contador
    self.valor =0

    # Titulo
    titulo = tk.Label(
      self.root,
      text="Contador",
      font=("Consolas",18,"bold"),
      fg="#c7d0d9"
      bg="#0b0f14"
    )

    # Pantalla Contador
    self.lbl_valor = tk.Label(
      self.root,
      text=str(self.valor),
      font=("Consolas",56,"bold")
      fg="#00ff99",
      bg="#0b0f14"
    )
    self.lbl_valor.pack(pady=(0,10))

    # Entrada para el "paso"
    # El paso es el valor por el cual aumenta/disminuye el contador.
    frame_paso = tk.Frame(self.root, bg = "#0b0f14")
    frame_paso.pack(pady=(0,12))

    lbl_paso = tk.Label(
      frame_paso,
      text = "Paso",
      font=("Consolas",12),
      fg ="#c7d0d9",
      bg="#0b0f14"
    )
    lbl_paso.pack(side="left",padx=(0,8))

    # StringVar permite leer/modificar el contenido del Entry fácilmente
    self.paso_var = tk.StringVar(value="1")

    self.entry_paso = tk.Entry(
      frame_paso,
      textvariable = self.paso_var,
      width = 6,
      font =("Consolas",12)
    )
    self.entry_paso.pack(side="left")

    # Botones
    frame_botones = tk.Frame(self.root, bg="#0b0f14")
    frame_botones.pack(pady=(0,8))

    btn_menos = tk.Button(
      frame_botones,
      text="-",
      width=8,
      font=("Consolas",12,"bold"),
      command = self.decrementar
    )
    btn_menos.pack(side="left",padx=6)

    btn_reset = tk.Button(
      frame_borones,
      text="Reset",
      width=8,
      font=("Consolas",12,"bold"),
      command =  self.resetear
    )
    btn_reset.pack(side="left",padx=6)

    btn_mas = tk.Button(
      frame_botones,
      text="+",
      width = 8,
      font=("Consols",12,"bold"),
      command= self.incrementar
    )
    btn_mas.pack(side="left",padx=5)

    # Atajos de teclado
