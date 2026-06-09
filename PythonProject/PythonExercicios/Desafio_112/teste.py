'''Crie um pacote chamado utilidadesCeV que tenha dois módulos 
internos chamados moeda e dado. Transfira todas as funções 
utilizadas nos desafios anteriores para o primeiro pacote 
e mantenha tudo funcionando.'''

from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)