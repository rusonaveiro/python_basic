# TRABAJAMOS CON CADENAS DE TEXTO

# Las cadenas pueden tratarse como listas
cadena = "Hola AcademiaCoder prueba"

# H o l a   A c a d e m  i  a  C  o  d  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

letra = cadena[5]
# print(letra)

letra = cadena[-18]
# print(letra)

letras = cadena[:2]
# print(letras)


# FUNCIONES DE LAS CADENAS DE TEXTO
# Tienen todas las funciones en https://docs.python.org/3/library/stdtypes.html#string-methods

modificada = cadena.split()
# print(modificada)

cadena_con_comas = "Marcos,Natalia,Tiziana,Benicio"
lista_nombres = cadena_con_comas.split(',')
# print(lista_nombres)


# UNIENDO VARIABLES Y CADENAS
alumnos = 2500
academia = "AcademiaCoder"

cadena = "Los " + str(alumnos) + " alumnos de " + academia + " son muy aplicados"
# print(cadena)

# .format
cadena = "Los {} alumnos de {} son muy aplicados".format(alumnos, academia)
# print(cadena)

cadena = "Los {a} alumnos de {b} son muy aplicados".format(a=alumnos, b=academia)
# print(cadena)

cadena = f"Los {alumnos} alumnos de {academia} son muy aplicados"
# print(cadena)


# INTRODUCIR TEXTO POR TECLADO
# la función de python que nos permite introducir texto es input()
# print("Ingresa tu Nombre:")
# nombre = input()

nombre = input("Ingresa tu Nombre: ")
print(f"El alumno se llama {nombre}")

##############################################################################

S = ' ' # String vacío
S = 's\np\ta' # Secuencia de escape \n es salto de línea y \t tabulación
S = b'abc' # Si al string lo precede una b se trata de información guardada como bits
S[i]  # Elemento i comenzando desde cero desde la izquierda
S[-i]  # Elemento i comenzando desde uno desde la derecha
S[i:j]  # Rango de i a j sin incluir j
S[i:]  # Rango a partir de i
S[i:-1]  # Rango a partir de i, sin incluir el último elemento
S[:]  # Selecciona todos los elementos
S[i: j: k]  # De i a j de a k
S[::-1]  # Lee S de derecha a izquierda
S[i: j:-1]  # Desde j a i (orden inverso)
'Pera'[1, 3]  # er
'Pera'[slice(1, 3)]  # er
len(S)  # Longitud
str(33)  # Convierte a string '33'
ord('s')  # Pasa a Unicode
chr(115)  # Obtiene carecter a partir de Unicode
"a %s ellos" % todos  # Da formato a expresión s = string, c = caracter, d=decimal, i=entero, f = flotante decimal
"a {0} ellos" .format(todos)  # Da formato por posición en python 2.6, 2.7 y 3.x
"a {valor} ellos" .format(valor = 1)  # Da formato por asignación
S.find('pa')  # Búsqueda de pa dentro de S Retorna ubicación de primer caracter
S.rstrip()  # Remueve espacio
S.replace('pa', 'xx')  # Reemplaza pa por xx
S.split(',')  # Separar según delimitador indicado
S.isdigit()  # Test de contenido
S.lower()  # Convierte S a minúscula
delim.join(S)  # Crea un string con los elementos de S separados por delim
' '.join(S)  # Crea un string con los elementos de S separados por espacio en blanco
for x in S: print(x)  # Iteración
'p' in perro  # Se fija si existe la letra p en el string perro
chars = list('manzana')  # chars = ['m', 'a', 'n', 'z', 'a', 'n', 'a']
chars.append('r')  # chars = ['m', 'a', 'n', 'z', 'a', 'n', 'a', 'r']
' '.join(chars)  # 'manzanar'

#############################################################################

# El operador "%" es usado para dar formato y fijar las variables juntos con una cadena con formato,
# el cual contiene el texto normal junto con "argumentos especificados", como los simbolos especiales "%s" y "%d".

# Esto imprime "Hola, Juan!"
nombre = "Juan"
print("Hola, %s!" % nombre)

# Usa dos o mas especificadores de argumento, usa un tupla (con parentesis):
# Esto imprime "John is 23 years old."
nombre = "John"
edad = 23
print("%s tiene %d años." % (nombre, edad))


