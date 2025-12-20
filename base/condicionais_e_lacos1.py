# Test Drive

idade = int(input("Informe sua idade: "))

if idade < 18:
    print("\nVocê não tem idade para dirigir.")

else:
    tem_cnh = int(input("Voce tem uma CNH? Responda 1 para Sim e 2 para Não: "))

    while tem_cnh != 1 and tem_cnh != 2:
        print("\nResponda corretamente!")
        tem_cnh = int(input("Voce tem uma CNH? Responda 1 para Sim e 2 para Não: "))

if idade >= 18 and tem_cnh == 1:
    print("\nVocê está autorizado a fazer o test drive.")

elif idade >= 18 and tem_cnh == 2:
    print("\nVocê tem idade, mas não tem CNH. Não está autorizado a fazer o test drive.")