#Conversor de temperatura: El usuario ingresa grados Celsius y elige (1: a Fahrenheit, 2: a Kelvin).
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
conversion = int(input("Elija la conversión a realizar (1: a Fahrenheit, 2: a Kelvin): "))
match conversion:
    case 1:
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura en Fahrenheit es: {fahrenheit}")
    case 2:
        kelvin = celsius + 273.15
        print(f"La temperatura en Kelvin es: {kelvin}")
    case _:
        print("Conversión no válida.")