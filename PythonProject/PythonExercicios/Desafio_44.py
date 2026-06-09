"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-À vista dinheiro/cheque:10% de desconto
-À vista no cartão:5% de desconto
-Em até 2x no cartão:Preço normal
-3x ou mais no cartão:20% de juros"""
from idlelib.colorizer import prog_group_name_to_tag

print('{:=^40}'.format(' \033[3;30;44mLOJAS PATRICIA\033[m'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2 x no cartão
[4] 3 x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
total = preco
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Obrigado por comprar na nossa loja!')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Obrigado por comprar na nossa loja!')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra vai ser parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra vai custar R${:.2f} no final.'.format(total))
    print('Obrigado por comprar na nossa loja!')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totslparc = int(input('Quantas parcelas? '))
    parcela = total / totslparc
    print('Sua compra vai ser parcelada em {}x de R${:.2f} COM JUROS'.format(totslparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Obrigado por comprar na nossa loja!')
else:
    total = preco
    print('Opção INVALIDA de pagamento. Tente novamente!')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Obrigado por comprar na nossa loja!')



