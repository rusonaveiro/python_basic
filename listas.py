# LISTAS
# Una lista es una colección de elementos, las listas están ordenadas, y son mutables.

# Crear Lista
F1 = [0, 1, 2]
F2 = F1 # F1 y F2 son el mismo objeto
# print(F2)

# Renombramos primer lista
F1[0]=4 # F1 y F2 son el mismo objeto
# print(F2)

# Renombramos primer lista # F1 y F2 son distintos objetos
F1 = [2, 1, 2]
print(F2)
input()

import copy
# Crear Lista
F1 = [0, 1, 2]
F2 = copy.copy(F1) # F1 y F2 son distintos objetos
print(F2)
input()

# De string a lista
J = 'Juan'
L = list(J)
print(L) #muestra ['J', 'u', 'a', 'n']
L[0] = 'P'
palabra = ''.join(L)
print(palabra) #muestra Puan
print(type(palabra)) #muestra <class 'str'>


numeros = [5, 2, 23, 55, 1, 9, 6]
frutas = ["Naranja", "Manzana", "Banana", "Kiwi", "Mandarina", "Uva", "Naranja", "Kiwi"]
print("LISTA ORIGINAL DE FRUTAS:")
print(frutas)
print()
# print(frutas[5])
# print(frutas[-6])
# print(frutas[1:5])

"""Métodos de listas (append – pop – extend – remove – insert)"""

peliculas = ["película1", "película2", "película3"]
print(peliculas) #muestra ['película1', 'película2', 'película3']
print(peliculas[0]) #muestra película1
print(len(peliculas)) #muestra 3

# Con append agregamos datos al final de una lista
peliculas.append("película4")
print(peliculas) #muestra ['película1', 'película2', 'película3', 'película4']

# Con pop removemos el último dato de una lista
peliculas.pop()
print(peliculas) #muestra ['película1', 'película2', 'película3']

# Con extend agregamos un grupo de datos al final de la lista
peliculas.extend(["película4", "película5"])
print(peliculas) #muestra ['película1', 'película2', 'película3', 'película4', 'película5']

# Con remove removemos un dato específico de la lista
peliculas.remove("película4")
print(peliculas) #muestra ['película1', 'película2', 'película3', 'película5']
# Con insert insertamos un dato en un lugar específico de la lista
peliculas.insert(0, "película0")
print(peliculas) #muestra ['película0', 'película1', 'película2', 'película3', 'película5']

# FUNCIONES DE LAS LISTAS
# https://docs.python.org/3/library/array.html
# list ,len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy
frutas2 = frutas.copy()
frutas3 = frutas
print(frutas2)

L = [] #Definición de lista vacía
L = [False]*10 #Lista con 10 elementos FALSE
L = [123, 'abc', {}] #Lista con tres elementos
L = ['Juan', 38, ['pintor', '5000']] #Listas de más de una dimensión
L =list('pera') #Genera una lista con las letras de pera L = [ 'p', 'e', 'r', 'a']
L=[i:j] #Longitud
len(L) #Cantidad de elementos de la lista
L * 2 #Genera una lista que posee los elementos
for x in L: print(x) #Recorre e imprime cada elementos de L
L.append(3) #Le agrega a la lista el número 3
L.extend([1, 2]) #Le agrega a L más de un elemento de lista
del L[i] #Elemento
del L[i:j] #Rango
L[i] = 3 #Asignar valor a componente i
L[i:j] = [4, 5] #Asigno valor a componente i:j
L = [x**2 for x in range(5)] #[0, 1, 4, 9, 16]
print(L[0]) #Imprimir el primer elemento desde la izquierda
print(L[-1]) #Imprimir el primer elemento desd
L=[[1,2][3,4]] #Matriz de 2*2
print(L[0].split()[-2]) #Juan

















