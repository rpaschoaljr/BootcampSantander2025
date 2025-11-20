# Iterar listas
carros = ["gol", "celta", "palio"]
#usando estrutura de repetição para iterar a lista
for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")