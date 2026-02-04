"""
​Cálculo de impuestos: Pide el salario y el tipo de empleado 
(1: Público 10%, 2: Privado 15%, 3: Independiente 8%).
"""
salario = float(input("Ingrese el salario mensual: Q"))
tip_empleado = int(input("Ingrese el tipo de empleado (1: Público, 2: Privado, 3: Independiente): "))
match tip_empleado:
    case 1:
        impuesto = salario * 0.10
        print(f"El impuesto para un empleado público es: Q{impuesto:.2f}")
    case 2:
        impuesto = salario * 0.15
        print(f"El impuesto para un empleado privado es: Q{impuesto:.2f}")
    case 3:
        impuesto = salario * 0.08
        print(f"El impuesto para un empleado independiente es: Q{impuesto:.2f}")
    case _:
        print("Tipo de empleado no válido.")