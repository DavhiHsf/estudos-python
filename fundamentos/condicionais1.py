# Test Drive (if, elif, else)

MAIOR_IDADE = 18

print("Bem vindo ao nosso Test Drive! Precisamos que informe algumas informações antes de começarmos.\n")

idade = int(input("Informe sua idade: "))

if idade < MAIOR_IDADE:
    print("\nVocê não tem idade para dirigir.")

else:
    tem_cnh = int(input("\nVoce tem uma CNH? Responda [1] para Sim e [2] para Não: "))

    if idade >= MAIOR_IDADE and tem_cnh == 1:
        print("\nVocê está autorizado a fazer o test drive.")

    elif idade >= MAIOR_IDADE and tem_cnh == 2:
        print("\nVocê tem idade, mas não tem CNH. Não está autorizado a fazer o test drive.")

    else:
        print("\nRegistro de CNH informado incorretamente. Você foi impossibilitado de prosseguir com o Test Drive.")