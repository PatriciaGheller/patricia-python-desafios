'''Crie um programa que leia nome, ano de nascimento e carteira de 
trabalho e cadastre-os (com idade) em um dicionário se por 
acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar. 
Considere que o tempo de contribuição para aposentadoria é de 35 anos, 
e a idade mínima para aposentadoria é de 65 anos.'''

from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade']= datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35 - datetime.now().year) + dados['idade'])
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}.')
    