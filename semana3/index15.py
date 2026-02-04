"""
​Sistema de notas: Pide una nota numérica (1-10) y muestra el rango 
(1-4: Insuficiente, 5-6: Suficiente, 7-8: Notable, 9-10: Sobresaliente).
"""
nota = float(input("Ingrese una nota numérica (1-10): "))
match nota:
    case 1 | 2 | 3 | 4:
        print("Rango: Insuficiente")
    case 5 | 6:
        print("Rango: Suficiente")
    case 7 | 8:
        print("Rango: Notable")
    case 9 | 10:
        print("Rango: Sobresaliente")
    case _:
        print("Nota no válida. Debe estar entre 1 y 10.")