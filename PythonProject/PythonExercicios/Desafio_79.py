'''Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.Caso o número já exista
lá dentro, ele não será adicionado.
No final, serão exebidos todos os valores únicos digitados, em ordem
crescente.'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:  # Loop para garantir que a resposta seja válida
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break  # Sai do loop interno e do loop principal
        elif r in 'Ss':
            break  # Sai do loop interno e continua o loop principal
        else:
            print('Valor inválido. Por favor, digite S para sim ou N para não.')
    if r in 'Nn':
        break  # Sai do loop principal se a resposta for N ou n
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores:{numeros}')

