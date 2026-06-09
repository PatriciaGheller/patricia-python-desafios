#Crie um algoritmo que mostre o preço de um produto com 10% de desconto no pagamento à vista e 10% de aumento para pagamento à prazo.

produto = float(input('Qual é o preço do produto?'))
avista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 10 / 100)

print('O preco do produto à vista fica em R${:.2f}, e à prazo R${:.2f}'.format(avista, parcelado))



