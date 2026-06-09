#A lista pode ser criada dessa forma
#valores = list()

#Também pode ser criada dessa forma:

valores = []
#vai adcionar os valores à lista
#valores.append(5)
#valores.append(9)
#valores.append(4)

#vai ler um valor dentro do append
for cont in range(0, 5):
    valores.append(int (input('Digite um valor: ')))

#print(valores)

#for v in valores:
    #print(f'{v}...', end= '')

  #busca tanto a chave quanto o valor
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')

#Ligação de duas listas sem o colchete [:], cópia com o [:]

'''a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''










