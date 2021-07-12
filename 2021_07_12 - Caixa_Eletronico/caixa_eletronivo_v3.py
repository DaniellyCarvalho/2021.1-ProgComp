# Solicitar o valor;
valor_saque = int(input("Valor do Saque: "))
valor_saque_saida = valor_saque

if (valor_saque > 0):
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
   print("Valor do Saque: R$ {0:.2f}".format(valor_saque_saida))

   # print("Cédulas de R$ 100,00 .:", cedulas_100)
   print("{0:>3} Cédulas de R$ 100,00: {0:>3} x R$ 100,00 = R${1:>8.2f}".format(cedulas_100, cedulas_100*100))

   #print("Cédulas de R$  50,00 .:", cedulas_50)
   print("{0:>3} Cédulas de R$  50,00: {0:>3} x R$  50,00 = R${1:>8.2f}".format(cedulas_50, cedulas_50*50))

   #print("Cédulas de R$  20,00 .:", cedulas_20)
   print("{0:>3} Cédulas de R$  20,00: {0:>3} x R$  20,00 = R${1:>8.2f}".format(cedulas_20, cedulas_20*20))

   #print("Cédulas de R$  10,00 .:", cedulas_10)
   print("{0:>3} Cédulas de R$  10,00: {0:>3} x R$  10,00 = R${1:>8.2f}".format(cedulas_10, cedulas_10*10))

   #print("Cédulas de R$   5,00 .:", cedulas_5)
   print("{0:>3} Cédulas de R$   5,00: {0:>3} x R$   5,00 = R${1:>8.2f}".format(cedulas_5, cedulas_5*5))

   #print("Cédulas de R$   2,00 .:", cedulas_2)
   print("{0:>3} Cédulas de R$   2,00: {0:>3} x R$   2,00 = R${1:>8.2f}".format(cedulas_2, cedulas_2*2))

   #print("Cédulas de R$   1,00 .:", cedulas_1)
   print("{0:>3} Cédulas de R$   1,00: {0:>3} x R$   1,00 = R${0:>8.2f}".format(cedulas_1))
else:
   print("Impossível sacar valor NEGATIVO...")