# Tipos básicos
# ==========================
nome = "Davi"
idade = 20
altura = 1.82
brasileiro = True

print(f"Meu nome é {nome},\ntenho {idade} anos e possuo {altura}m de altura.")

# --- Lógica booleana
# ==========================
ingressos_cinema = 95
clientes = 130

tem_ingressos_suficientes = ingressos_cinema >= clientes

print("\nTem ingressos suficientes para todos?", tem_ingressos_suficientes)

# --- Reatribuição de valores
# ==========================
raca_cachorro = "Husky Siberiano"
print("\n" + raca_cachorro)

raca_cachorro = "Golden Retriever"
print(raca_cachorro)

# --- Convenção de constantes
# ==========================
IMPOSTO_PADRAO = 0.15
DIAS_DA_SEMANA = 7
URL_API = "https://api.exemplo.com"

# --- Tipos e conversão
# ==========================
print(type(nome))
print(type(idade))
print(type(altura))
print(type(brasileiro))

idade_str = str(idade)
print(f"\nConvertida para string e salva em UMA NOVA variável, o novo tipo da variável idade (agora idade_str) é: {type(idade_str)}")