lista_siglas = ['BA', 'RN', 'CE', 'PE', 'MA', 'AL', 'PI', 'PB', 'SE']

lista_estados = [ ['BA', 'Salvador'   , 2872000],
                  ['RN', 'Natal'      , 884000],
                  ['CE', 'Fortaleza'  , 2669000],
                  ['PE', 'Recife'     , 1645000],
                  ['MA', 'São Luis'   , 1101000],
                  ['AL', 'Maceió'     , 1018000],
                  ['PI', 'Teresina'   , 864000],
                  ['PB', 'João Pessoa', 809000],
                  ['SE', 'Aracaju'    , 657000] ]

print('Listando os elementos da LISTA_SIGLAS')
for posicao in range(0, len(lista_siglas), 1):
   print(lista_siglas[posicao])

print('-'*50)

print('Listando os elementos da LISTA_ESTADOS')
for posicao in range(0, len(lista_estados), 1):
   print(lista_estados[posicao])

print('-'*50)

# Imprimindo cada valor individual de uma sublista
# da lista LISTA_ESTADOS
print('Eu moro na cidade', lista_estados[1][1])
print('que é capital do estado do', lista_estados[1][0])
print('e tem uma população de', lista_estados[1][2], ' habitantes')

print('-'*50)

# Listando o conteúdo da LISTA_ESTADOS da seguinte forma:
# A cidade nome_cidade(sigla) tem X habitantes 
for posicao in range(0, len(lista_estados), 1):
   cidade        = lista_estados[posicao][1]
   sigla         = lista_estados[posicao][0]
   qt_habitantes = lista_estados[posicao][2]
   print('A cidade ', cidade, ' (', sigla, ') tem ', qt_habitantes, ' habitantes')