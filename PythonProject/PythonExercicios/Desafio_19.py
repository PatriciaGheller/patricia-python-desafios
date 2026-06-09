#Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude a ele, lendo o nome delas e escrevendo o nome do escolhido.

from random import choice

n1 = str(input('Qual é o nome do primeiro aluno?'))
n2 = str(input('Qual é o nome do segundo aluno?'))
n3 = str(input('Qual é o nome do terceiro aluno?'))
n4 = str(input('Qual é o nome do quarto aluno?'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))




