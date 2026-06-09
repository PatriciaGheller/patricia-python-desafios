#Listas são mutáveis, diferente das tuplas

num = [2,5,9,1]

#substitui o elemento
num[2] = 3

#adiciona um elemento no final da lista
num.append(7)

#organiza os elementos
num.sort(reverse = True) #reverser = True inverte a ordem dos elementos...

#insere um elemento na posição indicada pelo index
num.insert(2, 0)

#exclui o ultimo valor
num.pop() #se eu colocar o dois no parentese ele elimina o '0' e 0 '1' volta para a lita. ex num.pop(2)

#vai remover do inicio da lista se houver dois iguais sera removido apenas um.
#num.remove(2)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)

#mostra a quantidade de elementos
print(f'Essa lista tem {len(num)} elementos')





