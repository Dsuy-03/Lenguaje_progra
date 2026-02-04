"""
Tipos de suscripción: Pide un número (1: Plan Básico Q. 9.00, 2: Plan Estándar Q.15.00,
 3: Plan Premium Q. 20.00) y muestra los beneficios.
"""
plan = int(input("Ingrese el número de su plan de suscripción (1: Básico, 2: Estándar, 3: Premium): "))
match plan:
    case 1:
        print("Plan Básico: Acceso a contenido limitado. Costo: Q. 9.00")
    case 2:
        print("Plan Estándar: Acceso a contenido estándar y calidad HD. Costo: Q. 15.00")
    case 3:
        print("Plan Premium: Acceso a todo el contenido en calidad Ultra HD y descargas. Costo: Q. 20.00")
    case _:
        print("Plan no válido. Por favor, elija 1, 2 o 3.")