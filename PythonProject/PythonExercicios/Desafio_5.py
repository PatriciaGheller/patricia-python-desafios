#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número:'))

ant = n - 1
suc = n + 1


print('Analizando o número: {}, seu antecessor é:{} e seu sucessor é:{}'.format(n, ant, suc))

#print('Analizando o número: {}, seu antecessor é:{} e seu sucessor é:{}'.format(n, (n - 1), (n + 1)))
# essa forma será usada caso não queira armazenar em uma variável, n - 1 e n + 1.