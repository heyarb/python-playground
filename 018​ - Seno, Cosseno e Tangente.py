import math

ang = int(input('Digite o valor do angulo: '))

print('O seu angulo de {} corresponde aos valores de {} seno, {} cosseno e {} tangente'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))

# TODO
# Verificar como se passa para graus