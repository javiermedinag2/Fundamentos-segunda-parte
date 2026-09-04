# Ejemplo de manejo de ventanas de Windows con Tkinter
from tkinter import Tk, Label, Button

ventana = Tk()
ventana.title("Cálculo de Áreas")
ventana.geometry("400x300")
ventana.configure(bg="#ADD8E6")
ventana.resizable(True, False)
ventana.context = Label(ventana, text="Bienvenido al programa de cálculo de áreas", bg="lightblue", font=("Arial", 12))
ventana.context.pack(pady=20)
ventana.boton = Button(ventana, text="Cerrar", command=ventana.destroy, bg="blue", fg="white", font=("Arial", 12))
ventana.boton.pack(pady=10)
ventana.label = Label(ventana, text="Seleccione una opción:", bg="lightblue", font=("Arial", 12))
ventana.label.pack(pady=10)
ventana.txt = Label(ventana, text="1. Área de Círculo\n2. Área de Triángulo\n3. Área de Cuadrado", bg="lightblue", font=("Arial", 12))
ventana.txt.pack(pady=10)
ventana.mainloop()

