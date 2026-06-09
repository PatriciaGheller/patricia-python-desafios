"""Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
A)Apenas os 5 primeiros colocados.
B)Os últimos 4 colocados da tabela.
C)Uma lista com os times em ordem alfabética.
D)Em que posição na tabela esta o time da Chapecoense."""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético - PR', 'Bahia',
         'São Paulo', 'Fluminence', 'Sporte Recife ',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético GO')
#print(f'LISTA DE TIMES: {times}')
print('LISTA DE TIMES DO BRASILEIRÃO')
for t in times:
    print('-=' * 15)
    print(t)
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição.')