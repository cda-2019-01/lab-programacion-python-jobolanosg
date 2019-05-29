##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,9
## bbb,0,9
## ccc,0,9
## ddd,0,9
## eee,0,7
## fff,0,9
## ggg,0,9
## hhh,0,9
## iii,0,9
## jjj,0,9
##
## Limpieza de la file
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
		temp[aux[0]] = []

for x in temp1:
	for y in x[4]:
		aux = y.split(':')
		temp[aux[0]].append(int(aux[1]))

for z in sorted(temp.keys()):  
     print(z + ',' + str(min(temp[z])) + ',' + str(max(temp[z])))
