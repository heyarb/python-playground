p = float(input("Qual o preço do produto? "))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(p, p-(p * 5 / 100)))
