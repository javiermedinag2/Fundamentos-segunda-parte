#Ejemplo de apertura de archivo json en Python para lectura y escritura
import json

# Abrir archivo JSON en modo lectura
archivo_json = open("libros.json", "r")  # Abrir archivo en modo lectura
contenido_json = json.load(archivo_json)  # Cargar el contenido del archivo JSON
print("Contenido del archivo JSON:")
for libro in contenido_json:
    print(f"Título: {libro['title']}, Autor: {libro['author']}, Año: {libro['publishedYear']}")

archivo_json.close()  # Cerrar el archivo después de leer
