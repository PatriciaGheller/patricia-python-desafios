"""Crie um programa que leia uma frase pelo teclado e mostre:
 Quantas vezes aparece a letra 'A'.
 Em que posição ela aparece a primeira vez.
 Em que posição ela aparece a última vez."""

from itertools import count

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A leta "A" aparece na posição {} pela primeira vez.'.format(frase.find('A')+1))
print('A letra "A" aparece na posição {} pela última vez'.format(frase.rfind('A')+1))




