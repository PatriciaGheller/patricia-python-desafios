"""Faça um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---------{}ªPESSOA---------'.format(p))
    nome = str(input('Qual é o seu nome? ')).strip()
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual é o seu sexo? [M/F] ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
        print('=' * 20)
    mediaidade = somaidade / 4
print('A media de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))




