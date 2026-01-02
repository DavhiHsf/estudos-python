# Contador de letras (for)

texto = input("Escreva uma palavra: ")
vogais = "aeiou"

contador_letras = 0
total_vogais = []

for letra in texto:
    contador_letras += 1
    total_letras = contador_letras

    if letra in vogais:
        total_vogais.append(letra)

print(f"\nHá um total de {total_letras} letras nessa palavra!")

print(f"Vogais na palavra: {total_vogais}\n")

# ==========================
# Exibindo Tabuadas (range com for)

print("TABUADAS")

for numero in range(0, 11, 1):
    print(numero, end=" ")

print()

for numero in range(0, 21, 2):

    print(numero, end=" ")

print()

for numero in range(0, 31, 3):

    print(numero, end=" ")

print()

for numero in range(0, 41, 4):

    print(numero, end=" ")

print()

for numero in range(0, 51, 5):

    print(numero, end=" ")

print()

for numero in range(0, 61, 6):

    print(numero, end=" ")

print()

for numero in range(0, 71, 7):

    print(numero, end=" ")

print()

for numero in range(0, 81, 8):

    print(numero, end=" ")

print()

for numero in range(0, 91, 9):

    print(numero, end=" ")

print()

for numero in range(0, 101, 10):

    print(numero, end=" ")

print()
