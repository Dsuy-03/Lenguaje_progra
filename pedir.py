#SOLICITAR AL USUARIO SU NOMBRE Y MOSTRARLO EN PANTALLA
nom = input("Por favor escriba su nombre: ")
print(f"Mucho gusto {nom} ")


#SOLICITAR AL USUARIO SU EDAD Y DETERMINAR SU AÑO DE NACIMIENTO

Edad = input("Ingrese su edad por favor: ")
AñoActual = 2024
AñoNacimiento = AñoActual - int(Edad)
print(f"Tu año de nacimiento es: {AñoNacimiento}")