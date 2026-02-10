from preguntas import PREGUNTAS
from validaciones import leer_texto_no_vacio
from quiz import ejecutar_quiz

def main():
  print("=== 08 - Cuestionario (Python) ===")
  nombre = leer_texto_no_vacio("Ingresa tu nombre")

  ejecutar_quiz(nombre=nombre, banco=PREGUNTAS, cantidad_preguntas=10)

if __name__ == "__main__":
  main()