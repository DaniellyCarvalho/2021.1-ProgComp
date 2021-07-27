#lista_siglas_1 = 'BA'
#lista_siglas_2 = 'RN'
#...
#lista_siglas_9 = 'SE'

# Declarando a lista já preenchida
lista_siglas = ['BA', 'RN', 'CE', 'PE', 'MA', 'AL', 'PI', 'PB', 'SE']

print('Listando o conteúdo da variável LISTA_SIGLAS')
print(lista_siglas)

print('-'*50)

print('Listando os elementos da lista sem usar laço de repetição')
#print(lista_siglas[0])
#print(lista_siglas[1])
#print(lista_siglas[2])
#print(lista_siglas[3])
#print(lista_siglas[4])
#print(lista_siglas[5])
#print(lista_siglas[6])
#print(lista_siglas[7])
#print(lista_siglas[8])

print('-'*50)

# Iterando a lista usando FOR
print('Iterando a lista usando FOR')
for posicao in range(0, 9, 1):
   print(lista_siglas[posicao])

print('-'*50)

# Iterando a lista usando WHILE
print('Iterando a lista usando WHILE')
posicao = 0
while posicao <= 8:
   print(lista_siglas[posicao])
   posicao += 1