# FOR
# Nos permite recorrer una colección de valores

for indice in range(5):
    for indice2 in range(3):  # primero imprime cada rango del indice2 0 al 3 dentro del indice 0, luego lo hace con el indice 1 y asi sucesivamente
        print(indice, indice2)
"""
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2"""

##################################################################

dias = ["lu", "ma", "mi"]

for dia in dias:
    print(dia)
"""
lu
ma
mi
"""

##################################################################

dias = {'lu': 'lunes', 'mar': 'martes', 'mier': 'miercoles'}

for clave, valor in dias.items():  # llamar a item para que nos de llave y valor
    print(valor)
"""
lunes
martes
miercoles
"""

##################################################################

for indice in range(2, 11, 2):  # primer parametro es start, luego finish y el ultimo son los step
    print(indice)
"""
2
4
6
8
10
"""

##################################################################

for indice in range(6):
    if indice == 3:
        print("Ganaste el sorteo")
    else:
        print("No eres ganador")

print(len(dias))
"""
No eres ganador
No eres ganador
No eres ganador
Ganaste el sorteo
No eres ganador
No eres ganador
3
"""

##################################################################

# lista Dentro De Lista con for

# Definir listas
Juan = ['Juan Garcia', 24, 5000, 'Pintor']
Susana = ['Susana Gomez', 25, 6000, 'Empleada']
print(Juan[0]) #  Juan Garcia es el indice 0

# Definir lista como Base de datos
personas = [Juan, Susana]

# Imprimo elementos de la lista de base de datos
for lista in personas:
    print(lista) #  ['Juan Garcia', 24, 5000, 'Pintor'] ['Susana Gomez', 25, 6000, 'Empleada']
print('------------------------------')

# Imprimo los apellidos y les doy aumento del 20%
for lista in personas:
    print((lista[0].split()[-1]))  # 1era lista Juan Garcia es indice 0 y nos pide -1 dando el apellido, hace lo mismo con la 2da lista
    lista[2] *= 1.20  # 1era lista indice 2 es el 5000 y lo multiplica por 1.2, lo misma hace con la 2da lista con el 6000
for lista in personas:
    print(lista)  # ['Juan Garcia', 24, 6000.0, 'Pintor'] ['Susana Gomez', 25, 7200.0, 'Empleada']
print('------------------------------')

# Agregamos un registro a la lista de base de datos
personas.append(['Pedro', 37, 7000, 'Plomero'])
for lista in personas:
    print(lista)  # ['Juan Garcia', 24, 6000.0, 'Pintor'] ['Susana Gomez', 25, 7200.0, 'Empleada'] ['Pedro', 37, 7000, 'Plomero']
print('------------------------------')

##################################################################

# Listas dentro de listas (for if else) - isinstance()

lista = ["caja1", "caja2", "caja3", ["frasco1", "frasco2", "frasco3", ["porotos", "lentejas", "garbanzos"]]]

# imprimimos la lista con 4 elementos caja1 caja2 caja3 y una lista
print(lista)  # ['caja1', 'caja2', 'caja3', ['frasco1', 'frasco2', 'frasco3', ['porotos', 'lentejas', 'garbanzos']]]
print('', end='\n################\n')

# imprimimos elementos de primer nivel
for a in lista:  # a seria una variable que se le asigna a cada objeto cuando pasa
    print(a)  # pasa el primer objeto caja1 y lo imprime, y asi hace con los 3 siguientes caja2 caja3 y una lista
print('', end='\n################\n')
"""Imprime cada objeto cuando finaliza cada ciclo
caja1
caja2
caja3
a ['frasco1', 'frasco2', 'frasco3', ['porotos', 'lentejas', 'garbanzos']]"""


# imprimimos elementos de primer y segundo nivel
# con el isinstance(objeto, tipo de objeto) veo si el objeto de la lista no es una lista
# si es una lista recorro la lista y sino paso al siguiente elemento
# lista = ["caja1", "caja2", "caja3", ["frasco1", "frasco2", "frasco3", ["porotos", "lentejas", "garbanzos"]]]
for a in lista:  # a seria una variable que se le asigna a cada objeto cuando pasa por aca
    if isinstance(a, list):  # si el objeto es una lista
        for b in a:  # el primer objeto de la lista anidada se imprime con print(b)
            print(b)
    else:
        print(a)  # si el objeto NO es una lista lo imprime
print('', end='\n################\n')
"""Imprime cada objeto cuando finaliza cada ciclo
caja1
caja2
caja3
frasco1
frasco2
frasco3
['porotos', 'lentejas', 'garbanzos']"""

# imprimimos elementos de primer y segundo y tercer nivel
# lista = ["caja1", "caja2", "caja3", ["frasco1", "frasco2", "frasco3", ["porotos", "lentejas", "garbanzos"]]]
for a in lista:
    if isinstance(a, list):
        for b in a:
            if isinstance(b, list):
                for c in b:
                    print(c)
            else:
                print(b)
    else:
        print(a)
"""Imprime cada objeto cuando finaliza cada ciclo
caja1
caja2
caja3
frasco1
frasco2
frasco3
porotos
lentejas
garbanzos"""


lista = ["Avion", ["Pasajero", "Asafata"], "Auto"]

for objeto in lista:
    print(objeto)
"""Imprime cada objeto por ciclo
Avion
['Pasajero', 'Asafata']
Auto"""

for objeto in lista:  # entra avion
    if isinstance(objeto, list):  # si avion es una lista imprime avion
        print(objeto)
    else:
        print(objeto)
"""Imprime cada objeto por ciclo
Avion
['Pasajero', 'Asafata']
Auto"""
print()

#lista = ["Avion", ["Pasajero", "Azafata"], "Auto"]
for objeto in lista:
    if isinstance(objeto, list):
        for anidado in objeto:
            print(anidado)
    else:
        print(objeto)
"""Imprime cada objeto por ciclo
Avion 
Pasajero
Azafata
Auto"""
print()

lista = ["Avion", ["Pasajero", "Azafata", ["piloto", "copiloto"]], "Auto"]
for objeto in lista:
    if isinstance(objeto, list):  # llega ["Pasajero", "Azafata", ["piloto", "copiloto"]] y es un objeto lista
        for anidado in objeto:  # pasajero es anidado en un objeto lista
            if isinstance(anidado, list):  # pasajero no es una lista, es objeto 'dentro de la lista'
                for recontra_anidado in anidado:
                    print(recontra_anidado)
            else:
                print(anidado)  # pasajero se imprime
    else:
        print(objeto)


# lista = ["Avion", ["Pasajero", "Azafata", ["piloto", "copiloto"]], "Auto"]
for objeto in lista:
    if isinstance(objeto, list):
        for anidado in objeto:
            if isinstance(anidado, list):
                for recontra_anidado in anidado:
                    print(recontra_anidado)  # piloto
            else:
                print(anidado)
    else:
        print(objeto)
"""Imprime cada objeto por ciclo
Avion
Pasajero
Asafata
piloto
copiloto
Auto"""

##################################################################
print()

# Recursividad (Ahorrar código con funciones)
lista = ["Avion", ["Pasajero", "Azafata"], "Auto"]

# imprimimos la lista
def recorrerLista(unoauno):
    for objeto in unoauno:
        if isinstance(objeto, list):
            recorrerLista(objeto)
        else:
            print(objeto)
recorrerLista(lista)
"""Muestra
Avion
Pasajero
Azafata
Auto
"""

##################################################################
print()

# Optimizando el código
# Podemos optimizar nuestro código si ahora agregamos un segundo parámetro a la función
# que imprima una separación extra por cada nivel de la lista
"""
#lista = ["Avion", ["Pasajero", "Azafata", ["piloto", "copiloto"]], "Auto"]
lista = ["elemento1n1", "elemento2n1", "elemento3n1", ["elemento1n2", "elemento2n2", "elemento3n2", ["elemento1n3", "elemento2n3", "elemento3n3"]]]


def recorrerLista(item, nivel):  # Agrego segundo parámetro
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print((''))
        print(x)
recorrerLista(lista)
"""
##################################################################
print()

# Optimizando aún más el código
"""Podría darse el caso en el cual una persona se olvide de agregar 
el parámetro que indica el nivel, en cuyo caso el programa daría un error. 
Para evitar esto le pasamos un valor por defecto al parámetro nivel, 
y si la persona se olvida de indicarlos al llamar a la función, el programa se seguiría ejecutando."""

#lista = ["Avion", ["Pasajero", "Azafata", ["piloto", "copiloto"]], "Auto"]
lista = ["elemento1n1", "elemento2n1", "elemento3n1", ["elemento1n2", "elemento2n2", "elemento3n2", ["elemento1n3", "elemento2n3", "elemento3n3"]]]
def recorrerLista(item, nivel=0):  # Agrego valor por defecto
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")  # Agrego indentación en lugar de saltos de línea
        print(x)
recorrerLista(lista)
"""Muestra
elemento1n1
elemento2n1
elemento3n1
	elemento1n2
	elemento2n2
	elemento3n2
		elemento1n3
		elemento2n3
		elemento3n3
['elemento1n3', 'elemento2n3', 'elemento3n3']
['elemento1n2', 'elemento2n2', 'elemento3n2', ['elemento1n3', 'elemento2n3', 'elemento3n3']]"""