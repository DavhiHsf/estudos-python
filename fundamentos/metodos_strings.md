# Métodos de Strings em Python

Aqui, **os principais métodos e operações disponíveis para strings em Python** são explorados e explicados, incluindo transformação de texto, remoção de espaços, junções, formatação, fatiamento e uso de strings multilinha.

## 1. Maiúsculo, minúsculo e título
Python possui métodos nativos para alterar a forma como o texto é exibido:

`upper()` → converte todos os caracteres para maiúsculo

`lower()` → converte todos os caracteres para minúsculo

`title()` → deixa a primeira letra de cada palavra em maiúsculo

```python
linguagem = "PyThOn"

print(linguagem.upper())
print(linguagem.lower())
print(linguagem.title())
```

Esses métodos não alteram a string original, apenas retornam uma nova versão formatada.

## 2. Removendo espaços em branco
É comum lidar com entradas de texto contendo espaços extras. Para isso, usamos:

`strip()` → remove espaços do início e do fim

`lstrip()` → remove apenas do lado esquerdo

`rstrip()` → remove apenas do lado direito

```python
linguagem = "      Python   "

print(linguagem.strip())
print(linguagem.lstrip())
print(linguagem.rstrip())
```

## 3. Junção e centralização
Também é possível alinhar textos e unir caracteres:

`center()` → centraliza a string, preenchendo com um caractere definido

`join()` → junta os caracteres de uma string usando um separador

```python
linguagem = "Python"

print(linguagem.center(10, "#"))
print(".".join(linguagem))
```

## 4. Interpolação de variáveis em strings
Interpolação é a forma de inserir valores dentro de uma string.

### Old Style (`%`)
Forma mais antiga e menos usada atualmente:

```python
print("Meu nome é %s e tenho %d anos." % (nome, idade))
```

### Método `format()`
Mais flexível e organizado:

```python
print("Meu nome é {}, tenho {} anos.".format(nome, idade))
print("Meu nome é {nome}, tenho {idade} anos.".format(nome=nome, idade=idade))
```

Também é possível passar um dicionário:

```python
print("Meu nome é {nome}, tenho {idade} anos.".format(**dados))
```

### f-strings
A forma mais recomendada atualmente, por ser mais legível:

```python
print(f"Meu nome é {nome}, tenho {idade} anos.")
```

## 5. Fatiamento de strings
Strings podem ser acessadas como sequências de caracteres, usando índices:

```python
nome = "Charlingtonglaevionbeecheknavare"

print(nome[0])        # primeiro caractere
print(nome[:9])       # do início até o índice 9
print(nome[10:])      # do índice 10 até o final
print(nome[10:15])    # intervalo específico
print(nome[10:15:2])  # intervalo com passo
print(nome[:])        # string completa
print(nome[::-1])     # string invertida
```

O fatiamento segue o padrão: `string[início:fim:passo]`

## 6. Strings triplas
Strings triplas permitem escrever textos com múltiplas linhas, mantendo a formatação:

```python
print(f"""
Olá! Meu nome é {nome},
Eu estou aprendendo Python.
""")
```

São muito usadas para mensagens longas, textos formatados e documentação.

---
**Como executar:**
No terminal, digite: `python metodos_strings.py` ou `py metodos_strings.py`