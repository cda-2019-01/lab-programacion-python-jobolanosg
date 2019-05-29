##
## Imprima la suma de la segunda columna.
##
## Limpieza de la data
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', ' ') for row in file]
file = [row.split(',') for row in file]
file = [row[0].split(' ') for row in file[0:]]
## Realizar la suma e imprimir
temp = 0
temp = [int(x[1]) for x in file]
print(sum(temp))
