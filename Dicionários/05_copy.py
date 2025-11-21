# O método copy() cria uma cópia rasa (shallow copy) do dicionário.
# Isso significa que um novo dicionário é criado, mas os objetos aninhados (se houver)
# ainda são referências aos objetos originais.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}