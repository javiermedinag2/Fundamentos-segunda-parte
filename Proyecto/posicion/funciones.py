#Funciones para calcular la distancia, velocidad y tiempo
def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def calcular_velocidad(distancia, tiempo):
    if tiempo != 0:
        velocidad = distancia / tiempo
    else:
        velocidad = 0
        print("El tiempo no puede ser cero para calcular la velocidad.")    
    return velocidad

def calcular_tiempo(distancia, velocidad):
    if velocidad > 0:
        tiempo = distancia / velocidad
    else:
        tiempo = 0
        print("La velocidad no puede ser cero o menor que cero para calcular el tiempo.")
    return tiempo
