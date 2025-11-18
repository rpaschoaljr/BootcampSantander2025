# Indentação de blocos em Python
# A indentação define blocos de código
# Em Python, a indentação é obrigatória para definir blocos
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)
