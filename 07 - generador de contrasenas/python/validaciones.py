def leer_entero(mensaje: str, minimo: int | None = None, maximo: int | None = None) -> int:
  while True:
    raw = input(mensaje).strip()
    if not raw.isdigit():
      print("Debes de ingresar un numero entero valido")
      continue

    valor = int(raw)

