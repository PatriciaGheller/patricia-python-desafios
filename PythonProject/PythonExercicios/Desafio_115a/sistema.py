from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    

cabeçalho('SISTEMA DE CADASTRO DE PESSOAS')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('\033[0;36mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[0;35mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
        
    