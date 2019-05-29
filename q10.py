##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', '') for row in file]
file = [row.split(' ') for row in file]

temp1 = []
i = 0
for f in file:
	temp1.append([])
	for a in f:
		b = a.split(',')
		if(len(b) == 1):
			temp1[i].append(b[0])
		else:
			temp1[i].append(b)
	i += 1

temp = {}

for x in temp1:
	for y in x[4]:
		aux = y.split(':')
		temp[aux[0]] = 0

for x in temp1:
	for y in x[4]:
		aux = y.split(':')
		temp[aux[0]] += 1

for z in sorted(temp):
	print(z + ',' + str(temp[z]))
