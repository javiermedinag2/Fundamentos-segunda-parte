import circulo
import cuadrado
import triangulo

seguir = 's'
while seguir == 's':
    opcion = input("Seleccione la figura geométrica (círculo 'c', cuadrado 'q', triángulo 't'): ")

    if opcion == 'c':
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", circulo.area_circulo(radio))
    elif opcion == 'q':
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El área del cuadrado es:", cuadrado.area_cuadrado(lado))
    elif opcion == 't':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", triangulo.area_triangulo(base, altura))
    else:
        print("Opción no válida.")

    seguir = input("¿Desea calcular otra área? (s/n): ")