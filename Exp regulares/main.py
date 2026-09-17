import re

email = input("Indique su correo electrónico ")

patron = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(patron, email):
    print("Correo válido")
else:
    print("Correo inválido")
