# Solicitar o valor;
valor_saque = int(input("Valor do Saque: "))
valor_saque_saida = valor_saque

# Calcular as cédulas:
cedulas_100 = valor_saque // 100 # Qt cédulas de 100
valor_saque = valor_saque % 100
cedulas_50  = valor_saque // 50  # Qt cédulas de 50 
valor_saque = valor_saque % 50
cedulas_20  = valor_saque // 20  # Qt cédulas de 20
valor_saque = valor_saque % 20
cedulas_10  = valor_saque // 10  # Qt cédulas de 10
valor_saque = valor_saque % 10
cedulas_5   = valor_saque // 5   # Qt cédulas de 5
valor_saque = valor_saque % 5
cedulas_2   = valor_saque // 2   # Qt cédulas de 2
valor_saque = valor_saque % 2
cedulas_1   = valor_saque

# Mostrar a quantidade de cédulas
print("")
print("Valor do Saque: R$", valor_saque_saida)
print("Cédulas de R$ 100,00 .:", cedulas_100)
print("Cédulas de R$  50,00 .:", cedulas_50)
print("Cédulas de R$  20,00 .:", cedulas_20)
print("Cédulas de R$  10,00 .:", cedulas_10)
print("Cédulas de R$   5,00 .:", cedulas_5)
print("Cédulas de R$   2,00 .:", cedulas_2)
print("Cédulas de R$   1,00 .:", cedulas_1)