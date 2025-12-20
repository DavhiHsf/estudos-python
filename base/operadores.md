# Operadores em Python

Aqui, construímos um script que realiza **as operações matemáticas mais básicas** dentro do Python, utilizando variáveis, operadores aritméticos e saída de dados com `print()`.

## 1. Soma (`+`)
O operador `+` é utilizado para somar dois valores.

```python
soma = 1 + 1
print(f"1 + 1 = {soma}")
```

## 2. Subtração (`-`)
O operador `-` realiza a subtração entre dois valores.

```python
subtracao = 10 - 5
print(f"\n10 - 5 = {subtracao}")
```

## 3. Multiplicação (`*`)
O operador `*` multiplica dois valores.

```python
multiplicacao = 6 * 2
print(f"\n6 * 2 = {multiplicacao}")
```

## 4. Divisão (`/`)
O operador `/` realiza a divisão entre dois valores e sempre retorna um número do tipo float, mesmo quando o resultado é um número inteiro.

```python
divisao = 21 / 7
print(f"\n21 / 7 = {divisao}")
```

## 5. Resto da divisão (`%`)
O operador `%` retorna o resto de uma divisão.

```python
resto_divisao = 9 % 2
print(f"\nO que resta da divisão 9 / 2 é {resto_divisao}")
```

## 6. Potenciação (`**`)
O operador `**` é utilizado para realizar cálculos de potência.

```python
potenciacao = 4 ** 4
print(f"\n4 elevado a 4 = {potenciacao}")
```

## 7. Operações com entrada do usuário
Também é possível realizar operações matemáticas utilizando valores informados pelo usuário por meio do `input()`.

Como o `input()` retorna uma **string**, é necessário converter os valores para `int`.

```python
num_1 = int(input("Digite um número para ser somado: "))
num_2 = int(input("Digite outro número para ser somado: "))

print(f"Você digitou {num_1} e {num_2}")
print(f"{num_1} + {num_2} = {num_1 + num_2}")
```

---
**Como executar:**
No terminal, digite: `python operadores.py` ou `py operadores.py`