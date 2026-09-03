#Ejemplos de inicialización de matrices
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[0 for _ in range(3)] for _ in range(3)]

print("Matriz 1:")
for renglon in matriz1:
    print(renglon)
print("\nMatriz 2:")
for renglon in matriz2:
    print(renglon)
    