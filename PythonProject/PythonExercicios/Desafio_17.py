#Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
cttoposto = float(input('Qual é o comprimento do cateto oposto?'))
cttadjacente = float(input('Qual é o comprimento do cateto adjacente?'))
hipotenusa = hypot(cttoposto, cttadjacente)

#(cttoposto ** 2 + cttadjacente ** 2) ** (1/2))

print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))

