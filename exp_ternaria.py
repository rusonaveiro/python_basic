# EXPANDIDO

a = 4

if a == 4:
    b = 4
else:
    b = 5

print(b)
print()


# COMPRIMIDO
b = 4 if a==4 else 5

print(b)
print()

# Si tiene problemas para recordar la orden, recuerde que cuando la lee en voz alta (casi) dice lo que quiere decir.
# Por ejemplo, x = 4 if b > 8 else 9 se lee en voz alta como x will be 4 if b is greater than 8 otherwise 9.

a = 1
b = 2
print(1 if a > b else -1)  # Imprime -1
a = 2
b = 2
print(1 if a > b else -1 if a < b else 0)  # Imprime 0


a, b = 10, 20
min = a if a < b else b  # Copia el valor de a en min si (if) a es menor que b sino (else) copia b
print(min)  # Imprime 10





