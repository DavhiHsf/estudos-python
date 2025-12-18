# Variáveis em Python

O papel das variáveis em toda linguagem de programação é armazenar dados em memória. Diferentes tipos de dados podem ser armazenados.

### 1. Tipos Primitivos Básicos
Em Python, a tipagem é dinâmica, mas os tipos principais são:

```python
# str (Texto)
nome = "Davi"

# int (Números inteiros)
idade = 20

# float (Ponto flutuante / Reais)
altura = 1.82

# bool (Booleano / Lógico)
brasileiro = True
```

### 2. Saída de Dados (f-strings)
Existem outras formas, mas a f-string é a mais elegante e performática para interpolar variáveis. O `\n` realiza a quebra de linha.

```python
print(f"Meu nome é {nome},\ntenho {idade} anos e possuo {altura}m de altura.")
```

### 3. Lógica Booleana em Variáveis
É possível armazenar o resultado de uma comparação lógica diretamente em uma variável.

```python
# Declarando as variáveis
ingressos_cinema = 95
clientes = 130

# A variável abaixo armazenará apenas True ou False
tem_ingressos_suficientes = (ingressos_cinema >= clientes)

print("Tem ingressos suficientes para todos?", tem_ingressos_suficientes)
# Saída esperada: Tem ingressos suficientes? False
```

### 4. Reatribuição de Valores (Tipagem Dinâmica)
Uma vez criada, a variável pode ter seu valor alterado a qualquer momento.

```python
raca_cachorro = "Husky Siberiano"
print(raca_cachorro)

# Reatribuindo valor à MESMA variável
raca_cachorro = "Golden Retriever"
print(raca_cachorro)
```

### 5. Constantes
No Python, **não existem constantes técnicas** (o interpretador não impede a mudança). A comunidade usa uma convenção social:

> **Regra:** Variáveis constantes devem ser escritas em **CAIXA_ALTA**. Isso sinaliza: "Somos adultos, por favor, não altere esse valor".

```python
IMPOSTO_PADRAO = 0.15
DIAS_DA_SEMANA = 7
URL_API = "https://api.exemplo.com"
```

### 6. Como o Python enxerga os dados
Também é possível verificar exatamente que tipo de dado nós estamos atribuindo como valor para uma variável usando `type()`

```python
print(type(nome))
print(type(idade))
print(type(altura))
print(type(brasileiro))
```

Bem como podemos converter um tipo específico de dado para outro:

```python
idade_str = str(idade)
print(type(idade_str))
```

---
**Como executar:**
No terminal, digite: `python variaveis.py` ou `py variaveis.py`