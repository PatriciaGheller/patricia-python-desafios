'''Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros: o nome de um jogador  e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='<desconecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
    