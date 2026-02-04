"""
​Direcciones de brújula: Pide un ángulo (0, 90, 180, 270) y muestra el punto
cardinal correspondiente.
"""
ang = int(input("Ingrese un ángulo (0, 90, 180, 270): "))
match ang:
    case 0:
        print("Norte")
    case 90:
        print("Este")
    case 180:
        print("Sur")
    case 270:
        print("Oeste")
    case _:
        print("Ángulo no válido.")