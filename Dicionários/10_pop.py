# O método pop() remove o item com a chave especificada de um dicionário e retorna o valor correspondente.
# Se a chave não for encontrada e um valor padrão (default) não for fornecido, ele levanta um KeyError.
# Exemplo: my_dict.pop('chave', 'valor_padrao_se_nao_encontrado')

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)