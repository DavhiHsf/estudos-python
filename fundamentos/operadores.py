# Operadores Aritméticos ==========================
soma = 1 + 1
print(f"1 + 1 = {soma}")

# ==========================
subtracao = 10 - 5
print(f"\n10 - 5 = {subtracao}")

# ==========================
multiplicacao = 6 * 2
print(f"\n6 * 2 = {multiplicacao}")

# ==========================
divisao = 21 / 7
print(f"\n21 / 7 = {divisao}")

# ==========================
divisao_inteira = 21 // 7
print(f"\n21 // 7 = {divisao_inteira}")

# ==========================
resto_divisao = 9 % 2
print(f"\nO que resta da divisão 9 / 2 é {resto_divisao}")

# ==========================
potenciacao = 4 ** 4
print(f"\n4 elevado a 4 = {potenciacao}")

# ==========================
print("\nAgora, some você mesmo!")

num_1 = int(input("\nDigite um número para ser somado: "))
num_2 = int(input("Digite outro número para ser somado: "))

print(f"\nVocê digitou {num_1} e {num_2}")
print(f"{num_1} + {num_2} = {num_1 + num_2}")


# Operadores de Comparação ==========================
saldo = 500
saque = 200

print("\nO saldo em questão é igual ao saque realizado?")
print(saldo == saque)

print("\nO saldo em questão é diferente do saque realizado?")
print(saldo != saque)

print("\nO saldo em questão é maior que o saque realizado?")
print(saldo > saque)

print("\nO saldo em questão é maior OU igual ao saque realizado?")
print(saldo >= saque)

print("\nO saldo em questão é menor que saque realizado?")
print(saldo < saque)

print("\nO saldo em questão é menor OU igual ao saque realizado?")
print(saldo <= saque)

# Operadores de Atribuição ==========================
print(saldo)

saldo += 100
print(saldo) # Atribuição com soma

saldo -= 50
print(saldo) # Atribuição com subtração

saldo *= 2
print(saldo) # Atribuição com multiplicação

saldo //= 2
print(saldo) # Atribuição com divisão inteira

saldo /= 2
print(saldo) # Atribuição com divisão

saldo %= 2
print(saldo) # atribuição com módulo / resto da divisão

saldo **= 2
print(saldo) # atribuição com potência

# Operadores Lógicos ==========================

# AND = Para ser True, tudo tem que ser True
# OR = Para ser True, pelo menos um tem que ser True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

# AND tem precedência sobre OR, or isso o uso de parênteses deixa a expressão mais clara
expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(expressao)
print(expressao_2)

# Operador de Negação ==========================
contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not ""

# Operadores de Identidade ==========================

curso = "Tipos de Operadores com Python"
nome_curso = curso

print(curso is nome_curso)
print(curso is not nome_curso)

saldo, limite = 200, 100

print(saldo is limite)
print(saldo is not limite)

# Operadores de Associação ==========================

frutas = ["limão", "uva", "maçã"]
dia = "30 de dezembro"

print("laranja" in frutas) # Verifica se "laranja" está na lista frutas
print("limão" in frutas)
print("uva" not in frutas) # Verifica se "uva" não está na lista frutas
print("dezembro" in dia) # Verifica se "dezembro" está na variável dia