'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    # O itemgetter é usado para ordenar o dicionário pelo valor, ou seja, pelo resultado do dado.
    # O reverse=True é usado para ordenar em ordem decrescente, ou seja, do maior para o menor.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  == Ranking dos jogadores ==')
print('-=' * 20)
for i, v in enumerate(ranking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
