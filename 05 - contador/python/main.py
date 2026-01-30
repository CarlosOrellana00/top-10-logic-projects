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



    # StringVar permite leer/modificar el contenido del Entry fácilmente
    # Botones
