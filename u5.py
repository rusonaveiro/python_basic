from tkinter import *
import random  # random para colores aleatorios

raiz = Tk()
raiz.title("Tarea POO")

Label(raiz, text="Ingrese sus datos", bg="purple", fg="white").grid(row=0, column=0, columnspan=3, sticky=W+E)  # encabezado

Label(raiz, text="Titulo").grid(row=1, column=0, sticky=W)  # etiquetas
Label(raiz, text="Ruta").grid(row=2, column=0, sticky=W)
Label(raiz, text="Descripcion").grid(row=3, column=0, sticky=W)


def entradas(valor, ancho, fila, columna):  # funcion de las entradas
    return Entry(raiz, textvariable=valor, width=ancho).grid(row=fila, column=columna)


linea1, linea2, linea3 = StringVar(), StringVar(), StringVar()  # declarar tecleo usuario como cadena de texto


Entry1 = entradas(linea1, 20, 1, 1)  # entrada del usuario
Entry2 = entradas(linea2, 20, 2, 1)
Entry3 = entradas(linea3, 20, 3, 1)


lista = []  # lista que tendra los diccionarios
inscrip = 0  # global que sumara inscripciones


def datos():
    global inscrip
    lista.append({"Titulo": linea1.get(), "Ruta": linea2.get(), "Descripcion": linea3.get()})
    print(inscrip)
    for i in lista:
        print(i)
    inscrip = inscrip + 1


Button(raiz, text="Alta", command=datos).grid(row=4, column=1)  # command llama a la funcion


def color():
    raiz.config(bg='white')  # Color blanco de la raiz
    colores = ['dark orange', 'blue', 'peach puff']  # lista de colores
    random_colores = random.choice(colores)  # elegir aleatorio de la lista
    raiz.config(bg=random_colores)


Button(raiz, text="Sorpresa", command=color).grid(row=4, column=2)

raiz.mainloop()
