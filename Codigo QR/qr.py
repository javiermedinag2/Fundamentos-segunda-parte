import qrcode

# Texto o enlace a codificar
url = "https://tecmilenio.mx/es"

# Generar la imagen del código QR
img = qrcode.make(url)

# Guardar la imagen en un archivo
img.save("Calajo.png")