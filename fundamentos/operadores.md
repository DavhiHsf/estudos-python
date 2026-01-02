# Operadores em Python

Este arquivo tem como objetivo apresentar, de forma prática, o**s principais tipos de operadores do Python.**
O foco aqui não é apenas o resultado, mas entender como cada operador se comporta e em quais situações ele é utilizado.

O script foi organizado por blocos, cada um representando uma categoria de operadores.

## Operadores Aritméticos
São usados para realizar cálculos matemáticos básicos.

### Soma (`+`)
O operador `+` é utilizado para somar dois valores.

```python
soma = 1 + 1
print(f"1 + 1 = {soma}")
```

### Subtração (`-`)
O operador `-` realiza a subtração entre dois valores.

```python
subtracao = 10 - 5
print(f"\n10 - 5 = {subtracao}")
```

### Multiplicação (`*`)
O operador `*` multiplica dois valores.

```python
multiplicacao = 6 * 2
print(f"\n6 * 2 = {multiplicacao}")
```

### Divisão (`/`)
O operador `/` realiza a divisão entre dois valores e sempre retorna um número do tipo float, mesmo quando o resultado é um número inteiro.

```python
divisao = 21 / 7
print(f"\n21 / 7 = {divisao}")
```

### Divisão Inteira (`//`)
O operador `//` realiza a divisão inteira, retornando apenas a parte inteira do resultado, descartando as casas decimais.

```python
divisao_inteira = 21 // 7
print(f"\n21 // 7 = {divisao_inteira}")
```

### Resto da divisão (`%`)
O operador `%` retorna o resto de uma divisão.

```python
resto_divisao = 9 % 2
print(f"\nO que resta da divisão 9 / 2 é {resto_divisao}")
```

### Potenciação (`**`)
O operador `**` é utilizado para realizar cálculos de potência.

```python
potenciacao = 4 ** 4
print(f"\n4 elevado a 4 = {potenciacao}")
```

## 2. Operações com entrada do usuário
Também é possível realizar operações matemáticas utilizando valores informados pelo usuário por meio do `input()`.

O `input()` sempre retorna uma string, por isso é necessário converter os valores para int antes de realizar cálculos matemáticos.

Esse bloco permite que o próprio usuário informe os valores da soma:

```python
num_1 = int(input("Digite um número para ser somado: "))
num_2 = int(input("Digite outro número para ser somado: "))

print(f"Você digitou {num_1} e {num_2}")
print(f"{num_1} + {num_2} = {num_1 + num_2}")
```

## 3. Operações de Comparação
São usados para comparar valores e sempre retornam um valor booleano `(True ou False)`.

```python
saldo = 500
saque = 200

saldo == saque   # igualdade
saldo != saque   # diferença
saldo > saque    # maior que
saldo >= saque   # maior ou igual
saldo < saque    # menor que
saldo <= saque   # menor ou igual
```

No arquivo .py, cada comparação é exibida com `print()` para facilitar a visualização do resultado.

## 4. Operadores de Atribuição
Servem para atualizar o valor de uma variável usando o próprio valor anterior.

```python
saldo += 100  # soma
saldo -= 50   # subtração
saldo *= 2    # multiplicação
saldo //= 2   # divisão inteira
saldo /= 2    # divisão
saldo %= 2    # resto da divisão
saldo **= 2   # potência
```

Muito usados em situações como controle de saldo, contadores e laços.

## 5. Operadores Lógicos
São usados para combinar expressões booleanas.

AND (`and`) = Para ser True, tudo tem que ser True.
OR (`or`) = Para ser True, pelo menos um tem que ser True.
NOT (`not`) Inverte o valor lógico.

```python
True and False
True or False
not True
```

Se usam parênteses nessas expressões para torná-las mais legíveis e evitar ambiguidades.

```python
not 1000 > 1500
not []
not ""
```

Listas vazias, strings vazias e `0` são considerados False em Python.

## 6. Operadores de Identidade
Verificam se duas variáveis apontam para o mesmo objeto na memória, e não apenas se têm o mesmo valor.

```python
nome_curso = curso

curso is nome_curso
curso is not nome_curso

# ==========================

saldo, limite = 200, 100

saldo is limite
saldo is not limite
```

Esse tipo de operador é mais comum em verificações internas e menos usado em lógica de negócio.

# 8. Operadores de Associação
Verificam se um valor existe dentro de uma sequência, como listas ou strings.

```python
"laranja" in frutas
"limão" in frutas
"uva" not in frutas
"dezembro" in dia
```

Buscas rápias e validações simples utilizam justamente esses operadores.

---
**Como executar:**
No terminal, digite: `python operadores.py` ou `py operadores.py`