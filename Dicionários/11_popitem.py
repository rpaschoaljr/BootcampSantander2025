# O método popitem() remove e retorna um par (chave, valor) arbitrário (geralmente o último inserido na versão 3.7+ do Python) do dicionário.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError