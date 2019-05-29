##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
file = open('data.csv', 'r').readlines()
file = [row.replace('\t', ' ') for row in file]
file = [row.replace('\n', ' ') for row in file]
file = [row.split(',') for row in file]
file = [row[0].split(' ') for row in file[0:]]
temp = {}
for x in file:
	temp[(x[2].split('-')[1])] = 0
for x in file:
	temp[(x[2].split('-')[1])] = temp[(x[2].split('-')[1])] + 1
for y in sorted(temp.keys()):  
     print(y + ',' + str(temp[y]))
