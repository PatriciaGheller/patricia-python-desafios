'''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável, 
de acordo com o tamanho do texto.'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)  
    
# programa principal
escreva('Patrícia Gheller')
escreva('Curso de Python no YouTube')
escreva('CeV')