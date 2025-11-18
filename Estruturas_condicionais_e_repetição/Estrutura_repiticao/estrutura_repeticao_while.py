# Repetição com while e uso do else em Python
# A estrutura de repetição while executa um bloco de código enquanto uma condição for verdadeira

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n-> "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao > 2:
        print("erro: opção inválida, tente novamente.")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")