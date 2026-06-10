# Exercício 02 - Variáveis e Listas
# Objetivo: criar um pequeno algoritmo usando variáveis e listas.

# 1) Guardar alguns valores em uma lista
precos = [10.50, 25.00, 7.90, 30.00]

# 2) Criar uma variável para armazenar o total
total = 0.0

# 3) Somar todos os preços usando um loop
for preco in precos:
    total += preco

# 4) Calcular a quantidade e a média
quantidade = len(precos)
media = total / quantidade

# 5) Mostrar o resultado
print('Lista de preços:', precos)
print('Quantidade de itens:', quantidade)
print(f'Total: R$ {total:.2f}')
print(f'Média: R$ {media:.2f}')

# Desafio extra (também usando listas):
# Adicionar um novo preço e recalcular o total.
novo_preco = 12.30
precos.append(novo_preco)

total = 0.0
for preco in precos:
    total += preco

print('\nApós adicionar um novo preço:', novo_preco)
print('Nova lista de preços:', precos)
print(f'Novo total: R$ {total:.2f}')

