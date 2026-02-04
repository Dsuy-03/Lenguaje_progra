"""
​Conversor de divisas: Pide una cantidad en moneda local y elige 
(1: a Dólares, 2: a Euros, 3: a Libras).
"""
cantidad = float(input("Ingrese la cantidad en moneda local: Q"))
opcion = int(input("Elija la conversión a realizar (1: a Dólares, 2: a Euros, 3: a Libras): "))
match opcion:
    case 1:
        dolares = cantidad / 7.65
        print(f"La cantidad en Dólares es: ${dolares:.2f}")
    case 2:
        euros = cantidad / 9.04
        print(f"La cantidad en Euros es: €{euros:.2f}")
    case 3:
        libras = cantidad / 11.0 
        print(f"La cantidad en Libras es: £{libras:.2f}")
    case _:
        print("Conversión no válida.")