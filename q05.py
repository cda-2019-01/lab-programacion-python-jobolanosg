##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', ' ') for row in file]
file = [row.split(',') for row in file]
file = [row[0].split(' ') for row in file[0:]]
temp = {}
for x in file:
	temp[x[0]] = []
for x in file:
	temp[x[0]].append(int(x[1]))
for y in sorted(temp.keys()):  
     print(y + ',' + str(max(temp[y])) + ',' + str(min(temp[y])))
