# Entrada e saída de dados em Python

Assim como podemos exibir informações com o `print()`, também é possível enviar informações diretamente para o Python por meio do `input()`.

O exemplo da vez é simples e direto: é solicitado ao usuário que informe alguns dados, e esses são armazenados diretamente em variáveis através do `input()`.

```python
nome_usuario = input("Digite o seu nome: ")
idade_usuario = int(input("Digite a sua idade: "))
cidade_usuario = input("Digite a sua cidade: ")

```

Depois, temos um exemplo de saída (output) com o `print()`, que informa ao usuário sobre a “corrente”:

``` python
print(f"""\nOlá {nome_usuario}!
Saiba que as informações que você escreveu (fora o seu nome) são desnecessárias e que agora você foi pego pela corrente do Hello World!""")
```

Por fim, em tom de brincadeira, é solicitado ao usuário que digite "Hello World" 25 vezes para se livrar da corrente:

``` python
reversao_de_corrente = input("\nDigite Hello World 25 vezes para se livrar de corrente: ")
```

### Observação: f-string multilinha
A f-string multilinha utiliza três aspas (`"""`) junto do prefixo `f`, permitindo escrever textos em várias linhas e interpolar variáveis de forma clara e legível, sem a necessidade de múltiplos `\n` ou concatenações.

```python
print(f"""Olá {nome}!
Esta mensagem possui
mais de uma linha.""")