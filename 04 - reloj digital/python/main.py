import tkinter as tk
from datetime import date

class RelojDigitalApp:
  def __init__(self, root: tk.Tk) -> None:
    self.root = root
    self.root.title("Reloj Digital")
    self.root.resizable(False, False)

    #Tamaño de la ventana
    self.root.geometry("420x180")

    #Fondo oscuro tipo digital
    self.root.configure(bg="0b0f14")

    #Etiqueta principal(pantalla del reloj)
    self.lbl_hora = tk.Label(
      self.root,
      text="00:00:00",
      font=("Consolas",52,"bold"),
      fg="00ff99",
      bg="#0b0f14"
    )
    self.lbl_hora.pack(pady=(25,0))

    #Etiqueta Secundaria(fecha)
    self.lbl_fecha = tk.Label(
      self.root,
      text="01-01-2000",
      font=("Consolas",16),
      fg="#c7d0d9",
      bg="#0b0f14"
    )
    self.lbl_fecha.pack(pady=(8,0))

    #Arranque del LOOP de actualizacion
    self.actualizar_reloj()

  def actualizar_reloj(self) -> None:
    ahora = datetime.now()

    #Formato Hora: HH:MM:SS
    hora_str = ahora.strftime("%H:%M:%S")

    #Formato Fecha: Dia, semana, dd-mm-yyyy
    fecha_str = ahora.str.strftime("%d-%m-%Y")

    self.lbl_hora.config(text=hora_str)
    self.lbl_fecha.config(text=fecha_str)

    #Repute cada 200ms (forma suave)
    self.root.after(200, self.actualizar_reloj)

def main()-> None:
  root = tk.Tk()
  app = RelojDigitalApp(root)
  root.mainloop()

if __name__ == "main":
  main()
