
#Conforme a la estructura  del switch case, realizar un menu de las 4 
#operaciones basicas utilizando dos numeros(solicitar)
print("1. Suma, 2. Resta, 3. Division, 4. Multiplicación")
opcion = int(input("Seleccione una de estas 3 opciones pa: "))
match opcion:
    case 1:
        print("has seleccionado la primer operacion, ingrese dos numeros:")
        num1 = int(input("Ingrese el primerr numero: "))
        num2 = int(input("Ingrese el segundoo numero: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    case 2:
        print("has seleccionado la segunda operacion, ingrese dos numeros:")
        num1 = int(input("Ingrese el primerrr numero: "))
        num2 = int(input("Ingrese el segundoo numero: "))
        resultado2 = num1 - num2
        print(f"El resultado de la resta es: {resultado2}")
    case 3:
        print("has seleccionado la tercera operacion, ingrese dos numeros:")
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        if num2 != 0:
            resultado3 = num1 / num2
            print(f"El resultado de la division es: {resultado3}")
        else:
            print("Error: No se puede dividir entre cero.")
    case 4:
        print("has seleccionado la cuarta operacion, ingrese dos numeros:")
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado4 = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado4}")