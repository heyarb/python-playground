frase = str(input("Digite algo: "))

print("O tipo primitivo desse valor é {}".format(type(frase)))
print("Só tem espaços? {}".format(frase.isspace()))
print("É um número? {}".format(frase.isnumeric()))
print("É alfabético? {}".format(frase.isalpha()))
print("É alfanumérico? {}".format(frase.isalnum()))
print("Esta em maiúsculas? {}".format(frase.isupper()))
print("Esta em minúsculas? {}".format(frase.islower()))
print("Esta capilatizado? {}".format(frase.istitle()))
