from tkinter import *
raiz = Tk()
raiz.title("Tarea POO")
raiz.resizable(0, 0)  # Desactivar redimensión de ventana

Label1 = Label(raiz, text="Ingrese sus datos", bg="purple", fg="white")
Label1.grid(row=0, column=0, columnspan=3, sticky=W+E)  # posicion en tabla expandido con columnspan y stick

Label2 = Label(raiz, text="Titulo")
Label2.grid(row=1, column=0, sticky=W)  # posicion en tabla a la izquierda
linea1 = StringVar()  # declarar tecleo usuario como cadena de texto
Entry(raiz, textvariable=linea1).grid(row=1, column=1) # entrada del usuario

Label3 = Label(raiz, text="Ruta")
Label3.grid(row=2, column=0, sticky=W)
linea2 = StringVar()
Entry(raiz, textvariable=linea2).grid(row=2, column=1)

Label4 = Label(raiz, text="Descripcion")
Label4.grid(row=3, column=0, sticky=W)
linea3 = StringVar()
Entry(raiz, textvariable=linea3).grid(row=3, column=1)

Button1 = Button(raiz, text="Alta")
Button1.grid(row=4, column=1)

Button2 = Button(raiz, text="Sorpresa")
Button2.grid(row=4, column=2)

raiz.mainloop()