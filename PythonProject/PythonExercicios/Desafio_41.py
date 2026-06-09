"""A confederação nacional de natação precisa de um programa que leia o ano
de nascimento de uma atleta e mostre sua categoria, de acordo com sua idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER"""

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MIRIM')
elif idade <=14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade <=19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: JUNIOR')
elif idade <=25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MASTER')



