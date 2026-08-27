#Ejemplo de cómo manipoular archivos en Python para lectura y escritura
try:
    # Intento de abrir un archivo que no existe
    archivo = open("archivo_inexistente.txt", "w")
    x=10/0  
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("Error: El archivo no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")

archivo = open("archivo.txt", "a")  # Abrir archivo en modo escritura
archivo.write("Hola, este es un ejemplo de escritura en un archivo.\n")  
archivo.write("Esta es el cuarto renglon del archivo.\n")
archivo.close()  # Cerrar el archivo después de escribir

# Abrir el archivo en modo lectura
archivo = open("archivo.txt", "r")  # Abrir archivo en modo lectura
contenido = archivo.read()  # Leer todo el contenido del archivo
print("Contenido del archivo:")
print(contenido)
archivo.close()  # Cerrar el archivo después de leer
