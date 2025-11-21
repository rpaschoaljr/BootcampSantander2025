# O método setdefault() retorna o valor da chave se a chave estiver no dicionário.
# Se a chave não estiver no dicionário, ele insere a chave com o valor especificado
# (ou None, se nenhum valor for especificado) e retorna esse valor.

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}