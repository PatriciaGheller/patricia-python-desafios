print('='*30)
print('{:^30}'.format('BANCO GHELLER'))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 100
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre! Tenha um bom dia!')
