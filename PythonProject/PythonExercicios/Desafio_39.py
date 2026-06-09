"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade.
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se ja passou do tempo do alistamento.
Seu programa deverá mostrar também o tempo que falta e o tempo que passou do prazo.
"""
from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos no ano {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade >18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))















