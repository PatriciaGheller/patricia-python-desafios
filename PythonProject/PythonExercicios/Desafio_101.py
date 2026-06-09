'''Crie um programa que tenha uma função chamada voto() 
que vai receber o ano de nascimento de uma pessoa como parâmetro.
A função vai retornar um valor literal 
indicando se uma pessoa tem voto NEGADO, 
OPCIONAL ou OBRIGATÓRIO nas eleições. '''

def voto(ano):
    from datetime import date #econômico importar a biblioteca dentro da função, pois só será usada nela.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
