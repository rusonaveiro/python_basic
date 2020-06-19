from tkinter import *
import random
import mysql.connector

raiz = Tk()
raiz.title("Tarea POO")

########################################################################################

# etiquetas de encabezado y columna 0
Label(raiz, text="Ingrese sus datos", bg="purple", fg="white").grid(row=0, column=0, columnspan=3, sticky=W+E)
Label(raiz, text="Titulo").grid(row=1, column=0, sticky=W)  # etiquetas
Label(raiz, text="Ruta").grid(row=2, column=0, sticky=W)
Label(raiz, text="Descripcion").grid(row=3, column=0, sticky=W)

########################################################################################

# funcion para 3 entradas en una sola linea
def entradas(valor, ancho, fila, columna):
    return Entry(raiz, textvariable=valor, width=ancho).grid(row=fila, column=columna)


linea1, linea2, linea3 = StringVar(), StringVar(), StringVar()

Entry1 = entradas(linea1, 20, 1, 1)  # entrada del usuario
Entry2 = entradas(linea2, 20, 2, 1)
Entry3 = entradas(linea3, 20, 3, 1)

########################################################################################

# crea registros en sql con datos de usuarios

def datos():
    try:
        base = mysql.connector.connect(
            user='root',
            passwd='root',
            unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
            raise_on_warnings=True,
            database='baseprueba1'
        )
        cursor = base.cursor()
        sql = "INSERT INTO producto(titulo, ruta, descripcion) VALUES(%s, %s, %s)"
        datos = (linea1.get(), linea2.get(), linea3.get())
        cursor.execute(sql, datos)
        base.commit()
        print("se ha agregado tu registro a la db")
    except:
        print("antes debes apretar el botoncito de crear db")



# boton de entrada de datos para la db
Button(raiz, text="Alta", command=datos).grid(row=4, column=1)  # command llama a la funcion

########################################################################################

# cambian los colores con el boton sorpresa
def color():
    raiz.config(bg='white')  # Color blanco de la raiz
    colores = ['dark orange', 'blue', 'peach puff']  # lista de colores
    random_colores = random.choice(colores)  # elegir aleatorio de la lista
    raiz.config(bg=random_colores)

# boton de cambio de colores
Button(raiz, text="Sorpresa", command=color).grid(row=4, column=2)

########################################################################################

# se crea la db y tabla al apretar el boton
def creadordb():
    try:
        base = mysql.connector.connect(
            user='root',
            passwd='root',
            unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
            raise_on_warnings=True
        )
        cursor = base.cursor()
        cursor.execute("CREATE DATABASE baseprueba1")
    except:
        print("La base de datos ya estaba creada antes de que llegaras")
    try:
        base = mysql.connector.connect(
            user='root',
            passwd='root',
            unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
            raise_on_warnings=True,
            database='baseprueba1'
        )
        cursor = base.cursor()
        cursor.execute(
            "CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
    except:
        print("La tabla producto ya esta creada, vete a freir churros")

# boton de creacion de db
Button(raiz, text="Crear bd", command=creadordb).grid(row=4, column=0)

########################################################################################

raiz.mainloop()

