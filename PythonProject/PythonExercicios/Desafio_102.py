'''Crie em programa que tenha uma função chamada fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular 
e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show=False):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat

n = int(input('Digite um número para calcular seu fatorial: '))
print(fatorial(n, show=True))