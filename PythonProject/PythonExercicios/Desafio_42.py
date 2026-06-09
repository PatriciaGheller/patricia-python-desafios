"""Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
 que tipo de triângulo será formado:

 -Equilátero: todos os lados iguais
 -Isósceles: dois lados iguais
 -Escaleno: todos os lados diferentes"""
r1 = float(input('\033[0;30;44mPrimeiro Segmento:\033[m '))
r2 = float(input('\033[4;38;45mSegundo Segmento:\033[m '))
r3 = float(input('\033[3;33;46mTerceiro Segmento:\033[m '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('\033[0;36;40mOs segmentos acima podem formar um triângulo\033[m ' ,end ='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO!')
    else:
        print('ISÓCELES!')

else:
    print('Os segmentos não formam um TRIÂNGULO.')





