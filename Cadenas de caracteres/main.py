#Ejemplos de manipulación de cadenas de caracteres en Python

nombre = input("Indique su nombre ")
apellido = input("Indique su apellido ")

cadena = "Buenos días {} {} {}".format(nombre, apellido, "Hola mundo")
print(cadena)

cadena2 = f"Buenas tardes {nombre}  {apellido} "
print(cadena2)



