# DICCIONARIOS
"""Los diccionarios son una colección de datos no ordenada, pero que
almacena sus datos utilizando una asignación (llave, valor)"""

# [] Listas - () Tuplas - {} Conjuntos y Diccionarios

# Crear diccionario
F = {'clave1': 'valor1', 'clave2':'valor2', 'claven':'valorn'}
print(F['clave1']) #muestra valor1

# Crear por asignación
J = {}
J['clave1'] = 'valor1'
J['clave2'] = 'valor2'
print(F['clave1']) #muestra valor1

# Crear mediante dict()
S = dict(clave1 = 'valor1', clave2 = 'valor2')
print(S['clave1']) #muestra valor1

# Crear mediante dict() y zip
P = dict(zip(['clave1', 'clave2'], ['valor1', 'valor2']))
print(P['clave1']) #muestra valor1
input()
##############################################################################

# Encadenamiento
F = {'nombre': {'primero':'Juan', 'segundo':'Marcelo'}, 'trabajo':['profesor','ingeniero']}
print(F) # {'nombre': {'primero': 'Juan', 'segundo': 'Marcelo'}, 'trabajo': ['profesor', 'ingeniero']}
print('nombre') #nombre
print(F['nombre']['primero']) #Juan

# Agregar elementos
F['trabajo'].append('pintor')
print(F) #{'nombre': {'primero': 'Juan', 'segundo': 'Marcelo'}, 'trabajo': ['profesor', 'ingeniero', 'pintor']}
input()
##############################################################################

"""Para definirlo junto con los miembros que va a contener, se encierra el listado de valores entre llaves,
las parejas de clave y valor se separan con comas, y la clave y el valor se separan con : """

punto = {'x': 2, 'y': 1, 'z': 4}

dias = {
    "lun": "Lunes",
    "mar": "Martes",
    "mie": "Miércoles",
    "jue": "Jueves",
    "vie": "Viernes",
    "sab": "Sabado",
    "dom": "Domingo"
}
print(dias["lun"])
##############################################################################

"""Para declararlo vacío y luego ingresar los valores, 
se lo declara como un par de llaves sin nada en medio, 
y luego se asignan valores directamente a los índices"""

materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

"""Para acceder al valor asociado a una determinada clave, 
se lo hace de la misma forma que con las listas, 
pero utilizando la clave elegida en lugar del índice"""

print(materias["lunes"]) # muestra Lunes [6103, 7540]
##############################################################################

# Pasar a lista
F = {'nombre': {'primero': 'Juan', 'segundo': 'Marcelo'}, 'trabajo': ['profesor', 'ingeniero']
}
P = list(F.keys())
print(P) #['nombre', 'trabajo']
S = list(F.values())
print(S) #[{'primero': 'Juan', 'segundo': 'Marcelo'}, ['profesor', 'ingeniero']]
input()
##############################################################################

D = { } #Diccionario vacío
D = { 'nombre: 'Juan', 'edad' = 39} #Dos ítems del diccionario
E = {'identificación': {'nombre': 'Juan', #Anidamiento
D = dict('nombre: 'Juan', 'edad' = 39) #Estructura alternativa
D = dict([('nombre', 'Juan'),('edad', 39)]) #Pares clave/valor
D = dict(zip(['clave1','clave2'],['valor1', 'valor2'])) #Crear lista con zip
D['identificación']['nombre'] #Indexado por identificación y nombre
'edad' in D #Chequear si un campo se encuentra en el diccionario
D.keys() #Todas las claves
D.values() #todos los valores
D.items() #Tuplas de todas las (clave, valor)
D.copy() #copiar
D.clear() #remueve todos los items
D.update(D2) #Agrego D2 a D
D.get(clave) #Obtiene el valor de una clave
D.pop(key) # Borra un elemento por su clave y retorna el valor
list(D.keys()) #Crea una lista que contiene las claves del diccionario
list(D.values()) #Crea una lista que contiene los valores del diccionario
list(D.items()) #Crea una lista que contiene las claves y los valores del diccionario
len(D) #Longitud
D[clave] = 42 #Agrega una nueva clave con su valor
##############################################################################






















