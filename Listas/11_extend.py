# Extend
# Adicionar elementos de uma lista a outra lista
lista = [1, 2, 3]
lista_2 = [4, 5, 6]

lista.extend(lista_2)

print(lista)  # [1, 2, 3, 4, 5, 6]

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]