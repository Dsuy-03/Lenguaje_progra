#Paridad y signo: Pide un número y elige una opción 
#(1: Verificar si es par, 2: Verificar si es positivo/negativo).
num = float(input("Ingrese un número: "))
opcion = int(input("Elija una opción (1: Verificar si es par, 2: Verificar si es positivo/negativo): "))
match opcion:
    case 1:
        if num % 2 == 0:
            print(f"El número {num} es par.")
        else:
            print(f"El número {num} es impar.")
    case 2:
        if num > 0:
            print(f"El número {num} es positivo.")
        elif num < 0:
            print(f"El número {num} es negativo.")
        else:
            print("El número es cero.")
    case _:
        print("Opción no válida.")