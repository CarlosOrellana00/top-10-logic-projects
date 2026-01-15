def sumar(a: float, b: float) -> float:
  return a + b

def restar(a: float, b: float) -> float:
  return a - b

def multiplicar(a: float, b: float) -> float:
  return a * b

def dividir(a: float, b: float) -> float:
  if b == 0:
    raise ZeroDivisionError("NO SE PUEDE DIVIDIR POR CERO.")
  return a / b