"""Melhore o jogo do DESAFIO028 onde o computador vai 'pensar'
em um número entre 0 e 10.Só que agora o jogador vai tentar advinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer."""
from random import randint
from time import sleep
computador = randint(0, 10) #Computador sorteia um número
print('-=-'*20)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
print('-=-'*20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))#Jogador tenta advinhar
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))







