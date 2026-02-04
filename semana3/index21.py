"""
Clasificación de vehículos: Pide el número de ruedas (2, 4, 6, 18) y di qué 
tipo de vehículo podría ser.
"""
ruedas = int(input("Ingrese el número de ruedas del vehículo (2, 4, 6, 18): "))
match ruedas:
    case 2:
        print("El vehículo podría ser una motocicleta.")
    case 4:
        print("El vehículo podría ser un automóvil.")
    case 6:
        print("El vehículo podría ser un camión pequeño.")
    case 18:
        print("El vehículo podría ser un camión de carga grande.")
    case _:
        print("Ese numero se pasho se pasho bro.")