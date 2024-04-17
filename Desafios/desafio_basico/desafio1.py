# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
def recomendar_plano(consumo):
    if consumo <= 10:
        return "O Plano Essencial Fibra de 50Mbps é o melhor para você!"
    elif consumo > 10 and consumo <= 20:
        return "O Plano Prata Fibra de 100Mbps é o melhor para você!"
    else:
        return "O Plano Premium Fibra de 300Mbps é o melhor para você!"
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("\nInsira seu consumo médio mensal de dados: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

