def leer_entero(mensaje: str, minimo: int | None = None, maximo: int | None = None) -> int:
  while True:
    raw = input(mensaje).strip()
    if not raw.isdigit():
      print("Debes de ingresar un numero entero valido")
      continue

    valor = int(raw)

    if minimo is not None and valor < minimo:
      print(f"Debe ser >= {minimo}.")
      continue

    if maximo is not None and valor > maximo:
      print(f"Debe ser <={maximo}.")
      continue

    return valor

def leer_si_no (mensaje: str) -> bool:
  while True:
    raw = input(mensaje).strip().lower()
    if raw in("s","si","sí","y","yes"):
      return True
    if raw in ("n","no"):
      return False
    print("Responde con 's'(si) o 'n' (no).")