lista_estados = [ ['BA', 'Salvador'   , 2872000 , ['BA_1', 'BA_2', 'BA_3'] ],
                  ['RN', 'Natal'      , 884000  , ['Parnamirim', 'Mossoró', 'Caicó'] ],
                  ['CE', 'Fortaleza'  , 2669000 , ['CE_1', 'CE_2', 'CE_3'] ],
                  ['PE', 'Recife'     , 1645000 , ['PE_1', 'PE_2', 'PE_3'] ],
                  ['MA', 'São Luis'   , 1101000 , ['MA_1', 'MA_2', 'MA_3'] ],
                  ['AL', 'Maceió'     , 1018000 , ['AL_1', 'AL_2', 'AL_3'] ],
                  ['PI', 'Teresina'   , 864000  , ['PI_1', 'PI_2', 'PI_3'] ],
                  ['PB', 'João Pessoa', 809000  , ['PB_1', 'PB_2', 'PB_3'] ],
                  ['SE', 'Aracaju'    , 657000  , ['SE_1', 'SE_2', 'SE_3'] ] ]

# Imprimindo cada valor individual de uma sublista
# da lista LISTA_ESTADOS
i = 5
print('Eu moro na cidade', lista_estados[i][1])
print('que é capital do estado do', lista_estados[i][0])
print('e tem uma população de', lista_estados[i][2], ' habitantes')
print('Principais Cidades:', lista_estados[i][3])
print(lista_estados[i][3][0])
print(lista_estados[i][3][1])
print(lista_estados[i][3][2])