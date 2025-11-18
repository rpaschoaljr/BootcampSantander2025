# Estruturas condicionais em Python
# Estruturas condicionais permitem executar blocos de código com base em condições

# Definindo constantes para maior clareza
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
# Solicitando a idade do usuário
idade = int(input("Informe sua idade: "))

# Verificando se a pessoa é maior de idade
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
# Verificando se a pessoa é menor de idade
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Usando if-else para duas condições mutuamente exclusivas
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")

# Verificando múltiplas condições com elif
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")