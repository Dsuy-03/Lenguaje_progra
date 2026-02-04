"""
​Calculadora de potencia/raíz: Pide un número y elige (1: Elevar al cuadrado, 2: Raíz cuadrada).
"""
calc = float(input("Ingrese un número: "))
op = int(input("Elija una opción (1: Elevar al cuadrado, 2: Raíz cuadrada): "))
match op:
    case 1:
        resultado = calc ** 2
        print(f"El número {calc} elevado al cuadrado es: {resultado}")
    case 2:
        if calc >= 0:
            resultado = calc ** 0.5
            print(f"La raíz cuadrada de {calc} es: {resultado}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    case _:
        print("Opción no válida.")