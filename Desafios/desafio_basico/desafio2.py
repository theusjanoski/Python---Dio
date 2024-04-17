# Crie uma lista vazia para armazenar os itens
itens = []

# Defina uma variável para controlar o loop

# Loop para solicitar itens ao usuário
for i in range(3):  # Loop será executado 3 vezes
    item = input("")
    itens.append(item)

# Exibe a lista de itens
print("\nLista de Equipamentos:")  
for item in itens:
    print(f"- {item}")

