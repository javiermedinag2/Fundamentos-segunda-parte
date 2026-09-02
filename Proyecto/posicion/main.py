import funciones
continuar = 's'
while continuar.lower() == 's':
    opcion = input("Ingrese la opción (1: Distancia, 2: Velocidad, 3: Tiempo): ")
    if opcion == '1':
        velocidad = float(input("Ingrese la velocidad (en m/s): "))
        tiempo = float(input("Ingrese el tiempo (en segundos): "))
        distancia = funciones.calcular_distancia(velocidad, tiempo)
        print(f"La distancia es: {distancia} m")
    elif opcion == '2':
        distancia = float(input("Ingrese la distancia (en metros): "))
        tiempo = float(input("Ingrese el tiempo (en segundos): "))
        velocidad = funciones.calcular_velocidad(distancia, tiempo)
        print(f"La velocidad es: {velocidad} m/s")
    elif opcion == '3':
        distancia = float(input("Ingrese la distancia (en metros): "))
        velocidad = float(input("Ingrese la velocidad (en m/s): "))
        tiempo = funciones.calcular_tiempo(distancia, velocidad)
        print(f"El tiempo es: {tiempo} s")
    else:
        print("Opción no válida.")
    continuar = input("¿Desea realizar otro cálculo? (s/n): ")