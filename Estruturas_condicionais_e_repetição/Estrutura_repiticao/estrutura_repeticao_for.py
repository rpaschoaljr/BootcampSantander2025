# Repetição com for em Python e uso do else
# A estrutura de repetição for itera sobre um iterável, como strings, listas, tuplas, dicionários, entre outros


texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5): # de 0 a 50, pulando de 5 em 5
    print(numero, end=" ")
print()  # adiciona uma quebra de linha