from tkinter import *
raiz = Tk()
raiz.title("Tarea POO")
raiz.resizable(0, 0) # Desactivar redimensión de ventana
raiz.geometry("500x200") #tamaño ventana

mi_Frame = Frame(raiz) #creo el contenedor
mi_Frame.grid() #sello el contenedor

mi_Label1 = Label(mi_Frame, text="Ingrese sus datos") #Creación del Label
mi_Label1.grid(row=0, column=1) #posicion en tabla
mi_Label1.config(bg="purple") #color de fondo
mi_Label1.config(fg="white") #color blanco en texto "Ingrese sus datos"

mi_Label2 = Label(mi_Frame, text="Titulo") #Creación del Label2
mi_Label2.grid(row=1, column=0, sticky=W) #posicion en tabla y a la izquierda
mi_Entry2 = Entry(mi_Frame) #entrada texto usuario
mi_Entry2.grid(row=1, column=1) #posicion en tabla

mi_Label3 = Label(mi_Frame, text="Ruta") #Creación del Label3
mi_Label3.grid(row=2, column=0, sticky=W) #posicion en tabla y a la izquierda
mi_Entry3 = Entry(mi_Frame) #entrada texto usuario
mi_Entry3.grid(row=2, column=1) #posicion en tabla

mi_Label4 = Label(mi_Frame, text="Descripcion") #Creación del Label4
mi_Label4.grid(row=3, column=0, sticky=W) #posicion en tabla y a la izquierda
mi_Entry4 = Entry(mi_Frame) #entrada texto usuario
mi_Entry4.grid(row=3, column=1) #posicion en tabla

def callback():
    print("Nuevo Socio")
button1 = Button(mi_Frame, text="Alta") #boton con llamada
button1.grid(row=4, column=1) #posicion en tabla

def callback():
    print("Kinder Sorpresa")
button2 = Button(mi_Frame, text="Sorpresa") #boton con llamada
button2.grid(row=4, column=2) #posicion en tabla

raiz.mainloop()


"""
no logro poner el fondo purple para que ocupe el tamaño de las 3 columnas y cree 2 label vacios para ponerle purple pero al parecer no es asi.
tampoco logro hacer que los botones me den una respuesta, solo algunas veces se dejan clickear"""