from math import hypot

cateto1 = int(input('Digite o valor do cateto 1: '))
cateto2 = int(input('Digite o valor do cateto 2: '))

print('A hipotenusa dos catetos {} e {} é igual a: {}'.format(cateto1, cateto2, hypot(cateto1, cateto2)))