# Fazer um programa que solicite um número inteiro
# e guarde em uma lista apenas os números pares e em
# outra lista apenas os ímpares. 
# 
# O programa deverá parar quando for informado o valor 0
#
# Ao término, o programa deverá:
#  - listar cada valor da lista dos números e calcular o seu cubo 

numeros_pares   = []
numeros_impares = []

x = int(input('Informe um valor: '))

while x != 0:
   if (x % 2 == 0):
      numeros_pares.append(x)
   else:
      numeros_impares.append(x)   
   x = int(input('Informe um valor: '))

print('-'*50)

# lista tem 10 elementos
# primeiro elemento -> lista[0]
# ultimo elemento ---> lista[9]
# x = len(lista)
# x = 10
# for i in range(0, x, 1)
#    print(lista[i])

for posicao in range(0, len(numeros_pares), 1):
   print(numeros_pares[posicao], ' -> ', numeros_pares[posicao] ** 3)

print('Programa Finalizado...')