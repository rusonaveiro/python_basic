from tkinter import *
formulario = Tk()
formulario.title("Tarea POO")

Label(formulario, text="Ingrese sus datos", fg="white", bg="purple", width=50).grid(row=0,column=0, columnspan=4)

##Creo la función para dar de alta las entradas
def entradas(valor, ancho, fila, columna):
    return Entry(formulario,width=ancho, textvariable=valor).grid(row=fila, column=columna)

##Defino las varaibles donde se guardará la entrada del usuario
titulo = StringVar()
ruta = StringVar()
descripcion = StringVar()


##Creo etiquetas del titulo, la ruta y la descripción
Label(formulario, text="Título").grid(row=1,column=0, sticky=W)
Label(formulario, text="Ruta").grid(row=2,column=0, sticky=W)
Label(formulario, text="Descripción").grid(row=3,column=0, sticky=W)

##Creo los widget de entrada a través de la función
etitulo = entradas(titulo,40,1,1)
eruta = entradas(ruta,40,2,1)
edescripcion = entradas(descripcion,40,3,1)

##Defino Lista donde estarán almacenados los diccionarios
bd=[]

registros=0
##Defino la funcion del boton alta
def b_alta():
    global registros
    bd.append({'Título':titulo.get(), 'ruta':ruta.get(), 'descripcion':descripcion.get()})
    print(registros)
    for a in bd:
        print(a)
    registros +=1

##Defino la función del boton sorpresa
indice = 0
def b_sorpresa():
    global indice
    colores = ['orange', 'blue', 'pink']
    if indice == 3:
        indice = 0
    formulario.config(bg=colores[indice])
    indice+=1


##Creo los 2 botones en el formulario
alta = Button(formulario, text="Alta", command=b_alta).grid(row=4,column=1)
sorpresa = Button(formulario, text="Sorpresa", command=b_sorpresa).grid(row=4, column=2)


mainloop()