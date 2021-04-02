name = input(str('Write your full name: '))

print('Your name with lower characters: {}'.format(name.lower()))
print('Your name with upper characters: {}'.format(name.upper()))

name_without_space = len(name) - name.count(' ')
print('Characters number in your name without count spaces: {}'.format(name_without_space))

first_name = name.split()
print('Characters number in your first name: {}'.format(len(first_name[0])))
