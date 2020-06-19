# INTERFACES GRÁFICAS CON PYTHON Y TKINTER

"""
EXPLICACIÓN RÁPIDA DE ALGUNOS COMPONENTES
Tk -    Es el contenedor de todos los elementos (widgets) que tendrá nuestra interfaz.
        Además es al que llamaremos Raiz o Root. Su tamaño puede definirse o ser modificable.

Frame - El Frame o Marco es por sí mismo un widget aunque no nos permita interactuar con el programa.
        El marco será el contenedor de los widgets que utilicemos.

Label - Es un widget en el que podemos mostrar textos estáticos.

Entry - Cuadro de texto para ingresar textos cortos (una sola linea)

Text -  Este widget nos permite escribir textos largos (multilinea).

Button - Es un botón con texto.

Radiobutton - Es un circulo al cual podemos hacerle clic y seleccionar una opción

Checkbutton - Es un cuadrado que nos permite seleccionar opciones.

Menu -  Son los típicos botones que vemos en las ventanas en la parte superior que despliegan opciones

Dialogs - Ventanas emergentes que muestran información al usuario. Como alertas o ventanas para elegir
          archivos, etc...
"""

# Importamos la biblioteca TKinter
from tkinter import *

# Creamos la raiz o root de nuestra app
root = Tk()
# Añadimos un título a la ventana
root.title("Academia Coder")
# Añadimos un icono para Windows (y creo que para linux NO PARA MAC)
root.iconbitmap("python_18894.ico")
# Decimos si puede redimensionarse o no con 0 y 1 o true y false
root.resizable(1, 0)  # No funciona en Mac en WINDOWS SI!!!
# Definir el alto y ancho que queramos
root.geometry("1000x300")
# Cambiar algunas opciones
root.config(bg="green")

# Ejecutamos el bucle infinito
root.mainloop()  # siempre va al final de nuestro programa


# 21 Widgets:
Toplevel widget
Label widget
Button widget
Canvas widget
Checkbutton widget
Entry widget
Frame widget #contenedor para los demás widgets, dentro de la ventana raíz
LabelFrame widget
Listbox widget
Menu widget
Menubutton widget
Message widget
OptionMenu widget
PanedWindow widget
Radiobutton widget
Scale widget
Scrollbar widget
Spinbox widget
Text widget
Bitmap Class widget
Image Class widget


#Crear ventana
from tkinter import * #importamos el módulo tkinter
raiz = Tk() #creamos una clase llamada raíz del tipo Tk
raiz.mainloop() #mantiene visible la ventana raíz

#cambiar el nombre de la ventana
from tkinter import *
raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.mainloop()

#cambiar tamaño llamamoss geometry
from tkinter import *
raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.geometry("520x480") #Configurar tamaño
raiz.mainloop()

#cambiar Icono llamando el método iconbitmap
from tkinter import *
raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.geometry("520x480") #Configurar tamaño
raiz.iconbitmap("form.ico") #Cambiar el icono
raiz.mainloop()

#cambiar color de fondo
"""le pasamos como parámetros las letras bg seguidas de un igual 
y dentro de comillas dobles, el color en inglés o en formato hexadecimal. 
Las letras bg vienen de la palabra background"""
from tkinter import *
raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.geometry("520x480") #Configurar tamaño
raiz.iconbitmap("form.ico") #Cambiar el icono
raiz.config(bg="blue") #Cambiar color de fondo
raiz.mainloop()

#prohibe manipular tamaño el metodo resizable
from tkinter import *
raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.geometry("520x480") #Configurar tamaño
raiz.iconbitmap("form.ico") #Cambiar el icono
raiz.config(bg="blue") #Cambiar color de fondo
raiz.resizable(0,0)
raiz.mainloop()
"""raiz.resizable(1,1) es el que viene por defecto en tkinter, 
para permitir la manipulacion del tamño de la venta por parte del usuario, 
pero sin embargo; tkinter tambien permite establecer que el ancho 
pueda ser manipulado pero el alto no y viceversa.
Si quisiera que en la ventana de mi programa se pueda manipular solo el ancho 
usaria raiz.resizable(1,0) y si quiero manipular solo el alto usaria raiz.resizable(0,1)."""

#####################################################################################

#Frame contenedor para los demás widgets, dentro de la ventana raíz
from tkinter import *
raiz = Tk()
mi_Frame = Frame() #Creación del Frame
mi_Frame.pack() #Empaquetamiento del Frame (le decimos al frame que debe estar dentro de la ventana raíz)
raiz.mainloop()

# personalizar el frame con método config
"""Cambiar el tamaño alto y ancho en pixeles con width y height mi_Frame.config(width=”400″, height=”200″)
#Cambiar color de fondo	mi_Frame.config(bg=”blue”)
#Cambiar grosor del borde con bd que viene de borderwidth mi_Frame.config(bd=24)
#Cambiar el tipo de borde o relieve	mi_Frame.config(relief=”sunken”)
#Cambiar el tipo de forma que tendrá el cursor al pasar por encima del frame mi_Frame.config(cursor=”heart”)"""
from tkinter import *
raiz = Tk()
mi_Frame = Frame() #Creacion del Frame
mi_Frame.pack()  #Empaquetamiento del Frame
mi_Frame.config(bg="blue") #cambiar color de fondo
mi_Frame.config(width="400", height="200") #cambiar tamaño
mi_Frame.config(bd=24) #cambiar el grosor del borde
mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor
raiz.mainloop()


#Método pack() ajusta todos los elementos acomodándolos entre sí uno debajo del otro
#gestor de geometría
#mi_Frame.pack(fill=”valor”)	‘x’, ‘y’, ‘both’, ‘none’
#mi_Frame.pack(expand=”valor”)	0, 1, “True”, “False”
#mi_Frame.pack(side=”valor”)	‘left’, ‘right’, ‘top’, ‘bottom’
from tkinter import *
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(fill="x") #Configurar el metodo pack() Al redimensionar la ventana observamos que el tamaño del frame se aumenta en la dirección x
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

from tkinter import *
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(expand=1) #Configurar el metodo pack() le añade un espacio adicional a medida que se redimensiona la ventana raíz
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

from tkinter import *
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(fill='x', expand=1) #Configurar el metodo pack() con fill y expand
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()

from tkinter import *
raiz = Tk()
mi_Frame=Frame()
mi_Frame.pack(side='left') #Configurar el metodo pack() cambia la posición del widget dependiendo del valor dado
mi_Frame.config(bg="blue")
mi_Frame.config(width="150", height="150")
raiz.mainloop()


#####################################################################################

#Label Son widgets de etiquetas para mostrar texto o imágenes
"""La sintaxis para crear los label es la siguiente:
nombre_del_label = Label(contenedor, text=“ ”)
Llamamos a la clase Label(), le pasamos como parámetros el contenedor donde estará, 
y por último el texto que mostrará, entre comillas dobles"""

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
raiz.mainloop()

# cambiaremos el color de fondo
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
raiz.mainloop()

# cambiar parametros con config font = (‘nombre_fuente’, tamaño)
"""Para los label existen parámetros que podemos configurar dentro del método config 
entre ellos el tipo de fuente, el color del texto, el tamaño, el margen de relleno, entre otros
Cambiar el tipo de fuente necesita que le demos como valores el nombre de la fuente y el tamaño"""
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
raiz.mainloop()

# cambiar el color del texto fg = “color”, fg de foreground
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
mi_Label.config(fg="red") #Cambiar color del texto
raiz.mainloop()

# Agregar margenes
"""Para que las letras no estén muy pegada al borde, le agregamos un margen de relleno o padding. 
El método config acepta dos parámetros el padx y el pady
padx: margen de relleno en el eje x, acepta valores en pixeles
pady: margen de relleno en el eje y, acepta valores en pixeles"""
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 44)) #Cambiar tipo y tamaño de fuente
mi_Label.config(fg="red") #Cambiar color del texto
mi_Label.config(padx=20, pady=20) #Agregar margen de relleno
raiz.mainloop()

#####################################################################################

# Entry widget de entrada del usuario nombre_entry = Entry(contenedor)
# están limitados a solo una línea de entrada
"""Llamamos a la clase Entry() y le pasamos el contenedor donde estará, en este caso el Frame"""
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
raiz.mainloop()

# Poner efectos al Entry con metodo config
"""
Cambiar color de la barra del texto insertbackground=”color”
Cambiar dirección del texto justify=RIGHT
Desactivar un entry state=DISABLE"""
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
mi_Entry.config(insertbackground="red") #Cambiar color del texto
mi_Entry.config(justify=RIGHT)
raiz.mainloop()

# Creamos otro entry y lo desactivamos
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Esto es un Entry") #Creación del Label
mi_Label.pack()
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.pack()
mi_Entry.config(insertbackground="red") #Cambiar color del texto
mi_Entry.config(justify=RIGHT) #Dirección del texto
mi_Entry2 = Entry(mi_Frame)
mi_Entry2.pack()
mi_Entry2.config(state=DISABLE) #Desactivar un Entry
raiz.mainloop()


#####################################################################################

# Obtener texto con GET()

from tkinter import *
root = Tk()
root.title("Tarea POO")


def Ver():
    print(escritor.get())


escritor = StringVar()

entrada1 = Entry(root, textvariable=escritor, width=20)
entrada1.grid(row=1, column=1)

Button(root, text="Ver", command=Ver).grid(row=6, column=1)

root.mainloop()


#####################################################################################


#Método Place necesita como parámetros los valores ‘x’ y ‘y’ en pixeles.
#gestor de geometría
#objeto.place(x=’valor’, y=’valor’)
#tener dos elementos alineados uno al lado del otro
from tkinter import *
raiz = Tk()
mi_Frame = Frame(raiz, width=500, height=250)
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Metodo place")
mi_Label.place(x=50, y=10)
mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.place(x=150, y=10)
raiz.mainloop()

#####################################################################################

# Separar dos textos
from tkinter import *
master = Tk()
Label(text="uno").pack()
separador = Frame(master, height=2, bd=1, relief=SUNKEN)
separador.pack(fill=X, padx=5, pady=5)
Label(text="dos").pack()
mainloop()

"""Agregamos el “Frame” en la ventana pasando la ventana como primer parámetro.
Esta es la forma de indicar que un componente cualquiera se encuentra dentro de otro.
Para hacer que un botón normal parezca presionado, por ejemplo, si desea implementar una caja de herramientas,
simplemente puede cambiar el relieve de LEVANTADO a SUNKEN: (relieve = SUNKEN)"""

#####################################################################################

# Grillas (tablas) objeto.grid(row= ‘valor’, column= ‘valor’)
#gestor de geometría

from tkinter import *
root = Tk()
Label(root, text="id").grid(row=0, column=0)
Label(root, text="nombre").grid(row=1, column=0)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

from tkinter import *
raiz = Tk()
mi_Frame = Frame(raiz)
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Metodo grid")
mi_Label.grid(row=0, column=0)
mi_Entry = Entry(mi_Frame)
mi_Entry.grid(row=0, column=1)
raiz.mainloop()

"""El elemento padre es particionado en un determinado número de filas y columnas, 
y cada "celda" de la tabla resultante puede contener una nueva aplicación."""

#####################################################################################

#Uso de sticky (ajustar texto de tabla a la izquierda)

from tkinter import *
root = Tk()
Label(root, text="id").grid(row=0, column=0, sticky=W) #texto a la izquierda
Label(root, text="nombre").grid(row=1, column=0, sticky=W)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

"""Dentro de una grilla, las aplicaciones se ubican centradas 
(esto se nota en el ejemplo anterior en el caso del Label que contiene el id), 
para modificar este comportamiento podemos utilizar el atributo “sticky”, 
el cual toma como parámetros las opciones: N, S, W y E """

#####################################################################################

# Botones estructura Button()
# Nomenclatura: Button(master=None, **options)

#creando un boton simple
from tkinter import *
def hola(): # Definimos una función a ejecutar al clic el botón
    print("Hola mundo!")
root = Tk()
Button(root, text="Clícame", command=hola).pack() # Enlezamos la función a la acción del botón
root.mainloop()


#Función callback
"""Un botón sin devolución de llamada es bastante inútil; simplemente no hace nada cuando presiona el botón. 
Es posible que desee utilizar dichos botones de todos modos al desarrollar una aplicación. 
En ese caso, probablemente sea una buena idea deshabilitar el botón """

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", command=callback)
b.pack()
mainloop()

"""creamos un botón asociado al widget master con texto y que ejecuta 
la función "callback" con la palabra reservada “def” que finaliza (:), 
y lo que hace la rutina se pone debajo 
agregando una tabulación para indicar que pertenece a la función"""

#####################################################################################

# Deshabilitado
# Para cuando hago pruebas, deshabilito el botón, le agrego state=DISABLED

b = Button(master, text="Help", state=DISABLED)

#####################################################################################

# dentro de Grid (Tabla) o uso pack() o uso grid()
# El método vuelve con los botones posicionados en la cuadrícula.
from tkinter import*
master = Tk()
master.title("Grid Widget")

label = Label(master, text="First Name",font=10)
label.grid(row=0)

entry = Entry(master)
entry.grid(row=0, column=1)

label = Label(master, text="Last Name", font=10)
label.grid(row=1)

entry = Entry(master)
entry.grid(row=1, column=1)

button1 = Button(master, text="Submit")
button1.grid(row=2, column=1)

master.mainloop()

#####################################################################################

# Padding es un espaciado dentro del mismo agrega padx y pady
"""Si no especifica un tamaño, el botón se hace lo suficientemente grande como para contener su contenido. 
Puede usar la opción padx y pady para agregar espacio adicional entre el contenido y el borde del botón."""

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", command=callback, padx=132, pady=132)
b.pack()
mainloop()

#####################################################################################

#Alto y ancho
"""Usar las opciones de alto y ancho para establecer explícitamente el tamaño. 
Si muestra texto en el botón, estas opciones definen el tamaño del botón en unidades de texto. 
Si en su lugar muestra mapas de bits o imágenes, definen el tamaño en píxeles"""

#Botón de texto en unidades de texto, imagenes en px.
from tkinter import *
master = Tk()
b = Button(master, text="Sure!", anchor=W, justify=LEFT, padx=22, height=3, width=12)
b.pack(fill=BOTH, expand=1)
mainloop()

#####################################################################################

# Imagen si no implementamos otra librería adicional debe estar en formato .gif

from tkinter import *
master = Tk()
photo = PhotoImage(file="download.gif")
c = Button(master, text="Sure!", anchor=W, justify=LEFT, image=photo)
c.pack(fill=BOTH, expand=1)
mainloop()

#####################################################################################

# Color
# Fondo: background="black" ó bg="black"
# Letra: foreground="red" ó fg="red"
# Fondo activo: activebackground="green"
# Letra activa: activeforeground="yellow",
# Letra deshabilitado: disabledforeground="blue"

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", command=callback, padx=132, pady=132, activebackground="green", activeforeground="yellow", background="black", foreground="red")
b.pack()
a = Button(master, text="OK", command=callback, padx=132, pady=132, state=DISABLED, background="black", disabledforeground="blue")
a.pack()
mainloop()

#####################################################################################

# Posición

# Posición de texto e imagen anchor=SW
"""Opciones: N, NE, E, SE, S, SW, W, NW, o CENTER.
Por default es CENTER.(anchor / Anchor)"""

# Posición de botón side=LEFT
"""Opciones: LEFT, TOP, RIGHT, BOTTOM
Esta opción va dentro de pack()"""

from tkinter import *
master = Tk()
master.geometry("300x300")
def callback():
    print("click!")
b = Button(master, text="OK", command=callback,
activebackground="green", activeforeground="yellow",
background="black", foreground="red", height=7, width=12, anchor=SW)
b.pack(side=LEFT)
mainloop()

#####################################################################################

# Tipo de texto font=('tipo', tamaño, 'peso')

from tkinter import *
master = Tk()
b = Button(master, text="Ok!", anchor=W, justify=LEFT, padx=22, height=3, width=12, font=('courier', 22, 'bold'))
b.pack(fill=BOTH, expand=1)
mainloop()

##############################################################################

#Relieves de botones

from tkinter import *
master = Tk()

B1 = Button(master, text ="FLAT", relief=FLAT ) #PLANO
B2 = Button(master, text ="RAISED", relief=RAISED ) #ELEVADO
B3 = Button(master, text ="SUNKEN", relief=SUNKEN ) #HUNDIDO
B4 = Button(master, text ="GROOVE", relief=GROOVE ) #RANURA
B5 = Button(master, text ="RIDGE", relief=RIDGE ) #CRESTA

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
mainloop()


##############################################################################

#creando un boton simple
from tkinter import *
# Definimos una función a ejecutar al clic el botón
def hola():
    print("Hola mundo!")
root = Tk()
# Enlazamos la función a la acción del botón
Button(root, text="Clícame", command=hola).pack()

root.mainloop()

##############################################################################

# Cajas de diálogo tkMessageBox
# uso de las funciones: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, o askretrycance

from tkinter import *
from tkinter.messagebox import *

def mensaje_error():
    showerror("Título de mensaje de error", "Contenido del mensaje de error")
def verificar():
    if askyesno('Título de la consulta de verificación', 'Contenido de verificación'):
        showinfo('Si', 'Mensaje de información')
    else:
        showinfo('No', 'Esta a punto de salir')

Button(text='Error', command=mensaje_error).pack(fill=X)
Button(text='Verificar', command=verificar).pack(fill=X)

mainloop()

############

# Usando Lamda misma situacion

from tkinter import *
from tkinter.messagebox import *

def verificar():
    if askyesno('Título de la consulta de verificación', 'Contenido de verificación'):
        showinfo('Si', 'Mensaje de información')
    else:
        showinfo('No', 'Esta a punto de salir')
Button(text='Error', command=(lambda: showerror('Título de mensaje de error',"Contenido del mensaje de error"))).pack(fill=X)
Button(text='Verificar', command=verificar).pack(fill=X)
mainloop()

############

# Cajas de diálogo – Seleccionar Archivo askopenfilename()

from tkinter import *
from tkinter.filedialog import askopenfilename

def callback():
    ruta = askopenfilename()
    print(ruta)
Button(text='Abrir archivo', command=callback).pack(fill=X)
mainloop()

############

# Cajas de diálogo – Selección de color askcolor()

from tkinter import *
from tkinter.colorchooser import askcolor
def callback():
    result = askcolor(color="#00ff00", title="Bernd's Colour Chooser")
    print(result)
    print(result[1])
root = Tk()
Button(root, text='Seleccionar color', fg="green", command=callback).pack(side=LEFT, padx=10)
Button(text='Cerrar', command=root.quit, fg="red").pack(side=LEFT, padx=10)
mainloop()

################################################

# Imágenes - pueden ser presentadas dentro de botones, cajas, canvas: PhotoImage()

from tkinter import *
ruta = "/Users/diegote/Desktop/Python Argento/Aprende-a-Programar-con-Python-3-master//"
win = Tk()
imagen = PhotoImage(file=ruta + "download.gif")
Button(win, image=imagen).pack()
win.mainloop()


# Ejemplo con canvas
from tkinter import *
ruta = "/Users/diegote/Desktop/Python Argento/Aprende-a-Programar-con-Python-3-master//"
win = Tk()
imagen = PhotoImage(file=ruta + "download.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=imagen, anchor=NW)
win.mainloop()


# Seleccionar imagen con Glob y Random
# Glob nos permite seleccionar una serie de archivos que tengan una determinada extensión y forma aleatoria con random
from tkinter import *
from glob import glob
import random
ruta = '/Users/diegote/Desktop/Python Argento/Aprende-a-Programar-con-Python-3-master//'

def seleccion():
    nombre, foto = random.choice(imagen)
    dialogo.config(text=nombre)
    boton.config(image=foto)

root=Tk()
dialogo = Label(root, text="aquí va a ir la ruta", bg='OrangeRed')
boton = Button(root, text="Presionar para ver imagen", command=seleccion)
dialogo.pack(fill=BOTH)
boton.pack()

archivo = glob(ruta + "*.gif")
imagen = [(x, PhotoImage(file=x)) for x in archivo]
print(archivo)
root.mainloop()


# Librería PILLOW png, jpeg, jpg
from tkinter import *
from PIL.ImageTk import PhotoImage
from glob import glob
import random
ruta = '/Users/diegote/Desktop/Python Argento/Aprende-a-Programar-con-Python-3-master//'

def seleccion():
    nombre, foto = random.choice(imagen)
    dialogo.config(text=nombre)
    boton.config(image=foto)

root=Tk()
dialogo = Label(root, text="aquí va a ir la ruta", bg='green')
boton = Button(root, text="Presionar para ver imagen", command=seleccion)
dialogo.pack(fill=BOTH)
boton.pack()

archivo = glob(ruta + "*.jpg")
imagen = [(x, PhotoImage(file=x)) for x in archivo]
print(archivo)
root.mainloop()


# Librería PILLOW - thumbnails
import os
from tkinter import *
from PIL import Image

def crearThumbs(directorio, size=(100, 100), subdirectorio='thumbs'):

    directorioParaThumb = os.path.join(directorio, subdirectorio)
    if not os.path.exists(directorioParaThumb):
        os.mkdir(directorioParaThumb)

    for imagen in os.listdir(directorio):
    thumbpath = os.path.join(directorioParaThumb, imagen)
    print('Creando', thumbpath)
    imgpath = os.path.join(directorio, imagen)
    try:
        imgobj = Image.open(imgpath)
        imgobj.thumbnail(size, Image.ANTIALIAS)
        imgobj.save(thumbpath)
    except:
        print("Skipping: ", imgpath)

if __name__ == '__main__':
    directorioImagenes = 'images'
    thumbs = crearThumbs(directorioImagenes)

# El resultado final, es un subdirectorio de imágenes miniatura de las imágenes originales.

########################################################################

# Texto

from tkinter import *
root = Tk()
T = Text(root, height=4, width=33)
T.pack()
texto1 = """
1.-Línea 1-------------------- 
\n2.-Línea 2------------------ 
\n3.-Línea 3------------------ 
\n4.-Línea 4------------------ 
\n5.-Línea 5------------------ 
\n6.-Línea 6------------------
"""
T.insert(END, texto1)
mainloop()

# Texto Scrollbar

from tkinter import *
root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
texto1 = """
1.-Línea 1--------------------
\n2.-Línea 2------------------ 
\n3.-Línea 3------------------ 
\n4.-Línea 4------------------ 
\n5.-Línea 5------------------ 
\n6.-Línea 6------------------ 
"""
T.insert(END, texto1)
mainloop( )

##############################################################

# Menu