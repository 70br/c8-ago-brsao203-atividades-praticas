# 1 - Classificador de Idade
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Classificação: Criança")
elif idade >= 13 and idade <= 17:
    print("Classificação: Adolescente")
elif idade >= 18 and idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")


# 2 - Calculadora de IMC
peso = float(input("\nDigite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("IMC:", round(imc, 2))
print("Classificação:", classificacao)


# 3 - Conversor de Temperatura
temperatura = float(input("\nDigite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = None

if resultado is not None:
    print("Temperatura convertida:", round(resultado, 2))
else:
    print("Conversão inválida")


# 4 - Verificador de Ano Bissexto
ano = int(input("\nDigite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto")
else:
    print("O ano", ano, "não é bissexto")
