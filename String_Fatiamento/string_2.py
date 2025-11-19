# String Fatiamento - Parte 2
nome = "Ricardo"
idade = 32
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}# Dicionário com dados
print("Metodo antigo com %s e %d")
print("Nome: %s Idade: %d" % (nome, idade))# Formatação antiga com %s e %d
print("Metodo .format")
print("Nome: {} Idade: {}".format(nome, idade))# Formatação com método format
print("Nome: {1} Idade: {0}".format(idade, nome))# Usando índices no método format
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))# Repetindo valores com índices no método format
print("Metodo .format com variáveis")
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))# Usando nomes no método format
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))# Repetindo valores com nomes no método format
print("Nome: {nome} Idade: {idade}".format(**dados))# Usando dicionário no método format
print("Metodo f-strings")
print(f"Nome: {nome} Idade: {idade}")# Formatação com f-strings
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")# Formatação com f-strings e duas casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")# Formatação com f-strings, largura 10 e uma casa decimal