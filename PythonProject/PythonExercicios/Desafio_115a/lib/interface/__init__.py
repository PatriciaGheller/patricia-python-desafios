'''Crie um pequeno sistema modularizado que permita 
cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. 
O sistema só vai aceitar 2 opções: cadastrar uma nova pessoa # -*- coding=utf-8 -*-
listar todas as pessoas cadastradas.'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[m{c}\033[m -\033[34m {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc