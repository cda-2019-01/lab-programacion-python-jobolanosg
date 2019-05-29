##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
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
	aux = 0
	for a in x[4]:
		aux += int(a.split(':')[1])
	print(x[0] + ',' + str(aux))
