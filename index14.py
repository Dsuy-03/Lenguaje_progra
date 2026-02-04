"""
Cajero automático: Define un saldo inicial. El usuario elige 
(1: Ver saldo, 2: Depositar, 3: Retirar).
"""
saldo = 20000.00
print("Bienvenido al cajero automático.")
opcion = int(input("Elija una opción (1: Ver saldo, 2: Depositar, 3: Retirar): "))
match opcion:
    case 1:
        print(f"Su saldo actual es: Q{saldo:.2f}")
    case 2:
        deposito = float(input("Ingrese la cantidad a depositar: Q"))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Su nuevo saldo es: Q{saldo:.2f}")
        else:
            print("Cantidad de depósito no válida.")
    case 3:
        retiro = float(input("Ingrese la cantidad a retirar: Q"))
        if 0 < retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Su nuevo saldo es: Q{saldo:.2f}")
        else:
            print("Cantidad de retiro no válida o saldo insuficiente.")