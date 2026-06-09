#Conversor de dolar para reais

# Definindo a cotação do dólar
cotacao_dolar = 6.05

# Solicita ao usuário que insira o valor em dólares
valor_dolares = float(input("Digite o valor em dólares (US$): "))

# Calcula o valor em reais
valor_reais = valor_dolares * cotacao_dolar

# Exibe o resultado
print(f"O valor de US${valor_dolares:.2f} é equivalente a R${valor_reais:.2f} na cotação atual.")



