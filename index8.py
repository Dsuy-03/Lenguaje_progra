#pide un numero del 1 al 10 y muestra su equivalente en numero romanos
num = int(input("Introduce un numero del 1 al 10: "))
match num:
    case 1:
        print("1: I")
    case 2:
        print("2: II")
    case 3:
        print("3: III")
    case 4:
        print("4: IV")
    case 5:
        print("5: V")
    case 6:
        print("6: VI")
    case 7:
        print("7: VII")
    case 8:
        print("8: VIII")
    case 9:
        print("9: IX")
    case 10:
        print("10: X")
    case _:
        print("Numero fuera de rango blo")