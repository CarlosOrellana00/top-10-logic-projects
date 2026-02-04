from validaciones import leer_entero, leer_si_no
from generador import generar_password

def main():
    print("=== 07 - Generador de Contraseñas (Python) ===")

    largo = leer_entero("Largo de la contraseña (8 a 64): ", minimo=8, maximo=64)

    usar_minus = leer_si_no("¿Incluir minúsculas? (s/n): ")
    usar_mayus = leer_si_no("¿Incluir mayúsculas? (s/n): ")
    usar_nums = leer_si_no("¿Incluir números? (s/n): ")
    usar_simb = leer_si_no("¿Incluir símbolos? (s/n): ")

    cantidad = leer_entero("¿Cuántas contraseñas generar? (1 a 20): ", minimo=1, maximo=20)

    try:
        print("\n--- Resultado ---")
        for i in range(1, cantidad + 1):
            pwd = generar_password(
                largo=largo,
                usar_minusculas=usar_minus,
                usar_mayusculas=usar_mayus,
                usar_numeros=usar_nums,
                usar_simbolos=usar_simb
            )
            print(f"{i}) {pwd}")
    except ValueError as e:
        print(f"\n Error: {e}")


if __name__ == "__main__":
    main()
