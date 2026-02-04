#sentencia switch
print("1. Azul, 2. amarillo, 3. Rojo")
opcion = int(input("Ingrese un numero para determinar tu color: "))

match opcion:
    case 1:
        print("has elegido el azul")
    case 2:
        print("has elegido el amarillo")
    case 3:
        print("has elegido el rojo")
    case _:
        print("Opcion no valida pa")