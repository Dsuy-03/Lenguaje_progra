"""
​Conversor de tiempo: Pide una cantidad en segundos y permite elegir 
(1: a Minutos, 2: a Horas).
"""
secundos = int(input("Ingrese la cantidad de segundos: "))
op = int(input("Elija la conversión a realizar (1: a Minutos, 2: a Horas): "))
match op:
    case 1:
        minutos = secundos / 60
        print(f"La cantidad en Minutos es: {minutos:.2f} minutos")
    case 2:
        horas = secundos / 3600
        print(f"La cantidad en Horas es: {horas:.2f} horas")
    case _:
        print("Conversión no válida.")