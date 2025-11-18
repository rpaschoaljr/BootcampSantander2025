# Estrutura condicional ternária em Python

saldo = 2000
saque = 2500
# Usando a estrutura condicional ternária para verificar se o saque pode ser realizado
status = "Sucesso" if saldo >= saque else "Falha" # Estrutura ternária deve ser dessa forma "<valor_se_verdadeiro> if <condição> else <valor_se_falso>"

print(f"{status} ao realizar o saque!")