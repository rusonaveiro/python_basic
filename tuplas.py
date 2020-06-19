# TUPLAS
# Las tuplas son una colección de elementos ordenados al igual que las listas
# pero las tuplas son inmutables.

coordenadas = (42.88, 55.16)
lista = [42.88, 55.16]

lista[1] = 5
print(lista)

print()
#definen datos que no cambian y llevan parentesis
#se usan en diccionarios o listas
x = (1, 2, 3)
print(x) #muestra (1, 2, 3)
print(type(x)) #muestra <type 'tuple'>

#datos que no cambian como los meses
months = ('January', 'Febreary')
print(months)

#ver todas las cosas que podemos hacer con esa tupla
print(dir(x))

#para que sea tupla debe tener mas de un dato, aunque sea una coma.
x = (1)
print(x) #imprime 1 sin parentesis
print(type(x)) #informa que es un entero y no una tupla <type 'int'>
x = (1,)
print(type(x)) #informa <type 'tuple'>

y = (1, 2, 3, 4, 5)
print(y[0]) #muestra el numero 1 que es el dato 0 que esta entre corchetes

A = x, y
print(A)
print(type(A))
# borrar la tupla del y print(y) muestra error porque ya borre y y no puede mostrarla

#latitud y longitud no cambia nunca por eso es tupla
#al ser diccionario va entre parentesis porque agrupa datos de una misma entidad
location = {
    (35.1212123, 34.59493): 'Tokio',
    (24.9594944, 12.00939): 'New York'
}
print()
print()

T1 = 1, 2, 3, 4, 5, 3
print(type(T1))
T2 = (1, 2, 3, 4, 5, 3)
print(type(T2))

T3 = T1, T2
print(type(T3)) #muestra ((1,), (1, 2, 3, 4, 5))
print(T3) #muestra <class 'tuple'>
print()

T4 = T3 + (6, 7) #determinar un elemento
print(T4) #muestra ((1, 2, 3, 4, 5, 3), (1, 2, 3, 4, 5, 3), 6, 7)
print(len(T4)) #muestra 4 elementos
print(T4[0]) # Posición de un elemento (1, 2, 3, 4, 5, 3)
print(T4.index(6)) # n° de veces que aparece un elemento
print(T4.count(7)) #muestra 1 porque solo una vez aparece el numero 7

print()
#tuplas que contienen 0 o 1 elementos
T5 = ()
T6 = 'Manzana',
print(len(T5)) #muestra 0
print(len(T6)) #muestra 1
print(T6) #muestra ('Manzana',)

##############################################################################
