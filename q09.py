##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', '') for row in file]
file = [row.split(' ') for row in file]

temp1 = file
temp = {}

for x in temp1:
	temp[x[1]] = []

for x in temp1:
	temp[x[1]].append(x[0])

temp2 = {}

for y in sorted(temp.items()):
	aux = set(y[1])
	aux = list(aux)
	temp2[y[0]] = sorted(aux)

for z in sorted(temp2.items()):
	print(z)
