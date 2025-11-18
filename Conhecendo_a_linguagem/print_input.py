# Entrada e saída de dados em Python
# print() e input()
#Recebe dados do usuário com input() e exibe com print()
nome = input("infome seu nome: ")
idade = input("informe sua idade: ")

# Diferentes formas de usar print()
print(nome, idade)
print(nome, idade, end="...\n") # muda o final da linha
print(nome, idade, sep="#") # muda o separador entre os valores
print(nome, idade, sep="#", end="...\n") # muda o separador e o final da linha

print(f"Meu nome é {nome} e eu tenho {idade} anos.") # f-string
print(f"Meu nome é {nome} e eu tenho {idade} anos.", end="...\n") #end personalizado
print(f"Meu nome é {nome} e eu tenho {idade} anos.", sep="#", end="...\n") #sep não funciona no f-string
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade)) # método format
print("Meu nome é {0} e eu tenho {1} anos.".format(nome, idade)) # método format com índices
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade)) # método format com nomeação