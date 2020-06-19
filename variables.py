# Una variable es un espacio en memoria capaz de almacenar información

# El operador de asignación es el simbolo = y nos permite asignar un valor a una variable

# Para asignar una variable lo hacemos de esta forma
numero = 10

# Podemos asignar varios valores a diferentes variables en una única linea
# separando los valores con comas
# Debe contener el mismo número de elementos antes y después del igual
numero1, numero2, numero3 = 1, 2, 3

x, book = 100, "I Robot"
print(x, book)  # muestra 100 I Robot

# Convenciones

book_name = "I Robot" # Snake case
bookName = "Digital fortress"  # Camel case
BookName = "asasasasasasasa"  # Pascal case

# constantes van con mayusculas y no cambian
PI = 3.14
MY_NAME = "Roberto"

# La función id() nos permite ver el identificador único de la variable
id(numero)

# La función del() nos permite eliminar de memoria una variable
del(numero)

# dir() nos permite ver todo el listado de nombres asignados
dir()

###########################################################################

"""Python distingue tres tipos de variables: 
las variables locales y dos tipos de variables libres (globales y no locales):
variables locales: las que pertenecen al ámbito de la subrutina (y que pueden ser accesibles a niveles inferiores)
variables globales: las que pertenecen al ámbito del programa principal.
variables no locales: las que pertenecen a un ámbito superior al de la subrutina, pero que no son globales.

Si el programa contiene solamente funciones que no contienen a su vez funciones, 
todas las variables libres son variables globales. Pero si el programa contiene una función que a su vez 
contiene una función, las variables libres de esas "subfunciones" pueden 
ser globales (si pertenecen al programa principal) o no locales (si pertenecen a la función)."""

# Local vs Global


def subrutina():
    a = 2  # 3ero La primera instrucción de la función asigna el valor 2 a la variable "a".
    print(a)  # 4to La segunda instrucción escribe el valor de la variable "a", es decir, 2.
    return  # 5to La instrucción return indica el final de la función y continúa la ejecución del programa tras la llamada a la función


a = 5  # 1ero La primera instrucción del programa asigna el valor 5 a la variable "a"
subrutina()  # 2do A continuación se llama a la función subrutina()
print(a)  # 6to La última instrucción del programa escribe de nuevo el valor de "a",
          # pero el valor que se escribe no es 2, sino 5, ya que la variable "a" del programa es distinta
          # de la variable "a" de la función, aunque se llamen igual.


# Otro Ejemplo

A = 5  # A es global


def sumemos(B):
    C = A + B  # B y C son locales a la función
    return C


c = sumemos(5)  # guardo resultado en variable c
print(c)

print(sumemos(5))  # solo imprimo sin guardar

##################################################################

# Variable se considera Libre porque no se le asigna valor en la función
# Para identificar explícitamente las variables globales y no locales se utilizan las palabras reservadas
# global y nonlocal. Las variables locales no necesitan identificación.

# Global libre (obtiene su valor del programa principal)


def subrutina():
    print(a)  # 3ero la variable "a" es libre puesto que no se le asigna valor. Su valor se busca en los niveles superiores, por orden
    return  # 4to indica el final de la función y continúa la ejecución del programa tras la llamada a la función.


a = 5  # 1ero La primera instrucción del programa asigna el valor 5 a la variable "a"

subrutina()  # 2do se llama a la función subrutina()
print(a)  # 5to escribe de nuevo el valor de "a", que sigue siendo 5 pues la función no ha modificado el valor de la variable.


###########################################################################

# No Local libre (porque obtiene su valor de una función intermedia)

def subrutina():
    def sub_subrutina():
        print(a)  # 6to Su valor se busca en los niveles superiores, por orden. Imprime 3. la variable "a" es una variable no local, porque su valor proviene de una función intermedia.
        return  # 5to indica el final de la función y continúa la ejecución del programa tras la llamada a la función.

    a = 3  # 3ero La primera instrucción de la función subrutina() asigna el valor 3 a la variable "a", así que esta variable "a" será una variable local.
    sub_subrutina()  # 4to A continuación se llama a la función sub_subrutina().
    print(a)  # 7mo La tercera instrucción de la función subrutina() escribe el valor de la variable local "a", es decir, 3.
    return  # 8vo indica el final de la función y continúa la ejecución del programa tras la llamada a la función.


a = 4  # 1ero asigna el valor 4 a la variable "a".

subrutina()  # 2do se llama a la función subrutina()
print(a)  # 9no La última instrucción del programa escribe el valor de la variable global "a", 4.

###########################################################################

# No uso de global

A = 5
B = 6


def nopisa():
    A = 10
    print('La variable A dentro de la función tiene por valor', A)  # La variable A dentro de la función tiene por valor 10
    print('B es global, por lo que puedo impirmirla acá', B)  # B es global, por lo que puedo impirmirla acá 6


nopisa()
print('La variable A fuera de la función tiene por valor', A)  # La variable A fuera de la función tiene por valor 5
print('',end='\n################\n')

##################################################################
"""
# Una variable no puede ser global y local a la vez

A = 5


def funcion():
    print(A)  # esta es global
    A = 10  # esta es local


funcion()  #da error
"""
##################################################################

# Variables declaradas Global. Se declara para usar la variable principal


def subrutina():
    global a  # 3ero Al declarar global la variable "a", la variable "a" de la función y la variable "a" del programa principal son la misma variable.
    print(a)  # 4to La segunda instrucción de la función escribe el valor de la variable "a", es decir, 5, puesto que se trata de la misma variable "a" del programa principal.
    a = 1    # 5to La siguiente instrucción cambia el valor de la variable "a" a 1.
    return  # 6to indica el final de la función y continúa la ejecución del programa tras la llamada a la función.


a = 5  # 1ero La primera instrucción del programa asigna el valor 5 a la variable "a".
subrutina()  # 2do llama a la función subrutina()
print(a)  # La última instrucción del programa escribe el valor de la variable global "a", que es ahora 1, puesto que la función ha modificado el valor de la variable.

##################################################################

# Variables declaradas No Local

def subrutina():
    def sub_subrutina():
        nonlocal a  # 5to Al declarar nonlocal la variable "a", Python busca en los niveles superiores, por orden, una variable que también se llame "a", que en este caso se encuentra en la función subrutina(). Python toma el valor de esa variable, es decir, 3.
        print(a)  # 6to escribe el valor de la variable no local "a", es decir, 3.
        a = 1  # 7mo cambia el valor de la variable "a" a 1.
        return  #8vo indica el final de la función y continúa la ejecución del programa tras la llamada a la función

    a = 3  # 3ero La primera instrucción de la función subrutina() asigna el valor 3 a la variable "a", así que esta variable "a" será una variable local.
    sub_subrutina()  # 4to llama a la función sub_subrutina().
    print(a)  # 9no La tercera instrucción de la función subrutina() escribe el valor de la variable local "a", es decir, 1.
    return  # 10mo indica el final de la función y continúa la ejecución del programa tras la llamada a la función.


a = 4  # 1ero asigna el valor 4 a la variable "a".
subrutina()  # 2do llama a la función subrutina().
print(a)  #11ero La última instrucción del programa escribe el valor de la variable global "a", que sigue siendo 4, puesto que ninguna función la ha modificado.

##################################################################


# Una variable no puede ser global y local a la vez - global

A = 5


def funcion():
    global A
    A = 10  # redefino A
    print(A) # esta es global  Muestra 10


funcion()
print(A)  # Muestra 10

##################################################################

# Cambiar Valor Global Desde Dentro (Evitar hacerlo)

ingreso = 0


def nuevoIngreso():
    global ingreso
    ingreso += 1
    print('Se ha realizado un nuevo ingreso', ingreso)

# cada vez que llamo a la función, redefino el valor de la variable "ingreso"


nuevoIngreso()  # Se ha realizado un nuevo ingreso 1
nuevoIngreso()  # Se ha realizado un nuevo ingreso 2
nuevoIngreso()  # Se ha realizado un nuevo ingreso 3
nuevoIngreso()  # Se ha realizado un nuevo ingreso 4
print(ingreso)  # 4

##################################################################

# Anidamiento y niveles – global vs nonlocal (Mierda inexplicable)
nivel0 = 0

def f1():
    nivel1 = 1
    def f2():
        nivel2 = 2
        print(nivel0, nivel1, nivel2)
    f2()
    print(nivel0, nivel1)
f1()
print(nivel0)

##################################################################