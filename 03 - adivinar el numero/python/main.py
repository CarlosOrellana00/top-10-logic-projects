from juego import generar_numero, evaluar_intento

def pedir_entero(mensaje: str) -> int:
  """ Pide un numero entero al usuario, validando que sea correcto"""
  while True:
    entrada = input(mensaje).strip()
    try:
      return int (entrada)
    except ValueError:
      print("Entrada Invalida. debes de ingresar un numero entero.")

def main()-> None:
  print("Adivina el numero")
  print("Debes adivinar el numero secreto. \n")

  minimo = 1
  maximo = 100
  intentos_max = 7

  secreto = generar_numero(minimo, maximo)
  intentos = 0

