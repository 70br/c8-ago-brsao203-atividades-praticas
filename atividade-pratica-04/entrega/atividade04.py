# ===============================
# Atividade Prática 04
# ===============================

# 1 - Calculadora básica
print("=== Calculadora Básica ===")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
print()


# 2 - Registro de notas e média da turma
print("=== Média da Turma ===")
quantidade = int(input("Quantos alunos? "))

soma_notas = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / quantidade
print(f"Média da turma: {media:.2f}")
print()


# 3 - Verificador de senha
print("=== Verificador de Senha ===")
senha = input("Digite uma senha: ")

tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
print()


# 4 - Analisador de números (pares e ímpares)
print("=== Analisador de Números ===")
pares = 0
impares = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
