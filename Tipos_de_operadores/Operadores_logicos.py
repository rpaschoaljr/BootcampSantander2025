# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True
print("true and true and true = ", True and True and True)
print("true and false and true = ", True and False and True)
print("false and false and false = ", False and False and False)
print("true or true or true = ", True or True or True)
print("true or false or false = ", True or False or False)
print("false or false or false = ", False or False or False) 

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)