# O método items() 
# retorna um objeto de visualização (view object) que exibe uma lista de pares chave-valor (tuplas) do dicionário.
# Este objeto de visualização reflete as alterações feitas no dicionário.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)