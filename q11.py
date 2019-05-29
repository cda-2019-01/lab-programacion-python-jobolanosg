##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', '') for row in file]
file = [row.split(' ') for row in file]

temp = []
i = 0
for f in file:
	temp.append([])
	for a in f:
		b = a.split(',')
		if(len(b) == 1):
			temp[i].append(b[0])
		else:
			temp[i].append(b)
	i += 1

for x in temp:
	print(x[0] + ',' + str(len(x[3])) + ',' + str(len(x[4])))
