# SENTENCIAS BREAK Y CONTINUE
# Las sentencias break y continue nos permiten manejar el flujo
# de la información en un bucle.


dias = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
]

for dia in dias:
    if dia == "jueves":  # se frena cuando llega a jueves
        break
    print(dia)
"""
lunes
martes
miércoles"""

for dia in dias:
    if dia == "jueves":  # llega al jueves y lo salta
        continue
    print(dia)
"""
lunes
martes
miércoles
lunes
martes
miércoles
viernes
sábado
domingo"""

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

a = []
for i in range(0, 11, 2):
	a.append(i)
print(a)