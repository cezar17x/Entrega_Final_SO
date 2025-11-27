import sys

def mostrar_uso():
    print("Modo CLI:")
    print("  calculadora.exe <operacion> <num1> <num2>")
    print("Ejemplo:")
    print("  calculadora.exe sumar 5 3")
    print("\nOperaciones: sumar, restar, multiplicar, dividir")


def main():
    try:
        if len(sys.argv) == 1:
            print("=== CALCULADORA CLI - MODO INTERACTIVO ===")
            operacion = input("Operación (sumar/restar/multiplicar/dividir): ").lower()
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))

        elif len(sys.argv) == 4:
            operacion = sys.argv[1].lower()
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])

        else:
            print("Parámetros incorrectos.")
            mostrar_uso()
            input("\nPresiona ENTER para cerrar...")
            return

        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
            if num2 == 0:
                print("Error: no se puede dividir por cero.")
                input("Presiona ENTER para cerrar...")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            mostrar_uso()
            input("Presiona ENTER para cerrar...")
            return

        print(f"\nResultado: {resultado}")

    except Exception as e:
        print("Error inesperado:", e)

    input("\nPresiona ENTER para cerrar...")


if __name__ == "__main__":
    main()