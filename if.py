# DECLARACIÓN IF (CONDICIONLES)
# Esta declaración condicional nos permite realizar una acción si una condición se cumple
# u otra acción en caso de que no se cumpla


"""
EJEMPLO REAL:
Voy a salir,

SI hace calor,
    saldre en camiseta

SINO SI hace frio,
    saldré abrigado

SINO SI está lloviendo,
    llevaré paraguas

SINO
    me quedaré en casa
"""


si_es_hombre = False
eres_alto = False


print("ANTES DEL IF\n")

if si_es_hombre and eres_alto:
    print("Eres un hombre alto")
elif si_es_hombre and not eres_alto :
    print("Eres un hombre bajo")
elif not si_es_hombre and eres_alto:
    print("No eres un hombre, pero eres alto")
else:
    print("No eres un hombre, y tampoco eres alto")

print("\nFUERA DEL IF")


hombre = False
puto = False

if hombre and puto:
    print('es hombre pero parece puto')
elif puto or hombre:
    print('sos un putaso')
elif not puto and not hombre:
    print('seguro sos puto')

###########################################################################

# Si no se quisiera ejecutar ninguna orden en alguno de los bloques, el bloque de órdenes
# debe contener al menos la instrucción pass (esta orden le dice a Python que no tiene que hacer nada).

edad = int(input("¿Cuántos años tiene? "))
if edad < 120:
    pass
else:
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")

# Evidentemente este programa podría simplificarse cambiando la desigualdad.

edad = int(input("¿Cuántos años tiene? "))
if edad >= 120:
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")

###########################################################################

# UTILIZANDO CONDICIONALES Y COMPARACIONES


def mayor_edad(num):  # creamos esto para saber si es mayor de edad para futuras acciones
    if num >= 18:
        return True
    else:
        return False


edad = input("Ingresa tu edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


#tambien se podria hacer el print directo ahorrando True y False, pero no almacenariamos si es mayor de edad para futuras acciones

def mayor_edad(num):
    if num >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")


edad = int(input("Ingresa tu edad: "))
mayor_edad(edad)


###########################################################################


def mayor_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


numero = mayor_numero(99, 556, 300)
print(numero)


###########################################################################

# Declaraciones largas

A = 1
B = 2
C = 3
print('spam' * 3)  # spamspamspam
if A == 1 and B == 2 and C == 3:
    print('REPETIR ' * 3)  # REPETIR REPETIR REPETIR

if (A == 1 and
    B == 2 and
    C == 3):
    print('REPETIR ' * 3)  # REPETIR REPETIR REPETIR

###########################################################################

# Uso de “in” dentro de la condición

nombre = 'juan'
if 'an' in 'juan':
    print('a')  # a
    if nombre.endswith('n'):
        nombre *= 2
        print(nombre)  # juanjuan

###########################################################################

# Si tiene problemas para recordar la orden, recuerde que cuando la lee en voz alta (casi) dice lo que quiere decir.
# Por ejemplo, x = 4 if b > 8 else 9 se lee en voz alta como x will be 4 if b is greater than 8 otherwise 9.




