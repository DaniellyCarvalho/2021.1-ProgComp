# Utilizando o FOR para iterar uma STRING
texto = 'PYTHON'

# Imprimindo caractere a caractere
for letra in texto:
   print(letra)

print('----------------------')

# Montando a string caractere a caractere
texto_saida = ''
for letra in texto:
   #texto_saida =  texto_saida + letra
   texto_saida += letra
   print(texto_saida)

print('----------------------')

# Montando a string invertida caractere a caractere
texto_saida = ''
for letra in texto:
   texto_saida = letra + texto_saida
   print(texto_saida)
