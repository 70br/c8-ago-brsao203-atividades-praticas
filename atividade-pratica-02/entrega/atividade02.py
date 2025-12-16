# 1 - Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Convertido para dólar: US$", round(valor_dolar, 2))
print("Convertido para euro: €", round(valor_euro, 2))


# 2 - Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("\nProduto:", produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))


# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("\nNotas do aluno:")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media, 2))


# 4 - Calculadora de Consumo de Combustível
distancia = 300
combustivel = 25

consumo_medio = distancia / combustivel

print("\nDados da viagem:")
print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", round(consumo_medio, 2), "km/l")
