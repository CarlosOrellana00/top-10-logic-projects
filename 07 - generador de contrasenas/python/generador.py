import secrets
import string

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
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    if largo < len(conjuntos):
        raise ValueError(
            f"El largo mínimo debe ser {len(conjuntos)} para incluir todos los tipos elegidos."
        )

    # 1.- Garantizar 1 carácter de cada tipo
    password_chars = [secrets.choice(c) for c in conjuntos]

    # 2.- Pool total para completar el resto
    pool = "".join(conjuntos)
    faltantes = largo - len(password_chars)
    password_chars += [secrets.choice(pool) for _ in range(faltantes)]

    # 3.- Mezclar
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
