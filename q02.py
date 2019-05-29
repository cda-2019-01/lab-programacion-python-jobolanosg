##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', ' ') for row in file]
file = [row.split(',') for row in file]
file = [row[0].split(' ') for row in file[0:]]
temp = []
[temp.append(row[0]) for row in file]
letters = sorted(list(set(temp)))
temp=[(w, temp.count(w)) for w in letters]
for row in temp:
    print(row[0],row[1], sep=",")
