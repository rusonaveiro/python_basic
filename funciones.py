# FUNCIONES
# Una función es un bloque de código que incluye instrucciones para realizar una taréa específica

# 1ero Las Funciones se definen con def
# 2do Las Funciones se invocan con la palabra de la funcion con () y parametros dentro
# 3ero los parametros dentro del parentesis se llaman Atributos


# Palabras que no se pueden usar para definir funcion
import builtins
print(dir(builtins))

##############################################################################################


def saludar_usuario(par1, par2):
    print("Hola " + par2 + " tienes " + par1 + " años")  # Hola Marcos tienes 35 años
    print("Adios")  # Adios


print("primero")
saludar_usuario("35", "Marcos")  # Hola Marcos tienes 35 años
print("ultimo")

##############################################################################################

# RETURN
# La declaración Return nos permite recibir datos de una función


def multiplicar(num1, num2):
    return num1 * num2


res_multi = multiplicar(2, 10)
print(res_multi)


# otro ejemplo:

def add(numero1, numero2):
    return numero1 + numero2


print(add(10, 30))  # muestra 40


# otro ejemplo mas:


def pantalla(insulto):
    return insulto


a = pantalla("forro del orto")  # guardo resultado en variable a
print(a)

##############################################################################################

# definir 2 funciones para modulo fmath

# sumar

def add(n1, n2):
    print(n1 + n2)


# restar
def substract(n1, n2):
    print(n1 - n2)
"""
# importar el modulo fmath que cree para sumas y restas
import fmath
fmath.add(1, 2)  # muestra 3, porque suma 1 + 2
fmath.substract(80, 70)  # muestra 3, porque resta 80 y 70

# otra opcion para importar, asi no llamo al modulo, no pongo fmath delante
from fmath import add, substract
add(1, 2)  # muestra 3, porque suma 1 + 2
substract(80, 70)  # muestra 3, porque resta 80 y 70"""

##############################################################################################

# funciones que vienen en python print, dir, type

# poner def delante convierte palabras a funciones como son print(), dir() o type()


def hello():
    print('hello world')  # no muestra nada


hello()  # muestra hello world


# otro Ejemplo


def hello(name):
    print('hola ' + name)  # unir o concatenar strings dejando espacio en la comilla final para generar espacio entre las palabras


hello('Diego')  # muestra hola Diego

##############################################################################################

# si no asigna nombre la fc hello le pondrá 'persona'
def hello(name='persona'):
    print('hola ' + name)


hello()  # muestra hola persona

##############################################################################################

# fc lambda (NO LA ENTIENDO)

add = lambda numero1, numero2: numero1 + numero2 #hace todo en una sola linea
print(add(20, 30)) #muestra 50

##############################################################################################

# Uso de Yield
# Funciona de manera similar al return pero yield conserva
# la iteración del bucle para la siguiente vez que se le invoque


def contador_yield1(max):
    n = 0
    while n < max:
        yield n
        n += 1


d = contador_yield1(3)

print(d)  # muestra <generator object contador_yield1 at 0x10290af90>
print(next(d))  # muestra 0
print(next(d))  # muestra 1
print(next(d))  # muestra 2
print('', end='\n################\n')
"""al imprimir d obtenemos una referencia al objeto creado, y luego 
con el uso de next, tenemos acceso a las salidas retornadas por yield, 
en donde cada vez que se invoca a la función con el uso de next() 
obtenemos un registro de que recuerda el valor retornado la vez anterior 
(esto podría ser utilizado para contar cuántas veces un usuario 
ha realizado alguna actividad mientras está logueado)"""

# Diferencia entre return que trabaja con bloques a Yield que almacena uno a uno


def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num = num + 1
    return miLista


print(generaPares(10))  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

#################


def generaPares(limite):
    num = 1
    # miLista = [] No la necesito porque tengo objeto iterable que almacena en estado de suspension
    while num < limite:
        # miLista.append(num*2) # no tengo lista a quien anexar numeros
        yield num*2
        num = num + 1
    # return miLista
# print(generaPares(10))  # [2, 4, 6, 8, 10, 12, 14, 16, 18]
devuelvePares = generaPares(10)  # almacena el objeto iterable uno en uno

for i in devuelvePares:
    print(i)
"""
2
4
6
8
10
12
14
16
18
"""

##################################################################
##################################################################

# Funciones - Sintaxis de asignación de argumentos

# Argumentos Mutables e Inmutables

def modificar(a, b):
    a = 2
    b[0] = "Manzana"  # modifica el elemento 0 de la lista, reemplaza el 1 por manzana


A = 1
L = [1, 2]
modificar(A, L)
print('', end='\n################\n')
print(A, L)  # Imprime 1 ['Manzana', 2], el 1 no es mutable por eso no se modifica

###############################################

# Asignación por nombre

# Por posición

def f(x, y, z):
    print(x, y, z)  # 1 2 3
f(1, 2, 3)
print('', end='\n################\n')


# Por nombre

def f(x, y, z):
    print(x,y,z)  # 1 2 3
f(z=3, y=2, x=1)
print('', end='\n################\n')


# Por mixto - primero de izquierda a derecha y luego por nombre

def f(x, y, z):
    print(x, y, z)
f(1, z=3, y=2)

###############################################

#  Argumentos Por Defecto

def f(a, b=2, c=3):
    print(a, b, c)  # 1 2 3
f(1)

###############################################

# Uso de * y **

# “pepe” es Tupla
# “*pepe” es Lista
# "**pepe" es Diccionario


def f(a, *pepe):  # datos pasados como Lista
    print("Tupla de valores: ", pepe)  # Tupla de valores:  (1, 2, 'Manzana')
    print("Lista de valores: ", *pepe)  # Lista de valores:  1 2 Manzana
    for argumento in pepe:
        print("Elemento de la tupla: ", argumento)  # Elemento de la tupla:  1
                                                    # Elemento de la tupla:  2
                                                    # Elemento de la tupla:  Manzana


f(0, 1, 2, "Manzana")
print('', end='\n################\n')


# para ver los elementos como lista deberia meterlos en una lista vacia A

A = []
def f(a, *args):

    for argumento in args:

        A.append(argumento)  # agrega los elemtentos dentro de lista vacia A

f(0, 1, 2, "Manzana")

print(A)  # Imprime la lista [1, 2, 'Manzana']

print()


def funcion(**pepe):
    if pepe is not None:  #ACLARACION
        for clave, valor in pepe.items():
            print("%s == %s" %(clave, valor))


funcion(nombre="Juan", edad=1, sexo="Masculino")
print("----------------------------------")

""" ACLARACION En el caso de que tomes más de un tipo de parámetros, así: def funcion(*args, **kwargs):
Podría darse que no pases elementos que sean tomados por el diccionario y por lo tanto no ingresaría en el if"""


def funcion(a, *tita, **rodesia):
    print(a, tita, rodesia)
    print("-----------")
    print(a)
    print("-----------")
    print(tita)
    print("-----------")
    if rodesia is not None:
        for clave, valor in rodesia.items():
            print( "%s == %s" %(clave, valor))


funcion(1, 2, 3, nombre="Juan", edad=1, sexo="Masculino")

###############################################

# Recursividad o Recurrencia


def misuma(L):
    print(L)  # 1ero imprime [1, 2, 3, 4, 5] # 2do BUCLE imprime [2, 3, 4, 5] # 3er BUCLE imprime [3, 4, 5]
    if not L:  # 2do se fija que no este vacía(no lo está) por lo que va al else
        return 0
    else:
        return L[0] + misuma(L[1:])  # 3ero toma el primer elemento de la lista (el 1) y lo retiene y manda lo que queda [2, 3, 4, 5] como argumento de la función misuma.
                                     # 2do BUCLE se guarda el 2 y manda el [3, 4, 5] al 3er BUCLE y asi sucesivamente
                                     # Uiltimo momento suma los numero atrapados metiendolos en misuma
"""
Que pasa en el else:
L = inicia dando 1, 
    primer bucle da 2, 
    segundo da 3, 
    tercero da 4, 
    cuarto da 5 
    ultimo da 0 por el if ya que no es lista
misuma = primer bucle da [2, 3, 4, 5]
        segundo da [3, 4, 5]
        tercero da [4, 5]
        cuarto da  [5]
"""

print(misuma([1, 2, 3, 4, 5]))  # imprime 15, que es la suma generada en return L[0] + misuma(L[1:]) ????
# “misuma” tiene un return por eso no puedo crear una variable misuma=[1,2,3,4] el sistema espera poder “retornarlo” a algún lado
# Con el print lo que hace es: lo que me retornas no lo guardes en ningún lado, solamente imprímemelo en pantalla
# Sino tendrías que hacer:
# Suma = misuma([1, 2, 3, 4, 5]) # Ahí le decís: el return guárdalo en Suma y después mostrármelo con el print de abajo
# print(Suma)
# Para evitar crear una variable une los 2 pasos en 1 solo print(misuma([1, 2, 3, 4, 5]))
# es porque no le interesa para el código tener guardado ese return en ningún lado.
# Si vos en tu código después lo vas a modificar lo que te devolvió ahí si lo guardas en variable

""" Cuando en el 3ero retiene el numero 5, la lista quedara vacia.
La imprime, se fija que no este vacia (lo está) por lo que en lugar del ir al else retorna 0 
y empieza a "subir" sumando los números que fue conservando en las ejecuciones "superiores" de la función, 
es decir: 1 + 2 + 3 + 4  + 5 + 0
Finalmente la función inicial de misuma() esta dentro de un print por lo que imprime el 15 final."""
print("---------")
print()

# esta mierda es lo mismo pero en formato ternario
"""
def miSuma(L):
return 0 if not L else L[0] + miSuma(L[1:])
print(miSuma([1, 2, 3, 4, 5]))"""
print("---------")

# Recursividad indirecta (utilizar una segunda funcion)

def misuma(L):
    if not L:
        return 0
    return novacia(L)  # llama a otra función que llama a misuma

def novacia(L):
    return L[0] + misuma(L[1:])  # Recursividad indirecta

print(misuma([1.1, 2.2, 3.3, 4.4]))  # imprime 11.0

print("---------")


# Recursividad vs loop.

L = [1, 2, 3, 4, 5]
suma = 0

while L:
    suma += L[0]  # es 0 (suma) + 1 (L[0]) y lo guarda en suma
    L = L[1:5]  # ahora suve con el 2 (L[1]) para sumarselo a 1 (suma)
print(suma)  # imprime 15

print("---------")

##############################################################################

# Datos de la función.


def misuma(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + misuma(L[1:])


print(misuma([1, 2, 3, 4, 5]))

print('', end='\n################\n')
print(misuma.__name__)  # Obtengo el nombre
print('', end='\n################\n')
print(dir(misuma))  # Obtengo sus atributos
print('', end='\n################\n')
print(misuma.__code__)  # Datos de la función
print('', end='\n################\n')
print(dir(misuma.__code__))  # Datos de la función
print('', end='\n################\n')
print(misuma.__code__.co_varnames)  # Nombre de variables utilizadas
print('', end='\n################\n')
print(misuma.__code__.co_argcount)  # Cantidad de argumentos

##############################################################################

# Uso de __anotations__


def func1(a, b, c):  # sin anotaciones
    return a + b + c


pepa = func1(1, 2, 3)  # Imprime 6
print(pepa)
# otra opcion es evitar la variable con el print directo
print(func1(1, 2, 3))  # si no pongo el print no veo el resultado porque return no muestra solo almacena
print('',end='\n################\n')


def func2(a: 'spam', b: (1, 10), c: float) -> int:  #Con -> índico un comentario para el tipo de retorno de la función
    return a + b + c

print(func2(1, 2, 3))  # Imprime 6
print(func2.__annotations__)  # Imprime {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
# Con __annotations__ recupero los comentarios
print('',end='\n################\n')


# También puedo usar valores por defecto junto con los comentarios

def func3(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func3(1, 2, 3))
print(func3.__annotations__)
# no se porque pero imprime lo mismo que el caso anterior

##############################################################################

# Función Lambda
# Son funciones anónimas que se ejecutan en una linea es decir solo pueden tener una expresión

def func1(a, b, c):
    return a + b + c


print(func1(1, 2, 3))  # Imprime 6

# En Lambda seria asi:
func2 = lambda a, b, c: a + b + c # es como hacer enroque entre def y func2 pero a def le pone el nombre de lambda
print(func2(1, 2, 3))

# La lista de argumentos no está entre paréntesis.
# La palabra reservada return está implícita, ya que la función entera debe ser una única expresión.
# La función no tiene nombre, pero puede ser llamada mediante la variable a que se ha asignado.
# Es posible definir una función lambda sin asignarla a una variable, pero su aplicación no es muy útil.

func3 = (lambda a=4, b=5, c=6: a + b + c)
print(func3(1, 2, 3))

##############################################################################################