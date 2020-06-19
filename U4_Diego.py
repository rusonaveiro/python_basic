from tkinter import *
import random  # random para colores aleatorios

raiz = Tk()
raiz.title("Tarea POO")
raiz.resizable(0, 0)  # Desactivar redimensión de ventana

Label1 = Label(raiz, text="Ingrese sus datos", bg="purple", fg="white")
Label1.grid(row=0, column=0, columnspan=3, sticky=W+E)  # posicion en tabla expandido con columnspan y stick

Label2 = Label(raiz, text="Titulo")
Label2.grid(row=1, column=0, sticky=W)  # posicion en tabla a la izquierda
linea1 = StringVar()  # declarar tecleo usuario como cadena de texto
Entry1 = Entry(raiz, textvariable=linea1)  # entrada del usuario
Entry1.grid(row=1, column=1)

Label3 = Label(raiz, text="Ruta")
Label3.grid(row=2, column=0, sticky=W)
linea2 = StringVar()
Entry2 = Entry(raiz, textvariable=linea2)
Entry2.grid(row=2, column=1)

Label4 = Label(raiz, text="Descripcion")
Label4.grid(row=3, column=0, sticky=W)
linea3 = StringVar()
Entry3 = Entry(raiz, textvariable=linea3)
Entry3.grid(row=3, column=1)


def datos():
    print("Titulo: " + Entry1.get() + "\n" + "Ruta: " + Entry2.get() + "\n" + "Descripcion: " + Entry3.get()) # Obtengo impresos los valores de cada entrada


Button1 = Button(raiz, text="Alta", command=datos)
Button1.grid(row=4, column=1)


def color():
    raiz.config(bg='white')  # Color blanco de la raiz
    colores = ['dark orange', 'blue', 'peach puff']  # lista de colores
    random_colores = random.choice(colores)  # elegir aleatorio de la lista
    raiz.config(bg=random_colores)


Button2 = Button(raiz, text="Sorpresa", command=color)  # con command el boton llama a la funcion color
Button2.grid(row=4, column=2)

raiz.mainloop()
