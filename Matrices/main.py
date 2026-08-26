#Ejemplo de manejo de matrices en Python utilizando listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]

# Función para imprimir la matriz
def imprimir_matriz(m):
    for fila in m:
        print(fila)

def indice_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"Elemento en la posición ({i}, {j}): {m[i][j]}")

# Imprimir la matriz
imprimir_matriz(matriz)

# Imprimir los índices y valores de la matriz
indice_matriz(matriz)

