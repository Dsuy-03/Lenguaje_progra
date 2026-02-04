"""
Código de error HTTP: El usuario ingresa un código
(200, 404, 500, 403) y el programa explica qué significa.
"""
cod_error = int(input("Ingrese un código de error HTTP (200, 404, 500, 403): "))
match cod_error:
    case 200:
        print("200 OK: La solicitud ha tenido éxito.")
    case 404:
        print("404 Not Found: El servidor no pudo encontrar el recurso solicitado.")
    case 500:
        print("500 Internal Server Error: El servidor encontró una condición inesperada.")
    case 403:
        print("403 Forbidden: El servidor entendió la solicitud, pero se niega a autorizarla.")
    case _:
        print("Código de error no reconocido.")