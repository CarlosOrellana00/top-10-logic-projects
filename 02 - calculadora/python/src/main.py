from calculadora import sumar, restar, multiplicar, dividir

def mostrar_menu() -> None:
  print("\n=== CALCULADORA ===")
  print("1) Sumar")
  print("2) Restar")
  print("3) Multiplicar")
  print("4) Dividir")
  print("0) Salir")

def pedir_numero(mensaje: str) -> float:
  while True:
    entrada = input(mensaje).strip().replace(",",".")
    try:
      return float(entrada)
    except ValueError:
      print("Entrada inválida. Ingresa un número (ej: 10 o 10.5).")

def main() -> None:
  while True:
    mostrar_menu()
    opcion = input("Elije una opción: ").strip()

    if opcion == "0":
      print("Adios!...nos vemos ;) ")
      break

    if opcion not in {"1","2","3","4"}:
      print("la opción no valida, intentalo nuevamente.")
      continue

    a = pedir_numero("Ingresa el Primer Numero: ")
    b = pedir_numero("Ingresa el Segundo Numero: ")

    try:
      if opcion == "1":
        resultado = sumar(a,b)
        operacion = "sumar"
      elif opcion == "2":
        resultado = restar(a,b)
        operacion = "restar"
      elif opcion == "3":
        resultado = multiplicar(a,b)
        operacion = "multiplicar"
      else:
        resultado = dividir(a,b)
        operacion = "dividir"

      print(f"Resultado de la Operación {operacion}: {resultado}")

    except ZeroDivisionError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()