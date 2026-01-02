# Número Secreto (while)

numero = int(input("Tente adivinhar qual o número secreto! Ele está entre 0 e 50: "))

while True:
    if numero == 49:
        break
    else:
        print("\nVocê errou 🤣")

        numero = int(input("\nContinue tentando! Ele está entre 0 e 50: "))

print(f"Você (finalmente) acertou o número secreto {numero}!")
