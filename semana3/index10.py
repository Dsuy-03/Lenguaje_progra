#Pide al usuario elegir una figura (1: Cuadrado, 2: Triángulo, 3: Círculo)
#y solicita los datos necesarios para calcular su área.
form = float(input("Elige una figura para calcular su área (1: Cuadrado, 2: Triángulo, 3: Círculo): "))
match form:
    case 1:
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        area = lado * lado
        print(f"El área del cuadrado es: {area}")
    case 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    case 3:
        radio = float(input("Ingrese el radio del círculo: "))
        area = 3.1416 * radio * radio
        print(f"El área del círculo es: {area}")
    case _:
        print("Figura no válida paput xdd")