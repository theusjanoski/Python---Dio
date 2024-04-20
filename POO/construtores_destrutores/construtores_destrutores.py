class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("removendo a instância da classe")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola, Mundo")

del c

print("Ola, Mundo")
print("Ola, Mundo")
print("Ola, Mundo")

# criar_cachorro()