#Pide tres números y luego la operación (1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir).
num = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = int(input("Ingrese la operación a realizar (1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir): "))
num3 = float(input("Ingrese el tercer número: "))
match operacion:
    case 1:
        resultado = num + num2 + num3
        print(f"La suma de {num}, {num2} y {num3} es: {resultado}")
    case 2:
        resultado = num - num2 - num3
        print(f"La resta de {num}, {num2} y {num3} es: {resultado}")
    case 3:
        resultado = num * num2 * num3
        print(f"La multiplicación de {num}, {num2} y {num3} es: {resultado}")
    case 4:
        if num2 != 0 and num3 != 0:
            resultado = num / num2 / num3
            print(f"La división de {num} entre {num2} entre {num3} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Operación no válida.")