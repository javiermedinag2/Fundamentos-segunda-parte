matriz = [[0,0,0],[0,0,0],[0,0,0]]
acumulador =0
for renglon in range(3):
    for columna in range (3):
        acumulador += 1
        matriz[renglon][columna]= acumulador

for renglon in range(3):
    info_renglon=""
    for columna in range (3):
        info_renglon += " " + str(matriz[renglon][columna])
    print(info_renglon)
