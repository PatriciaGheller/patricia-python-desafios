"""Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas."""

dis = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {:.2f} km. '.format(dis))
if dis <=200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print('O valor da passagem é R${:.2f}'.format(preco))







