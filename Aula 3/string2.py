nome = "Matheus"
idade = 19
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Matheus", "idade": 19}

print("Nome %s e Idade: %d" % (nome, idade))
print("Nome {} e Idade: {}".format(nome, idade))
print("Nome {1} e Idade: {0}".format(idade, nome))
print("Nome {1} e Idade: {0}".format(idade, nome))
print("Nome {1} e Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome {nome} e Idade: {idade}".format(nome=nome, idade=idade))
print("Nome {name} e Idade: {age} {name} {age}".format(age=idade, name=nome))
print("Nome {nome} e Idade: {idade}".format(**dados))

print(f"Nome {nome} e Idade: {idade}")
print(f"Nome {nome} e Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome {nome} e Idade: {idade} Saldo: {saldo:10.2f}")
