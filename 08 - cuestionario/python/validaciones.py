def leer_texto_no_vacio(mensaje: str) -> str:
  while True:
    texto = input(mensaje).strip()
    if texto:
      return texto
    print("No puede estar vacio.")

def leer_opcion(mensaje: str, opciones_validas=("A","B","C","D")) -> str:
  opciones_validas = tuple(o.upper() for o in opciones_validas)

  while True:
    op = input(mensaje).strip().upper()
    if op in opciones_validas:
      return op
    print("Opción invalida. Debes escribir: {', '.join(opciones_validas)}")

