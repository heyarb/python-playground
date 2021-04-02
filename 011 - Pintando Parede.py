lar = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a Altura da sua parede? '))

metrosq = alt * lar

litros_tinta = metrosq / 2

print('Sua parede tem {}m de largura, {}m de altura e a área é {}m2 \nVocê vai precisar de {} litros de tinta para pintar sua parede'.format(lar, alt, metrosq, litros_tinta))