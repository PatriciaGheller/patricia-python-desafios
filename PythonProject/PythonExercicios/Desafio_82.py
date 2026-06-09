'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
No final mostre o conteúdo das três listas geradas.'''
valores = []
valores_par = []
valores_impares = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    if v % 2 == 0:
        valores_par.append(v)
    else:
        valores_impares.append(v)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares foram: {valores_par}')
print(f'Os valores impares foram: {valores_impares}')




