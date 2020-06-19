# CONJUNTOS o SET
# Los conjuntos son una colección de datos pero que no se ecuentra ordenada.

# [] Listas - () Tuplas - {} Conjuntos y Diccionarios

conjunto = {"Hola", 2, False, 48.03, True}

print(conjunto) #muestra {False, 'Hola', 2, True, 48.03}

conjunto.add(True) #muestra {False, 'Hola', 2, True, 48.03} no muestra mas de una vez el mismo elemento, hay dos True

print(conjunto)

conjunto.remove(True) #muestra {False, 'Hola', 2, 48.03} porque removio el True por mas que sean dos, porque es el mismo elemento

print(conjunto)

print()
#definir conjunto de datos que no queremos ordenar, que no llevan indice
colores_tupla = ('red', 'green, blue') #todos estos tienen su indice 0, 1, 2
colores_set = {'red', 'green, blue'} #no tienen indice
print(colores_tupla)
print(colores_set)
print(type(colores_set)) #muestra <type 'set'>
print(colores_set) #muestra set(['green, blue', 'red'])

#ver si esta red
print('red' in colores_set) #muestra True

#agregar color
colores_set.add('violet') #agrega color violeta
print(colores_set) #muestra set(['green, blue', 'red', 'violet'])

#borrar color
colores_set.remove('red') #borro color red
print(colores_set) #muestra set(['green, blue', 'violet'])

#vaciar el set
colores_set.clear()
print(colores_set)

"""borrar el set
del colores_set
print(colores_set)"""

print()

# Crear set
F = {1, 2, 3, 4, 5, 3}
print(F) # no muestra el segundo 3 {1, 2, 3, 4, 5}
print(len(F)) #muestra 5 porque solo cuenta una vez el numero 3

print()
# Crear set
F = {1, 2, 3, 4, 5, 3}
F1 = {10, 2, 13, 4, 15, 3, 1}
F2 = {10, 2, 13, 4, 15, 3}

print(F & F1) # Crear Intersección {1, 2, 3, 4}
print(F | F1) # Crear Unión {1, 2, 3, 4, 5, 10, 13, 15}
print(F - F1) # Crear Diferencia {5}
print(F1 > F2 ) # Crear Superset F1 es un set que contiene todos los elementos de F2 y más. Muestra True

print()

# Remover duplicados de una Lista
L = [1, 2, 1, 3, 2, 4, 5]
set(L) #pasar la lista a set para remover
print(L)
L = list(set(L)) # remueve duplicados
print(L)

print()

#Ejemplo aplicacion de set en un club de 2 deportes
socios = ["Juan", "Pedro", "Susana", "Anna", "Sofía", "Pablo"]
ajedrez = ["Pedro", "Susana", "Anna", "Sofía", "Pablo"]
natacion = ["Juan", "Pedro", "Susana"]
resultado = set(ajedrez).intersection(natacion)
print(resultado) # muestra {'Susana', 'Pedro'}
print(type(resultado)) # muestra <class 'set'>

