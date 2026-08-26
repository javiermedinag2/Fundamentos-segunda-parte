#Ejemplo de manejo de errores en Python
try:
    #x= 10/0  # Intento de división por cero
    print(a)
    lista = [1, 2, 3]
    print(lista[5])  # Intento de acceder a un índice fuera de rango

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

except NameError:
    print("Error: Variable no definida.")

except IndexError:
    print("Error: Índice fuera de rango.")

finally:
    print("Bloque finally: Se ejecuta siempre, haya o no error.")
