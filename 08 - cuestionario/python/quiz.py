import random
from typing import List, Dict, Any
from validaciones import leer_opcion


def aplicar_escala_nota(porcentaje: float) -> float:
    """
    Escala simple:
    - 60% => 4.0 (aprobación)
    - 100% => 7.0
    - Menos de 60% => lineal desde 1.0 a 3.9
    """
    if porcentaje >= 60.0:
        return 4.0 + (porcentaje - 60.0) * (3.0 / 40.0)
    else:
        return 1.0 + porcentaje * (2.9 / 60.0)


def mensaje_logro(porcentaje: float) -> str:
    if porcentaje == 100.0:
        return "¡Perfecto! Tienes un dominio total."
    if porcentaje >= 80.0:
        return "¡Excelente! Muy buen nivel."
    if porcentaje >= 60.0:
        return "¡Bien! Has aprobado."
    if porcentaje >= 40.0:
        return "Vas mejorando, casi lo logras."
    return "Necesitas repasar más para lograrlo. ¡Ánimo!"


def ejecutar_quiz(nombre: str, banco: List[Dict[str, Any]], cantidad_preguntas: int = 10) -> None:
    preguntas = random.sample(banco, k=cantidad_preguntas)

    correctas = 0
    print(f"\n¡Comenzamos, {nombre}! Responde con A, B, C o D.\n")

    for i, p in enumerate(preguntas, start=1):
        print(f"Pregunta {i}/{cantidad_preguntas}: {p['enunciado']}")
        for letra, texto in p["opciones"].items():
            print(f"  {letra}) {texto}")

        resp = leer_opcion("Tu respuesta (A/B/C/D): ")

        if resp == p["correcta"]:
            print("Correcto!\n")
            correctas += 1
        else:
            correcta = p["correcta"]
            print(f" Incorrecto. La correcta era {correcta}) {p['opciones'][correcta]}\n")

    puntaje_total = correctas * 10
    porcentaje = (correctas / cantidad_preguntas) * 100.0
    nota = aplicar_escala_nota(porcentaje)

    print("=== RESULTADO FINAL ===")
    print(f"Jugador: {nombre}")
    print(f"Aciertos: {correctas}/{cantidad_preguntas}")
    print(f"Puntaje: {puntaje_total}/100")
    print(f"Porcentaje: {porcentaje:.1f}%")
    print(f"Nota: {nota:.1f}")
    print(mensaje_logro(porcentaje))
