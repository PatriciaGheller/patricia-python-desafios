""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre um mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""

vel = float(input('Qual é a velocidade do carro?: '))
if vel >80:
    print('MULTADO! Você excedeu a velocidade máxima que é de 80km/h.')
    multa = (vel - 80) * 7.00
    print('Você deverá pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')




