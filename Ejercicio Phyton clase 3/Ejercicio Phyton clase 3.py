""" Calcular el mayor de dos números ingresados por teclado usando un operador
ternario"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mayor = num1 if num1 > num2 else num2
print("El mayor es:", mayor)


"""Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario"""

def buscar_palabra(palabra_buscada, *args):
    encontrado = "Encontrada" if palabra_buscada in args else "No encontrada"
    return encontrado


print(buscar_palabra("python", "html", "css", "python", "javascript"))


"""Determinar si un número es par o impar"""

num = int(input("Ingrese un numero: "))

resultado = "Par" if num % 2 == 0 else "Impar"
print("El número es:", resultado)


"""Calcular el promedio de una lista de números usando args y un operador ternario"""

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio
print("El promedio es:", calcular_promedio(10, 20, 30, 40, 50))
print("El promedio es:", calcular_promedio())  


"""Imprimir un mensaje de error si no se pasan suficientes argumentos"""

def imprimir_mensaje_error(*args):
    mensaje = "Error: no se pasaron suficientes argumentos" if len(args) < 2 else "Argumentos suficientes"
    return mensaje
print(imprimir_mensaje_error("arg1", "arg2"))
print(imprimir_mensaje_error("arg1"))