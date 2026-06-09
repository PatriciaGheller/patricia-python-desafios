n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2

di = n1 // n2
ex = n1 ** n2

print('A soma vale: {},\n o produto é: {} e a divisão é :{:.3f}'.format(s, m, d), end = '>>>>>>> ')
print('A divisão inteira é: {} e a potência é: {}'.format(di, ex))

#end= '' indica que não há uma quebra de linha
# :.3f significa a quantidade de casas decimais que devem ser apresentadas
#\n significa uma nova linha

