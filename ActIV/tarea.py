#funcion para sumar los numeros de la tupla
def suma(tupla):
    total = 0
    for numero in tupla:
        total += numero
    return total
#funcion para ver el telefono de un contacto
def ver_telefono(diccionario, nombre):
    if nombre in diccionario:
        return diccionario[nombre]
    else:
        return "El contacto no existe"
    
numeros = (5,6,7,8,9)
print(numeros[2])
agregado = int(input("Proporcione un numero "))
Lista = list(numeros)
Lista.append(agregado)
numeros = tuple(Lista)
print(numeros)
print("La suma de los números es: ", suma(numeros))

#Uso de diccionarios
diccionario = {"Chilpandolfo":45654646, "Juan": 12345678, "Pedro": 98765432}
print(diccionario["Chilpandolfo"])
print(diccionario.get("Juan"))
print(diccionario.get("Pedro"))
#Agregar un nuevo elemento al diccionario
nuevo_nombre = input("Ingrese un nuevo nombre: ")
nuevo_numero = int(input("Ingrese un nuevo número: "))
diccionario[nuevo_nombre] = nuevo_numero
print(diccionario)

#Mostrar los nombres de los contactos
print("Los nombres de los contactos son: ")
for nombre in diccionario.keys():
    print(nombre)

buscar_nombre = input("Ingrese el nombre del contacto que desea buscar: ")
telefono = ver_telefono(diccionario, buscar_nombre)
if telefono != "El contacto no existe":
    print(f"El teléfono de {buscar_nombre} es: {telefono}")

#manejo de excepciones
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: Debe ingresar un número válido.")
#manejo de excepciones con division
try:
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

    