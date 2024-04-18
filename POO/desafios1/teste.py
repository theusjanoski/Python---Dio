class Bicicletas:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("BIBII")

    def parar(self):
        print("OIA O FREIOOO")

    def correr(self):
        print("VRUMMMM")


bicicleta1 = Bicicletas("amarelo", "BMX", "2015", "2500")

menu = """
    O que você vai fazer com a bicicleta?

    [b] Buzinar
    [c] Correr
    [p] Parar

=> """

while True:
    opcao = input(menu).strip().lower()

    if opcao == "b":
        bicicleta1.buzinar()
        print("=" * 30)
    elif opcao== "c":
        bicicleta1.correr()
        print("=" * 30)
    elif opcao == "p":
        bicicleta1.parar()
        print("=" * 30)
    else:
        print("Ação não permitida")
        print("=" * 30)