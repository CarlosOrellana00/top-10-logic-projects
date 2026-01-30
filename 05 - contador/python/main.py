import tkinter as tk
from tkinter import messagebox


class ContadorApp:
  def __init__(self, root: tk.Tk) -> None:
    # Confirguracion de la ventana
    self.root = root
    self.root.title("Contador")
    self.root.resizable(False, True)
    self.root.geometry("420x260")
    self.root.configure(bg="#0b0f14")

    # Estado del Programa
    # valor contador
    self.valor = 0

    # Titulo
    titulo = tk.Label(
      self.root,
      text="Contador",
      font=("Consolas", 18, "bold"),
      fg="#c7d0d9",
      bg="#0b0f14"
    )
    titulo.pack(pady=(18, 8))

    # Pantalla Contador
    self.lbl_valor = tk.Label(
      self.root,
      text=str(self.valor),
      font=("Consolas", 56, "bold"),
      fg="#00ff99",
      bg="#0b0f14"
    )
    self.lbl_valor.pack(pady=(0, 10))

    # Entrada para el "paso"
    # El paso es el valor por el cual aumenta/disminuye el contador.
    frame_paso = tk.Frame(self.root, bg="#0b0f14")
    frame_paso.pack(pady=(0, 12))

    lbl_paso = tk.Label(
      frame_paso,
      text="Paso",
      font=("Consolas", 12),
      fg="#c7d0d9",
      bg="#0b0f14"
    )
    lbl_paso.pack(side="left", padx=(0, 8))

    # StringVar permite leer/modificar el contenido del Entry fácilmente
    self.paso_var = tk.StringVar(value="1")

    self.entry_paso = tk.Entry(
      frame_paso,
      textvariable=self.paso_var,
      width=6,
      font=("Consolas", 12)
    )
    self.entry_paso.pack(side="left")

    # Botones
    frame_botones = tk.Frame(self.root, bg="#0b0f14")
    frame_botones.pack(pady=(0, 8))

    btn_menos = tk.Button(
      frame_botones,
      text="-",
      width=8,
      font=("Consolas", 12, "bold"),
      command=self.decrementar
    )
    btn_menos.pack(side="left", padx=6)

    btn_reset = tk.Button(
      frame_botones,
      text="Reset",
      width=8,
      font=("Consolas", 12, "bold"),
      command=self.resetear
    )
    btn_reset.pack(side="left", padx=6)

    btn_mas = tk.Button(
      frame_botones,
      text="+",
      width=8,
      font=("Consolas", 12, "bold"),
      command=self.incrementar
    )
    btn_mas.pack(side="left", padx=5)

    # Atajos de teclado
    # Flecha arriba: sumar
    # Flecha abajo: restar
    # Tecla R: reset
    self.root.bind("<Up>", lambda event: self.incrementar())
    self.root.bind("<Down>", lambda event: self.decrementar())
    self.root.bind("r", lambda event: self.resetear())

    # Texto pequeño de ayuda
    ayuda = tk.Label(
      self.root,
      text="Atajos: ↑ suma, ↓ resta, R resetea",
      font=("Consolas", 10),
      fg="#7f8c99",
      bg="#0b0f14"
    )
    ayuda.pack(pady=(6, 0))

  # ----- Función para leer el paso de forma segura -----
  def obtener_paso(self) -> int:
    """
    Lee el paso desde el Entry.
    - Si el usuario escribe algo no válido, mostramos un mensaje y usamos 1.
    """
    texto = self.paso_var.get().strip()

    try:
      paso = int(texto)
      if paso <= 0:
        raise ValueError("El paso debe ser mayor que 0")
      return paso
    except ValueError:
      messagebox.showwarning(
        "Paso inválido",
        "El paso debe ser un número entero mayor que 0.\nSe usará paso = 1."
      )
      self.paso_var.set("1")
      return 1

  # ----- Actualiza la pantalla con el valor actual -----
  def refrescar(self) -> None:
    self.lbl_valor.config(text=str(self.valor))

  # ----- Acciones de los botones -----
  def incrementar(self) -> None:
    paso = self.obtener_paso()
    self.valor += paso
    self.refrescar()

  def decrementar(self) -> None:
    paso = self.obtener_paso()
    self.valor -= paso
    self.refrescar()

  def resetear(self) -> None:
    self.valor = 0
    self.refrescar()


def main() -> None:
  root = tk.Tk()
  app = ContadorApp(root)
  root.mainloop()


if __name__ == "__main__":
  main()
