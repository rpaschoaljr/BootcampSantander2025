#remove
#É possível remover um elemento de um conjunto com a função remove()
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(1))  # None
print(numeros.remove(45))  # KeyError
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}