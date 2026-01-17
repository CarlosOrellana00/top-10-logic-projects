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

  print(f"Estoy pensando un numero entre {minimo} y {maximo}.")
  print(f"Tienes {intentos_max} intentos .\n")

  while intentos < intentos_max:
    intento = pedir_entero(f"Intento N°{intentos +1}: ")
    intentos += 1

    resultado = evaluar_intento(secreto, intento)

    if resultado == "correcto":
      print(f"EXCELENTE!!! solo te tomo {intentos} intento(s).")
      break
    elif resultado == "alto":
      print("Muy Alto!. intenta un numero menor")
    else:
      print("Muy Bajo, intenta un numero mas alto")

  else:
    print(f"LO SIENTO, se acabaron los intentos. el numero correcto era: {secreto}")

if __name__ == "__main__":
  main()
