##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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
	for key in x[3]:
		if key in temp:
			temp[key] += int(x[1])
		else:
			temp[key] = int(x[1])


for key in sorted(temp.keys()):
     print(key + ',' + str(temp[key]))
