# Fazer um programa que solicite um número inteiro
# e guarde em uma lista apenas os números pares e em
# outra lista apenas os ímpares. 
# 
# O programa deverá parar quando for informado o valor 0
# 
# Ao término, o programa deverá listar os valores 
# guardados na lista

numeros_pares = []
numeros_impares = []

x = int(input('Informe um valor: '))

while x != 0:
   if (x % 2 == 0):
      numeros_pares.append(x)
   else:
      numeros_impares.append(x)   
   x = int(input('Informe um valor: '))

print(numeros_pares)
print(numeros_impares)
print('Programa Finalizado...')