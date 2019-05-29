##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', ' ') for row in file]
file = [row.split(',') for row in file]
file = [row[0].split(' ') for row in file[0:]]
## Imprima la suma de la columna 2 por cada letra
temp = {}
for x in file:
	temp[x[0]] = 0
for x in file:
	temp[x[0]] = temp[x[0]] + int(x[1])
for y in sorted(temp.keys()):
    print(y + ',' + str(temp[y]))
