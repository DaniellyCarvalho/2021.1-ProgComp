# Informando 2 valores inteiros do teclado
valor_x = int(input('Informe o valor de X: '))
valor_y = int(input('Informe o valor de Y: '))

'''
if valor_x > valor_y:
   print('O Valor de X é MAIOR...')
else:
   if valor_y > valor_x:
      print('O Valor de Y é MAIOR...')
   else:
      print('Os Valores de X e Y são IGUAIS')
'''

if valor_x > valor_y:
   print('O Valor de X é MAIOR...')
elif valor_y > valor_x:
   print('O Valor de Y é MAIOR...')
else:
   print('Os Valores de X e Y são IGUAIS')
