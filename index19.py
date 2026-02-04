"""
Piedra, Papel o Tijera: El usuario ingresa 1, 2 o 3. Usa match-case para 
determinar qué eligió y compararlo contra un valor fijo.
"""
elec_usuario = int(input("1. Piedra, 2. Papel, 3. Tijera: "))
elec_computadora = 2  
match elec_usuario:
    case 1:
        print("El usuario eligió Piedra.")
        if elec_computadora == 1:
            print("La computadora eligió Piedra. Empate.")
        elif elec_computadora == 2:
            print("La computadora eligió Papel. La computadora gana.")
        else:
            print("La computadora eligió Tijera. El usuario gana.")
    case 2:
        print("El usuario eligió Papel.")
        if elec_computadora == 1:
            print("La computadora eligió Piedra. El usuario gana.")
        elif elec_computadora == 2:
            print("La computadora eligió Papel. Empate.")
        else:
            print("La computadora eligió Tijera. La computadora gana.")
    case 3:
        print("El usuario eligió Tijera.")
        if elec_computadora == 1:
            print("La computadora eligió Piedra. La computadora gana.")
        elif elec_computadora == 2:
            print("La computadora eligió Papel. El usuario gana.")
        else:
            print("La computadora eligió Tijera. Empate.")
    case _:
        print("Elección no válida. Por favor, ingrese 1, 2 o 3.")