import random

def generar_numero(secreto_min, secreto_max: int) -> int:
  """ Generar un numero secreto entre un numoero minimo o un numero maximo."""
  return random.randint(secreto_min, secreto_max)

def evaluar_intento(secreto: int, intento: int) -> str:
  """
  Compara el intento con el numero secreto.

  Retorna:
  - "correcto" si adivino
  - "te pasaste" si el intento es mayor al numero
  - "te falta" si el intento es mejor al numero
  """

  if intento == secreto:
    return "correcto"
  elif intento > secreto:
    return "alto"
  else:
    return "bajo"