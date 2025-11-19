# String Fatiamento - Parte 1
nome = "SaNtAndEr BOoTCAmp"

print(nome.upper())# Converte todos os caracteres para maiúsculo
print(nome.lower())# Converte todos os caracteres para minúsculo
print(nome.title())# Converte para o formato título (primeira letra maiúscula)
print(nome.capitalize())# Converte apenas a primeira letra da string para maiúsculo

texto = "  Olá mundo!    "

print(texto + ".")# Adiciona um ponto final ao texto
print(texto.strip() + ".")# Remove espaços em branco do início e do fim
print(texto.rstrip() + ".")# Remove espaços em branco do fim
print(texto.lstrip() + ".")# Remove espaços em branco do início

menu = "Python"

print("####" + menu + "####")# Adiciona caracteres antes e depois da string
print(menu.center(14))# Centraliza a string em um campo de largura 14
print(menu.center(14, "#"))# Centraliza a string em um campo de largura 14, preenchendo com '#'
print("-".join(menu))# Adiciona um hífen entre cada caractere da string
print(" ".join(menu))# Adiciona um espaço entre cada caractere da string