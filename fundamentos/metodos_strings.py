# Maiúsculo, minúsculo e título
linguagem = "PyThOn"

print(linguagem.upper())
print(linguagem.lower())
print(linguagem.title())

# ==========================
# Eliminando espaços em branco
linguagem = "      Python   "

print(linguagem.strip())
print(linguagem.lstrip())
print(linguagem.rstrip())

# ==========================
# Junções e Centralização
linguagem = "Python"

print(linguagem.center(10, "#"))
print(".".join(linguagem))

# ==========================
# Interpolação de variáveis

nome = "Davi"
idade = 20
data = "02/01/2026"

dados = {"nome": "Davi", "idade": "20", "data": "02/01/2026"}

# Old style
print("\nBom dia (ou tarde, ou noite), meu nome é %s, tenho %d anos atualmente. Hoje é %s e sigo estudando Python!" % (nome, idade, data))

# Método format
print("\nBom dia (ou tarde, ou noite), meu nome é {}, tenho {} anos atualmente. Hoje é {} e sigo estudando Python!".format(nome, idade, data))

print("\nBom dia (ou tarde, ou noite), meu nome é {0}, tenho {1} anos atualmente. Hoje é {2} e sigo estudando Python!".format(nome, idade, data))

print("\nBom dia (ou tarde, ou noite), meu nome é {nome}, tenho {idade} anos atualmente. Hoje é {data} e sigo estudando Python!".format(nome=nome, idade=idade, data=data))

print("\nBom dia (ou tarde, ou noite), meu nome é {nome}, tenho {idade} anos atualmente. Hoje é {data} e sigo estudando Python!".format(**dados))

# f-string
print(f"\nBom dia (ou tarde, ou noite), meu nome é {nome}, tenho {idade} anos atualmente. Hoje é {data} e sigo estudando Python!")

# Formatar strings com f-string
PI = 3,14159265358979323846

# print(f"\nValor de PI: {PI:.2f}")
# print(f"\nValor de PI: {PI:10.2f}")

# ==========================
# Fatiamento de strings

nome = "Charlingtonglaevionbeecheknavare"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:15])
print(nome[10:15:2])
print(nome[:])
print(nome[::-1])

# Strings triplas
nome = "Davi"

print(f"""
Olá! Meu nome é {nome},
Eu estou aprendendo Python.
""")
