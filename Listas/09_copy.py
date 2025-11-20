# Copy
# Copiar lista
lista = [1, "Python", [40, 30, 20]]

print("Print da lista:", lista)  # [1, "Python", [40, 30, 20]]

lista_2 = lista.copy()

print("Print da lista_2 recem copiada:", lista_2)  # [1, "Python", [40, 30, 20]]

lista_2[0] = "Java" # Modifica o primeiro elemento da lista_2

print("Print da lista:", lista)  # [1, "Python", [40, 30, 20]]

print("Print da lista_2:", lista_2)  # ["Java", "Python", [40, 30, 20]]