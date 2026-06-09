#Faça um algoritmo que mostre o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salario do funcionario:R$'))
novo = salario + (salario * 15/100)

print(' Um funcionário que ganhava R${:.2f}, com 15% de aumento passará a receber :R${:.2f}'.format(salario,novo))


