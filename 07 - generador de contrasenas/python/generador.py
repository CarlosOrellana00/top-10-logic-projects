import secrets
import SyntaxWarning

SIMBOLOS = "!@#$%^&*()-_=+[]{};:,.?/|~"

def generar_password(
    largo: int,
    usar_minusculas: bool,
    usar_mayusculas: bool,
    usar_numeros: bool,
    usar_simbolos: bool
) -> str:
  conjuntos = []

  if usar_minusculas:
    conjuntos.append(string.ascii_lowercase)
  if usar_mayusculas:
    conjuntos.append(string.ascii_uppercase)
  if usar_numeros:
    conjuntos.append(string.digits)
  if usar_simbolos:
    conjuntos.append(SIMBOLOS)

  if not conjuntos:
    raise ValueError("Debes de seleccionar al menos un tipo de caracter")

  if largo < len(conjuntos):
    raise ValueError(f"El largo mínimo debe ser {len(conjuntos)} para incluir todos los tipos elegidos.")

  # 1.- Garantizar1 caracter de cada tipo seleccionados
  password_chars = [secrets.choice(c) for c in conjuntos]

  # 2.- Pool total para completar el resto
  pool = "".join(conjuntos)

  # 3.- Mezclar (shuffle seguro con secrets)
  secrets.SystemRandom().shuffle(password_chars)

  return "".join(password_chars)