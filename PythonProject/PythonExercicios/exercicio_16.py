"""Lista:
lache = []
dicionário:
lanche = {}"""

"""Tupla:"""
#Tuplas são imutáveis
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim','Batata Frita')
    #print(lanche[1:3])
#print(sorted(lanche)) Cola em ordem, transforma em uma lista

  #Exemplos de for que podem ser usados para o mesmo caso

#for comida in lanche:
    #print(f'Eu vou comer {comida}')

#for pos, comida in enumerate (lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')








