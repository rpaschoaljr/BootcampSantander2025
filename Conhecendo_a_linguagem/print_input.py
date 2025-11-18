nome = input("infome seu nome: ")
idade = input("informe sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#")
print(nome, idade, sep="#", end="...\n")

print(f"Meu nome é {nome} e eu tenho {idade} anos.")
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
print("Meu nome é {0} e eu tenho {1} anos.".format(nome, idade))
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade))
print(f"Meu nome é {nome} e eu tenho {idade} anos.", end="...\n")
print(f"Meu nome é {nome} e eu tenho {idade} anos.", sep="#", end="...\n") #sep não funciona no f-string