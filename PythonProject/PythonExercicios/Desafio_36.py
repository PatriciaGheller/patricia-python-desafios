"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não poderá exceder 30% do salário ou então o emprestimo será negado. """

valor =float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos será pago? '))
prestacao = valor / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(valor, anos), end='')
print('o valor da prestação será de: R${:.2f} '.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONSEDIDO!')
else:
    print('Emprestimo NEGADO!')

