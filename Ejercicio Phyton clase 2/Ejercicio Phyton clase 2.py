"""Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario."""


def dividir(a, b):
    return a / b


try:
    resultado = dividir(25, 0)
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No es posible dividir por cero.")



"""Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario"""

try:
    numero = 10
    cadena= "20"
    
    resultado = numero + cadena
    print(f"El resultado es: {resultado}")  
except TypeError as e:
    print("Error no se puede sumar un numero y una cadena de texto.")
    print(f"Detalle del error:{e}")


"""Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra"""


usuario= {

    "nombre":"Ana",
    "edad": "25",
    "ciudad": "Madrid"
}

try:
    print(usuario["profesion"])
except KeyError as e:
    print("Error: La clave no existe en el diccionario.")
    print(f"Detalle del error: {e}")



"""Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe"""

nombre_archivo="datos_usuarios.txt"

try:

    with open (nombre_archivo, "r")as archivo:
        contenido= archivo.read()
        print("Contenido del archivo:")
        print:(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe. Creándolo ahora...")  

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo creado automáticamente tras la excepción.\n")
        
    print(f"Archivo '{nombre_archivo}' creado con éxito.") 


"""Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario."""

try:

    num1= float(input(f"Ingrese el primer numero: "))
    num2= float(input(f"Ingrese el segundo numero: "))

    resultado=num1/num2

    print(f"El resultado de la division es:{resultado}")

except valueError:
    print("Error: Debe ingresar un valor numerico valido.")

except ZeroDivisionError:
    print("Error:No se puede dividir por cero.")
