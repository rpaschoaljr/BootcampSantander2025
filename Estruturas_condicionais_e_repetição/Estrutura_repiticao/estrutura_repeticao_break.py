# Estrutura de repetição com break e continue em Python
# O break interrompe a execução do loop
# O continue pula para a próxima iteração do loop

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")