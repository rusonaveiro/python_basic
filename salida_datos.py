# imprimir varios resultados juntos separados por espacios u otros tipos de caracteres:
x = 1
y = 2
z = ['juan']
print(x, y, z, sep=' ') # muestra 1 2 ['juan']
print(x, y, z, sep=' , ') # muestra 1 , 2 , ['juan']

#agregar instrucción al final de cada línea, como una descripción, tabulación o salto de línea.
print(x, y, z, sep=' , ', end='!\n') # muestra 1 , 2 , ['juan']!

#############################################################################################
print()

#Secuencia de datos
seq = [1, 2, 3, 4] #lista

a, b, c, d = seq #asociamos una posición a una referencia
print(a, b, c, d) #muestra 1 2 3 4
print(a, b ,c ,d, sep=',') #muestra 1,2,3,4

a, *b = seq #asociar a un grupo de valores una lista
#el primer valor está asociado a la letra “a” y el resto a una lista llamada “b” anteponiendo un asterisco a la letra b
print(a, b, type(b)) #muestra 1 [2, 3, 4] <class 'list'>

# en lugar de una lista estemos trabajando con un string
a, *b = 'Manzana' # b crearía una lista de caracteres
print(a, b, type(b)) #muestra M ['a', 'n', 'z', 'a', 'n', 'a'] <class 'list'>

##############################################################################################
print()

# Formato literal (f-strings)
nombre = 'Pedro'
edad = 40
print(f'La edad de {nombre} es de {edad} años') # comenzar una cadena de texto con “f” o “F” antes de las comillas de apertura
# muestra La edad de Pedro es de 40 años


"""realizar columnas de datos, agregando luego de lo que estamos imprimiendo, 
dos puntos seguidos de la mínima cantidad de caracteres que queremos imprimir."""
nombre = 'Pedro'
edad = 40
print(f'{"fila":30}==>{nombre:10}{edad}') # muestra fila                          ==>Pedro     40


# especificar la cantidad de decimales luego de la coma de un número
valor = 3.141659
print(f'El valor redondeado a 3 dígitos luego de la coma queda: {valor:.3f}.')
# muestra El valor redondeado a 3 dígitos luego de la coma queda: 3.142.


# Formato con format()
#hacer referencia por posición utilizando números
votos = 42572654
voto_en_blanco = 43132495
porcentaje = (votos / (votos + voto_en_blanco)) *100
print('Los votos a favor son: {0} con un porcentaje de: {1:.2f}'.format(votos, porcentaje))
#muestra Los votos a favor son: 42572654 con un porcentaje de: 49.67
"""Notemos que las posiciones se comienzan a numerar desde 0 y que en particular el segundo parámetro 
posee un 1 (el cual representa la posición dentro de format()) seguido de dos puntos
y a continuación la cantidad de dígitos después de la coma (.2f)"""
print()

#############################################################################
print()

# pprint importar modulo para que se vea mas bonito el resultado en pantalla
import pprint

Juan = {
    'identificacion': {
        'nombre': 'Juan',
        'apellido': 'Garcia'
    },
    'edad': 24,
    'sueldo': 5000,
    'profesión': 'Pintor'
}
Susana = {
    'identificacion': {
        'nombre': 'Susana',
        'apellido': 'Gomez'
    },
    'edad':25,
    'sueldo': 6000,
    'profesión': 'Empleada'}
db = {}
db['Juan'] = Juan
db['Susana'] = Susana
print(db) #muestra apelotonado en una linea {'Juan': {'identificacion': {'nombre': 'Juan', 'apellido': 'Garcia'}, 'edad': 24, 'sueldo': 5000, 'profesión': 'Pintor'}, 'Susana': {'identificacion': {'nombre': 'Susana', 'apellido': 'Gomez'}, 'edad': 25, 'sueldo': 6000, 'profesión': 'Empleada'}}
print('------------------------------')
pprint.pprint(db)
"""muestra {'Juan': {'edad': 24,
          'identificacion': {'apellido': 'Garcia', 'nombre': 'Juan'},
          'profesión': 'Pintor',
          'sueldo': 5000},
 'Susana': {'edad': 25,
            'identificacion': {'apellido': 'Gomez', 'nombre': 'Susana'},
            'profesión': 'Empleada',
            'sueldo': 6000}}"""

#############################################################################
print()

# Date
import datetime
datetime.datetime.now()

print(datetime.datetime.utcnow()) #muestra 2020-05-22 08:59:03.376294
print(datetime.datetime.now()) #muestra 2020-05-22 10:59:03.377550
print(datetime.datetime.now().day) #muestra 22
print(datetime.datetime.now().month) #muestra 5
print(datetime.datetime.now().minute) #muestra 59
print(datetime.datetime.now().second) #muestra 3
print(datetime.datetime.now().microsecond) #muestra 377799
print(datetime.datetime.today().strftime("%H:%M:%S--%d/%m/%y")) #muestra 10:59:03--22/05/20

#Diferencia de fechas 1
actual = datetime.datetime.now()
anterior = datetime.datetime(1975, 9, 15, 0, 0, 0)
print(actual-anterior)

#Diferencia de fechas 2
hoy = datetime.date.today()
hace5 = datetime.timedelta(days=5)
print(hoy)
print(hace5)
print(hoy - hace5) #Resto 5 días

print(datetime.date.today()) #muestra 2020-04-30
#convierte minutos a horas
print(datetime.timedelta(minutes=70)) #muestra 1:10:00

#tambien puedo hacerlo de otra manera, importando solo timedelta de la biblioteca datetime
from datetime import timedelta, date
print(timedelta(minutes=80)) #muestra 1:20:00
#puedo importar la fecha (date) junyo al timedelta
print(date.today()) #muestra fecha de hoy2020-05-05
##############################################################################
