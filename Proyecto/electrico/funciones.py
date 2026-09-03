#Funciones para implementar la ley de Ohm

def intensidad(resistencia, voltaje):
    if resistencia != 0:
        corriente = voltaje/resistencia
    else:
        print("No se puede hacer división por cero")
    return corriente

def resistencia(intensidad, voltaje):
    if intensidad != 0:
        resistencia = voltaje/intensidad
    else:
        print("No se puede hacer división por cero")
    return resistencia

def voltaje(intensidad, resistencia):
    voltaje = intensidad * resistencia
    return voltaje
