#Pide el numero de un mes y di a que estacion pertenece
mes = int(input("Ingrese un numero del 1 al 12: "))
match mes:
    case 1:
        print("Enero: Invierno")
    case 2:
        print("Febrero: Invierno")
    case 3:
        print("Marzo: Primavera")
    case 4:
        print("Abril: Primavera")
    case 5:
        print("Mayo: Primavera")
    case 6:
        print("Junio: Verano")
    case 7:
        print("Julio: Verano")
    case 8:
        print("Agosto: Verano")
    case 9:
        print("Septiembre: Otoño")
    case 10:
        print("Octubre: Otoño")
    case 11:
        print("Noviembre: Otoño")
    case 12:
        print("Diciembre: Invierno")
    case _:
        print("Numero invalido w")