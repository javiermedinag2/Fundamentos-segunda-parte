import funciones
continuar = 's'
while continuar.lower() == 's':
    opcion = input("Ingrese la opción (1: Voltaje, 2: Resistencia, 3: Intensidad): ")
    if opcion == '1':
        resistencia = float(input("Ingrese la resistencia: "))
        intensidad = float(input("Ingrese la intensidad: "))
        voltaje = funciones.voltaje(intensidad, resistencia)
        print(f"El voltaje es: {voltaje} ")
    elif opcion == '2':
        intensidad = float(input("Ingrese la intensidad: "))
        voltaje = float(input("Ingrese el voltaje: "))
        resistencia = funciones.resistencia(intensidad, voltaje)
        print(f"La resistencia es: {resistencia} ")
    elif opcion == '3':
        resistencia = float(input("Ingrese la resistencia: "))
        voltaje = float(input("Ingrese el voltaje: "))
        intensidad = funciones.voltaje(resistencia, voltaje)
        print(f"El voltaje es: {intensidad} ")
    else:
        print("Opción no válida.")
    continuar = input("¿Desea realizar otro cálculo? (s/n): ")