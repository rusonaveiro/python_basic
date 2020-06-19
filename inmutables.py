# Inmutable
pipo = 10
print(id(pipo)) #imprime espacio de memoria 4328098752

pipo = 12
print(id(pipo)) #imprime espacio de memoria 4328098816

# Mutable
lista1 = ['manzana', 'naranja']
print(id(lista1)) #imprime espacio de memoria 4330857664
lista1.append('banana')
print(lista1)
print(id(lista1)) #imprime el mismo espacio de memoria 4330857664 por mas que modifique la lista

