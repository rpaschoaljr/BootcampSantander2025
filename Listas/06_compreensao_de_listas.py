# Compreensão de listas

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]#Filtrar pares
print(pares)

# Para melhor compreensão do código já que estamos começando a aprender python
# O código faz a mesma coisa que o de cima, mas de forma mais "clara"
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []  # Cria uma lista vazia

# O Loop começa aqui
for numero in numeros:          # "Para cada número na lista..."
    if numero % 2 == 0:         # "...se o número for par..."
        pares.append(numero)    # "...adicione ele na nova lista."

print(pares)


# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]#Calcular quadrado
print(quadrado)

# Para melhor compreensão do código já que estamos começando a aprender python
# O código faz a mesma coisa que o de cima, mas de forma mais "clara"
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []  # Começa vazia

# O Loop começa aqui
for numero in numeros:          # 1. Pega um número de cada vez
    resultado = numero ** 2     # 2. Faz o cálculo (modifica)
    quadrado.append(resultado)  # 3. Guarda na nova lista

print(quadrado)