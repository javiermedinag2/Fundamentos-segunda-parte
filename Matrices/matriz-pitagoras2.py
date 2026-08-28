renglones= int(input("Indique el numero de renglones de la matriz"))
columnas = int(input("Indique el numero de columnas"))

matriz = [[0 for _ in range(columnas)] for _ in range(renglones)]
acumulador =0
for renglon in range(renglones):
    for columna in range (columnas):
        acumulador += 1
        matriz[renglon][columna]= acumulador

for renglon in range(renglones):
    info_renglon=""
    for columna in range (columnas):
        info_renglon += " " + str(matriz[renglon][columna])
    print(info_renglon)