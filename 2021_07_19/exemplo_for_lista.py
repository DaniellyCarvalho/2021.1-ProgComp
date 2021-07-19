lista_sigla = ['RN', 'PB', 'CE', 'PE', 'BA', 'AL', 'SE', 'MA', 'PI']

# Iterando a lista usando FOR
print('Iterando a lista usando FOR')
for sigla in lista_sigla:
   print(sigla)

print('------------------------')

# Iterando a lista usando WHILE
print('Iterando a lista usando WHILE')
posicao = 0
qt_elementos = len(lista_sigla)
while posicao < qt_elementos:
   print(lista_sigla[posicao])
   posicao += 1