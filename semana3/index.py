#pedir al usuario 3 numeros y hallar el mayor de ellos
num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))
num3 = float(input("Ingrese tercer numero: "))
if num1 > num2 and num3:
    print(f"El numero {num1} es mayor que el {num2} y el {num3}")
    if num2 > num1 and num3:
        print(f"El numero {num2} es mayor que {num1} y {num3}")
        if num3 > num1 and num2:
            print(f"El numero {num3} es mayor que el {num1} y {num2}")
