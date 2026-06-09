"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas não atigiram a maioridade e quantas ja são maiores."""
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input(' Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >=21:
        totalmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))




