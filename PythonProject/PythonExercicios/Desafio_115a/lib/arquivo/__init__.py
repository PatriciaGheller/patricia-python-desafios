from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.strip().split(';')
            if len(dado) >= 2:
                nome = dado[0]
                idade = dado[1]
                print(f'{nome:<30}{idade:>3} anos')
    finally:
        a.close()
        

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
        finally:
            a.close()