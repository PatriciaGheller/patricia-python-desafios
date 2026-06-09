nome = str(input('Digite seu nome: '))
if nome == 'Patrícia':
    print('\033[2;30;45mQue nome bonito!\033[m')
    print('Muito prazer em te conhecer {}!!!\033[m'.format(nome))
elif nome == 'Bruna':
    print('\033[0;30;45mEsse nome é lindo!\033[m')
elif nome == 'Pedro' or nome =='Lucas' or nome == 'Felipe':
    print('Esse nome é tão normal!')
elif nome in 'Andressa Jéssica Paola':
    print('Que nome feminino lindo!')
else:
    print('Nome legal')

